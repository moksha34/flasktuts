from collections import namedtuple,deque,defaultdict
import time
from typing import *
from itertools import islice

Post = namedtuple("post",["username","timestamp","text"])  #type: namedtuple
User = str
posts=deque() #type: deque
user_posts=defaultdict(deque) #type: DefaultDict[str,deque]
following=defaultdict(set) #type: DefaultDict[User,set]
followers=defaultdict(set)  #type: DefaultDict[User,set]

def post_message(user,text,timestamp=None):
    timestamp= timestamp or time.time()
    post=Post(user,timestamp,text)
    posts.appendleft(post)
    user_posts[user].appendleft(post)

def follow(user: User,followed_user: User)->None:
    following[user].add(followed_user)
    followers[followed_user].add(user)

def posts_by_user(user: User,limit: Optional[int]):
    return list(islice(user_posts[user],limit))