import random

from telegram import ParseMode
from telethon import Button

from GreyRobot import OWNER_ID, SUPPORT_CHAT
from GreyRobot import telethn as tbot

from ..events import register


@register(pattern="/feedback ?(.*)")
async def feedback(e):
    quew = e.pattern_match.group(1)
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
    GREY = (
        "https://telegra.ph/file/3a82e93893021e47d7d97.png",
        "https://telegra.ph/file/e7927a3a91041d9c533c9.png",
        "https://telegra.ph/file/4b46f79d220ff4e3951cc.png",
        "https://telegra.ph/file/497ad5ab369111b7a925f.png",
        "https://telegra.ph/file/a13cf7210472f23332bd6.png",
    )
    NATFEED = ("https://telegra.ph/file/2dd04f407b16bc2cfdf76.jpg",)
    BUTTON = [[Button.url("View Feedback ✨", f"https://t.me/{SUPPORT_CHAT}")]]
    TEXT = "Thanks For Your Feedback, I Hope You Happy With Our Service"
    GIVE = "Give Some Text For Feedback ✨"
    logger_text = f"""
**New Feedback**

**From User:** {mention}
**Username:** @{e.sender.username}
**User ID:** `{e.sender.id}`
**Feedback:** `{e.text}`
"""
    if e.sender_id != OWNER_ID and not quew:
        await e.reply(
            GIVE,
            parse_mode=ParseMode.MARKDOWN,
            buttons=BUTTON,
            file=random.choice(NATFEED),
        ),
        return

    await tbot.send_message(
        SUPPORT_CHAT,
        f"{logger_text}",
        file=random.choice(GREY),
        link_preview=False,
    )
    await e.reply(TEXT, file=random.choice(GREY), buttons=BUTTON)
