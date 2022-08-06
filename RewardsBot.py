import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = "-") # set your prefix here
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(
        type=discord.ActivityType.playing, name="https://dsc.gg/sparxcave")) # set your status
    print("")
    print(" Rewards Bot is online!")
    print(" Now you can use the bot.") 

@client.command(pass_context=True)
async def claim(ctx):
  user = ctx.author
  DM = True # set if you want the bot to write to DM 
  channel = client.get_channel(1005390020615602277) # write the ID of your channel where the rewards will appear
 
  if ctx.channel.name == "claim": # write the name of your channel where the rewards will be claimed
    
 
     Lose = f"{ctx.author.mention} **>>** Unfortunately, you won nothing." # if you want you can change text of lose 
     Vip = f"{ctx.author.mention} **>>** You won the VIP for 3 days. :partying_face: (Create a ticket to claim)" # if you want you can change text of win
     # add more wins (if you want)
     rewards = [Lose,
                Lose,
                Lose,
                Vip,
                Lose,
                Lose
    # you can edit the chance of winning as you want        
                  ]
     reward = random.choice(rewards)
     await channel.send(reward)
 
     if DM == True:
      await user.send(reward)
  else:
      await ctx.send(f":rage: Hey! {ctx.author.mention} :rage: This command is not allowed here!") # set the message that the bot will write when the command is used in the wrong channel


client.run("token") # put your bot token here
 
