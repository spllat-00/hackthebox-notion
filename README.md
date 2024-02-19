# hackthebox-notion
 
This script allows you to pull data from HackTheBox and store it in Notion with a pre-made template.

## Requirements
- [Python 3.x](https://www.python.org/downloads/)
- [Notion API Credentials](https://www.notion.so/my-integrations)
- [Hack The Box APp Token](https://app.hackthebox.com/profile/settings)

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
    - Add to your required workspace
    - Give the integration a name: `HackTheBox-Notion` (Can be anything as per user)
    - Add logo for easy access. (Logo provided in git repo)
    - Hit Submit
    - View your Secret, by click `show`
    - This is: `NOTIONTOKEN` in .env file

4. Setup your Hack The Box App Token
    - Visit [Hack The Box Settings](https://app.hackthebox.com/profile/settings)
    - Click `Generate Identifier`
    - Give it a name: `HackTheBox2Notion` (Can be anything as per user)
    - Set the expire time: `1 Year`
    - Copy the App Token
    - This is: `HTBTOKEN` in .env file

5. Copy the template Hack The Box - Notion Template
    - Open the [Hack The Box - Notion Template](https://maroon-bobcat-3c4.notion.site/Hack-The-Box-Notion-Template-7ecd6321ffda4a3dad998ccbd36c6b9d?pvs=4)
    - Click `Duplicate` button on top-right
    - Select the same workspace you created the Notion Integration.

6. Connect the newly created notion integration to the workspace
    - Select `options` in top-right.
    - In `Connections > Connect to`, select: `HackTheBox-Notion`
    - Hit Confirm

7. Find the Database ID
    - On the top-right, hit `Share`
    - It will be in this format: https://www.notion.so/Hack-The-Box-Notion-Template-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    - We need the `xxxxx` part, that should be of 32 characters
    - This is: `NOTIONDATABASEID`
6. Update the `.env` file with `NOTIONTOKEN`, `HTBTOKEN` and `NOTIONDATABASEID`

## Usage
Run the script
```bash
python3 HTB2Notion.py
```

> For checking the help, use flag: -h / --help

## Configuration
- HTBTOKEN = HTB_JWT_Token
- NOTIONTOKEN = Notion_Token
- NOTIONDATABASEID = 32-bit-ID

## Contributing
Contributions are welcome! Feel free to open issues or pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
