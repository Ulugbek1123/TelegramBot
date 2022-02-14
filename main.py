import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
import info as inf


from aiogram.types import URLInputFile


TOKEN = "5183833517:AAGNIXXSOULBeINkcOQ4QRb34DFuRzYSaWA"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Assalomu Alaykum, {0.first_name}. \n SpringWater kompaniyasining rasmiy telegram botiga xush kelibsiz!. '
                                                 '\n Bu yerda siz, murojaatlaringizni qoldirishingiz va mahsulotga '
                                                 'buyurtma berishingiz mumkin.'.format(message.from_user), reply_markup = nav.menuSSettings)
    await bot.send_message(message.from_user.id, 'Tilni tanlang / Выберите язык')

#@dp.message_handler()
#async def bot_message(message: types.Message):
#    #await bot.send_message(message.from_user.id, message.text)
#    if message.text == 'About Us':
#        await bot.send_message(message.from_user.id, inf.about_us)

@dp.message_handler()
async def bot_message(message: types.Message):
    #await bot.send_message(message.from_user.id, message.text)
    if message.text == '🗂 Biz haqimizda':
        await bot.send_message(message.from_user.id, inf.biz_haqimizda)

    elif message.text == '🗂 О нас':
        await bot.send_message(message.from_user.id, inf.biz_haqimizdaRu)

    elif message.text == '🇺🇿 O\'zbek Tili':
        await bot.send_message(message.from_user.id, '🇺🇿 O\'zbek Tili', reply_markup=nav.mainMenu)

    elif message.text == '🇷🇺 Русский язык':
        await bot.send_message(message.from_user.id, '🇷🇺 Русский язык', reply_markup=nav.mainMenuRu)

    elif message.text == '🛒 Mahsulotlar':
        await bot.send_message(message.from_user.id, '🛒 Mahsulotlar', reply_markup = nav.ProductList)

    elif message.text == '🛒 Продукты':
        await bot.send_message(message.from_user.id, '🛒 Продукты', reply_markup = nav.ProductListRu)

    elif message.text == '🧾 Buyurtma Berish':
        await bot.send_message(message.from_user.id,
                               'Quyidagi link orqali ro\'yxatdan o\'ting \nhttps://springwater.uz/order.html',
                               reply_markup=nav.mainMenu)

    elif message.text == '🧾 Заказать':
        await bot.send_message(message.from_user.id,
                               'Заказать по ссылке ниже \nhttps://springwater.uz/order.html',
                               reply_markup=nav.mainMenuRu)



    elif message.text == '⚙ Tilni o\'zgartirish':
        await bot.send_message(message.from_user.id, '🌍 Tilni tanlang', reply_markup = nav.menuSettings)

    elif message.text == '⚙ Изменить язык':
        await bot.send_message(message.from_user.id, '🌍 Выберите язык', reply_markup = nav.menuSettings)

    elif message.text == '📱 Murojaat uchun ma\'lumotlaar':
        await bot.send_message(message.from_user.id, '📱 Murojaat uchun ma\'lumotlaar', reply_markup = nav.contactMenu)

    elif message.text == '📱 Контакты':
        await bot.send_message(message.from_user.id, '📱 Контакты', reply_markup = nav.contactMenuRu)

    elif message.text == '📱 Telefon Raqam':
        await bot.send_message(message.from_user.id, '📱 Telefon raqam: +998942871123')

    elif message.text == '📱 Контактный Телефон':
        await bot.send_message(message.from_user.id, '📱 Контактный Телефон: +998942871123')

    elif message.text == '📨 Электронная почта':
        await bot.send_message(message.from_user.id, '📨 Электронная почта: info@springwater.uz')

    elif message.text == '🌐 Веб-сайт':
        await bot.send_message(message.from_user.id, '🌐 Веб-сайт: www.springwater.uz')

    elif message.text == '🔙 Bosh Menu':
        await bot.send_message(message.from_user.id, 'Main Menu', reply_markup = nav.mainMenu)

    elif message.text == '🔙 Главное меню':
        await bot.send_message(message.from_user.id, 'Главное меню', reply_markup = nav.mainMenuRu)



    #elif message.text == 'Info':
    #    await bot.send_message(message.from_user.id, 'Info about channel')

    #elif message.text == 'Buyurtma Berish':
    #    await bot.send_message(message.from_user.id, 'You can view currency exchange rate')

    # ----------------------------Products-----------------------
    elif message.text == inf.p1:
        await bot.send_photo(message.from_user.id, photo='https://springwater.uz/assets/images/resource/shop/xshop-2.jpg.pagespeed.ic.6aJqDfcWLb.webp',
                             caption='19L Hajmdagi Mineral Suv')
        await bot.send_message(message.from_user.id, '🎁🎁 Ushbu mahsulotimizga buyurtma berib 1ta limonad bonus olasiz')

    elif message.text == inf.p2:
        await bot.send_photo(message.from_user.id, photo='https://springwater.uz/assets/images/resource/shop/xshop-1.jpg.pagespeed.ic.6JI-ATWvCn.webp',
                             caption='6L hajmdagi gazlanmagan suv')

    elif message.text == inf.p3:
        await bot.send_photo(message.from_user.id, photo='https://springwater.uz/assets/images/resource/shop/shop-8.jpg',
                             caption='1.5L Gazlangan suv')

    elif message.text == inf.p4:
        await bot.send_photo(message.from_user.id, photo='https://springwater.uz/assets/images/resource/shop/shop-6.jpg',
                             caption='1.5L Gazlanmagan suv')

    elif message.text == inf.p5:
        await bot.send_photo(message.from_user.id, photo='https://springwater.uz/assets/images/resource/shop/shop-5.jpg',
                             caption='1.0L Gazlangan suv')

    elif message.text == inf.p6:
        await bot.send_photo(message.from_user.id, photo='https://springwater.uz/assets/images/resource/shop/xshop-3.jpg.pagespeed.ic.4xX7r5Ru1U.webp',
                             caption='1.0L Gazlanmagan suv')

    elif message.text == inf.p7:
        await bot.send_photo(message.from_user.id, photo='https://springwater.uz/assets/images/resource/shop/shop-4.jpg',
                             caption='0.33L Gazlangan suv')

    elif message.text == inf.p8:
        await bot.send_photo(message.from_user.id, photo='https://springwater.uz/assets/images/resource/shop/shop-7.jpg',
                             caption='0.33L Gazlanmagan suv')

    # ----------------------------Products----------------------- Russian -------------

    elif message.text == inf.p1ru:
        await bot.send_photo(message.from_user.id, photo='https://springwater.uz/assets/images/resource/shop/xshop-2.jpg.pagespeed.ic.6aJqDfcWLb.webp',
                             caption=inf.p1ru)
        await bot.send_message(message.from_user.id, '🎁🎁 Закажите 19-ти литровую бутыль воды и вы получаете в подарок бонус - 1 шт Лимонода бесплатно.')

    elif message.text == inf.p2ru:
        await bot.send_photo(message.from_user.id, photo='https://springwater.uz/assets/images/resource/shop/xshop-1.jpg.pagespeed.ic.6JI-ATWvCn.webp',
                             caption=inf.p2ru)

    elif message.text == inf.p3ru:
        await bot.send_photo(message.from_user.id, photo='https://springwater.uz/assets/images/resource/shop/shop-8.jpg',
                             caption=inf.p3ru)

    elif message.text == inf.p4ru:
        await bot.send_photo(message.from_user.id, photo='https://springwater.uz/assets/images/resource/shop/shop-6.jpg',
                             caption=inf.p4ru)

    elif message.text == inf.p5ru:
        await bot.send_photo(message.from_user.id, photo='https://springwater.uz/assets/images/resource/shop/shop-5.jpg',
                             caption=inf.p5ru)

    elif message.text == inf.p6ru:
        await bot.send_photo(message.from_user.id, photo='https://springwater.uz/assets/images/resource/shop/xshop-3.jpg.pagespeed.ic.4xX7r5Ru1U.webp',
                             caption=inf.p6ru)

    elif message.text == inf.p7ru:
        await bot.send_photo(message.from_user.id, photo='https://springwater.uz/assets/images/resource/shop/shop-4.jpg',
                             caption=inf.p7ru)

    elif message.text == inf.p8ru:
        await bot.send_photo(message.from_user.id, photo='https://springwater.uz/assets/images/resource/shop/shop-7.jpg',
                             caption=inf.p8ru)


#async def command_order(message: types.Message):
  #  if message.text == '🧾 Buyurtma Berish':
  #      await message.reply('Telefon raqamingizni region kodi bilan kiriting \n'
  #                          'Masalan, + 998 xx xxx xx xx', reply_markup=nav.btnOrder)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)

