import random #NIKHIL SAINI BOTS
import time #NIKHIL SAINI BOTS
from vars import CREDIT #NIKHIL SAINI BOTS
from pyrogram.errors import FloodWait #NIKHIL SAINI BOTS
from datetime import timedelta #NIKHIL SAINI BOTS

class Timer: #NIKHIL SAINI BOTS
    def __init__(self, time_between=5): #NIKHIL SAINI BOTS
        self.start_time = time.time() #NIKHIL SAINI BOTS
        self.time_between = time_between #NIKHIL SAINI BOTS

    def can_send(self): #NIKHIL SAINI BOTS
        if time.time() > (self.start_time + self.time_between): #NIKHIL SAINI BOTS
            self.start_time = time.time() #NIKHIL SAINI BOTS
            return True #NIKHIL SAINI BOTS
        return False #NIKHIL SAINI BOTS

def hrb(value, digits=2, delim="", postfix=""): #NIKHIL SAINI BOTS
    if value is None: #NIKHIL SAINI BOTS
        return None #NIKHIL SAINI BOTS
    chosen_unit = "B" #NIKHIL SAINI BOTS
    for unit in ("KB", "MB", "GB", "TB"): #NIKHIL SAINI BOTS
        if value > 1000: #NIKHIL SAINI BOTS
            value /= 1024 #NIKHIL SAINI BOTS
            chosen_unit = unit #NIKHIL SAINI BOTS
        else: #NIKHIL SAINI BOTS
            break #NIKHIL SAINI BOTS
    return f"{value:.{digits}f}" + delim + chosen_unit + postfix #NIKHIL SAINI BOTS

def hrt(seconds, precision=0): #NIKHIL SAINI BOTS
    pieces = [] #NIKHIL SAINI BOTS
    value = timedelta(seconds=seconds) #NIKHIL SAINI BOTS
    if value.days: pieces.append(f"{value.days}day") #NIKHIL SAINI BOTS
    seconds = value.seconds #NIKHIL SAINI BOTS
    if seconds >= 3600: #NIKHIL SAINI BOTS
        hours = int(seconds / 3600) #NIKHIL SAINI BOTS
        pieces.append(f"{hours}hr") #NIKHIL SAINI BOTS
        seconds -= hours * 3600 #NIKHIL SAINI BOTS
    if seconds >= 60: #NIKHIL SAINI BOTS
        minutes = int(seconds / 60) #NIKHIL SAINI BOTS
        pieces.append(f"{minutes}min") #NIKHIL SAINI BOTS
        seconds -= minutes * 60 #NIKHIL SAINI BOTS
    if seconds > 0 or not pieces: #NIKHIL SAINI BOTS
        pieces.append(f"{seconds}sec") #NIKHIL SAINI BOTS
    return "".join(pieces[:precision]) if precision else "".join(pieces) #NIKHIL SAINI BOTS

timer = Timer() #NIKHIL SAINI BOTS

styles = [
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
        "complete": "🟩", "remain": "⬜",
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
    }
]

async def progress_bar(current, total, reply, start): #NIKHIL SAINI BOTS
    if timer.can_send(): #NIKHIL SAINI BOTS
        now = time.time() #NIKHIL SAINI BOTS
        diff = now - start #NIKHIL SAINI BOTS
        if diff < 1: return #NIKHIL SAINI BOTS

        perc = f"{current * 100 / total:.1f}%" #NIKHIL SAINI BOTS
        speed = current / diff if diff > 0 else 0 #NIKHIL SAINI BOTS
        eta = hrt((total - current) / speed if speed else 0, precision=1) #NIKHIL SAINI BOTS
        sp = hrb(speed) + "/s" #NIKHIL SAINI BOTS
        cur = hrb(current) #NIKHIL SAINI BOTS
        tot = hrb(total) #NIKHIL SAINI BOTS

        style = random.choice(styles) #NIKHIL SAINI BOTS
        done = int(current * 10 / total) #NIKHIL SAINI BOTS
        bar = style['complete'] * done + style['remain'] * (10 - done) #NIKHIL SAINI BOTS

        text = style['template'].format(bar=bar, perc=perc, sp=sp, cur=cur, tot=tot, eta=eta, CREDIT=CREDIT) #NIKHIL SAINI BOTS

        try:
            await reply.edit(text) #NIKHIL SAINI BOTS
        except FloodWait as e:
            time.sleep(e.x) #NIKHIL SAINI BOTS
