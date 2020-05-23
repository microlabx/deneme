"""Emoji
Available Commands:
.emoji shrug
.emoji apple
.emoji :/
.emoji -_-"""

from telethon import events

import asyncio
from userbot.events import register




@register(outgoing=True, pattern="^.ahmt")

async def port_hack(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 11)

    #input_str = event.pattern_match.group(1)

    #if input_str == "ahmt":

    await event.edit("Ahmet s2şe hazırlanıyor DiQat..")

    animation_chars = [
        
            "`Açın arayı Ahmet geldi...`",
            "`Ahmet s2şe hazır.`",
            "`S2ş başladı... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`S2ş devam ediyor... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Daha başlarında... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Ahmet dur durak bilmiyordu... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`S2ş tüm hızıyla devam ediyordu... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Ahmet S2şin ortalarındaydı... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Bi rahatlama sesi geldi... 84%\n█████████████████████▒▒▒▒ `",
            "`S2Ş BİTTİ... 100%\n█████████Ahmet Sikti Ohh███████████ `",
            "`Sizde böyle bir temiz S2ş istiyorsanız @ayemahmet1 Ulaşınız :d..`"
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 11])
