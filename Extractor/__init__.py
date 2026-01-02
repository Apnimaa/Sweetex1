import asyncio
import logging
import os
from pyromod import listen
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

# Create sessions directory if it doesn't exist
if not os.path.exists("sessions"):
    os.makedirs("sessions")

loop = asyncio.get_event_loop()

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.INFO,
)

app = Client(
    "Extractor",
    api_id=27433400,
    api_hash="1a286620de5ffe0a7d9b57e604293555",
    bot_token="8282655063:AAFKE7fkSPMg_nEiaV1gTKY87JK7Jgd-y7s",
    workdir="sessions",
    workers=200,
)

# Initialize pyromod attributes
app.listening = {}
app.listening_cb = {}
app.waiting_input = {}

async def info_bot():
    global BOT_ID, BOT_NAME, BOT_USERNAME
    await app.start()
    getme = await app.get_me()
    BOT_ID = getme.id
    BOT_USERNAME = getme.username
    if getme.last_name:
        BOT_NAME = getme.first_name + " " + getme.last_name
    else:
        BOT_NAME = getme.first_name

loop.run_until_complete(info_bot())


