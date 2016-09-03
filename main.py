'''
Created on Sep 3, 2016

@author: anatoly
'''
import functions


if __name__ == '__main__':
    pass

print("Hello World")


mysql_host = 'localhost'
# mysql_host = '10.30.1.14'
mysql_database = 'gosms'
mysql_username = 'root'
mysql_password = ''

p = []
p.append(r'^VISA(?P<NCARD>\d{4}) (?P<DATE>\d{2}\.\d{2}\.\d{2}) (?P<TIME>\d{2}\:\d{2}) покупка (?P<SUM>[0-9.]+)р (?P<WHERE>.*) Баланс: (?P<BALANCE>[0-9.]+)р$')
p.append(r'^VISA(?P<NCARD>\d{4}) (?P<DATE>\d{2}\.\d{2}\.\d{2}) (?P<TIME>\d{2}\:\d{2}) списание (?P<SUM>[0-9.]+)р (?P<OTHER>.*\ )?Баланс: (?P<BALANCE>[0-9.]+)р$')
p.append(r'^VISA(?P<NCARD>\d{4}) (?P<DATE>\d{2}\.\d{2}\.\d{2}) (?P<TIME>\d{2}\:\d{2}) выдача наличных (?P<SUM>[0-9.]+)р (?P<WHERE>.*) Баланс: (?P<BALANCE>[0-9.]+)р$')
p.append(r'^VISA(?P<NCARD>\d{4}) (?P<DATE>\d{2}\.\d{2}\.\d{2}) (?P<TIME>\d{2}\:\d{2}) оплата услуг (?P<SUM>[0-9.]+)р (?P<OTHER>.* )?Баланс: (?P<BALANCE>[0-9.]+)р$')
p.append(r'^VISA(?P<NCARD>\d{4}) (?P<DATE>\d{2}\.\d{2}\.\d{2}) оплата Мобильного банка за (?P<PERIOD>.*) (?P<SUM>[0-9.]+)р Баланс: (?P<BALANCE>[0-9.]+)р$')

p.append(r'^VISA(?P<NCARD>\d{4}) (?P<DATE>\d{2}\.\d{2}\.\d{2}) (?P<TIME>\d{2}\:\d{2}) (?:зачисление|поправка по счету) (?P<SUM>[0-9.]+)р (?:[A-Z0-9 ]+)?Баланс: (?P<BALANCE>[0-9.]+)р$')
p.append(r'^VISA(?P<NCARD>\d{4}) (?P<DATE>\d{2}\.\d{2}\.\d{2}) (?P<TIME>\d{2}\:\d{2}) зачисление (?P<SUM>[0-9.]+)р (?P<OTHER>[A-Z0-9 ]+ )?s karty (?P<FROM>\d{4}\*\*\*\*\d{4}) Баланс: (?P<BALANCE>[0-9.]+)р$')
p.append(r'^VISA(?P<NCARD>\d{4})\: (?P<TIME>\d{2}\:\d{2})(?:\:\d{2})? зачисление (?P<SUM>[0-9.]+)р(?:\.)? от отправителя (?P<FROM>[А-Я. ]+)(?: Сообщение: )?(?P<MESSAGE>.+)?$')
p.append(r'^Сбербанк Онлайн. (?P<WHO>[А-Я. ]+) перевел\(а\) Вам (?P<SUM>[0-9.]+) RUB(?:. Сообщение: )?(?P<MESSAGE>.*)?$')

p.append(r'^(?P<DATE>\d{2}\.\d{2}\.\d{2}) (?P<WHO>.*) оплатил\(а\) Ваш телефон ([0-9]{10}) (?P<SUM>[0-9.]+)р\. Ваш Сбербанк!$')

p.append(r'^VISA(?P<NCARD>\d{4})\: перевод (?P<SUM>[0-9.]+).*на карту получателя (?P<WHO>[А-Я. ]+) (?P<OTHER>[A-Z]{4}\d{4} )?выполнен.*')

#

p.append(r'.*(?:Чтобы присвоить получателю|Операция не выполнена|Имя присвоено|Обязательный платеж|Неизвестный смс-запрос|Для перевода|Вход в Сбербанк Онлайн|пароль|Пароль|ОТКАЗ|Для оплаты|К сожалению|Отправьте СМС|Экономьте свое время|Рады сообщить|Предоставление услуги|Для по).*')
p.append(r'.*(?:\n.*)*(?:Уважаемый клиент|Ваша заявка|выполнена регистрация|Мобильный банк|успейте купить|можете воспользоваться).*')

# p1 = []
# for i in range(len(p)):
# 	p1.append(0)

# p2 = 0

# mn = -1
# mn = 12

# Типы расходов
# types = ['Снятие','Перевод','Оплата']

# Места выдачи наличных
# type1 = []

# Адресаты при переводе
# type2 = []

# Места оплаты
# type3 = []


# for a in get_dict(r'C:\gosms\gosms.xml'):
# d = a['date']
# b = a['body']
# matched = False
# for aa in range(len(p)):
#    m = re.match(p[aa],b)
#   if m:
#     p1[aa] += 1
#     matched = True
#     if mn >= 0 and aa == mn:
#       print(m.groups())
#       print (b)
#     break
# if not matched:
#   p2 += 1
#   if mn == -1:
#     print(a)
# print(p1, p2)
# print(get_dict(r'C:\gosms\gosms.xml'))

# sql = "CREATE DATABASE 'gosms'"
# sql = "SHOW TABLES LIKE 'credit_card'"
# sql = """INSERT INTO contacts(name, mail, adres, tel) VALUES ('%(name)s', '%(mail)s', '%(adres)s', '%(tel)s')"""%{"name":fname, "mail":fmail, "adres":fadres, "tel":ftel}
# sql = """INSERT INTO contacts(name, mail, adres, tel) VALUES ('%(name)s', '%(mail)s', '%(adres)s', '%(tel)s')"""%{"name":fname, "mail":fmail, "adres":fadres, "tel":ftel}


xml1 = functions.Xml_(r'C:\gosms\gosms.xml')
# xml1 = xml_('/home/anatoly/yandex.disk/gosms/gosms.xml')
# print(xml1.get_dict())

test = functions.Mysql_(host=mysql_host, username=mysql_username, password=mysql_password, database=mysql_database)
# test.tables_create()
print(test.table_list())
# print(test.card_add('тест'))
# print(test.cards_get())
b = test.table_list()
