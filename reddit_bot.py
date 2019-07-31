import praw
import os
import json
import random

facts = {}

with open("facts.json") as factData:
	facts = json.load(factData)

#create the reddit instance
reddit = praw.Reddit("bot1") #note all my credentials are stored in the praw.ini file. See README for more details

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

		#if title contains a keyword then add a comment
		for key in facts.keys():
			if key in title:
				print("Replying to: " + submission.title)
				factReply = "Beep Boop\nDid you know " + random.choice(facts[key])
				submission.reply(factReply)
				replied_posts.append(submission.id)
				break #exit out of loop after 1 comment, dont want to spam

#write updated list of seen posts to the file
with open("replied_posts.txt", "w") as file:
	for submission_id in replied_posts:
		file.write(submission_id + "\n")

