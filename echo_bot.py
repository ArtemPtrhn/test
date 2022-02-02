from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, CommandHandler
from key import TOKEN


def main():
    updater = Updater(
        token=TOKEN,
        use_context=True
    )

    dispatcher = updater.dispatcher

    # создаем обработчик, который ловит все сообщения
    echo_handler = MessageHandler(Filters.all, do_echo)
    hello_handler = MessageHandler(Filters.text('Привет, привет'), say_hello)

    # регистрируем обработчик. ПОРЯДОК ВАЖЕН!
    dispatcher.add_handler(hello_handler)
    dispatcher.add_handler(echo_handler)

    updater.start_polling()
    print('Бот успешно запустился')  # Отладочная идея
    updater.idle()


def do_echo(update: Update, context: CallbackContext):
    name = update.message.from_user.first_name
    chat_id = update.message.chat_id
    text = update.message.text
    update.message.reply_text(text=f'Твой id: {id}\n'
                                   f'Ты написал: {text}\n')


def say_hello(update: Update, context: CallbackContext):
    name = update.message.from_user.first_name
    chat_id = update.message.chat_id
    text = update.message.text
    update.message.reply_text(text=f'Привет, {name}!\n'
                                   f'Приятно познакомиться с живым человеком.\n'
                                   f'Я - бот, пшел отсюда!')


if __name__ == '__main__':
    main()
