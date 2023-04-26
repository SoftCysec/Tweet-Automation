# Tweet-Automation

This project is a Python script that automatically generates and posts tech-related content on Twitter using the OpenAI GPT-3 API. The script posts daily tweets for the next 6 months.

## Requirements
- Python 3.6 or higher
- Tweepy
- OpenAI
- python-dotenv
- Transformers (optional, for using GPT-2)

## Installation
1. Clone the repository:
```
git clone https://github.com/SoftCysec/Tweet-Automation.git
```
```
cd Tweet-Automation
```
2. Install the required libraries:
```
pip install tweepy openai python-dotenv transformers
```
3. Create a `.env` file in the project directory and add your API keys and access tokens:
```
TWITTER_CONSUMER_KEY=your_consumer_key
TWITTER_CONSUMER_SECRET=your_consumer_secret
TWITTER_ACCESS_TOKEN=your_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
OPENAI_API_KEY=your_openai_api_key
```
Replace the placeholders with your actual keys and tokens.

## Usage
1. Run the script:
```
python app.py
```
The script will start posting auto-generated tech-related content daily for the next 6 months.
