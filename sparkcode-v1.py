import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "s!")

@client.event
async def on_ready():
    print("Spark, active!")
    print("Logged in as:", client.user.name, "(", client.user.id, ")")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Izumi and Ichiki sparring! (s!help)"))

@client.command()
async def ping(ctx):
"""Test the bot's skills on ping-pong."""
    await ctx.send("Pong!")
    
@client.command()
async def about(ctx):
"""Learn more about this bot."""
    await ctx.send("```SparkBot™, a small quarantine project created by the loud-mouthed, purple-haired guy with little knowledge in programming - A.K.A Ichiki Hayaite#1111!\n\nSpecial thanks to Lexi#2249!```")

@client.command(name="secret",hidden=True)
async def heeho(ctx):
    await ctx.send("Super command yo - It's a secret to everybody!")

tokenfile = open("./token.txt")
token = tokenfile.read()
client.run(token)
