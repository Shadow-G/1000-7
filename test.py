import keyboard 
import time

time.sleep(3.0)

x = 1000
# Работает
while x >= 0:
	x = x - 7

	f = open('D:\\Counter-Strike 1.6\\cstrike\\my_cfg_spam.cfg', 'w')
	f.write('bind "p" "say {}"'.format(x))
	f.close()

	keyboard.send("i")

	time.sleep(0.3)

	keyboard.send("p")

	time.sleep(1.0)


""" Метод 1
import keyboard 
import time

time.sleep(3.0)

x = 1000
o = 0
while x >= 0:
	o += 1
	x = x - 7

	# print(str(x) + '|' + str(o))
	
	# xl = x
	
	# keyboard.send("u")
	
	# time.sleep(0.1)

	# xx = list(str(xl))

	# keyboard.send(xx[0])
	# time.sleep(0.1)
	# keyboard.send(xx[1])
	# time.sleep(0.1)
	# keyboard.send(xx[2])

	# keyboard.send("Enter")
	# time.sleep(1.0) """




""" 
cs1.6 
bind "(кнопка)" "say (слово)"
bind "j" "say New" 
bind "p" "say Hello" 

cstrikie/my_cfg_spam.cfg

1) Создаем cfg с биндом на вывод текста в чате
my_cfg_spam.cfg
>> bind "p" "say Lol"

2) В основном cfg добавляем бинд на добавление нашего cfg
config.cfg
>> bind "i" "exec my_cfg_spam.cfg"

3) обновляем текст в нашем cfg
4) нажимаем кнопку 'i' обновления нашего cfg
5) Нажимаем на кнопку 'p' из нашего cgf
"""