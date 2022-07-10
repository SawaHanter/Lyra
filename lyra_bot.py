#!/usr/bin/python3
import os

import logging
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.exceptions import ValidationError
from dotenv import load_dotenv


# Configure logging
logging.basicConfig(level=logging.INFO)

# load environment variables from .env
load_dotenv()


token: str = os.getenv("token")

try:
    bot: Bot = Bot(token)
except ValidationError as e:
    logging.critical(f"Error: app was shut down [{e}]")
    raise


dp: Dispatcher = Dispatcher(bot)


async def on_startup(_):
    logging.info("app was up")


async def on_shutdown(_):
    logging.info("app was down")


@dp.message_handler()
async def echo_send(message: types.Message):
    logging.info(f"get message: {message.text}")
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
