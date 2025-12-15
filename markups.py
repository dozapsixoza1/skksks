from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, message, KeyboardButton, ReplyKeyboardMarkup


# Клавиатура главная ---------------------------------------------------
button_menu = KeyboardButton('📓 Меню')
button_settings = KeyboardButton('👤 Профиль')
button_que = KeyboardButton('❓Задать вопрос')
button_guide = KeyboardButton('✅ Купить')
alarm = KeyboardButton('🥶 Alarm-система')
button_donate = KeyboardButton('🎊 Поддержать')
menu_b = ReplyKeyboardMarkup(resize_keyboard=True).add(button_menu,button_settings,button_que,button_guide,alarm,button_donate)
# --------------------------------------------------------------
# Клавиатура меню ---------------------------------------------
email = KeyboardButton('📧 Почта')
phone = KeyboardButton('☎ Номер телефона')
db = KeyboardButton('🗄 Базы данных')
tg = KeyboardButton('💎 Telegram')
ip = KeyboardButton('🌐 IP-адрес')
nick = KeyboardButton('🧧 Никнейм')
main = KeyboardButton('🏠 Главная')
menu_m = ReplyKeyboardMarkup(resize_keyboard=True).add(email,phone,db,tg,nick,ip,main)
# --------------------------------------------------------------
# Telegram -----------------------------------------------------
check_ch = KeyboardButton('🔧 Чекер каналов')
pwned = KeyboardButton('🗃 Утечка')
main = KeyboardButton('🏠 Главная')
menu_tg = ReplyKeyboardMarkup(resize_keyboard=True).add(pwned,main)
# ------------------------------------------------

# Проверка
urlch = InlineKeyboardButton(text='ПОДПИСАТЬСЯ', url='https://t.me/visiiione')
checkch = InlineKeyboardButton(text='✅ Я подписался', callback_data='subchanneldone')
subchanneldonw = InlineKeyboardMarkup(row_width=1)
subchanneldonw.insert(urlch)