import datetime
import discord
import json
import asyncio
import os

with open("config.json") as f:
    config = f.read()
config = json.loads(config)
token = config["token"]
prefix = config["prefix"]
presence = config["status"]
ch_name = config["channel_name"]
ch_id = config["channel_id"]


intents = discord.Intents().default()
client = discord.Client(command_prefix=prefix, intents=intents)

async def on_ready():
    print("Bot logged in! Driver Bot, initializing!")
    await client.change_presence(activity=discord.Game(name=presence))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if not message.content.startswith(prefix):
        return
    if message.channel.name != f"{ch_name}":
        bot_msg = await message.channel.send(f"Sorry! This command can only be used in <#{ch_id}> channel!")
        await asyncio.sleep(5)
        await bot_msg.delete()
        return

    #Command List:
    if message.content.startswith(prefix + 'search'):
        await send_search(message)
    elif message.content.startswith(prefix + 'help'):
        await send_help_message(message)
    elif message.content.startswith(prefix + 'info'):
        await send_info_message(message)

# Driver Search command
async def send_search(message):
    if message.content.startswith(prefix + 'search'):
        search_term = message.content[8:]
        if not search_term:
            embed = discord.Embed(title="Error", description=f"Please specify a search term after the **{prefix}search** command.", color=0xff0000)
            await message.channel.send(embed=embed)
            return
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        print("[{}] User: {}#{} searched: {}".format(timestamp, message.author.name, message.author.discriminator, search_term))
        search_term = message.content[8:]
        found = False
        for file in os.listdir("driver_repo"):
            if search_term in file:
                with open(os.path.join("driver_repo", file)) as f:
                    data = json.load(f)
                    driver_name = data["driver_name"]
                    description = data["description"]
                    brand_model = data["brand_model"]
                    stock_tuning = data["stock_tuning"]
                    ohms = data["ohm"]
                    driver_size = data["driver_size"]
                    tuning_diff = data["tuning_diff"]
                    price = data["price"]
                    driver_image = data["driver_image"]

                    # create the embed
                    embed = discord.Embed(title=driver_name, description=description, color=0x7289da)
                    embed.add_field(name="Branded Models", value=brand_model)
                    embed.add_field(name="Stock Tuning (Unmodded)", value=stock_tuning)
                    embed.add_field(name="Resistance (in ohms)", value=ohms)
                    embed.add_field(name="Driver Size", value=driver_size)
                    embed.add_field(name="Tuning Difficulty (1-5 scale)", value=tuning_diff)
                    embed.add_field(name="Price (in USD)", value=price)
                    embed.set_image(url=driver_image)
                    embed.set_footer(text="Driver Bot - still under development.", icon_url=client.user.avatar_url)
                    await message.channel.send(embed=embed)
                    found = True

        if not found:
            embed = discord.Embed(title="Error", description="No driver found for search term: {}".format(search_term), color=0xff0000)
            await message.channel.send(embed=embed)

#Bot Help command
async def send_help_message(message):
    embed = discord.Embed(title="Driver Bot Help", description="List of available commands:", color=0x3189da)
    embed.add_field(name=prefix + "search [term]", value="Searches for a driver with the specified term in its name or description. Prints all matching search terms.")
    embed.add_field(name=prefix + "info", value="Shows developer info.")
    embed.add_field(name=prefix + "help", value="Displays this help message.")
    embed.set_footer(text="Driver Bot - still under development.", icon_url=client.user.avatar_url)
    await message.channel.send(embed=embed)

#Bot Info command
async def send_info_message(message):
    embed = discord.Embed(title="Driver Bot Info", description="List of developers/contributors", color=0x4817da)
    embed.add_field(name="Created by", value="Aspidiske#8080")
    embed.add_field(name="Fork or Contribute on GitHub!", value="[GitHub Link](https://github.com/Yuuhei/diy-driver-bot)")
    embed.add_field(name="Join my Discord Server! (Acts as a support server too)", value="[Click Here!](https://discord.gg/mj2jbz3RWw)")
    embed.set_footer(text="Driver Bot - still under development.", icon_url=client.user.avatar_url)
    await message.channel.send(embed=embed)

client.run(token)
