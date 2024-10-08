import sqlite3 

insert_professions = [
    (1, 'Водитель такси'),
    (2, 'Курьер'),
    (3, 'Программист'),
    (4, 'Аниматор'),
    (5, 'Оператор call-центра'),
    (6, 'Бариста/бармен'),
    (7, 'Официант'),
    (8, 'Промоутер'),
    (9, 'Менеджер по продажам'),
    (10, 'Мерчандайзер'),
    (11, 'Продавец-консультант'),
    (12, 'Финансовый менеджер'),
    (13, 'Клиентский менеджер'),
    (14, 'Кредитный специалист'),
    (15, 'Системный аналитик'),
    (16, 'Системный администратор'),
    (17, 'Программист 1С'),
    (18, 'Врач-терапевт'),
    (19, 'Врач-невролог'),
    (20, 'Медсестра'),
    (21, 'Врач — анестезиолог-реаниматолог'),
    (22, 'Администратор'),
    (23, 'Секретарь'),
    (24, 'Офис-менеджер'),
    (25, 'Маркетолог'),
    (26, 'Графический дизайнер'),
    (27, 'Контент-менеджер'),
    (28, 'Электрогазосварщик'),
    (29, 'Электромонтажник'),
    (30, 'Токарь'),
    (31, 'Инженер-сметчик'),
    (32, 'Инженер ПТО'),
    (33, 'Риелтор'),
    (34, 'Инженер-конструктор'),
    (35, 'Специалист по охране труда'),
    (36, 'Инженер-технолог'),
    (37, 'Бухгалтер'),
    (38, 'Экономист'),
    (39, 'Финансовый контролер'),
]

with sqlite3.connect('professii_database.db') as db:
    cursor = db.cursor()
    query1 = """ INSERT INTO professions (id, name) VALUES (?,?) ; """
    query2 = """ INSERT INTO professions (id, name) VALUES (?,?) ; """
    query3 = """ INSERT INTO professions (id, name) VALUES (?,?) ; """
    cursor.executemany(query1,insert_professions)
    cursor.executemany(query2,insert_professions)
    cursor.executemany(query3,insert_professions)
    db.commit()
    print(cursor.rowcount, "Строк добавлено")

insert_payments = [
    (1, 120000),
    (2, 100000),
    (3, 130000),
    (4, 40000),
    (5, 40000),
    (6, 35000),
    (7, 50000),
    (8, 40000),
    (9, 70000),
    (10, 50000),
    (11, 40000),
    (12, 70000),
    (13, 80000),
    (14, 40000),
    (15, 200000),
    (16, 70000),
    (17, 100000),
    (18, 95000),
    (19, 85000),
    (20, 50000),
    (21, 120000),
    (22, 60000),
    (23, 55000),
    (24, 65000),
    (25, 105000),
    (26, 65000),
    (27, 50000),
    (28, 135000),
    (29, 85000),
    (30, 150000),
    (31, 80000),
    (32, 130000),
    (33, 80000),
    (34, 75000),
    (35, 70000),
    (36, 70000),
    (37, 75000),
    (38, 60000),
    (39, 100000)
]

with sqlite3.connect('professii_database.db') as db:
    cursor = db.cursor()
    query = """ INSERT INTO payments(id, amount) VALUES (?,?)"""
    cursor.executemany(query, insert_payments)
    db.commit()
    print(cursor.rowcount, "Строк добавлено")
    

