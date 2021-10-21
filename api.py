from googleapiclient.discovery import build
from config import YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_KEY, YOUTUBE_API_VERSION, MAX_RESULTS

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                developerKey=YOUTUBE_API_KEY)


def search(query):
    request = youtube.search().list(
        part='id,snippet',
        q=query,
        maxResults=MAX_RESULTS,
        type='video'
    )

    response = request.execute()
    search_results = []

    for video in response['items']:
        item = {
            'name': video["snippet"]["title"],
            'value': f'https://www.youtube.com/watch?v={video["id"]["videoId"]}',
        }

        search_results.append(item)

    return search_results
