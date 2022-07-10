import os

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv


# load environment variables from .env
load_dotenv()


token: str = os.getenv("token")
if not token:
    print("Error: token not found")

bot: Bot = Bot(token)
dp: Dispatcher = Dispatcher(bot)


async def on_startup(_):
    print("я прокинулась")


async def on_shutdown(_):
    print("я спати")


@dp.message_handler()
async def echo_send(message: types.Message):
    if message.text == "БООДЯЯЯ":
        await message.answer("ПЕГАСИК")
    if message.text == "спокс":
        await message.reply("і тобі, лапко")
    if message.text == "доброго ранку, сонечки":
        await message.reply("і тобі, лапко")


# 	await bot.send_message(message.from_user.id, message.text)

executor.start_polling(
    dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown
)
