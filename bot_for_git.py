# Бот выводит на экран в виде кнопок
# города-столицы областей России, виды товара, затем
# запрашивает у пользователя сделать выбор вида, нажав
# соответсвующую кнопку товара из предложенного списка;
# после выбора, возвращает на экран товары выбранного вида
# с ценами в виде кнопок, затем запрашивает у пользователя
# выбор конкретного товара; запрашивает у пользователя адрес
# доставки; возвращает номер заказа, указанный адрес доставки
# и реквизиты для оплаты; выводит инструкцию для пользователя
# для совершения оплаты; запрашивает у пользователя номер
# платёжки/поручения об оплате товара, если номер платежки
# введён выводит на экран "спасибо за заказ"
# иначе "ошибка"; данные о совершённом заказе выгружает
# в файл эксель. Информацию о службе поддержки вписать в приветсвенные сообщения.

# импортируем библиотеки
import random

from xlwt import Workbook

import telebot

# вводим токен
bot = telebot.TeleBot('___')

# делаем списки и словари, куда вносим товары по виду и номенклатуре и цены
types_of_furnt = ['Стулья', 'Столы']
types_of_goods = ['Стул барокко, 279 р.', 'Стул рококо, 283 р.', 'Стол барокко, 283 р.', 'Стол рококо, 283 р.']
recive_payments = 'VISA 3842 3462 3342 2345'
cities_list = ["Москва", "Санкт-Петербург", "Барнаул"]
furnit_catal = {types_of_furnt[0]: [{types_of_goods[0]: 279}, {types_of_goods[1]: 283}],
                types_of_furnt[1]: [{types_of_goods[2]: 283}, {types_of_goods[3]: 283}]}
cart = []
casher = []
order_num = random.randint(1, 10001)


# делаем кнопки
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    keyboard_cities = telebot.types.InlineKeyboardMarkup()
    callback_button1 = telebot.types.InlineKeyboardButton(text=cities_list[0], callback_data='1')
    callback_button2 = telebot.types.InlineKeyboardButton(text=cities_list[1], callback_data='2')
    callback_button3 = telebot.types.InlineKeyboardButton(text=cities_list[2], callback_data='3')
    # пустая кнопка для оператора
    callback_button4 = telebot.types.InlineKeyboardButton(text='Оператор техподдержки', url='https://www.google.ru/')
    keyboard_cities.add(callback_button1, callback_button2, callback_button3, callback_button4)
    bot.send_message(message.chat.id, "Здравствуйте! Добро пожаловать в наш магазин!"
                                      "Пожалуйста, выберете город:", reply_markup=keyboard_cities)


# делаем функции для работы с данными, получаемыми от нажатия кнопок, каждый кнопке присвоен
# уникальный код, соответственно под каждый товар нужно делать кнопку
@bot.callback_query_handler(func=lambda call: True)
def callback_query_1(call):
    if call.data == '1':
        keyboard_furn = telebot.types.InlineKeyboardMarkup()
        callback_button_1f = telebot.types.InlineKeyboardButton(text='Стулья', callback_data='4')
        callback_button_2f = telebot.types.InlineKeyboardButton(text='Столы', callback_data='5')
        keyboard_furn.add(callback_button_1f, callback_button_2f)
        bot.send_message(call.message.chat.id, f'Вы выбрали город {cities_list[0]}. '
                                               f'Какой тип мебели вы хотите посмотреть?', reply_markup=keyboard_furn)
    elif call.data == '2':
        keyboard_furn = telebot.types.InlineKeyboardMarkup()
        callback_button_1f = telebot.types.InlineKeyboardButton(text='Стулья', callback_data='4')
        callback_button_2f = telebot.types.InlineKeyboardButton(text='Столы', callback_data='5')
        keyboard_furn.add(callback_button_1f, callback_button_2f)
        bot.send_message(call.message.chat.id, f'Вы выбрали город {cities_list[1]}. '
                                               f'Какой тип мебели вы хотите посмотреть?', reply_markup=keyboard_furn)
    elif call.data == '3':
        keyboard_furn = telebot.types.InlineKeyboardMarkup()
        callback_button_1f = telebot.types.InlineKeyboardButton(text='Стулья', callback_data='4')
        callback_button_2f = telebot.types.InlineKeyboardButton(text='Столы', callback_data='5')
        keyboard_furn.add(callback_button_1f, callback_button_2f)
        bot.send_message(call.message.chat.id, f'Вы выбрали город {cities_list[2]}. '
                                               f'Какой тип мебели вы хотите посмотреть?', reply_markup=keyboard_furn)

    elif call.data == '4':
        keyboard_furn_1 = telebot.types.InlineKeyboardMarkup()
        callback_button_1f_1 = telebot.types.InlineKeyboardButton(text=types_of_goods[0], callback_data='6')
        callback_button_2f_1 = telebot.types.InlineKeyboardButton(text=types_of_goods[1], callback_data='7')
        keyboard_furn_1.add(callback_button_1f_1, callback_button_2f_1)
        bot.send_message(call.message.chat.id, f'Вы выбрали {types_of_furnt[0]}. '
                                               f'Выберете товар. Кликнете по нему, чтобы добавить в корзину.',
                         reply_markup=keyboard_furn_1)
    elif call.data == '5':
        keyboard_furn_2 = telebot.types.InlineKeyboardMarkup()
        callback_button_1f_2 = telebot.types.InlineKeyboardButton(text=types_of_goods[2], callback_data='8')
        callback_button_2f_2 = telebot.types.InlineKeyboardButton(text=types_of_goods[3], callback_data='9')
        keyboard_furn_2.add(callback_button_1f_2, callback_button_2f_2)
        bot.send_message(call.message.chat.id, f'Вы выбрали {types_of_furnt[1]}. '
                                               f'Выберете товар. Кликнете по нему, чтобы добавить в корзину.',
                         reply_markup=keyboard_furn_2)

    elif call.data == '6':
        keyboard_cash = telebot.types.InlineKeyboardMarkup()
        callback_button_cash_on_1 = telebot.types.InlineKeyboardButton(text="Оформить заказ", callback_data='123')
        callback_button_cash_on_2 = telebot.types.InlineKeyboardButton(text="Очистить корзину заказов",
                                                                       callback_data='234')
        keyboard_cash.add(callback_button_cash_on_1, callback_button_cash_on_2)
        cart.append(types_of_goods[0])
        casher.append(furnit_catal[types_of_furnt[0]][0][types_of_goods[0]])
        casher_sum = sum(casher)
        bot.send_message(call.message.chat.id, f'Вы выбрали товар.'
                                               f'Общая сумма заказа {casher_sum} руб. Нажмите "Оформить заказ", чтобы '
                                               f'перейти к методу оплаты, '
                                               f' или кнопку "Очистить корзину заказов", чтобы удалить все заказы',
                         reply_markup=keyboard_cash)
    elif call.data == '7':
        keyboard_cash = telebot.types.InlineKeyboardMarkup()
        callback_button_cash_on_1 = telebot.types.InlineKeyboardButton(text="Оформить заказ", callback_data='123')
        callback_button_cash_on_2 = telebot.types.InlineKeyboardButton(text="Очистить корзину заказов",
                                                                       callback_data='234')
        keyboard_cash.add(callback_button_cash_on_1, callback_button_cash_on_2)
        cart.append(types_of_goods[1])
        casher.append(furnit_catal[types_of_furnt[0]][1][types_of_goods[1]])
        casher_sum = sum(casher)
        bot.send_message(call.message.chat.id, f'Вы выбрали товар.'
                                               f'Общая сумма заказа {casher_sum} руб. Нажмите "Оформить заказ", чтобы '
                                               f'перейти к методу оплаты, '
                                               f' или кнопку "Очистить корзину заказов", чтобы удалить все заказы',
                         reply_markup=keyboard_cash)
    elif call.data == '8':
        keyboard_cash = telebot.types.InlineKeyboardMarkup()
        callback_button_cash_on_1 = telebot.types.InlineKeyboardButton(text="Оформить заказ", callback_data='123')
        callback_button_cash_on_2 = telebot.types.InlineKeyboardButton(text="Очистить корзину заказов",
                                                                       callback_data='234')
        keyboard_cash.add(callback_button_cash_on_1, callback_button_cash_on_2)
        cart.append(types_of_goods[2])
        casher.append(furnit_catal[types_of_furnt[1]][0][types_of_goods[2]])
        casher_sum = sum(casher)
        bot.send_message(call.message.chat.id, f'Вы выбрали товар.'
                                               f'Общая сумма заказа {casher_sum} руб. Нажмите "Оформить заказ", чтобы '
                                               f'перейти к методу оплаты, '
                                               f' или кнопку "Очистить корзину заказов", чтобы удалить все заказы',
                         reply_markup=keyboard_cash)

    elif call.data == '9':
        keyboard_cash = telebot.types.InlineKeyboardMarkup()
        callback_button_cash_on_1 = telebot.types.InlineKeyboardButton(text="Оформить заказ", callback_data='123')
        callback_button_cash_on_2 = telebot.types.InlineKeyboardButton(text="Очистить корзину заказов",
                                                                       callback_data='234')
        keyboard_cash.add(callback_button_cash_on_1, callback_button_cash_on_2)
        cart.append(types_of_goods[3])
        casher.append(furnit_catal[types_of_furnt[1]][1][types_of_goods[3]])
        casher_sum = sum(casher)
        bot.send_message(call.message.chat.id, f'Вы выбрали товар.'
                                               f'Общая сумма заказа {casher_sum} руб. Нажмите "Оформить заказ", чтобы '
                                               f'перейти к методу оплаты, '
                                               f' или кнопку "Очистить корзину заказов", чтобы удалить все заказы',
                         reply_markup=keyboard_cash)
    # кнопки для работы с оформлеием и "отменой"
    elif call.data == '234':
        casher.clear()
        cart.clear()
        bot.send_message(call.message.chat.id, f'Корзина заказов пуста ')

    elif call.data == '123':
        casher_sum = sum(casher)
        bot.send_message(call.message.chat.id, f'Вот ваш список заказов {cart}, '
                                               f'на общую сумму {casher_sum} руб. Номер вашего заказа {order_num}. '
                                               f'Для осуществления оплаты произведите перевод суммы по '
                                               f'реквизитам: {recive_payments}'
                                               f' Введите ваш номер телефона, адрес доставки и номер чека об '
                                               f'оплате/платёжного поручения ')


# функция для приёма тектовых сообщений, вбирает в себя данные по адресу, номеру телефона и платёжке
@bot.message_handler(content_types=['text'])
def get_data(message):
    payment_data = message.text
    bot.send_message(message.chat.id, f'Ваш номер телефона, адрес и номер чека об оплате {payment_data}. ')
    bot.send_message(message.chat.id, f'Благодарим за покупку! Оператор перезвонит вам для уточнения деталей.'
                                      f' Срок доставки уточните у оператора')
    # сохраняем заказы в файле эксель в папке с кодом,
    # можно директорию поменять по желанию с помощью функции wb.save
    # wb = Workbook()
    # sheet1 = wb.add_sheet('Orders')
    # sheet1.write(0, 0, 'Order Number')
    # sheet1.write(0, 1, 'Cart')
    # sheet1.write(0, 2, 'Cash')
    # sheet1.write(0, 3, 'Details')
    # sheet1.write(1, 0, order_num)
    # sheet1.write(1, 1, cart)
    # sheet1.write(1, 2, casher)
    # sheet1.write(1, 3, payment_data)
    # wb.save('orders.xls')


bot.polling()
