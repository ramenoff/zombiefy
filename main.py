from youtube_side import *
from format import *
import secrets

def returnVideo():

    pl_items = returnPlaylist('PLqzSfsmcCgJlqHShyMeimQNsPLEveckEK')

    yt_list = []

    for eachItem in pl_items:
        yt_list.append(eachItem['contentDetails']['videoId'])

    return formatVideo(secrets.choice(yt_list))