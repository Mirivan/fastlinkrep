import random
""" module by mirivan """
from telethon.tl import functions

from datetime import datetime

from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="\.aniart")
async def _(ani):
    ch = '@module_aniart'
    al = int((await ani.client.get_messages(ch, limit=0)).total)
    result = await ani.client(functions.messages.GetHistoryRequest(
        peer=ch,
        offset_id=0,
        add_offset=random.randint(0, al),
        offset_date=datetime.now(),
        limit=1,
        max_id=0,
        min_id=0,
        hash=0
    ))
    await ani.delete()
    await ani.client.send_message(ani.chat_id, result.messages[0])

    if BOTLOG:
        await purg.client.send_message(
            BOTLOG_CHATID,
            "Parsed message from "+ch+" by aniart module!")
    await sleep(2)
    await done.delete()

CMD_HELP.update({
    'aniart':
    '.aniart\
        \nUsage: Parse random Anime ASCII Art from AniArt Module💕 channel.'
})
