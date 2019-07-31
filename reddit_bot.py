import praw
import os
import json

facts = {}

with open("facts.json") as factData
	facts = json.loads("facts.json")

#create the reddit instance
reddit = praw.Reddit("animalFactsBot") #note all my credentials are stored in the praw.ini file. See README for more details

#check to see if file is present, if not create an empty list
if not os.path.isfile("already_replied.txt"):
	replied_posts = []

#if reddit post ids are in the file, read them into a list
else:

	with open("already_replied.txt", "r") as file:
		replied_posts = file.read()
		replied_posts = replied_posts.split("\n") #each id is on a new line
		replied_posts = list(filter(None, replied_posts)) #removes empty values

#get top ten posts from the subreddit
subreddit = reddit.subreddit("AnimalsBeingBros")
for submission in subreddit.hot(limit=10):

	#check to see if the bot has already replied to this post
	if submission.id not in replied_posts:

		#get the title in lowercase
		title = submission.title.lower()

