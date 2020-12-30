#@pic_finder_mipt_bot
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
#PROXY_URL = 'socks5://89.254.200.51' # вставить здесь подходящий ip

secret_token = '1493836461:AAHYF3co7zKr3dlFnqQ79v3CWNNMqS-fpm8'  # строка вида: 123456789:ABCDEFGHJABCDEFGHJABCDEFGHJABCDEFGHJ

bot = Bot(token=secret_token)
dp = Dispatcher(bot)

 
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Приветик:)")


@dp.message_handler()
async def echo(message: types.Message):
    await message.reply("здесь должна быть какая-то соответствующая картинка")


if __name__ == '__main__':
    executor.start_polling(dp)