
from telethon import events

import asyncio

from userbot.events import register

@register(outgoing=True, pattern="^.hamamtası")

async def istiklalmarsi(event):

    if event.fwd_from:

        return

    animation_interval = 2.3
    animation_ttl = range(0, 8)
    await event.edit("🇹🇷 @ayemahmet1")

    animation_chars = ['hamam tası gümüsten;', 'yeni geldin sikişten.', 'bize bunu öğreten;', 'senin yavşak enişten.', 'CETE GURURLA SUNAR',"]


    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i])
