import discord
from discord.ext import commands
import time

# Configuration
OWNER_IDS = [123456789]  # Replace with your user ID(s)
PREFIX = "."

# Create bot with intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, self_bot=True, intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print(f"Bot is running as a selfbot")

@bot.command(name="ping")
async def ping(ctx):
    """Ping command - only for owners"""
    # Check if user is owner
    if ctx.author.id not in OWNER_IDS:
        await ctx.message.delete()
        return
    
    # Calculate latency
    latency = round(bot.latency * 1000)
    
    # Send ping message
    embed = discord.Embed(
        title="🏓 Pong!",
        description=f"Latency: `{latency}ms`",
        color=discord.Color.green()
    )
    
    await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        pass
    else:
        print(f"Error: {error}")

# Run the bot with your token
if __name__ == "__main__":
    TOKEN = "YOUR_DISCORD_TOKEN_HERE"  # Replace with your token
    try:
        bot.run(TOKEN)
    except Exception as e:
        print(f"Failed to start bot: {e}")
