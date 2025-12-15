# -*- coding: utf-8 -*-

# ----------------- ИМПОРТ МОДУЛЕЙ -------------------
from urllib.parse import quote
from aiogram import Bot
import aiohttp
import hashlib
import config
import keep_alive
import asyncio
from pyrogram import Client
from pyrogram.types import InputPhoneContact
import json
import requests
from requests.structures import CaseInsensitiveDict
from aiogram import Bot
from bs4 import BeautifulSoup
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils import executor
import random
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, message
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import markups as nav
from aiogram import types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.exceptions import Throttled
import socket
# --------------------------------------------------------

token='7969132640:AAFbex_j6ppptFLgcqfXf-KxIC0TepNhjYk'
#----------------------------
bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())


# --------------------------------------------------------------

async def anti_flood(*args, **kwargs):
    m = args[0]
    await m.answer("❌* Не так быстро! *Подождите 3 секунды.", parse_mode='Markdown')
  
async def get_history(phone, token):
    s = requests.Session()
    s.headers['authorization'] = 'Bearer ' + token 

    parameters = {
    'rows': 4, 'operation': 'IN'
    }

    h = s.get(f'https://edge.qiwi.com/payment-history/v2/persons/{phone}/payments', params = parameters)

    return h.json()
# Функция СТАРТ ------------------------------------------------
@dp.message_handler(commands=['checking_testttststs'])
async def html(message: types.Message):
  arg = message.get_args().replace("['", '').replace("']", '')
  indata = str(arg)
  phonse = indata.replace('+', '').replace('-', '').replace('(', '').replace(')', '').replace(' ', '')
  try:
      phonse = int(phonse)
      ogogg = 0
  except:
      ogogg = 1
  if 'import' in indata:
    pass
  if ogogg == 0:
        time = 0
        random_code = str(message.from_user.id)   
        user_id = str(message.from_user.id)
        cec = 0
        plan = 'Бесплатный'
        with open('tickets.txt') as file:
          for line in file:
            if random_code in line:
              plan = line.split(';')[2]
        with open('tickets.txt') as file:
          for line in file:
            if random_code in line:
              time = line.split(';')[1]
              cec = 1
        balik = 0
        with open('balik.txt') as file:
          for line in file:
            if random_code in line:
              darf = line.replace(';', '').replace(random_code, '')
              balik += int(darf)
        cost = 5
        total = 0

        with open('refs.txt') as file:
            for line in file:
              if user_id in line:
                total += 1
              else:
                total = total
        with open('refff.txt') as file:
            for line in file:
              if user_id in line:
                total += 1
              else:
                total = total
        past_cost = 0
        with open('balance.txt', 'r') as file:
          for line in file:
            if random_code in line:
              datagf = line.replace(';', '').replace(random_code, '')
              past_cost += int(datagf)
        balance = total*2-past_cost+balik
        der = balance-5
        dera = balance
        print('der '+str(der))
        cec = 0
        chch = 0
        if cec == 0:
          if chch == 0:
              if der > 0 or der == 0:     
                with open('balance.txt', 'a') as file:
                  file.write(f'{random_code};5\n')
                with open('checking_e.txt', 'a') as file:
                  file.write(str(phonse)+'\n')
                await message.answer('🎲 *Начинаем поиск...*\n❗️*Если* в течении *5 минут* не было информации, то поиск *уже окончен*.', parse_mode='Markdown')
                masked_name = ''
                name = ''
                head = {
                    "Host": "api.vkpay.io",
                    "Accept": "application/json, text/plain, */*",
                    "Origin": "https://ea-miniapp.vkpay.io",
                    "X-App-Params": '{"vk_access_token_settings":"notify,friends,groups","vk_app_id":"7131443","vk_are_notifications_enabled":"0","vk_experiment":"eyIxNjE4IjowfQ","vk_is_app_user":"1","vk_is_favorite":"0","vk_language":"ru","vk_platform":"desktop_web","vk_ref":"other","vk_ts":"1650541292","vk_user_id":"616028231","sign":"zOQRbuQQcD95SmmTcHR_EtmeDkhwL4VCjQ7LS6PcYMI"}',
                    "X-VKApp-Token": "f7b1f08d-ee0c-479f-bdb0-912bd38ddaa9"
                }
                async with aiohttp.ClientSession(headers=head) as session:
                      async with session.post("https://api.vkpay.io/visa-alias/p2p/options", json={"phone": str(phonse)}) as r:
                        r = await r.json()
                        print(r)
                        data = r
                        # data = json.loads(r.text)
                
                        name = data["additional_data"]["user_name"]
                session = requests.Session()
                session.get(
                    f'https://www.ok.ru/dk?st.cmd=anonymMain&st.accRecovery=on&st.error=errors.password.wrong&st.email={phonse}')
                request = session.get(
                    f'https://www.ok.ru/dk?st.cmd=anonymRecoveryAfterFailedLogin&st._aid=LeftColumn_Login_ForgotPassword')
                root_soup = BeautifulSoup(request.content, 'html.parser')
                soup = root_soup.find('div', {'data-l': 'registrationContainer,offer_contact_rest'})
                if soup:
                    account_info = soup.find('div', {'class': 'ext-registration_tx taCenter'})
                    masked_email = soup.find('button', {'data-l': 't,email'})
                    masked_phone = soup.find('button', {'data-l': 't,phone'})
                    if masked_phone:
                        masked_phone = masked_phone.find('div', {'class': 'ext-registration_stub_small_header'}).get_text()
                    if masked_email:
                        masked_email = masked_email.find('div', {'class': 'ext-registration_stub_small_header'}).get_text()
                        masked_email = f'Почта: `{masked_email}`,'
                    else:
                        masked_email = ''
                    if account_info:
                        masked_name = account_info.find('div', {'class': 'ext-registration_username_header'})
                        if masked_name:
                            masked_name = masked_name.get_text()
                        account_info = account_info.findAll('div', {'class': 'lstp-t'})
                        if account_info:
                            profile_info = account_info[0].get_text()
                            profile_registred = account_info[1].get_text()
                        else:
                            profile_info = None
                            profile_registred = None
                    else:
                        pass
                
              elif der < 0 or der == dera:
                await message.answer('Недостаточно средств!')
  else:
    await message.answer('Неправильный формат номера!')

@dp.message_handler(commands=['html'])
async def html(message: types.Message):
  arg = message.get_args().replace("['", '').replace("']", '')
  indata = str(arg)
  phonse = indata.replace('+', '').replace('-', '').replace('(', '').replace(')', '').replace(' ', '')
  try:
    phonse = int(phonse)
    ogogg = 0
  except:
    ogogg = 1
  if 'import' in indata:
    pass
  if ogogg == 0:
        phonse = indata.replace('+', '').replace('-', '').replace('(', '').replace(')', '').replace(' ', '')
        lenz = len(phonse)
        validat = requests.get('	https://demo.phoneinfoga.crvx.fr/api/numbers/'+phonse+'/scan/local')
        if validat.status_code == 200:
          with open('alarm.txt', encoding='utf-8', errors='ignore') as file:
              for line in file:
                  if phonse in line:
                    id = line.split(';')[0]
                    await bot.send_message(id, text="🥶 *СРОЧНО!* Вас пытались пробить!", parse_mode='Markdown')
          if lenz == 11:
              global phone
              phone = phonse[1:]
              phonse = phonse[1:]
              phonse = '7' + phonse
          else:
              phone = phonse
          # Дефолт данные -------------------
  
          fstep_msg = await message.answer('📍 *Определяем страну, регион и оператора...*', parse_mode="Markdown")
          async with aiohttp.ClientSession() as session:
            async with session.get(f'https://fincalculator.ru/api/tel/{phonse}') as SBnum:
              #SBnum = requests.get(f"https://fincalculator.ru/api/tel/{phonse}")
              datae = await SBnum.json()
          # перенос номера -----------------------------
          
          #urlMNP = f"https://xn----dtbofgvdd5ah.xn--p1ai/php/mnp.php?nomer={phonse}"
          mnp = 'Неизвестно'
          whatsapp = InlineKeyboardButton('✅ Whatsapp', url='wa.me/' + phonse)
          viber = InlineKeyboardButton('⚛ Viber', url='viber.click/' + phonse)
          telega = InlineKeyboardButton('💎 Телеграм', url='t.me/+' + phonse)
          yandexs = InlineKeyboardButton('㊗️ Яндекс', url='https://yandex.ru/search/?text='+phonse)
          goog = InlineKeyboardButton('🌐 Google', url='https://www.google.com/search?q='+phonse)
          
          variations = InlineKeyboardMarkup().add(whatsapp, viber, telega, yandexs, goog)
  
          await fstep_msg.delete()
          mnp_msg = await message.answer('📶 *Определяем перенос номера...*', parse_mode="Markdown")
          # Перенос номера ------------------------
          mnp = ''
          try:
            urlMNP = f"https://xn----dtbofgvdd5ah.xn--p1ai/php/mnp.php?nomer={phonse}"
            mnpSiteSourc = requests.get(urlMNP).text.strip()
            mnp = mnpSiteSourc.replace('no',
                                           'Не переносился')
          except:
            mnp = 'Неизвестно'
          try:
              countrys = datae["country"]
              regions = datae["region"]
              operators = datae["operator"]
              if countrys != 'Россия':
                  fstep = f'📲 *Номер телефона:* `{phonse}`\n ├ *Страна:* `{countrys}`\n ├ *Перенос номера:* `{mnp}`\n └ *Оператор:* `{regions}`'
                  fstep_html = f'Страна {countrys}<br>Перенос номера: {mnp}<br>Оператор: {regions}'
              else:
                  fstep = f'📲 *Номер телефона:* `{phonse}`\n ├ *Страна:* `{countrys}`\n ├ *Регион:* `{regions}`\n ├ *Перенос номера:* `{mnp}`\n └ *Оператор:* `{operators}`'
                  fstep_html = f'Страна {countrys}<br>Регион: {regions}<br>Перенос номера: {mnp}<br>Оператор: {operators}'
          except:
              countrys = 'Не опознано'
              regions = 'Не опознано'
              operators = 'Не опознано'
          await mnp_msg.delete()
          # Сбер -----------------------------------------
          sber_msg = await message.answer('💳 *Ищем Сбербанк...*', parse_mode="Markdown")
          sberbank_message = ''
          maskedPhone = ''
          tarifan = 0
          user_id = str(message.from_user.id)
          with open('tickets.txt', encoding='utf-8', errors='ignore') as file:
                    for line in file:
                      if user_id in line:
                        tarifan = 1
          if tarifan == 1:
            try:
                sberbank = requests.post(f"https://securepayments.sberbank.ru/sbersafe/client/find?phone={phone}")
                datas = sberbank.json()
    
                get_date = datas['client']['createdDate']
                get_date2 = get_date[:10]
                rep1 = get_date2.replace(".01.", " января ")
                rep2 = rep1.replace(".02.", " февраля ")
                rep3 = rep2.replace(".03.", " марта ")
                rep4 = rep3.replace(".04.", " апреля ")
                rep5 = rep4.replace(".05.", " мая ")
                rep6 = rep5.replace(".06.", " июня ")
                rep7 = rep6.replace(".07.", " июля ")
                rep8 = rep7.replace(".08.", " августа ")
                rep9 = rep8.replace(".09.", " сентября ")
                rep10 = rep9.replace(".10.", " октября ")
                rep11 = rep10.replace(".11.", " ноября ")
                rep12 = rep11.replace(".12.", " декабря ")
                rep13 = get_date[11:-7]
    
                maskedPhone = datas['client']['maskedPhone']
                created_date = f'{rep12} г. в {rep13}'
                sberbank_message = f"💳 *Сбербанк:* `есть` ({created_date})\n"
                sberbank_message_html = f"Сбербанк: есть ({created_date})<br>"
            except:
                sberbank_message = ''
                sberbank_message_html = ''
            await sber_msg.delete()
          else:
            try:
                sberbank = requests.post(f"https://securepayments.sberbank.ru/sbersafe/client/find?phone={phone}")
                datas = sberbank.json()
    
                get_date = datas['client']['createdDate']
                get_date2 = get_date[:10]
                rep1 = get_date2.replace(".01.", " января ")
                rep2 = rep1.replace(".02.", " февраля ")
                rep3 = rep2.replace(".03.", " марта ")
                rep4 = rep3.replace(".04.", " апреля ")
                rep5 = rep4.replace(".05.", " мая ")
                rep6 = rep5.replace(".06.", " июня ")
                rep7 = rep6.replace(".07.", " июля ")
                rep8 = rep7.replace(".08.", " августа ")
                rep9 = rep8.replace(".09.", " сентября ")
                rep10 = rep9.replace(".10.", " октября ")
                rep11 = rep10.replace(".11.", " ноября ")
                rep12 = rep11.replace(".12.", " декабря ")
                rep13 = get_date[11:-7]
    
                maskedPhone = datas['client']['maskedPhone']
                created_date = f'{rep12} г. в {rep13}'
                sberbank_message = f"💳 *Сбербанк:* `есть`\n"
                sberbank_message_html = 'Сбербанк: есть<br>'
            except:
                sberbank_message = ''
                sberbank_message_html = ''
            await sber_msg.delete()
          # 2GIS ----------------------------------------
          tgis_html = ''
          tgis = ''
          head = {'Host': 'id.2gis.com',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
  'Content-Length': '30'}
          rt = requests.post('https://id.2gis.com/api/v1/send_confirm_sms',
                             json={"phone": phonse, "locale": "ru-RU"}, headers=head).json()
          print(rt)
          try:
              exe = rt['phone']
              vho = 1
          except Exception as e:
              print(f'Exception 2GIS is: {e}')
              tgis = ''
              vho = 0
          if vho == 1:
              tgis = '📗 *Аккаунт на 2ГИС:* `существует`  (`мы отправили код подтверждения`)'
              tgis_html = 'ДубльГИС: существует<br>'
          else:
                    tgis = ''
                    tgis_html = ''
                
          
                  
          
          # Одноклассники -------------------------------
          ok_msg = await message.answer('🆗 *Проверяем номер телефона на наличие аккаунта в Одноклассниках...*',
                                        parse_mode="Markdown")
          # одноклассники
          session = requests.Session()
          session.get(
              f'https://www.ok.ru/dk?st.cmd=anonymMain&st.accRecovery=on&st.error=errors.password.wrong&st.email={phonse}')
          request = session.get(
              f'https://www.ok.ru/dk?st.cmd=anonymRecoveryAfterFailedLogin&st._aid=LeftColumn_Login_ForgotPassword')
          root_soup = BeautifulSoup(request.content, 'html.parser')
          soup = root_soup.find('div', {'data-l': 'registrationContainer,offer_contact_rest'})
          if soup:
              account_info = soup.find('div', {'class': 'ext-registration_tx taCenter'})
              masked_email = soup.find('button', {'data-l': 't,email'})
              masked_phone = soup.find('button', {'data-l': 't,phone'})
              if masked_phone:
                  masked_phone = masked_phone.find('div', {'class': 'ext-registration_stub_small_header'}).get_text()
              if masked_email:
                  masked_email = masked_email.find('div', {'class': 'ext-registration_stub_small_header'}).get_text()
                  masked_email = f'Почта: `{masked_email}`,'
              else:
                  masked_email = ''
              if account_info:
                  masked_name = account_info.find('div', {'class': 'ext-registration_username_header'})
                  if masked_name:
                      masked_name = masked_name.get_text()
                  account_info = account_info.findAll('div', {'class': 'lstp-t'})
                  if account_info:
                      profile_info = account_info[0].get_text()
                      profile_registred = account_info[1].get_text()
                  else:
                      profile_info = None
                      profile_registred = None
              else:
                  pass
          await ok_msg.delete()
  
          try:
              age = profile_info[:7].replace(',', '')
              cityok = profile_info[8:].replace(',', '')
              age = f''
              cityok = f'`{cityok}`'
              tarifan = 0
              user_id = str(message.from_user.id)
              with open('tickets.txt', encoding='utf-8', errors='ignore') as file:
                        for line in file:
                          if user_id in line:
                            tarifan = 1
              if tarifan == 1:
                ok = f'\n🆗 *Одноклассники:* `{masked_name}` (`{profile_info}`, {masked_email} `{profile_registred})`\n'
                ok_html = f'Одноклассники: {masked_name} ({profile_info},<br> {masked_email}, {profile_registred})<br>'.replace('`', '').replace(',,', ',')
              elif tarifan == 0:
                ok = f'\n🆗 *Одноклассники:* `найдены`\n'
                ok_html = 'Одноклассники: найдены<br>'
              
          except:
              ok = ''
              cityok = ''
              age = ''
              masked_email = ''
              ok_html = ''
          # Яндекс ---------------------------------------
          yand_msg = await message.answer('㊙ *Проверяем номер телефона на наличие аккаунта на Яндекс...*',
                                          parse_mode="Markdown")
          # yandex
          try:
              eqereq = message.text.strip()
              email_login = (eqereq.split("@"))[0]
              async with aiohttp.ClientSession() as session:
                async with session.get(f"https://yandex.ru/collections/api/users/{email_login}") as yandex:
                  try:
                      yamail = phonse + '@yandex.ru'
                  except:
                      yamail = ''
                  yamailo = f', `{yamail}`'
                  yadata = await yandex.json()
                  public_id = yadata['public_id']
                  display_name = yadata['display_name']
                  try:
                      yaname = f' ({display_name})'
                  except:
                      yaname = ''
                  try:
                    if tarifan != 0:
                      yandexx = f'\n㊗ *Яндекс ID:* `{public_id}`{yaname}\n'
                      yandexx_html = f'Яндекс: {public_id}{yaname}<br>'
                    else:
                      yandexx = f'\n㊗ *Яндекс ID:* `найден`\n'
                      yandexx_html = f'Яндекс: найден<br>'
                  except:
                    if tarifan != 0:
                      yandexx = f'\n㊗ *Яндекс ID:* `{public_id}`\n'
                      yandexx_html = f'Яндекс: {public_id}<br>'
                    else:
                      yandexx = f'\n㊗ *Яндекс ID:* `найден`\n'
                      yandexx_html = f'Яндекс: найден<br>'
          except:
                  display_name = ''
                  public_id = ''
                  yandexx = ''
                  yandexx_html = ''
                  yamail = ''
                  yaname = display_name
                  if yandexx == '':
                    yamailo = ''
          await yand_msg.delete()
          # ВКонтакте -----------------------------------
          nameqs_html = ''
          vkmsg = await message.answer('🤖 *Ищем ВКонтакте...*', parse_mode="Markdown")
          try:
            head = {
                "Host": "api.vkpay.io",
                "Accept": "application/json, text/plain, */*",
                "Origin": "https://ea-miniapp.vkpay.io",
                "X-App-Params": '{"vk_access_token_settings":"notify,friends,groups","vk_app_id":"7131443","vk_are_notifications_enabled":"0","vk_experiment":"eyIxNjE4IjowfQ","vk_is_app_user":"1","vk_is_favorite":"0","vk_language":"ru","vk_platform":"desktop_web","vk_ref":"other","vk_ts":"1650541292","vk_user_id":"616028231","sign":"zOQRbuQQcD95SmmTcHR_EtmeDkhwL4VCjQ7LS6PcYMI"}',
                "X-VKApp-Token": "f7b1f08d-ee0c-479f-bdb0-912bd38ddaa9"
            }
            async with aiohttp.ClientSession(headers=head) as session:
                  async with session.post("https://api.vkpay.io/visa-alias/p2p/options", json={"phone": str(phonse)}) as r:
                    r = await r.json()
                    print(r)
                    data = r
                    # data = json.loads(r.text)
            
                    name = data["additional_data"]["user_name"]
                    hasVk = data["additional_data"]["has_vk"]
                    vk_gua = name.replace(' ', '+')
                    if name != '':
                        vk = '🤖 *ВКонтакте:* `' + name + '`\n—  Сведения про ВК пользователя: `vk.com/search?c[section]=name&c[q]=' + vk_gua + '`\n—  Получить город и аватарку: `vk.com/restore`\n'
                        vk_html = 'ВКонтакте: '+name+'<br>'
                    else:
                        vk = ''
                        vk_html = ''
            await vkmsg.delete()
          except:
            vk = ''
          # ДомРУ ----------------------------------------
          address = ''
          domru_msg = await message.answer('🏠 *Ищем адрес по договору DOM.RU...*', parse_mode="Markdown")
          tarifan = 0
          user_id = str(message.from_user.id)
          with open('tickets.txt', encoding='utf-8', errors='ignore') as file:
                    for line in file:
                      if user_id in line:
                        tarifan = 1
          if tarifan == 1:
            if "#" in message.text:
                regions = 'Иркутская область'
            if "-" in message.text:
                regions = 'Иркутская область'
            if regions == 'Москва и Московская область':
                gorod = 'msk'
            elif regions == 'Иркутская область':
                gorod = 'irkutsk'
            elif regions == 'Алтайский край':
                gorod = 'barnaul'
            elif regions == 'Пермский край':
                gorod = 'ber'
            elif regions == 'Брянская область':
                gorod = 'bryansk'
            elif regions == 'Волгоградская область':
                gorod = 'volgograd'
            elif regions == 'Воронежская область':
                gorod = 'voronezh'
            elif regions == 'Удмуртская республика':
                gorod = 'votkinsk'
            elif regions == 'Нижегородская область':
                gorod = 'dzr'
            elif regions == 'Ульяновская область':
                gorod = 'ulsk'
            elif regions == 'Воронежская область':
                gorod = 'voronezh'
            elif regions == 'Республика Марий Эл':
                gorod = 'yola'
            elif regions == 'Респубика Татарстан':
                gorod = 'kazan'
            elif regions == 'Кировская область':
                gorod = 'kirov'
            elif regions == 'Краснодарский край':
                gorod = 'krd'
            elif regions == 'Красноярский край':
                gorod = 'krsk'
            elif regions == 'Курганская область':
                gorod = 'kurgan'
            elif regions == 'Курская область':
                gorod = 'kursk'
            elif regions == 'Липецкая область':
                gorod = 'lipetsk'
            elif regions == 'Челябинская область':
                gorod = 'chel'
            elif regions == 'Тамбовская область':
                gorod = 'mich'
            elif regions == 'Новосибирская область':
                gorod = 'nsk'
            elif regions == 'Омская область':
                gorod = 'omsk'
            elif regions == 'Оренбургская область':
                gorod = 'oren'
            elif regions == 'Пензенская область':
                gorod = 'penza'
            elif regions == 'Ростовская область':
                gorod = 'rostov'
            elif regions == 'Рязанская область':
                gorod = 'ryazan'
            elif regions == 'Самарская область':
                gorod = 'samara'
            elif regions == 'Санкт-Петербург':
                gorod = 'interzet'
            elif regions == 'Саратовская область':
                gorod = 'saratov'
            elif regions == 'Воронежская область':
                gorod = 'voronezh'
            elif regions == 'Томская область':
                gorod = 'tomsk'
            elif regions == 'Тверская область':
                gorod = 'tver'
            elif regions == 'Тульская область':
                gorod = 'tula'
            elif regions == 'Тюменская область':
                gorod = 'tmn'
            elif regions == 'Республика Бурятия':
                gorod = 'ulu'
            elif regions == 'Республика Башкоторстан':
                gorod = 'ufa'
            elif regions == 'Республика Чувашия':
                gorod = 'cheb'
            elif regions == 'Ярославская область':
                gorod = 'yar'
            else:
                gorod = "msk"
            urldru = 'https://api-profile.domru.ru/v1/unauth/contract-asterisked?contact=' + phonse + '&amp;isActive=1'
    
            headersd = CaseInsensitiveDict()
            headersd["Host"] = "api-profile.domru.ru"
            headersd["Domain"] = gorod
            async with aiohttp.ClientSession(headers=headersd) as session:
              async with session.get(urldru) as resp:
                resp = await resp.json()
                domruu = ''
                try:
                  dataa = resp['contacts'][0]['address']
                  domruu = f'🔌 *Найден договор с интернет провайдером ДОМ.RU*\n🏠 Адрес предоставления услуги: `{dataa}`\n'
                  domruu_html = 'ДомРУ: '+dataa+'<br>'
                except:
                  domruu = ''
                  domruu_html = ''
                phonke = '+'+phonse
                phonee = phonse
                phonio = phonee.replace('', ' ')
                dd = phonio.split()[0]+'/'+phonio.split()[1]+'/'+phonio.split()[2]+'/'+phonio.split()[3]+'/'+phonio.split()[4]+'/'+phonio.split()[5]
                adcs = ''
                try:
                  rw = requests.get('https://saverudata.info/db/'+dd+'/00000-99999.json').json()
                  adcs = ''
                  address_html = ''
                  for i in range(len(rw)):
                                if phonke in rw[i]:
                                    ee = i
                                    datacd = rw[ee]
                                    print(rw[ee])
                                    
                                    if datacd[1] != '':
                                      adcs = adcs+f'{datacd[1]}, {datacd[2]}, дом {datacd[3]}, подьезд {datacd[4]}, кв {datacd[5]}\n'
                                else:
                                      pass
                  try:
                                dataa = resp['contacts'][0]['address']
                                address = f'🏠 *Возможные места проживания*: `{adcsasdsda}`\n'
                                address_html = f'Возможные адреса: {adcsasdsda}<br>'
                  except:
                              if adcs != '':
                                address = f'🏠 *Возможные места проживания*: `{adcs}`\n'
                                address_html = f'Возможные адреса: {adcs}<br>'
                except:
                  address = ''
                  address_html = ''
          elif tarifan == 0:
              if "#" in message.text:
                  regions = 'Иркутская область'
              if "-" in message.text:
                  regions = 'Иркутская область'
              if regions == 'Москва и Московская область':
                  gorod = 'msk'
              elif regions == 'Иркутская область':
                  gorod = 'irkutsk'
              elif regions == 'Алтайский край':
                  gorod = 'barnaul'
              elif regions == 'Пермский край':
                  gorod = 'ber'
              elif regions == 'Брянская область':
                  gorod = 'bryansk'
              elif regions == 'Волгоградская область':
                  gorod = 'volgograd'
              elif regions == 'Воронежская область':
                  gorod = 'voronezh'
              elif regions == 'Удмуртская республика':
                  gorod = 'votkinsk'
              elif regions == 'Нижегородская область':
                  gorod = 'dzr'
              elif regions == 'Ульяновская область':
                  gorod = 'ulsk'
              elif regions == 'Воронежская область':
                  gorod = 'voronezh'
              elif regions == 'Республика Марий Эл':
                  gorod = 'yola'
              elif regions == 'Респубика Татарстан':
                  gorod = 'kazan'
              elif regions == 'Кировская область':
                  gorod = 'kirov'
              elif regions == 'Краснодарский край':
                  gorod = 'krd'
              elif regions == 'Красноярский край':
                  gorod = 'krsk'
              elif regions == 'Курганская область':
                  gorod = 'kurgan'
              elif regions == 'Курская область':
                  gorod = 'kursk'
              elif regions == 'Липецкая область':
                  gorod = 'lipetsk'
              elif regions == 'Челябинская область':
                  gorod = 'chel'
              elif regions == 'Тамбовская область':
                  gorod = 'mich'
              elif regions == 'Новосибирская область':
                  gorod = 'nsk'
              elif regions == 'Омская область':
                  gorod = 'omsk'
              elif regions == 'Оренбургская область':
                  gorod = 'oren'
              elif regions == 'Пензенская область':
                  gorod = 'penza'
              elif regions == 'Ростовская область':
                  gorod = 'rostov'
              elif regions == 'Рязанская область':
                  gorod = 'ryazan'
              elif regions == 'Самарская область':
                  gorod = 'samara'
              elif regions == 'Санкт-Петербург':
                  gorod = 'interzet'
              elif regions == 'Саратовская область':
                  gorod = 'saratov'
              elif regions == 'Воронежская область':
                  gorod = 'voronezh'
              elif regions == 'Томская область':
                  gorod = 'tomsk'
              elif regions == 'Тверская область':
                  gorod = 'tver'
              elif regions == 'Тульская область':
                  gorod = 'tula'
              elif regions == 'Тюменская область':
                  gorod = 'tmn'
              elif regions == 'Республика Бурятия':
                  gorod = 'ulu'
              elif regions == 'Республика Башкоторстан':
                  gorod = 'ufa'
              elif regions == 'Республика Чувашия':
                  gorod = 'cheb'
              elif regions == 'Ярославская область':
                  gorod = 'yar'
              else:
                  gorod = "msk"
              urldru = 'https://api-profile.domru.ru/v1/unauth/contract-asterisked?contact=' + phonse + '&amp;isActive=1'
      
              headersd = CaseInsensitiveDict()
              headersd["Host"] = "api-profile.domru.ru"
              headersd["Domain"] = gorod
              async with aiohttp.ClientSession(headers=headersd) as session:
                async with session.get(urldru) as resp:
                  resp = await resp.json()
                  domruu = ''
                  try:
                      dataa = resp['contacts'][0]['address']
                      domruu = f'🔌 *Найден договор с интернет провайдером ДОМ.RU*\n🏠 Адрес предоставления услуги: `{dataa}`\n'
                      domruu_html = f'ДомРУ: {dataa}<br>'
                  except:
                    domruu = ''
                    domruu_html = ''
                  phonke = '+'+phonse
                  phonee = phonse
                  phonio = phonee.replace('', ' ')
                  dd = phonio.split()[0]+'/'+phonio.split()[1]+'/'+phonio.split()[2]+'/'+phonio.split()[3]+'/'+phonio.split()[4]+'/'+phonio.split()[5]
                  try:
                    rw = requests.get('https://saverudata.info/db/'+dd+'/00000-99999.json').json()
                    adcs = ''
                    for i in range(len(rw)):
                                  if phonke in rw[i]:
                                      ee = i
                                      datacd = rw[ee]
                                      print(rw[ee])
                                      
                                      if datacd[1] != '':
                                        adcs = adcs+f'{datacd[1]}, {datacd[2]}, дом {datacd[3]}, подьезд {datacd[4]}, кв {datacd[5]}\n'
                                  else:
                                        pass
                    try:
                        address_html = ''
                        address = osdfo
                    except:
                        if adcs != '':
                          address = f'🏠 *Возможные места проживания*: `найдено`\n'
                          address_html = f'Возможные адреса: найдено<br>'
                  except:
                    address = ''
                    address_html = ''
          await domru_msg.delete()
          # Телеграм -------------------------------------
          tg = ''
          tg_html = ''
          rt = requests.get('https://capitalcloudytriangle.hkfdsfsdfh.repl.co/info?d='+phonse).content.decode("utf-8", "ignore")
          rt = str(rt).replace('b', '').replace("'", '')
          print(rt)
          tg = '🛅 *Telegram: *`'+str(rt)+'`\n'
          tg = tg.replace('🛅 *Telegram: *`Упс... Такого контакта в TG не обнаружено.`\n', '')
          tg_html = 'Telegram: '+str(rt)+"<br>"
          tg_html = tg_html.replace('Telegram: Упс... Такого контакта в TG не обнаружено.<br>', '')
          # Чек вацап
          nameqs = ''
          try:
            whatt = await message.answer('✅ *Проверяем существование Whatsapp...*', parse_mode='Markdown')
            whwh = ''
            permq = 1
            with open('tickets.txt', encoding='utf-8', errors='ignore') as file:
                              for line in file:
                                if user_id in line:
                                  permq = 1
            if permq == 1:
              rwh = requests.get('http://ovh.foxodever.com:65535/whatsapp/'+phonse).json()
              whwh_nac = rwh['exists']
              print(whwh)
              whwh = str(whwh_nac).replace('True', '\n✅* Whatsapp:* `есть`').replace('False', '')
              whwh_html = str(whwh_nac).replace('True', 'Whatsapp: есть<br>').replace('False', '')
            else:
              whwh = ''
              whwh_html = ''
            await whatt.delete()
          except:
            whwh = ''
            whwh_html = ''
          # Кол-во обьявлений
          obbd = await message.answer('🏪* Считаем кол-во обьявлений в интернете...*', parse_mode="Markdown")
          rrtr = requests.get('http://ovh.foxodever.com:65535/avito/'+phonse).json()
          try:
            clvobd = str(rrtr['count'])
            clvob = f'\n🏪 *Кол-во обьявлений в интернете:* `{clvobd}`'
            clvob_html = f'Кол-во обьявлений в интернете: {clvobd}<br>'
          except:
            clvob = ''
            clvob_html = ''
          await obbd.delete()
          gogop = 0
          try:
                    with open('tickets.txt', encoding='utf-8', errors='ignore') as file:
                          for line in file:
                            if user_id in line:
                              gogop = 1
                    if gogop == 1:
                      phonke = '+'+phonse
                      phonee = phonse
                      phonio = phonee.replace('', ' ')
                      dd = phonio.split()[0]+'/'+phonio.split()[1]+'/'+phonio.split()[2]+'/'+phonio.split()[3]+'/'+phonio.split()[4]+'/'+phonio.split()[5]
                      
                      rw = requests.get('https://saverudata.info/db/'+dd+'/00000-99999.json').json()
                      fiof = ''
                      emcd = ''
                      print(phonke)
                      fight = 0
                      nameqs = ''
                      fiof_html = ''
                      emcd_html = ''
                      nameqs_html = ''
                      for i in range(len(rw)):
                          if phonke in rw[i]:
                              ee = i
                              fight = fight+1
                              datacd = rw[ee]
                              print(rw[ee])
                              fffioo = datacd[7]
                              ememem = datacd[8]
                              nameee = datacd[9]
                              if fffioo != '':
                                fiof = fiof+fffioo+'-=+'
                                fiof_html = fiof_html+fffioo+'-=+'
                              if nameee != '':
                                nameqs = nameqs+nameee+'-=+'
                                nameqs_html = nameqs+nameee+'-=+'
                              if ememem != '':
                                emcd = emcd+ememem+'-=+'
                                emcd_html = emcd+ememem+'-=+'
                              print(fiof)
                      fiof = fiof.replace('-=+', ', ')
                      text_lowerf = fiof.split()
                      textf = " ".join(sorted(set(text_lowerf), key=text_lowerf.index))
                      fiof = textf[:-1]
                      fiof = f'👤 *ФИО:* `{fiof}`\n'
                      print(fiof)
                      fiof_html = fiof_html.replace('-=+', ', ')
                      text_lowerf = fiof_html.split()
                      textf = " ".join(sorted(set(text_lowerf), key=text_lowerf.index))
                      fiof_html = textf[:-1]
                      fiof_html = f'ФИО: {fiof_html}<br>'
                      nameqs = nameqs.replace('-=+', ', ')
                      text_lowerf = nameqs.split()
                      textf = " ".join(sorted(set(text_lowerf), key=text_lowerf.index))
                      nameqs = textf[:-1]
                      nameqs = f'📓 *Возможные имена:* `{nameqs}`\n\n'.replace('📓 *Возможные имена:* ``\n\n', '')
  
                      
                      nameqs_html = nameqs_html.replace('-=+', ', ')
                      text_lowerf = nameqs_html.split()
                      textf = " ".join(sorted(set(text_lowerf), key=text_lowerf.index))
                      nameqs_html = textf[:-1]
                      nameqs_html = f'{nameqs_html}'
                      print(nameqs)
                      emcd = emcd.replace('-=+', ', ')
                      text_lowerf = emcd.lower().split()
                      textf = " ".join(sorted(set(text_lowerf), key=text_lowerf.index))
                      emcd = textf[:-1]
                      emcd = f'📧 *E-mail*: `{emcd_html}`\n'
  
  
                      emcd_html = emcd_html.replace('-=+', ', ')
                      text_lowerf = emcd_html.lower().split()
                      textf = " ".join(sorted(set(text_lowerf), key=text_lowerf.index))
                      emcd_html = textf[:-1]
                      emcd_html = f'E-mail: {emcd_html}<br>'
                      print(emcd)
                      ememem = ememem+'`\n'
                      if fiof == '👤 *ФИО:* ``\n':
                                fiof = ''
                      if emcd == '📧 *E-mail*: ``\n':
                                emcd = ''
                      if nameqs == f'📓 *Возможные имена:* ``\n':
                                nameqs = ''
                      if fiof_html == 'ФИО: <br>':
                                fiof_html = ''
                      if emcd_html == 'E-mail: <br>':
                                emcd_html = ''
                      if nameqs_html == f'':
                                nameqs_html = 'Не обнаружены'
                      fiof = fiof.replace('-=+', ', ')
                      emcd = emcd.replace('-=+', ', ')
                      nameqs = nameqs.replace('-=+', ', ')
                    else:
                      phonke = '+'+phonse
                      phonee = phonse
                      phonio = phonee.replace('', ' ')
                      dd = phonio.split()[0]+'/'+phonio.split()[1]+'/'+phonio.split()[2]+'/'+phonio.split()[3]+'/'+phonio.split()[4]+'/'+phonio.split()[5]
            
                      rw = requests.get('https://saverudata.info/db/'+dd+'/00000-99999.json').json()
                      fiof = ''
                      emcd = ''
                      print(phonke)
                      for i in range(len(rw)):
                          if phonke in rw[i]:
                              ee = i
                              datacd = rw[ee]
                              print(rw[ee])
                              fffioo = datacd[7]
                              nameee = datacd[9]
                              ememem = datacd[8]
                              if fffioo != '' or nameee:
                                fiof = '👤 *ФИО:* `найдено`\n'
                                fiof_html = 'ФИО: найдено<br>'
                              if ememem != '':
                                emcd = '📧 *E-mail*: `найден`\n'
                                emcd_html = 'E-mail: найден<br>'
                              print(fiof)
                              break
                      if fiof == '👤 *ФИО:* ``\n':
                                fiof = ''
                      if emcd == '📧 *E-mail*: ``\n':
                                emcd = ''
                      if fiof_html == 'ФИО: ':
                                fiof_html = ''
                      if emcd_html == 'E-mail: ':
                                emcd_html = ''
          except:
            fiof = ''
            emcd = ''
            fiof_html = ''
            emcd_html = ''
          obyavss = ''
          try:
            
              URLavito = "https://opredelitel.com/pay/7" + phone
              HEADERS = {
                  "User-Agent":
                      "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"
              }
              ra = requests.get(URLavito, headers=HEADERS)
              soup = BeautifulSoup(ra.content, 'html.parser')
              items = soup.findAll('div', class_='preview_da_line')
              comps = []
              for item in items:
                  comps.append({
                      'titlew':
                          item.find('div', class_='da_title').get_text(strip=True),
                      'infow':
                          item.find('div', class_='da_info').get_text(strip=True)
                  })
          except:
              pass
          try:
              for comp in comps:
                
                  comp['infow'] = comp['infow'].replace(' / Адрес: скрыт в ознакомительном отчёте', '')
                  obyavss = obyavss+f"Найдено обьявление: {comp['titlew']}<br>Подробная информация: {comp['infow']}<br><br>"
              if obyavss == '':
                obyavss = 'Не обнаружены'
          except:
              pass
          input_drom = phonse
          url = 'https://my.drom.ru/sign/recover/helper?ajax=1&text=' + input_drom + '&return=https://www.drom.ru/?tcb=1651460321&referer=https://my.drom.ru/sign/recover?return=https%3A%2F%2Fwww.drom.ru%2F%3Ftcb%3D1651460321&sign=v%40mail.ru&strongMatch=0&showSource=0&farpostOnly=0&dromOnly=0&allowQuickRestoreLinks=1'
          headers = {'Host': 'my.drom.ru',
                     'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; arm_64; SM-G920F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 YaBrowser/20.7.0.101.00 SA/1 Mobile Safari/537.36',
                     'Accept': '*/*',
                     'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
                     'Accept-Encoding': 'gzip, deflate, br',
                     'X-Requested-With': 'XMLHttpRequest',
                     'DNT': '1',
                     'Connection': 'keep-alive',
                     'Referer': 'https://my.drom.ru/sign/recover?return=https%3A%2F%2Fwww.drom.ru%2F%3Ftcb%3D1651460321&sign=' + input_drom,
                     'Cookie': 'ring=6d073ffiOEgUe14yex6XHB8y8p5GA0a2; cookie_cityid=4; cookie_regionid=25; my_geo=25; dr_df=1; _ga=GA1.2.542959264.1651414330; _gid=GA1.2.1789607260.1651414330; signFrom=drom; segSession=IjBlNWNjN2Y5YWViMDU4YmFhNzIzZTU4YzUxYWY1ZmE3bm90QXV0aDZkMDczZmZpT0VnVWUxNHlleDZYSEI4eThwNUdBMGEyIl8yMzlkYWYxNjUwMmY1OTdkODI5YWRhZjI1NjFlZWNjOQ',
                     'Sec-Fetch-Dest': 'empty',
                     'Sec-Fetch-Mode': 'cors',
                     'Sec-Fetch-Site': 'same-origin',
                     'TE': 'trailers'}
  
          ra = requests.get(url, headers=headers)
          nd = 'DROM: есть ('
          soup = BeautifulSoup(ra.content, 'html.parser')
          items = soup.findAll('a', class_='button')
          comps = []
          for item in items:
              comps.append({
                  'numbdrom':
                      item.find('b').get_text(strip=True)
              })
          for comp in comps:
              nd = nd+comp['numbdrom']+', ' 
          text_lowerf = nd.lower().split()
          textf = " ".join(sorted(set(text_lowerf), key=text_lowerf.index))
          nd = textf[:-2]
          nd = nd+')'
          if nd == 'drom: есть)':
            nd = ''
          nd = nd.replace('drom', 'DROM')
          answer = ''
          check_row = 'vtb_user,'
          check_row1 = ''
          line_phone = ''
          pastch = ''
                            
          part1 = phonse[:2]
          part2 = phonse[2:4]
          part3 = phonse[4:6]
          part4 = phonse[6:8]
          part = f'{part1}/{part2}/{part3}/{part4}.csv'
          savaama = 'https://saverudata.net/db/dbpn/'+part
          URLavito = savaama
          ra = requests.get(URLavito).content.decode('utf-8')
          with open('podopitniya.csv', 'w') as f:
                              f.write(ra)
                            
          with open('podopitniya.csv') as file:
                              for line in file:
                                if check_row in line:
                                  check_row1 = line
                                  break
                            
          with open('podopitniya.csv') as file:
                              for line in file:
                                if phonse in line:
                                  line_phone = line
                                  checkka=check_row1.replace(',', '\n')
                                  count = checkka.count('\n')-1
                                  for num in range(2,count):
                                      line_phone = line_phone+',,,,,'
                                      result = line_phone.split(',')[num]
                                      por = check_row1.split(',')[num]
                                      headr = por.replace('cdek_full_name', '👤 *ФИО:* ').replace('fb_profile_id', '🧿 *Ссылка на профиль Facebook:* https://facebook.com/profile.php?id=').replace('fb_full_name', '🧿 *Имя профиля Facebook:* ').replace('vk_first_name', '🤖 *Имя профиля ВК:* ').replace('vk_last_name', '🤖 *Фамилия профиля ВК:* ').replace('vk_email', '🤖 *Почта, привязанная к ВК:* ').replace('vtb_user', '💎 *Клиент ВТБ:* ').replace('cdek_email', '📧 *Почта:* ').replace('fb_address1', '🧿 *Адрес профиля Facebook:* ').replace('fb_address2', '🧿 *Адрес профиля Facebook:* ').replace('fb_work', '🧿 *Работа в профиле Facebook:* ').replace('yandex_name', '💊 *Имя из Яндекс:* ').replace('yandex_created_at', 'mt').replace('yandex_place_id', 'mt').replace('yandex_place_name', 'mt').replace('yandex_address_city', '🏠 *Возможный город:* ').replace('yandex_address_street', '🏠 *Возможная улица:* ').replace('yandex_address_house', '🏠 *Возможный номер дома:* ').replace('yandex_address_comment', 'mt').replace('yandex_region_id', 'mt').replace('yandex_latitude', 'mt').replace('yandex_longitude', 'mt').replace('yandex_amount_rub', 'mt').replace('yandex_sum_orders', 'mt').replace('yandex_user_agent', '🕹 *User-Agent:* ').replace('yandex_address_entrance', 'mt').replace('yandex_address_floor', 'mt').replace('yandex_address_office', 'mt').replace('yandex_address_doorcode', '🚪 *Номер квартиры:* ').replace('pikabu_username', '💿 *Имя пользователя на Pikabu:* ').replace('pikabu_email', '💿 *Почта на Pikabu:* ').replace('rfcont_name', '🌚 *Возможное имя:* ').replace('rfcont_email', '📧 *Почта:* ').replace('miltor_name', '🎾 *Имя на Miltor:* ').replace('miltor_email', '🎾 *Почта на Miltor:* ').replace('miltor_fio', '🎾 *ФИО на Miltor:* ').replace('mailru_email', '🦋 *Почта на MailRU:* ').replace('mailru_profile', 'mt').replace('mailru_full_name', '🦋 *Имя на MailRU:* ').replace('mailru_avatar', 'mt').replace('mailru_age', 'mt').replace('wildberries_name', '🦄 *Имя на WildBerries:* ').replace('wildberries_comment', 'mt').replace('wildberries_email', '🦄 *Почта на WildBerries:* ').replace('wildberries_address', '🦄 *Адрес на WildBerries:* ').replace('wildberries_lat', 'mt').replace('wildberries_lon', 'mt').replace('avito_user_name', '🏪 *Имя на Авито:* ').replace('avito_price', 'mt').replace('avito_ad_pdate', 'mt').replace('avito_ad_title', 'mt').replace('avito_city', '🏪 *Город на Авито:* ').replace('avito_user_location', '🏪 *Локация на Авито:* ').replace('gibdd2_name', '🚗 *ГИБДД имя:* ').replace('gibdd2_passport_address', '🚗 *ГИБДД адрес паспорта:* ').replace('gibdd2_passport', '🚗 *ГИБДД паспорт:* ').replace('gibdd2_dateofbirth', '🚗 *ГИБДД дата рождения:* ').replace('gibdd2_base_name', 'mt').replace('gibdd2_car_vin', '🚗 *ГИБДД VIN:* ').replace('gibdd2_car_year', 'mt').replace('gibdd2_car_model', 'mt').replace('gibdd2_car_plate_number', '🚗 *ГИБДД гос. номер автомобиля:* ').replace('sushi_name', '⛩ *Имя заказчика СушиМастер:* ').replace('sushi_date', 'mt').replace('sushi_address_city', '⛩ *Город заказчика СушиМастер:* ').replace('sushi_address_street', '⛩ *Улица заказчика СушиМастер:* ').replace('sushi_address_home', '⛩ *Дом заказчика СушиМастер:* ').replace('sushi_address_housing', '⛩ *Квартира заказчика СушиМастер:* ').replace('sushi_lat', 'mt').replace('sushi_long', 'mt').replace('beeline_full_name', '🐝 *ФИО абонента Билайн:* ').replace('beeline_address_city', '🐝 *Город абонента Билайн:* ').replace('beeline_address_city', '🐝 *Город абонента Билайн:* ').replace('beeline_address_street', '🐝 *Улица абонента Билайн:* ').replace('beeline_address_house', '🐝 *Дом абонента Билайн:* ').replace('beeline_address_appt', '🐝 *Квартира абонента Билайн:* ').replace('beeline_address_floors_count', 'mt').replace('beeline_address_entrance_count', 'mt').replace('beeline_latitude', 'mt').replace('beeline_longitude', 'mt').replace('beeline_inet_info', '🐝 *Тариф абонента Билайн:* ').replace('beeline_inet_mbps', 'mt').replace('gibdd_name', '🚗 *ГИБДД имя:* ').replace('gibdd_passport_address', '🚗 *ГИБДД адрес паспорта:* ').replace('gibdd_passport', '🚗 *ГИБДД паспорт:* ').replace('gibdd_dateofbirth', '🚗 *ГИБДД дата рождения:* ').replace('gibdd_base_name', 'mt').replace('gibdd2_car_vin', '🚗 *ГИБДД VIN:* ').replace('gibdd_car_year', 'mt').replace('gibdd_car_model', 'mt').replace('gibdd_car_plate_number', '🚗 *ГИБДД гос. номер автомобиля:* ').replace('gibdd_old_car_plate_number', '🚗 *ГИБДД старый гос. номер автомобиля:* ').replace('gibdd2_old_car_plate_number', '🚗 *ГИБДД старый гос. номер автомобиля:* ')
                                      fbex = ''
                                      line_phone = line_phone.replace(', Russia', '').replace('"', '')
                                      try:
                                        fbex = line_phone.split('"')[1]
                                      except:
                                        pass
                                      if result != '':
                                        if headr != 'mt':
                                          answer = answer+headr+'`'+result+'`<br>'
          # Отчет ----------------------------------------
          plan = 'Бесплатный'
          user_id = str(message.from_user.id)
          with open('tickets.txt', encoding='utf-8', errors='ignore') as file:
              for line in file:
                  if user_id in line:
                      time = line.split(';')[1]
                      plan = line.split(';')[2]
          with open('visione_result.html', 'w') as file:
            posnamo_css = ''
            utch_css = ''
            print('answer is '+answer)
            if answer != '':
              answer_html = answer.replace('*', '').replace('`', '')
              utch_css = "<div class='commutation'>        <svg class='img' width='39' height='39' viewBox='0 0 39 39' fill='none' xmlns='http://www.w3.org/2000/svg'><rect width='39' height='39' rx='10' fill='#1E1E1E'/><path fill-rule='evenodd' clip-rule='evenodd' d='M10 20C10 19.4696 10.2107 18.9609 10.5858 18.5858C10.9609 18.2107 11.4696 18 12 18C12.5304 18 13.0391 18.2107 13.4142 18.5858C13.7893 18.9609 14 19.4696 14 20C14 20.5304 13.7893 21.0391 13.4142 21.4142C13.0391 21.7893 12.5304 22 12 22C11.4696 22 10.9609 21.7893 10.5858 21.4142C10.2107 21.0391 10 20.5304 10 20ZM18 20C18 19.4696 18.2107 18.9609 18.5858 18.5858C18.9609 18.2107 19.4696 18 20 18C20.5304 18 21.0391 18.2107 21.4142 18.5858C21.7893 18.9609 22 19.4696 22 20C22 20.5304 21.7893 21.0391 21.4142 21.4142C21.0391 21.7893 20.5304 22 20 22C19.4696 22 18.9609 21.7893 18.5858 21.4142C18.2107 21.0391 18 20.5304 18 20ZM26 20C26 19.4696 26.2107 18.9609 26.5858 18.5858C26.9609 18.2107 27.4696 18 28 18C28.5304 18 29.0391 18.2107 29.4142 18.5858C29.7893 18.9609 30 19.4696 30 20C30 20.5304 29.7893 21.0391 29.4142 21.4142C29.0391 21.7893 28.5304 22 28 22C27.4696 22 26.9609 21.7893 26.5858 21.4142C26.2107 21.0391 26 20.5304 26 20Z' fill='#0071F5'/></svg>        <h2 class='block-header'>Данные из утечек</h2>        <h4 class='data'>"+answer_html+"</h4>    </div>"
            if nameqs_html != '':
              posnamo_css = "<div class='commutation'>        <svg class='img' width='39' height='39' viewBox='0 0 39 39' fill='none' xmlns='http://www.w3.org/2000/svg'><rect width='39' height='39' rx='10' fill='#1E1E1E'/><path d='M13.012 25H28V11C28 10.4696 27.7893 9.96086 27.4142 9.58579C27.0391 9.21071 26.5304 9 26 9H13C11.794 9 10 9.799 10 12V26C10 28.201 11.794 29 13 29H28V27H13.012C12.55 26.988 12 26.805 12 26C12 25.195 12.55 25.012 13.012 25V25Z' fill='#0071F5'/><path d='M15 13H24V15H15V13Z' fill='black'/></svg>        <h2 class='block-header'>Возможные имена</h2>        <h4 class='data'>"+nameqs_html+"</h4>    </div>"
            gghhjjhh = fiof_html+address_html+domruu_html+emcd_html
            poslinf_css = ''
            if gghhjjhh != '':
              poslinf_css = "<div class='commutation'>        <svg class='img' width='39' height='39' viewBox='0 0 39 39' fill='none' xmlns='http://www.w3.org/2000/svg'><rect width='39' height='39' rx='10' fill='#1E1E1E'/><path d='M10.6667 30C10.6667 30 9 30 9 28.25C9 26.5 10.6667 21.25 19 21.25C27.3333 21.25 29 26.5 29 28.25C29 30 27.3333 30 27.3333 30H10.6667ZM19 19.5C20.3261 19.5 21.5979 18.9469 22.5355 17.9623C23.4732 16.9777 24 15.6424 24 14.25C24 12.8576 23.4732 11.5223 22.5355 10.5377C21.5979 9.55312 20.3261 9 19 9C17.6739 9 16.4021 9.55312 15.4645 10.5377C14.5268 11.5223 14 12.8576 14 14.25C14 15.6424 14.5268 16.9777 15.4645 17.9623C16.4021 18.9469 17.6739 19.5 19 19.5Z' fill='#0071F5'/></svg><h2 class='block-header'>Личность</h2>        <h4 class='data'>"+fiof_html+address_html+domruu_html+emcd_html+"</h4>    </div>".replace("<div class='commutation'>        <img src='https://svgshare.com/i/hHJ.svg' class='img'>        <h2 class='block-header'>Личность</h2>        <h4 class='data'></h4>    </div>", "")
            soc_htm = yandexx_html+ok_html+vk_html
            soc_css = ''
            if soc_htm != '':
              soc_css = "<div class='commutation'>        <svg class='img' width='39' height='39' viewBox='0 0 39 39' fill='none' xmlns='http://www.w3.org/2000/svg'><rect width='39' height='39' rx='10' fill='#1E1E1E'/><path d='M27.4987 19.2694C29.5246 19.2694 31.1675 17.6329 31.1675 15.6135C31.1675 13.5946 29.5246 11.9576 27.4987 11.9576C25.4712 11.9576 23.828 13.5949 23.828 15.6135C23.8277 17.6329 25.4712 19.2694 27.4987 19.2694Z' fill='#0071F5'/><path d='M11.7356 20.5559C13.377 20.5559 14.7082 19.2309 14.7082 17.5955C14.7082 15.9596 13.377 14.6341 11.7356 14.6341C10.0937 14.6341 8.76305 15.9596 8.76305 17.5955C8.76305 19.2312 10.0935 20.5559 11.7356 20.5559V20.5559ZM11.7356 21.2321C9.85063 21.2321 8.46873 22.8865 8.46873 24.5955V25.746C8.46873 25.9087 8.60185 26.0424 8.76565 26.0424H14.7048C14.8692 26.0424 15.0023 25.9087 15.0023 25.746V24.5955C15.0023 22.8865 13.6204 21.2321 11.7356 21.2321ZM19.232 20.6968C17.1377 20.6968 15.6018 22.5352 15.6018 24.4345V25.713C15.6018 25.8937 15.7498 26.0424 15.9318 26.0424H22.5311C22.6186 26.0424 22.7025 26.0078 22.7645 25.946C22.8264 25.8843 22.8613 25.8004 22.8616 25.713V24.4345C22.8618 22.5355 21.3263 20.6968 19.232 20.6968ZM27.4981 20.1032C25.1711 20.1032 23.465 22.1458 23.465 24.2564V25.6766C23.465 25.8775 23.6293 26.0424 23.8316 26.0424H31.1636C31.3669 26.0424 31.5313 25.8773 31.5313 25.6766V24.2564C31.5313 22.146 29.8251 20.1032 27.4981 20.1032V20.1032Z' fill='#0071F5'/><path d='M19.232 19.9464C21.056 19.9464 22.5347 18.4732 22.5347 16.6559C22.5347 14.8385 21.056 13.3653 19.232 13.3653C17.4079 13.3653 15.9292 14.8385 15.9292 16.6559C15.9292 18.4732 17.4079 19.9464 19.232 19.9464Z' fill='#0071F5'/></svg><h2 class='block-header'>Социальные сети</h2>        <h4 class='data'>"+yandexx_html+ok_html+vk_html+"</h4>    </div>".replace("<div class='commutation'>        <img src='https://svgshare.com/i/hLK.svg' class='img'>        <h2 class='block-header'>Социальные сети</h2>        <h4 class='data'></h4>    </div>", "")
            pogogog = sberbank_message_html+tgis_html+whwh_html+tg_html+clvob_html+nd
            check_css = ''
            if pogogog != '':
              check_css = "<div class='commutation'>        <svg class='img' width='39' height='39' viewBox='0 0 39 39' fill='none' xmlns='http://www.w3.org/2000/svg'><rect width='39' height='39' rx='10' fill='#1E1E1E'/><path d='M10.7372 20L16.787 28L26.8701 12' stroke='#0071F5' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/></svg>        <h2 class='block-header'>Чекеры</h2>        <h4 class='data'>"+sberbank_message_html+tgis_html+''+whwh_html+tg_html+clvob_html+nd+"</h4>    </div>".replace("<div class='commutation'>        <img src='https://svgshare.com/i/hLW.svg' class='img'>        <h2 class='block-header'>Чекеры</h2>        <h4 class='data'></h4>    </div>", "")
            obyaby = ''
            if obyavss != 'Не обнаружены':
              obyaby = "<div class='commutation'>        <svg class ='img' width='39' height='39' viewBox='0 0 39 39' fill='none' xmlns='http://www.w3.org/2000/svg'><rect width='39' height='39' rx='10' fill='#1E1E1E'/><path d='M28.436 19.4124L20.0491 10.5801C19.6977 10.2101 19.2133 10 18.7099 10H11.8996C10.8548 10 10 10.9002 10 12.0005V19.1723C10 19.7024 10.1995 20.2126 10.5604 20.5826L18.9473 29.4149C19.6882 30.195 20.8945 30.195 21.6353 29.4149L28.4455 22.2431C29.1864 21.4629 29.1864 20.2026 28.436 19.4124ZM14.2742 16.0015C13.4858 16.0015 12.8495 15.3313 12.8495 14.5011C12.8495 13.6709 13.4858 13.0008 14.2742 13.0008C15.0625 13.0008 15.6989 13.6709 15.6989 14.5011C15.6989 15.3313 15.0625 16.0015 14.2742 16.0015Z' fill='#0071F5'/></svg>        <h2 class='block-header'>Обьявления</h2>        <h4 class='data'>"+obyavss+"</h4>    </div>".replace("<div class='commutation'>        <img src='https://svgshare.com/i/hLC.svg' class='img'>        <h2 class='block-header'>Обьявления</h2>        <h4 class='data'></h4>    </div>", "")
            file.write("<!DOCTYPE html><html lang='en'><head>    <meta charset='UTF-8'>    <title>Отчет по номеру: "+phonse+"</title>    <style>        * {        box-sizing: border-box;        }        body {         width: 80%;max-width: 720px;        }        .back {            position: absolute;            width: 30px;            height: 30px;            left: 20px;            top: 27px;        }        .result_header {            position: absolute;             height: 18px;            left: 69px;            top: 19px;            font-family: 'Inter';            font-style: normal;            font-weight: 400;            font-size: 15px;            line-height: 18px;            letter-spacing: -0.02em;            color: #EBEBEB;        }               .block-header {        position: absolute;width: 263px;height: 18px;margin-left: 75px;margin-top: -35px;font-family: 'Inter';font-style: normal;font-weight: 500;font-size: 15px;line-height: 18px;letter-spacing: -0.02em;color: #FFFFFF;        }        .img {        margin-left: 20px;        margin-top: 100px;        }        .data {        position: absolute;margin-top: 0px;margin-left: 75px;font-family: 'Inter';font-style: normal;font-weight: 400;font-size: 15px;line-height: 18px;letter-spacing: -0.01em;color: #CFCFCF;        }        .data-names {        position: absolute;width: 271px;height: 72px;margin-top: 0px;margin-left: 75px;font-family: 'Inter';font-style: normal;font-weight: 400;font-size: 15px;line-height: 18px;letter-spacing: -0.01em;color: #CFCFCF;        }        .more {        margin-top: 100px;        }        .whatsapp-button {        margin-left: 75px;        }        .button {        margin-left: 10px;        }    </style></head><body bgcolor='#0b0b0b'>    <div class='header'>        <a class='back' href='https://t.me/visionerobot' ><svg width='30' height='30' viewBox='0 0 30 30' fill='none' xmlns='http://www.w3.org/2000/svg'><circle cx='15' cy='15' r='15' fill='#1C1C1C'/><path d='M9.29289 14.2929C8.90237 14.6834 8.90237 15.3166 9.29289 15.7071L15.6569 22.0711C16.0474 22.4616 16.6805 22.4616 17.0711 22.0711C17.4616 21.6805 17.4616 21.0474 17.0711 20.6569L11.4142 15L17.0711 9.34315C17.4616 8.95262 17.4616 8.31946 17.0711 7.92893C16.6805 7.53841 16.0474 7.53841 15.6569 7.92893L9.29289 14.2929ZM11 14H10V16H11V14Z' fill='#0358D9'/></svg></a>        <h3 class='result_header'>Отчет по номеру: "+phonse+"</h3>    </div>    <div class='commutation'>        <svg class='img' width='39' height='39' viewBox='0 0 39 39' fill='none' xmlns='http://www.w3.org/2000/svg'><rect width='39' height='39' rx='10' fill='#1E1E1E'/><path d='M19 31C19 31 28 22.8264 28 16.625C28 14.3375 27.0518 12.1437 25.364 10.5262C23.6761 8.9087 21.3869 8 19 8C16.6131 8 14.3239 8.9087 12.636 10.5262C10.9482 12.1437 10 14.3375 10 16.625C10 22.8264 19 31 19 31ZM19 20.9375C17.8065 20.9375 16.6619 20.4831 15.818 19.6744C14.9741 18.8656 14.5 17.7687 14.5 16.625C14.5 15.4813 14.9741 14.3844 15.818 13.5756C16.6619 12.7669 17.8065 12.3125 19 12.3125C20.1935 12.3125 21.3381 12.7669 22.182 13.5756C23.0259 14.3844 23.5 15.4813 23.5 16.625C23.5 17.7687 23.0259 18.8656 22.182 19.6744C21.3381 20.4831 20.1935 20.9375 19 20.9375Z' fill='#0071F5'/></svg>        <h2 class='block-header'>Сведения о коммутации устройства</h2>        <h4 class='data'>"+fstep_html+"</h4>    </div>    "+posnamo_css+"    "+poslinf_css+"    "+soc_css+"    "+check_css+"    <br>    "+obyaby+"    <div class='more'>        <svg class='img' width='39' height='39' viewBox='0 0 39 39' fill='none' xmlns='http://www.w3.org/2000/svg'><rect width='39' height='39' rx='10' fill='#1E1E1E'/><path d='M21.5443 17.4563C20.7252 16.6376 19.6144 16.1776 18.4563 16.1776C17.2981 16.1776 16.1874 16.6376 15.3683 17.4563L12.2793 20.5443C11.4602 21.3634 11 22.4744 11 23.6328C11 24.7912 11.4602 25.9022 12.2793 26.7213C13.0984 27.5404 14.2094 28.0006 15.3678 28.0006C16.5262 28.0006 17.6372 27.5404 18.4563 26.7213L20.0003 25.1773' stroke='#0071F5' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/><path d='M18.4563 20.5443C19.2754 21.3631 20.3861 21.823 21.5443 21.823C22.7024 21.823 23.8132 21.3631 24.6323 20.5443L27.7213 17.4563C28.5404 16.6372 29.0006 15.5262 29.0006 14.3678C29.0006 13.2094 28.5404 12.0984 27.7213 11.2793C26.9022 10.4602 25.7912 10 24.6328 10C23.4744 10 22.3634 10.4602 21.5443 11.2793L20.0003 12.8233' stroke='#0071F5' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/></svg>        <h2 class='block-header'>Полезные ссылки для дальнейшей разведки...</h2>        <br>        <br>        <a class='whatsapp-button' href='https://wa.me/"+phonse+"'><button>Whatsapp</button></a>        <a class='button' href='https://t.me/+"+phonse+"'><button>Telegram</button></a>        <a class='button' href='https://viber.click/"+phonse+"'><button>Viber</button></a>        <a class='button' href='https://yandex.ru/search/?text="+phonse+"'><button>Яндекс</button></a>        <a class='button' href='https://www.google.com/search?q="+phonse+"'><button>Google</button></a>        <a class='button' href='https://intelx.io/?s="+phonse+"'><button>IntelX</button></a>    </div>"+utch_css+"</body></html>")
          
          if plan == 'Бесплатный':
              await message.answer('Извините, но HTML-отчеты доступны по подписке Профи.')
          else:
              await message.reply_document(open('visione_result.html', 'rb'))


@dp.message_handler(commands=['inbuy'])
async def main(message: types.Message):
  arg = message.get_args().replace("['", '').replace("']", '')
  argi = arg
  print(argi)
  if 'import' in argi:
    pass
  try:
          
          uid = str(message.from_user.id)
          
          random_code = random.randint(1, 1000000)
          cost = argi
          
          check_true = int(argi)
          with open('buyings.txt', 'a') as f:
            f.write(uid+';'+cost+';;\n')
          if config.pay_to_nick:
              link = f"https://qiwi.com/payment/form/99999?extra%5B%27account%27%5D={config.nick}&amountInteger={cost}&amountFraction=0&extra%5B%27comment%27%5D={random_code}&currency=643&blocked%5B0%5D=sum&blocked%5B1%5D=comment&blocked%5B2%5D=account"
      
              payment = InlineKeyboardMarkup()
              payment.add(InlineKeyboardButton('Проверить оплату', callback_data = f'check_payment_{random_code}'), InlineKeyboardButton('Перейти к оплате', url=link))
      
              await message.reply(f'*✉️ Положите деньги на счет ✉️*\n\n📱 *Никнейм:* `{config.nick}`\n🔐 *Комментарий:* `{random_code}`\n💰 *Цена:* `{cost}р`\n\n🚀 _Для удобства перейдите по ссылке._', reply=False, reply_markup=payment, parse_mode='Markdown')
          else:
              link = f"https://qiwi.com/payment/form/99?extra%5B%27account%27%5D={config.number}&amountInteger={cost}&amountFraction=0&extra%5B%27comment%27%5D={random_code}&currency=643&blocked%5B0%5D=sum&blocked%5B1%5D=comment&blocked%5B2%5D=account"
      
              payment = InlineKeyboardMarkup()
              payment.add(InlineKeyboardButton('Проверить оплату', callback_data = f'check_payment_{random_code}'), InlineKeyboardButton('Перейти к оплате', url=link))
      
              await message.reply(f'*✉️ Положите деньги на счет ✉️*\n\n📱 *Номер:* `{config.number}`\n🔐 *Комментарий:* `{random_code}` (`ОБЯЗАТЕЛЬНО УКАЗЫВАТЬ`)\n💰 *Цена:* `{cost}р`\n\n🚀 _Для удобства перейдите по ссылке._', reply=False, reply_markup=payment, parse_mode='Markdown')
              
  except:
          await message.answer('*Некорректный ввод!*\n_Пример правильного ввода:_ /inbuy 100', parse_mode='Markdown')

def check_sub_channel(chat_member):
  print(chat_member['status'])
  if chat_member['status'] != 'left':
    return True
  else:
    return False


@dp.message_handler(commands=['start'])
async def main(message: types.Message):
    if check_sub_channel(await bot.get_chat_member(chat_id='@visiiione', user_id=message.from_user.id)):
        global z
        z = 0
        subn = InlineKeyboardButton('Подписаться', url='https://t.me/visiiione')
        subkaa = InlineKeyboardMarkup.add(subn)
        await message.answer('*Здарова, брат!* _Бот принимает такие данные, как:_\n\n📲 *Номер телефона* (`Пример: +79876543210, +7 987 654 32 10, +7 (987) 654-32-10, 79876543210`)\n📧 *Адрес эл. почты* (`Пример: aroundtheworld@gmail.com`)\n💎 *Telegram* (`Пример: #446752031`)\n🌐 *IP-адрес* (`Пример: 8.8.8.8`)\n\n⁉️ *Другое* (`Пример: *ФИО,Фамилия и т.п.`)', reply_markup=nav.menu_b, parse_mode="Markdown")
        arg = message.get_args().replace("['", '').replace("']", '')
        argi = arg
        with open('exists.txt') as file:
          for line in file:
            if str(message.from_user.id) in line:
              
              z = 1
        
        with open('refff.txt', 'a') as file:
              print(z)
              if z == 0:
                ff = str(arg)+'\n'
                file.write(ff+'\n')
                await bot.send_message(argi, text='💡* Тук-тук... *К вам пришел реферал!', parse_mode='Markdown')
                
        with open('exists.txt', 'a') as file:
          file.write(str(message.from_user.id)+'\n')
    else:
        await message.answer('Подпишитесь, чтобы пользоваться ботом. После подписки заного пропишите команду /start или, если вы перешли по реферальной ссылке, перейдите по ней заного.', reply_markup=nav.subchanneldonw)
    
# --------------------------------------------------------------
# Обработчик ---------------------------------------------------

  






  
@dp.message_handler()
@dp.throttled(anti_flood,rate=3)
async def buttons(message: types.Message):
    global tarifan
    tarifan = 0
    user_id = str(message.from_user.id)
    with open('tickets.txt', encoding='utf-8', errors='ignore') as file:
              for line in file:
                if user_id in line:
                  tarifan = 1
    token_yandex = '7d982772d748841b9bc505d72c131845b59f4d3977b7a303bb8a6809a609c892'
    indata = message.text
    phonse = indata.replace('+', '').replace('-', '').replace('(', '').replace(')', '').replace(' ', '')
    print(str(tarifan)+'t')
    try:
      phonse = int(phonse)
      ogogg = 0
    except:
      ogogg = 1
    if 'import' in indata:
      pass
    if ogogg == 0:
        phonse = indata.replace('+', '').replace('-', '').replace('(', '').replace(')', '').replace(' ', '')
        lenz = len(phonse)
        validat = requests.get('	https://demo.phoneinfoga.crvx.fr/api/numbers/'+phonse+'/scan/local')
        if validat.status_code == 200:
          with open('alarm.txt', encoding='utf-8', errors='ignore') as file:
              for line in file:
                  if phonse in line:
                    id = line.split(';')[0]
                    await bot.send_message(id, text="🥶 *СРОЧНО!* Вас пытались пробить!", parse_mode='Markdown')
          if lenz == 11:
              global phone
              phone = phonse[1:]
              phonse = phonse[1:]
              phonse = '7' + phonse
          else:
              phone = phonse
          # Дефолт данные -------------------
  
          fstep_msg = await message.answer('📍 *Определяем страну, регион и оператора...*', parse_mode="Markdown")
          async with aiohttp.ClientSession() as session:
            async with session.get(f'https://fincalculator.ru/api/tel/{phonse}') as SBnum:
              #SBnum = requests.get(f"https://fincalculator.ru/api/tel/{phonse}")
              datae = await SBnum.json()
          # перенос номера -----------------------------
          
          #urlMNP = f"https://xn----dtbofgvdd5ah.xn--p1ai/php/mnp.php?nomer={phonse}"
          mnp = 'Неизвестно'
          whatsapp = InlineKeyboardButton('✅ Whatsapp', url='wa.me/' + phonse)
          viber = InlineKeyboardButton('⚛ Viber', url='viber.click/' + phonse)
          telega = InlineKeyboardButton('💎 Телеграм', url='t.me/+' + phonse)
          yandexs = InlineKeyboardButton('㊗️ Яндекс', url='https://yandex.ru/search/?text='+phonse)
          goog = InlineKeyboardButton('🌐 Google', url='https://www.google.com/search?q='+phonse)
          name='empty'
          head = {
                "Host": "api.vkpay.io",
                "Accept": "application/json, text/plain, */*",
                "Origin": "https://ea-miniapp.vkpay.io",
                "X-App-Params": '{"vk_access_token_settings":"notify,friends,groups","vk_app_id":"7131443","vk_are_notifications_enabled":"0","vk_experiment":"eyIxNjE4IjowfQ","vk_is_app_user":"1","vk_is_favorite":"0","vk_language":"ru","vk_platform":"desktop_web","vk_ref":"other","vk_ts":"1650541292","vk_user_id":"616028231","sign":"zOQRbuQQcD95SmmTcHR_EtmeDkhwL4VCjQ7LS6PcYMI"}',
                "X-VKApp-Token": "f7b1f08d-ee0c-479f-bdb0-912bd38ddaa9"
            }
           
          async with aiohttp.ClientSession(headers=head) as session:
                  async with session.post("https://api.vkpay.io/visa-alias/p2p/options", json={"phone": str(phonse)}) as r:
                    r = await r.json()
                    print(r)
                    data = r
                    # data = json.loads(r.text)
            
                    name = data["additional_data"]["user_name"].replace(' ', '+')
          vkments = InlineKeyboardButton('📢 Искать ВК', url='https://www.social-searcher.com/social-buzz/?q5='+name)
          if name != '':
            variations = InlineKeyboardMarkup().add(whatsapp, viber, telega, yandexs, goog, vkments)
          else:
            variations = InlineKeyboardMarkup().add(whatsapp, viber, telega, yandexs, goog)
  
          await fstep_msg.delete()
          mnp_msg = await message.answer('📶 *Определяем перенос номера...*', parse_mode="Markdown")
          # Перенос номера ------------------------
          mnp = ''
          try:
            urlMNP = f"https://xn----dtbofgvdd5ah.xn--p1ai/php/mnp.php?nomer={phonse}"
            mnpSiteSourc = requests.get(urlMNP).text.strip()
            mnp = mnpSiteSourc.replace('no',
                                           'Не переносился')
          except:
            mnp = 'Неизвестно'
          try:
              countrys = datae["country"]
              regions = datae["region"]
              operators = datae["operator"]
              if countrys != 'Россия':
                  fstep = f'📲 *Номер телефона:* `{phonse}`\n ├ *Страна:* `{countrys}`\n ├ *Перенос номера:* `{mnp}`\n └ *Оператор:* `{regions}`'
                  fstep_html = f'Страна {countrys}<br>Перенос номера: {mnp}<br>Оператор: {regions}'
              else:
                  fstep = f'📲 *Номер телефона:* `{phonse}`\n ├ *Страна:* `{countrys}`\n ├ *Регион:* `{regions}`\n ├ *Перенос номера:* `{mnp}`\n └ *Оператор:* `{operators}`'
                  fstep_html = f'Страна {countrys}<br>Регион: {regions}<br>Перенос номера: {mnp}<br>Оператор: {operators}'
          except:
              countrys = 'Не опознано'
              regions = 'Не опознано'
              operators = 'Не опознано'
          await mnp_msg.delete()
          # Сбер -----------------------------------------
          sber_msg = await message.answer('💳 *Ищем Сбербанк...*', parse_mode="Markdown")
          sberbank_message = ''
          maskedPhone = ''
          tarifan = 0
          user_id = str(message.from_user.id)
          with open('tickets.txt', encoding='utf-8', errors='ignore') as file:
                    for line in file:
                      if user_id in line:
                        tarifan = 1
          if tarifan == 1:
            try:
                sberbank = requests.post(f"https://securepayments.sberbank.ru/sbersafe/client/find?phone={phone}")
                datas = sberbank.json()
    
                get_date = datas['client']['createdDate']
                get_date2 = get_date[:10]
                rep1 = get_date2.replace(".01.", " января ")
                rep2 = rep1.replace(".02.", " февраля ")
                rep3 = rep2.replace(".03.", " марта ")
                rep4 = rep3.replace(".04.", " апреля ")
                rep5 = rep4.replace(".05.", " мая ")
                rep6 = rep5.replace(".06.", " июня ")
                rep7 = rep6.replace(".07.", " июля ")
                rep8 = rep7.replace(".08.", " августа ")
                rep9 = rep8.replace(".09.", " сентября ")
                rep10 = rep9.replace(".10.", " октября ")
                rep11 = rep10.replace(".11.", " ноября ")
                rep12 = rep11.replace(".12.", " декабря ")
                rep13 = get_date[11:-7]
    
                maskedPhone = datas['client']['maskedPhone']
                created_date = f'{rep12} г. в {rep13}'
                sberbank_message = f"💳 *Сбербанк:* `есть` ({created_date})\n"
                sberbank_message_html = f"Сбербанк: есть ({created_date})<br>"
            except:
                sberbank_message = ''
                sberbank_message_html = ''
            await sber_msg.delete()
          else:
            try:
                sberbank = requests.post(f"https://securepayments.sberbank.ru/sbersafe/client/find?phone={phone}")
                datas = sberbank.json()
    
                get_date = datas['client']['createdDate']
                get_date2 = get_date[:10]
                rep1 = get_date2.replace(".01.", " января ")
                rep2 = rep1.replace(".02.", " февраля ")
                rep3 = rep2.replace(".03.", " марта ")
                rep4 = rep3.replace(".04.", " апреля ")
                rep5 = rep4.replace(".05.", " мая ")
                rep6 = rep5.replace(".06.", " июня ")
                rep7 = rep6.replace(".07.", " июля ")
                rep8 = rep7.replace(".08.", " августа ")
                rep9 = rep8.replace(".09.", " сентября ")
                rep10 = rep9.replace(".10.", " октября ")
                rep11 = rep10.replace(".11.", " ноября ")
                rep12 = rep11.replace(".12.", " декабря ")
                rep13 = get_date[11:-7]
    
                maskedPhone = datas['client']['maskedPhone']
                created_date = f'{rep12} г. в {rep13}'
                sberbank_message = f"💳 *Сбербанк:* `есть`\n"
                sberbank_message_html = 'Сбербанк: есть<br>'
            except:
                sberbank_message = ''
                sberbank_message_html = ''
            await sber_msg.delete()
          # 2GIS ----------------------------------------
          tgis_html = ''
          tgis = ''
          head = {'Host': 'id.2gis.com',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
  'Content-Length': '30'}
          rt = requests.post('https://id.2gis.com/api/v1/send_confirm_sms',
                             json={"phone": phonse, "locale": "ru-RU"}, headers=head).json()
          print(rt)
          try:
              exe = rt['phone']
              vho = 1
          except Exception as e:
              print(f'Exception 2GIS is: {e}')
              tgis = ''
              vho = 0
          if vho == 1:
              tgis = '📗 *Аккаунт на 2ГИС:* `существует`  (`мы отправили код подтверждения`)'
              tgis_html = 'ДубльГИС: существует<br>'
          else:
                    tgis = ''
                    tgis_html = ''
                
          
                  
          
          # Одноклассники -------------------------------
          ok_msg = await message.answer('🆗 *Проверяем номер телефона на наличие аккаунта в Одноклассниках...*',
                                        parse_mode="Markdown")
          # одноклассники
          session = requests.Session()
          session.get(
              f'https://www.ok.ru/dk?st.cmd=anonymMain&st.accRecovery=on&st.error=errors.password.wrong&st.email={phonse}')
          request = session.get(
              f'https://www.ok.ru/dk?st.cmd=anonymRecoveryAfterFailedLogin&st._aid=LeftColumn_Login_ForgotPassword')
          root_soup = BeautifulSoup(request.content, 'html.parser')
          soup = root_soup.find('div', {'data-l': 'registrationContainer,offer_contact_rest'})
          if soup:
              account_info = soup.find('div', {'class': 'ext-registration_tx taCenter'})
              masked_email = soup.find('button', {'data-l': 't,email'})
              masked_phone = soup.find('button', {'data-l': 't,phone'})
              if masked_phone:
                  masked_phone = masked_phone.find('div', {'class': 'ext-registration_stub_small_header'}).get_text()
              if masked_email:
                  masked_email = masked_email.find('div', {'class': 'ext-registration_stub_small_header'}).get_text()
                  masked_email = f'Почта: `{masked_email}`,'
              else:
                  masked_email = ''
              if account_info:
                  masked_name = account_info.find('div', {'class': 'ext-registration_username_header'})
                  if masked_name:
                      masked_name = masked_name.get_text()
                  account_info = account_info.findAll('div', {'class': 'lstp-t'})
                  if account_info:
                      profile_info = account_info[0].get_text()
                      profile_registred = account_info[1].get_text()
                  else:
                      profile_info = None
                      profile_registred = None
              else:
                  pass
          await ok_msg.delete()
  
          try:
              age = profile_info[:7].replace(',', '')
              cityok = profile_info[8:].replace(',', '')
              age = f''
              cityok = f'`{cityok}`'
              tarifan = 0
              user_id = str(message.from_user.id)
              with open('tickets.txt', encoding='utf-8', errors='ignore') as file:
                        for line in file:
                          if user_id in line:
                            tarifan = 1
              if tarifan == 1:
                ok = f'\n🆗 *Одноклассники:* `{masked_name}` (`{profile_info}`, {masked_email} `{profile_registred})`\n'
                ok_html = f'Одноклассники: {masked_name} ({profile_info},<br> {masked_email}, {profile_registred})<br>'.replace('`', '').replace(',,', ',')
              elif tarifan == 0:
                ok = f'\n🆗 *Одноклассники:* `найдены`\n'
                ok_html = 'Одноклассники: найдены<br>'
              
          except:
              ok = ''
              cityok = ''
              age = ''
              masked_email = ''
              ok_html = ''
          # Яндекс ---------------------------------------
          yand_msg = await message.answer('㊙ *Проверяем номер телефона на наличие аккаунта на Яндекс...*',
                                          parse_mode="Markdown")
          # yandex
          try:
              eqereq = message.text.strip()
              email_login = (eqereq.split("@"))[0]
              async with aiohttp.ClientSession() as session:
                async with session.get(f"https://yandex.ru/collections/api/users/{email_login}") as yandex:
                  try:
                      yamail = phonse + '@yandex.ru'
                  except:
                      yamail = ''
                  yamailo = f', `{yamail}`'
                  yadata = await yandex.json()
                  public_id = yadata['public_id']
                  display_name = yadata['display_name']
                  try:
                      yaname = f' ({display_name})'
                  except:
                      yaname = ''
                  try:
                    if tarifan != 0:
                      yandexx = f'\n㊗ *Яндекс ID:* `{public_id}`{yaname}\n'
                      yandexx_html = f'Яндекс: {public_id}{yaname}<br>'
                    else:
                      yandexx = f'\n㊗ *Яндекс ID:* `найден`\n'
                      yandexx_html = f'Яндекс: найден<br>'
                  except:
                    if tarifan != 0:
                      yandexx = f'\n㊗ *Яндекс ID:* `{public_id}`\n'
                      yandexx_html = f'Яндекс: {public_id}<br>'
                    else:
                      yandexx = f'\n㊗ *Яндекс ID:* `найден`\n'
                      yandexx_html = f'Яндекс: найден<br>'
          except:
                  display_name = ''
                  public_id = ''
                  yandexx = ''
                  yandexx_html = ''
                  yamail = ''
                  yaname = display_name
                  if yandexx == '':
                    yamailo = ''
          await yand_msg.delete()
          # ВКонтакте -----------------------------------
          nameqs_html = ''
          vkmsg = await message.answer('🤖 *Ищем ВКонтакте...*', parse_mode="Markdown")
          try:
            head = {
                "Host": "api.vkpay.io",
                "Accept": "application/json, text/plain, */*",
                "Origin": "https://ea-miniapp.vkpay.io",
                "X-App-Params": '{"vk_access_token_settings":"notify,friends,groups","vk_app_id":"7131443","vk_are_notifications_enabled":"0","vk_experiment":"eyIxNjE4IjowfQ","vk_is_app_user":"1","vk_is_favorite":"0","vk_language":"ru","vk_platform":"desktop_web","vk_ref":"other","vk_ts":"1650541292","vk_user_id":"616028231","sign":"zOQRbuQQcD95SmmTcHR_EtmeDkhwL4VCjQ7LS6PcYMI"}',
                "X-VKApp-Token": "f7b1f08d-ee0c-479f-bdb0-912bd38ddaa9"
            }
            async with aiohttp.ClientSession(headers=head) as session:
                  async with session.post("https://api.vkpay.io/visa-alias/p2p/options", json={"phone": str(phonse)}) as r:
                    r = await r.json()
                    print(r)
                    data = r
                    # data = json.loads(r.text)
            
                    name = data["additional_data"]["user_name"]
                    hasVk = data["additional_data"]["has_vk"]
                    vk_gua = name.replace(' ', '+')
                    if name != '':
                        vk = '🤖 *ВКонтакте:* `' + name + '`\n—  Сведения про ВК пользователя: `vk.com/search?c[section]=name&c[q]=' + vk_gua + '`\n—  Получить город и аватарку: `vk.com/restore`\n'
                        vk_html = 'ВКонтакте: '+name+'<br>'
                    else:
                        vk = ''
                        vk_html = ''
            await vkmsg.delete()
          except:
            vk = ''
          # ДомРУ ----------------------------------------
          address = ''
          domru_msg = await message.answer('🏠 *Ищем адрес по договору DOM.RU...*', parse_mode="Markdown")
          tarifan = 0
          user_id = str(message.from_user.id)
          with open('tickets.txt', encoding='utf-8', errors='ignore') as file:
                    for line in file:
                      if user_id in line:
                        tarifan = 1
          if tarifan == 1:
            if "#" in message.text:
                regions = 'Иркутская область'
            if "-" in message.text:
                regions = 'Иркутская область'
            if regions == 'Москва и Московская область':
                gorod = 'msk'
            elif regions == 'Иркутская область':
                gorod = 'irkutsk'
            elif regions == 'Алтайский край':
                gorod = 'barnaul'
            elif regions == 'Пермский край':
                gorod = 'ber'
            elif regions == 'Брянская область':
                gorod = 'bryansk'
            elif regions == 'Волгоградская область':
                gorod = 'volgograd'
            elif regions == 'Воронежская область':
                gorod = 'voronezh'
            elif regions == 'Удмуртская республика':
                gorod = 'votkinsk'
            elif regions == 'Нижегородская область':
                gorod = 'dzr'
            elif regions == 'Ульяновская область':
                gorod = 'ulsk'
            elif regions == 'Воронежская область':
                gorod = 'voronezh'
            elif regions == 'Республика Марий Эл':
                gorod = 'yola'
            elif regions == 'Респубика Татарстан':
                gorod = 'kazan'
            elif regions == 'Кировская область':
                gorod = 'kirov'
            elif regions == 'Краснодарский край':
                gorod = 'krd'
            elif regions == 'Красноярский край':
                gorod = 'krsk'
            elif regions == 'Курганская область':
                gorod = 'kurgan'
            elif regions == 'Курская область':
                gorod = 'kursk'
            elif regions == 'Липецкая область':
                gorod = 'lipetsk'
            elif regions == 'Челябинская область':
                gorod = 'chel'
            elif regions == 'Тамбовская область':
                gorod = 'mich'
            elif regions == 'Новосибирская область':
                gorod = 'nsk'
            elif regions == 'Омская область':
                gorod = 'omsk'
            elif regions == 'Оренбургская область':
                gorod = 'oren'
            elif regions == 'Пензенская область':
                gorod = 'penza'
            elif regions == 'Ростовская область':
                gorod = 'rostov'
            elif regions == 'Рязанская область':
                gorod = 'ryazan'
            elif regions == 'Самарская область':
                gorod = 'samara'
            elif regions == 'Санкт-Петербург':
                gorod = 'interzet'
            elif regions == 'Саратовская область':
                gorod = 'saratov'
            elif regions == 'Воронежская область':
                gorod = 'voronezh'
            elif regions == 'Томская область':
                gorod = 'tomsk'
            elif regions == 'Тверская область':
                gorod = 'tver'
            elif regions == 'Тульская область':
                gorod = 'tula'
            elif regions == 'Тюменская область':
                gorod = 'tmn'
            elif regions == 'Республика Бурятия':
                gorod = 'ulu'
            elif regions == 'Республика Башкоторстан':
                gorod = 'ufa'
            elif regions == 'Республика Чувашия':
                gorod = 'cheb'
            elif regions == 'Ярославская область':
                gorod = 'yar'
            else:
                gorod = "msk"
            urldru = 'https://api-profile.domru.ru/v1/unauth/contract-asterisked?contact=' + phonse + '&amp;isActive=1'
    
            headersd = CaseInsensitiveDict()
            headersd["Host"] = "api-profile.domru.ru"
            headersd["Domain"] = gorod
            async with aiohttp.ClientSession(headers=headersd) as session:
              async with session.get(urldru) as resp:
                resp = await resp.json()
                domruu = ''
                try:
                  dataa = resp['contacts'][0]['address']
                  domruu = f'🔌 *Найден договор с интернет провайдером ДОМ.RU*\n🏠 Адрес предоставления услуги: `{dataa}`\n'
                  domruu_html = 'ДомРУ: '+dataa+'<br>'
                except:
                  domruu = ''
                  domruu_html = ''
                phonke = '+'+phonse
                phonee = phonse
                phonio = phonee.replace('', ' ')
                dd = phonio.split()[0]+'/'+phonio.split()[1]+'/'+phonio.split()[2]+'/'+phonio.split()[3]+'/'+phonio.split()[4]+'/'+phonio.split()[5]
                adcs = ''
                try:
                  rw = requests.get('https://saverudata.info/db/'+dd+'/00000-99999.json').json()
                  adcs = ''
                  address_html = ''
                  for i in range(len(rw)):
                                if phonke in rw[i]:
                                    ee = i
                                    datacd = rw[ee]
                                    print(rw[ee])
                                    
                                    if datacd[1] != '':
                                      adcs = adcs+f'{datacd[1]}, {datacd[2]}, дом {datacd[3]}, подьезд {datacd[4]}, кв {datacd[5]}\n'
                                else:
                                      pass
                  try:
                                dataa = resp['contacts'][0]['address']
                                address = f'🏠 *Возможные места проживания*: `{adcsasdsda}`\n'
                                address_html = f'Возможные адреса: {adcsasdsda}<br>'
                  except:
                              if adcs != '':
                                address = f'🏠 *Возможные места проживания*: `{adcs}`\n'
                                address_html = f'Возможные адреса: {adcs}<br>'
                except:
                  address = ''
                  address_html = ''
          elif tarifan == 0:
              if "#" in message.text:
                  regions = 'Иркутская область'
              if "-" in message.text:
                  regions = 'Иркутская область'
              if regions == 'Москва и Московская область':
                  gorod = 'msk'
              elif regions == 'Иркутская область':
                  gorod = 'irkutsk'
              elif regions == 'Алтайский край':
                  gorod = 'barnaul'
              elif regions == 'Пермский край':
                  gorod = 'ber'
              elif regions == 'Брянская область':
                  gorod = 'bryansk'
              elif regions == 'Волгоградская область':
                  gorod = 'volgograd'
              elif regions == 'Воронежская область':
                  gorod = 'voronezh'
              elif regions == 'Удмуртская республика':
                  gorod = 'votkinsk'
              elif regions == 'Нижегородская область':
                  gorod = 'dzr'
              elif regions == 'Ульяновская область':
                  gorod = 'ulsk'
              elif regions == 'Воронежская область':
                  gorod = 'voronezh'
              elif regions == 'Республика Марий Эл':
                  gorod = 'yola'
              elif regions == 'Респубика Татарстан':
                  gorod = 'kazan'
              elif regions == 'Кировская область':
                  gorod = 'kirov'
              elif regions == 'Краснодарский край':
                  gorod = 'krd'
              elif regions == 'Красноярский край':
                  gorod = 'krsk'
              elif regions == 'Курганская область':
                  gorod = 'kurgan'
              elif regions == 'Курская область':
                  gorod = 'kursk'
              elif regions == 'Липецкая область':
                  gorod = 'lipetsk'
              elif regions == 'Челябинская область':
                  gorod = 'chel'
              elif regions == 'Тамбовская область':
                  gorod = 'mich'
              elif regions == 'Новосибирская область':
                  gorod = 'nsk'
              elif regions == 'Омская область':
                  gorod = 'omsk'
              elif regions == 'Оренбургская область':
                  gorod = 'oren'
              elif regions == 'Пензенская область':
                  gorod = 'penza'
              elif regions == 'Ростовская область':
                  gorod = 'rostov'
              elif regions == 'Рязанская область':
                  gorod = 'ryazan'
              elif regions == 'Самарская область':
                  gorod = 'samara'
              elif regions == 'Санкт-Петербург':
                  gorod = 'interzet'
              elif regions == 'Саратовская область':
                  gorod = 'saratov'
              elif regions == 'Воронежская область':
                  gorod = 'voronezh'
              elif regions == 'Томская область':
                  gorod = 'tomsk'
              elif regions == 'Тверская область':
                  gorod = 'tver'
              elif regions == 'Тульская область':
                  gorod = 'tula'
              elif regions == 'Тюменская область':
                  gorod = 'tmn'
              elif regions == 'Республика Бурятия':
                  gorod = 'ulu'
              elif regions == 'Республика Башкоторстан':
                  gorod = 'ufa'
              elif regions == 'Республика Чувашия':
                  gorod = 'cheb'
              elif regions == 'Ярославская область':
                  gorod = 'yar'
              else:
                  gorod = "msk"
              urldru = 'https://api-profile.domru.ru/v1/unauth/contract-asterisked?contact=' + phonse + '&amp;isActive=1'
      
              headersd = CaseInsensitiveDict()
              headersd["Host"] = "api-profile.domru.ru"
              headersd["Domain"] = gorod
              async with aiohttp.ClientSession(headers=headersd) as session:
                async with session.get(urldru) as resp:
                  resp = await resp.json()
                  domruu = ''
                  try:
                      dataa = resp['contacts'][0]['address']
                      domruu = f'🔌 *Найден договор с интернет провайдером ДОМ.RU*\n🏠 Адрес предоставления услуги: `{dataa}`\n'
                      domruu_html = f'ДомРУ: {dataa}<br>'
                  except:
                    domruu = ''
                    domruu_html = ''
                  phonke = '+'+phonse
                  phonee = phonse
                  phonio = phonee.replace('', ' ')
                  dd = phonio.split()[0]+'/'+phonio.split()[1]+'/'+phonio.split()[2]+'/'+phonio.split()[3]+'/'+phonio.split()[4]+'/'+phonio.split()[5]
                  try:
                    rw = requests.get('https://saverudata.info/db/'+dd+'/00000-99999.json').json()
                    adcs = ''
                    for i in range(len(rw)):
                                  if phonke in rw[i]:
                                      ee = i
                                      datacd = rw[ee]
                                      print(rw[ee])
                                      
                                      if datacd[1] != '':
                                        adcs = adcs+f'{datacd[1]}, {datacd[2]}, дом {datacd[3]}, подьезд {datacd[4]}, кв {datacd[5]}\n'
                                  else:
                                        pass
                    try:
                        address_html = ''
                        address = osdfo
                    except:
                        if adcs != '':
                          address = f'🏠 *Возможные места проживания*: `найдено`\n'
                          address_html = f'Возможные адреса: найдено<br>'
                  except:
                    address = ''
                    address_html = ''
          await domru_msg.delete()
          # Телеграм -------------------------------------
          tg = ''
          tg_html = ''
          rt = requests.get('https://capitalcloudytriangle.hkfdsfsdfh.repl.co/info?d='+phonse).content.decode("utf-8", "ignore")
          rt = str(rt).replace('b', '').replace("'", '')
          print(rt)
          tg = '🛅 *Telegram: *`'+str(rt)+'`\n'
          tg = tg.replace('🛅 *Telegram: *`Упс... Такого контакта в TG не обнаружено.`\n', '')
          tg_html = 'Telegram: '+str(rt)+"<br>"
          tg_html = tg_html.replace('Telegram: Упс... Такого контакта в TG не обнаружено.<br>', 'Telegram: ')
          # Чек вацап
          nameqs = ''
          try:
            whatt = await message.answer('✅ *Проверяем существование Whatsapp...*', parse_mode='Markdown')
            whwh = ''
            permq = 1
            with open('tickets.txt', encoding='utf-8', errors='ignore') as file:
                              for line in file:
                                if user_id in line:
                                  permq = 1
            if permq == 1:
              rwh = requests.get('http://ovh.foxodever.com:65535/whatsapp/'+phonse).json()
              whwh_nac = rwh['exists']
              print(whwh)
              whwh = str(whwh_nac).replace('True', '\n✅* Whatsapp:* `есть`').replace('False', '')
              whwh_html = str(whwh_nac).replace('True', 'Whatsapp: есть<br>').replace('False', '')
            else:
              whwh = ''
              whwh_html = ''
            await whatt.delete()
          except:
            whwh = ''
            whwh_html = ''
          # Кол-во обьявлений
          obbd = await message.answer('🏪* Считаем кол-во обьявлений в интернете...*', parse_mode="Markdown")
          rrtr = requests.get('http://ovh.foxodever.com:65535/avito/'+phonse).json()
          try:
            clvobd = str(rrtr['count'])
            clvob = f'\n🏪 *Кол-во обьявлений в интернете:* `{clvobd}`'
            clvob_html = f'Кол-во обьявлений в интернете: {clvobd}<br>'
          except:
            clvob = ''
            clvob_html = ''
          await obbd.delete()
          gogop = 1
          if gogop == 1:
                      phonke = '+'+phonse
                      phonee = phonse
                      phonio = phonee.replace('', ' ')
                      dd = phonio.split()[0]+'/'+phonio.split()[1]+'/'+phonio.split()[2]+'/'+phonio.split()[3]+'/'+phonio.split()[4]+'/'+phonio.split()[5]
                      
                      
                      fiof = ''
                      emcd = ''
                      print(phonke)
                      fight = 0
                      nameqs = ''
                      fiof_html = ''
                      emcd_html = ''
                      nameqs_html = ''
                      
          try: 
              URLavito = "https://opredelitel.com/pay/7" + phone
              HEADERS = {
                  "User-Agent":
                      "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"
              }
              ra = requests.get(URLavito, headers=HEADERS)
              soup = BeautifulSoup(ra.content, 'html.parser')
              items = soup.findAll('div', class_='preview_da_line')
              comps = []
              for item in items:
                  comps.append({
                      'titlew':
                          item.find('div', class_='da_title').get_text(strip=True),
                      'infow':
                          item.find('div', class_='da_info').get_text(strip=True)
                  })
          except:
              pass
          try:
              for comp in comps:
                
                  comp['infow'] = comp['infow'].replace(' / Адрес: скрыт в ознакомительном отчёте', '')
                  obyavss = obyavss+f"Найдено обьявление: {comp['titlew']}<br>Подробная информация: {comp['infow']}<br><br>"
              if obyavss == '':
                obyavss = 'Не обнаружены'
          except:
              pass
          # Отчет ----------------------------------------
          plan = 'Бесплатный'
          user_id = str(message.from_user.id)
          with open('tickets.txt', encoding='utf-8', errors='ignore') as file:
              for line in file:
                  if user_id in line:
                      time = line.split(';')[1]
                      plan = line.split(';')[2]
          numcg = 0
          chcks = 'ℹ️ *Если информации мало,* купите _расширенный поиск_, он стоит 5 рублей (Дает ссылки на вероятные профили ВК, ОК, дает от 1 до 3 обьявлений). Чтобы заказать, используйте команду `/checking '+phonse+'`'
          with open('checking_e.txt') as file:
            for line in file:
              if phone in line:
                chcks = '❗️*По этому номеру генерировали отчет! *'
                numcg = 1
          if plan == 'Бесплатный':
              await message.answer(
              f'{fstep}\n\n{nameqs}{fiof}{address}{domruu}\n{sberbank_message}{emcd}{yandexx}{ok}{vk}{tgis}{tg}{whwh}',
              parse_mode="Markdown", reply_markup=variations, disable_web_page_preview=True)
              #await message.answer('*Если нужно* экспортировать в виде *HTML-отчета*, введите следующее: `/html НОМЕР ТЕЛЕФОНА` (пример: `/html +79876543210`)', parse_mode='Markdown')  
          else:
              await message.answer(
                  f'{fstep}\n\n{nameqs}{fiof}{address}{domruu}\n{sberbank_message}{emcd}{yandexx}{ok}{vk}{tgis}{tg}{whwh}{clvob}',
                  parse_mode="Markdown", reply_markup=variations, disable_web_page_preview=True)
          #await message.answer('*Если нужно* экспортировать в виде *HTML-отчета*, введите следующее: `/html НОМЕР ТЕЛЕФОНА` (пример: `/html +79876543210`)', parse_mode='Markdown')
              cekss = 0
              numcg = 1
              if numcg == 1:
                try:
                  ok = masked_name
                except:
                  ok = ''
                try:
                  vk = name
                except:
                  vk = 'dfneiubfuerof reherfreghregregurhiu'
                tarifan = 1
                okki = '😄 *Вероятный профиль в ОК:*\n'
                if ok != '':
                  name_okk = masked_name.split(' ')[0]
                  full_fam_len = len(masked_name.split(' ')[1])
                  first_fam = masked_name.split(' ')[1].replace('*', '')
                  query = name_okk+' '+profile_info.replace(', ', ' ')
                  answer = ''
                  okki = ''
                  zelda = ''
                  for_q = quote(query)
                  
                  try:
                              
                                URLavito = "https://ok.ru/dk?st.cmd=searchResult&st.mode=Users&st.query=" + query
                                HEADERS = {
                                    'Host': 'ok.ru',
                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
                                    'Connection': 'keep-alive',
                                    'Cookie': 'bci=-2116531667307403995; _statid=7a791825-c288-47c2-8b6e-877341a13a58; _hd=h; mtrc=%7B%22mytrackerid%22%3A53328%7D; _userIds=""; _suserIds=""; AUTHCODE=nqIFPG9MF_N5Cx4352YxqMDRhjMoxw0XKGcMoYjmf6KZSRoy0Hldpmjf7mgmd4KFaVfXrIKWuaAQEz0tPj4lsCOTaWViA5YjeyeE5yKb6pqZAPI87JN1Q9IUzvpD9pt3sNC7kHSJsvlXEdApKg_5; msg_conf=2468555756792551; _flashVersion=0; nbp=1; klos=0; JSESSIONID=967b9a9fdddf07194f430a2c5dc747a6de196a9fde104ca.a6013af9; LASTSRV=ok.ru; vdt="kxsV4uaqClVwUT54YoRNTuESxigIkLF24Oi5yyXDKHcAAABgOWyq6wTvvg3tBoR4TFO7fGilNnkzJRLiLh/uv6UVU7MmGswtDKwBijB/qzmKFXGDEN1Mx9+wARgcr22gRHh/f+FPFzHQ7ElAwKI1weniL9v5fO/QHmgQXu5rOwHIWiQE4ie8AFY="; viewport=800; CDN=; TZD=20.-122; TZ=20; TD=-122; cudr=0',
                  'Upgrade-Insecure-Requests': '1'
                                }
                                ra = requests.get(URLavito, headers=HEADERS).content
                                soup = BeautifulSoup(ra, 'html.parser')
                                items = soup.findAll('a', class_='link__91azp title-link__79ad9')
                                comps = []
                                for item in items:
                                    comps.append({
                                        'titlew':
                                            item.find('div', class_='sm__79ad9 __ellipted__79ad9').get_text(strip=True)
                                    })
                  except:
                                pass
                  try:
                                for comp in comps:
                                  zelda = zelda+comp['titlew']+', '
                  except:
                                pass
                  try:
                              
                                URLavito = "https://ok.ru/dk?st.cmd=searchResult&st.mode=Users&st.query=" + query
                                HEADERS = {
                                    'Host': 'ok.ru',
                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
                                    'Connection': 'keep-alive',
                                    'Cookie': 'bci=-2116531667307403995; _statid=7a791825-c288-47c2-8b6e-877341a13a58; _hd=h; mtrc=%7B%22mytrackerid%22%3A53328%7D; _userIds=""; _suserIds=""; AUTHCODE=nqIFPG9MF_N5Cx4352YxqMDRhjMoxw0XKGcMoYjmf6KZSRoy0Hldpmjf7mgmd4KFaVfXrIKWuaAQEz0tPj4lsCOTaWViA5YjeyeE5yKb6pqZAPI87JN1Q9IUzvpD9pt3sNC7kHSJsvlXEdApKg_5; msg_conf=2468555756792551; _flashVersion=0; nbp=1; klos=0; JSESSIONID=967b9a9fdddf07194f430a2c5dc747a6de196a9fde104ca.a6013af9; LASTSRV=ok.ru; vdt="kxsV4uaqClVwUT54YoRNTuESxigIkLF24Oi5yyXDKHcAAABgOWyq6wTvvg3tBoR4TFO7fGilNnkzJRLiLh/uv6UVU7MmGswtDKwBijB/qzmKFXGDEN1Mx9+wARgcr22gRHh/f+FPFzHQ7ElAwKI1weniL9v5fO/QHmgQXu5rOwHIWiQE4ie8AFY="; viewport=800; CDN=; TZD=20.-122; TZ=20; TD=-122; cudr=0',
                  'Upgrade-Insecure-Requests': '1'
                                }
                                ra = requests.get(URLavito, headers=HEADERS).content
                                soup = BeautifulSoup(ra, 'html.parser')
                                items = soup.findAll('div', class_='card__kq7ru __h__kq7ru')
                                comps = []
                                for item in items:
                                    comps.append({
                                        'titlew':
                                            item.find('a', class_='link__91azp photo-link__79ad9').get('href')
                                    })
                  except:
                                pass
                  try:
                                for comp in comps:
                                  answer = answer+'https://ok.ru'+comp['titlew']+', '
                  except:
                                pass
                  qwe = zelda.count(', ')
                  zelda = zelda[:-1].replace('  ', ' ')
                  for num in range(qwe):
                    num_nameok = zelda.split(', ')[num]
                    try:
                      umfmm = num_nameok.split(' ')[1]
                    except:
                      umfmm = num_nameok.split(' ')[0]
                    findname = num_nameok.split(' ')[0]
                    nfname = masked_name.split(' ')[0]
                    f_w_fmm = umfmm[0]
                    len_umfmm = len(umfmm)
                    if f_w_fmm == first_fam:
                      if len_umfmm == full_fam_len:
                        if findname == nfname: 
                          ok_profile = answer.split(', ')[num]
                          okki = okki+'`'+ok_profile+'` (`'+num_nameok+'`)\n'
                if okki != '😄 *Вероятный профиль в ОК:*\n':
                  if tarifan != 0:
                    try:
                      await message.answer(okki, parse_mode='Markdown')
                    except:
                      pass
                URLavito = "https://opredelitel.com/pay/" + str(phonse)
                HEADERS = {
                        "User-Agent":
                            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"
                    }
                ra = requests.get(URLavito, headers=HEADERS)
                soup = BeautifulSoup(ra.content, 'html.parser')
                items = soup.findAll('div', class_='preview_da_line')
                comps = []
                for item in items:
                        comps.append({
                            'titlew':
                                item.find('div', class_='da_title').get_text(strip=True),
                            'infow':
                                item.find('div', class_='da_info').get_text(strip=True)
                        })
                for comp in comps:
                        comp['infow'] = comp['infow'][:40]
                        if plan != 'Бесплатный':
                            await message.answer(
                            f"🏪 *Найдено обьявление:* `{comp['titlew']}`, \n*Подробная информация:* `{comp['infow']}`",
                            parse_mode="Markdown")
                        else:
                         pass
                try:
                    URLrep = "https://www.neberitrubku.ru/nomer-telefona/8" + phone
                    HEADERS = {
                        "User-Agent":
                            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"
                    }
                    ra = requests.get(URLrep, headers=HEADERS)
                    soup = BeautifulSoup(ra.content, 'html.parser')
                    items = soup.findAll('div', class_='categories')
                    comps = []
                    for item in items:
                        comps.append({
                            'ratee':
                                item.find('li', class_='active').get_text(strip=True)
                        })
                    for comp in comps:
                        await message.answer(f"🏅 *Найдена оценка:*  {comp['ratee']}\n", parse_mode="Markdown")
                except:
                    pass
                plan = 'Бесплатный'
                user_id = str(message.from_user.id)
                permq = 0
                with open('prems.txt', encoding='utf-8', errors='ignore') as file:
                                  for line in file:
                                    if user_id in line:
                                      permq = 1
                if permq == 1:
                                  if vk != '':
                                    vk_forlink = quote(name)
                                    print(vk+'  '+vk_forlink)
                                    rvkp = ''
                                    tryr = ''
                                    async with aiohttp.ClientSession() as session:
                                        async with session.get('https://technicalunknownlaws.hkfdsfsdfh.repl.co/info?d='+vk_forlink) as rvkp:
                                          rvkp = await rvkp.text()
                                    async with aiohttp.ClientSession() as session:
                                        async with session.get('https://helplessdarkorangesoftwaresuite.hkfdsfsdfh.repl.co/kozinak?d='+vk_forlink) as tryr:
                                          tryr = await tryr.text()
                                    async with aiohttp.ClientSession() as session:
                                        async with session.get('https://helplessdarkorangesoftwaresuite.hkfdsfsdfh.repl.co/info?d='+vk_forlink) as rv:
                                          
                                          
                                          rv = await rv.text()
                                    
                                    rvkp = str(rvkp+rv+tryr).replace('empty', '').replace('<br>', '/n')
                                    rtryt = len(rvkp)
                                    rvkp = rvkp[:-2]
                                    rvkp = rvkp.replace('/n', '\n')
      
                                    print(rvkp)
                                    
                                    await message.answer('🎯 *Поиск людей во ВКонтакте (вероятные профили, функция в бета версии):*', parse_mode='Markdown')
                                    await message.answer(rvkp)
                                    check_phone = phonse[:1]
                                    if check_phone == '7':
                                        #BDrom
                                        code_region = phonse[1:4]
                                        middle_phone = phonse[4:7]
                                        last_phone = phonse[7:11]
                                        bdrom_phone = '+7 ('+code_region+') '+middle_phone+'-'+last_phone
                                        links = ''
                                        vkq = '"'+bdrom_phone+'" inurl:bdrom.ru/view_phone.aspx'
                                        fvk = quote(vkq)
                                        urlfs = 'https://serpapi.com/search.json?engine=yandex&text='+fvk+'&api_key='+token_yandex
                                        rsr = requests.get(urlfs).json()
                                        try:
                                          found = rsr['organic_results'][0]['link']
                                          chfound = rsr['organic_results'][0]['title']
                                          if bdrom_phone in chfound:
                                            await message.answer('🚘 *Найдено возможное обьявление на сайте BDrom:* `'+found+'`', parse_mode='Markdown')
                                        except:
                                          pass
                                    
                                        # BBro
                                        ch_last = last_phone.replace('', '/')
                                        ch_last = ch_last[1:]
                                        ch_last = ch_last[:-1]
                                        ch_last = ch_last.split('/')
                                        lastbbro = ch_last[0]+ch_last[1]+'-'+ch_last[2]+ch_last[3]
                                        
                                        bbro_phone = '8 '+code_region+' '+middle_phone+'-'+lastbbro
                                        inks = ''
                                        vkq = '"'+bbro_phone+'" inurl:bbro.su/view_phone.aspx'
                                        fvk = quote(vkq)
                                        urlfs = 'https://serpapi.com/search.json?engine=yandex&text='+fvk+'&api_key='+token_yandex
                                        rsr = requests.get(urlfs).json()
                                        try:
                                          
                                          found = rsr['organic_results'][0]['link']
                                          chfound = rsr['organic_results'][0]['title']
                                          if bbro_phone in chfound:
                                            await message.answer('🏣 *Найдено возможное обьявление на сайте BBro:* `'+found+'`', parse_mode='Markdown')
                                        except:
                                          pass
                                    
                                        # 100Realt
                                        realt_phone = '+7('+code_region+') '+middle_phone+'-'+lastbbro
                                        inks = ''
                                        vkq = '"'+realt_phone+'" inurl:100realt.ru/user'
                                        fvk = quote(vkq)
                                        urlfs = 'https://serpapi.com/search.json?engine=yandex&text='+fvk+'&api_key='+token_yandex
                                        rsr = requests.get(urlfs).json()
                                        try:
                                          found = rsr['organic_results'][0]['link']
                                          chfound = rsr['organic_results'][0]['snippet']
                                          if realt_phone in chfound:
                                            await message.answer('🛖 *Найден профиль на 100Realt:* `'+found+'`', parse_mode='Markdown')
                                        except:
                                          pass
                                    
                                        # Kvartelia
                                        realt_phone = '+7('+code_region+')'+middle_phone+'-'+lastbbro
                                        inks = ''
                                        vkq = '"'+realt_phone+'" inurl:kvartelia.ru/user'
                                        fvk = quote(vkq)
                                        urlfs = 'https://serpapi.com/search.json?engine=yandex&text='+fvk+'&api_key='+token_yandex
                                        rsr = requests.get(urlfs).json()
                                        try:
                                          found = rsr['organic_results'][0]['link']
                                          chfound = rsr['organic_results'][0]['title']
                                          if bbro_phone in chfound:
                                            await message.answer('🕋 *Найден профиль на Kvartelia:* `'+found+'`', parse_mode='Markdown')
                                        except:
                                          pass
              else:
                pass
              if cekss == 0:
                            phonet = phone
                            await message.answer('Начался поиск по базам. Номер: '+phonet)
                            '''
                            baseep = requests.get('https://cumbersomehungrycodec.hkfdsfsdfh.repl.co/info?d='+phonse).content.decode('utf-8').replace('#$', '\n')
                            try:
                              await message.answer(baseep, parse_mode='Markdown')
                            except:
                              pass
                            '''
                            check_row = 'vtb_user,'
                            check_row1 = ''
                            line_phone = ''
                            pastch = ''
                            
                            part1 = phonse[:2]
                            part2 = phonse[2:4]
                            part3 = phonse[4:6]
                            part4 = phonse[6:8]
                            part = f'{part1}/{part2}/{part3}/{part4}.csv'
                            savaama = 'https://saverudata.net/db/dbpn/'+part
                            answer = ''
                            
                            URLavito = savaama
                            ra = requests.get(URLavito).content.decode('utf-8')
                            with open('podopitniya.csv', 'w') as f:
                              f.write(ra)
                            
                            with open('podopitniya.csv') as file:
                              for line in file:
                                if check_row in line:
                                  check_row1 = line
                                  break
                            
                            with open('podopitniya.csv') as file:
                              for line in file:
                                if phonse in line:
                                  line_phone = line
                                  checkka=check_row1.replace(',', '\n')
                                  count = checkka.count('\n')-1
                                  for num in range(2,count):
                                      line_phone = line_phone+',,,,,'
                                      result = line_phone.split(',')[num]
                                      por = check_row1.split(',')[num]
                                      headr = por.replace('cdek_full_name', '👤 *ФИО:* ').replace('fb_profile_id', '🧿 *Ссылка на профиль Facebook:* https://facebook.com/profile.php?id=').replace('fb_full_name', '🧿 *Имя профиля Facebook:* ').replace('vk_first_name', '🤖 *Имя профиля ВК:* ').replace('vk_last_name', '🤖 *Фамилия профиля ВК:* ').replace('vk_email', '🤖 *Почта, привязанная к ВК:* ').replace('vtb_user', '💎 *Клиент ВТБ:* ').replace('cdek_email', '📧 *Почта:* ').replace('fb_address1', '🧿 *Адрес профиля Facebook:* ').replace('fb_address2', '🧿 *Адрес профиля Facebook:* ').replace('fb_work', '🧿 *Работа в профиле Facebook:* ').replace('yandex_name', '💊 *Имя из Яндекс:* ').replace('yandex_created_at', 'mt').replace('yandex_place_id', 'mt').replace('yandex_place_name', 'mt').replace('yandex_address_city', '🏠 *Возможный город:* ').replace('yandex_address_street', '🏠 *Возможная улица:* ').replace('yandex_address_house', '🏠 *Возможный номер дома:* ').replace('yandex_address_comment', 'mt').replace('yandex_region_id', 'mt').replace('yandex_latitude', 'mt').replace('yandex_longitude', 'mt').replace('yandex_amount_rub', 'mt').replace('yandex_sum_orders', 'mt').replace('yandex_user_agent', '🕹 *User-Agent:* ').replace('yandex_address_entrance', 'mt').replace('yandex_address_floor', 'mt').replace('yandex_address_office', 'mt').replace('yandex_address_doorcode', '🚪 *Номер квартиры:* ').replace('pikabu_username', '💿 *Имя пользователя на Pikabu:* ').replace('pikabu_email', '💿 *Почта на Pikabu:* ').replace('rfcont_name', '🌚 *Возможное имя:* ').replace('rfcont_email', '📧 *Почта:* ').replace('miltor_name', '🎾 *Имя на Miltor:* ').replace('miltor_email', '🎾 *Почта на Miltor:* ').replace('miltor_fio', '🎾 *ФИО на Miltor:* ').replace('mailru_email', '🦋 *Почта на MailRU:* ').replace('mailru_profile', 'mt').replace('mailru_full_name', '🦋 *Имя на MailRU:* ').replace('mailru_avatar', 'mt').replace('mailru_age', 'mt').replace('wildberries_name', '🦄 *Имя на WildBerries:* ').replace('wildberries_comment', 'mt').replace('wildberries_email', '🦄 *Почта на WildBerries:* ').replace('wildberries_address', '🦄 *Адрес на WildBerries:* ').replace('wildberries_lat', 'mt').replace('wildberries_lon', 'mt').replace('avito_user_name', '🏪 *Имя на Авито:* ').replace('avito_price', 'mt').replace('avito_ad_pdate', 'mt').replace('avito_ad_title', 'mt').replace('avito_city', '🏪 *Город на Авито:* ').replace('avito_user_location', '🏪 *Локация на Авито:* ').replace('gibdd2_name', '🚗 *ГИБДД имя:* ').replace('gibdd2_passport_address', '🚗 *ГИБДД адрес паспорта:* ').replace('gibdd2_passport', '🚗 *ГИБДД паспорт:* ').replace('gibdd2_dateofbirth', '🚗 *ГИБДД дата рождения:* ').replace('gibdd2_base_name', 'mt').replace('gibdd2_car_vin', '🚗 *ГИБДД VIN:* ').replace('gibdd2_car_year', 'mt').replace('gibdd2_car_model', 'mt').replace('gibdd2_car_plate_number', '🚗 *ГИБДД гос. номер автомобиля:* ').replace('sushi_name', '⛩ *Имя заказчика СушиМастер:* ').replace('sushi_date', 'mt').replace('sushi_address_city', '⛩ *Город заказчика СушиМастер:* ').replace('sushi_address_street', '⛩ *Улица заказчика СушиМастер:* ').replace('sushi_address_home', '⛩ *Дом заказчика СушиМастер:* ').replace('sushi_address_housing', '⛩ *Квартира заказчика СушиМастер:* ').replace('sushi_lat', 'mt').replace('sushi_long', 'mt').replace('beeline_full_name', '🐝 *ФИО абонента Билайн:* ').replace('beeline_address_city', '🐝 *Город абонента Билайн:* ').replace('beeline_address_city', '🐝 *Город абонента Билайн:* ').replace('beeline_address_street', '🐝 *Улица абонента Билайн:* ').replace('beeline_address_house', '🐝 *Дом абонента Билайн:* ').replace('beeline_address_appt', '🐝 *Квартира абонента Билайн:* ').replace('beeline_address_floors_count', 'mt').replace('beeline_address_entrance_count', 'mt').replace('beeline_latitude', 'mt').replace('beeline_longitude', 'mt').replace('beeline_inet_info', '🐝 *Тариф абонента Билайн:* ').replace('beeline_inet_mbps', 'mt').replace('gibdd_name', '🚗 *ГИБДД имя:* ').replace('gibdd_passport_address', '🚗 *ГИБДД адрес паспорта:* ').replace('gibdd_passport', '🚗 *ГИБДД паспорт:* ').replace('gibdd_dateofbirth', '🚗 *ГИБДД дата рождения:* ').replace('gibdd_base_name', 'mt').replace('gibdd2_car_vin', '🚗 *ГИБДД VIN:* ').replace('gibdd_car_year', 'mt').replace('gibdd_car_model', 'mt').replace('gibdd_car_plate_number', '🚗 *ГИБДД гос. номер автомобиля:* ').replace('gibdd_old_car_plate_number', '🚗 *ГИБДД старый гос. номер автомобиля:* ').replace('gibdd2_old_car_plate_number', '🚗 *ГИБДД старый гос. номер автомобиля:* ')
                                      fbex = ''
                                      line_phone = line_phone.replace(', Russia', '').replace('"', '')
                                      try:
                                        fbex = line_phone.split('"')[1]
                                      except:
                                        pass
                                      if result != '':
                                        if headr != 'mt':
                                          answer = answer+headr+'`'+result+'`\n'
                            try:
                              await message.answer(answer, parse_mode='Markdown')
                            except:
                              with open('dbs_visione.html', 'w') as file:
                                answer = answer.replace('\n', '<br>').replace('*', '').replace('`', '')
                                file.write('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Отчет</title></head><body>'+answer+'</body></html>')
                              if answer != '':
                                await message.reply_document(open('dbs_visione.html', 'rb'))
                                await message.answer('❗️Отчет по базам слишком велик. Мы *не можем его отправить в виде сообщения*.', parse_mode='Markdown')
                            async def phonet():
                              phonet = phone
                              # ebbd
                              async with aiohttp.ClientSession() as session:
                                  async with session.get('https://safsdaecr34r34wevtbernt.sdfsdfsfsd2321.repl.co/info?d=' + phonet) as ebbd:
                                    try:
                                          
                                      wmsg = await ebbd.text()
                                      wuid = wmsg.split(',')[0]
                                      wname = wmsg.split(',')[1]
                                      wpass = wmsg.split(',')[2]
                                      wtz = wmsg.split(',')[9]
                                      await message.answer(f'🧿 *База данных Warframe:*\n\n🧧 Уникальный ID: `{wuid}`\n👤 Имя пользователя: `{wname}`\n🔑 Пароль (в зашифрованном виде): `{wpass}`\n⏰ Часовой пояс: `{wtz}`', parse_mode='Markdown')
                                    except:
                                          pass
                              # ebbd1
                              async with aiohttp.ClientSession() as session:
                                  async with session.get('https://wdwfg454df4gf45gf4d5fdfff.sdfsdfsfsd2321.repl.co/info?d=' + phonet) as ebbd1:
                                      try:
                                          np = await ebbd1.text()
                                          np = np.replace('|', '').replace('"', '')
                                          npln = np.split(',')[0]
                                          npfn = np.split(',')[1]
                                          npo = np.split(',')[2]
                                          npfio = f'{npln} {npfn} {npo}'
                                          npem = np.split(',')[3]
                                          npdr = np.split(',')[4]
                                          npphh = np.split(',')[8]
                                          await message.answer(f'📧 *База данных Новой Почты (УКР):*\n\n👤 ФИО: `{npfio}`\n📮 Почтовый ящик: `{npem}`\n🏩 День рождения: `{npdr}`\n📞 Номер телефона: `{npphh}`', parse_mode='Markdown')
                                      except:
                                          pass
                              # ebbd2
                              async with aiohttp.ClientSession() as session:
                                  async with session.get('https://asd.sdfsdfsfsd2321.repl.co/info?d=' + phonet) as ebbd2:
                                      try:
                                        dd = await ebbd2.text()
                                        if dd != '':
                                          await message.answer('*💊 Какие-то "смешанные" базы:*\n\n'+dd+'`', parse_mode='Markdown')
                                      except:
                                          pass
                                          # bbd
                              async with aiohttp.ClientSession() as session:
                                  async with session.get(
                                          'https://4m89t04ghtm8mieieieieie9mtie9dbigdatanum.sdfsdfsfsd2321.repl.co/info?d=' + phonet) as bbd:
                                      try:
                                        df = await bbd.text()
                                        if df != '':
                                          await message.answer('*🧾 Данные из 12 небольших баз:*\n\n`'+df+'`', parse_mode='Markdown')
                                      except:
                                          pass
                              # bbd2
                              async with aiohttp.ClientSession() as session:
                                  async with session.get('https://werwecrvebt434b654ft43d3fg.sdfsdfsfsd2321.repl.co/info?d=' + phonet) as bbd2:
                                      try:
                                        ty = await bbd2.text()
                                        if ty != '':
                                          await message.answer('😶 *База (ИмяТелефонАдрес):*\n\n`'+ty+'`', parse_mode='Markdown')
                                      except:
                                          pass
                              
                              
                              # bbd5
                              async with aiohttp.ClientSession() as session:
                                  async with session.get('https://pungentfrigidchief.sdfsdfsfsd2321.repl.co/info?d=' + phonet) as bbd5:
                                      try:
                                          dye = await bbd5.text()
                                          
                                          yename = dye.split(';')[1]
                                          yeaddr = dye.split(';')[4]
                                          hdk = dye.split(';')[0]
                                          await message.answer(f'🏉 *База ЯндексЕды*:\n\n👤 Имя: `{yename}`\n🏠 Адрес: `{yeaddr}`\n📲 Номер телефона: `{hdk}`', parse_mode='Markdown')
                                      except:
                                          pass
                              # bbd3
                              async with aiohttp.ClientSession() as session:
                                async with session.get('https://servttbertbertvsrf.sdfsdfsfsd2321.repl.co/info?d=' + phone) as bbd3:
                                  try:
                                          rr = await bbd3.text()
                                          rre = rr.split(',')[3]
                                          ryy = rre[:2]
                                          print(ryy)
                                          if ryy == '98':
                                            rre = '7'+rre[2:]
                                          uidd = rr.split(',')[4]
                                    
                                          rra = f'🧧 *ID:* `{uidd}`\n📱 *Номер телефона:* `{rre}`'
                                          await message.answer(rra, parse_mode='Markdown')
                                  except:
                                                  pass
                              # bbd4
                              async with aiohttp.ClientSession() as session:
                                    async with session.get('https://refretertertbert54vt45b65.sdfsdfsfsd2321.repl.co/info?d=' + phone) as bbd4:
                                          rr = await bbd4.text()
                                          print(rr)
                                          rre = rr.split(',')[3]
                                          ryy = rre[:2]
                                          print(ryy)
                                          if ryy == '98':
                                            rre = '7'+rre[2:]
                                          uidd = rr.split(',')[4]
                                          rra = f'🧧 *ID:* `{uidd}`\n📱 *Номер телефона:* `{rre}`'
                                          await message.answer(rra, parse_mode='Markdown')
                              # bbd7
                              async with aiohttp.ClientSession() as session:
                                  async with session.get('https://forsakenyummyleads.hkfdsfsdfh.repl.co/info?d=' + phonet) as bbd7:
                                      try:
                                          fbf = await bbd7.text()
                                          linkf = 'https://www.facebook.com/profile.php?id='+fbf.split(':')[1]
                                          fifb = fbf.split(':')[2]+' '+fbf.split(':')[3]
                                          fbkd = fbf.split(':')[0]
                                          await message.answer(f'🧿* База данных Facebook:*\n\n🛎 Ссылка на профиль: `{linkf}`\n👤 Имя: `{fifb}`\n📲 Номер телефона: `{fbkd}`', parse_mode='Markdown')
                                      except:
                                          pass
                              
                              # bbd8
                              async with aiohttp.ClientSession() as session:
                                  async with session.get('https://feistyunwittinginstructionset.sdfsdfsfsd2321.repl.co/info?d=' + phonet) as bbd8:
                                      try:
                                          gc = await bbd8.text()
                                          gctag = gc.split(';')[1]
                                          qq = gc.split(';')[0]
                                          await message.answer(f'🔖 *Записи из GetContact:* `{gctag}`\n📲 Номер телефона: `{qq}`', parse_mode='Markdown')
                                      except:
                                          pass
                              # bbd9
                              async with aiohttp.ClientSession() as session:
                                  async with session.get('https://mellowhardtofindcopycat.sdfsdfsfsd2321.repl.co/info?d=' + phonet) as bbd9:
                                      try:
                                          gc = await bbd9.text()
                                          gctag = gc.split(';')[1]
                                          qq = gc.split(';')[0]
                                          await message.answer(f'🔖 *Записи из GetContact:* `{gctag}`\n📲 Номер телефона: `{qq}`', parse_mode='Markdown')
                                      except:
                                          pass
                              # bbd10
                              async with aiohttp.ClientSession() as session:
                                  async with session.get('https://essentiallivespellchecker.sdfsdfsfsd2321.repl.co/info?d=' + phonet) as bbd10:
                                      try:
                                          gc = await bbd10.text()
                                          gctag = gc.split(';')[1]
                                          qq = gc.split(';')[0]
                                          await message.answer(f'🔖 *Записи из GetContact:* `{gctag}`\n📲 Номер телефона: `{qq}`', parse_mode='Markdown')
                                      except:
                                          pass
                              # bbd11
                              async with aiohttp.ClientSession() as session:
                                  async with session.get('https://achingcheerfullinuxpc.sdfsdfsfsd2321.repl.co/info?d=' + phonet) as bbd11:
                                      try:
                                          gc = await bbd11.text()
                                          gctag = gc.split(';')[1]
                                          qq = gc.split(';')[0]
                                          await message.answer(f'🔖 *Записи из GetContact:* `{gctag}`\n📲 Номер телефона: `{qq}`', parse_mode='Markdown')
                                      except:
                                          pass
                              # bbd12
                              async with aiohttp.ClientSession() as session:
                                  async with session.get('https://urbanexhaustedautosketch.hkfdsfsdfh.repl.co/info?value=' + phonet) as bbd12:
                                      try:
                                          gc = await bbd12.text()
                                          fio = gc.split(';')[1]+' '+gc.split(';')[2]+' '+gc.split(';')[3]
                                          drkb = gc.split(';')[4]
                                          numbkb = gc.split(';')[5]
                                          await message.answer(f'🍷 *Красное&Белое*\n\n👤 ФИО: `{fio}`\n🏩 День рождения: `{drkb}`\n📱 Номер телефона: `{numbkb}`', parse_mode='Markdown')
                                      except:
                                          pass
                            await phonet()
          if tarifan == 0:
            await message.answer('К обычному поиску по номеру пристроен поиск по базам и похоже, что у вас нет подписки Профи. Мы не можем искать по базам без Профи.')
        else:
          await message.answer('Неправильный формат номера!')
    elif '!?@@"' in message.text:
      user_id = str(message.from_user.id)
      if user_id == '5182046516' or user_id == '1903214150':
        roww = message.text
        roww = roww.replace('!?@@"', ';')
        tarif = roww.split(';')[2]
        print(roww)
        with open('tickets.txt', 'a') as file:
            file.write(f'{roww}\n')
        if tarif == 'Профи':
            with open('prems.txt', 'a') as file:
              file.write(f'{roww}\n')
        elif tarif != 'Профи':
            pass
        await message.answer('Успешно!')
      else:
        await message.answer('Доступ ограничен!')
    elif message.text == '🥶 Alarm-система':
      await message.answer('*Введите номер телефона или почту, чтобы включить оповещение, когда вас пробивают.*\nПример: `%79876543234, %example@domain.com`', parse_mode='Markdown')
    elif '%' in message.text:
      f = open('alarm.txt', 'a')
      user_id = str(message.from_user.id)
      inputt = message.text.replace('%', '')
      f.write(f'{user_id};{inputt}\n')
      f.close()
      await message.answer('🥶 Alarm-система включена!')
    elif '&@$' in message.text:
      indata = message.text.replace('&@$', ';')
      if message.from_user.id == 5182046516 or message.from_user.id == 1903214150:
        with open('balik.txt', 'a') as f:
          f.write(indata+'\n')
    elif 'vk.com' in message.text:
      await message.answer('По ВК пока нет функции.')
    elif "#" in indata:
                  global perma
                  perma = 0
                  plan = 'Бесплатный'
                  user_id = str(message.from_user.id)
                  with open('prems.txt', encoding='utf-8', errors='ignore') as file:
                      for line in file:
                          if user_id in line:
                            perma = 1
                  if perma == 1:
                    indataaa = message.text
                    phone = indataaa.replace('#', '')
                    await message.answer('Начинаем поиск...')
                    with open('alarm.txt', encoding='utf-8', errors='ignore') as file:
                      for line in file:
                          if phone in line:
                            id = line.split(';')[0]
                            ia = line.split(';')[1]
                            rra = f'🧧 *ID:* `{id}`\n🗄 *Данные:* `{ia}`'
                            await message.answer(rra, parse_mode='Markdown')
                            await bot.send_message(id, text="🥶 *СРОЧНО!* Вас пытались пробить!", parse_mode='Markdown')
                    # bbd3
                    async with aiohttp.ClientSession() as session:
                      async with session.get('https://servttbertbertvsrf.sdfsdfsfsd2321.repl.co/info?d=' + phone) as bbd3:
                        try:
                                rr = await bbd3.text()
                                rre = rr.split(',')[3]
                                ryy = rre[:2]
                                print(ryy)
                                if ryy == '98':
                                  rre = '7'+rre[2:]
                                uidd = rr.split(',')[4]
                                rra = f'🧧 *ID:* `{uidd}`\n📱 *Номер телефона:* `{rre}`'
                                await message.answer(rra, parse_mode='Markdown')
                        except:
                                        pass
                    # bbd4
                    async with aiohttp.ClientSession() as session:
                          async with session.get('https://refretertertbert54vt45b65.sdfsdfsfsd2321.repl.co/info?d=' + phone) as bbd4:
                                rr = await bbd4.text()
                                rre = rr.split(',')[3]
                                ryy = rre[:2]
                                print(ryy)
                                if ryy == '98':
                                  rre = '7'+rre[2:]
                                uidd = rr.split(',')[4]
                                rra = f'🧧 *ID:* `{uidd}`\n📱 *Номер телефона:* `{rre}`'
                                await message.answer(rra, parse_mode='Markdown')
                             
                    
                  else:
                    await message.answer('Если выдало только это сообщение, то у вас нет Профи-подписки. Только люди с Профи-подпиской могут искать по базам.')
                  await message.answer('Поиск окончен!')
    elif "*" in indata:
                        plan = 'Бесплатный'
                        user_id = str(message.from_user.id)
                        permq = 0
                        with open('prems.txt', encoding='utf-8', errors='ignore') as file:
                          for line in file:
                            if user_id in line:
                              permq = 1
                        if permq == 1:
                          fb_msg = await message.answer(
                              '*📘 Ищем в базах, приготовьте чай или кофе или погладьте питомца, пока мы ищем. Это займет около 5-7 минут...*',
                              parse_mode="Markdown")
                          async def phonet():
                            phonet = message.text.replace('*', '')
                            # ebbd
                            async with aiohttp.ClientSession() as session:
                                async with session.get('https://safsdaecr34r34wevtbernt.sdfsdfsfsd2321.repl.co/info?d=' + phonet) as ebbd:
                                  try:
                                        
                                    wmsg = await ebbd.text()
                                    wuid = wmsg.split(',')[0]
                                    wname = wmsg.split(',')[1]
                                    wpass = wmsg.split(',')[2]
                                    wtz = wmsg.split(',')[9]
                                    await message.answer(f'🧿 *База данных Warframe:*\n\n🧧 Уникальный ID: `{wuid}`\n👤 Имя пользователя: `{wname}`\n🔑 Пароль (в зашифрованном виде): `{wpass}`\n⏰ Часовой пояс: `{wtz}`', parse_mode='Markdown')
                                  except:
                                        pass
                            # ebbd1
                            async with aiohttp.ClientSession() as session:
                                async with session.get('https://wdwfg454df4gf45gf4d5fdfff.sdfsdfsfsd2321.repl.co/info?d=' + phonet) as ebbd1:
                                    try:
                                        np = await ebbd1.text()
                                        np = np.replace('|', '').replace('"', '')
                                        npln = np.split(',')[0]
                                        npfn = np.split(',')[1]
                                        npo = np.split(',')[2]
                                        npfio = f'{npln} {npfn} {npo}'
                                        npem = np.split(',')[3]
                                        npdr = np.split(',')[4]
                                        npphh = np.split(',')[8]
                                        await message.answer(f'📧 *База данных Новой Почты (УКР):*\n\n👤 ФИО: `{npfio}`\n📮 Почтовый ящик: `{npem}`\n🏩 День рождения: `{npdr}`\n📞 Номер телефона: `{npphh}`', parse_mode='Markdown')
                                    except:
                                        pass
                            # ebbd2
                            async with aiohttp.ClientSession() as session:
                                async with session.get('https://asd.sdfsdfsfsd2321.repl.co/info?d=' + phonet) as ebbd2:
                                    try:
                                      dd = await ebbd2.text()
                                      if dd != '':
                                        await message.answer('*💊 Какие-то "смешанные" базы:*\n\n'+dd+'`', parse_mode='Markdown')
                                    except:
                                        pass
                                        # bbd
                            async with aiohttp.ClientSession() as session:
                                async with session.get(
                                        'https://4m89t04ghtm8mieieieieie9mtie9dbigdatanum.sdfsdfsfsd2321.repl.co/info?d=' + phonet) as bbd:
                                    try:
                                      df = await bbd.text()
                                      if df != '':
                                        await message.answer('*🧾 Данные из 12 небольших баз:*\n\n`'+df+'`', parse_mode='Markdown')
                                    except:
                                        pass
                            # bbd2
                            async with aiohttp.ClientSession() as session:
                                async with session.get('https://werwecrvebt434b654ft43d3fg.sdfsdfsfsd2321.repl.co/info?d=' + phonet) as bbd2:
                                    try:
                                      ty = await bbd2.text()
                                      if ty != '':
                                        await message.answer('😶 *База (ИмяТелефонАдрес):*\n\n`'+ty+'`', parse_mode='Markdown')
                                    except:
                                        pass
                            
                            
                            # bbd5
                            async with aiohttp.ClientSession() as session:
                                async with session.get('https://pungentfrigidchief.sdfsdfsfsd2321.repl.co/info?d=' + phonet) as bbd5:
                                    try:
                                        dye = await bbd5.text()
                                        
                                        yename = dye.split(';')[1]
                                        yeaddr = dye.split(';')[4]
                                        hdk = dye.split(';')[0]
                                        await message.answer(f'🏉 *База ЯндексЕды*:\n\n👤 Имя: `{yename}`\n🏠 Адрес: `{yeaddr}`\n📲 Номер телефона: `{hdk}`', parse_mode='Markdown')
                                    except:
                                        pass
                            # bbd7
                            async with aiohttp.ClientSession() as session:
                                async with session.get('https://forsakenyummyleads.hkfdsfsdfh.repl.co/info?d=' + phonet) as bbd7:
                                    try:
                                        fbf = await bbd7.text()
                                        linkf = 'https://www.facebook.com/profile.php?id='+fbf.split(':')[1]
                                        fifb = fbf.split(':')[2]+' '+fbf.split(':')[3]
                                        fbkd = fbf.split(':')[0]
                                        await message.answer(f'🧿* База данных Facebook:*\n\n🛎 Ссылка на профиль: `{linkf}`\n👤 Имя: `{fifb}`\n📲 Номер телефона: `{fbkd}`', parse_mode='Markdown')
                                    except:
                                        pass
                            
                            # bbd8
                            async with aiohttp.ClientSession() as session:
                                async with session.get('https://feistyunwittinginstructionset.sdfsdfsfsd2321.repl.co/info?d=' + phonet) as bbd8:
                                    try:
                                        gc = await bbd8.text()
                                        gctag = gc.split(';')[1]
                                        qq = gc.split(';')[0]
                                        await message.answer(f'🔖 *Записи из GetContact:* `{gctag}`\n📲 Номер телефона: `{qq}`', parse_mode='Markdown')
                                    except:
                                        pass
                            # bbd9
                            async with aiohttp.ClientSession() as session:
                                async with session.get('https://mellowhardtofindcopycat.sdfsdfsfsd2321.repl.co/info?d=' + phonet) as bbd9:
                                    try:
                                        gc = await bbd9.text()
                                        gctag = gc.split(';')[1]
                                        qq = gc.split(';')[0]
                                        await message.answer(f'🔖 *Записи из GetContact:* `{gctag}`\n📲 Номер телефона: `{qq}`', parse_mode='Markdown')
                                    except:
                                        pass
                            # bbd10
                            async with aiohttp.ClientSession() as session:
                                async with session.get('https://essentiallivespellchecker.sdfsdfsfsd2321.repl.co/info?d=' + phonet) as bbd10:
                                    try:
                                        gc = await bbd10.text()
                                        gctag = gc.split(';')[1]
                                        qq = gc.split(';')[0]
                                        await message.answer(f'🔖 *Записи из GetContact:* `{gctag}`\n📲 Номер телефона: `{qq}`', parse_mode='Markdown')
                                    except:
                                        pass
                            # bbd11
                            async with aiohttp.ClientSession() as session:
                                async with session.get('https://achingcheerfullinuxpc.sdfsdfsfsd2321.repl.co/info?d=' + phonet) as bbd11:
                                    try:
                                        gc = await bbd11.text()
                                        gctag = gc.split(';')[1]
                                        qq = gc.split(';')[0]
                                        await message.answer(f'🔖 *Записи из GetContact:* `{gctag}`\n📲 Номер телефона: `{qq}`', parse_mode='Markdown')
                                    except:
                                        pass
                            # bbd12
                            async with aiohttp.ClientSession() as session:
                                async with session.get('https://urbanexhaustedautosketch.hkfdsfsdfh.repl.co/info?value=' + phonet) as bbd12:
                                    try:
                                        gc = await bbd12.text()
                                        fio = gc.split(';')[1]+' '+gc.split(';')[2]+' '+gc.split(';')[3]
                                        drkb = gc.split(';')[4]
                                        numbkb = gc.split(';')[5]
                                        await message.answer(f'🍷 *Красное&Белое*\n\n👤 ФИО: `{fio}`\n🏩 День рождения: `{drkb}`\n📱 Номер телефона: `{numbkb}`', parse_mode='Markdown')
                                    except:
                                        pass
                          await phonet()
                        else:
                          await message.answer('Если выдало только это сообщение, то у вас нет Профи-подписки. Только люди с Профи-подпиской могут искать по базам.')
                        await message.answer('Поиск окончен!')
    elif '@' in indata:
        # Сортировка ------------------------------
        email_msg = await message.answer('🗄 *Сортируем...*', parse_mode="Markdown")
        emaill = indata
        user_id = str(message.from_user.id)
        with open('alarm.txt', encoding='utf-8', errors='ignore') as file:
            for line in file:
                if emaill in line:
                  id = line.split(';')[0]
                  await bot.send_message(id, text="🥶 *СРОЧНО!* Вас пытались пробить!", parse_mode='Markdown')
        try:
            nickmail = emaill.split('@')[0]
            domain = emaill.split('@')[1]
        except:
            pass
        await email_msg.delete()
        # Сбер- -------------------------------
        sber_msg = await message.answer('💳 *Ищем Сбербанк...*', parse_mode="Markdown")
        sberbank_message = ''
        maskedPhone = ''
        try:
            email = message.text.strip()
            sberbank = requests.post(f"https://securepayments.sberbank.ru/sbersafe/client/find?email={emaill}")
            datas = sberbank.json()

            get_date = datas['client']['createdDate']
            get_date2 = get_date[:10]
            rep1 = get_date2.replace(".01.", " января ")
            rep2 = rep1.replace(".02.", " февраля ")
            rep3 = rep2.replace(".03.", " марта ")
            rep4 = rep3.replace(".04.", " апреля ")
            rep5 = rep4.replace(".05.", " мая ")
            rep6 = rep5.replace(".06.", " июня ")
            rep7 = rep6.replace(".07.", " июля ")
            rep8 = rep7.replace(".08.", " августа ")
            rep9 = rep8.replace(".09.", " сентября ")
            rep10 = rep9.replace(".10.", " октября ")
            rep11 = rep10.replace(".11.", " ноября ")
            rep12 = rep11.replace(".12.", " декабря ")
            rep13 = get_date[11:-7]

            maskedPhone = datas['client']['maskedPhone']
            created_date = f'{rep12} г. в {rep13}'
            if tarifan != 0:
              sberbank_message = f"💳 *Сбербанк:* `есть` ({created_date})"
            else:
              sberbank_message = f"💳 *Сбербанк:* `есть`)"
        except:
            sberbank_message = ''
        await sber_msg.delete()
        # Яндекс ------------------------------
        yand_msg = await message.answer('㊙ *Проверяем почту на наличие аккаунта на Яндекс...*',
                                        parse_mode="Markdown")
        yandexxx = ''
        try:
            eqereq = message.text.strip()
            email_login = (eqereq.split("@"))[0]
            yandex = requests.get(f"https://yandex.ru/collections/api/users/{email_login}")
            try:
                yamail = email_login + '@yandex.ru'
            except:
                yamail = ''
            yadata = yandex.json()
            public_id = yadata['public_id']
            try:
                display_name = yadata['display_name']
            except:
                display_name = ''
            if tarifan != 0:
              yandexxx = f'㊗ *Яндекс:* `{display_name}` (`{public_id}`)'
            else:
              yandexxx = f'㊗ *Яндекс:* `найден`'
        except:
            display_name = ''
            public_id = ''
        icq = ''
        await yand_msg.delete()
        # Одноклассники
        ok_msg = await message.answer('🆗 *Проверяем почту на наличие аккаунта в Одноклассниках...*',
                                      parse_mode="Markdown")
        masked_phone = ''

        # одноклассники
        session = requests.Session()
        session.get(
            f'https://www.ok.ru/dk?st.cmd=anonymMain&st.accRecovery=on&st.error=errors.password.wrong&st.email={email}')
        request = session.get(
            f'https://www.ok.ru/dk?st.cmd=anonymRecoveryAfterFailedLogin&st._aid=LeftColumn_Login_ForgotPassword')
        root_soup = BeautifulSoup(request.content, 'html.parser')
        soup = root_soup.find('div', {'data-l': 'registrationContainer,offer_contact_rest'})
        if soup:
            account_info = soup.find('div', {'class': 'ext-registration_tx taCenter'})
            masked_email = soup.find('button', {'data-l': 't,email'})
            masked_phone = soup.find('button', {'data-l': 't,phone'})
            if masked_phone:
                masked_phone = masked_phone.find('div', {'class': 'ext-registration_stub_small_header'}).get_text()
            if masked_email:
                masked_email = masked_email.find('div', {'class': 'ext-registration_stub_small_header'}).get_text()
            else:
                masked_email = ''
            if account_info:
                masked_name = account_info.find('div', {'class': 'ext-registration_username_header'})
                if masked_name:
                    masked_name = masked_name.get_text()
                account_info = account_info.findAll('div', {'class': 'lstp-t'})
                if account_info:
                    profile_info = account_info[0].get_text()
                    profile_registred = account_info[1].get_text()
                else:
                    profile_info = None
                    profile_registred = None
            else:
                pass
        await ok_msg.delete()
        try:
            age = profile_info[:7].replace(',', '')
            cityok = profile_info[8:].replace(',', '')
            age = f'\n🧿 *Предпологаемый возвраст:* `{age}`'
            cityok = f'`{cityok}`'
            if tarifan != 0:
              ok = f'\n🆗 *Одноклассники:* `{masked_name}` (`{profile_info}`, {masked_phone} `{profile_registred})`\n'
            else:
              ok = f'\n🆗 *Одноклассники:* `найдены`\n'


        except:
            ok = ''
            cityok = ''
            age = ''
            masked_email = ''
        # ICQ
        icq_msg = await message.answer('✅ *Проверяем на наличие ICQ...*', parse_mode="Markdown")
        try:
            URLicq = "https://icq.im/" + emaill
            HEADERS = {
                "User-Agent":
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"
            }
            raq = requests.get(URLicq, headers=HEADERS)
            soup = BeautifulSoup(raq.content, 'html.parser')
            items = soup.findAll('div', class_='icq-profile__box')
            comps = []
            for item in items:
                comps.append({
                    'icq':
                        item.find('h2', class_='icq-profile__name').get_text(strip=True)
                })
            for comp in comps:
                icq = comp['icq']
                icq = f'🟢 *ICQ:* `{icq}`'.replace('🟢 *ICQ:* `Profile not found`', '')
        except:
            icq = ''
        # 2GIS
        tgis = ''
        rt = requests.post('https://id.2gis.com/api/v1/recovery', json={"email": email, "locale": "ru-RU"}).json()
        try:
            exe = rt['status']
            if tarifan != 0:
              tgis = '📗 *Аккаунт на 2ГИС:* `существует` (`мы отправили код подтверждения`)'
            else:
              tgis = ''
        except:
            tgis = ''
        skype = '🎇 *Чекнуть скайп:* https://www.vedbex.com/email2skype'
        dop = '*Дополнительно:* https://tools.epieos.com/?q=' + email.replace('@', '%40')
        phone_list = ''
        phone_bk = ''
        phone_inet = ''
        phone_inbox = ''
        await icq_msg.delete()
        # Gravatar
        gr_msg = await message.answer('🛅 *Подбираем хеш для Gravatar...*', parse_mode="Markdown")
        gravatar = ''
        try:
            emailtohash = message.text.strip()
            hashed_name = hashlib.md5(emailtohash.encode()).hexdigest()
            rhash = requests.get(f'https://gravatar.com/{hashed_name}.json')
            data = rhash.json()
            GravatarFullName = data['entry'][0]['displayName']
            if rhash.status_code == 200:
                gravatar = f'🌐 *Gravatar:* gravatar.com/{GravatarFullName}'
        except:
            pass
        plan = 'Бесплатный'
        user_id = str(message.from_user.id)
        with open('tickets.txt', encoding='utf-8', errors='ignore') as file:
            for line in file:
                if user_id in line:
                    time = line.split(';')[1]
                    plan = line.split(';')[2]
        
        if plan != 'Бесплатный':
            if domain == 'yandex.ru':
                rayon = InlineKeyboardButton('Район', url='https://local.yandex.ru/users/' + public_id)
                maps = InlineKeyboardButton('Карты', url='https://n.maps.yandex.ru/#!/users/' + public_id)
                market = InlineKeyboardButton('Карты', url='https://market.yandex.ru/user/' + public_id)
                q = InlineKeyboardButton('Кью', url='https://yandex.ru/q/profile/' + public_id)
                coll = InlineKeyboardButton('Коллекции', url='https://yandex.ru/collections/' + public_id)
                dzen = InlineKeyboardButton('Дзен', url='https://zen.yandex.ru/user/' + public_id)
                links_mail = InlineKeyboardMarkup().add(rayon, maps, market, q, coll, dzen)
                fstep = f'📪\n├  *Логин:* `{nickmail}`\n└  *Домен:* `{domain}`'
                list_phones = f'\n☎ *Вероятные части номеров телефонов:* {phone_list}, {masked_phone},{phone_bk}, {phone_inet}, {phone_inbox}, {maskedPhone}\n'

                await message.answer(
                    f'{fstep}\n{list_phones}{age}\n{yandexxx}\n{sberbank_message}\n{ok}\n{icq}\n{gravatar}\n{tgis}\n\n{skype}\n{dop}',
                    parse_mode="Markdown", reply_markup=links_mail)
            elif domain == 'mail.ru' or 'bk.ru' or 'list.ru' or 'inbox.ru':
                mail = InlineKeyboardButton('📮 Профиль «Мой мир» ', url='https://my.mail.ru/mail/' + nickmail)
                links_mail = InlineKeyboardMarkup().add(mail)
                fstep = f'📪\n├  *Логин:* `{nickmail}`\n└  *Домен:* `{domain}`'
                list_phones = f'\n☎ *Вероятные части номеров телефонов:* {phone_list}, {masked_phone},{phone_bk}, {phone_inet}, {phone_inbox}, {maskedPhone}\n'

                await message.answer(
                    f'{fstep}\n{list_phones}{age}\n{yandexxx}\n{sberbank_message}\n{ok}\n{icq}\n{gravatar}\n{tgis}\n\n{skype}\n{dop}',
                    parse_mode="Markdown", reply_markup=links_mail)
            else:
                fstep = f'📪\n├  *Логин:* `{nickmail}`\n└  *Домен:* `{domain}`'
                list_phones = f'\n☎ *Вероятные части номеров телефонов:* {phone_list}, {masked_phone},{phone_bk}, {phone_inet}, {phone_inbox}, {maskedPhone}\n'

                await message.answer(
                    f'{fstep}\n{list_phones}{age}\n{yandexxx}\n{sberbank_message}\n{ok}\n{icq}\n{gravatar}\n{tgis}\n\n{skype}\n{dop}',
                    parse_mode="Markdown")
        else:
            if domain == 'yandex.ru':
                rayon = InlineKeyboardButton('Район', url='https://local.yandex.ru/users/' + public_id)
                maps = InlineKeyboardButton('Карты', url='https://n.maps.yandex.ru/#!/users/' + public_id)
                market = InlineKeyboardButton('Карты', url='https://market.yandex.ru/user/' + public_id)
                q = InlineKeyboardButton('Кью', url='https://yandex.ru/q/profile/' + public_id)
                coll = InlineKeyboardButton('Коллекции', url='https://yandex.ru/collections/' + public_id)
                dzen = InlineKeyboardButton('Дзен', url='https://zen.yandex.ru/user/' + public_id)
                links_mail = InlineKeyboardMarkup().add(rayon, maps, market, q, coll, dzen)
                fstep = f'📪\n├  *Логин:* `{nickmail}`\n└  *Домен:* `{domain}`'
                list_phones = f'\n☎ *Вероятные части номеров телефонов:* {phone_list}, {masked_phone},{phone_bk}, {phone_inet}, {phone_inbox}, {maskedPhone}\n'

                await message.answer(
                    f'{fstep}\n{age}\n{yandexxx}\n{sberbank_message}\n{ok}\n{icq}\n{gravatar}\n{tgis}\n\n{skype}\n{dop}\n\n⚡️ Для полного результата купите *Базовый тариф.* Он стоит 7 рублей за день.',
                    parse_mode="Markdown", reply_markup=links_mail)
            elif domain == 'mail.ru' or 'bk.ru' or 'list.ru' or 'inbox.ru':
                mail = InlineKeyboardButton('📮 Профиль «Мой мир» ', url='https://my.mail.ru/mail/' + nickmail)
                links_mail = InlineKeyboardMarkup().add(mail)
                fstep = f'📪\n├  *Логин:* `{nickmail}`\n└  *Домен:* `{domain}`'
                list_phones = f'\n☎ *Вероятные части номеров телефонов:* {phone_list}, {masked_phone},{phone_bk}, {phone_inet}, {phone_inbox}, {maskedPhone}\n'

                await message.answer(
                    f'{fstep}\n{age}\n{yandexxx}\n{sberbank_message}\n{ok}\n{icq}\n{gravatar}\n{tgis}\n\n{skype}\n{dop}\n\n⚡️ Для полного результата купите *Базовый тариф.* Он стоит 7 рублей за день.',
                    parse_mode="Markdown", reply_markup=links_mail)
            else:
                fstep = f'📪\n├  *Логин:* `{nickmail}`\n└  *Домен:* `{domain}`'
                list_phones = f'\n☎ *Вероятные части номеров телефонов:* {phone_list}, {masked_phone},{phone_bk}, {phone_inet}, {phone_inbox}, {maskedPhone}\n'

                await message.answer(
                    f'{fstep}\n{age}\n{yandexxx}\n{sberbank_message}\n{ok}\n{icq}\n{gravatar}\n{tgis}\n\n{skype}\n{dop}\n\n⚡️ Для полного результата купите *Базовый тариф.* Он стоит 7 рублей за день.',
                    parse_mode="Markdown")
        icqq = InlineKeyboardButton('🟢 ICQ', url='https://icq.im/' + email)
        iqcq = InlineKeyboardMarkup().add(icqq)
        if icq != '':
            await message.answer('🟢 *Ссылка на профиль ICQ:*', reply_markup=iqcq, parse_mode='Markdown')
        else:
            pass
        try:
            rps = requests.get(f"https://2ip.ru/?area=ajaxHaveIBeenPwned&query={email}`")
            passdata = rps.json()

            pass0 = passdata['result'][0]['pass']
            sources0 = passdata['result'][0]['sources'][0]
            last_breach0 = passdata['result'][0]['last_breach']

            pass1 = passdata['result'][1]['pass']
            sources1 = passdata['result'][1]['sources'][0]
            last_breach1 = passdata['result'][1]['last_breach']

            pass2 = passdata['result'][2]['pass']
            sources2 = passdata['result'][2]['sources'][0]
            last_breach2 = passdata['result'][2]['last_breach']

            pass3 = passdata['result'][3]['pass']
            sources3 = passdata['result'][3]['sources'][0]
            last_breach3 = passdata['result'][3]['last_breach']

            pass4 = passdata['result'][4]['pass']
            sources4 = passdata['result'][4]['sources'][0]
            last_breach4 = passdata['result'][4]['last_breach']

            pass5 = passdata['result'][5]['pass']
            sources5 = passdata['result'][5]['sources'][0]
            last_breach5 = passdata['result'][5]['last_breach']

            pass6 = passdata['result'][6]['pass']
            sources6 = passdata['result'][6]['sources'][0]
            last_breach6 = passdata['result'][6]['last_breach']

            pass7 = passdata['result'][7]['pass']
            sources7 = passdata['result'][7]['sources'][0]
            last_breach7 = passdata['result'][7]['last_breach']

            pass8 = passdata['result'][8]['pass']
            sources8 = passdata['result'][8]['sources'][0]
            last_breach8 = passdata['result'][8]['last_breach']

            pass9 = passdata['result'][9]['pass']
            sources9 = passdata['result'][9]['sources'][0]
            last_breach9 = passdata['result'][9]['last_breach']

            pass10 = passdata['result'][10]['pass']
            sources10 = passdata['result'][10]['sources'][0]
            last_breach10 = passdata['result'][10]['last_breach']

            await message.answer(
                f'🔑 *Пароль:* `{pass0}`\n🌐 *Источник:* {sources0}`\n🕘 *Дата:* {last_breach0}`\n')

            await message.answer(
                f'🔑 *Пароль:* `{pass1}`\n🌐 *Источник:* {sources1}`\n🕘 *Дата:* {last_breach1}`\n')

            await message.answer(
                f'🔑 *Пароль:* `{pass2}`\n🌐 *Источник:* {sources2}`\n🕘 *Дата:* {last_breach2}`\n')

            await message.answer(
                f'🔑 *Пароль:* `{pass3}`\n🌐 *Источник:* {sources3}`\n🕘 *Дата:* {last_breach3}`\n')

            await message.answer(
                f'🔑 *Пароль:* `{pass4}`\n🌐 *Источник:* {sources4}`\n🕘 *Дата:* {last_breach4}`\n')

            await message.answer(
                f'🔑 *Пароль:* `{pass5}`\n🌐 *Источник:* {sources5}`\n🕘 *Дата:* {last_breach5}`\n')

            await message.answer(
                f'🔑 *Пароль:* `{pass6}`\n🌐 *Источник:* {sources6}`\n🕘 *Дата:* {last_breach6}`\n')

            await message.answer(
                f'🔑 *Пароль:* `{pass7}`\n🌐 *Источник:* {sources7}`\n🕘 *Дата:* {last_breach7}`\n')

            await message.answer(
                f'🔑 *Пароль:* `{pass8}`\n🌐 *Источник:* {sources8}`\n🕘 *Дата:* {last_breach8}`\n')

            await message.answer(
                f'🔑 *Пароль:* `{pass9}`\n🌐 *Источник:* {sources9}`\n🕘 *Дата:* {last_breach9}`\n')

            await message.answer(
                f'🔑 **Пароль:** `{pass10}`\n🌐 **Источник:** `{sources10}`\n🕘 *Дата:* `{last_breach10}`\n')

        except:
            pass
        URLavitos = "https://sovaweb.herokuapp.com/find_em?em=" + emaill
        HEADERS = {
            "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"
        }
        ra = requests.get(URLavitos, headers=HEADERS)
        soup = BeautifulSoup(ra.content, 'html.parser')
        items = soup.findAll('form')
        comps = []
        for item in items:
            comps.append({
                'infof':
                    item.find('textarea', class_='form-control').get_text(strip=True)
            })
        for comp in comps:
            if plan != 'Бесплатный':
                await message.answer(f"📘 *Где зарегистрирован:*\n{comp['infof']}\n", parse_mode="Markdown")
        try:
            URLavitos = "https://sovaweb.herokuapp.com/find_nick?nick=" + nickmail
            HEADERS = {
                "User-Agent":
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"
            }
            ra = requests.get(URLavitos, headers=HEADERS)
            soup = BeautifulSoup(ra.content, 'html.parser')
            items = soup.findAll('form')
            comps = []
            for item in items:
                comps.append({
                    'infof':
                        item.find('textarea', class_='form-control').get_text(strip=True)
                })
            for comp in comps:
                if plan != 'Бесплатный':
                    await message.answer(f"📘 Проверка логина от почты:\n\n{comp['infof']}\n")
        except:
            pass
            # @mail.ru
        try:
            memail = message.text.strip()
            mlogin = (memail.split("@"))[0]
            rm = requests.post(f"https://account.mail.ru/api/v1/user/password/restore?email={mlogin}@mail.ru")
            mdata = rm.json()

            phone = mdata['body']['phones'][0]

            await message.answer(
                f'<b>🗳 Восстановление Mail.ru:</b> <code>{mlogin}@mail.ru</code>\n<b>📞 Номер телефона: </b><code>{phone}</code>\n<b>👤 Профиль:</b> <a href="https://my.mail.ru/mail.ru/{mlogin}/">Открыть</a>',
                parse_mode="HTML")

            emails = mdata['body']['emails'][0]
            emails2 = mdata['body']['emails'][1]

            await message.answer(f'<b>📧 Резервная почта: </b><code>{emails}</code>', parse_mode="HTML")
            await message.answer(f'<b>📧 Резервная почта: </b><code>{emails2}</code>', parse_mode="HTML")
        except:
            pass

            # @list.ru
            try:
                memail = message.text.strip()
                mlogin = (memail.split("@"))[0]
                rm = requests.post(f"https://account.mail.ru/api/v1/user/password/restore?email={mlogin}@list.ru")
                mdata = rm.json()

                phone = mdata['body']['phones'][0]

                await message.answer(
                    f'<b>🗳 Восстановление List.ru:</b> <code>{mlogin}@list.ru</code>\n<b>📞 Номер телефона: </b><code>{phone}</code>\n<b>👤 Профиль:</b> <a href="https://my.mail.ru/list.ru/{mlogin}/">Открыть</a>',
                    parse_mode="HTML")

                emails = mdata['body']['emails'][0]
                emails2 = mdata['body']['emails'][1]

                await message.answer(f'<b>📧 Резервная почта: </b><code>{emails}</code>', parse_mode="HTML")
                await message.answer(f'<b>📧 Резервная почта: </b><code>{emails2}</code>', parse_mode="HTML")
            except:
                pass

            # @bk.ru
            try:
                memail = message.text.strip()
                mlogin = (memail.split("@"))[0]
                rm = requests.post(f"https://account.mail.ru/api/v1/user/password/restore?email={mlogin}@bk.ru")
                mdata = rm.json()

                phone = mdata['body']['phones'][0]

                await message.answer(
                    f'<b>🗳 Восстановление bk.ru:</b> <code>{mlogin}@bk.ru</code>\n<b>📞 Номер телефона: </b><code>{phone}</code>\n<b>👤 Профиль:</b> <a href="https://my.mail.ru/bk.ru/{mlogin}/">Открыть</a>',
                    parse_mode="HTML")

                emails = mdata['body']['emails'][0]
                emails2 = mdata['body']['emails'][1]

                await message.answer(f'<b>📧 Резервная почта: </b><code>{emails}</code>', parse_mode="HTML")
                await message.answer(f'<b>📧 Резервная почта: </b><code>{emails2}</code>', parse_mode="HTML")
            except:
                pass

            # @inbox.ru
            try:
                memail = message.text.strip()
                mlogin = (memail.split("@"))[0]
                rm = requests.post(f"https://account.mail.ru/api/v1/user/password/restore?email={mlogin}@inbox.ru")
                mdata = rm.json()

                phone = mdata['body']['phones'][0]

                await message.answer(
                    f'<b>🗳 Восстановление Inbox.ru:</b> <code>{mlogin}@inbox.ru</code>\n<b>📞 Номер телефона: </b><code>{phone}</code>\n<b>👤 Профиль:</b> <a href="https://my.mail.ru/inbox.ru/{mlogin}/">Открыть</a>',
                    parse_mode="HTML")

                emails = mdata['body']['emails'][0]
                emails2 = mdata['body']['emails'][1]

                await message.answer(f'<b>📧 Резервная почта: </b><code>{emails}</code>', parse_mode="HTML")
                await message.answer(f'<b>📧 Резервная почта: </b><code>{emails2}</code>', parse_mode="HTML")
            except:
                pass

            # @internet.ru
            try:
                memail = message.text.strip()
                mlogin = (memail.split("@"))[0]
                rm = requests.post(f"https://account.mail.ru/api/v1/user/password/restore?email={mlogin}@internet.ru")
                mdata = rm.json()

                phone = mdata['body']['phones'][0]

                await message.answer(
                    f'<b>🗳 Восстановление Internet.ru:</b> <code>{mlogin}@internet.ru</code>\n<b>📞 Номер телефона: </b><code>{phone}</code>\n<b>👤 Профиль:</b> <a href="https://my.mail.ru/internet.ru/{mlogin}/">Открыть</a>',
                    parse_mode="HTML")

                emails = mdata['body']['emails'][0]
                emails2 = mdata['body']['emails'][1]

                await message.answer(f'<b>📧 Резервная почта: </b><code>{emails}</code>', parse_mode="HTML")
                await message.answer(f'<b>📧 Резервная почта: </b><code>{emails2}</code>', parse_mode="HTML")
            except:
                pass
    elif message.text == 'варингиканалотехрабо':
      with open('exists.txt') as file:
        for line in file:
          id = int(line)
          try:
            await bot.send_message(id, text='🛎 Начинаются технические работы, они будут длиться *час*.', parse_mode='Markdown')
          except:
            pass
    elif message.text == 'каналищеуауакшщыв':
      with open('exists.txt') as file:
        for line in file:
          id = int(line)
          try:
            await bot.send_message(id, text='🎯 *Подпишитесь на канал, *чтобы следить за новостями!\n❗️Канал: @visiiione', parse_mode='Markdown')
          except:
            pass
    elif message.text == '📓 Меню':
        await message.answer('*Здарова, брат!* _Бот принимает такие данные, как:_\n\n📲 *Номер телефона* (`Пример: +79876543210, +7 987 654 32 10, +7 (987) 654-32-10, 79876543210`)\n📧 *Адрес эл. почты* (`Пример: aroundtheworld@gmail.com`)\n💎 *Telegram* (`Пример: #446752031`)\n🌐 *IP-адрес* (`Пример: 8.8.8.8`)\n\n⁉️ *Другое* (`Пример: *ФИО,Фамилия и т.п.`)', reply_markup=nav.menu_b, parse_mode="Markdown")
    elif message.text == '💎 Telegram':
        await message.answer('Выберите один из пунктов.', reply_markup=nav.menu_tg)
    elif message.text == '🔧 Чекер каналов':
        await message.answer('*Введите канал и айди аккаунта.*\nПример:`tg:@visiiione;5182046516` (Приставка `tg:` обязательна)', parse_mode='Markdown')
    elif message.text == 'Колибри клоун':
        await message.answer('Согласен')
    elif message.text == '🏠 Главная':
        await message.answer('*Здарова, брат!* _Бот принимает такие данные, как:_\n\n📲 *Номер телефона* (`Пример: +79876543210, +7 987 654 32 10, +7 (987) 654-32-10, 79876543210`)\n📧 *Адрес эл. почты* (`Пример: aroundtheworld@gmail.com`)\n💎 *Telegram* (`Пример: #446752031`)\n🌐 *IP-адрес* (`Пример: 8.8.8.8`)\n\n⁉️ *Другое* (`Пример: *ФИО,Фамилия и т.п.`)', reply_markup=nav.menu_b, parse_mode="Markdown")
    
    elif message.text == '🗄 Базы данных':
        
        await message.answer('*Введите то, что хотите искать в базах данных.*\nПример: `*Клюев` (Перед запросом писать звездочку).\n\n*💡 Совет:* Если вводишь номер телефона, вводи его без кода страны.', parse_mode="Markdown")
    elif message.text == '👤 Профиль':
        time = 0
        random_code = str(message.from_user.id)
        alarm = '🥶 *Alarm-система:* `выключена`'          
        plan = 'Бесплатный'
        with open('tickets.txt') as file:
          for line in file:
            if random_code in line:
              plan = line.split(';')[2]
        with open('tickets.txt') as file:
          for line in file:
            if random_code in line:
              time = line.split(';')[1]
        global balik
        balik = 0
        with open('balik.txt') as file:
          for line in file:
            if random_code in line:
              darf = line.replace(';', '').replace(random_code, '')
              balik += int(darf)
        
        
        global total
        total = 0

        with open('refs.txt') as file:
            for line in file:
              if user_id in line:
                total += 1
              else:
                total = total
        with open('refff.txt') as file:
            for line in file:
              if user_id in line:
                total += 1
              else:
                total = total
        with open('alarm.txt', encoding='utf-8', errors='ignore') as file:
            for line in file:
                if user_id in line:
                  alarm = '🥶 *Alarm-система*: `включена`'
        global past_cost
        past_cost = 0
        with open('balance.txt', 'r') as file:
          for line in file:
            if random_code in line:
              datagf = line.replace(';', '').replace(random_code, '')
              past_cost += int(datagf)
        balance = '💰 *Баланс:* `'+str(total*2-past_cost+balik)+'` рублей'
        await message.answer('🆔 *Ваш ID:* `'+user_id+'`\n⏳ *Длительность подписки:* `'+str(time)+' дней`\n📊 *Тариф:* `'+plan+'`\n\n'+alarm+'\n🧰 *Перешло по вашей ссылке: *`'+str(total)+'`\n'+balance+'\n🔗 *Ваша персональная ссылка:* `t.me/visionerobot?start='+user_id+'` (`1 реферал = 2 рубля`)', parse_mode='Markdown')
    elif indata == '🗃 Утечка':
        await message.answer('*Введите айди Telegram-аккаунта, чтобы проверить его в утечке.*\nПример: `#51000000` (Решетка в начале сообщения обязательна)', parse_mode='Markdown')
    elif '🌐 IP-адрес' == message.text:
      await message.answer('*Введите IP-адрес.*\nПример: `8.8.8.8`', parse_mode='Markdown')
    elif '.' in message.text:
          ip_in = message.text
          ip = requests.get('http://ipwho.is/'+ip_in).json()
      #try:
          mas = [21, 22, 25, 53, 80, 443]
          try:
            lat = ip['latitude']
            lon = ip['longitude']
          except:
            await message.answer('Х**вый айпишник.')
          loc = f'`{lat},{lon}`'
          org = ip['connection']['isp']
          city = ip['city']
          await message.answer(f'🌐 *IP:* {ip_in}\n\n🏠 *Город:* {city}\n🗺 *Координаты:* {loc}\n\nНеобработанная информация: `{ip}`\n\n_Ищем открытые порты..._', parse_mode='Markdown')
          host = ip_in
          for port in mas:
              s = socket.socket()
              s.settimeout(1)
              try:
                  s.connect((host, port))
              except socket.error:
                  pass
              else:
                  s.close
                  await message.answer('`'+host + '`: *' + str(port) + '* порт активен', parse_mode='Markdown')
          try:
            URLavito = 'https://2whois.ru/?t=whois&data='+ip_in
            HEADERS = {
                "User-Agent":
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"
            }
            ra = requests.get(URLavito, headers=HEADERS)
            soup = BeautifulSoup(ra.content, 'html.parser')
            items = soup.findAll('div', class_='tag-box tag-box-v4 margin-bottom-40')
            comps = []
            for item in items:
                comps.append({
                    'pre':
                        item.find('pre').get_text(strip=True)
                })
          except:
              pass
          try:
            for comp in comps:
                await message.answer(f'*💊 WHOIS данные:*\n\n`{comp["pre"]}`', parse_mode='Markdown')
          except:
            pass
    elif '!' in message.text:
        uid = str(message.from_user.id)
        msgg = str(message.text)
        msggi = str(message.text).replace('!', ';').replace(' ', '')
        tf = int(msgg.split('!')[0])
        print('tff '+str(tf))
        tarif = msgg.split('!')[1]
        with open('buyings.txt', 'a') as f:
          f.write(uid+';'+msggi+';'+tarif+'\n')
        
        random_code = str(message.from_user.id)
        days = msgg.split('!')[0]
        days = int(days)
        daystr = str(days)
        if '-' in daystr:
          pass
        global cost
        global chch
        chch = 0
        cost = 0
        if tarif == 'Профи':
          
          cost = 10*days
        elif tarif == 'Базовый':
          cost = 6*days
        else:
          await message.answer('Недопустимый тариф. Если вы ввели тариф с маленькой буквы, вам нужно ввести с большой.')
          random_code = '0'
          chch = 1
        time = 0
        random_code = str(message.from_user.id)           
        cec = 0
        plan = 'Бесплатный'
        with open('tickets.txt') as file:
          for line in file:
            if random_code in line:
              plan = line.split(';')[2]
        with open('tickets.txt') as file:
          for line in file:
            if random_code in line:
              time = line.split(';')[1]
              cec = 1
        balik = 0
        with open('balik.txt') as file:
          for line in file:
            if random_code in line:
              darf = line.replace(';', '').replace(random_code, '')
              balik += int(darf)
        
        total = 0

        with open('refs.txt') as file:
            for line in file:
              if user_id in line:
                total += 1
              else:
                total = total
        with open('refff.txt') as file:
            for line in file:
              if user_id in line:
                total += 1
              else:
                total = total
        with open('alarm.txt', encoding='utf-8', errors='ignore') as file:
            for line in file:
                if user_id in line:
                  alarm = '🥶 *Alarm-система*: `включена`'
        past_cost = 0
        with open('balance.txt', 'r') as file:
          for line in file:
            if random_code in line:
              datagf = line.replace(';', '').replace(random_code, '')
              past_cost += int(datagf)
        balance = total*2-past_cost+balik
        der = balance-cost
        dera = balance
        print('der '+str(der))
        if cec == 0:
          if chch == 0:
              if der > 0 or der == 0:   
                if cost > 0:
                  with open('balance.txt', 'a') as file:
                    file.write(f'{random_code};{cost}\n')
                    if random_code != 0:
                      await message.answer('Покупка сделана!')
                  with open('tickets.txt', 'a') as file:
                    file.write(f'{random_code};{days};{tarif}\n')
                  if tarif == 'Профи':
                    with open('prems.txt', 'a') as file:
                      file.write(f'{random_code};{days} дней;{tarif}\n')
                  elif tarif != 'Профи':
                    pass
              elif der < 0 or der == dera:
                await message.answer('Недостаточно средств!')
        else:
          await message.answer('У вас уже есть подписка. Дождитесь ее окончания.')
    elif ';;' in message.text:
        try:
          
          uid = str(message.from_user.id)
          
          random_code = random.randint(1, 1000000)
          cost = message.text.replace(';;', '').replace(' ', '')
          check_true = int(cost)
          with open('buyings.txt', 'a') as f:
            f.write(uid+';'+cost+';;\n')
          if config.pay_to_nick:
              link = f"https://qiwi.com/payment/form/99999?extra%5B%27account%27%5D={config.nick}&amountInteger={cost}&amountFraction=0&extra%5B%27comment%27%5D={random_code}&currency=643&blocked%5B0%5D=sum&blocked%5B1%5D=comment&blocked%5B2%5D=account"
      
              payment = InlineKeyboardMarkup()
              payment.add(InlineKeyboardButton('Проверить оплату', callback_data = f'check_payment_{random_code}'), InlineKeyboardButton('Перейти к оплате', url=link))
      
              await message.reply(f'*✉️ Положите деньги на счет ✉️*\n\n📱 *Никнейм:* `{config.nick}`\n🔐 *Комментарий:* `{random_code}`\n💰 *Цена:* `{cost}р`\n\n🚀 _Для удобства перейдите по ссылке._', reply=False, reply_markup=payment, parse_mode='Markdown')
          else:
              link = f"https://qiwi.com/payment/form/99?extra%5B%27account%27%5D={config.number}&amountInteger={cost}&amountFraction=0&extra%5B%27comment%27%5D={random_code}&currency=643&blocked%5B0%5D=sum&blocked%5B1%5D=comment&blocked%5B2%5D=account"
      
              payment = InlineKeyboardMarkup()
              payment.add(InlineKeyboardButton('Проверить оплату', callback_data = f'check_payment_{random_code}'), InlineKeyboardButton('Перейти к оплате', url=link))
      
              await message.reply(f'*✉️ Положите деньги на счет ✉️*\n\n📱 *Номер:* `{config.number}`\n🔐 *Комментарий:* `{random_code}`\n💰 *Цена:* `{cost}р`\n\n🚀 _Для удобства перейдите по ссылке._', reply=False, reply_markup=payment, parse_mode='Markdown')
        except:
          await message.answer('*Некорректный ввод!*\n_Пример правильного ввода:_ ;;100', parse_mode='Markdown')
    elif message.text == '✅ Купить':
        await message.answer('📲 *Чтобы положить деньги на баланс, пропишите:* `/inbuy (СУММА ПОПОЛНЕНИЯ)`, например: `/inbuy 50`\n\n💵 *Чтобы купить подписку в боте, пропишите:* `(КОЛ-ВО ДНЕЙ)!(СУММА ПОПОЛНЕНИЯ)`, например: `1!Профи`\n\n🧿 *Базовый тариф:* 6 рублей за день\n🛡 *Профи-тариф:* 10 рублей за день', parse_mode="Markdown")
        
              
              
    elif message.text == '❓Задать вопрос':
        await message.answer('*Visione* готова ответить на ваш вопрос! Но из-за географического расположения автора, нужно будет *писать ближе к утру:* `с 3:00 до 6:00 по МСК, с 11:00 до 16:00 по МСК`\n\n*Писать сюда*: @kalabarassupport', parse_mode="Markdown")
    elif message.text == '📖 Как искать?':
        await message.answer('*Меню* `>` *(Тип данных)* `>` *Введите то, что нужно найти!*', parse_mode='Markdown')
    elif message.text == '🎊 Поддержать':
        await message.answer('*Visione* ценит поддержку! Заранее *спасибо* за каждый рубль, вложенный в наше развитие!\n\n*QIWI ник:* `VLADONXHACKER` _(не обращайте внимание, он старый :D)_\n*QIWI карта:* `4890 4947 4225 9690`', parse_mode='Markdown')
    elif message.text == '📧 Почта':
        await message.answer('*Введите почту для поиска.*\nПример: `vasya@mail.ru`', parse_mode='Markdown')
    elif message.text == '☎ Номер телефона':
        await message.answer('*Введите номер телефона для поиска.*\nПример: `+79876543210, +7 987 654 32 10, +7 (987) 654-32-10` _(обязательно с плюсом)_', parse_mode='Markdown')

    elif message.text == '🧧 Никнейм':
      await message.answer('*Введите никнейм через "$".*\nПример: `$visione`', parse_mode='Markdown')
    elif '$' in message.text:
      n = await message.answer('🧧 Начинаем искать...')
      nickmail = message.text.replace('$', '')
      try:
            URLavitos = "https://sovaweb.herokuapp.com/find_nick?nick=" + nickmail
            HEADERS = {
                "User-Agent":
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"
            }
            ra = requests.get(URLavitos, headers=HEADERS)
            soup = BeautifulSoup(ra.content, 'html.parser')
            items = soup.findAll('form')
            comps = []
            for item in items:
                comps.append({
                    'infof':
                        item.find('textarea', class_='form-control').get_text(strip=True)
                })
            await n.delete()
            for comp in comps:
                await message.answer(f"📘 Проверка ника:\n\n{comp['infof']}\n")
      except:
          pass
    else:
        await message.answer('*Это заклинание из майнкрафта?* Непонятно, пиши разборчивее.', parse_mode='Markdown')

@dp.callback_query_handler(text_contains='check_payment_')
async def menu(call: types.CallbackQuery):
    uid = str(call.from_user.id)
    code = call.data[14:]
    result_pay = False
    cost = 0
    try:
        with open('buyings.txt') as file:
          for line in file:
            if uid in line:
              cost = line.split(';')[1]
        qiwi_history = await get_history(config.number, config.qiwi)

        for i in range(4):
            if qiwi_history['data'][i]['comment'] == str(code) and qiwi_history['data'][i]['sum']['amount'] == int(cost):
                result_pay = True
                await call.message.edit_text(f'🔐 Оплата найдена 🔐')
                with open('buyings.txt', 'w') as file:
                  file.write('\n')
                with open('balik.txt', 'a') as file:
                  file.write(uid+';'+cost+'\n')
                
        if not result_pay:
            payment = InlineKeyboardMarkup()
            payment.add(InlineKeyboardButton('Проверить оплату', callback_data = f'check_payment_{code}'))
            await bot.send_message(call.from_user.id, 'Платеж не найден.', reply_markup=payment)
    except Exception as e:
        payment = InlineKeyboardMarkup()
        payment.add(InlineKeyboardButton('Проверить оплату', callback_data = f'check_payment_{code}'))
        await bot.send_message(call.from_user.id, "Администратор не настроил оплату, уведомите его об этом")
        print(e)

# --------------------------------------------------------------
# ЗАПУСК БОТА ---------------------------------------------------
keep_alive.keep_alive()
executor.start_polling(dp, skip_updates=True)
# ---------------------------------------------------------------
