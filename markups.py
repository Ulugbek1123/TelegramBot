from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import info as a
btnMain = KeyboardButton('🔙 Bosh Menu')
btnMainRu = KeyboardButton('🔙 Главное меню')

# ---- Main menu ----
btnAbout = KeyboardButton('🗂 Biz haqimizda')
btnProducts = KeyboardButton('🛒 Mahsulotlar')
btnOrder = KeyboardButton('🧾 Buyurtma Berish', url='https://springwater.uz/order.html')
btnContact = KeyboardButton('📱 Murojaat uchun ma\'lumotlaar')
btnSettings = KeyboardButton('⚙ Tilni o\'zgartirish')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnAbout, btnProducts, btnOrder, btnContact).add(btnSettings)

# --------------Русский язык ---------------
btnAboutRu = KeyboardButton('🗂 О нас')
btnProductsRu = KeyboardButton('🛒 Продукты')
btnOrderRu = KeyboardButton('🧾 Заказать', url='https://springwater.uz/order.html')
btnContactRu = KeyboardButton('📱 Контакты')
btnSettingsRu = KeyboardButton('⚙ Изменить язык')
mainMenuRu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnAboutRu, btnProductsRu, btnOrderRu, btnContactRu).add(btnSettingsRu)



# ----  Contacts Menu ----
btnPhone = KeyboardButton('📱 Telefon Raqam')
btnEmail = KeyboardButton('📨 Email')
btnWebSite = KeyboardButton('🌐 Web site')
contactMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnPhone, btnEmail, btnWebSite, btnMain)



# ----  Contacts Menu Russian ----
btnPhoneRu = KeyboardButton('📱 Контактный Телефон')
btnEmailRu = KeyboardButton('📨 Электронная почта')
btnWebSiteRu = KeyboardButton('🌐 Веб-сайт')
contactMenuRu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnPhoneRu, btnEmailRu, btnWebSiteRu, btnMainRu)


# ----  Other Menu ----




# ----  Product List ----
btn1 = KeyboardButton(a.p1)
btn2 = KeyboardButton(a.p2)
btn3 = KeyboardButton(a.p3)
btn4 = KeyboardButton(a.p4)
btn5 = KeyboardButton(a.p5)
btn6 = KeyboardButton(a.p6)
btn7 = KeyboardButton(a.p7)
btn8 = KeyboardButton(a.p8)
ProductList = ReplyKeyboardMarkup(resize_keyboard=True).add(btn1).add(btn2).add(btn3).add(btn4).add(btn5).add(btn6).add(btn7).add(btn8).add(btnOrder).add(btnMain)


# ----  Product List Russian ----
btn1ru = KeyboardButton(a.p1ru)
btn2ru = KeyboardButton(a.p2ru)
btn3ru = KeyboardButton(a.p3ru)
btn4ru = KeyboardButton(a.p4ru)
btn5ru = KeyboardButton(a.p5ru)
btn6ru = KeyboardButton(a.p6ru)
btn7ru = KeyboardButton(a.p7ru)
btn8ru = KeyboardButton(a.p8ru)
ProductListRu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn1ru).add(btn2ru).add(btn3ru).add(btn4ru).add(btn5ru).add(btn6ru).add(btn7ru).add(btn8ru).add(btnOrderRu).add(btnMainRu)



# ---- Order ----
btnContact = KeyboardButton('Telefon raqamni jo\'natish', request_contact=True, one_time_keyboard=True)
btnOrder = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(btnContact)


# ---- Language ----

btnUz = KeyboardButton('🇺🇿 O\'zbek Tili')
btnRu = KeyboardButton('🇷🇺 Русский язык')
menuSettings = ReplyKeyboardMarkup(resize_keyboard=True).add(btnUz, btnRu).add(btnMain)
#menuSettings = KeyboardButton('Tilni o\'zgartirish')

menuSSettings = ReplyKeyboardMarkup(resize_keyboard=True).add(btnUz, btnRu)