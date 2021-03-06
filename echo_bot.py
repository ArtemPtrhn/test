from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
from key import TOKEN
from openpyxl import load_workbook
from connect_to_database import stickers, replies


def main():
    updater = Updater(
        token=TOKEN,
        use_context=True
    )

    dispatcher = updater.dispatcher

    echo_handler = MessageHandler(Filters.all, do_echo)
    text_handler = MessageHandler(Filters.text, say_smth)
    hello_handler = MessageHandler(Filters.text('Привет'), say_hello)
    murad_handler = MessageHandler(Filters.text('Мурад'), say_ahay)
    keyboard_handler = MessageHandler(Filters.text('Клавиатура'), keyboard)

    dispatcher.add_handler(murad_handler)
    dispatcher.add_handler(text_handler)
    dispatcher.add_handler(hello_handler)
    dispatcher.add_handler(keyboard_handler)
    dispatcher.add_handler(echo_handler)

    updater.start_polling()
    print('Всё чики-пуки!')
    updater.idle()


def do_echo(update: Update, context: CallbackContext):
    name = update.message.from_user.first_name
    id = update.message.chat_id
    text = update.message.text if update.message.text else "текста нет"
    sticker = update.message.sticker
    if sticker:
        sticker_id = sticker.file_id
        update.message.reply_sticker(sticker_id)
    update.message.reply_text(text=f'Твой id: {id}\n'
                                   f'Твой текст: {text}\n'
                                   f'Твой стикер: {sticker}')


def say_hello(update: Update, context: CallbackContext):
    name = update.message.from_user.first_name
    id = update.message.chat_id
    text = update.message.text
    update.message.reply_text(text=f'Здарова, {name}!\n'
                                   f'Приятно познакомиться с живым человеком!\n'
                                   f'Я - бот!')


def say_ahay(update: Update, context: CallbackContext):
    text = update.message.text
    update.message.reply_text(text=f'Ахай!')


def say_smth(update: Update, context: CallbackContext):
    name = update.message.from_user.first_name
    text = update.message.text
    for keyword in stickers:
        if keyword in text:
            update.message.reply_sticker(stickers[keyword])
            update.message.reply_text(replies[keyword].format(name))
            break
    else:
        do_echo(update, context)


def keyboard(update: Update, context: CallbackContext):
    buttons = [
        ['1','2','3'],
        ['привет','пока']
    ]
    keys = ReplyKeyboardMarkup(
        buttons
    )

    update.message.reply_text(
        text='Смотри! У тебя появилась клавиатура',
        reply_markup=ReplyKeyboardMarkup(
            buttons,
            resize_keyboard=True,
            # one_time_keyboard=True

        )
    )


if __name__ == '__main__':
    main()
