import io, random
from PIL import Image, ImageFilter
from wand.image import Image as IM
""" module by mirivan """

from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="жмых ?(.*)")
async def distortdef(message):
    if message.is_reply:
        reply_message = await message.get_reply_message()
        (data, mime) = await check_media(reply_message)
        if isinstance(data, bool):
            await message.reply("🐺 Перешлите фото.")
            return
    else:
        await message.reply("🐺 Перешлите фото.")
        return
    a = message.pattern_match.group(1)
    force_file = False
    if a:
        if int(a) > 150:
            rescale_rate = 100
        else:
            rescale_rate = int(a)
    else:
        rescale_rate = random.randint(35,100)
    file = await message.client.download_media(data, bytes)
    file, img = io.BytesIO(file), io.BytesIO()
    img.name = 'img.png'
    Image.open(file).save(img, 'PNG')
    media = await distort(io.BytesIO(img.getvalue()), rescale_rate)
    out, im = io.BytesIO(), Image.open(media)
    if force_file:
        mime = 'png'
    out.name = f'out.{mime}'
    im.save(out, mime.upper())
    out.seek(0)
    await message.client.send_file(message.chat_id, out, reply_to=reply_message.id)

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

CMD_HELP.update({
    'жмых':
    '.жмых 35\
        \nUsage: Сжатие изображений.'
})