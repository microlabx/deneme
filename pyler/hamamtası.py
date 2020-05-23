"""Emoji
Available Commands:
.hamamtası
`@ayemahmet1`"""

from telethon import events

import asyncio

from userbot.events import register

@register(outgoing=True, pattern="^.hamamtası")
async def slx(event):
    if event.fwd_from:
        return
    animation_interval = 2.5
    animation_ttl = range(0, 25)
    await event.edit("o7")
    animation_chars = [
    "Hamam tası",
    "GÜMÜŞTEN!",
    "Yeni geldim",
    "SİKİŞTEN!",
    "Bana bunu öğreten",
    "Benim yavşak Eniştem!",

]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i %25 ])
