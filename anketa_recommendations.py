from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, ParseMode
from telegram.ext import ConversationHandler


def anketa_reco_start(update, context):
    update.message.reply_text('Напишите названия фильмов через запятую (можно указать и одно название). \nЯ их проанализирую и подберу для вас похожие')
    return 'user_movies'

final_movie_list_reco = [
    'Красотка','Зеленая миля','Бетмен: начало','Форрест Гамп','Перл Харбор',
    'Храброе сердце','Девчата', 'Терминатор', 'Терминатор 2','Терминатор 3', 'Терминатор 4',
    'Терминатор 5', 'Терминатор 6', 'Терминатор 7', 'Терминатор 8', 'Терминатор 9'
]


def users_movies(update, context):
    context.user_data['user_movies'] = str(update.message.text).lower()
    update.message.reply_text(f'Вы ввели следующие названия: {context.user_data["user_movies"]}')
    update.message.reply_text('Дайте мне немного времени')
    update.message.reply_text(
        f'Вот ваша подборка: {final_movie_list_reco[:5]}',
        reply_markup=ReplyKeyboardMarkup(
            [['Другие 5 фильмов', 'Я нашел нужный фильм']], 
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )
    return 'final_reco'


def other_five_movies_reco(update, context):

    del final_movie_list_reco[0:5]
    if len(final_movie_list_reco) > 0:
        update.message.reply_text(
            f'Ваши следующие 5 фильмов: {final_movie_list_reco[:5]}',
            reply_markup=ReplyKeyboardMarkup(
                [['Другие 5 фильмов', 'Я нашел нужный фильм']], 
                one_time_keyboard=True,
                resize_keyboard=True
            )
        )
        return 'final_reco'
    else:
        update.message.reply_text(
            f'Фильмы, похожие на ваши, закончились, попробуйте указать другие', 
            reply_markup=ReplyKeyboardMarkup([['Вернуться в начало']], 
            one_time_keyboard=True,
            resize_keyboard=True
        )
        )
        return ConversationHandler.END  


def final_reco(update, context):
    update.message.reply_text(
        f'Рад был помочь!', 
        reply_markup=ReplyKeyboardMarkup([['Вернуться в начало']], 
        one_time_keyboard=True,
        resize_keyboard=True
    )
    )
    return ConversationHandler.END


def anketa_dontknow_reco(update, context):
    update.message.reply_text('Я вас не понимаю')
