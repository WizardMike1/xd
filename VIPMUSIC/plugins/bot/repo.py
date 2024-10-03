from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from VIPMUSIC import app
from config import BOT_USERNAME
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
✪ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ˹ ᴍᴜsɪᴄ™ ˼ ʙᴏᴛ ✪
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔𝗗𝗗 𝗠𝗘", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗦𝗨𝗣𝗣𝗢𝗥𝗧", url="https://t.me/TheBAAPx"),
          InlineKeyboardButton("𝗢𝗪𝗡𝗘𝗥", url="https://t.me/TheBAAPx"),
          ],
               [
                InlineKeyboardButton("𝗨𝗣𝗗𝗔𝗧𝗘𝗦", url="https://t.me/TheBAAPx"),

],
[
              InlineKeyboardButton("𝗠𝗨𝗦𝗜𝗖", url=f"https://t.me/TheBAAPx"),
              InlineKeyboardButton("︎𝗠𝗨𝗦𝗜𝗖", url=f"https://t.me/TheBAAPx"),

        ]]

    reply_markup = InlineKeyboardMarkup(buttons)

    await msg.reply_photo(
        photo="https://envs.sh/bJh.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
