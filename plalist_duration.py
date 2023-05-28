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

#Default Channel ID of Corey Schafer
#will be used if no parameter is passed.
channel_ID = "UCCezIgC97PvUuR4_gbFUs5g"
channel_name = 'Corey Schafer'


print(f'Usage Format: python playlist_duration.py "Channel Name"\n')


try:
    channel_name = sys.argv[1]
    # Search for the channel using the channel name
    search_response = youtube.search().list(
        q=channel_name,
        part='id',
        type='channel',
        maxResults=1
    ).execute()

    # Retrieve the channel ID from the search response

    try:
        channel_ID = search_response['items'][0]['id']['channelId']
        print(f'Channel Name: {channel_name} \nChannel Id: {channel_ID}\n')
    except IndexError as e:
        print(f'No Channel Found for "{channel_name}"')
except IndexError as e:
    print(f"Using default Channel name '{channel_name}'")
    




# print(channel_ID)
# print()

# print(json.dumps(response,indent=4))
# print('Channel ID: ',channel_ID)

max_video_playlist_ID = None
nextPageToken = None
videosCount = 0

PlayList_IDs = []

playlist_Name = dict()

# pandasPlaylist_ID = None

while True:
    request_pl = youtube.playlists().list(
        part="contentDetails,id,snippet",
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
        # if vc==11:
        #     pandasPlaylist_ID = videos['id']
        PlayList_IDs.append(videos['id'])
        
        playlist_Name[videos['id']] = videos['snippet']['title']

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


# total_playlists = 0

if PlayList_IDs:

    # print(f'Name\tPlaylist LINK\t\t\t\t\t\t\t\t\t\t\tDuration(HH:MM:SS)\t\tTotal Videos ')

    for playlist_ID in PlayList_IDs:
        # total_playlists+=1
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


        print(f'Name: {playlist_Name[playlist_ID]}')
        print(f'Link: {pl_link}')
        print(f'Duration(HH:MM:SS): {hours:02d}:{minutes:02d}:{seconds:02d}')
        print(f'Total Videos: {total_videos}')
        print()


else:
    print("No Playlists!")


