import logging
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

from anketa_parametres import (anketa_start, anketa_dontknow, genre, 
                                director, actor, other_five_movies, years, country, not_want, final_task)

from anketa_recommendations import anketa_reco_start, users_movies, final_reco, anketa_dontknow_reco, other_five_movies_reco
from anketa_random import anketa_random_start, anketa_random_result, final_random, anketa_dontknow_random, other_random
from handlers import greet_user


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher

    anketa_parametres = ConversationHandler(
    entry_points=[MessageHandler(Filters.regex('^(Подобрать по параметрам)$'), anketa_start)],
    states={
        'genre': [MessageHandler(Filters.text, genre)],
        'director': [MessageHandler(Filters.text, director)],
        'actor': [MessageHandler(Filters.text, actor)],
        'years': [MessageHandler(Filters.text, years)],
        'country': [MessageHandler(Filters.text, country)],
        'not_want': [MessageHandler(Filters.text, not_want)],
        'final_task': [
            MessageHandler(Filters.regex('^(Я нашел нужный фильм)$'), final_task), 
            MessageHandler(Filters.regex('^(Следующие 5 фильмов)$'), other_five_movies)
        ]
    },
    fallbacks=[
        MessageHandler(Filters.text | Filters.photo | Filters.video | Filters.document | Filters.location, anketa_dontknow)
    ]
    )

    anketa_recommendations = ConversationHandler(
    entry_points=[MessageHandler(Filters.regex('^(Подобрать похожий на...)$'), anketa_reco_start)],
    states={
        'user_movies': [MessageHandler(Filters.text, users_movies)],
        'final_reco': [
            MessageHandler(Filters.regex('^(Я нашел нужный фильм)$'), final_reco), 
            MessageHandler(Filters.regex('^(Другие 5 фильмов)$'), other_five_movies_reco)
        ]

    },
    fallbacks=[
        MessageHandler(Filters.text | Filters.photo | Filters.video | Filters.document | Filters.location, anketa_dontknow_reco)
    ]
    )

    anketa_random = ConversationHandler(
    entry_points=[MessageHandler(Filters.regex('^(Подобрать случайный)$'), anketa_random_start)],
    states={
        'anketa_random_result': [MessageHandler(Filters.regex('^(Получить фильм)$'), anketa_random_result)],
        'final_random': [
            MessageHandler(Filters.regex('^(Я нашел нужный фильм)$'), final_random), 
            MessageHandler(Filters.regex('^(Подобрать другой случайный фильм)$'), other_random)
        ]

    },
    fallbacks=[
        MessageHandler(Filters.text | Filters.photo | Filters.video | Filters.document | Filters.location, anketa_dontknow_random)
    ]
    )
    

    dp.add_handler(anketa_parametres)
    dp.add_handler(anketa_recommendations)
    dp.add_handler(anketa_random)
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.regex('^(Вернуться в начало)$'), greet_user))


    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
