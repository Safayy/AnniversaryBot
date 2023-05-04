import datetime
import random
import discord
from discord import app_commands
import json
import sys
import os

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

if not os.path.isfile(f"{os.path.realpath(os.path.dirname(__file__))}/config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open(f"{os.path.realpath(os.path.dirname(__file__))}/config.json") as file:
        config = json.load(file)

# @tree.command(name = "setup", description = "Setup tool (Future) ", guild=discord.Object(id=965005898319802409))
# async def first_command(interaction):
#     await interaction.response.send_message("""```🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍\n```""")

# @tree.command(name="now", description="Duration of current years and days dated")
# async def first_command(interaction):
    
@tree.command(name = "now", description = "Duration of current years and days dated", guild=discord.Object(id=965005898319802409))
async def first_command(interaction):
    start_date = datetime.datetime(2022, 4, 1)
    current_date = datetime.datetime.now()
    days = (current_date - start_date).days
    total_seconds = (current_date - start_date).total_seconds()
    u_years = total_seconds / (365.25 * 24 * 60 * 60)    
    years = "{:.1f}".format(u_years)
    
    image_dir = "images"
    files = os.listdir(image_dir)
    random_file = random.choice(files)
    file = discord.File(os.path.join(image_dir,random_file), random_file)
    
    embed = discord.Embed(title="Been together for", color=0XEE578C)
    embed.add_field(name="", value=f"{years} years or")
    embed.add_field(name="", value=f"{days} days!")
    embed.set_thumbnail(url=f"attachment://{random_file}")
    await interaction.response.send_message(embed=embed, file=file)

@tree.command(name = "next", description = "Date of next anniversary", guild=discord.Object(id=965005898319802409))
async def first_command(interaction):
    current_date = datetime.datetime.now()
    next_april_1st = datetime.datetime(current_date.year + 1, 4, 1) if current_date.month >= 4 else datetime.datetime(current_date.year, 4, 1)
    days = (next_april_1st - current_date).days
    
    # Get random thumbnail
    image_dir = "images"
    files = os.listdir(image_dir)
    random_file = random.choice(files)
    file_path = os.path.join(image_dir, random_file)
    file = discord.File(file_path, filename=random_file)
    
    print(f"{random_file}\t{file_path}")

    embed = discord.Embed(title="Anniversary is on", color=0XEE578C)
    embed.add_field(name="", value=next_april_1st.date())
    embed.add_field(name=f'', value="")
    embed.add_field(name=f'In {days} days!', value="")
    embed.set_thumbnail(url=f"attachment://{random_file}")
    await interaction.response.send_message(embed=embed, file=file)

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=965005898319802409))
    print(f'{client.user} is now running')

client.run(config["token"])