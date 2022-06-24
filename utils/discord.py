import discord, aiohttp
from discord.ext import commands
from . import config

discordbot = commands.Bot(
	command_prefix="$",
	description=config.DESCRIPTION
)

@discordbot.event
async def on_ready():
	print("Discord | Ready")

@discordbot.command()
async def test(ctx):
	embed = discord.Embed(title="I'm connected! :D")
	await ctx.channel.send(embed=embed)

async def send_to_discord(webhook_url, username, avatar_url, message):
	webhook = discord.Webhook.from_url(
		webhook_url,
		adapter=discord.RequestsWebhookAdapter()
	)
	webhook.send(message, username=f"[GUILDED] {username}", avatar_url=avatar_url)