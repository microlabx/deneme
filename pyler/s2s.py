#By ayemahmet1
from telethon import events
import asyncio
import os
import sys
from userbot.events import register

@register(outgoing=True, pattern="^.s2s")
async def s2s(event):
    if event.fwd_from:
        return
        
        
    await event.edit("ÇETE-------------varezm")
    await asyncio.sleep(1)
    await event.edit("-ÇETE------------varezm")
    await asyncio.sleep(1)
    await event.edit("--ÇETE-----------varezm")
    await asyncio.sleep(1)
    await event.edit("---ÇETE----------varezm")
    await asyncio.sleep(1)
    await event.edit("----ÇETE---------varezm")
    await asyncio.sleep(1)
    await event.edit("-----ÇETE--------varezm")
    await asyncio.sleep(1)
    await event.edit("------ÇETE-------varezm")
    await asyncio.sleep(1)
    await event.edit("-------ÇETE------varezm")
    await asyncio.sleep(1)
    await event.edit("--------ÇETE-----varezm")
    await asyncio.sleep(1)
    await event.edit("---------ÇETE----varezm")
    await asyncio.sleep(1)
    await event.edit("----------ÇETE---varezm")
    await asyncio.sleep(1)
    await event.edit("-----------ÇETE--varezm")
    await asyncio.sleep(1)
    await event.edit("------------ÇETE-varezm")
    await asyncio.sleep(1)
    await event.edit("-------------ÇETEs2Şvarezm")
	await asyncio.sleep(5)
    await event.delete()

