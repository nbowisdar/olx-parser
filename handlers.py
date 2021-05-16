from back import show_last, X, show_all, data
from telegram.ext import *
import time
urls = []
count = 40

def set_count(x):
    global count
    count = int(x)



def start(update, context):
    update.message.reply_text('Что бы начать работу: '
                              'Укажи количество операций и  отправь мне ссылку. '
                              'Для запуска используй команду /go. '
                              'Что бы увидитеть все доступные команды используй /info')

def set_link(update, context):
    if update.message.text.isdigit():
        set_count(update.message.text)
        update.message.reply_text(f'Счетчик был обнавлен {count}')
    elif 'https://www.olx.ua' not in update.message.text:
        update.message.reply_text('Я не могу обработать эту ссылку.')
    else:
        global url
        urls.append(update.message.text)
        update.message.reply_text('Ссылка была добавленна')
        print(urls)

def work_flow(update, context):
    c = 0
    while True:
        for i in urls:
            last = show_all(i)
            if last != False:
                c += 1
                update.message.reply_text((count-c))
                update.message.reply_text(last)

        if c > count:
            update.message.reply_text(f'Было показанно {c} объявлений. Нужен перезапуск.')
            break
        time.sleep(4)



def check(update, context):
    if len(urls) == 0:
        update.message.reply_text('Список ссылок пуст.')
    for i in urls:
        update.message.reply_text(i)

def error(update, context):
    print(f'Update {update} caused error {context.error}')

def info(update, context):
    update.message.reply_text('''Доступные команды:
    
    /start - Старт
    /check - Проверить список ссылок
    /go - Начать парсинг
    /info - Посмотреть все возможные команды
    /clear - Очистить список ссылок''')

def clear(update, context):
    urls.clear()
    update.message.reply_text('Список ссылок был полностью очищен!')

