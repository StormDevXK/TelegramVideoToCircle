from aiogram import Bot, Dispatcher, types, exceptions, F
from aiogram.filters import Command
from video_edit import cut_video
from modules.settings import *
from modules.loger import log_bot
import asyncio
import time
import os

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command('start'))
async def send_welcome(message: types.Message):
    log_bot(message.chat.id, message.from_user.username, 'send_welcome', message.text)
    await bot.send_message(message.chat.id, "Привет!\nЯ бот, с помощью которого ты сможешь преобразовать видео в "
                                            "кружочек!\nПросто отправь мне видео, а я пришлю тебе результат.")
    await bot.send_message(message.chat.id, 'Для получения дополнительной информации воспользуйтесь командой /help')


@dp.message(Command('help'))
async def helps(message: types.Message):
    log_bot(message.chat.id, message.from_user.username, 'help', message.text)
    await bot.send_message(message.chat.id, "Рекомендации для входного видео:\n• Длительность видео должна быть менее "
                                            "1 минуты.\n• Размер файла не должен превышать 20 мегабайт (МБ).\n• При "
                                            "установке ширины и высоты видео увеличение размеров бесполезно, "
                                            "поскольку максимальный размер видеосообщения составляет 576 пикселей. "
                                            "Рекомендуется обрезать видео вручную, сделав его квадратным, "
                                            "перед загрузкой. Также возможно внесение изменений непосредственно в "
                                            "редакторе Telegram.\n• Рекомендуемая частота кадров - 30 кадров в "
                                            "секунду.")


@dp.message(F.video)
async def video_circle(message: types.Message):
    log_bot(message.chat.id, message.from_user.username, 'video_circle', message.text)
    file_id = message.video.file_id
    try:
        file = await bot.get_file(file_id)
        await message.reply('Идет обработка видео...')
        video_title = f'video_storage/{message.from_user.id}_{int(time.time()*100)}'
        vide = await bot.download_file(file.file_path, f'{video_title}.mp4')
        await cut_video(f'{video_title}.mp4', f'{video_title}ex.mp4')
        vid = open(f'{video_title}ex.mp4', 'rb')
        await bot.send_video_note(message.chat.id, vid)
        vide.close()
        vid.close()
        os.remove(f'{video_title}ex.mp4')
        os.remove(f'{video_title}.mp4')  # ERROR: файл не удаляется (проблема наблюдается на ОС Windows, Linux Ubuntu работает корректно)
    except Exception as ex:
        print(ex)
        await bot.send_message(message.chat.id, 'Размер файла слишком большой')


@dp.message()
async def echo(message: types.Message):
    print(f'{message.from_user.id}_{int(time.time()*100)}')
    log_bot(message.chat.id, message.from_user.username, 'echo', message.text)
    # vid = open('vid.mp4', 'rb')
    # await bot.send_video_note(message.chat.id, vid)
    await message.answer(message.text)


async def main():
    print("Бот запущен")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
