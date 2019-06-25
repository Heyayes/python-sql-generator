from random import randint as ri
from datetime import datetime
import time

number_of_orders = 30000 # Задаём число нужных сущностей заказов.
saches_count = 5   # Эта строка и три ниже отражают количество существующих
cover_count = 3    # сущностей в БД, идентификаторы которых будут вложены
delivery_count = 4 # в запрос.
canvas_count = 4   #

def readToList(filename):
  return [line.strip() for line in open(filename,'r',encoding='utf-8')]

def getRand(input):
  if type(input) == int  : return ri(1,input)
  if type(input) == list : return input[ri(0,len(input)-1)]

def phonegen():
  return '790'+str(ri(10000000,99999999))

def getRandomOrdeState():
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

def getBoy():
  return str('%s %s %s' % (getRand(bnm), getRand(bfn), getRand(bsn)))

def getGirl():
  return str('%s %s %s' % (getRand(gnm), getRand(gfn), getRand(gsn)))

def getPerson():
  choise = ri(0,1)
  return getGirl() if choise == 1 else getBoy()

#Возвращает случайный адрес вида "г.Москва, Пролетарская набережная, дом 41, кв.88"
def getAddress():
  return str('г.%s, %s, дом %d, кв.%d' % 
    (getRand(city), getRand(street), ri(1,50), ri(1,150)))

def getOrderCort():
	return (getAddress(), getPerson(), phonegen(), getRand(delivery_count), 
		getRandomOrdeState(), ri(1000,3000), getTrueOrFalse(), get_date(), 
		getRand(canvas_count), getTrueOrFalse(), getRand(saches_count), getRand(cover_count))

# Объявление списков имен, отчеств и фамилий g*-женских, b*-мужских
# *fn - отчество, *sn - фамилия, *nm - имя
bfn = readToList('boys/fathername')
bsn = readToList('boys/surname')
bnm = readToList('boys/name')
gfn = readToList('girls/fathername')
gsn = readToList('girls/surname')
gnm = readToList('girls/name')
city = readToList('address/city')
street = readToList('address/street')

output = open('insert_orders.sql','w', encoding='utf-8')
# будем генерировать sql запрос для заполнения таблицы заказов из сырых данных 
output.write("insert into ORDERS (ADRESS, RECIPIENT, PHONE, DELIVERYTYPE_ID, ORDERSTATE, SUMM, HAVEPATCH, ORDER_DATE, CANVAS_ID, PAYED, SACHE_ID, COVER_ID)\n")
output.write("VALUES\n")

for i in range(0,number_of_orders-1):
  output.write("\t('%s', '%s', '%s', %d, '%s', %d, %s, to_date('dd.mm.yyyy', '%s'), %d, %s, %d, %d ),\n" % getOrderCort())

output.write("\t('%s', '%s', '%s', %d, '%s', %d, %s, to_date('dd.mm.yyyy', '%s'), %d, %s, %d, %d );" % getOrderCort())

output.close()
