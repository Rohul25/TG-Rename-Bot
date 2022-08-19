1. Required Fields

BOT_TOKEN: 
GDRIVE_FOLDER_ID: 
OWNER_ID: 
DOWNLOAD_DIR: 
DOWNLOAD_STATUS_UPDATE_INTERVAL:
AUTO_DELETE_MESSAGE_DURATION: 
IS_TEAM_DRIVE: 
TELEGRAM_API: 
TELEGRAM_HASH: 

DATABASE_URL: 
AUTHORIZED_CHATS: 
SUDO_USERS: 
IGNORE_PENDING_REQUESTS: 
USE_SERVICE_ACCOUNTS: Whether to use Service Accounts or not. For this to work see Using Service Accounts section below. Default is False. Bool
INDEX_URL: 
STATUS_LIMIT: 
STOP_DUPLICATE: 
CMD_INDEX: commands index number. This number will added at the end all commands.
UPTOBOX_TOKEN: Uptobox token to mirror uptobox links. Get it from Uptobox Premium Account.
TORRENT_TIMEOUT: Timeout of dead torrents downloading with qBittorrent and Aria2c in seconds.
EXTENTION_FILTER: File extentions that won't upload/clone. Separate them by space.
INCOMPLETE_TASK_NOTIFIER: Get incomplete task messages after restart. Require database and (supergroup or channel). Default is False. Bool
Update
UPSTREAM_REPO: Your github repository link, if your repo is private add https://username:{githubtoken}@github.com/{username}/{reponame} format. Get token from Github settings. So you can update your bot from filled repository on each restart. NOTE: Any change in docker or requirements you need to deploy/build again with updated repo to take effect. DON'T delete .gitignore file. For more information read THIS.
UPSTREAM_BRANCH: Upstream branch for update. Default is master.
Auto Mute
AUTO_MUTE: Set it True if you want to use Auto Mute. (False by default)
CHAT_ID: Id of the group where you want to use AUTO_MUTE. (Mandatory if AUTO_MUTE is True)
Force SUB
FSUB: Force BOT users to subscribe a specific channel in order to use the bot. Set it True if you want to use FSUB. Default is False.
CHANNEL_USERNAME: Add the channel username for force sub. (Example: If the channel link is https://t.me/z_mirror then write z_mirror)
FSUB_CHANNEL_ID: Add channel id for FSUB. (Ex: -1001232292892). ( Note Don't add "" )
