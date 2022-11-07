import isodate
from googleapiclient.discovery import build
import os
from dotenv import load_dotenv
import sys

load_dotenv()

key = os.getenv("API_KEY")

youtube = build('youtube', 'v3', developerKey=key)


# request = youtube.channels().list(
#     part="contentDetails,contentOwnerDetails,id,statistics",
#     forUsername = YT_channel
# )


# response = request.execute()

channel_ID = "UCCezIgC97PvUuR4_gbFUs5g"

try:
    channel_ID = sys.argv[1]
except IndexError as e:
    print("Using Default channel_ID")

print(channel_ID)

# print(json.dumps(response,indent=4))
# print('Channel ID: ',channel_ID)

max_video_playlist_ID = None
nextPageToken = None
videosCount = 0

PlayList_IDs = []

pandasPlaylist_ID = None

while True:
    request_pl = youtube.playlists().list(
        part="contentDetails,id",
        channelId=channel_ID,
        pageToken=nextPageToken,
        maxResults=20
    )
    response_pl = request_pl.execute()

    videosList = response_pl['items']

    for videos in videosList:
        vc = videos['contentDetails']['itemCount']
        if vc>videosCount:
            videosCount = vc
            max_video_playlist_ID = videos['id']
        if vc==11:
            pandasPlaylist_ID = videos['id']
        PlayList_IDs.append(videos['id'])

    nextPageToken = response_pl.get('nextPageToken')

    if not nextPageToken:
        break


# print(max_video_playlist_ID)
# print(PlayList_IDs)

# nextPageToken = None
# playlist_ID = max_video_playlist_ID

def findVideoIDs(playlist_ID):
    vds_IDs = []
    global nextPageToken
    nextPageToken = None

    while True:
        pl_request = youtube.playlistItems().list(
            part="contentDetails,id",
            playlistId=playlist_ID,
            maxResults=50,
            pageToken=nextPageToken
        )

        pl_response = pl_request.execute()

        for items in pl_response['items']:
            vds_IDs.append(items['contentDetails']['videoId'])

        nextPageToken = pl_response.get('nextPageToken')

        if not nextPageToken:
            break

    return vds_IDs



def formorethan30(TotalvideoIDs):
    done = 0

    x=0
    range = 50
    y = range

    totalseconds = 0
    videoscount = 0

    while True:
        videoids = ','.join(TotalVideoIDs[x:y])

        x = y
        y += range

        vd_request = youtube.videos().list(
            part="contentDetails,id,statistics",
            id=videoids
        )

        vd_response = vd_request.execute()

        for items in vd_response['items']:
            videoscount+=1
            duration = items['contentDetails']['duration']
            time = isodate.parse_duration(duration)
            totalseconds += time.total_seconds()

        done+=range

        if done > len(TotalvideoIDs):
            break

    return totalseconds,videoscount



# for playlist_ID in PlayList_IDs:
#     video = findVideoIDs(playlist_ID)
#     print(len(video),end=" ")


total_playlists = 0

print(f'PN\tPlaylist LINK\t\t\t\t\t\t\t\t\t\t\tDuration(HH:MM:SS)\t\tTotal Videos ')

if PlayList_IDs:
    for playlist_ID in PlayList_IDs:
        total_playlists+=1
        total_seconds = 0
        total_videos = 0

        TotalVideoIDs = findVideoIDs(playlist_ID)

        if len(TotalVideoIDs)>30:
            total_seconds,total_videos = formorethan30(TotalVideoIDs)
        else:
            nextPageToken = None

            vd_request = youtube.videos().list(
                part="contentDetails,id,statistics",
                id=','.join(TotalVideoIDs)
            )

            vd_response = vd_request.execute()

            for items in vd_response['items']:
                total_videos += 1
                duration = items['contentDetails']['duration']
                time = isodate.parse_duration(duration)
                total_seconds += time.total_seconds()

        minutes, seconds = divmod(total_seconds, 60)
        hours, minutes = divmod(minutes, 60)

        hours = int(hours)
        minutes = int(minutes)
        seconds = int(seconds)

        pl_link = f'https://www.youtube.com/playlist?list={playlist_ID}'


        print(total_playlists,end=".\t")
        print('%34s' %pl_link, end = "\t\t\t",)
        print(f'{hours:02d}:{minutes:02d}:{seconds:02d}',end = "\t\t\t")
        print(f'{total_videos:02d}')

else:
    print("No Playlists!")


