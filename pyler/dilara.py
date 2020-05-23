# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# @ayemahmet1 tarafından portlanmıştır.

from userbot.events import register 
from userbot import CMD_HELP, bot

PENİS_TEMPLATE = """
                   .
                   ❤️ ❤️         ❤️ ❤️                       
                 ❤️      ❤️   ❤️      ❤️
                ❤️           ❤️           ❤️
                 ❤️                         ❤️
                   ❤️       DİLARA         ❤️     
                      ❤️               ❤️
                         ❤️         ❤️
                            ❤️   ❤️
                                ❤️
"""

@register(outgoing=True, pattern=r"^\.(?:dilara|dilara)\s?(.)?")
async def emoji_penis(e):
    emoji = e.pattern_match.group(1)

    await e.edit("Ahmet seni seviyor...")
    message = PENIS_TEMPLATE
    if emoji:
        message = message.replace('🍆', emoji)

    await e.edit(message)

CMD_HELP.update({
    "dilara": 
    ".dilara \
    \nKullanım: kalp yaratır :o\n"
})