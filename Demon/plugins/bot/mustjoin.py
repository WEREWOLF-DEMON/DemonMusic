from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from Demon import app

#--------------------------
MUST_JOIN = "WerewolfDemonUpdate"  # Channel username without @
#--------------------------

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not MUST_JOIN:
        return

    try:
        # ✅ Check if user is a member
        await app.get_chat_member(MUST_JOIN, msg.from_user.id)

    except UserNotParticipant:
        # ✅ Generate invite link
        if MUST_JOIN.isalpha():
            link = f"https://t.me/{MUST_JOIN}"
        else:
            chat_info = await app.get_chat(MUST_JOIN)
            link = chat_info.invite_link

        try:
            # ✅ Send join message
            await msg.reply_photo(
                photo="https://i.ibb.co/S7yCBSDR/must-join.jpg",
                caption=(
                    f"๏ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ, ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ ᴊᴏɪɴᴇᴅ [๏sᴜᴘᴘᴏʀᴛ๏]({link}) ʏᴇᴛ.\n\n"
                    "ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴀɴᴅ sᴛᴀʀᴛ ᴍᴇ ᴀɢᴀɪɴ!"
                ),
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("๏ Jᴏɪɴ ๏", url=link)]]
                )
            )

            # ❌ Incorrect method name in your original: `stop_DEMONpagation()` doesn't exist
            return  # Just return to stop further handling

        except ChatWriteForbidden:
            # Bot can't send messages in this chat
            pass

    except ChatAdminRequired:
        print(f"⚠️ Please promote the bot as admin in: {MUST_JOIN} to use invite links.")
