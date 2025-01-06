from telethon import TelegramClient, events

# Telegram API credentials
api_id = '14045006'  # Yahan apna API ID paste karein
api_hash = '56237985ec088ca7aedfbfc34d448647'  # Yahan apna API Hash paste karein

# Source (VIP Channel) and Target (Your Bot/Group)
source_channel = '@sourcetradebbl'  # VIP channel ka username ya ID
target_chat = '@bottradesystem'  # Apne bot/group ka username ya ID
phone_number = '+916350242728'

# Telegram client setup
client = TelegramClient('bot_session', api_id, api_hash)

# Client start (this will use session file and skip OTP if already authenticated)
client.start(phone=phone_number)  # This will skip OTP if session file is present

# Forward message from source_channel to target_chat
@client.on(events.NewMessage(chats=source_channel))
async def forward_message(event):
    try:
        await client.send_message(target_chat, event.message.text)
        print(f"Forwarded: {event.message.text}")
    except Exception as e:
        print(f"Error: {e}")

# Now start the bot after login
print("Bot is running...")
client.run_until_disconnected()
