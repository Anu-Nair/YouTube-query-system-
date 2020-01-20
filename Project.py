import requests
import json

print("\t\tWelcome to the YouTube text-based Query application.\n\t\t----------------------------------------------------")
print("You can select a popular feed to perform a query on and view statistical information about the related videos and users.")

print('---------------------------------------------------------------------------------------------------------------------------')


print('\n1)Most Popular\n2)Top Rated')

ch=int(input('Select the feed from following:'))


if ch==1:
    print("\n\nYOU ARE VIEWING 'MOST POPULAR VIDEOS' OF TODAY: \n")
    no_of_results = int(input("Enter the maximum number of results to obtain: "))

    if no_of_results == 1:
        l = requests.Session().get(
            'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&chart=mostPopular&regionCode=IN&key=AIzaSyBLgYSlrf_-WCInXhij1PvFY_gx9mi0rrk&maxResults=1')
    elif no_of_results == 2:
        l = requests.Session().get(
            'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&chart=mostPopular&regionCode=IN&key=AIzaSyBLgYSlrf_-WCInXhij1PvFY_gx9mi0rrk&maxResults=2')
    elif no_of_results == 3:
        l = requests.Session().get(
            'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&chart=mostPopular&regionCode=IN&key=AIzaSyBLgYSlrf_-WCInXhij1PvFY_gx9mi0rrk&maxResults=3')
    elif no_of_results == 4:
        l = requests.Session().get(
            'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&chart=mostPopular&regionCode=IN&key=AIzaSyBLgYSlrf_-WCInXhij1PvFY_gx9mi0rrk&maxResults=4')
    elif no_of_results == 5:
        l = requests.Session().get(
            'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&chart=mostPopular&regionCode=IN&key=AIzaSyBLgYSlrf_-WCInXhij1PvFY_gx9mi0rrk&maxResults=5')

    output = json.loads(l.content)
    for video in output['items']:
        Title = video['snippet']['title']
        Views = video['statistics']['viewCount']
        print('Title:', Title)
        print('Views:', Views)

        if 'likeCount' in video['statistics'].keys():
            LikeCount = video['statistics']['likeCount']
            print('LikeCount:', LikeCount)

        if 'dislikeCount' in video['statistics'].keys():
            DislikeCount = video['statistics']['dislikeCount']
            print('DislikeCount:', DislikeCount)

        '''if 'description' in video['snippet'].keys():
            Description = video['snippet']['description']
            print('Description: ', Description)'''

        if 'commentCount' in video['statistics'].keys():
            CommentCount = video['statistics']['commentCount']
            print('CommentCount:', CommentCount)

        if 'channelTitle' in video['snippet'].keys():
            Uploader = video['snippet']['channelTitle']
            print('Uploader:', Uploader, '\n')

        print(
            '************************************************************************************************************************************************************************\n')

elif ch==2:
    payload = {'part': 'snippet', 'key': 'AIzaSyBLgYSlrf_-WCInXhij1PvFY_gx9mi0rrk', 'order': 'rating', 'type': 'video',
               'videoLicense': 'youtube', 'publishedAfter': '2018-08-31T06:46:11.000Z'}
    l = requests.Session().get('https://www.googleapis.com/youtube/v3/search', params=payload)
    resp_dict = json.loads(l.content)
    print(resp_dict)
    for i in resp_dict['items']:
        print("Title: ", i['snippet']['title'],'\n','PublishedAt: ', i['snippet']['publishedAt'])

else:
    print('Invalid Input')
