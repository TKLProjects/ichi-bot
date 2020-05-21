import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "s!")

@client.event
async def on_ready():
    print("Spark, active!")

@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

@client.command()
async def about(ctx):
    await ctx.send("```SparkBot™, by the loud-mouthed guy with little knowledge in programming - A.K.A Ichiki Hayaite#1111, special thanks to Lexi#2249.```")

@client.command(name="secret",hidden=True)
async def heehoo(ctx):
    await ctx.send("Super command yo - It's a secret to everybody!")
  
client.run("<token>")
