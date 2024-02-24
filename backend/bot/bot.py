import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from config import BOT_KEY
from aiogram.types.web_app_info import WebAppInfo
from aiogram.dispatcher.filters import Text, Command
from aiogram.contrib.middlewares.logging import LoggingMiddleware

# types.ContentType.AUDIO
# from aiogram.utils.exceptions
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=BOT_KEY)
# Диспетчер
dp = Dispatcher(bot=bot)
dp.middleware.setup(LoggingMiddleware())


# @dp.message_handler(Text(equals='s'))
# @dp.message_handler(content_types=[types.ContentType.AUDIO])
# @dp.message_handler(commands=)

@dp.message_handler()
async def start(message: types.Message):
    text = (
        f'Добро пожаловать в DonorSearch App!\nИспользуйте наше приложение для записи на донацию, отслеживания срочных запросов на кровь, просмотра журнала и многого другого')
    website_url1 = 'https://shorturl.at/eprEL'
    url_help_project = 'https://donorsearch.org/donate/'


    keyboard = types.InlineKeyboardMarkup()
    handler_button0 = types.InlineKeyboardButton(text='🩸Мои донации', callback_data='my_donations')
    handler_button1 = types.InlineKeyboardButton(text='📌Cдать кровь', callback_data='donate_blood')
    handler_button2 = types.InlineKeyboardButton(text='💌Журнал и события', callback_data='magazine')
    handler_button3 = types.InlineKeyboardButton(text='💸Помощь проекту', web_app=WebAppInfo(url=url_help_project))
    handler_button4 = types.InlineKeyboardButton(text='👤Mой профиль', callback_data='profile')
    keyboard.row(handler_button0, handler_button1)
    keyboard.row(handler_button2, handler_button3)
    keyboard.row(handler_button4)
    await message.answer(text=text, reply_markup=keyboard)


#


@dp.callback_query_handler(text='my_donations')
async def my_donations(callback: types.CallbackQuery):
    text = (
        f'Регистрируйте здесь свои благотворительные поступки, добавляйте фото, планируйте будущие донорские акции, получайте информацию для подготовки и отслеживайте свой статус.')
    website_url1 = 'https://shorturl.at/eprEL'
    url4 = 'https://shorturl.at/eprEL'
    url0 = 'https://shorturl.at/fJY15'

    keyboard = types.InlineKeyboardMarkup()
    handler_button0 = types.InlineKeyboardButton(text='🩸Добавить донацию', web_app=WebAppInfo(url=url0))
    handler_button1 = types.InlineKeyboardButton(text='📅Запланировать донацию', web_app=WebAppInfo(url=url0))
    handler_button2 = types.InlineKeyboardButton(text='✏️Редактировать донацию', web_app=WebAppInfo(url=website_url1))
    handler_button3 = types.InlineKeyboardButton(text='🏆Рейтинг доноров', web_app=WebAppInfo(url=website_url1))
    handler_button4 = types.InlineKeyboardButton(text='🔖Памятка донора', callback_data='send_photo')
    keyboard.row(handler_button0)
    keyboard.row(handler_button1)
    keyboard.row(handler_button2)

    keyboard.row(handler_button3, handler_button4)

    await callback.message.answer(text=text, reply_markup=keyboard)


@dp.callback_query_handler(text='donate_blood')
async def donate_blood(callback: types.CallbackQuery):
    text = (
        f'Регистрируйте здесь свои благотворительные поступки, добавляйте фото, планируйте будущие донорские акции, получайте информацию для подготовки и отслеживайте свой статус.')
    website_url1 = 'https://shorturl.at/eprEL'
    url4 = 'https://shorturl.at/eprEL'
    url0 = 'https://shorturl.at/fJY15'
    url_centers_blood = 'https://donorsearch.org/bloodstations/sankt-peterburg/'

    keyboard = types.InlineKeyboardMarkup()
    handler_button0 = types.InlineKeyboardButton(text='🏥Центры крови', web_app=WebAppInfo(url=url_centers_blood))
    handler_button1 = types.InlineKeyboardButton(text='🚨Срочные заявки', callback_data='null')
    handler_button2 = types.InlineKeyboardButton(text='🔖Памятка донора', callback_data='send_photo')

    keyboard.row(handler_button0, handler_button1)
    keyboard.row(handler_button2)
    await callback.message.answer(text=text, reply_markup=keyboard)


@dp.callback_query_handler(text='magazine')
async def magazine_and_events(callback: types.CallbackQuery):
    text = (
        f'Регистрируйте здесь свои благотворительные поступки, добавляйте фото, планируйте будущие донорские акции, получайте информацию для подготовки и отслеживайте свой статус.')

    url_states = 'https://journal.donorsearch.org/?utm_source=header&utm_medium=ds&utm_campaign=donor_search'
    url_projects = 'https://unity.donorsearch.org/'
    keyboard = types.InlineKeyboardMarkup()
    handler_button0 = types.InlineKeyboardButton(text='🎮Игры', callback_data='null')
    handler_button1 = types.InlineKeyboardButton(text='📄Статьи', web_app=WebAppInfo(url=url_states))
    handler_button2 = types.InlineKeyboardButton(text='⭐️️Спецпроекты', web_app=WebAppInfo(url=url_projects))

    keyboard.row(handler_button0, handler_button1)
    keyboard.row(handler_button2)
    await callback.message.answer(text=text, reply_markup=keyboard)


# @dp.callback_query_handler(text='profile')
# async def profile(callback: types.CallbackQuery):
#     text = (
#         f'Регистрируйте здесь свои благотворительные поступки, добавляйте фото, планируйте будущие донорские акции, получайте информацию для подготовки и отслеживайте свой статус.')
#     website_url1 = 'https://shorturl.at/eprEL'
#     url0 = 'https://shorturl.at/fJY15'
#
#     keyboard = types.InlineKeyboardMarkup()
#     handler_button0 = types.InlineKeyboardButton(text='🎮Игры', web_app=WebAppInfo(url=url0))
#     handler_button1 = types.InlineKeyboardButton(text='📄Статьи', web_app=WebAppInfo(url=url0))
#     handler_button2 = types.InlineKeyboardButton(text='⭐️️Спецпроекты', web_app=WebAppInfo(url=website_url1))
#
#     keyboard.row(handler_button0, handler_button1)
#     keyboard.row(handler_button2)
#     await callback.message.answer(text=text, reply_markup=keyboard)


@dp.callback_query_handler(text='profile')
async def profile(callback: types.CallbackQuery):
    text = (
        f'Зарегистрируйтесь в DonorSearch или проверьте свой статус Почетного донора. Узнайте о бонусах для доноров и посмотрите топ-100 доноров.')
    website_url1 = 'https://shorturl.at/eprEL'
    url_signin = 'https://shorturl.at/ioz18'
    url_bonus ='https://shorturl.at/fAPRT'
    url0 = 'https://shorturl.at/fJY15'

    keyboard = types.InlineKeyboardMarkup()
    handler_button0 = types.InlineKeyboardButton(text='🎖Статус почетного донора', callback_data='null')
    handler_button1 = types.InlineKeyboardButton(text='👤Вход или регистрация', web_app=WebAppInfo(url=url_signin))
    handler_button2 = types.InlineKeyboardButton(text='🎁Бонусы',
                                                 web_app=WebAppInfo(url=url_bonus))
    handler_button3 = types.InlineKeyboardButton(text='🏆Рейтинг доноров', web_app=WebAppInfo(url=website_url1))

    keyboard.row(handler_button0)
    keyboard.row(handler_button1)
    keyboard.row(handler_button2, handler_button3)
    await callback.message.answer(text=text, reply_markup=keyboard)


#
# @dp.callback_query_handler(text='send_photo')
# async def profile(callback: types.CallbackQuery):
#
#     await bot.send_photo(chat_id=callback.message.chat.id,
#                          photo='https://avatars.mds.yandex.net/i?id=c39b4a72a7e6228d38bf87fbe5744f6084ec8773-9052192-images-thumbs&n=13')
#     await bot.send_photo(chat_id=callback.message.chat.id,
#                          photo='https://avatars.mds.yandex.net/i?id=c39b4a72a7e6228d38bf87fbe5744f6084ec8773-9052192-images-thumbs&n=13')

async def send_local_photo(chat_id, photo_path):
    with open(photo_path, 'rb') as photo:
        photo_data = types.InputFile(photo)
        await bot.send_photo(chat_id, photo=photo_data)


@dp.callback_query_handler(text='send_photo')
async def profile(callback: types.CallbackQuery):
    await send_local_photo(chat_id=callback.message.chat.id, photo_path=f'./files/one.jpg')
    await send_local_photo(chat_id=callback.message.chat.id, photo_path=f'./files/two.jpg')
    await send_local_photo(chat_id=callback.message.chat.id, photo_path=f'./files/three.jpg')


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
