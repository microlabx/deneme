#By ayemahmet1
from telethon import events
import asyncio
import os
import sys
from userbot.events import register

@register(outgoing=True, pattern="^.yürü")
async def yürü(event):
    if event.fwd_from:
        return
        
        
    await event.edit("AHMET-------------")
    await asyncio.sleep(1)
    await event.edit("-AHMET------------")
    await asyncio.sleep(1)
    await event.edit("--AHMET-----------")
    await asyncio.sleep(1)
    await event.edit("---AHMET----------")
    await asyncio.sleep(1)
    await event.edit("----AHMET---------")
    await asyncio.sleep(1)
    await event.edit("-----AHMET--------")
    await asyncio.sleep(1)
    await event.edit("------AHMET-------")
    await asyncio.sleep(1)
    await event.edit("-------AHMET------")
    await asyncio.sleep(1)
    await event.edit("--------AHMET-----")
    await asyncio.sleep(1)
    await event.edit("---------AHMET----")
    await asyncio.sleep(1)
    await event.edit("----------AHMET---")
    await asyncio.sleep(1)
    await event.edit("-----------AHMET--")
    await asyncio.sleep(1)
    await event.edit("------------AHMET-")
    await asyncio.sleep(1)
    await event.edit("-------------AHMET")
    await asyncio.sleep(5)
    await event.delete()

