import discord
import time
from discord import app_commands 
from discord.ext import commands
import random
import string

# intents = discord.Intents().all()
# bot = commands.Bot(command_prefix="!", intents = intents,
# case_insensitive=True)
# bot.remove_command('help')

# @bot.command()
# async def help(ctx):
#     embed = discord.Embed(title="Help Command (Custom)",
# description="/mines - for bloxflip mines - in tile_amt type how many mines u want to mine and in round_id type your round id which u can see in game settings")
#     await ctx.channel.send(embed = embed)


class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False
 
    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync() 
            self.synced = True
        print(f"We have logged in as {self.user}.")
        await client.change_presence(activity=discord.Streaming(name='Your Dedismuteli', url='https://www.twitch.tv/baxadoto'))


client = aclient()
tree = app_commands.CommandTree(client)
 
@tree.command(name = 'mines', description='mines game mode')
async def mines(interaction: discord.Interaction, tile_amt: int, round_id : str):
    if len(round_id) == 36:
        start_time = time.time()
        grid = ['❌','❌','❌','❌','❌','❌','❌','❌','❌','❌','❌','❌','❌','❌','❌','❌','❌','❌','❌','❌','❌','❌','❌','❌','❌']
        already_used = []
 
        count = 0
        while tile_amt > count:
            a = random.randint(0, 24)
            if a in already_used:
                continue
            already_used.append(a)
            grid[a] = '✅'
            count += 1
 
        chance = random.randint(45,95)
        if tile_amt < 4:
            chance = chance - 15
 

        em = discord.Embed(color=0xfff700)
        em.add_field(name='Grid', value="\n" + "```"+grid[0]+grid[1]+grid[2]+grid[3]+grid[4]+"\n"+grid[5]+grid[6]+grid[7]+grid[8]+grid[9]+"\n"+grid[10]+grid[11]+grid[12]+grid[13]+grid[14]+"\n"+grid[15]+grid[16]+grid[17] \
            +grid[18]+grid[19]+"\n"+grid[20]+grid[21]+grid[22]+grid[23]+grid[24] + "```\n" + f"**Accuracy**\n```{chance}%```\n**Round ID**\n```{round_id}```\n**Response Time:**\n```{str(int(time.time() - int(start_time)))}```")
        em.set_footer(text='made by ratiela')
        await interaction.response.send_message(embed=em)
    else:
        em = discord.Embed(color=0xfff700)
        em.add_field(name='Error', value="Invalid round id")
        await interaction.response.send_message(embed=em)

 
client.run('MTE2MDE2MTMxMzgwNTMxNjE4Ng.GMgpYs.dMcNkdOHxP5-NVzpg2gq5QuAbsUq5Q-qhfeG-s')