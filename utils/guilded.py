import guilded
from guilded.ext import commands
from . import config

guildedbot = commands.Bot(
	command_prefix="$",
	description=config.DESCRIPTION
)

@guildedbot.event
async def on_ready():
	print('Guilded | Ready')

@guildedbot.command()
async def test(ctx):
	embed = guilded.Embed(title="I'm connected! :D")
	await ctx.channel.send(embed=embed)

async def send_to_guilded(webhool_url, username, avatar_url, message):
	print("WIP")