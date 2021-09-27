# Copyright (C) 2021 TeamDaisyX


# This file is part of Daisy (Telegram Bot)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import os

import cloudmersive_virus_api_client
from telethon.tl import functions, types
from telethon.tl.types import DocumentAttributeFilename, MessageMediaDocument

from DewmiBot.config import get_str_key
from DewmiBot.events import register
from DewmiBot import telethn as tbot


async def is_register_admin(chat, user):
    if isinstance(chat, (types.InputPeerChannel, types.InputChannel)):
        return isinstance(
            (
                await tbot(functions.channels.GetParticipantRequest(chat, user))
            ).participant,
            (types.ChannelParticipantAdmin, types.ChannelParticipantCreator),
        )
    if isinstance(chat, types.InputPeerUser):
        return True


VIRUS_API_KEY = get_str_key("VIRUS_API_KEY", required=False)
configuration = cloudmersive_virus_api_client.Configuration()
configuration.api_key["Apikey"] = VIRUS_API_KEY
api_instance = cloudmersive_virus_api_client.ScanApi(
    cloudmersive_virus_api_client.ApiClient(configuration)
)
allow_executables = True
allow_invalid_files = True
allow_scripts = True
allow_password_protected_files = True


@register(pattern="^/scanit$")
async def virusscan(event):
    if event.fwd_from:
        return
    if event.is_group:
        if await is_register_admin(event.input_chat, event.message.sender_id):
            pass
        else:
            return
    if not event.reply_to_msg_id:
        await event.reply("Reply to a file to scan it.")
        return

    c = await event.get_reply_message()
    try:
        c.media.document
    except Exception:
        await event.reply("💁🏼‍♂️ This bot accepts only files.\n💬support chat👉 @slbotzone")
        return
    h = c.media
    try:
        k = h.document.attributes
    except Exception:
        await event.reply("💁🏼‍♂️ This bot accepts only files.\n💬support chat👉 @slbotzone")
        return
    if not isinstance(h, MessageMediaDocument):
        await event.reply("💁🏼‍♂️ This bot accepts only files.\n💬support chat👉 @slbotzone")
        return
    if not isinstance(k[0], DocumentAttributeFilename):
        await event.reply("💁🏼‍♂️ This bot accepts only files.\n💬support chat👉 @slbotzone")
        return
    try:
        virus = c.file.name
        await event.client.download_file(c, virus)
        gg = await event.reply("🚀 ** File initialized**.\n✅ File downloaded.\n✅ File uploaded to telegram.")
        fsize = c.file.size
        if not fsize <= 3145700:  # MAX = 3MB
            await gg.edit("🔗 This file size is not supported. File size exceeds 3MB")
            return
        api_response = api_instance.scan_file_advanced(
            c.file.name,
            allow_executables=allow_executables,
            allow_invalid_files=allow_invalid_files,
            allow_scripts=allow_scripts,
            allow_password_protected_files=allow_password_protected_files,
        )
        if api_response.clean_result is True:
            await gg.edit("This file is safe ✅\n🧬 `Detections: 0 / 57`\n[⚜️ Link to VirusTotal ](https://www.virustotal.com)\n💬support chat👉 @slbotzone")
        else:
            await gg.edit("This file is Dangerous ☠️️\nVirus detected ❌\n[⚜️ Link to VirusTotal ](https://www.virustotal.com)\n💬support chat👉 @slbotzone")
        os.remove(virus)
    except Exception as e:
        print(e)
        os.remove(virus)
        await gg.edit("Some error occurred.")
        return

__help__ = """
@szrosebot🇱🇰
 ❍ /scanit: Scan a file for virus (MAX SIZE = 3MB)
"""
__mod_name__ = "virus"
