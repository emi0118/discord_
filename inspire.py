from class_bot import bot


import discord


import os
import random


@bot.command()
async def inspire(ctx):
    # List of motivational quotes
    quotes = [
        "This meme is so relatable!!",
        "trying to understand!",
        "The only limit is your mind.",
        "ordinary things can be very complicated!",
        "The best time for a new beginning is now."
    ]

    # Choose a random image and quote
    img_name = random.choice(os.listdir('images'))
    quote = random.choice(quotes)

    # Open and send the image
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)

    # Send the image with the quote
    await ctx.send(file=picture, content=quote)