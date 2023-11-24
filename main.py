from assets import *

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=get_prefix, intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} is now running!')
    await bot.change_presence(status=discord.Status.idle)

    channel_id = 1176920698640408576
    startup_channel = bot.get_channel(channel_id)

    if startup_channel:
        await startup_channel.purge(limit=None)
        await startup_channel.send("@everyone")
        await startup_channel.send("https://tenor.com/view/mr-bean-wave-hi-gif-6019924917754082345")
    else:
        print("Could not find the specified channel for startup message.")


@bot.event
async def on_message(message):
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f'{username} said: "{user_message}" ({channel})')

    if message.author == bot.user:
        return
    if "change prefix to" in user_message:
        put_prefix(user_message[17:18])
        await message.channel.send(f"{message.author.mention} the prefix has been changed to `{get_pre()}`")

    if 'bot' in user_message:

        if any(insult in user_message for insult in br.insults):
            await message.channel.send(random.choice(br.savage_bot_replies))

        else:
            await message.channel.send(random.choice(br.bot_responses))
    if any(insult in user_message for insult in br.insults) and "bot" not in user_message:
        await message.channel.send(random.choice(br.insult_gifs))

    await bot.process_commands(message)


@bot.command(name='dm')
async def bot_command(ctx):
    response = f"I slid into your dm :wink:"
    await send_message(ctx, response=response, is_private=True)
    await ctx.message.delete()


@bot.command(name='roll')
async def roll_command(ctx, max_value: int):
    response = str(random.randint(1, max_value))
    await ctx.send(response)


@bot.command(name='walls')
async def rdwalls_command(ctx):
    file_path = f"wallpapers/{random.choice(os.listdir('wallpapers'))}"
    response = {'file': file_path}
    await ctx.send(file=discord.File(response['file']))


@bot.command(name='roast')
async def roast(ctx, person: discord.User = ""):
    if person != "":
        response = f"{person.mention} {random.choice(br.roasts)}"
        await ctx.send(response)
    else:
        response = f"{ctx.author.mention} {random.choice(br.roasts_for_missing_argument)}"
        await ctx.send(response)


@bot.command(name='annoy')
async def annoy(ctx, person: discord.User, times: int = ""):
    if times != "":
        for i in range(times):
            response = f"{person.mention}"
            await ctx.send(response)
            time.sleep(0.6)
    else:
        response = f"{ctx.author.mention} {random.choice(br.roasts_for_missing_argument)}"
        await ctx.send(response)


@bot.command(name="timer")
async def timer(ctx, value: float, what: str = ""):
    if what == "mins":
        response = f"timer set for {value} minutes"
        await ctx.send(response)
        await asyncio.sleep(value*60)

    if what == "hours":
        response = f"timer set for {value} hours"
        await ctx.send(response)
        await asyncio.sleep(value*60*60)
    if what == "secs":
        response = f"timer set for {value} seconds"
        await ctx.send(response)
        await asyncio.sleep(value)

    if what not in clock:
        response = f"{value} what? mins, hours or secs? :facepalm:"
        await ctx.send(response)
        return

    response = f"{ctx.author.mention} Time's up!"
    await ctx.send(response)