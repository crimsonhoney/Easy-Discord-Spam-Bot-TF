import discord
import random
import asyncio

# Set your bot token here
TOKEN = 'YOUR_DISCORD_BOT_TOKEN'

# List of spam messages
spam_messages = [
    "Hey there! Check out this cool website: example.com",
    "Did you know that our Discord server is the best? Join now!",
    "Looking for new members to join our community! Join us today!",
    "Join our Discord server for fun events and giveaways!",
    "Spamming is bad, but not when it's for a good cause! Join us now!",
    "Have you seen our latest updates? Join our Discord server to stay informed!"
]

# Create a Discord client
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    # Check if the message is from the bot itself
    if message.author == client.user:
        return
    
    # Check if the message starts with !spam
    if message.content.startswith('!spam'):
        # Spam the channel with random messages from the spam_messages list
        for i in range(5):  # Change 5 to the desired number of messages to spam
            await message.channel.send(random.choice(spam_messages))
            await asyncio.sleep(1)  # Change 1 to adjust the delay between messages

client.run(TOKEN)
