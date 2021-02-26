import random
""" module by mirivan """
from telethon.tl import functions

from datetime import datetime

import logging

from .. import loader, utils

logger = logging.getLogger(__name__)

class HentaiMod(loader.Module)
	strings = {"name": "(mirivan) Fastlinkrep"}

	@loader.unrestricted
	async def hentaicmd(self, message):
		"""Hentai image parser"""
		links = ['https://t.me/joinchat/AAAAAEkJjU8L9J6TDdkAIw', '@hentai', '@uncensored_channel']
        ch = links[random.randint(0, len(links)-1)]
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
