import logging

from aiogram import Bot, Dispatcher, executor, types
from checkWord import  checkWord

API_TOKEN = '6102748847:AAH1M1rOBMXya8glFg5aelTEhaZWe423xAw'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("imlouz botiga  hush kelibsiz!")

@dp.message_handler(commands='help')
async def help_user(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("imlouz bot  so'zlarni ma'nosini ifodalaydi.so'z yuboring!")



@dp.message_handler()
async def checkImlo(message: types.Message):
    word=message.text
    result=checkWord(word)
    if result['available']:
        response=f"✅{word.capitalize()}"
    else:
        response=f"⛔{word.capitalize()}\n"
        for text  in result['matches']:
            response += f"✅{text.capitalize()}"
    await message.answer(response)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)