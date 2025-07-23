import random
import time
from vars import CREDIT
from pyrogram.errors import FloodWait
from datetime import timedelta

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
    if value.days: pieces.append(f"{value.days}day")
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
    return "".join(pieces[:precision]) if precision else "".join(pieces)

timer = Timer()
sent_stickers = {}  # Used to ensure only 1 sticker per chat

styles = [  # [.. shortened for brevity .. include your full styles list here ..]
    {
        "complete": "🟩", "remain": "⬜",
        "template": "<code>╭──⬇️ 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 ══╮\n🔋 [{bar}]\n📈 {perc} | 🚀 {sp}\n📦 {cur}/{tot}\n⏳ ETA: {eta}\n╰── {CREDIT}</code>"
    },
    {
        "complete": "🟦", "remain": "⬜",
        "template": "<b>📥 Download Stats</b>\n[{bar}]\n✔ {perc} | ⚡ {sp} | 📤 {cur}/{tot} | ⏱️ {eta}"
    },
    {
        "complete": "🟩", "remain": "⬛",
        "template": "🔄 <b>Progress Update</b>:\n➤ {bar} {perc}\n➤ Speed: {sp}\n➤ Done: {cur} of {tot}\n➤ ETA: {eta}"
    },
    {
        "complete": "🟥", "remain": "⬜",
        "template": "[ {bar} ]\n*Progress:* {perc}\n*Speed:* {sp}\n*Size:* {cur}/{tot}\n*ETA:* {eta}"
    },
    {
        "complete": "🔰", "remain": "⚪",
        "template": "🇮🇳 <b>Bharatiya Stats</b>\n{bar}\n📊 Pragati: {perc}\n⚡ Raftar: {sp}\n🗃 Aakar: {cur}/{tot}\n🕐 Samay: {eta}"
    },
    {
        "complete": "◾️", "remain": "◽️",
        "template": "<code>╭──⬇️ 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 ══╮\n🔋 [{bar}]\n📈 {perc} | 🚀 {sp}\n📦 {cur}/{tot}\n⏳ ETA: {eta}\n╰── {CREDIT}</code>"
    },
    {
        "complete": "💠", "remain": "🤖",
        "template": "<b>📥 Download Stats</b>\n[{bar}]\n✔ {perc} | ⚡ {sp} | 📤 {cur}/{tot} | ⏱️ {eta}"
    },
    {
        "complete": "🟩", "remain": "⬛",
        "template": "🔄 <b>Progress Update</b>:\n➤ {bar} {perc}\n➤ Speed: {sp}\n➤ Done: {cur} of {tot}\n➤ ETA: {eta}"
    },
    {
        "complete": "🟥", "remain": "⬜",
        "template": "[ {bar} ]\n*Progress:* {perc}\n*Speed:* {sp}\n*Size:* {cur}/{tot}\n*ETA:* {eta}"
    },
    {
        "complete": "🤖", "remain": "👝",
        "template": "🇮🇳 <b> STRANGER INDIAN</b>\n{bar}\n📊 Pragati: {perc}\n⚡ Raftar: {sp}\n🗃 Aakar: {cur}/{tot}\n🕐 Samay: {eta}"
    },
    {
        "complete": "■", "remain": "·",
        "template": "[DOWNLOADING]\n[{bar}]\nPROGRESS: {perc} | SPEED: {sp}\nSIZE: {cur}/{tot} | ETA: {eta}"
    },
    # NEW STYLES BELOW
    {
        "complete": "🔵", "remain": "⚪",
        "template": "<b>🚀 Upload In Progress</b>\n[{bar}]\n✅ {perc}\n📤 Uploaded: {cur}/{tot}\n🕒 Time Left: {eta}"
    },
    {
        "complete": "🟫", "remain": "⬜",
        "template": "💠 <b>Data Transfer:</b>\n┌ {bar} ┐\n├ 📶 {perc} | 💾 {sp}\n├ 📁 {cur}/{tot}\n└ 🕐 ETA: {eta}"
    },
    {
        "complete": "🟪", "remain": "⬛",
        "template": "<i>📊 Transfer Report</i>\n⏩ {bar} {perc}\n📡 Speed: {sp}\n📦 Done: {cur}/{tot}\n⏳ ETA: {eta}"
    },
    {
        "complete": "🌕", "remain": "🌑",
        "template": "🌗 <b>Moonlight Progress</b>\n[{bar}]\n🔺 {perc} | 🌠 {sp}\n📘 {cur}/{tot} | ⌛ {eta}"
    },
    {
        "complete": "🧿", "remain": "🔘",
        "template": "<code>💾 Loading Data...</code>\n[{bar}]\n✔ {perc} | 🌀 {sp}\n📂 {cur}/{tot} | ⏲️ {eta}"
    },
    {
        "complete": "⣿", "remain": "⠿",
        "template": "<b>🧠 Neural Sync</b>\n{bar}\n🎯 {perc} | ⚙️ {sp}\n📉 {cur}/{tot} | 🧭 ETA: {eta}"
    },
    {
        "complete": "■", "remain": "·",
        "template": "[DOWNLOADING]\n[{bar}]\nPROGRESS: {perc} | SPEED: {sp}\nSIZE: {cur}/{tot} | ETA: {eta}"
    },
    {
        "complete": "🟥", "remain": "⬜",
        "template": "[ {bar} ]\n*Progress:* {perc}\n*Speed:* {sp}\n*Size:* {cur}/{tot}\n*ETA:* {eta}"
    },
    {
        "complete": "🤖", "remain": "👝",
        "template": "🇮🇳 <b> STRANGER INDIAN</b>\n{bar}\n📊 Pragati: {perc}\n⚡ Raftar: {sp}\n🗃 Aakar: {cur}/{tot}\n🕐 Samay: {eta}"
    },
    # Add the rest of your styles here as you originally provided...
]

async def progress_bar(current, total, reply, start):
    if timer.can_send():
        now = time.time()
        diff = now - start
        if diff < 1:
            return

        # Send sticker only once per chat before progress updates
        chat_id = reply.chat.id
        if chat_id not in sent_stickers:
            try:
                await reply.reply_sticker("CAACAgUAAxkBAAEEV6Rlm9ss-VKRz8RE0WQbEO0f_qBRaQAC-wEAAj-V0Vafeyu3RxiIzzQE")
                sent_stickers[chat_id] = True
            except Exception as e:
                print("❌ Sticker send failed:", e)

        perc = f"{current * 100 / total:.1f}%"
        speed = current / diff if diff > 0 else 0
        eta = hrt((total - current) / speed if speed else 0, precision=1)
        sp = hrb(speed) + "/s"
        cur = hrb(current)
        tot = hrb(total)

        style = random.choice(styles)
        done = int(current * 10 / total)
        bar = style['complete'] * done + style['remain'] * (10 - done)

        text = style['template'].format(
            bar=bar, perc=perc, sp=sp, cur=cur, tot=tot, eta=eta, CREDIT=CREDIT
        )

        try:
            await reply.edit(text)
        except FloodWait as e:
            time.sleep(e.x)
