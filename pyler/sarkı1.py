"""Emoji
Available Commands:
.sarkı1
`@ayemahmet1`"""

from telethon import events

import asyncio

from userbot.events import register

@register(outgoing=True, pattern="^.sarkı1")
async def slx(event):
    if event.fwd_from:
        return
    animation_interval = 2.5
    animation_ttl = range(0, 25)
    await event.edit("edit ByᏗᏂᎷᏋᏖ✇")
    animation_chars = [
    "haWli olma zaManı",
    "Kimseyi görmedim ben",
    "Senden daha güzel",
    "Kimseyi tanımadım ben",
    "Senden daha özel",
    "Kimselere de bakmadım",
	"Aklından geçen",
	"Kimseyi tanımadım ben",
	"Senden daha güzel",
	"Senden daha güzeeel",
	"Sana nerden rastladım",
	"Oldum derbeder",
	"Kendimi sana sakladım",
	"Senden daha güzel",
	"BİTTİ DİNLEDİNİZ İÇİN TŞQRLER :D",
]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i %25 ])
