# just some code to scan for ports on an ip via an discord bot

import discord
from discord.ext import commands, tasks
from discord_slash import SlashCommand, SlashContext
import socket

@slash.slash(name='portscan', description='→ Scan for Ports on an IP/Domain.')
async def portscanner(ctx, ip: str):
    await ctx.send(f'→ Started scan on {ip}(:1-443)... This may take a while.')

    open_ports = []
    for port in range(1, 443):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.001)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except socket.error:
            pass

    if open_ports:
        ports_list = ', '.join(str(port) for port in open_ports)
        await ctx.send(f'→ Scan completed. The following ports are open on {ip}: {ports_list}')
    else:
        await ctx.send(f'→ Scan completed. \nNo open ports found on {ip}')
