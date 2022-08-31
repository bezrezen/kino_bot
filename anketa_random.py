from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, ParseMode
from telegram.ext import ConversationHandler
import random


def anketa_random_start(update, context):
    update.message.reply_text(
        f'Вы выбрали случайный фильм. Нажмите на кнопку "Получить фильм" и подождите немного, пока его подберу', 
        reply_markup=ReplyKeyboardMarkup(
            [["Получить фильм"]], 
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )
    return 'anketa_random_result'
    
movies_list = ['Красотка','Зеленая миля','Бетмен: начало','Форрест Гамп','Перл Харбор','Храброе сердце','Девчата']


def anketa_random_result(update, context):

    random_movie = movies_list[random.randint(0,len(movies_list)-1)]
    update.message.reply_text(
        f'Ваш случайный фильм: {random_movie}. \nМожете попросить меня подобрать другой случайный фильм', 
        reply_markup=ReplyKeyboardMarkup([['Подобрать другой случайный фильм', 'Я нашел нужный фильм']], 
        one_time_keyboard=True,
        resize_keyboard=True
    )
    )
    movies_list.remove(random_movie)
    return 'final_random'


def other_random(update, context):
    
    if len(movies_list) > 0:
        other_random_movie = movies_list[random.randint(0,len(movies_list)-1)]
        update.message.reply_text(
            f'Ваш следующий рандомный фильм: {other_random_movie}',
            reply_markup=ReplyKeyboardMarkup([['Подобрать другой случайный фильм', 'Я нашел нужный фильм']], 
            one_time_keyboard=True,
            resize_keyboard=True
        )
        )
        movies_list.remove(other_random_movie)
        return 'final_random'
    else:
        update.message.reply_text(
            f'У меня закончились фильмы, вы маньяк', reply_markup=ReplyKeyboardMarkup([['Вернуться в начало']], 
            one_time_keyboard=True,
            resize_keyboard=True
        )
        )
        return ConversationHandler.END   


def final_random(update, context):

        update.message.reply_text(
            f'Рад был помочь!', reply_markup=ReplyKeyboardMarkup([['Вернуться в начало']], 
            one_time_keyboard=True,
            resize_keyboard=True
        )
        )
        return ConversationHandler.END


def anketa_dontknow_random(update, context):
    update.message.reply_text('Я вас не понимаю')
