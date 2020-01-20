import requests
import json

# Perform the actual HTTP request and initial parsing to build the Video objects from the response.
class Query:
    videos=[]

    # Takes as input the type of query (feed_id) and the maximum number of results (max_results) that the query should obtain.
    # The correct HTTP request must be constructed and submitted. The results are converted
    # into Video objects, which are stored within this class
    def __init__(self, feed_id, max_results):
        if feed_id == 1:
            if max_results == 1:
                l = requests.Session().get(
                    'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&chart=mostPopular&regionCode=IN&key=AIzaSyBLgYSlrf_-WCInXhij1PvFY_gx9mi0rrk&maxResults=1')
            elif max_results == 2:
                l = requests.Session().get(
                    'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&chart=mostPopular&regionCode=IN&key=AIzaSyBLgYSlrf_-WCInXhij1PvFY_gx9mi0rrk&maxResults=2')
            elif max_results == 3:
                l = requests.Session().get(
                    'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&chart=mostPopular&regionCode=IN&key=AIzaSyBLgYSlrf_-WCInXhij1PvFY_gx9mi0rrk&maxResults=3')
            elif max_results == 4:
                l = requests.Session().get(
                    'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&chart=mostPopular&regionCode=IN&key=AIzaSyBLgYSlrf_-WCInXhij1PvFY_gx9mi0rrk&maxResults=4')
            elif max_results == 5:
                l = requests.Session().get(
                    'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&chart=mostPopular&regionCode=IN&key=AIzaSyBLgYSlrf_-WCInXhij1PvFY_gx9mi0rrk&maxResults=5')

            output = json.loads(l.content)
            #print(output)
            for video in output['items']:
                videoObj=Video(video)
                self.videos.append(videoObj)



    # Prints out information on each video and YouTube user, include the aforementioned statistics data.
    #def str__(self):
     #   print('statistical data')


class Video:
    Title ='Title of the Video'
    #UserObj = User('fsddsffs')
    Description='Media Description'
    FavoriteCount = 'favoriteCount'
    TotalViews = 'Total Views'
    LikeCount='Like Count'
    DisLikeCount='Dislike Count'
    CommentCount='Comment Count'
    # The entry_str will contain the text encapsulated in a single <entry> section.
    # The string must be parsed to extract the various pieces of information and the text to create the User instance.
    def __init__(self, entry_str):
        self.Title=entry_str['snippet']['title']
        self.TotalViews = entry_str['statistics']['viewCount']
        if 'favoriteCount' in entry_str['statistics'].keys():
            self.FavoriteCount = entry_str['statistics']['favoriteCount']
        if 'likeCount' in entry_str['statistics'].keys():
            self.LikeCount = entry_str['statistics']['likeCount']

        if 'dislikeCount' in entry_str['statistics'].keys():
            self.DisLikeCount = entry_str['statistics']['dislikeCount']
        if 'commentCount' in entry_str['statistics'].keys():
            self.CommentCount = entry_str['statistics']['commentCount']

        if 'description' in entry_str['snippet'].keys():
            self.Description = entry_str['snippet']['description']


    # Include this function to display the stored Video data, as well as data for the associated uploader.
    def __str__(self):
        print ('Title: ',self.Title)
        print ('ViewCount: ',self.TotalViews)
        print('Description: ',self.Description)
        print('LikeCount:', self.LikeCount)
        print('DislikeCount: ',self.DisLikeCount)
        print('CommentCount:', self.CommentCount)




def main():
    print("\t\tWelcome to the YouTube text-based Query application.\n\t\t----------------------------------------------------")
    print("You can select a popular feed to perform a query on and view statistical information about the related videos and users.")
    print('---------------------------------------------------------------------------------------------------------------------------')
    print('\n1)Most Popular\n2)Quit')
    choice = int(input('Select the feed from following:'))
    if (choice==1):
        max_result = int(input('Enter the maximum number of the result: '))
        query = Query(choice, max_result)
        print('**************************************************************************************************')
        print("                                    Most Popular                                                  ")
        print('**************************************************************************************************')

        for i in range(max_result):
            query.videos[i].__str__()
            print('**************************************************************************************************')

    else:
        print('ThankYou')

main()