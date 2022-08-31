from telegram import ReplyKeyboardMarkup, KeyboardButton


def greet_user(update, context):
    reply_keyboard = [['Подобрать по параметрам', 'Подобрать похожий на...', 'Подобрать случайный']]
    update.message.reply_text(
        f'Привет! Я бот, который умеет подбирать фильмы. Выбери каким способом подобрать тебе фильм',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, 
            one_time_keyboard=True,
            resize_keyboard=True
        )
        )
