from random import randint as ri
from datetime import datetime
import time

number_of_orders = 30000 # Задаём число нужных сущностей заказов.
saches_count = 5   # Эта строка и три ниже отражают количество существующих
cover_count = 3    # сущностей в БД, идентификаторы которых будут вложены
delivery_count = 4 # в запрос.
canvas_count = 4   #

# Объявление списков имен, отчеств и фамилий g*-женских, b*-мужских
# *fn - отчество, *sn - фамилия, *nm - имя
bfn =    [line.strip() for line in open('boys/fathername','r',encoding='utf-8')]
bsn =    [line.strip() for line in open('boys/surname','r',encoding='utf-8')]
bnm =    [line.strip() for line in open('boys/name','r',encoding='utf-8')]
gfn =    [line.strip() for line in open('girls/fathername','r',encoding='utf-8')]
gsn =    [line.strip() for line in open('girls/surname','r',encoding='utf-8')]
gnm =    [line.strip() for line in open('girls/name','r',encoding='utf-8')]
city =   [line.strip() for line in open('address/city','r',encoding='utf-8')]
street = [line.strip() for line in open('address/street','r',encoding='utf-8')]

def getRand(input):
  if type(input) == int  : return ri(1,input)
  if type(input) == list : return input[ri(0,len(input)-1)]

def phonegen():
  return '790'+str(ri(10000000,99999999))

def getordestate():
  states = ['CREATED','PROCESS','SENDED','DELIVERED'] #Массив возможных статусов заявлений
  return getRand(states)

def getTrueOrFalse():
  boolean = ['TRUE','FALSE']
  return getRand(boolean)

#Возвращает случайную дату от 01.01.2017 до настоящего момента
def get_date(): 
  now = int(time.time()) 
  later = 1483228800 #01.01.2017 in timestamp 
  return str(datetime.utcfromtimestamp(ri(later,now)).strftime('%d.%m.%Y')) 

def get_boy():
  return str('%s %s %s' % (getRand(bnm), getRand(bfn), getRand(bsn)))

def get_girl():
  return str('%s %s %s' % (getRand(gnm), getRand(gfn), getRand(gsn)))

def get_person():
  choise = ri(0,1)
  return get_girl() if choise == 1 else get_boy()

#Возвращает случайный адрес вида "г.Москва, Пролетарская набережная, дом 41, кв.88"
def get_address():
  return str('г.%s, %s, дом %d, кв.%d' % 
    (getRand(city), getRand(street), ri(1,50), ri(1,150)))


output = open('insert_orders.sql','w', encoding='utf-8')
# будем генерировать sql запрос для заполнения таблицы заказов из сырых данных 
output.write("insert into ORDERS (ADRESS, RECIPIENT, PHONE, DELIVERYTYPE_ID, ORDERSTATE, SUMM, HAVEPATCH, ORDER_DATE, CANVAS_ID, PAYED, SACHE_ID, COVER_ID)\n")
output.write("VALUES\n")

for i in range(0,number_of_orders-1):
  output.write('\t(\'%s\', \'%s\', \'%s\', %d, \'%s\', %d, %s, to_date(\'dd.mm.yyyy\', \'%s\'), %d, %s, %d, %d ),\n' 
    % (get_address(), get_person(), phonegen(), getRand(delivery_count), getordestate(), ri(1000,3000), getTrueOrFalse(), get_date(), getRand(canvas_count), getTrueOrFalse(), getRand(saches_count), getRand(cover_count)))

output.write('\t(\'%s\', \'%s\', \'%s\', %d, \'%s\', %d, %s, to_date(\'dd.mm.yyyy\', \'%s\'), %d, %s, %d, %d );' 
    % (get_address(), get_person(), phonegen(), getRand(delivery_count), getordestate(), ri(1000,3000), getTrueOrFalse(), get_date(), getRand(canvas_count), getTrueOrFalse(), getRand(saches_count), getRand(cover_count)))

output.close()
