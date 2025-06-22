from pyrogram import filters  # Make sure this is imported
from Demon.utils.database.clonedb import is_bot_verified
from Demon import app

@app.on_message(filters.command("play"))
async def play_music(client, message):
    bot_id = (await client.get_me()).id
    if not is_bot_verified(bot_id):
        return await message.reply_text(
            "⛔ Ye cloned bot abhi verify nahi hua hai. Kripya @WerewolfDemon se verify karwaayein."
        )
    
    # Proceed with play logic here
    await message.reply_text("✅ Bot verified! Playing music...")  # Placeholder
