# requires: lottie, pillow, wand
import io, os, random
from PIL import Image
from wand.image import Image as IM
""" module by mirivan """

import logging

from .. import loader, utils

logger = logging.getLogger(__name__)

@loader.tds
class FastlinkrepMod(loader.Module):
    strings = {"name": "(mirivan) FuckSticker"}

    @loader.unrestricted
    async def fascmd(self, message):
        reply = await message.get_reply_message()
        if message.is_reply:
            if reply.file and reply.file.name.endswith(".tgs"):
                await message.edit("🐺 Обработка...")
                await reply.download_media("tgs.tgs")
                os.system("lottie_convert.py tgs.tgs json.json")
                with open("json.json","r") as f: stick = f.read(); f.close()
                for i in range(1, random.randint(6, 10)):
                    stick = random.choice([stick.replace(f'[{i}]', f'[{(i+i)*7}]'),
                                                              stick.replace(f'[{i}]', f'[{(i+i)*6}]'),
                                                              stick.replace(f'[{i}]', f'[{(i+i)*5}]'),
                                                              stick.replace(f'[{i}]', f'[{(i+i)*4}]'),
                                                              stick.replace(f'[{i}]', f'[{(i+i)*3}]')])
                    with open("json.json","w") as f: f.write(stick); f.close()
                os.system("lottie_convert.py json.json tgs.tgs")
                await reply.reply(file="tgs.tgs")
                os.remove("tgs.tgs")
                os.remove("json.json")
                await message.delete()
            elif reply.file and reply.file.name.endswith(".webp"):
                await message.edit("🐺 Обработка...")
                a = utils.get_args_raw(message)
                if a:
                    if int(a) > 150:
                        rescale_rate = 100
                    else:
                        rescale_rate = int(a)
                else:
                        rescale_rate = random.randint(35,100)
                file = await message.client.download_media(reply.document, bytes)
                file, img = io.BytesIO(file), io.BytesIO()
                img.name = 'img.png'
                Image.open(file).save(img, 'PNG')
                media = await distort(io.BytesIO(img.getvalue()), rescale_rate)
                out, im = io.BytesIO(), Image.open(media)
                mime = 'webp'
                out.name = f'out.{mime}'
                im.save(out, mime.upper())
                out.seek(0)
                await message.client.send_file(message.chat_id, out, reply_to=reply.id)
                await message.delete()
            else:
                await message.edit('🐺 Перешлите стикер в любом формате.')
        else:
            await message.edit('🐺 Перешлите стикер в любом формате.')

async def distort(file, rescale_rate):
    img = IM(file=file)
    x, y = img.size[0], img.size[1]
    popx = int(rescale_rate*(x//100))
    popy = int(rescale_rate*(y//100))
    img.liquid_rescale(popx, popy, delta_x=1, rigidity=0)
    img.resize(x, y)
    out = io.BytesIO()
    out.name = f'output.png'
    img.save(file=out)
    return io.BytesIO(out.getvalue())
