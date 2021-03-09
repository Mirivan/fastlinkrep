import io
""" module by mirivan """

import logging

from .. import loader, utils

logger = logging.getLogger(__name__)

@loader.tds
class GugliMod(loader.Module):
    strings = {"name": "(mirivan) Fastlinkrep"}

    @loader.unrestricted
    async def guglicmd(self, google):
        """Gugli blyat"""
        if google.is_reply:
            reply_message = await google.get_reply_message()
        else:
            reply_message = None
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
