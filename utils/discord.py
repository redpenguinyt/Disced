import discord, aiohttp
from discord.ext import commands
from . import config

discordbot = commands.Bot(
	command_prefix="$",
	description=config.DESCRIPTION
)

@discordbot.event
async def on_ready():
	print("Discord| Ready")

@discordbot.command()
async def test(ctx):
	embed = discord.Embed(title="I'm connected! :D")
	await ctx.channel.send(embed=embed)

async def send_to_discord(webhook_url, username, avatar_url, message):
	async with aiohttp.ClientSession() as session:
		webhook = discord.Webhook.from_url(
			webhook_url,
			adapter=discord.AsyncWebhookAdapter(session)
		)
	await webhook.send(message, username=username, avatar_url=avatar_url)