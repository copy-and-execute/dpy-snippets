# just some code to create an shortlink via an discord bot (using an api)

import discord
from discord.ext import commands, tasks
from discord_slash import SlashCommand, SlashContext
import requests

@slash.slash(name="short-url", description="→ Shorten an long URL via shrtco")
async def shorten_url(ctx: SlashContext, url: str):
    api_url = f"https://api.shrtco.de/v2/shorten?url={url}"
    response = requests.get(api_url)
    data = json.loads(response.text)
    short_url = data['result']['full_short_link']
    await ctx.send(f"→ Your Short URL for {url}: {short_url}")
