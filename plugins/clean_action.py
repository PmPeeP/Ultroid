# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available -

•`{i}addclean`
    Clean all Upcoming action msg in added chat like someone joined/left/pin etc.

•`{i}remclean`
    Remove chat from database.

•`{i}listclean`
   To get list of all chats where its activated.

"""

from pyUltroid.functions.clean_db import *

from . import *


@ultroid_bot.on(events.ChatAction())
async def _(event):
    if is_clean_added(event.chat_id):
        try:
            await event.delete()
        except BaseException:
            pass


@ultroid_cmd(pattern="addclean$")
async def _(e):
    if e.chat.admin_rights:
        add_clean(e.chat_id)
        return await eod(e, "Added Clean Action Setting For this Chat")
    return await eod(e, "`ADMIN PERMISSION REQUIRED`")


@ultroid_cmd(pattern="remclean$")
async def _(e):
    if e.chat.admin_rights:
        rem_clean(e.chat_id)
        return await eod(e, "Removed Clean Action Setting For this Chat")
    return await eod(e, "`ADMIN PERMISSION REQUIRED`")


@ultroid_cmd(pattern="listclean$")
async def _(e):
    k = udB.get("CLEANCHAT")
    if k:
        k = k.split(" ")
        o = ""
        for x in k:
            title = (await ultroid_bot.get_entity(int(x))).title
            o += x + " " + title + "\n"
        await eor(e, o)
    else:
        await eod(e, "`No Chat Added`")


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
