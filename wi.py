from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
""" module by mirivan """

import logging

from .. import loader, utils

logger = logging.getLogger(__name__)

@loader.tds
class WhoIsMod(loader.Module):
    strings = {"name": "WhoIs"}
    @loader.unrestricted
    async def wicmd(self, event):
        cat = await event.edit("`сбор информации. . .`")
        if not os.path.isdir("tmp"):
            os.makedirs("tmp")
        replied_user = await get_user(event)
        try:
            photo, caption = await fetch_info(replied_user, event)
        except AttributeError:
            await event.edit("`не удалось получить информацию о пользователе.`")
            return
        message_id_to_reply = event.message.reply_to_msg_id
        if not message_id_to_reply:
            message_id_to_reply = None
        try:
            await event.client.send_file(
                event.chat_id,
                photo,
                caption=caption,
                link_preview=False,
                reply_to=message_id_to_reply,
                parse_mode="html",
            )
            if not photo.startswith("http"):
                os.remove(photo)
            await cat.delete()
        except TypeError:
            await cat.edit(caption, parse_mode="html")

async def get_user(event): 
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
    else:
        user = utils.get_args_raw(event)
        if user.isnumeric():
            user = int(user)
        if not user:
            self_user = await event.client.get_me()
            user = self_user.id
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user
        try:
            user_object = await event.client.get_entity(user)
            replied_user = await event.client(GetFullUserRequest(user_object.id))
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return replied_user

async def fetch_info(replied_user, event):
    user_id = replied_user.user.id
    first_name = replied_user.user.first_name
    last_name = replied_user.user.last_name
    username = replied_user.user.username
    user_bio = replied_user.about
    is_bot = "✓" if replied_user.user.bot else ("✖")
    verified = "✓" if replied_user.user.verified else ("✖")
    photo = await client.download_profile_photo(
        user_id, "tmp" + str(user_id) + ".jpg", download_big=True
    )
    first_name = (
        first_name.replace("\u2060", "")
        if first_name
        else ("нет имени")
    )
    last_name = last_name.replace("\u2060", "") if last_name else (" ")
    username = "@{}".format(username) if username else ("нет username")
    user_bio = "пусто" if not user_bio else user_bio
    caption = f"<b>👤 Имя:</b> {first_name} {last_name}\n"
    caption += f"<b>🤵 Username:</b> {username}\n"
    caption += f"<b>🔖 ID:</b> <code>{user_id}</code>\n"
    caption += f"<b>🤖 Бот:</b> {is_bot}\n"
    caption += f"<b>🌐 Верифицирован:</b> {verified}\n\n"
    caption += f"<b>✍️ Био:</b> \n<code>{user_bio}</code>\n\n"
    return photo, caption