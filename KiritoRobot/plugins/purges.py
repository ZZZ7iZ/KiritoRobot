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

import time

from telethon import Button, events

from KiritoRobot import tbot
from KiritoRobot.status import *

PR_HELP = """
**- لحذف الكثير من الرسائل داخل المجموعة!

➛ /purge - قم بالرد على رسالة لحذف الرسائل من هناك.
➛ /spurge - مثل التطهير، لكنه لا يرسل رسالة التأكيد النهائية.
➛ /del - لحذف الرد على الرسالة.**
"""


@tbot.on(events.NewMessage(pattern=r"^[?!]purge"))
@is_admin
async def purge_messages(event, perm):
    if not perm.delete_messages:
        await event.reply(
            "أنت تفتقد الحقوق التالية لاستخدام هذا الأمر : الاشراف "
        )
        return
    start = time.perf_counter()
    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.reply("قم بالرد على رسالة لتحديد المكان الذي ستبدأ منه عملية الحذف.")
        return
    messages = []
    message_id = reply_msg.id
    delete_to = event.message.id

    messages.append(event.reply_to_msg_id)
    for msg_id in range(message_id, delete_to + 1):
        messages.append(msg_id)
        if len(messages) == 100:
            await event.client.delete_messages(event.chat_id, messages)
            messages = []

    await event.client.delete_messages(event.chat_id, messages)
    time_ = time.perf_counter() - start
    text = f"Purged in {time_:0.2f} Second(s)"
    await event.respond(text, parse_mode="markdown")


@tbot.on(events.NewMessage(pattern="^[!?/]spurge"))
@is_admin
async def spurge(event, perm):
    if not perm.delete_messages:
        await event.reply(
            "أنت تفتقد الحقوق التالية لاستخدام هذا الأمر: الاشراف"
        )
        return
    time.perf_counter()
    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.reply("قم بالرد على رسالة لتحديد المكان الذي ستبدأ منه عملية الحذف.")
        return
    messages = []
    message_id = reply_msg.id
    delete_to = event.message.id

    messages.append(event.reply_to_msg_id)
    for msg_id in range(message_id, delete_to + 1):
        messages.append(msg_id)
        if len(messages) == 100:
            await event.client.delete_messages(event.chat_id, messages)
            messages = []

    await event.client.delete_messages(event.chat_id, messages)


@tbot.on(events.NewMessage(pattern="^[!?/]del$"))
@is_admin
async def delete_messages(event, perm):
    if not perm.delete_messages:
        await event.reply(
            "أنت تفتقد الحقوق التالية لاستخدام هذا الأمر: الاشراف"
        )
        return
    msg = await event.get_reply_message()
    if not msg:
        await event.reply("الرد على رسالة لحذفها.")
        return

    await msg.delete()
    await event.delete()


@tbot.on(events.callbackquery.CallbackQuery(data="purges"))
async def _(event):
    await event.edit(PR_HELP, buttons=[[Button.inline("رجوع", data="help")]])
