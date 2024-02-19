# hackthebox-notion
 
This script allows you to pull data from HackTheBox and store it in Notion with a pre-made template.

## Requirements
- [Python 3.x](https://www.python.org/downloads/)
- [Notion API Credentials](https://www.notion.so/my-integrations)
- [Hack The Box App Token](https://app.hackthebox.com/profile/settings)

## Installation
1. Clone this repository:
```bash
git clone https://github.com/spllat-00/hackthebox-notion.git
  ```
2. Install the required Python packages
```bash
pip install -r requirements.txt
```
3. Setup your Notion integration and get your API credentials.
    - Visit [Notion integration](https://www.notion.so/my-integrations)
  
      ![NotionIntegration-Step1](https://github.com/spllat-00/hackthebox-notion/assets/50944153/091f76d6-4033-4856-a85d-13e293595ad0)

    - Add to your required workspace
    
    - Give the integration a name: `HackTheBox-Notion` (Can be anything as per user)
    - Add logo for easy access. (Logo provided in git repo)
    - Hit Submit
  
      ![NotionIntegration-Step2](https://github.com/spllat-00/hackthebox-notion/assets/50944153/83b86505-b5a0-4fd7-9cd7-f5fcbdf7195e)
    
    - View your Secret, by click `show`
  
      ![NotionIntegration-Step3](https://github.com/spllat-00/hackthebox-notion/assets/50944153/68ba1fd2-cb37-4c28-a9b8-43976151716f)
    
    - This is: `NOTIONTOKEN` in .env file

4. Setup your Hack The Box App Token
    - Visit [Hack The Box Settings](https://app.hackthebox.com/profile/settings)
    - Click `Generate Identifier`
  
      ![HackTheBox-Step1](https://github.com/spllat-00/hackthebox-notion/assets/50944153/421705fd-f7a9-48b7-9ac8-8037651ddc09)
    
    - Give it a name: `HackTheBox2Notion` (Can be anything as per user)
    - Set the expire time: `1 Year`
  
      ![HackTheBox-Step2](https://github.com/spllat-00/hackthebox-notion/assets/50944153/085015c5-fe82-41ea-8133-21bf7c4e51ff)
    
    - Copy the App Token
  
      ![HackTheBox-Step3](https://github.com/spllat-00/hackthebox-notion/assets/50944153/302da8e1-4334-4e28-9e72-c0d18c9d815d)
    
    - This is: `HTBTOKEN` in .env file

5. Copy the template Hack The Box - Notion Template
    - Open the [Hack The Box - Notion Template](https://maroon-bobcat-3c4.notion.site/Hack-The-Box-Notion-Template-7ecd6321ffda4a3dad998ccbd36c6b9d?pvs=4)
    - Click `Duplicate` button on top-right
  
      ![NotionTemplate-Step1](https://github.com/spllat-00/hackthebox-notion/assets/50944153/12741221-ae22-489c-8cdc-b2f1887efdce)

    - Select the same workspace you created the Notion Integration.
  
      ![NotionTemplate-Step2](https://github.com/spllat-00/hackthebox-notion/assets/50944153/6b84d616-20ee-4009-969e-12201072cfc0)


7. Connect the newly created notion integration to the workspace
    - Select `options` in top-right.
    - In `Connections > Connect to`, select: `HackTheBox-Notion`
  
      ![NotionConnections-Step1](https://github.com/spllat-00/hackthebox-notion/assets/50944153/950a1c7c-63fb-4a7e-b3b4-550dffcc7348)

    - Hit Confirm
  
      ![NotionConnections-Step2](https://github.com/spllat-00/hackthebox-notion/assets/50944153/9530fa1f-6928-4613-9d67-8e4f05dcb64a)


8. Find the Database ID
    - On the database of gallery, hit 6-dots
  
     ![NotionDatabaseID-Step1](https://github.com/spllat-00/hackthebox-notion/assets/50944153/8e202a35-0134-4a46-a761-1577f2880f17)

    - Select `Copy link`
  
     ![NotionDatabaseID-Step2](https://github.com/spllat-00/hackthebox-notion/assets/50944153/53156dae-d043-430b-9c0c-52464adcebed)

    - It will be in this format: https://www.notion.so/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx?v=someOtherFormathere&pvs=4
    - We need the `xxxxx` part, that should be of 32 characters
    - This is: `NOTIONDATABASEID`
9. Create a file with name `.env` file with `NOTIONTOKEN`, `HTBTOKEN` and `NOTIONDATABASEID` values from above

## Usage
Run the script
```bash
python3 HTB2Notion.py
```

> For checking the help, use flag: -h / --help

## Screenshots
1. Running of the script for new machines

![RunningScript](https://github.com/spllat-00/hackthebox-notion/assets/50944153/d41293b6-d0e0-4e99-859b-4b094719ab9a)


2. Template

![NotionMachineTemplate-Step1](https://github.com/spllat-00/hackthebox-notion/assets/50944153/fedd862c-c0a9-4fd3-868b-29f102c0157a)

![NotionMachineTemplate-Step2](https://github.com/spllat-00/hackthebox-notion/assets/50944153/062029b0-c4e7-4d74-a616-2588c008d0ae)

![NotionMachineTemplate-Step3](https://github.com/spllat-00/hackthebox-notion/assets/50944153/026b5110-29b2-4029-bee1-fea274f241d8)


## Configuration
- HTBTOKEN=HTB_JWT_Token
- NOTIONTOKEN=Notion_Token
- NOTIONDATABASEID=32-bit-ID

## Contributing
Contributions are welcome! Feel free to open issues or pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
