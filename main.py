import praw
import requests

reddit_client_id = 'YOUR_REDDIT_CLIENT_ID'
reddit_client_secret = 'YOUR_REDDIT_CLIENT_SECRET'
reddit_username = 'YOUR_REDDIT_USERNAME'
reddit_password = 'YOUR_REDDIT_PASSWORD'
reddit_user_agent = 'YOUR_REDDIT_USER_AGENT'
subreddit_name = 'YOUR_SUBREDDIT_NAME'
discord_webhook_url = 'YOUR_DISCORD_WEBHOOK_URL'

try:
    reddit = praw.Reddit(
        client_id=reddit_client_id,
        client_secret=reddit_client_secret,
        username=reddit_username,
        password=reddit_password,
        user_agent=reddit_user_agent,
    )

    subreddit = reddit.subreddit(subreddit_name)

    for message in subreddit.modmail.conversations(limit=None):
        for message in message.messages:
            message_text = f'From: {message.author}\nSubject: {message.subject}\n\n{message.body}'

            discord_embed = {
                "title": message.subject,
                "description": message_text,
                "url": message.permalink,
                "color": 0x00FF00  
            }

            discord_payload = {
                'embeds': [discord_embed]
            }

            response = requests.post(discord_webhook_url, json=discord_payload)

            if response.status_code == 204:
                print('Message sent to Discord successfully!')
            else:
                print(f'Failed to send message to Discord. Status code: {response.status_code}')
except Exception as e:
    print(f'An error occurred: {str(e)}')
