import os
from pyrogram import Client, filters
from pyrogram.types import *

from DewmiBot.config import get_str_key
from DewmiBot import pbot

REPO_TEXT = "**A Powerful BOT to Make Your Groups Secured and Organized ! \n\n↼ Øwñêr ⇀ : 『 @supunmabot 』\n╭──────────────\n┣─ » Python ~ 3.8.6\n┣─ » Update ~ Resently\n╰──────────────\n\n»»» @szrosebot «««"
  
BUTTONS = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("Repository", url=f"https://github.com/youtubeslgeekshow/sz-rose-bot"),
        InlineKeyboardButton("Video info ", url=f"https://www.youtube.com/channel/UCvYfJcTr8RY72dIapzMqFQA"),
      ],[
        InlineKeyboardButton("𝑺𝒍 𝑩𝒐𝒕 𝒁𝒐𝒏𝒆 ", url="https://t.me/SL_bot_zone"),
        InlineKeyboardButton("𝓢𝓛 𝓑𝓸𝓽 𝓒𝓱𝓪𝓽", url="https://t.me/slbotzone"),
      ],[
        InlineKeyboardButton("rosebot update info", url="https://t.me/szroseupdates"),
        InlineKeyboardButton("Developer", url="https://t.me/supunmabot"),
      ]]
    )
  
  
@pbot.on_message(filters.command(["repo"]))
async def repo(pbot, update):
    await update.reply_text(
        text=REPO_TEXT,
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
