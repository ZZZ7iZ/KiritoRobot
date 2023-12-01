"""
BSD 2-Clause License

Copyright (c) 2022, Awesome-Prince (https://github.com/Awesome-Prince)
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from telethon import Button, events

from KiritoRobot import tbot
from KiritoRobot.status import *

LOCKS_HELP = """
** هل تزعجك الملصقات؟ أو تريد تجنب مشاركة الأشخاص للروابط؟ أو الصور؟ أنت في المكان الصحيح! **

➛ /lock - لقفل الوحده في المجموعه.
➛ /unlock - لفتح وحدة في المجموعه.
➛ /locktypes - للحصول على قائمة الوسائط ولملصقات التي يمكن قفلها**
"""


@tbot.on(events.NewMessage(pattern="^قفل$"))
@is_admin
async def lock(event, perm):
    if not perm.change_info:
        await event.reply(
            "أنت تفتقد الحقوق التالية لاستخدام هذا الأمر: الاشراف"
        )
        return
    input_str = event.pattern_match.group(1)
    if not input_str:
        await event.reply("You haven't specified anything to lock.")
        return
    if "الرسائل" in input_str:
        await tbot.edit_permissions(event.chat_id, send_messages=False)
        await event.reply("مقفل `نص`.")
    elif "وسائط" in input_str:
        await tbot.edit_permissions(event.chat_id, send_media=False)
        await event.reply("مقفل `وسائط`.")
    elif "ملصقات" in input_str:
        await tbot.edit_permissions(event.chat_id, send_stickers=False)
        await event.reply("مقفل `ملصقات`.")
    elif "صور متحركه" in input_str:
        await tbot.edit_permissions(event.chat_id, send_gifs=False)
        await event.reply("مقفل `صور متحركة`.")
    elif "forward" in input_str:
        await tbot.edit_permissions(event.chat_id, forwards=False)
        await event.reply("مقفل `إلى الأمام`.")
    elif "العاب" in input_str:
        await tbot.edit_permissions(event.chat_id, send_games=False)
        await event.reply("مقفل `ألعاب`.")
    elif "inline" in input_str:
        await tbot.edit_permissions(event.chat_id, send_inline=False)
        await event.reply("مقفل `inline`.")
    elif "استفتاء" in input_str:
        await tbot.edit_permissions(event.chat_id, send_polls=False)
        await event.reply("مقفل `استفتاء`.")
    elif "معاينة" in input_str:
        await tbot.edit_permissions(event.chat_id, embed_link_previews=False)
        await event.reply("مقفل `معاينة`.")
    elif "الكل" in input_str:
        await tbot.edit_permissions(
            event.chat_id,
            send_messages=False,
            send_media=False,
            send_stickers=False,
            send_gifs=False,
            send_games=False,
            send_inline=False,
            send_polls=False,
            embed_link_previews=False,
        )
        await event.reply("مقفل `all`.")


@tbot.on(events.NewMessage(pattern="^فتح$"))
@is_admin
async def unlock(event, perm):
    if not perm.change_info:
        await event.reply(
            "أنت تفتقد الحقوق التالية لاستخدام هذا الأمر: الاشراف"
        )
        return
    input_str = event.pattern_match.group(1)
    if not input_str:
        await event.reply("لم تقم بتحديد أي شيء لفتحه.")
        return
    if "text" in input_str:
        await tbot.edit_permissions(event.chat_id, send_messages=True)
        await event.reply("مفتوحة `الرسائل`.")
    elif "media" in input_str:
        await tbot.edit_permissions(event.chat_id, send_media=True)
        await event.reply("مفتوحة `وسائط`.")
    elif "sticker" in input_str:
        await tbot.edit_permissions(event.chat_id, send_stickers=True)
        await event.reply("مفتوحة `ملصقات`.")
    elif "gifs" in input_str:
        await tbot.edit_permissions(event.chat_id, send_gifs=True)
        await event.reply("مفتوحة `صور متحركة`.")
    elif "forward" in input_str:
        await tbot.edit_permissions(event.chat_id, forwards=True)
        await event.reply("مفتوحة `forward`.")
    elif "games" in input_str:
        await tbot.edit_permissions(event.chat_id, send_games=True)
        await event.reply("مفتوحة `العاب`.")
    elif "inline" in input_str:
        await tbot.edit_permissions(event.chat_id, send_inline=True)
        await event.reply("مفتوحة `inline`.")
    elif "polls" in input_str:
        await tbot.edit_permissions(event.chat_id, send_polls=True)
        await event.reply("مفتوحة `استفتاء`.")
    elif "preview" in input_str:
        await tbot.edit_permissions(event.chat_id, embed_link_previews=True)
        await event.reply("مفتوحة `preview`.")
    elif "all" in input_str:
        await tbot.edit_permissions(
            event.chat_id,
            send_messages=True,
            send_media=True,
            send_stickers=True,
            send_gifs=True,
            send_games=True,
            send_inline=True,
            send_polls=True,
            embed_link_previews=True,
        )
        await event.reply("مفتوحة `all`.")


@tbot.on(events.NewMessage(pattern="^اوامر الفتح ولقفل$"))
async def locktypes(event):
    TEXT = """
**قفل :**

➛ الرسائل
➛ الوسائط 
➛ ملصقات
➛ صور متحركة 
➛ مقاطع فيديو 
➛ جهات الاتصال 
➛ ألعاب 
➛ عبر الإنترنت 
➛ الكل
"""
    await event.reply(TEXT)


@tbot.on(events.callbackquery.CallbackQuery(data="locks"))
async def _(event):

    await event.edit(LOCKS_HELP, buttons=[[Button.inline("رجوع", data="help")]])
