import os, asyncio, requests
from utils.discord import discord, discordbot, send_to_discord
from utils.guilded import guilded, guildedbot, send_to_guilded
from discord_webhook import DiscordWebhook

# Guilded

@guildedbot.event
async def on_message(message):
	if not "Gil" in message.author.name:
		if message.channel.id == "97b0c27c-aa0a-4c2a-9c42-414982d19506":
			print(f"Guilded > {message.author.name} > {message.content}")
			await send_to_discord(
				os.environ['discord-webhook'],
				message.author.name,
				message.author.avatar.url,
				message.content
			)

# Discord

@discordbot.event
async def on_message(message):
	if not message.author.bot:
		if message.channel.id == 884525097677910033:
			print(f"Discord > {message.author.name} > {message.content}")
			await send_to_guilded(
				os.environ["guilded-webhook"],
				message.author.name,
				message.author.avatar_url,
				message.content
			)

# Run

# discordbot.run(os.environ["discord-token"])
guildedbot.run(os.environ['guilded-token'])