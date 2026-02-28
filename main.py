import os
from aiogram import Bot, Dispatcher, executor, types
from yt_dlp import YoutubeDL

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(
        "🎧 NavoMir Music Bot\n"
        "Qo‘shiq nomini yozing — topib beraman 🎶"
    )

@dp.message_handler()
async def search_music(message: types.Message):
    query = message.text
    await message.answer("🔍 Qidirilyapti...")

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "music.%(ext)s",
        "quiet": True,
        "noplaylist": True,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([f"ytsearch1:{query}"])

        await message.answer_audio(
            audio=open("music.mp3", "rb"),
            caption=f"🎶 {query}"
        )

        os.remove("music.mp3")

    except:
        await message.answer("❌ Xatolik, boshqa nom bilan urinib ko‘ring")

if __name__ == "__main__":
    executor.start_polling(dp)
