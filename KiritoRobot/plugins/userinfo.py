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
from telethon.tl.functions.photos import GetUserPhotosRequest as P
from telethon.tl.functions.users import GetFullUserRequest

from KiritoRobot import tbot

USERINFO_HELP = """
**- للأوامر الصغيرة والبسيطة التي لا تناسب أي مكان.

➛ /id - للحصول على معرف الدردشة الحالي أو معرف المستخدم الذي تم الرد عليه.
➛ /info - للحصول على معلومات المستخدم.**
"""


@tbot.on(events.NewMessage(pattern="^[!?/]id"))
async def id(event):

    if event.is_private:
        await event.reply(f"هويتك هي `{event.sender_id}`.")
        return

    ID = """
**ايدي المجموعه :** `{}`
**ايدي المستخدم :** `{}`
"""

    msg = await event.get_reply_message()
    if not msg:
        await event.reply(ID.format(event.chat_id, event.sender_id))
        return

    await event.reply(f"User {msg.sender.first_name} id is `{msg.sender_id}`.")


@tbot.on(events.NewMessage(pattern="^[!?/]info ?(.*)"))
async def info(event):

    sed = await tbot(P(user_id=event.sender_id, offset=42, max_id=0, limit=80))
    hn = await tbot(GetFullUserRequest(event.sender_id))
    text = "**╒═══「 نتائج التقييم : 」**\n\n"
    text += "**➛ الاسم الأول :** {}\n"
    text += "**➛ اسم العائلة :** {}\n"
    text += "**➛ الايدي :** `{}`\n"
    text += "**➛ اسم المستخدم :** @{}\n"
    text += "**➛ النبذه :** `{}`\n"
    text += "**➛ حسابك :** [Link](tg://user?id={})\n"

    input_str = event.pattern_match.group(1)
    if not input_str:
        await tbot.send_message(
            event.chat_id,
            text.format(
                hn.user.first_name,
                hn.user.last_name,
                event.sender_id,
                event.sender.username,
                sed.count,
                hn.about,
                event.sender_id,
            ),
        )
        return

    input_str = event.pattern_match.group(1)
    ha = await tbot.get_entity(input_str)
    hu = await tbot(GetFullUserRequest(id=input_str))
    sedd = await tbot(P(user_id=input_str, offset=42, max_id=0, limit=80))

    text += "**╒═══「 نتائج التقييم : 」**\n\n"
    text += "**➛ الاسم الأول :** {}\n"
    text += "**➛ اسم العائلة :** {}\n"
    text += "**➛ الايدي :** `{}`\n"
    text += "**➛ اسم المستخدم :** @{}\n"
    text += "**➛ النبذه :** `{}`\n"
    text += "**➛ حسابك :** [Link](tg://user?id={})\n"

    await event.reply(
        textn.format(
            ha.first_name, ha.last_name, ha.id, ha.username, sedd.count, hu.about, ha.id
        )
    )


@tbot.on(events.callbackquery.CallbackQuery(data="userinfo"))
async def _(event):
    await event.edit(USERINFO_HELP, buttons=[[Button.inline("رجوع", data="help")]])
