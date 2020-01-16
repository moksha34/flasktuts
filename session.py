from pubsub import *
from pprint import pprint

post_message("moksha","dad where are you")
post_message("dad","baby where are you")
post_message("moksha","dad are you behind the door")
post_message("mom","where are you guys")
post_message("dad","baby its a good day today")
post_message("dad","baby where are you both")


follow('moksha','dad')
follow('mom','dad')
if __name__=="__main__":
    #  for post in posts:
    #      pprint(post)
    #  for user in user_posts.keys():
    #      pprint(user_posts[user])
    pprint(followers)
    pprint(following)
    pprint(posts_by_user('dad',3))