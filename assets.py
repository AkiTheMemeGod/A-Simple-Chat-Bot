import discord
import random
import time
import os
from discord.ext import commands
import bot_replies as br
import tokens
import asyncio
clock = ["mins", "hours", "secs"]


async def send_message(ctx, response, is_private):
    try:
        if isinstance(response, dict) and 'file' in response:
            await ctx.send(file=discord.File(response['file']))
        else:
            await ctx.author.send(response) if is_private else await ctx.send(response)
    except Exception as e:
        print(e)


def get_prefix(bot, message):
    with open("prefix.txt", 'r') as file:
        prefix = file.read()
    return prefix


def get_pre():
    with open("prefix.txt", 'r') as file:
        prefix = file.read()
    return prefix


def put_prefix(arg, filepath="prefix.txt"):
    with open(filepath, 'w') as file:
        file.write(arg)


