import base64
import os

# Render secret se session file ko decode karen
session_base64 = os.getenv('SESSION_FILE')

# Base64 decode karen
session_data = base64.b64decode(session_base64)

# Session file ko disk par save karen
with open('bot_session.session', 'wb') as session_file:
    session_file.write(session_data)

# Telegram client setup
from telethon import TelegramClient, events

api_id = '14045006'  # Your API ID
api_hash = '56237985ec088ca7aedfbfc34d448647'  # Your API Hash

client = TelegramClient('bot_session', api_id, api_hash)

# Client ko start karen, ye session file ko use karega
client.start()

# Forward messages from source channel to target chat
@client.on(events.NewMessage(chats='@sourcetradebbl'))
async def forward_message(event):
    try:
        await client.send_message('@bottradesystem', event.message.text)
        print(f"Forwarded: {event.message.text}")
    except Exception as e:
        print(f"Error: {e}")

client.run_until_disconnected()
