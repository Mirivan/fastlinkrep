import requests

from userbot import CMD_HELP
from userbot.events import register

@register(pattern=r"^\.test$", outgoing=True)
async def cats(event):
    await event.edit("**Processing...**")

CMD_HELP.update(
    {
        "test_name": ">`.testplug`"
        "\nUsage: Test plugin."
    }
)
