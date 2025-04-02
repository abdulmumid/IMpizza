import time

import telebot
from telebot import types

from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = telebot.TeleBot('7778745100:AAGLYmKzkr_ezGuVxZwabW247Nem7Ss1rWI')
korzina = []
sena = 0
itogo = 0

@bot.message_handler(commands=['start'])
def start(message):
    knopki = {
        "Меню": types.KeyboardButton("Меню"),
        "Назад": types.KeyboardButton("Назад"),
        "Главная страница": types.KeyboardButton("Главная страница"),
        "Корзина": types.KeyboardButton("Корзина"),
        "Наши Филиалы": types.KeyboardButton("Наши Филиалы")
    }

    knopka = types.ReplyKeyboardMarkup(resize_keyboard=True)
    knopka.row(knopki['Меню'])
    knopka.row(knopki['Наши Филиалы'])
    knopka.row(knopki['Назад'], knopki['Главная страница'], knopki['Корзина'])
    bot.send_message(message.chat.id, f"Приветствую {message.from_user.first_name}")
    bot.send_message(message.chat.id, "Добро пожаловать! \n🍕IMperia Pizza🍕 \nСамая лучшая в Кыргызстане.",
                     reply_markup=knopka)


@bot.message_handler()
def comand(message):
    if message.text == "Меню":
        time.sleep(5)
        bot.delete_message(message.chat.id, message.message_id)
        knopka = types.InlineKeyboardMarkup()
        pizza = InlineKeyboardButton("Пицца", callback_data="pizza")
        chaurma = InlineKeyboardButton("Шаурма", callback_data="shaurma")
        hoddog = InlineKeyboardButton("Ход-Дог", callback_data="xoddog")
        disert = InlineKeyboardButton("Дисерт", callback_data="disert")
        napitki = InlineKeyboardButton("Напитки", callback_data="napitki")
        knopka.row(pizza)
        knopka.row(chaurma)
        knopka.row(hoddog)
        knopka.row(disert)
        knopka.row(napitki)
        bot.send_photo(message.chat.id, open("menu/img.png", 'rb'), "Выберите один из этих каталогов",
                       reply_markup=knopka)

    elif message.text == "Наши Филиалы":
        adres = InlineKeyboardMarkup()
        adres1 = InlineKeyboardButton("Филиалы Империя Пицца",
                                      url="https://www.google.com/maps/search/%D0%98%D0%BC%D0%BF%D0%B5%D1%80%D0%B8%D1%8F+%D0%9F%D0%B8%D1%86%D1%86%D1%8B/@42.8672086,74.5832448,13z/data=!3m1!4b1?entry=ttu&g_ep=EgoyMDI1MDMxOS4yIKXMDSoJLDEwMjExNDU1SAFQAw%3D%3D")
        adres.row(adres1)
        bot.send_photo(message.chat.id, open("menu/img.png", 'rb'),
                       "Вы можете посмотрет наши филиалы на карте", reply_markup=adres)

    elif message.text == "Главная страница":
        knopki = {
            "Меню": types.KeyboardButton("Меню"),
            "Назад": types.KeyboardButton("Назад"),
            "Главная страница": types.KeyboardButton("Главная страница"),
            "Корзина": types.KeyboardButton("Корзина"),
            "Наши Филиалы": types.KeyboardButton("Наши Филиалы")
        }

        knopka = types.ReplyKeyboardMarkup(resize_keyboard=True)
        knopka.row(knopki['Меню'])
        knopka.row(knopki['Наши Филиалы'])
        knopka.row(knopki['Назад'], knopki['Главная страница'], knopki['Корзина'])
        bot.send_message(message.chat.id,
                         "Добро пожаловать! \n🍕IMperia Pizza🍕 \nСамая лучшая в Кыргызстане.",
                         reply_markup=knopka)
    elif message.text == "Корзина":
        global sena
        global itogo
        if not korzina:
            knopki = {
                "Меню": types.KeyboardButton("Меню"),
                "Назад": types.KeyboardButton("Назад"),
                "Главная страница": types.KeyboardButton("Главная страница"),
                "Корзина": types.KeyboardButton("Корзина"),
                "Перейти к оформлению": types.KeyboardButton("Перейти к оформлению"),
                "Очистить Корзину": types.KeyboardButton("Очистить Корзину")
            }

            knopka = types.ReplyKeyboardMarkup(resize_keyboard=True)
            knopka.row(knopki['Меню'])
            knopka.row(knopki['Перейти к оформлению'])
            knopka.row(knopki['Очистить Корзину'])
            knopka.row(knopki['Назад'], knopki['Главная страница'], knopki['Корзина'])
            bot.send_message(message.chat.id, "Ваша корзина пуста", reply_markup=knopka)
        else:
            knopki = {
                "Меню": types.KeyboardButton("Меню"),
                "Назад": types.KeyboardButton("Назад"),
                "Главная страница": types.KeyboardButton("Главная страница"),
                "Корзина": types.KeyboardButton("Корзина"),
                "Перейти к оформлению": types.KeyboardButton("Перейти к оформлению"),
                "Очистить Корзину": types.KeyboardButton("Очистить Корзину")
            }

            knopka = types.ReplyKeyboardMarkup(resize_keyboard=True)
            knopka.row(knopki['Меню'])
            knopka.row(knopki['Перейти к оформлению'])
            knopka.row(knopki['Очистить Корзину'])
            knopka.row(knopki['Назад'], knopki['Главная страница'], knopki['Корзина'])
            items = "\n".join(korzina)
            bot.send_message(
                message.chat.id,
                f"Ваша корзина:\n{items}\n\nОбщая стоимость: {itogo} сом",
                reply_markup=knopka
            )

    elif message.text == "Очистить Корзину":
        korzina.clear()
        sena = 0
        bot.send_message(message.chat.id, "Ваша корзина очищина")


@bot.callback_query_handler(func=lambda callback: True)
def callback_worker(callback):
    global korzina
    global sena
    global itogo

    if callback.data == "pizza":
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        pizza = types.InlineKeyboardMarkup()
        peperoni = types.InlineKeyboardButton("Пеперони", callback_data="peperoni")
        margarita = types.InlineKeyboardButton("Маргарита", callback_data="margarita")
        sire = types.InlineKeyboardButton("Четыре Цыра", callback_data="sire")
        mysa = types.InlineKeyboardButton("Мясная", callback_data="mysa")
        rime = types.InlineKeyboardButton("Римская", callback_data="rime")
        pizza.add(peperoni, margarita, sire, mysa, rime)
        bot.send_photo(callback.message.chat.id,open("menu/pizza/peperoni.png", 'rb'), "Пицца", reply_markup=pizza)

    if callback.data == "peperoni":
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        pizza = types.InlineKeyboardMarkup()
        pizza1 = types.InlineKeyboardButton("Большая-650сом", callback_data="peperoni1")
        pizza2 = types.InlineKeyboardButton("Средьная-450сом", callback_data="peperoni2")
        pizza3 = types.InlineKeyboardButton("Маленькая-350сом", callback_data="peperoni3")
        pizza.add(pizza1, pizza2, pizza3)
        bot.send_photo(callback.message.chat.id, open("menu/pizza/peperoni.png", 'rb'), "Выберите один из этих котологов", reply_markup=pizza)
    elif callback.data == "peperoni1":
        sena += 650
        korzina.append("Пицца Пеперони большая")
        bot.send_message(callback.message.chat.id, "Ваш заказ в корзине")
    elif callback.data == "peperoni2":
        sena += 450
        korzina.append("Пицца Пеперони Средьная")
        bot.send_message(callback.message.chat.id, "Ваш заказ в корзине")
    elif callback.data == "peperoni3":
        sena += 350
        korzina.append("Пицца Пеперони Маленькая")
        bot.send_message(callback.message.chat.id, "Ваш заказ в корзине")


    if callback.data == "margarita":
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        pizza = types.InlineKeyboardMarkup()
        pizza1 = types.InlineKeyboardButton("Большая-950сом", callback_data="margarita1")
        pizza2 = types.InlineKeyboardButton("Средьная-650сом", callback_data="margarita2")
        pizza3 = types.InlineKeyboardButton("Маленькая-450сом", callback_data="margarita3")
        pizza.add(pizza1, pizza2, pizza3)
        bot.send_photo(callback.message.chat.id,open("menu/pizza/Margarita.png", 'rb'), "Выберите один из этих котологов", reply_markup=pizza)
    elif callback.data == "margarita1":
        sena += 950
        korzina.append("Пицца Маргарита большая")
        bot.send_message(callback.message.chat.id, "Ваш заказ в корзине")
    elif callback.data == "margarita2":
        sena += 650
        korzina.append("Пицца Маргарита Средьная")
        bot.send_message(callback.message.chat.id, "Ваш заказ в корзине")
    elif callback.data == "margarita3":
        sena += 450
        korzina.append("Пицца Маргарита Маленькая")
        bot.send_message(callback.message.chat.id, "Ваш заказ в корзине")



    if callback.data == "sire":
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        pizza = types.InlineKeyboardMarkup()
        pizza1 = types.InlineKeyboardButton("Большая-999сом", callback_data="sire1")
        pizza2 = types.InlineKeyboardButton("Средьная-850сом", callback_data="sire2")
        pizza3 = types.InlineKeyboardButton("Маленькая-550сом", callback_data="sire3")
        pizza.add(pizza1, pizza2, pizza3)
        bot.send_photo(callback.message.chat.id, open("menu/pizza/sira.png", 'rb'), "Выберите один из этих котологов", reply_markup=pizza)
    elif callback.data == "sire1":
        sena += 999
        korzina.append("Пицца Четыре Цыра большая")
        bot.send_message(callback.message.chat.id, "Ваш заказ в корзине")
    elif callback.data == "sire2":
        sena += 850
        korzina.append("Пицца Четыре Цыра Средьная")
        bot.send_message(callback.message.chat.id, "Ваш заказ в корзине")
    elif callback.data == "sire3":
        sena += 550
        korzina.append("Пицца Четыре Цыра Маленькая")
        bot.send_message(callback.message.chat.id, "Ваш заказ в корзине")

    if callback.data == "mysa":
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        pizza = types.InlineKeyboardMarkup()
        pizza1 = types.InlineKeyboardButton("Большая-750сом", callback_data="mysa1")
        pizza2 = types.InlineKeyboardButton("Средьная-450сом", callback_data="mysa2")
        pizza3 = types.InlineKeyboardButton("Маленькая-350сом", callback_data="mysa3")
        pizza.add(pizza1, pizza2, pizza3)
        bot.send_photo(callback.message.chat.id, open("menu/pizza/mysnay.png", 'rb'), "Выберите один из этих котологов", reply_markup=pizza)
    elif callback.data == "mysa1":
        sena += 750
        korzina.append("Пицца Римская большая")
        bot.send_message(callback.message.chat.id, "Ваш заказ в корзине")
    elif callback.data == "mysa2":
        sena += 450
        korzina.append("Пицца Римская Средьная")
        bot.send_message(callback.message.chat.id, "Ваш заказ в корзине")
    elif callback.data == "mysa3":
        sena += 350
        korzina.append("Пицца Римская Маленькая")
        bot.send_message(callback.message.chat.id, "Ваш заказ в корзине")


    if callback.data == "rime":
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        pizza = types.InlineKeyboardMarkup()
        pizza1 = types.InlineKeyboardButton("Большая-850сом", callback_data="rim1")
        pizza2 = types.InlineKeyboardButton("Средьная-650сом", callback_data="rim2")
        pizza3 = types.InlineKeyboardButton("Маленькая-450сом", callback_data="rim3")
        pizza.add(pizza1, pizza2, pizza3)
        bot.send_photo(callback.message.chat.id,open("menu/pizza/rimskay.png", 'rb'),"Выберите один из этих котологов", reply_markup=pizza)
    elif callback.data == "rim1":
        sena += 850
        korzina.append("Пицца Римская большая")
        bot.send_message(callback.message.chat.id, "Ваш заказ в корзине")
    elif callback.data == "rim2":
        sena += 650
        korzina.append("Пицца Римская Средьная")
        bot.send_message(callback.message.chat.id, "Ваш заказ в корзине")
    elif callback.data == "rim3":
        sena += 450
        korzina.append("Пицца Римская Маленькая")
        bot.send_message(callback.message.chat.id, "Ваш заказ в корзине")



    if callback.data == "shaurma":
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        shaurma = types.InlineKeyboardMarkup()
        shaurma1 = types.InlineKeyboardButton("Класическая-180сом", callback_data="shaurma1")
        shaurma2 = types.InlineKeyboardButton("Маленькая-160сом", callback_data="shaurma2")
        shaurma3 = types.InlineKeyboardButton("Запечёная-190сом", callback_data="shaurma3")
        shaurma4 = types.InlineKeyboardButton("Сырная-200сом", callback_data="shaurma4")
        shaurma.row(shaurma1, shaurma2)
        shaurma.row(shaurma3, shaurma4)
        bot.send_photo(callback.message.chat.id,open("menu/shaurma/clasika.png", 'rb'), "Шаурма", reply_markup=shaurma)

    elif callback.data == "shaurma1":
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        sena += 180
        korzina.append("Шаурма Класика")
        bot.send_photo(callback.message.chat.id, open("menu/shaurma/clasika.png"),"Ваш заказ в корзине")

    elif callback.data == "shaurma2":
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        sena += 160
        korzina.append("Шаурма Маленькая")
        bot.send_photo(callback.message.chat.id, open("menu/shaurma/malenkay.png", 'rb'), "Ваш заказ в корзине")
    elif callback.data == "shaurma3":
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        sena += 190
        korzina.append(f"Шаурма Запечёная")
        bot.send_photo(callback.message.chat.id,open("menu/shaurma/jarennay.png", 'rb'), "Ваш заказ в корзине")
    elif callback.data == "shaurma4":
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        sena += 200
        korzina.append(f"Шаурма Сырная")
        bot.send_photo(callback.message.chat.id, open("menu/shaurma/sirenay.png", 'rb'), "Ваш заказ в корзине")

    if callback.data == "xoddog":
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        xoddog = types.InlineKeyboardMarkup()
        clasika = types.InlineKeyboardButton("Класика-120сом", callback_data="clasika")
        chili = types.InlineKeyboardButton("Чили-160сом", callback_data="chili")
        korea = types.InlineKeyboardButton("Кореяская-90сом", callback_data="korea")
        gril = types.InlineKeyboardButton("Гриль-140сом", callback_data="gril")
        xoddog.row(clasika, chili)
        xoddog.row(korea, gril)
        bot.send_photo(callback.message.chat.id, open("menu/xoddog/xoddog.png", 'rb'), "Ход-дог", reply_markup=xoddog)

    elif callback.data == "clasika":
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        sena += 120
        korzina.append("Ход-дог Класика")
        bot.send_photo(callback.message.chat.id, open("menu/xoddog/clasika.png", 'rb'))
    elif callback.data == "chili":
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        sena += 160
        korzina.append("Ход-дог Чили")
        bot.send_photo(callback.message.chat.id, open("menu/xoddog/chili.png", 'rb'))
    elif callback.data == "korea":
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        sena += 90
        korzina.append("Ход-дог Корейская")
        bot.send_photo(callback.message.chat.id, open("menu/xoddog/korea.png", 'rb'))
    elif callback.data == "gril":
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        sena += 140
        korzina.append("Ход-дог Гриль")
        bot.send_photo(callback.message.chat.id, open("menu/xoddog/gril.png", 'rb'))



    if callback.data == "disert":
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        disert = types.InlineKeyboardMarkup()
        chiskeyk = types.InlineKeyboardButton("Чискейк-150сом", callback_data="chiskeyk")
        malina = types.InlineKeyboardButton("Воздушный десерт с малиной-200сом", callback_data="malina")
        ikler = types.InlineKeyboardButton("Иклеры-60сом", callback_data="ikler")
        tiramisi = types.InlineKeyboardButton("Тирамиси-120сом", callback_data="tiramisi")
        disert.row(chiskeyk)
        disert.row(malina)
        disert.row(ikler, tiramisi)
        bot.send_photo(callback.message.chat.id, open("menu/disert/chiskeyk.png", 'rb'), "Выберите Дисерт", reply_markup=disert)
    elif callback.data == "chiskeyk":
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        sena += 150
        korzina.append(f"Чискейк")
        bot.send_photo(callback.message.chat.id, open("menu/disert/chiskeyk.png", 'rb'))
    elif callback.data == "malina":
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        sena += 200
        korzina.append("Воздушный десерт с малиной")
        bot.send_photo(callback.message.chat.id, open("menu/disert/malina.png", 'rb'))
    elif callback.data == "ikler":
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        sena += 60
        korzina.append("Иклеры")
        bot.send_photo(callback.message.chat.id, open("menu/disert/ikler.png", 'rb'))
    elif callback.data == "tiramisi":
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        sena += 120
        korzina.append("Тирамиси")
        bot.send_photo(callback.message.chat.id, open("menu/disert/tiramisi.png", 'rb'))


    if callback.data == "napitki":
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        napitok = types.InlineKeyboardMarkup()
        kola = types.InlineKeyboardButton("Сок", callback_data="kola")
        coffee = types.InlineKeyboardButton("Коффе", callback_data="coffee")
        tea = types.InlineKeyboardButton("Чай", callback_data="tea")
        napitok.row(coffee)
        napitok.row(kola, tea)
        bot.send_photo(callback.message.chat.id,open("menu/napitok/cola/napitki.png", 'rb'), "Выберите один из этих котегорий", reply_markup=napitok)

    elif callback.data == "kola":
        sok = types.InlineKeyboardMarkup()
        cola = types.InlineKeyboardButton("Coca-Cola", callback_data="cola")
        pepsi = types.InlineKeyboardButton("Pepsi", callback_data="pepsi")
        lipton = types.InlineKeyboardButton("Lipton", callback_data="lipton")
        sok.row(lipton)
        sok.row(cola, pepsi)
        bot.send_photo(callback.message.chat.id, open("menu/napitok/cola/cola.png", 'rb'), "Какой сок хотите", reply_markup=sok)
    elif callback.data in ["cola", "pepsi"]:
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        litr = types.InlineKeyboardMarkup()
        litr1 = types.InlineKeyboardButton("🥤0.5 литр🥤-60сом", callback_data="litr1")
        litr2 = types.InlineKeyboardButton("🥤1 литр🥤-90сом", callback_data="litr2")
        litr3 = types.InlineKeyboardButton("🥤2 литр🥤-150сом", callback_data="litr3")
        litr.row(litr1,litr2, litr3)
        bot.send_message(callback.message.chat.id, "Выберите один этик пунктов:", reply_markup=litr)
    elif callback.data == "litr1":
        korzina.append(callback.message.message_id)
        sena += 60
        bot.send_message(callback.message.chat.id, f"Ваш заказ добавлео в корзину")
    elif callback.data == "litr2":
        korzina.append(callback.message.message_id)
        sena += 90
        bot.send_message(callback.message.chat.id, f"Ваш заказ добавлео в корзину")
    elif callback.data == "litr3":
        korzina.append(callback.message.message_id)
        sena += 150
        bot.send_message(callback.message.chat.id, f"Ваш заказ добавлео в корзину")

    elif callback.data == "lipton":
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        litr = types.InlineKeyboardMarkup()
        litr1 = types.InlineKeyboardButton("🥤0.5 литр-55сом🥤", callback_data="litr01")
        litr2 = types.InlineKeyboardButton("🥤1 литр🥤-85сом", callback_data="litr02")
        litr.row(litr1, litr2)
        bot.send_message(callback.message.chat.id, "Выберите один этик пунктов:", reply_markup=litr)
    elif callback.data == "litr01":
        sena += 55
        bot.send_message(callback.message.chat.id, f"Ваш заказ добавлео в корзину")
    elif callback.data == "litr02":
        sena += 85
        bot.send_message(callback.message.chat.id, f"Ваш заказ добавлео в корзину")




    if callback.data in ["peperoni", "margarita", "sire", "mysa", "rime",
                         "shaurma1", "shaurma2", "shaurma3","shaurma4",
                         "clasika", "chili", "korea", "gril",
                         "chiskeyk", "malina", "ikler", "tiramisi", "litr1", "litr2", "litr3", 'litr01', 'litr02',]:
        knopka = types.InlineKeyboardMarkup()
        knopka1 = types.InlineKeyboardButton("1️⃣", callback_data="knopka1")
        knopka2 = types.InlineKeyboardButton("2️⃣", callback_data="knopka2")
        knopka3 = types.InlineKeyboardButton("3️⃣", callback_data="knopka3")
        knopka4 = types.InlineKeyboardButton("4️⃣", callback_data="knopka4")
        knopka5 = types.InlineKeyboardButton("Другое", callback_data="knopka5")
        knopka.row(knopka1, knopka2)
        knopka.row(knopka5)
        knopka.row(knopka3, knopka4)
        time.sleep(2)
        bot.send_message(callback.message.chat.id, "Выберите количество", reply_markup=knopka)

    elif callback.data == "knopka1":
        sena *= 1
        itogo += sena
        sena = 0
        korzina.append(f"{'1шт':_^20}")
        bot.send_message(callback.message.chat.id, "Ваш заказ добавлен в корзину")
        time.sleep(2)
        bot.send_message(callback.message.chat.id, callback.message.message_id)
        time.sleep(2)
        bot.send_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == "knopka2":
        sena *= 2
        itogo += sena
        sena = 0
        korzina.append(f"{'2шт':_^20}")
        bot.send_message(callback.message.chat.id, "Ваш заказ добавлен в корзину")
        time.sleep(2)
        bot.send_message(callback.message.chat.id, callback.message.message_id )
    elif callback.data == "knopka3":
        sena *= 3
        itogo += sena
        sena = 0
        korzina.append(f"{'3шт':_^20}")
        bot.send_message(callback.message.chat.id, "Ваш заказ добавлен в корзину")
        time.sleep(2)
        bot.send_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == "knopka4":
        sena *= 4
        itogo += sena
        sena = 0
        korzina.append(f"{'4шт':_^20}")
        bot.send_message(callback.message.chat.id, "Ваш заказ добавлен в корзину")
        time.sleep(2)
        bot.send_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == "knopka5":
        bot.send_message(callback.message.chat.id, "Пожалуйста, напишите сколько вам нужно")
        bot.register_next_step_handler(callback.message, process_custom_quantity)
        time.sleep(2)

def process_custom_quantity(message):
    global sena, korzina

    if message.text.isdigit():
        quantity = int(message.text)
        if quantity > 0:
            sena *= quantity
            korzina.append(f"{quantity:_^20}")
            bot.send_message(message.chat.id, "Ваш заказ добавлен в корзину")
        else:
            bot.send_message(message.chat.id, "Введите число больше нуля")
            bot.register_next_step_handler(message, process_custom_quantity)
    else:
        bot.send_message(message.chat.id, "Вы ввели не число, повторите.")
        bot.register_next_step_handler(message, process_custom_quantity)

while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        print(f"Ошибка: {e}")
        time.sleep(5)

