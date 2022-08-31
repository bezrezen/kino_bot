from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, ParseMode
from telegram.ext import ConversationHandler


def anketa_start(update, context):
    update.message.reply_text(
        f'Введите желаемый жанр, можно ввести несколько через запятую. \nНажмите кнопку "Жанр не важен", чтобы пропустить вопрос', 
        reply_markup=ReplyKeyboardMarkup([['Жанр не важен']], 
        one_time_keyboard=True, 
        resize_keyboard=True)
    )
    return 'genre'


#def movie_type(update, context):
#    type_choice = str(update.message.text)
#    context.user_data['anketa'] = {'type': type_choice.split()[1]}
#    reply_keyboard = [['Да, хочу чтобы была премия','Наличие премии не важно']]
#    update.message.reply_text(
#        f'Отлично, теперь я буду задавать тебе вопросы, которые помогут мне при подборке! \nВы можете пропустить любой вопрос, нажав на кнопку "не важно" \nВопрос №1: важно ли, чтобы у фильма или сериала была премия Оскар или Эмми?',
#        reply_markup=ReplyKeyboardMarkup(
#            reply_keyboard, 
#            one_time_keyboard=True, 
#            resize_keyboard=True
#        )
#    )
#    return 'oskar'


#def anketa_oskar(update, context):
#    oskar_choice = update.message.text
#    reply_keyboard1=[['Жанр не важен']]
#    
#    if oskar_choice == 'Да, хочу чтобы была премия':
#        context.user_data['anketa']['oskar'] = 'yes'
#        update.message.reply_text(
#            f'Введите желаемый жанр, можно ввести несколько через запятую. \nНажмите кнопку "Жанр не важен", чтобы пропустить вопрос', 
#            reply_markup=ReplyKeyboardMarkup(
#                reply_keyboard1,
#                one_time_keyboard=True, 
#                resize_keyboard=True
#            )
#        )
#        return 'genre'
#    elif oskar_choice.lower() == 'да': 
#        context.user_data['anketa']['oskar'] = 'yes'
#        update.message.reply_text(
#            f'Введите желаемый жанр, можно ввести несколько через запятую.\nНажмите кнопку "Жанр не важен", чтобы пропустить вопрос', 
#            reply_markup=ReplyKeyboardMarkup(
#                reply_keyboard1, 
#                one_time_keyboard=True, 
#                resize_keyboard=True
#            )
#        )
#        return 'genre'
    
#    elif oskar_choice == 'Наличие премии не важно':
#        context.user_data['anketa']['oskar'] = 'no'
#        update.message.reply_text(
#            f'Введите желаемый жанр, можно ввести несколько через запятую.\nНажмите кнопку "Жанр не важен", чтобы пропустить вопрос', 
#            reply_markup=ReplyKeyboardMarkup(
#                reply_keyboard1, 
#                one_time_keyboard=True, 
#                resize_keyboard=True
#            )
#        )
#        return 'genre'
    
#    elif oskar_choice.lower() == 'нет': 
#        context.user_data['anketa']['oskar'] = 'no'
#        update.message.reply_text(
#            f'Введите желаемый жанр, можно ввести несколько через запятую.\nНажмите кнопку "Жанр не важен", чтобы пропустить вопрос', 
#            reply_markup=ReplyKeyboardMarkup(
#                reply_keyboard1, 
#                one_time_keyboard=True, 
#                resize_keyboard=True
#            )
#        )
#        return 'genre'


def genre(update,context):
    genres = str(update.message.text).lower()
    genres_list=genres.split(',')
    true_genres_list=['комедия', 'детектив', 'фантастика', 'ужасы']
    x = 0
    if genres.lower() == 'жанр не важен':
        context.user_data['anketa'] = {'genre': 'not set'}
        update.message.reply_text(
            f'Укажите режиссера, можно ввести несколько через запятую.\nНажмите кнопку "Режиссер не важен", чтобы пропустить вопрос', 
            reply_markup=ReplyKeyboardMarkup(
                [['Режиссер не важен']], 
                one_time_keyboard=True, 
                resize_keyboard=True
            )
        )
        return 'director'
    else:
        for one_genre in genres_list:
            if one_genre.strip() not in true_genres_list:
                x = x + 1    
        if x > 0:
            update.message.reply_text(f'Вы ввели неизвестный мне жанр. Я знаю только такие жанры: {true_genres_list}')
            return 'genre'
        else:
            context.user_data['anketa'] = {'genre': genres_list}
            #update.message.reply_text(f'Тип: {context.user_data["anketa"]["type"]}, Премия: {context.user_data["anketa"]["oskar"]}, Жанр: {context.user_data["anketa"]["genre"]}') 
            update.message.reply_text(
                f'Укажите режиссера, можно ввести несколько через запятую.\nНажмите кнопку "Режиссер не важен", чтобы пропустить вопрос', 
                reply_markup=ReplyKeyboardMarkup(
                    [['Режиссер не важен']], 
                    one_time_keyboard=True, 
                    resize_keyboard=True
                )
            )
            return 'director'


def director(update, context):
    directors = str(update.message.text).lower()
    if directors == 'режиссер не важен':
        context.user_data['anketa']['director'] = 'not set'
        update.message.reply_text(
            f'Укажите актера, можно ввести несколько через запятую.\nНажмите кнопку "Актер не важен", чтобы пропустить вопрос', 
            reply_markup=ReplyKeyboardMarkup(
                [['Актер не важен']], 
                one_time_keyboard=True, 
                resize_keyboard=True
            )
        )
        return 'actor'
    else:
        context.user_data['anketa']['director'] = directors
        update.message.reply_text(
            f'Укажите актера, можно ввести несколько через запятую.\nНажмите кнопку "Актер не важен", чтобы пропустить вопрос', 
            reply_markup=ReplyKeyboardMarkup([['Актер не важен']], 
            one_time_keyboard=True, 
            resize_keyboard=True
        )
        ) 
        #update.message.reply_text(f'Тип: {context.user_data["anketa"]["type"]}, Премия: {context.user_data["anketa"]["oskar"]}, Жанр: {context.user_data["anketa"]["genre"]}, режиссер: {context.user_data["anketa"]["director"]}') 
        return 'actor'


def actor(update, context):
    actors = str(update.message.text).lower()
    if actors == 'актер не важен':
        context.user_data['anketa']['actor'] = 'not set'
        update.message.reply_text(
            f'Укажите год выпуска фильма, можно ввести период в несколько лет в формате "2000 - 2010" (не забудьте разделить пробелами).\nНажмите кнопку "Год выпуска не важен", чтобы пропустить вопрос', 
            reply_markup=ReplyKeyboardMarkup(
                [['Год выпуска не важен']], 
                one_time_keyboard=True, 
                resize_keyboard=True
            )
        )
        return 'years'
    else:
        context.user_data['anketa']['actor'] = actors
        update.message.reply_text(
            f'Укажите год выпуска фильма, можно ввести период в несколько лет в формате "2000 - 2010" (не забудьте разделить пробелами).\nНажмите кнопку "Год выпуска не важен", чтобы пропустить вопрос', 
            reply_markup=ReplyKeyboardMarkup(
                [['Год выпуска не важен']], 
                one_time_keyboard=True, 
                resize_keyboard=True
            )
        )
        return 'years'


def years(update, context):
    year = str(update.message.text)
    year_list = year.split()
    if year.lower() == 'год выпуска не важен':
        context.user_data['anketa']['year_start'] = 'not set'
        context.user_data['anketa']['year_finish'] = 'not set'
        update.message.reply_text(
                f'Укажите страну выпуска фильма, можно ввести несколько через запятую\nНажмите кнопку "Страна выпуска не важна", чтобы пропустить вопрос', 
                reply_markup=ReplyKeyboardMarkup(
                    [['Страна выпуска не важна']], 
                    one_time_keyboard=True, 
                    resize_keyboard=True
                )
                )
        return 'country'
    else:
        try:
            if len(year_list) > 1:
                context.user_data['anketa']['year_start'] = int(year_list[0])
                context.user_data['anketa']['year_finish'] = int(year_list[2])
                update.message.reply_text(
                f'Укажите страну выпуска фильма, можно ввести несколько через запятую\nНажмите кнопку "Страна выпуска не важна", чтобы пропустить вопрос', 
                reply_markup=ReplyKeyboardMarkup(
                    [['Страна выпуска не важна']], 
                    one_time_keyboard=True, 
                    resize_keyboard=True
                )
                )

                return 'country'
            else:
                context.user_data['anketa']['year_start'] = int(year)
                context.user_data['anketa']['year_finish'] = int(year)
                update.message.reply_text(
                f'Укажите страну выпуска фильма, можно ввести несколько через запятую\nНажмите кнопку "Страна выпуска не важна", чтобы пропустить вопрос', 
                reply_markup=ReplyKeyboardMarkup(
                    [['Страна выпуска не важна']], 
                    one_time_keyboard=True, 
                    resize_keyboard=True
                )
                )
                return 'country'
        except:
            update.message.reply_text('Вы ввели не числа, либо ввели период в неправильном формате, напоминаю формат: хххх - хххх. пробелы перед и после тире обязательны')
            return 'years'


def country(update, context):
    countries = str(update.message.text)
    countries_list = countries.split(',')
    true_countries_list_lower=['россия', 'сша', 'индия', 'франция', 'ссср']
    true_countries_list_for_user=['Россия', 'США', 'Индия', 'Франция', 'СССР']
    x = 0
    if countries.lower() == 'страна выпуска не важна':
        context.user_data['anketa']['country'] = 'not set'
        update.message.reply_text(
            f'Ну и последнее: укажите фильмы, которые бы вы не хотели видеть в предложенных.\nМожно ввести несколько через запятую \nЕсли таких фильмов нет, то нажмите на кнопку "Таких фильмов нет"', 
            reply_markup=ReplyKeyboardMarkup(
                [['Таких фильмов нет']], 
                one_time_keyboard=True, 
                resize_keyboard=True
            )
        )

        return 'not_want'
    else:
        bad_countries_list =[]
        for one_country in countries_list:
            if one_country.lower().strip() not in true_countries_list_lower:
                x = x + 1
                bad_countries_list.append(one_country)    
        if x > 0:
            update.message.reply_text(f'Фильмов из {bad_countries_list} я не знаю... \nЯ знаю фильмы из следующих стран: {true_countries_list_for_user}')
            return 'country'

        else:
            context.user_data['anketa']['country'] = countries.lower().split(',')
            update.message.reply_text(
                f"""Ну и последнее: укажите фильмы, которые бы вы не хотели видеть в предложенных.
                \nМожно ввести несколько через запятую
                \nЕсли таких фильмов нет, то нажмите на кнопку 'Таких фильмов нет'""", 
                reply_markup=ReplyKeyboardMarkup(
                    [['Таких фильмов нет']], 
                    one_time_keyboard=True, 
                    resize_keyboard=True
                )
            )

            return 'not_want'

final_movie_list = [
    'Красотка','Зеленая миля','Бетмен: начало','Форрест Гамп','Перл Харбор',
    'Храброе сердце','Девчата', 'Терминатор', 'Терминатор 2','Терминатор 3', 'Терминатор 4',
    'Терминатор 5', 'Терминатор 6', 'Терминатор 7', 'Терминатор 8', 'Терминатор 9'
]


def not_want(update, context):
    not_want_movies = update.message.text
    if not_want_movies == 'Таких фильмов нет':
        context.user_data['anketa']['not_want'] = 'not set'
    else:
        context.user_data['anketa']['not_want'] = str(update.message.text).lower()


    update.message.reply_text(
        f'Введенные параметры: \nЖанр: {context.user_data["anketa"]["genre"]}, \nРежиссер: {context.user_data["anketa"]["director"]}, \nАктер: {context.user_data["anketa"]["actor"]}, \nГоды выпуска: {context.user_data["anketa"]["year_start"]} - {context.user_data["anketa"]["year_finish"]}, \nСтрана: {context.user_data["anketa"]["country"]}, \nНе предлагать: {context.user_data["anketa"]["not_want"]}')
    update.message.reply_text('Дайте мне немного времени')
    update.message.reply_text(
        f'Вот ваша подборка: {final_movie_list[:5]}',
        reply_markup=ReplyKeyboardMarkup(
            [['Следующие 5 фильмов', 'Я нашел нужный фильм']], 
            one_time_keyboard=True, 
            resize_keyboard=True
        )
    )
    return 'final_task'


def other_five_movies(update, context):

    del final_movie_list[0:5]
    if len(final_movie_list) > 0:
        update.message.reply_text(
            f'Ваши следующие 5 фильмов: {final_movie_list[:5]}',
            reply_markup=ReplyKeyboardMarkup(
                [['Следующие 5 фильмов', 'Я нашел нужный фильм']], 
                one_time_keyboard=True, 
                resize_keyboard=True
            )
        )
        return 'final_task'
    else:
        update.message.reply_text(
            f'Фильмы, подходящие по параметрам закончились, попробуйте задать другие параметры', 
            reply_markup=ReplyKeyboardMarkup(
                [['Вернуться в начало']], 
                one_time_keyboard=True, 
                resize_keyboard=True
            )
        )
        return ConversationHandler.END   


def final_task(update, context):

    update.message.reply_text(
        f'Рад был помочь!', 
        reply_markup=ReplyKeyboardMarkup(
            [['Вернуться в начало']], 
            one_time_keyboard=True, 
            resize_keyboard=True
        )
    )
    return ConversationHandler.END
    

def anketa_dontknow(update, context):
    update.message.reply_text('Я вас не понимаю')



    


