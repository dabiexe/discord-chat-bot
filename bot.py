import discord
import asyncio

TOKEN = "YOUR_TOKEN"

class DiscordClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.servers = None

    async def on_ready(self):
        print(f'Logged in as {self.user}')

        self.servers = {guild.name: guild for guild in self.guilds}
        print("Your servers:")
        for idx, (name, guild) in enumerate(self.servers.items(), 1):
            print(f"{idx}. {name}")

        server_idx = int(input("Enter the number of the server you want to join: ")) - 1
        server = list(self.servers.values())[server_idx]

        print(f"Joining server: {server.name}")

        channels = {channel.name: channel for channel in server.text_channels}
        print("Channels in this server:")
        for idx, (name, channel) in enumerate(channels.items(), 1):
            print(f"{idx}. {name}")

        channel_idx = int(input("Enter the number of the channel you want to join: ")) - 1
        channel = list(channels.values())[channel_idx]

        print(f"Joining channel: {channel.name}")

        await self.send_message(channel)

    async def send_message(self, channel):
        while True:
            message = input("Enter your message: ")
            if message.lower() == 'quit':
                await self.logout()
                return
            await channel.send(message)

if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.typing = False
    intents.presences = False
    client = DiscordClient(intents=intents)
    client.run(TOKEN)
