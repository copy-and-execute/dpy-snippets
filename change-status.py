# just some code for an automatic-changing status

import discord
from discord.ext import commands, tasks
from discord_slash import SlashCommand, SlashContext
import random

@tasks.loop(seconds=5)
async def change_status():
    statuses = [
        {'type': discord.ActivityType.listening, 'text': 'your commands'},
        {'type': discord.ActivityType.watching, 'text': 'this channel'},
    ]
    status = random.choice(statuses)
    activity = discord.Activity(type=status['type'], name=f'{status["text"]}')
    await bot.change_presence(activity=activity)
