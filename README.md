```markdown
# Discord Chat Bot

This Python script is a simple Discord chat bot that allows you to send messages to a specific server and channel within your Discord account.

## Getting Started

To use this script, you'll need to create a Discord bot application and obtain its token. Here's how:

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click on "New Application" and give your bot a name.
3. Go to the "Bot" tab on the left sidebar and click on "Add Bot".
4. Copy the token under the "Token" section. **Keep this token private and do not share it with anyone.**

### Prerequisites

- Python 3.x
- discord.py library
  ```bash
  pip install discord.py
  ```

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/profshad0/discord-chat-bot.git
   ```

2. Navigate to the project directory:

   ```bash
   cd discord-chat-bot
   ```

3. Replace `'YOUR_TOKEN'` in the script with your actual Discord bot token.

4. Run the script:

   ```bash
   python bot.py
   ```

## Usage

1. Once the bot is running, it will prompt you to select a server and channel to join.
2. Enter the number corresponding to the server and channel you want to join.
3. You can then start typing messages to send to the selected channel.
4. To quit the bot, simply type 'quit' and press Enter.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [discord.py](https://github.com/Rapptz/discord.py) library for providing an easy-to-use interface for Discord bots.
```
