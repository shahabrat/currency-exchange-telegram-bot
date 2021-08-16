import logging
from aiogram import Bot, Dispatcher, executor, types
import wikipedia
API_TOKEN = '#'

wikipedia.set_lang('uz')
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
     await message.reply("Salom VALYUTA KURSI botiga xush kelibsiz!\nQaysi valyutaning so'mga nisbatini bilishni xohlaysiz?")



@dp.message_handler()
async def summary(message: types.Message):
    import requests
    val = message.text
    # Where USD is the base currency you want to use
    url = f'https://v6.exchangerate-api.com/v6/fe358256c2b329fab6668a6b/pair/{val}/UZS'
    # Making our request
    response = requests.get(url)
    data = response.json()
    answer=f"1{data['base_code']} = {data['conversion_rate']} {data['target_code']}"
    await message.reply(answer)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)