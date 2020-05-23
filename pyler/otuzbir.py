#asena
from telethon import events

import asyncio

from userbot.events import register

@register(outgoing=True, pattern="^.otuzbir")

async def otuzbir(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 12)

    await event.edit("31 Çekiorm Lna")

    animation_chars = [
        
            "8=👊====D",
            "8==👊===D",
            "8===👊==D",
            "8====👊=D",
            "8=====👊D",    
            "8====👊=D",
            "8===👊==D",
            "8==👊===D",
            "8=👊====D",
            "8👊=====D",
            "Ohh",
            "💦"

 ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 12])
