# [Join TorLeechGram Group for DEMO](https://t.me/PriiiyoLeech)
# TorLeechGram Telegram
So basically TorLeechGram is aimed to be the most versatile torrent leecher and Youtube-DL bot for telegram. This bot is highly customizable and to customize this bot you don't need to restart the bot every time. 
The bot gets started with minimum variables and others can be set as and when needed using the /settings.

Table of Content
- [FEATURES](#features)
- [TEST THE BOT (DEMO)](https://t.me/PriiiyoLeech)
- [DEPLOYMENT METHODS](#deployment)
  - [Heroku](##heroku)
  - [Zeet](##zeet)
  - [VPS DEPLOYMENT USING DOCKER](#vps-deployment-docker)
  - [VPS DEPLOYMENT WITHOUT DOCKER](#vps-deployment-without-docker)


# Features
Following are some awesome features offered by this bot:-
- Using the best torrent client to deal with torrent : [qBittorrent](https://github.com/qbittorrent/qBittorrent)
- You can choose which files you want to download from the torrent.
- A glorious settings menu from you can control the bot.
- If the bot is in the group, the users have their own settings like:
  - Permanent thumbnail support.
  - Users can choose if they want a file or video.
  - Load in their own rclone config so that the torrent/direct link is uploaded to their drive. (Work in Progress)
- Extraction of ZIP, TAR, ISO, RAR wih and without password. If you chose to extarct the archive and you enter the password wrong it will prompt you to enter the password upto 3 times after that zip will be uploaded as it is.
- G Drive Index support.
- Admins can put hard limits on the max torrent size and max youtube playlist size.
- Aria2 for direct links download.
- Upload to gdrive by using RCLONE.
  - You can load multiple drives in the conf and can switch on fly using the settings.
- Sorted YTDL download menu.
- Zip and upload also available.
- Get the server status.
- InstaDL support
- Browse the settings menu and try stuff. ;)

### ***Compulsory Vars***

- `API_HASH`
  - Values :- Valid API HASH obtained from Telegram.
  - Default Value :- `""`
  - Use :- To connect to Telegram.

- `API_ID`
  - Values :- Valid API ID obtained from Telegram.
  - Default Value :- `0`
  - Use :- To connect to Telegram.

- `BOT_TOKEN`
  - Values :- Valid BOT TOKEN Obtained from Botfather.
  - Default Value :- `""`
  - Use :- To connect to Telegram as BOT.

- `BASE_URL_OF_BOT`
  - Values :- Valid BASE URL of where the bot is deploy. Ip/domain of your bot like "http://myip" or if oy have chosen other port then 80 then "http://myip:port". No slash at the end.
  - Default Value :- `""`
  - Use :- This is used for file selection of the torrent.

- `ALD_USR`
  - Values :- It is a list of IDs of all the allowed groups and useres who can use this bot in private. 
    - To supply multiple IDs in ExecVarsSample.py seperate by comma ','. 
    - To supply multiple IDs from Environemnt variable seperate by spaces.
  - Default Value :- `[]` 
  - Use :- Users and groups with ids here can use the bot.

- `DB_URI` = 
  - Values :- Postgres database URL. Just replace your credentials from below. OR directly Paste the URI you obtained from a database hosting or somewhere else.
  - Default Value :- `dbname=tortk user=postgres password=your-pass host=127.0.0.1 port=5432`
  - Use :- Used to connect to DB. DB is used for many stuff in this bot. 

- `OWNER_ID` = 
  - Values :- Owner's ID
  - Default Value :- `0`
  - Use :- Used to restrict use of certain stuff to owner only. 
### ***Optional Vars***
- `GD_INDEX_URL`
  - Values :- Base URL of the index that you are using. (Now that you should include the directory also in URL if you have set `RCLONE_BASE_DIR`). (Dosen't matter if a slash is at the end or not)
  - Default Value :- `False`
  - Use :- Provides an addition Index link for Google Drive Upload.

- `EDIT_SLEEP_SECS`
  - Values :- Seconds to Sleep before edits. Recommended is 40. (If you are using the bot for your own you can try 10 if you get FloodWait Error in LOGS then increase the value) [Can be set from settings menu]
  - Default Value :- `40`
  - Use :- The bot will update the progress regulary after these number of seconds.

- `TG_UP_LIMIT`
  - Values :- Telegram Upload limit in bytes. (you can set max `2147483648` which is ~2GB) [Can be set from settings menu]
  - Default Value :- `1700000000`
  - Use :- The bot will use this value to automatically slice the file bigger that this size into small parts to upload to Telegram.

- `FORCE_DOCUMENTS`
  - Values :- `True`/`False` [Can be set from settings menu]
  - Default Value :- `False`
  - Use :- Should all the upload to telegram be forced as documents or not.

- `COMPLETED_STR`
  - Values :- Any character [Only 1 character] [Can be set from settings menu]
  - Default Value :- `▰`
  - Use :- Character used to denote completed progress in the progress bar. 


- `REMAINING_STR`
  - Values :- Any character [Only 1 character] [Can be set from settings menu]
  - Default Value :- `▱`
  - Use :- Character used to denote remaining progress in the progress bar. 

- `RCLONE_BASE_DIR`
  - Values :- Rclone Base Directory to where stuff should be clonned inside your drive. [Cannot be configured from settings]
  - Default Value :- `"/"`
  - Use :- The bot will upload all the files to that folder in the drive.

- `LEECH_ENABLED`
  - Values :- `True`/`False` [Can be set from settings under control action]
  - Default Value :- `True`
  - Use :- Upload to telegram should be enabled or not.

- `RCLONE_ENABLED`
  - Values :- `True`/`False` [Can be set from settings under control action]
  - Default Value :- `False`
  - Use :- Upload to rclone should be enabled or not.


- `DEFAULT_TIMEOUT`
  - Values :- `"leech"`/`"rclone"`
  - Default Value :- `"leech"`
  - Use :- Default destination (rclone or leech) to choose if the user fails to choose upload destination in 60 seconds.

- `RCLONE_CONFIG`
  - Values :- Path to the RCLONE.conf file [IT IS RECOMMENDED TO SET THIS FROM SETTINGS MENU]
  - Default Value :- `False`
  - Use :- Rclone file path.

- `DEF_RCLONE_DRIVE`
  - Values :- Default Rclone drive from the config file. This is the heading of a config from the file. [IT IS RECOMMENDED TO SET THIS FROM SETTINGS MENU]
  - Default Value :- `""`
  - Use :- Name of the config in the conf file to refer to.

- `MAX_YTPLAYLIST_SIZE`
  - Values :- Max size of a playlist that is allowed (Number of videos) [Can be set from settings menu]
  - Default Value :- `20` 
  - Use :- Stops the user from downloading big playlists.

- `MAX_TORRENT_SIZE`
  - Values :- Max torrent size in GBs that is allowed. [Can be set from settings menu]
  - Default Value :- `10`
  - Use :- Stops the user from downloading big torrents.

- `USER_CAP_ENABLE` : Work in progress
- `USER_CAP_LIMIT` : Work in progress

## **Rest Variables are not to be changed** 


# Deploying:

## Prerequisites

- Install Python3.
```
sudo apt install python3
```

## Setup

- Install Requirements:
```
pip3 install -r requirements.txt
```

- Build Docker:
```
sudo docker build . -t torleechgram
```

- Run Docker:
```
sudo docker run torleechgram
```


## Commands

    leech - To Leech a torrent or download a direct link
    ytdl - Donwload YouTube Video
    pytdl - Download YouTube Playlist
    about - About the bot
    status - Status of all the downloads
    server - Get server status
    usettings - User Settings (private also)
    instadl - Instagram Post/Reel/IGTV download
    setthumb - Set the thumbnail
    clearthumb - Clear the thumbnail
    settings - Settings of the bot ⚠️ Admin Only
    pauseall - Pause all torrents⚠️ Admin Only
    resumeall - Resume all torrents⚠️ Admin Only
    purge - Delete all torrents ⚠️ Admin Only
    getlogs - Get the robot logs ⚠️ Admin Only

# Credits
[Priiiyo(me)](https://github.com/priiiyo/TorLeechGram) 😊

[yash-dk](https://github.com/yash-dk/TorToolkit-Telegram) for orginal repo 👍

[Lonami](https://github.com/LonamiWebs/Telethon/) for awesome Telethon

[All the Libraries owner](https://github.com/yash-dk/TorToolkit-Telegram/blob/master/requirements.txt)
