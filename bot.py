import discord
import requests
import os

TOKEN = os.getenv("DISCORD_TOKEN")
WEBHOOK_URL = os.getenv("MAKE_WEBHOOK_URL")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    data = {
        "username": str(message.author),
        "user_id": str(message.author.id),
        "channel": str(message.channel),
        "content": message.content
    }

    requests.post(WEBHOOK_URL, json=data)

client.run(TOKEN)
