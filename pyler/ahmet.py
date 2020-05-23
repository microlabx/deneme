"""Emoji

Available Commands:

.ahmet"""

from telethon import events

import asyncio

from userbot.events import register

@register(outgoing=True, pattern="^.ahmet")
async def port_wtf(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 5)
    await event.edit("ahmet")
    animation_chars = [
            "Aç",
            "Aç yolu",
            "Aç yolu lna",
            "Açın yolu lna bne",
            "Açın yolu lna bne geldim Selamkee"
        ]

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i %5 ])
