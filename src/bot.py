import asyncio
import logging
from io import BytesIO

import pytesseract
from PIL import Image
from aiogram import Bot, Dispatcher, executor, types

from config import BotConfig, WebAppConfig
from response_msgs import ResponseMsgs

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
loop = asyncio.get_event_loop()
bot = Bot(token=BotConfig.API_TOKEN, loop=loop)
dp = Dispatcher(bot)


async def on_startup(dp):
    """
    Called on bot startup.
    """
    await bot.set_webhook(BotConfig.WEBHOOK_URL)


async def on_shutdown(dp):
    """
    Called on bot shutdown.
    """
    await bot.delete_webhook()


@dp.message_handler(content_types=['photo'])
async def get_text_from_photo(message: types.Message):
    """
    This handler will be called when user sends a photo
    """
    # noinspection PyBroadException
    try:
        with BytesIO() as bio:
            await message.photo[-1].download(bio)
            with Image.open(bio) as image:
                text = await loop.run_in_executor(None, image_to_string, image)

        if not text.strip():
            res_msg = ResponseMsgs.EMPTY_PHOTO
        else:
            res_msg = text
    except Exception:
        res_msg = ResponseMsgs.INTERNAL_ERROR
    await message.answer(res_msg)


@dp.message_handler(commands=['about', 'contact'])
async def send_contact_details(message: types.Message):
    """
    This handler will be called when user sends `/about` or `/contact` command
    """
    await message.answer(ResponseMsgs.CONTACT)


@dp.message_handler()
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends any text messages
    """
    await message.answer(ResponseMsgs.HELP)


def image_to_string(image, lang='hye'):
    return pytesseract.image_to_string(image, lang=lang)


if __name__ == '__main__':
    executor.start_webhook(dp, '/', on_startup=on_startup, on_shutdown=on_shutdown, host='0.0.0.0',
                           port=WebAppConfig.PORT)
