import io, urllib
""" module by mirivan """

import logging

from .. import loader, utils

logger = logging.getLogger(__name__)

@loader.tds
class GugliMod(loader.Module):
    strings = {"name": "Gugli"}

    @loader.unrestricted
    async def guglicmd(self, google):
        """Gugli blyat"""
        reply_message = None
        if google.is_reply:
            reply_message = await google.get_reply_message()
        url = "https://github.com/Mirivan/fastlinkrep/raw/main/google.jpg"
        file = get(url)
        if not file.ok:
            await google.edit("🐺 File doesn't exist.")
            return
        file = io.BytesIO(file.content)
        file.name = "google.jpg"
        file.seek(0)
        await google.delete()
        await google.client.send_message(google.chat_id,
            file=file,
            reply_to=reply_message)
    async def ggencmd(self, msg):
        pattern = utils.get_args_raw(msg)
        reply = await msg.get_reply_message()
        if pattern: text = pattern
        elif msg.is_reply: text = reply.text
        else: await msg.edit('🦈 **Необходим паттерн.**'); return
        url = urllib.parse.quote_plus(text)
        await msg.edit(f'🦈 [Google](google.com/search?q={url}) **<-**',
                                     link_preview=False)
