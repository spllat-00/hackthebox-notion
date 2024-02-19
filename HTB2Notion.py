#!/usr/bin/env python3

# Author: spllat-00
# Description: This script will take Hack The Box machines and store them in Notion Database

import requests
from dotenv import load_dotenv
import os
from helpers import writeup_template, serializeData
from time import sleep
import argparse
import logging
from math import ceil
from time import time

class HTB2Notion:
    def __init__(self) -> None:
        # Token
        self.htbToken: str = os.getenv("HTBTOKEN")
        self.notionToken: str = os.getenv("NOTIONTOKEN")
        
        # Notion Database ID
        self.notionDatabaseID: str = os.getenv("NOTIONDATABASEID")
        
        # Lists
        self.htbActiveList: list[dict] = []
        self.htbRetiredList: list[dict] = []
        
        # Set
        self.preExistingMachines: set[str] = None
        
        # Notion URL
        self.notionBaseURL: str = "https://api.notion.com/"
        
        # HackTheBox URL
        self.activeURL: str = "https://www.hackthebox.com/api/v4/machine/paginated?per_page=25&page=1"
        self.retiredURL: str = "https://www.hackthebox.com/api/v4/machine/list/retired/paginated?per_page=25&page="

        # Headers
        self.htbHeaders: dict[str:str] = {
            "Authorization": f"Bearer {self.htbToken}",
            "user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0",
        }
        self.notionHeader: dict[str: str] = {
            "Authorization" : f"Bearer {self.notionToken}",
            "Notion-Version" : "2022-06-28",
            "Content-Type": "application/json"
        }
        
        self.checkEnivronmentVariables()
    
    def checkEnivronmentVariables(self) -> None:
        issues = {}
        if not self.htbToken:
            issues["htbToken"] = {
                "error": "HTB Token not Found",
                "fix": "Add \"htbToken\" in .env file"
            }
        if not self.notionToken:
            issues["notionToken"] = {
                "error": "Notion Token not Found",
                "fix": "Add \"notionToken\" in .env file"
            }
        if not self.notionDatabaseID:
            issues["notionDatabaseID"] = {
                "error": "Notion Database ID not Found",
                "fix": "Add \"notionDatabaseID\" in .env file"
            }
        
        if len(issues) > 0:
            logger.critical("Error while running script!!")
            for index, (value) in enumerate(issues.values()):
                logger.critical(f"Fix #{index+1:02}: {value['fix']}")
            exit()

    def MyDecorator(func):
        def inner(self):
            func(self)
            logger.info("-"*10)
        return inner
    
    @MyDecorator
    def fetchActiveHTBMachines(self) -> None:
        """Fetches list of active machines from HTB server.
        """
        # Active Machine Requests
        logger.info(f"Getting List of Active Machines")
        try:
            activeMachineResponse = requests.get(url=self.activeURL, headers=self.htbHeaders).json()
        except requests.exceptions.JSONDecodeError: # Sometimes HTB request fails, then retry a few times.
            tries = 0
            while tries < 3:
                logger.warning(f"Failed to get response from HTB for Active Machines.")
                logger.warning(f"\tRetrying {tries+1}...")
                activeMachineResponse = requests.get(url=self.activeURL, headers=self.htbHeaders)
                if 200 <= activeMachineResponse.status_code < 300:
                    activeMachineResponse = activeMachineResponse.json()
                    break
                else:
                    tries += 1
        
        for box in activeMachineResponse["data"]:
            self.htbActiveList.append({
                "id": box["id"],
                "avatar": box["avatar"],
                "name": box["name"],
                "os": box["os"],
                "star": box["star"],
                "release": box["release"],
                "difficultyText": box["difficultyText"],
                "authUserInUserOwns": box["authUserInUserOwns"], # User Flag
                "authUserInRootOwns": box["authUserInRootOwns"], # Root Flag
                "isTodo": bool(box["isTodo"]),
                "isActive": True,
            })
        logger.info(f"Found {len(self.htbActiveList)} Active Machines")
    
    @MyDecorator
    def fetchRetiredHTBMachines(self) -> None:
        """Fetches list of retired machines from HTB server.
        """
        logger.info(f"Getting List of Retired Machines")
        retiredMachineListResponses=[]
        pageNum = 1
        while True:
            try:
                logger.debug(f"Fetching machines from page number: {pageNum}")
                retiredMachineResponse = requests.get(url=f"{self.retiredURL}{pageNum}", headers=self.htbHeaders).json()
            except requests.exceptions.JSONDecodeError: # Sometimes HTB request fails, then retry a few times.
                tries = 0
                while tries < 3:
                    logger.warning(f"Failed to get response from HTB for Retired Machines.")
                    logger.warning(f"\tFailed @ page number: {pageNum}")
                    logger.warning(f"\tRetrying {tries+1}...")
                    retiredMachineResponse = requests.get(url=f"{self.retiredURL}{pageNum}", headers=self.htbHeaders)
                    if 200 <= retiredMachineResponse.status_code < 300:
                        retiredMachineResponse = retiredMachineResponse.json()
                        break
                    else:
                        tries += 1
                
            retiredMachineListResponses += retiredMachineResponse["data"]

            if retiredMachineResponse["links"]["next"] == None:
                break
            
            pageNum += 1
            sleep(0.5)

        for box in retiredMachineListResponses:
            self.htbRetiredList.append({
                "id": box["id"],
                "avatar": box["avatar"],
                "name": box["name"],
                "os": box["os"],
                "star": box["star"],
                "release": box["release"],
                "difficultyText": box["difficultyText"],
                "authUserInUserOwns": box["authUserInUserOwns"], # User Flag
                "authUserInRootOwns": box["authUserInRootOwns"], # Root Flag
                "isTodo": bool(box["isTodo"]),
                "isActive": False,
            })

        logger.info(f"Found {len(self.htbRetiredList)} Retired Machines")
    
    @MyDecorator
    def fetchExistingNotionMachines(self) -> None:
        """Fetches list of machines from Notion.
        """
        logger.info(f"Fetching list of existing machines from Notion...")
        url=f"{self.notionBaseURL}v1/databases/{self.notionDatabaseID}/query"
        response=requests.post(
            url=url,
            headers=self.notionHeader,
        )
        totalMachinesList = response.json()["results"]
        while response.json()["next_cursor"]:
            response=requests.post(
                url=url,
                headers=self.notionHeader,
                json={
                    "start_cursor": response.json()["next_cursor"]
                }
            )
            sleep(0.5)
            totalMachinesList += response.json()["results"]
        self.preExistingMachines = serializeData(totalMachinesList)
        logger.info(f"Fetched {len(self.preExistingMachines)} machine{'s' if len(self.preExistingMachines)>1 else ''} from Notion.")
        
    def checkIfMachineExists(self, machineName:str, machineID: int) -> bool:
        """Function to check if supplied machine name and ID exists in list of notion notes

        Args:
            machineName (str): Name of the Machine as per HTB
            machineID (int): ID of the Machine as per HTB

        Returns:
            bool: Boolean value depending on the existance of machine
        """        
        if f"{machineName}--{machineID}" in self.preExistingMachines:
            return True # Machine Exists
        else:
            return False # Machine Doesn't Exist

    @MyDecorator
    def addToNotionPage(self) -> None:
        """Add the list of HTB machines to Notion Database
        """        
        machinesList = self.htbActiveList + self.htbRetiredList
        added_machines = 0
        
        pagesURL=f"{self.notionBaseURL}v1/pages"

        notionBlocks = [
            block 
            for block in writeup_template
        ]

        logger.info(f"Found {len(machinesList)} machines.")
        logger.warning(f"This may take approximately {int(ceil(len(machinesList)*1.5))//60} mins: {int(ceil(len(machinesList)*1.5))%60} secs.")
        logger.info(f"-"*5)
        for index, element in enumerate(machinesList):
            if not self.checkIfMachineExists(element["name"], element["id"]):
                logger.info(f"{index+1:04}:\tAdding: {element['name']:<20}: {element['id']:<4}\t\t<<<")
                jsonData = {
                    "parent": {"database_id": f"{self.notionDatabaseID}"},
                    "icon": {
                        "type": "external",
                        "external": {
                            "url": f"https://www.hackthebox.com/{element['avatar']}"
                        }
                    },
                    "cover":{
                        "type": "external",
                        "external": {
                            "url": f"https://www.hackthebox.com/{element['avatar']}"
                        }
                    },
                    "properties":{
                        "Name": {
                            "title": [
                                {
                                    "text": {
                                        "content": element["name"]
                                    }
                                }
                            ]
                        },
                        "Difficulty": {
                            "select": {
                                "name": element["difficultyText"]
                            }
                        },
                        "ID": {
                            "number": element["id"]
                        },
                        "OS": {
                            "select": {
                                "name": element["os"]
                            }
                        },
                        "Rating": {
                            "number": element["star"]
                        },
                        "Release Date": {
                            "date": {
                                "start": element["release"]
                            }
                        },
                        "Root Flag": {
                            "checkbox": element["authUserInRootOwns"]
                        },
                        "Todo": {
                            "checkbox": element["isTodo"]
                        },
                        "User Flag": {
                            "checkbox": element["authUserInUserOwns"]
                        },
                        "isActive": {
                            "checkbox": element["isActive"]
                        },
                    },
                    "children": notionBlocks
                }

                response = requests.post(
                    url=pagesURL,
                    headers=self.notionHeader,
                    json=jsonData
                )
                if 200 <= response.status_code < 300:
                    logger.debug(f"Added {element['name']} to Notion")
                    added_machines += 1
                else:
                    logger.error(f"Something failed while adding {element['name']} to Notion")
                    logger.error(response.text)
                sleep(0.5)
            else:
                logger.info(f"{index:04}:\tAlready Present: {element['name']}: {element['id']}")
            logger.info(f"-"*subTopicSeprator)
        logger.info(f"Added {added_machines} Machine{'s' if added_machines>1 else ''} to Notion") 
    
    @MyDecorator
    def notionActiveToRetired(self) -> None:
        """Change the status of Active machines to Retired as per HTB
        """        
        logger.info(f"Getting list of active machines from Notion...")
        url=f"{self.notionBaseURL}v1/databases/{self.notionDatabaseID}/query"
        jsonDictionary={
            "filter":{
                "property": "isActive",
                "checkbox": {
                    "equals": True
                }
            }
        }
        response=requests.post(
            url=url,
            headers=self.notionHeader,
            json=jsonDictionary
        )
        responseList = response.json()["results"]
        notionActiveList = {}
        while response.json().get("has_more"):
            logger.debug(f"Getting more active machines from Notion...")

            jsonDictionary["start_cursor"]=response.json()["next_cursor"]
            response=requests.post(
                url=url,
                headers=self.notionHeader,
                json=jsonDictionary
            )
            responseList += response.json()["results"]
        for item in responseList:
            notionActiveList[item["properties"]["Name"]["title"][0]["text"]["content"]]= {
                "notionID": item["id"],
                "id": item["properties"]["ID"]["number"],
            }
        
        # HTB Part
        logger.info(f"Getting list of active machines from Hack The Box...")
        activeMachineResponse = requests.get(url=self.activeURL, headers=self.htbHeaders).json()
        activeMachinesDict: dict[str:str] = {}
        for box in activeMachineResponse["data"]:
            activeMachinesDict[box["name"]]={"id": box["id"]}
        
        logger.info(f"Checking Notion Datbase and Updating Active to Retired")
        machinesUpdated=0
        for key, value in notionActiveList.items():
            if not (key in activeMachinesDict and value["id"] == activeMachinesDict[key]["id"]) :
                url = f"{self.notionBaseURL}v1/pages/{value['notionID']}"
                jsonDict = {
                    "properties": {
                        "isActive": {
                            "checkbox": False
                        }
                    }
                }
                response=requests.patch(
                    url=url,
                    headers=self.notionHeader,
                    json=jsonDict
                )
                machinesUpdated += 1
                if 200 <= response.status_code < 300:
                    logger.warning(f"RETIRED: {key:<20}: {value['id']:<20}\t\t<<<")
                    logger.debug(f"-"*subTopicSeprator)
                else:
                    logger.error(f"Failed to update {key} to Retired list")
                sleep(0.5)
            else:
                logger.debug(f"Checked: {key:<20}: {value['id']:<4}")
        if machinesUpdated != 0:
            logger.info(f"{machinesUpdated} machines were updated!!!")
        else:
            logger.info(f"Notion already up to date.")

    def checkAndValidateDatabase(self) -> None:
        response=requests.get(url=f"https://api.notion.com/v1/databases/{self.notionDatabaseID}", headers=self.notionHeader)
        
        if not (200 <= response.status_code < 300):
            logger.error("Error while checking Database")
            logger.error(f"{response.json()['message']}")
        
        notionDatabaseProperties = response.json()["properties"]
        requiredProperties = {
            "Difficulty": "select",
            "ID": "number",
            "Name": "title",
            "OS": "select",
            "Rating": "number",
            "Release Date": "date",
            "Root Flag": "checkbox",
            "Todo": "checkbox",
            "User Flag": "checkbox",
            "isActive": "checkbox",
        }
        
        missingOrWrong = {}
        for key, value in requiredProperties.items():
            if key not in notionDatabaseProperties:
                missingOrWrong[f"{key}"]={
                    "error": "Missing", 
                    "fix": f"Create a property name of \"{key}\" with type \"{value}\"",
                }
            elif value != notionDatabaseProperties[key]["type"]:
                missingOrWrong[f"{key}"]={
                    "error": "Wrong Property",
                    "fix": f"Change the property type of \"{key}\" to \"{value}\""
                    }
        if len(missingOrWrong)>0:
            for index, (value) in enumerate(missingOrWrong.values()):
                logger.critical(f"Fix #{index+1:02}: {value['fix']}")
            return False # Something is wrong in DB
        return True # Correct Database

if __name__ == "__main__":
    startTime = time()
    
    # Initialize logging
    logging.basicConfig(format='%(levelname)-10s %(message)s', level=logging.INFO)
    
    # Create a logger object
    logger = logging.getLogger(__name__)
    
    # Load .env variables
    load_dotenv(".env")
    
    # Arguments
    parser = argparse.ArgumentParser(
        description="HTB2Notion: Takes HTB machines and make templates in Notion"
    )
    parser.add_argument( # --debug
        "--debug", 
        action="store_true", 
        help="Enables debug logging"
    )
    parser.add_argument( # --active / -a
        "--active",
        "-a",
        action="store_true", 
        help="Will check for only active machines"
    )
    parser.add_argument( # --retired / -r
        "--retired",
        "-r", 
        action="store_true", 
        help="Update Active Machines to Retire"
    )
    
    args = parser.parse_args()
    
    # Misc Variables
    subTopicSeprator = 10
    
    # Debugger
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    h2nObj = HTB2Notion()
    if h2nObj.checkAndValidateDatabase():
        if args.retired:
            h2nObj.notionActiveToRetired()
        else:
            h2nObj.fetchActiveHTBMachines()
            if not args.active:
                h2nObj.fetchRetiredHTBMachines()
            h2nObj.fetchExistingNotionMachines()
            h2nObj.addToNotionPage()
	
    endTime = time()
    
    print(f"Code ran successfully in {int(endTime-startTime)//60} mins {int(endTime-startTime)%60} secs")