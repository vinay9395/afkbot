#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiAFKBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiAFKBot/blob/master/LICENSE >
#
# All rights reserved.
#

from os import getenv

from dotenv import load_dotenv

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("22243185"))
API_HASH = getenv("39d926a67155f59b722db787a23893ac")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("6818012318:AAHgCOQwJEM8s57IBLVsbbNnsHqzUCartMw")

# Database to save your chats and stats... Get MongoDB:-  https://notreallyshikhar.gitbook.io/yukkimusicbot/deployment/mongodb#4.-youll-see-a-deploy-cloud-database-option.-please-select-shared-hosting-under-free-plan-here
MONGO_DB_URI = getenv("mongodb+srv://vanshfrr:Ml6VgeE6fXVo29mw@vanshfrr.ukmgk1i.mongodb.net/?retryWrites=true&w=majority&appName=vanshfrr", None)

# SUDO USERS
SUDO_USER = list(
    map(int, getenv("5086819565", "").split())
)  # Input type must be interger
