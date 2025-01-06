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

# Non-interactive login function
async def start_client():
    # Client ko connect karte hain
    await client.connect()

    # Check karte hain ki user already authorized hai ya nahi
    if not await client.is_user_authorized():
        # Agar authorized nahi hai, toh phone number ke liye code request karte hain
        print("Sending OTP to the phone number...")
        await client.send_code_request(phone_number)

        # OTP ko automatically handle karna
        await client.sign_in(phone_number)

# Forward message from source_channel to target_chat
@client.on(events.NewMessage(chats=source_channel))
async def forward_message(event):
    try:
        await client.send_message(target_chat, event.message.text)
        print(f"Forwarded: {event.message.text}")
    except Exception as e:
        print(f"Error: {e}")

# Start the client and handle login
client.loop.run_until_complete(start_client())

# Now start the bot after login
print("Bot is running...")
client.run_until_disconnected()
