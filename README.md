# Reddit-Bot-Animal-Facts
This is my code for a reddit bot that scans the subreddit r/aww for posts containing words relating to dogs, cats or pandas and then posts a fact about said animal

You should keep in mind many people when starting out with the reddit API hard code their login username, password, secret key and use script id into their code. For obvious reasons I have not done this. 

Instead I have copied the praw.ini to the same folder as where my script is and added the following

oauth_url=https://oauth.reddit.com
reddit_url=https://www.reddit.com
short_url=https://redd.it

[bot1]
client_id=*******
client_secret=*******
password=******
username=*******
user_agent=******

then in my ptyhon script have used:
reddit = praw.Reddit('bot1')
to connect to the API

So if you wish to use this code you must have your own reddit account, create your own developed application on reddit and take note of the secret and use keys and enter them as above. The user_agent can be anything as long as it is unique.
