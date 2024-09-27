import telebot
import sqlite3
from telebot import types

bot = telebot.TeleBot("7292791343:AAERxmcgjgd7vzDbXobKAExpiqcVXRZamMI")


insert_professions = [
    (1, 'Водитель такси', 60000),
    (2, 'Курьер', 61000),
    (3, 'Программист', 130000),
    (4, 'Аниматор', 40000),
    (5, 'Оператор call-центра', 41000),
    (6, 'Бариста/бармен', 35000),
    (7, 'Официант', 50000),
    (8, 'Промоутер', 42000),
    (9, 'Менеджер по продажам', 70000),
    (10, 'Мерчандайзер', 50000),
    (11, 'Продавец-консультант', 40000),
    (12, 'Финансовый менеджер', 70000),
    (13, 'Клиентский менеджер', 80000),
    (14, 'Кредитный специалист', 40000),
    (15, 'Системный аналитик', 200000),
    (16, 'Системный администратор', 70000),
    (17, 'Программист 1С', 100000),
    (18, 'Врач-терапевт', 95000),
    (19, 'Врач-невролог', 85000),
    (20, 'Медсестра', 50000),
    (21, 'Врач — анестезиолог-реаниматолог', 120000),
    (22, 'Администратор', 60000),
    (23, 'Секретарь', 55000),
    (24, 'Офис-менеджер', 65000),
    (25, 'Маркетолог', 105000),
    (26, 'Графический дизайнер', 65000),
    (27, 'Контент-менеджер', 50000),
    (28, 'Электрогазосварщик', 135000),
    (29, 'Электромонтажник', 85000),
    (30, 'Токарь', 150000),
    (31, 'Инженер-сметчик', 80000),
    (32, 'Инженер ПТО', 130000),
    (33, 'Риелтор', 81000),
    (34, 'Инженер-конструктор', 75000),
    (35, 'Специалист по охране труда', 70000),
    (36, 'Инженер-технолог', 71000),
    (37, 'Бухгалтер', 75000),
    (38, 'Экономист', 60000),
    (39, 'Финансовый контролер', 100000)
]

    
@bot.message_handler(commands=['start'])
def start (message):
	with sqlite3.connect('professii_database.db') as db:
		cursor = db.cursor()
		query = """ INSERT INTO professions(id, name, amount ) VALUES (?,?,?)"""
		cursor.executemany(query, insert_professions)
		db.commit()
		print(cursor.rowcount, "Строк добавлено")
    
	markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
	item1 = types.KeyboardButton ('Начать искать профессию!')
	item2 = types.KeyboardButton('О боте')
	item3 = types.KeyboardButton('Информация')
	markup.add (item1, item2, item3)
	bot.send_message(message.chat.id, 'Привет, {0.first_name}!'. format (message. from_user), reply_markup = markup)


@bot.message_handler(content_types=['text'])
def proffes(message):
	if message.chat.type == 'private':
		if message.text == 'Начать искать профессию!':
			markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
			back = types.KeyboardButton('Назад')
			item1 = types.KeyboardButton('Продажи')
			item2 = types.KeyboardButton('Медицина и фармацевтика')
			item3 = types.KeyboardButton('Административный персонал')
			item4 = types.KeyboardButton('Информационные технологии, интернет, телеком')
			item5 = types.KeyboardButton('Банки, инвестиции, лизинг')
			item6 = types.KeyboardButton('Маркетинг, реклама, PR')
			item7 = types.KeyboardButton('Рабочий персонал')
			item8 = types.KeyboardButton('Строительство и недвижимость')
			item9 = types.KeyboardButton('Производство и сельское хозяйство')
			item10 = types.KeyboardButton('Бухгалтерия, управленческий учет, финансы предприятия')
			item11 = types.KeyboardButton('Другое')
			markup.add (back, item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11)
			msg = bot.send_message(message.chat.id, 'Выберите сферу которую вы хотите', reply_markup = markup)
			bot.register_next_step_handler(msg, user_answer)

		elif message.text == 'О боте':
			markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
			back = types.KeyboardButton('Назад')
			markup.add (back)
			bot.send_message(message.chat.id, 'Бот  сделан на языке PYTHON🌐и является Советчиком по выбору карьеры и профессии👮‍♂️👨‍🚒👨‍⚕️ Для написания бота использовалась база данных и много-много времени', reply_markup = markup)

		elif message.text == 'Информация':
			markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
			back = types.KeyboardButton('Назад')
			markup.add (back)
			bot.send_message(message.chat.id, 'Привет👋, я юный разработчик👨‍💻.Меня зовут Мамиев Рафаэль. мне 13 лет, я из города Москвы. Это мой итоговый проект курса Python 3 в Kodland. Мой проект сделан на языке PYTHON🌐. Я буду делать проект "Советчик по выбору карьеры и профессии"👮‍♂️👨‍🚒👨‍⚕️. Постараюсь всё сделать максимально хорошо💯.', reply_markup = markup)

		elif message.text == 'Назад':
			markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
			item1 = types.KeyboardButton ('Начать искать профессию!')
			item2 = types.KeyboardButton('О боте')
			item3 = types.KeyboardButton(' Информация')
			markup.add (item1, item2, item3)
			bot.send_message(message.chat.id, 'Возвращение в главное меню', reply_markup = markup)

		
			
def user_answer(message):
	if message.text == 'Продажи':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		item1 = types.KeyboardButton('50000+')
		item2 = types.KeyboardButton('40000+')
		item3 = types.KeyboardButton('70000+')
		back = types.KeyboardButton('Назад')
		markup.add (item1, item2, item3, back)
		msg = bot.send_message(message.chat.id, 'Нашлось три работы✅! Выберите зарплату которую бы вы хотели получать💰', reply_markup = markup)
		bot.register_next_step_handler(msg, user_answer1)
	
	elif message.text == 'Медицина и фармацевтика':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		item1 = types.KeyboardButton('95000+')
		item2 = types.KeyboardButton('85000+')
		item3 = types.KeyboardButton('50000+')
		back = types.KeyboardButton('Назад')
		markup.add (item1, item2, item3, back)
		msg = bot.send_message(message.chat.id, 'Нашлось три работы✅! Выберите зарплату которую бы вы хотели получать💰', reply_markup = markup)
		bot.register_next_step_handler(msg, user_answer2)

	elif message.text == 'Административный персонал':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		item1 = types.KeyboardButton('55000+')
		item2 = types.KeyboardButton('60000+')
		item3 = types.KeyboardButton('65000+')
		back = types.KeyboardButton('Назад')
		markup.add (item1, item2, item3, back)
		msg = bot.send_message(message.chat.id, 'Нашлось три работы✅! Выберите зарплату которую бы вы хотели получать💰', reply_markup = markup)
		bot.register_next_step_handler(msg, user_answer3)

	elif message.text == 'Информационные технологии, интернет, телеком':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		item1 = types.KeyboardButton('200000+')
		item2 = types.KeyboardButton('70000+')
		item3 = types.KeyboardButton('100000+')
		back = types.KeyboardButton('Назад')
		markup.add (item1, item2, item3, back)
		msg = bot.send_message(message.chat.id, 'Нашлось три работы✅! Выберите зарплату которую бы вы хотели получать💰', reply_markup = markup)
		bot.register_next_step_handler(msg, user_answer4)

	elif message.text == 'Банки, инвестиции, лизинг':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		item1 = types.KeyboardButton('70000+')
		item2 = types.KeyboardButton('80000+')
		item3 = types.KeyboardButton('40000+')
		back = types.KeyboardButton('Назад')
		markup.add (item1, item2, item3, back)
		msg = bot.send_message(message.chat.id, 'Нашлось три работы✅! Выберите зарплату которую бы вы хотели получать💰', reply_markup = markup)
		bot.register_next_step_handler(msg, user_answer5)

	elif message.text == 'Маркетинг, реклама, PR':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		item1 = types.KeyboardButton('105000+')
		item2 = types.KeyboardButton('65000+')
		item3 = types.KeyboardButton('50000+')
		back = types.KeyboardButton('Назад')
		markup.add (item1, item2, item3, back)
		msg = bot.send_message(message.chat.id, 'Нашлось три работы✅! Выберите зарплату которую бы вы хотели получать💰', reply_markup = markup)
		bot.register_next_step_handler(msg, user_answer6)

	elif message.text == 'Рабочий персонал':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		item1 = types.KeyboardButton('85000+')
		item2 = types.KeyboardButton('135000+')
		item3 = types.KeyboardButton('150000+')
		back = types.KeyboardButton('Назад')
		markup.add (item1, item2, item3, back)
		msg = bot.send_message(message.chat.id, 'Нашлось три работы✅! Выберите зарплату которую бы вы хотели получать💰', reply_markup = markup)
		bot.register_next_step_handler(msg, user_answer7)

	elif message.text == 'Строительство и недвижимость':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		item1 = types.KeyboardButton('80000+')
		item2 = types.KeyboardButton('81000+')
		item3 = types.KeyboardButton('130000+')
		back = types.KeyboardButton('Назад')
		markup.add (item1, item2, item3, back)
		msg = bot.send_message(message.chat.id, 'Нашлось три работы✅! Выберите зарплату которую бы вы хотели получать💰', reply_markup = markup)
		bot.register_next_step_handler(msg, user_answer8)

	elif message.text == 'Производство и сельское хозяйство':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		item1 = types.KeyboardButton('70000+')
		item2 = types.KeyboardButton('71000+')
		item3 = types.KeyboardButton('75000+')
		back = types.KeyboardButton('Назад')
		markup.add (item1, item2, item3, back)
		msg = bot.send_message(message.chat.id, 'Нашлось три работы✅! Выберите зарплату которую бы вы хотели получать💰', reply_markup = markup)
		bot.register_next_step_handler(msg, user_answer9)

	elif message.text == 'Бухгалтерия, управленческий учет, финансы предприятия':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		item1 = types.KeyboardButton('60000+')
		item2 = types.KeyboardButton('75000+')
		item3 = types.KeyboardButton('100000+')
		back = types.KeyboardButton('Назад')
		markup.add (item1, item2, item3, back)
		msg = bot.send_message(message.chat.id, 'Нашлось три работы✅! Выберите зарплату которую бы вы хотели получать💰', reply_markup = markup)
		bot.register_next_step_handler(msg, user_answer10)
	
	elif message.text == 'Назад':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		item1 = types.KeyboardButton ('Начать искать профессию!')
		item2 = types.KeyboardButton('О боте')
		item3 = types.KeyboardButton(' Информация')
		markup.add (item1, item2, item3)
		bot.send_message(message.chat.id, 'Возвращение в главное меню', reply_markup = markup)
	
	elif message.text == 'Начать искать профессию!':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		back = types.KeyboardButton('Назад')
		item1 = types.KeyboardButton('Продажи')
		item2 = types.KeyboardButton('Медицина и фармацевтика')
		item3 = types.KeyboardButton('Административный персонал')
		item4 = types.KeyboardButton('Информационные технологии, интернет, телеком')
		item5 = types.KeyboardButton('Банки, инвестиции, лизинг')
		item6 = types.KeyboardButton('Маркетинг, реклама, PR')
		item7 = types.KeyboardButton('Рабочий персонал')
		item8 = types.KeyboardButton('Строительство и недвижимость')
		item9 = types.KeyboardButton('Производство и сельское хозяйство')
		item10 = types.KeyboardButton('Бухгалтерия, управленческий учет, финансы предприятия')
		item11 = types.KeyboardButton('Другое')
		markup.add (back, item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11)
		msg = bot.send_message(message.chat.id, 'Выберите сферу которую вы хотите', reply_markup = markup)
		bot.register_next_step_handler(msg, user_answer)
	
	elif message.text == 'О боте':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		back = types.KeyboardButton('Назад')
		markup.add (back)
		bot.send_message(message.chat.id, 'Бот  сделан на языке PYTHON🌐и является Советчиком по выбору карьеры и профессии👮‍♂️👨‍🚒👨‍⚕️ Для написания бота использовалась база данных и много-много времени', reply_markup = markup)

	elif message.text == 'Информация':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		back = types.KeyboardButton('Назад')
		markup.add (back)
		bot.send_message(message.chat.id, 'Привет👋, я юный разработчик👨‍💻.Меня зовут Мамиев Рафаэль. мне 13 лет, я из города Москвы. Это мой итоговый проект курса Python 3 в Kodland. Мой проект сделан на языке PYTHON🌐. Я буду делать проект "Советчик по выбору карьеры и профессии"👮‍♂️👨‍🚒👨‍⚕️. Постараюсь всё сделать максимально хорошо💯.', reply_markup = markup)

	elif message.text == 'Другое':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		item1 = types.KeyboardButton('35000+')
		item2 = types.KeyboardButton('40000+')
		item3 = types.KeyboardButton('41000+')
		item4 = types.KeyboardButton('42000+')
		item5 = types.KeyboardButton('50000+')
		item6 = types.KeyboardButton('60000+')
		item7 = types.KeyboardButton('61000+')
		item8 = types.KeyboardButton('130000+')
		back = types.KeyboardButton('Назад')
		markup.add (item1, item2, item3, item4, item5, item6, item7, item8, back)
		msg = bot.send_message(message.chat.id, 'Нашлось восемь работ✅! Выберите зарплату которую бы вы хотели получать💰', reply_markup = markup)
		bot.register_next_step_handler(msg, user_answer11)


def user_answer1(message):
	if message.text == '50000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 10').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == '40000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 11').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == '70000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 12').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == 'Назад':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		item1 = types.KeyboardButton ('Начать искать профессию!')
		item2 = types.KeyboardButton('О боте')
		item3 = types.KeyboardButton(' Информация')
		markup.add (item1, item2, item3)
		bot.send_message(message.chat.id, 'Возвращение в главное меню', reply_markup = markup)

	elif message.text == 'Начать искать профессию!':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		back = types.KeyboardButton('Назад')
		item1 = types.KeyboardButton('Продажи')
		item2 = types.KeyboardButton('Медицина и фармацевтика')
		item3 = types.KeyboardButton('Административный персонал')
		item4 = types.KeyboardButton('Информационные технологии, интернет, телеком')
		item5 = types.KeyboardButton('Банки, инвестиции, лизинг')
		item6 = types.KeyboardButton('Маркетинг, реклама, PR')
		item7 = types.KeyboardButton('Рабочий персонал')
		item8 = types.KeyboardButton('Строительство и недвижимость')
		item9 = types.KeyboardButton('Производство и сельское хозяйство')
		item10 = types.KeyboardButton('Бухгалтерия, управленческий учет, финансы предприятия')
		item11 = types.KeyboardButton('Другое')
		markup.add (back, item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11)
		msg = bot.send_message(message.chat.id, 'Выберите сферу которую вы хотите', reply_markup = markup)
		bot.register_next_step_handler(msg, user_answer)

	elif message.text == 'О боте':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		back = types.KeyboardButton('Назад')
		markup.add (back)
		bot.send_message(message.chat.id, 'Бот  сделан на языке PYTHON🌐и является Советчиком по выбору карьеры и профессии👮‍♂️👨‍🚒👨‍⚕️ Для написания бота использовалась база данных и много-много времени', reply_markup = markup)

	elif message.text == 'Информация':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		back = types.KeyboardButton('Назад')
		markup.add (back)
		bot.send_message(message.chat.id, 'Привет👋, я юный разработчик👨‍💻.Меня зовут Мамиев Рафаэль. мне 13 лет, я из города Москвы. Это мой итоговый проект курса Python 3 в Kodland. Мой проект сделан на языке PYTHON🌐. Я буду делать проект "Советчик по выбору карьеры и профессии"👮‍♂️👨‍🚒👨‍⚕️. Постараюсь всё сделать максимально хорошо💯.', reply_markup = markup)

def user_answer2(message):
	if message.text == '95000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 18').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == '85000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 19').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == '50000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 20').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == 'Назад':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		item1 = types.KeyboardButton ('Начать искать профессию!')
		item2 = types.KeyboardButton('О боте')
		item3 = types.KeyboardButton(' Информация')
		markup.add (item1, item2, item3)
		bot.send_message(message.chat.id, 'Возвращение в главное меню', reply_markup = markup)

	elif message.text == 'Начать искать профессию!':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		back = types.KeyboardButton('Назад')
		item1 = types.KeyboardButton('Продажи')
		item2 = types.KeyboardButton('Медицина и фармацевтика')
		item3 = types.KeyboardButton('Административный персонал')
		item4 = types.KeyboardButton('Информационные технологии, интернет, телеком')
		item5 = types.KeyboardButton('Банки, инвестиции, лизинг')
		item6 = types.KeyboardButton('Маркетинг, реклама, PR')
		item7 = types.KeyboardButton('Рабочий персонал')
		item8 = types.KeyboardButton('Строительство и недвижимость')
		item9 = types.KeyboardButton('Производство и сельское хозяйство')
		item10 = types.KeyboardButton('Бухгалтерия, управленческий учет, финансы предприятия')
		item11 = types.KeyboardButton('Другое')
		markup.add (back, item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11)
		msg = bot.send_message(message.chat.id, 'Выберите сферу которую вы хотите', reply_markup = markup)
		bot.register_next_step_handler(msg, user_answer)

	elif message.text == 'О боте':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		back = types.KeyboardButton('Назад')
		markup.add (back)
		bot.send_message(message.chat.id, 'Бот  сделан на языке PYTHON🌐и является Советчиком по выбору карьеры и профессии👮‍♂️👨‍🚒👨‍⚕️ Для написания бота использовалась база данных и много-много времени', reply_markup = markup)

	elif message.text == 'Информация':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		back = types.KeyboardButton('Назад')
		markup.add (back)
		bot.send_message(message.chat.id, 'Привет👋, я юный разработчик👨‍💻.Меня зовут Мамиев Рафаэль. мне 13 лет, я из города Москвы. Это мой итоговый проект курса Python 3 в Kodland. Мой проект сделан на языке PYTHON🌐. Я буду делать проект "Советчик по выбору карьеры и профессии"👮‍♂️👨‍🚒👨‍⚕️. Постараюсь всё сделать максимально хорошо💯.', reply_markup = markup)

def user_answer3(message):
	if message.text == '55000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 23').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == '60000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 22').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == '65000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 24').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == 'Назад':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		item1 = types.KeyboardButton ('Начать искать профессию!')
		item2 = types.KeyboardButton('О боте')
		item3 = types.KeyboardButton(' Информация')
		markup.add (item1, item2, item3)
		bot.send_message(message.chat.id, 'Возвращение в главное меню', reply_markup = markup)

	elif message.text == 'Начать искать профессию!':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		back = types.KeyboardButton('Назад')
		item1 = types.KeyboardButton('Продажи')
		item2 = types.KeyboardButton('Медицина и фармацевтика')
		item3 = types.KeyboardButton('Административный персонал')
		item4 = types.KeyboardButton('Информационные технологии, интернет, телеком')
		item5 = types.KeyboardButton('Банки, инвестиции, лизинг')
		item6 = types.KeyboardButton('Маркетинг, реклама, PR')
		item7 = types.KeyboardButton('Рабочий персонал')
		item8 = types.KeyboardButton('Строительство и недвижимость')
		item9 = types.KeyboardButton('Производство и сельское хозяйство')
		item10 = types.KeyboardButton('Бухгалтерия, управленческий учет, финансы предприятия')
		item11 = types.KeyboardButton('Другое')
		markup.add (back, item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11)
		msg = bot.send_message(message.chat.id, 'Выберите сферу которую вы хотите', reply_markup = markup)
		bot.register_next_step_handler(msg, user_answer)

	elif message.text == 'О боте':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		back = types.KeyboardButton('Назад')
		markup.add (back)
		bot.send_message(message.chat.id, 'Бот  сделан на языке PYTHON🌐и является Советчиком по выбору карьеры и профессии👮‍♂️👨‍🚒👨‍⚕️ Для написания бота использовалась база данных и много-много времени', reply_markup = markup)

	elif message.text == 'Информация':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		back = types.KeyboardButton('Назад')
		markup.add (back)
		bot.send_message(message.chat.id, 'Привет👋, я юный разработчик👨‍💻.Меня зовут Мамиев Рафаэль. мне 13 лет, я из города Москвы. Это мой итоговый проект курса Python 3 в Kodland. Мой проект сделан на языке PYTHON🌐. Я буду делать проект "Советчик по выбору карьеры и профессии"👮‍♂️👨‍🚒👨‍⚕️. Постараюсь всё сделать максимально хорошо💯.', reply_markup = markup)

def user_answer4(message):
	if message.text == '200000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 15').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == '70000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 16').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == '100000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 17').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == 'Назад':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		item1 = types.KeyboardButton ('Начать искать профессию!')
		item2 = types.KeyboardButton('О боте')
		item3 = types.KeyboardButton(' Информация')
		markup.add (item1, item2, item3)
		bot.send_message(message.chat.id, 'Возвращение в главное меню', reply_markup = markup)

	elif message.text == 'Начать искать профессию!':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		back = types.KeyboardButton('Назад')
		item1 = types.KeyboardButton('Продажи')
		item2 = types.KeyboardButton('Медицина и фармацевтика')
		item3 = types.KeyboardButton('Административный персонал')
		item4 = types.KeyboardButton('Информационные технологии, интернет, телеком')
		item5 = types.KeyboardButton('Банки, инвестиции, лизинг')
		item6 = types.KeyboardButton('Маркетинг, реклама, PR')
		item7 = types.KeyboardButton('Рабочий персонал')
		item8 = types.KeyboardButton('Строительство и недвижимость')
		item9 = types.KeyboardButton('Производство и сельское хозяйство')
		item10 = types.KeyboardButton('Бухгалтерия, управленческий учет, финансы предприятия')
		item11 = types.KeyboardButton('Другое')
		markup.add (back, item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11)
		msg = bot.send_message(message.chat.id, 'Выберите сферу которую вы хотите', reply_markup = markup)
		bot.register_next_step_handler(msg, user_answer)

	elif message.text == 'О боте':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		back = types.KeyboardButton('Назад')
		markup.add (back)
		bot.send_message(message.chat.id, 'Бот  сделан на языке PYTHON🌐и является Советчиком по выбору карьеры и профессии👮‍♂️👨‍🚒👨‍⚕️ Для написания бота использовалась база данных и много-много времени', reply_markup = markup)

	elif message.text == 'Информация':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		back = types.KeyboardButton('Назад')
		markup.add (back)
		bot.send_message(message.chat.id, 'Привет👋, я юный разработчик👨‍💻.Меня зовут Мамиев Рафаэль. мне 13 лет, я из города Москвы. Это мой итоговый проект курса Python 3 в Kodland. Мой проект сделан на языке PYTHON🌐. Я буду делать проект "Советчик по выбору карьеры и профессии"👮‍♂️👨‍🚒👨‍⚕️. Постараюсь всё сделать максимально хорошо💯.', reply_markup = markup)

def user_answer5(message):
	if message.text == '70000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 12').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == '80000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 13').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == '40000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 14').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == 'Назад':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		item1 = types.KeyboardButton ('Начать искать профессию!')
		item2 = types.KeyboardButton('О боте')
		item3 = types.KeyboardButton(' Информация')
		markup.add (item1, item2, item3)
		bot.send_message(message.chat.id, 'Возвращение в главное меню', reply_markup = markup)

	elif message.text == 'Начать искать профессию!':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		back = types.KeyboardButton('Назад')
		item1 = types.KeyboardButton('Продажи')
		item2 = types.KeyboardButton('Медицина и фармацевтика')
		item3 = types.KeyboardButton('Административный персонал')
		item4 = types.KeyboardButton('Информационные технологии, интернет, телеком')
		item5 = types.KeyboardButton('Банки, инвестиции, лизинг')
		item6 = types.KeyboardButton('Маркетинг, реклама, PR')
		item7 = types.KeyboardButton('Рабочий персонал')
		item8 = types.KeyboardButton('Строительство и недвижимость')
		item9 = types.KeyboardButton('Производство и сельское хозяйство')
		item10 = types.KeyboardButton('Бухгалтерия, управленческий учет, финансы предприятия')
		item11 = types.KeyboardButton('Другое')
		markup.add (back, item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11)
		msg = bot.send_message(message.chat.id, 'Выберите сферу которую вы хотите', reply_markup = markup)
		bot.register_next_step_handler(msg, user_answer)

	elif message.text == 'О боте':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		back = types.KeyboardButton('Назад')
		markup.add (back)
		bot.send_message(message.chat.id, 'Бот  сделан на языке PYTHON🌐и является Советчиком по выбору карьеры и профессии👮‍♂️👨‍🚒👨‍⚕️ Для написания бота использовалась база данных и много-много времени', reply_markup = markup)

	elif message.text == 'Информация':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		back = types.KeyboardButton('Назад')
		markup.add (back)
		bot.send_message(message.chat.id, 'Привет👋, я юный разработчик👨‍💻.Меня зовут Мамиев Рафаэль. мне 13 лет, я из города Москвы. Это мой итоговый проект курса Python 3 в Kodland. Мой проект сделан на языке PYTHON🌐. Я буду делать проект "Советчик по выбору карьеры и профессии"👮‍♂️👨‍🚒👨‍⚕️. Постараюсь всё сделать максимально хорошо💯.', reply_markup = markup)

def user_answer6(message):
	if message.text == '105000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 25').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == '65000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 26').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == '50000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 27').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == 'Назад':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		item1 = types.KeyboardButton ('Начать искать профессию!')
		item2 = types.KeyboardButton('О боте')
		item3 = types.KeyboardButton(' Информация')
		markup.add (item1, item2, item3)
		bot.send_message(message.chat.id, 'Возвращение в главное меню', reply_markup = markup)

	elif message.text == 'Начать искать профессию!':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		back = types.KeyboardButton('Назад')
		item1 = types.KeyboardButton('Продажи')
		item2 = types.KeyboardButton('Медицина и фармацевтика')
		item3 = types.KeyboardButton('Административный персонал')
		item4 = types.KeyboardButton('Информационные технологии, интернет, телеком')
		item5 = types.KeyboardButton('Банки, инвестиции, лизинг')
		item6 = types.KeyboardButton('Маркетинг, реклама, PR')
		item7 = types.KeyboardButton('Рабочий персонал')
		item8 = types.KeyboardButton('Строительство и недвижимость')
		item9 = types.KeyboardButton('Производство и сельское хозяйство')
		item10 = types.KeyboardButton('Бухгалтерия, управленческий учет, финансы предприятия')
		item11 = types.KeyboardButton('Другое')
		markup.add (back, item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11)
		msg = bot.send_message(message.chat.id, 'Выберите сферу которую вы хотите', reply_markup = markup)
		bot.register_next_step_handler(msg, user_answer)

	elif message.text == 'О боте':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		back = types.KeyboardButton('Назад')
		markup.add (back)
		bot.send_message(message.chat.id, 'Бот  сделан на языке PYTHON🌐и является Советчиком по выбору карьеры и профессии👮‍♂️👨‍🚒👨‍⚕️ Для написания бота использовалась база данных и много-много времени', reply_markup = markup)

	elif message.text == 'Информация':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		back = types.KeyboardButton('Назад')
		markup.add (back)
		bot.send_message(message.chat.id, 'Привет👋, я юный разработчик👨‍💻.Меня зовут Мамиев Рафаэль. мне 13 лет, я из города Москвы. Это мой итоговый проект курса Python 3 в Kodland. Мой проект сделан на языке PYTHON🌐. Я буду делать проект "Советчик по выбору карьеры и профессии"👮‍♂️👨‍🚒👨‍⚕️. Постараюсь всё сделать максимально хорошо💯.', reply_markup = markup)

def user_answer7(message):
	if message.text == '85000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 29').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == '135000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 28').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == '150000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 30').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == 'Назад':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		item1 = types.KeyboardButton ('Начать искать профессию!')
		item2 = types.KeyboardButton('О боте')
		item3 = types.KeyboardButton(' Информация')
		markup.add (item1, item2, item3)
		bot.send_message(message.chat.id, 'Возвращение в главное меню', reply_markup = markup)

	elif message.text == 'Начать искать профессию!':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		back = types.KeyboardButton('Назад')
		item1 = types.KeyboardButton('Продажи')
		item2 = types.KeyboardButton('Медицина и фармацевтика')
		item3 = types.KeyboardButton('Административный персонал')
		item4 = types.KeyboardButton('Информационные технологии, интернет, телеком')
		item5 = types.KeyboardButton('Банки, инвестиции, лизинг')
		item6 = types.KeyboardButton('Маркетинг, реклама, PR')
		item7 = types.KeyboardButton('Рабочий персонал')
		item8 = types.KeyboardButton('Строительство и недвижимость')
		item9 = types.KeyboardButton('Производство и сельское хозяйство')
		item10 = types.KeyboardButton('Бухгалтерия, управленческий учет, финансы предприятия')
		item11 = types.KeyboardButton('Другое')
		markup.add (back, item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11)
		msg = bot.send_message(message.chat.id, 'Выберите сферу которую вы хотите', reply_markup = markup)
		bot.register_next_step_handler(msg, user_answer)

	elif message.text == 'О боте':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		back = types.KeyboardButton('Назад')
		markup.add (back)
		bot.send_message(message.chat.id, 'Бот  сделан на языке PYTHON🌐и является Советчиком по выбору карьеры и профессии👮‍♂️👨‍🚒👨‍⚕️ Для написания бота использовалась база данных и много-много времени', reply_markup = markup)

	elif message.text == 'Информация':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		back = types.KeyboardButton('Назад')
		markup.add (back)
		bot.send_message(message.chat.id, 'Привет👋, я юный разработчик👨‍💻.Меня зовут Мамиев Рафаэль. мне 13 лет, я из города Москвы. Это мой итоговый проект курса Python 3 в Kodland. Мой проект сделан на языке PYTHON🌐. Я буду делать проект "Советчик по выбору карьеры и профессии"👮‍♂️👨‍🚒👨‍⚕️. Постараюсь всё сделать максимально хорошо💯.', reply_markup = markup)

def user_answer8(message):
	if message.text == '80000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 31').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == '81000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 33').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == '130000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 32').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == 'Назад':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		item1 = types.KeyboardButton ('Начать искать профессию!')
		item2 = types.KeyboardButton('О боте')
		item3 = types.KeyboardButton(' Информация')
		markup.add (item1, item2, item3)
		bot.send_message(message.chat.id, 'Возвращение в главное меню', reply_markup = markup)

	elif message.text == 'Начать искать профессию!':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		back = types.KeyboardButton('Назад')
		item1 = types.KeyboardButton('Продажи')
		item2 = types.KeyboardButton('Медицина и фармацевтика')
		item3 = types.KeyboardButton('Административный персонал')
		item4 = types.KeyboardButton('Информационные технологии, интернет, телеком')
		item5 = types.KeyboardButton('Банки, инвестиции, лизинг')
		item6 = types.KeyboardButton('Маркетинг, реклама, PR')
		item7 = types.KeyboardButton('Рабочий персонал')
		item8 = types.KeyboardButton('Строительство и недвижимость')
		item9 = types.KeyboardButton('Производство и сельское хозяйство')
		item10 = types.KeyboardButton('Бухгалтерия, управленческий учет, финансы предприятия')
		item11 = types.KeyboardButton('Другое')
		markup.add (back, item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11)
		msg = bot.send_message(message.chat.id, 'Выберите сферу которую вы хотите', reply_markup = markup)
		bot.register_next_step_handler(msg, user_answer)

	elif message.text == 'О боте':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		back = types.KeyboardButton('Назад')
		markup.add (back)
		bot.send_message(message.chat.id, 'Бот  сделан на языке PYTHON🌐и является Советчиком по выбору карьеры и профессии👮‍♂️👨‍🚒👨‍⚕️ Для написания бота использовалась база данных и много-много времени', reply_markup = markup)

	elif message.text == 'Информация':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		back = types.KeyboardButton('Назад')
		markup.add (back)
		bot.send_message(message.chat.id, 'Привет👋, я юный разработчик👨‍💻.Меня зовут Мамиев Рафаэль. мне 13 лет, я из города Москвы. Это мой итоговый проект курса Python 3 в Kodland. Мой проект сделан на языке PYTHON🌐. Я буду делать проект "Советчик по выбору карьеры и профессии"👮‍♂️👨‍🚒👨‍⚕️. Постараюсь всё сделать максимально хорошо💯.', reply_markup = markup)

def user_answer9(message):
	if message.text == '70000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 35').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == '71000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 36').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == '75000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 34').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == 'Назад':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		item1 = types.KeyboardButton ('Начать искать профессию!')
		item2 = types.KeyboardButton('О боте')
		item3 = types.KeyboardButton(' Информация')
		markup.add (item1, item2, item3)
		bot.send_message(message.chat.id, 'Возвращение в главное меню', reply_markup = markup)

	elif message.text == 'Начать искать профессию!':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		back = types.KeyboardButton('Назад')
		item1 = types.KeyboardButton('Продажи')
		item2 = types.KeyboardButton('Медицина и фармацевтика')
		item3 = types.KeyboardButton('Административный персонал')
		item4 = types.KeyboardButton('Информационные технологии, интернет, телеком')
		item5 = types.KeyboardButton('Банки, инвестиции, лизинг')
		item6 = types.KeyboardButton('Маркетинг, реклама, PR')
		item7 = types.KeyboardButton('Рабочий персонал')
		item8 = types.KeyboardButton('Строительство и недвижимость')
		item9 = types.KeyboardButton('Производство и сельское хозяйство')
		item10 = types.KeyboardButton('Бухгалтерия, управленческий учет, финансы предприятия')
		item11 = types.KeyboardButton('Другое')
		markup.add (back, item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11)
		msg = bot.send_message(message.chat.id, 'Выберите сферу которую вы хотите', reply_markup = markup)
		bot.register_next_step_handler(msg, user_answer)

	elif message.text == 'О боте':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		back = types.KeyboardButton('Назад')
		markup.add (back)
		bot.send_message(message.chat.id, 'Бот  сделан на языке PYTHON🌐и является Советчиком по выбору карьеры и профессии👮‍♂️👨‍🚒👨‍⚕️ Для написания бота использовалась база данных и много-много времени', reply_markup = markup)

	elif message.text == 'Информация':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		back = types.KeyboardButton('Назад')
		markup.add (back)
		bot.send_message(message.chat.id, 'Привет👋, я юный разработчик👨‍💻.Меня зовут Мамиев Рафаэль. мне 13 лет, я из города Москвы. Это мой итоговый проект курса Python 3 в Kodland. Мой проект сделан на языке PYTHON🌐. Я буду делать проект "Советчик по выбору карьеры и профессии"👮‍♂️👨‍🚒👨‍⚕️. Постараюсь всё сделать максимально хорошо💯.', reply_markup = markup)

def user_answer10(message):
	if message.text == '60000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 38').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == '75000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 37').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == '100000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 39').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == 'Назад':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		item1 = types.KeyboardButton ('Начать искать профессию!')
		item2 = types.KeyboardButton('О боте')
		item3 = types.KeyboardButton(' Информация')
		markup.add (item1, item2, item3)
		bot.send_message(message.chat.id, 'Возвращение в главное меню', reply_markup = markup)

	elif message.text == 'Начать искать профессию!':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		back = types.KeyboardButton('Назад')
		item1 = types.KeyboardButton('Продажи')
		item2 = types.KeyboardButton('Медицина и фармацевтика')
		item3 = types.KeyboardButton('Административный персонал')
		item4 = types.KeyboardButton('Информационные технологии, интернет, телеком')
		item5 = types.KeyboardButton('Банки, инвестиции, лизинг')
		item6 = types.KeyboardButton('Маркетинг, реклама, PR')
		item7 = types.KeyboardButton('Рабочий персонал')
		item8 = types.KeyboardButton('Строительство и недвижимость')
		item9 = types.KeyboardButton('Производство и сельское хозяйство')
		item10 = types.KeyboardButton('Бухгалтерия, управленческий учет, финансы предприятия')
		item11 = types.KeyboardButton('Другое')
		markup.add (back, item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11)
		msg = bot.send_message(message.chat.id, 'Выберите сферу которую вы хотите', reply_markup = markup)
		bot.register_next_step_handler(msg, user_answer)

	elif message.text == 'О боте':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		back = types.KeyboardButton('Назад')
		markup.add (back)
		bot.send_message(message.chat.id, 'Бот  сделан на языке PYTHON🌐и является Советчиком по выбору карьеры и профессии👮‍♂️👨‍🚒👨‍⚕️ Для написания бота использовалась база данных и много-много времени', reply_markup = markup)

	elif message.text == 'Информация':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		back = types.KeyboardButton('Назад')
		markup.add (back)
		bot.send_message(message.chat.id, 'Привет👋, я юный разработчик👨‍💻.Меня зовут Мамиев Рафаэль. мне 13 лет, я из города Москвы. Это мой итоговый проект курса Python 3 в Kodland. Мой проект сделан на языке PYTHON🌐. Я буду делать проект "Советчик по выбору карьеры и профессии"👮‍♂️👨‍🚒👨‍⚕️. Постараюсь всё сделать максимально хорошо💯.', reply_markup = markup)

def user_answer11(message):
	if message.text == '35000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 6').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == '40000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 4').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == '41000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 5').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == '42000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 8').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == '50000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 7').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == '60000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 1').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == '61000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 2').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == '130000+':
		with sqlite3.connect('professii_database.db') as db:
			cursor = db.cursor()
			job = cursor.execute('SELECT name FROM professions WHERE id = 3').fetchone()
			name = job[0]
			bot.send_message(message.chat.id, f'Ваша работа: {name}')
	elif message.text == 'Назад':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		item1 = types.KeyboardButton ('Начать искать профессию!')
		item2 = types.KeyboardButton('О боте')
		item3 = types.KeyboardButton(' Информация')
		markup.add (item1, item2, item3)
		bot.send_message(message.chat.id, 'Возвращение в главное меню', reply_markup = markup)

	elif message.text == 'Начать искать профессию!':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		back = types.KeyboardButton('Назад')
		item1 = types.KeyboardButton('Продажи')
		item2 = types.KeyboardButton('Медицина и фармацевтика')
		item3 = types.KeyboardButton('Административный персонал')
		item4 = types.KeyboardButton('Информационные технологии, интернет, телеком')
		item5 = types.KeyboardButton('Банки, инвестиции, лизинг')
		item6 = types.KeyboardButton('Маркетинг, реклама, PR')
		item7 = types.KeyboardButton('Рабочий персонал')
		item8 = types.KeyboardButton('Строительство и недвижимость')
		item9 = types.KeyboardButton('Производство и сельское хозяйство')
		item10 = types.KeyboardButton('Бухгалтерия, управленческий учет, финансы предприятия')
		item11 = types.KeyboardButton('Другое')
		markup.add (back, item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11)
		msg = bot.send_message(message.chat.id, 'Выберите сферу которую вы хотите', reply_markup = markup)
		bot.register_next_step_handler(msg, user_answer)

	elif message.text == 'О боте':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		back = types.KeyboardButton('Назад')
		markup.add (back)
		bot.send_message(message.chat.id, 'Бот  сделан на языке PYTHON🌐и является Советчиком по выбору карьеры и профессии👮‍♂️👨‍🚒👨‍⚕️ Для написания бота использовалась база данных и много-много времени', reply_markup = markup)

	elif message.text == 'Информация':
		markup = types. ReplyKeyboardMarkup(resize_keyboard = True)
		back = types.KeyboardButton('Назад')
		markup.add (back)
		bot.send_message(message.chat.id, 'Привет👋, я юный разработчик👨‍💻.Меня зовут Мамиев Рафаэль. мне 13 лет, я из города Москвы. Это мой итоговый проект курса Python 3 в Kodland. Мой проект сделан на языке PYTHON🌐. Я буду делать проект "Советчик по выбору карьеры и профессии"👮‍♂️👨‍🚒👨‍⚕️. Постараюсь всё сделать максимально хорошо💯.', reply_markup = markup)


bot.infinity_polling()
