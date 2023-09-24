# just some code to delete messages

import discord
import discord.ext import commands, tasks
from discord_slash import SlashCommand, SlashContext

@slash.slash(name="clear", description="→ Delete Messages in a Channel.")
async def clear(ctx, number: int):
    await ctx.defer()
    if number <= 0:
        await ctx.send("→ Please provide a valid number of messages to delete.")
        return

    messages = await ctx.channel.history(limit=number + 1).flatten()
    await ctx.channel.delete_messages(messages)
    await ctx.send(f"→ Successfully deleted {number} messages.", delete_after=5)
