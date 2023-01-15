import os
import time

from sys import argv

from lxml import html
import requests
from winotify import Notification, audio


def get_live_id(channel_id):
    if channel_id.startswith('@'):
        url = f'https://youtube.com/{channel_id}/live'
    else:
        url = f'https://youtube.com/channel/{channel_id}/live'
    page = requests.get(url)
    tree = html.fromstring(page.content)
    canonical_url = tree.xpath('//link[@rel="canonical"]/@href')[0]
    if "/channel/" not in canonical_url:
        print(f"found live url ({canonical_url}) for channel {channel_id}")
        return str(canonical_url)
    return None


def os_notify(video_url, channel_id):
    yt_icon = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'youtube.png')
    try:
        toast = Notification(app_id="ytchat-notify",
                             title=f"Live video found for channel {channel_id}",
                             msg=video_url,
                             icon=yt_icon)
        toast.add_actions(label="Open Video",
                          launch=video_url)
        toast.set_audio(audio.IM, loop=False)
        toast.show()
    except:
        print(f'could not show notification for video: {video_url}')


if __name__ == '__main__':
    chan_id = "UCrPseYLGpNygVi34QpGNqpA" if len(argv) == 1 else argv[1]
    chan_id = os.environ['YTCHAT_CHANNELID'] if 'YTCHAT_CHANNELID' in os.environ else chan_id
    vid_id = None
    while True:
        new_video_id = get_live_id(chan_id)
        if new_video_id is not None and vid_id != new_video_id:
            print("found new video_id, notifying")
            vid_id = new_video_id
            os_notify(vid_id, chan_id)
        time.sleep(90)
