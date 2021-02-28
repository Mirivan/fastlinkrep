# requires: upsidedown
import logging
import upsidedown
from .. import loader, utils

logger = logging.getLogger(__name__)

@loader.tds
class ReverseMod(loader.Module):
    """Reverse"""
    strings = {"name": "Message reverser"}
    @loader.unrestricted
    async def reversecmd(self, message):
        if message.is_reply:
            txt = await message.get_reply_message()
            txt = txt.raw_text
            txt = txt[::-1]
            if len(txt) > 4096:
                await message.edit('🐺 Сообщение слишком длинное (`4096`).')
            else:
                await message.edit(txt)
        else:
            await message.edit('🐺 Перешлите сообщения с командой `.reverse` для его переворота.')
    @loader.unrestricted
    async def upsidecmd(self, message):
        if message.is_reply:
            txt = await message.get_reply_message()
            txt = txt.raw_text
            txt = upsidedown.transform(txt)
            if len(txt) > 4096:
                await message.edit('🐺 Сообщение слишком длинное (`4096`).')
            else:
                await message.edit(txt)
        else:
            await message.edit('🐺 Перешлите сообщения с командой `.upside` для его переворота.')
    @loader.unrestricted
    async def хлопcmd(self, message):
        if message.is_reply:
            txt = await message.get_reply_message()
            txt = txt.raw_text
            txt = txt.replace(' ', ' 👏 ')
            if len(txt) > 4096:
                await message.edit('🐺 Сообщение слишком длинное (`4096`).')
            else:
                await message.edit(txt)
        else:
            await message.edit('🐺 Где хлопать?')