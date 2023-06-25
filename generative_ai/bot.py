# bot.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()

from vertexai.preview.language_models import ChatModel, InputOutputTextPair
import argparse

chat_model = ChatModel.from_pretrained("chat-bison@001")

# TODO developer - override these parameters as needed:
parameters = {
    # Temperature controls the degree of randomness in token selection.
    "temperature":  0.2,
    # Token limit determines the maximum amount of text output.
    "max_output_tokens": 256,
    # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
    "top_p": 0.95,
    # A top_k of 1 means the selected token is the most probable among all tokens.
    "top_k": 40,
}
chat = chat_model.start_chat()

TOKEN = os.getenv('DISCORD_TOKEN')


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    response = ""
    # if message.content == 'what is your name':
    if message.content.startswith("!"):
        # response = random.choice(brooklyn_99_quotes)
        response = chat.send_message(
            message.content[1:], **parameters
        )
        print(message.content)
    if response:
        await message.channel.send(response)

client.run(TOKEN)
