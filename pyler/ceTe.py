"""Emoji
Available Commands:
.emoji shrug
.emoji apple
.emoji :/
.emoji -_-"""

from telethon import events

import asyncio
from userbot.events import register




@register(outgoing=True, pattern="^.cetee")

async def port_hack(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 11)

    #input_str = event.pattern_match.group(1)

    #if input_str == "hack":

    await event.edit("CeTe s2şe hazırlanıyor..")

    animation_chars = [
        
            "`DiQQat varezm Cete ananı sikmeye geliyor...`",
            "`s2ş başlasın.`",
            "`varezm anan sikiliyor... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`varezm anan sikiliyor... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`varezm anan sikiliyor... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`varezm anan sikiliyor... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`varezm anan sikiliyor... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`varezm anan sikiliyor... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`varezm anan sikiliyor... 84%\n█████████████████████▒▒▒▒ `",
            "`varezm anan sikiliyor... 100%\n█████████ÇETE SİKTİ███████████ `",
            "`CETE TARAFINDAN SİKİLMİŞTİR İYİ GÜNLER`"
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 11])
