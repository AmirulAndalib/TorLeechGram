# Copyright (c) 2021 Priiiyo [priiiyo@github]
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__version__ = "0.2.4"
__author__ = "Priiiyo Github@priiiyo"

import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s",
    handlers=[logging.StreamHandler(),logging.FileHandler("torlog.txt")]
)

from torleechgram.core.wserver import start_server
from .core.database_handle import TlgUpload,TorLeechGramDB,TlgTorrents, UserDB
from .core.varholdern import VarHolder
import time

logging.info("Database created")
upload_db = TlgUpload()
var_db = TorLeechGramDB()
tor_db = TlgTorrents()
user_db = UserDB()

uptime = time.time()
to_del = []
SessionVars = VarHolder(var_db)
