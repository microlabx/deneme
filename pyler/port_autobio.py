#autobio for @PhycoNinja13b, Edit bio strings Amigo if u use this plugin, Or else u are cursed :)
import asyncio
import time
from telethon import events
import random, re
from telethon.tl import functions
from telethon.errors import FloodWaitError
from userbot.events import register


BIO_STRINGS = [
     "00:00 ●━━━━━━━━━ 04:18\n      ⇆ ◁ ❚❚ ▷ ↻",
     "01:17 ━━●━━━━━━━ 04:18\n      ⇆ ◁ ❚❚ ▷ ↻",
     "02:08 ━━━━●━━━━━ 04:18\n      ⇆ ◁ ❚❚ ▷ ↻",
     "02:44 ━━━━━●━━━━ 04:18\n      ⇆ ◁ ❚❚ ▷ ↻",
     "03:02 ━━━━━━●━━━ 04:18\n      ⇆ ◁ ❚❚ ▷ ↻",
     "03:52 ━━━━━━━●━━ 04:18\n      ⇆ ◁ ❚❚ ▷ ↻",
     "04:18 ━━━━━━━━━● 04:18\n      ⇆ ◁ ↻ ▷ ",

]


DEL_TIME_OUT = 120


@register(outgoing=True, pattern="^.autobio")  # pylint:disable=E0602
async def port_autobio(event):
    if event.fwd_from:
        return
    while True:
        bro = random.randint(0, len(BIO_STRINGS) - 1)
        #input_str = event.pattern_match.group(1)
        Bio = BIO_STRINGS[bro]
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%H:%M:%S")
        #bio = f"📅 {DMY} | ᗯᗩᏆᎢᏆᑎᏀ ᏞᏆᏦᗴ ᎢᏆᗰᗴ | ⌚️ {HM}"
        logger.info(Bio)
        try:
            await borg(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                about=Bio
            ))
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
        # else:
            # logger.info(r.stringify())
            # await event.client.send_message(  # pylint:disable=E0602
            #     Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
            #     "Successfully Changed Profile Bio"
            # )
        await asyncio.sleep(DEL_TIME_OUT)
