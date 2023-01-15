# ytchat-notify

## Installation
```shell
git clone https://github.com/spedrickson/ytchat-notify
cd ytchat-notify
pip install -r requirements.txt
```

## Usage
```shell
# script takes 1 argument, the channel to check for live broadcast
# can be either a handle (@Ludwig) or a channelID (UCrPseYLGpNygVi34QpGNqpA)
# can also set the environment variable YTCHAT_CHANNELID, which will override script launch arguments 
python main.py "@Ludwig"
# or
python main.py UCrPseYLGpNygVi34QpGNqpA
```

## What It Does
Loops endlessly checking the specified channel every 90 seconds for a live broadcast (scheduled or active)  
Every time a new video is found, generate a Windows toast notification with a clickable link:  

![Notification Example](/resources/notification.png?raw=true "Notification Example")
