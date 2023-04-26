import tweepy
import datetime
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API keys and access tokens from environment variables
consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
access_token = os.getenv('TWITTER_ACCESS_TOKEN')
access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
openai_api_key = os.getenv('OPENAI_API_KEY')

# Set OpenAI API key
openai.api_key = openai_api_key

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# Function to generate tech-related content using GPT-3
def generate_tech_content(prompt, max_tokens=50):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.7,
    )

    content = response.choices[0].text.strip()
    return content


# Function to post a tweet
def post_tweet(content):
    try:
        api.update_status(content)
        print(f"Tweet posted: {content}")
    except tweepy.TweepError as e:
        print(f"Error posting tweet: {e}")


# Function to post auto-generated tech-related content daily for the next 6 months
def post_tech_content_daily():
    today = datetime.date.today()
    end_date = today + datetime.timedelta(days=6*30)  # 6 months from today

    while today <= end_date:
        prompt = "Generate a daily tech-related tweet about one of the following topics: AI, ML, Data Science, Mobile Development, Software Development, Cyber Security, and more. The tweet should include a fact, tip, news, or other interesting information related to the topic."
        content = generate_tech_content(prompt)
        post_tweet(content)
        today += datetime.timedelta(days=1)


# Call the function to start posting
post_tech_content_daily()
