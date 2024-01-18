import praw
import requests
import time

reddit_client_id = 'YOUR_CLIENT_ID'
reddit_client_secret = 'YOUR_CLIENT_SECRET'
reddit_username = 'YOUR_REDDIT_USERNAME'
reddit_password = 'YOUR_REDDIT_PASSWORD'
reddit_user_agent = 'YOUR_USER_AGENT'

discord_webhook_url = 'YOUR_DISCORD_WEBHOOK_URL'

# do not include "r/"
subreddit_to_monitor = 'YOUR_SUBREDDIT'

reddit = praw.Reddit(
    client_id=reddit_client_id,
    client_secret=reddit_client_secret,
    username=reddit_username,
    password=reddit_password,
    user_agent=reddit_user_agent
)

processed_conversations = set()

def send_discord_webhook(embed_data):
    payload = {
        "embeds": [embed_data]
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(discord_webhook_url, json=payload, headers=headers)

def monitor_modmail():
    subreddit = reddit.subreddit(subreddit_to_monitor)

    while True:
        unread_modmail = subreddit.modmail.conversations(state="new")

        for conversation in unread_modmail:
            if conversation.id not in processed_conversations:
                subject = conversation.subject
                sender = conversation.participant.name
                body = conversation.messages[-1].body_markdown
                message_link = f"https://mod.reddit.com/mail/all/{conversation.id}"

                embed_data = {
                    "title": f"New Modmail: {subject}",
                    "description": f"**Sender:** {sender}\n\n**Body:** {body}\n\n[Message Link]({message_link})",
                    "color": 0x00ff00
                }

                send_discord_webhook(embed_data)

                conversation.read()
                processed_conversations.add(conversation.id)

        time.sleep(1)

if __name__ == "__main__":
    monitor_modmail()
