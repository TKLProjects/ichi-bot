import discord
from discord.ext import commands
import asyncio
import time

client = commands.Bot(command_prefix = "s!")

async def status.task():
    while True:
				await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Izumi and Kazuki sparring! (s!help)"))
				await asyncio.sleep(30)
				await client.change_presence(activity=discord.Game(name="poker with Wryin! (s!help)"))
				await asyncio.sleep(30)
				await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the moon with Tsuki! (s!help)"))
				await asyncio.sleep(30)

@client.event
async def on_ready():
    print("Spark, active!")
    print("Logged in as:", client.user.name, "(", client.user.id, ")")
    client.loop.create_task(status_task())

@client.command()
async def ping(ctx):
"""Ping the Discord API."""
    await ctx.message.delete()
    before = time.monotonic()
    message = await ctx.send("Pinging...")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f("Pong!{int(ping)}ms"))
    print (f"Ping {int(ping)}ms")
    
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
