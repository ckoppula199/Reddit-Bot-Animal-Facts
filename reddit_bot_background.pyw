import praw
import os
import json
import random
import time

"""
Data Source Credit: https://gitlab.insrt.uk/BarkingDog/barking-bot/blob/9ce097b0e7421770ef676e609e5fd7559d3cf96c/Data/facts.json
"""

#function to comment on reddit posts
def commentFacts(sub):
	subreddit = reddit.subreddit(sub)
	for submission in subreddit.hot(limit=5):

		#check to see if the bot has already replied to this post
		if submission.id not in replied_posts:

			#get the title in lowercase
			title = submission.title.lower()

			#if title contains a keyword then add a comment
			for key in facts.keys():
				if key in title:
					#print("Replying to: " + submission.title + " in " + sub)
					factReply = "Did you know " + random.choice(facts[key])
					submission.reply(factReply)
					replied_posts.append(submission.id)
					break #exit out of loop after 1 comment, dont want to spam


while True:
	
	with open("facts.json") as factData:
		facts = json.load(factData)

	#create the reddit instance
	reddit = praw.Reddit("animalFactsBot") #note all my credentials are stored in the praw.ini file. See README for more details

	#check to see if file is present, if not create an empty list
	if not os.path.isfile("replied_posts.txt"):
		replied_posts = []

	#if reddit post ids are in the file, read them into a list
	else:

		with open("replied_posts.txt", "r") as file:
			replied_posts = file.read()
			replied_posts = replied_posts.split("\n") #each id is on a new line
			replied_posts = list(filter(None, replied_posts)) #removes empty values
			#print(replied_posts)

	commentFacts("AnimalsBeingBros")
	commentFacts("AnimalsBeingDerps")
	commentFacts("AnimalsBeingJerks")
	commentFacts("funny")
	commentFacts("science")
	commentFacts("art")
	commentFacts("gifs")
	commentFacts("mildlyinteresting")
	commentFacts("interestingasfuck")
	commentFacts("tumblr")
	commentFacts("UpliftingNews")
	

	#if file size is over half a MB then remove the oldest half of the codes as the are likely no longer in scope of top 50 in the subreddit
	#this prevents the file size getting too big with long run times
	if os.path.getsize("replied_posts.txt") > 500000:
		length = len(replied_posts)
		to_remove = int(length/2)
		replied_posts = replied_posts[to_remove:]

	#write updated list of seen posts to the file
	with open("replied_posts.txt", "w") as file:
		#print(replied_posts)
		for submission_id in replied_posts:
			file.write(submission_id + "\n")

	


	#wait an hour before running again
	time.sleep(3600) 

