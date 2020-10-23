import discord
import random
import praw

reddit = praw.Reddit(client_id='m698iLcU-E3xAg',
                     client_secret='vlzb46Pvasjktp7O6RV3esSHKeU',
                     password="Mercedes250173",
                     user_agent='The Serbian Discord Bot',
                     username='Drywipes')

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!info'):
        await message.channel.send('My primary purpose id to help you rob rehan')
    if message.content.startswith('!hello'):
        await message.channel.send('Welcome to the Heist All Day Server')
    if message.content.startswith('!meme'):
        memes_submissions = reddit.subreddit('LaCasaDePapel').hot()
        post_to_pick = random.randint(1, 10)
        submission = "LaCasaDePapel"
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)
        await message.channel.send(submission.url)
    if message.content.startswith('!opinion'):
        if message.content.startswith('!opinion israel'):
            await message.channel.send("Israel shall reign supreme!")
        else:
            msg = message.content.split("!opinion")[1]
            await message.channel.send("Try again, " + msg + " is gay.")

client.run('NzY2NjYwMTE2Mjk2MjM3MDU4.X4ml3w.tfE9RTcRREGO9sBWJEKGTXLbxtc')