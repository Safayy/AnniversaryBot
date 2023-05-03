import datetime
import random
import discord
from discord import app_commands

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# @tree.command(name = "setup", description = "Setup tool (Future) ", guild=discord.Object(id=965005898319802409))
# async def first_command(interaction):
#     await interaction.response.send_message("""```🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍\n```""")

images = ["https://i.imgur.com/mxQSP5i.gif",
              "https://media1.giphy.com/media/IOnEXnUXwQ7yE/giphy.gif",
              "https://image.myanimelist.net/ui/kvW-ZKVqtlVlpFs6Iopx44-Z-x51OUKslYWxByiGVrd911JTQVUYCtead14MZt7R6QgGHUfjU6yrGDIDPLE6LJhmVHmsd3TVGU_JBb-ITLA",
              "https://animesher.com/orig/2/206/2063/20636/animesher.com_pastel-daddy-pale-2063631.gif",
              "https://media.tenor.com/ORr3CX9EknYAAAAC/chocolate-banana-mikazuki.gif",
              "https://media.tenor.com/-UolTt_O2JoAAAAM/hot-sex.gif",
              "https://i2.kym-cdn.com/photos/images/original/000/929/108/c7f.gif",
              "https://i2.kym-cdn.com/photos/images/original/000/929/108/c7f.gif",
              "https://media.tenor.com/jleVaFqBaP4AAAAC/excited-anime.gif",
              "https://64.media.tumblr.com/00c444d523134660bb1b3a7dd48482cc/2c1e576087251d59-9c/s500x750/4d62f3c685435838576b24ea6d5c9239bc1f928a.gif"
              ]

@tree.command(name = "now", description = "Date of current years dated", guild=discord.Object(id=965005898319802409))
async def first_command(interaction):
    start_date = datetime.datetime(2022, 4, 1)
    current_date = datetime.datetime.now()
    total_seconds = (current_date - start_date).total_seconds()
    u_years = total_seconds / (365.25 * 24 * 60 * 60)    
    years = "{:.1f}".format(u_years)

    embed = discord.Embed(title="Been together for", color=0xFFFFFF)
    embed.add_field(name="", value=f"{years} year(s)!")
    embed.set_thumbnail(url=images[random.randint(0,len(images)-1)]) #Get random gif
    await interaction.response.send_message(embed=embed)

@tree.command(name = "next", description = "Date of next anniversary", guild=discord.Object(id=965005898319802409))
async def first_command(interaction):
    current_date = datetime.datetime.now()
    next_april_1st = datetime.datetime(current_date.year + 1, 4, 1) if current_date.month >= 4 else datetime.datetime(current_date.year, 4, 1)
    days = (next_april_1st - current_date).days
    embed = discord.Embed(title="Anniversary is on", color=0xFFFFFF)
    embed.add_field(name="", value="2023-05-04")
    embed.add_field(name=f'', value="")
    embed.add_field(name=f'In {days} days!', value="")
    
    embed.set_thumbnail(url=images[random.randint(0,len(images)-1)]) #Get random gif
    await interaction.response.send_message(embed=embed)

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=965005898319802409))
    print("Ready!")
    
@client.event
async def on_message(message):
    print(f'{message.content}')

client.run("MTEwMzMwMDk4MTczMjY3NTY0NQ.GZ5Xpe.msnAsB8f4f7g8StrmUgu8Z3HLB86KauBNo4Dgk")