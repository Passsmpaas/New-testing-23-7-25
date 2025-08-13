import random
import time
import math
import os
from vars import CREDIT
from pyrogram.errors import FloodWait
from datetime import datetime, timedelta

class Timer:
    def __init__(self, time_between=5):
        self.start_time = time.time()
        self.time_between = time_between

    def can_send(self):
        if time.time() > (self.start_time + self.time_between):
            self.start_time = time.time()
            return True
        return False

def hrb(value, digits=2, delim="", postfix=""):
    if value is None:
        return None
    chosen_unit = "B"
    for unit in ("KB", "MB", "GB", "TB"):
        if value > 1000:
            value /= 1024
            chosen_unit = unit
        else:
            break
    return f"{value:.{digits}f}" + delim + chosen_unit + postfix

def hrt(seconds, precision=0):
    pieces = []
    value = timedelta(seconds=seconds)
    if value.days:
        pieces.append(f"{value.days}day")
    seconds = value.seconds
    if seconds >= 3600:
        hours = int(seconds / 3600)
        pieces.append(f"{hours}hr")
        seconds -= hours * 3600
    if seconds >= 60:
        minutes = int(seconds / 60)
        pieces.append(f"{minutes}min")
        seconds -= minutes * 60
    if seconds > 0 or not pieces:
        pieces.append(f"{seconds}sec")
    if not precision:
        return "".join(pieces)
    return "".join(pieces[:precision])

timer = Timer()

# Sticker set
STICKERS = [
    "CAACAgUAAxkBAAEBYJtgYqLZQF7JmXYAVB_SG14LgMyVowACRgMAApK68VbA3rcuf6ZqXjAE",
    "CAACAgUAAxkBAAEBYJ9gYqLdtLZ96sKSc8F-FSHkNfpxjQAC2gsAAojEwVVZTeGvuPL3HTAE",
    "CAACAgUAAxkBAAEBYJ5gYqLa0Tf3pArwv0ooAAGG-rDq7v8AAqYRAAIY8sFVAFHdCJ3Hg-MkBA"
]

async def progress_bar(current, total, reply, start, app=None, chat_id=None):
    if timer.can_send():
        now = time.time()
        diff = now - start
        elapsed = hrt(diff, precision=2)

        if diff < 1:
            return
        perc = f"{current * 100 / total:.1f}%"
        speed = current / diff
        remaining_bytes = total - current
        eta = hrt(remaining_bytes / speed, precision=1) if speed > 0 else "-"
        sp = str(hrb(speed)) + "/s"
        tot = hrb(total)
        cur = hrb(current)
        bar_length = 10
        completed_length = int(current * bar_length / total)
        remaining_length = bar_length - completed_length
        completed_symbol, remaining_symbol = random.choice([("▪️", "▫️")])
        progress_bar = completed_symbol * completed_length + remaining_symbol * remaining_length

        try:
            await reply.edit(
                f'<blockquote>`╭──⌯═════『 STRANGER 』════⌯──╮\n'
                f'├⚡ {progress_bar}\n'
                f'├⚙️ Progress ➤ | {perc} |\n'
                f'├🚀 Speed ➤ | {sp} |\n'
                f'├📟 Processed ➤ | {cur} |\n'
                f'├🧲 Size ➤ | {tot} |\n'
                f'├⏱️ Elapsed ➤ | {elapsed} |\n'
                f'├🕑 ETA ➤ | {eta} |\n'
                f'╰─═══🦋『 STRANGER 』🦋═══─╯`</blockquote>'
            )

            # Optional sticker send
            if app and chat_id:
                sticker_id = random.choice(STICKERS)
                await app.send_sticker(chat_id, sticker_id)

        except FloodWait as e:
            time.sleep(e.x)
