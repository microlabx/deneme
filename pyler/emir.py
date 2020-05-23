from telethon import events

import asyncio

from userbot.utils import admin_cmd

@borg.on(admin_cmd("^.emir")
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 4)
    await event.edit("????????")
    animation_chars = [
            "BEN CETEEMÝR",
            "CETEDE OLMAK BÝR AYRICALIKTIR
            "SÝZDE KULLANMA ??????",
        ]

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i %5 ])