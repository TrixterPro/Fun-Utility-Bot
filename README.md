
# Image Generation Discord Bot  
A Discord bot that enables seamless image generation using the `/imagine` command. It's quick to set up and easy to use!


## Commands

### Fun & Games
-   `/8ball` – Ask the magic 8-ball a question.
-   `/coinflip` – Flip a coin for heads or tails.
-   `/dice roll` – Roll a customizable dice.
-   `/truth` – Get a random truth.
-   `/dare` – Get a random dare.

### Entertainment
-   `/joke` – Fetches a random joke.
-   `/memes` – Fetches a random meme from Reddit.
    

### Utility
-   `/avatar` – Get a user's avatar.
-   `/ping` – Show bot's response time.
-   `/qr` – Generate a QR code from text.
-   `/youtube search` – Search for YouTube videos from Discord.

---

## Installation & Setup
### Prerequisites
1. Ensure you have **Python 3.8+** installed.
2. Clone or download this repository to your local machine.

### Step 1: Install Dependencies  
**Run the following command** in your terminal to install the required libraries:
```bash
pip install -r requirements.txt
```
### Step 2: Generate and Configure config.yml
-   Run the bot initially to generate the `config.yml` file:
```bash
python main.py
``` 
-   Open the generated `config.yml` file and configure it with your details.

**The default config file looks like this:**
```yml
# Your discord bot token get it by creating an application at https://discord.com/developers/applications

TOKEN: ''

# Prefix is for the discord bot prefixed commands (such as !help, '!' is the prefix here)

PREFIX: '!'

# Client Secret for Reddit API integrations (https://www.reddit.com/prefs/apps/)

CLIENT_SECRET: ''

# User Agent string for API requests

USER_AGENT: ''
```
You can enter `fun_meme_bot/0.1 by u/YourRedditUsername` in USER_AGENT Field.

### How to Get Your Discord Bot Token
-   Go to the [Discord Developer Portal](https://discord.com/developers/applications).
-   Create a **new application**.
-   **Open the application** that you just created.
-   Go to **Bot tab**.
-    Click on **reset token**.
-    **Copy** your bot token.
-   **Paste** it into the `TOKEN` field in your `config.yml`.
-   __**Make sure to enable all Gateway Intents from the bot tab.**__
  ![image_2024-12-06_181240534](https://github.com/user-attachments/assets/7c16144f-1507-4919-a406-01c290310b54)
### Running the Bot
Once configured:
```bash
python main.py
```
### Troubleshooting
-   Ensure the bot has the right permissions to register and use slash commands.
-   Double-check the `TOKEN` in your `config.yml` if issues persist.
-   Ensure the token is valid.

### Contributing
Feel free to contribute by opening issues or submitting pull requests. All contributions are welcome!
