# Copyright (C) 2020 Asena.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# @Qulec tarafından yazılmıştır.
import userbot
import os
import random

from userbot import CMD_HELP, SILINEN_PLUGIN, bot, tgbot
from telethon import custom, events

DOGRULUK = ["Kaç tane sevgilin oldu?", "En son ne zaman yalan söyledin?", "Telegramda nefret ettiğin bir kişinin ismini söyle.", "Bu gruptan kiminle çıkmak isterdin?"]
CESARET = ["Telegramı sil.", "Miyavlıyıp ses at", "Bağırarak şarkı söyle ve videosunu at", "Bir kişiyi engelle"]

@tgbot.on(events.NewMessage(pattern="/dogruluk"))
async def bot_dogruluk(event):
    await event.reply(random.choice(DOGRULUK))

@tgbot.on(events.NewMessage(pattern="/cesaret"))
async def bot_cesaret(event):
    await event.reply(random.choice(CESARET))
