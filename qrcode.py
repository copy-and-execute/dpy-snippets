# just some code to create an qrcode via an discord bot (using an api)

import discord
from discord.ext import commands, tasks
from discord_slash import SlashCommand, SlashContext
import qrcode

@slash.slash(name="qr", description="→ Create an QR-Code for an Domain/IP.")
async def qr(ctx: SlashContext, url: str):
    qr_data = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://{url}"
    qr_image = qrcode.make(qr_data)
    qr_image.save("qr_code.png")

    file = discord.File("qr_code.png")
    await ctx.send(f"→ Your QR-Code for **{url}**.", file=file)
