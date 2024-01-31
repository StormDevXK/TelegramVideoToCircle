from aiogram import Bot, Dispatcher, executor, types
import config
from video_edit import cut_video

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nЯ бот, с помощью которого ты сможешь преобразовать видео в кружочек!")


@dp.message_handler(content_types=['video'])
async def save_video(message: types.Message):
    file_id = message.video.file_id # Get file id
    file = await bot.get_file(file_id) # Get file path
    await bot.download_file(file.file_path, "video.mp4")
    cut_video('video.mp4', 'vid.mp4')
    vid = open('vid.mp4', 'rb')
    await bot.send_video_note(message.chat.id, vid)


@dp.message_handler()
async def echo(message: types.Message):
    # vid = open('video.mp4', 'rb')
    vid = open('vid.mp4', 'rb')
    await bot.send_video_note(message.chat.id, vid)
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
