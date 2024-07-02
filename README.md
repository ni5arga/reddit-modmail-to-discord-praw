# Reddit to Discord Modmail Bot (PRAW)

This Python script is designed to create a Reddit bot that monitors incoming modmails to a specific subreddit and sends them to a Discord channel using webhooks.

## Prerequisites

Before using this script, you need to have the following:

- Python installed on your system.
- Reddit API credentials (client ID, client secret, username, password, and user agent).
- A Reddit account that is a moderator of the subreddit you want to monitor.
- The name of the subreddit you want to monitor.
- A Discord server with a text channel where you can create a webhook.
- The Discord webhook URL.

## Installation

1. Clone or download this repository to your local machine.

2. Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. Open the main.py script in a text/code editor.

Replace the following placeholders with your actual information:

`YOUR_REDDIT_CLIENT_ID`
`YOUR_REDDIT_CLIENT_SECRET`
`YOUR_REDDIT_USERNAME`
`YOUR_REDDIT_PASSWORD`
`YOUR_REDDIT_USER_AGENT`
`YOUR_SUBREDDIT_NAME`
`YOUR_DISCORD_WEBHOOK_URL`

4. Run the script `py main.py`
