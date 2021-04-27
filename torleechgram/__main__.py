# Copyright (c) 2021 Priiiyo [priiiyo@github]
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telethon import TelegramClient
from torleechgram.core.HandleManager import add_handlers
from torleechgram.core.getVars import get_val
import logging,asyncio
from torleechgram.core.wserver import start_server_async
from torleechgram.core.status.auto_delete import del_status
from pyrogram import Client
try:
    from torleechgram.functions.rstuff import get_rstuff
except ImportError:pass

from torleechgram.tlg_client import TorlgClient

if __name__ == "__main__":

    #logging stuff
    #thread name is just kept for future use
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s"
    )
    logging.getLogger("pyrogram").setLevel(logging.ERROR)
    
    # parallel connections limiter
    queue = asyncio.Queue()
    for i in range(1,4):
        queue.put_nowait(i)

    # Telethon client creation
    tlgbot = TorlgClient("TorLeechGramBot",get_val("API_ID"),get_val("API_HASH"))
    tlgbot.queue = queue
    tlgbot.start(bot_token=get_val("BOT_TOKEN"))
    logging.info("Telethon Client created.")

    # Pyro Client creation and linking
    pyroclient = Client("pyrosession", api_id=get_val("API_ID"), api_hash=get_val("API_HASH"), bot_token=get_val("BOT_TOKEN"), workers=100)
    pyroclient.start()
    tlgbot.pyro = pyroclient
    logging.info("Pryogram Client created.")

    # Associate the handlers
    add_handlers(tlgbot)

    tlgbot.loop.create_task(del_status())

    if get_val("IS_VPS"):
        tlgbot.loop.run_until_complete(start_server_async(get_val("SERVPORT")))
    try:
        tlgbot.loop.run_until_complete(get_rstuff())
    except:pass
    
    logging.info("THE BOT IS READY TO GOOOOOOO")

    tlgbot.run_until_disconnected()
