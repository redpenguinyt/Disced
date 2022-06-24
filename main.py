import os, asyncio
from utils.discord import discord, discordbot, send_to_discord
from utils.guilded import guilded, guildedbot, send_to_guilded

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

	await guildedbot.process_commands(message)

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

	await discordbot.process_commands(message)

# Run

loop = asyncio.get_event_loop()
loop.create_task(guildedbot.start(os.environ['guilded-token']))
loop.create_task(discordbot.start(os.environ['discord-token']))
loop.run_forever()