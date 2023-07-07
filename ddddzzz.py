>> import tkinter

Если
Python
ответит
ImportError: No
module
named
'tkinter', то
вам
нужно
установить
этот
пакет.Установить
стандартный
пакет
в
Python
очень
просто, для
этого
есть
специальный
менеджер
пакетов(pip).Чтобы
воспользоваться
им, запустите
терминал(в
Windows
для
этого
нужно
нажать
Пуск, набрать
cmd
и
нажать
Enter).В
терминале
нужно
набрать:

> pip
install
tkinter
Затем
нужно
нажать
Enter
и
ввести(y), чтобы
подтвердить
установку
пакета.

Позже
мы
поговорим
про
pip
более
подробно, пока
он
нужен
нам
лишь
для
установки
одного
пакета.

Итак, после
того
как
пакет
установлен, мы
можем
написать
нашу
первую
программу, использующую
графический
интерфейс:

import tkinter

master = tkinter.Tk()
master.mainloop()
После
её
выполнения
на
экране
должно
появиться
окно.Пока
это
можно
только
подвигать
или
закрыть, потому
что
мы
ничем
его
не
наполнили.Прежде
чем
переходить
к
наполнению, обсудим, что
делают
написанные
нами
строчки.

Первая — просто
подключение
пакета, с
такими
строчками
мы
уже
встречались.

Вторая
строчка
создает
объект
Tk() — основное
окно.Дальше
мы
будем
наполнять
его
объектами.

Третья
строчка — самая
необычная.Дело
в
том, что
приложение
с
графическим
интерфейсом
работает
не
так, как
консольные
приложения, которые
мы
писали
раньше.В
консольных
приложениях
компьютер
исполнял
наши
инструкции
одну
за
другой.В
программе
с
графическим
интерфейсом
такой
подход
работать
не
будет, потому
что
компьютер
должен
реагировать
на
действия
пользователя.Поэтому
вместо
того, чтобы
выполнять
команды, он
ждет
сигналов
от
пользователя, которые
нужно
как - то
обрабатывать.

Команда
master.mainloop()
запускает
для
нашего
окна «основной
цикл».Он
получает
информацию
о
важных
событиях(нажатии
клавиш, движениях
мышки
и
пр.), обрабатывает
эти
события
и
перерисовывает
окно.

Так
работают
все
приложения
с
графическим
интерфейсом.Если
вы
пользуетесь
Windows, то
наверняка
встречали
сообщение, что
какая - то
программа «не
отвечает».Обычно
это
означает, что
внутри
основного
цикла
что - то
пошло
не
так(например, программа
вошла
в
бесконечный
цикл).Система
продолжает
посылать
программе
сообщения
о
событиях, но
та
перестала
их
принимать, потому
что
занята
чем - то
другим.

Обратите
внимание, что
выполнение
программы
как
бы
приостанавливается, когда
она
доходит
до
команды
master.mainloop(), и
продолжается
только
после
закрытия
окна.Попробуйте
предсказать, что
произойдет
со
следующей
программой(а
потом
проверьте
свое
предположение):

import tkinter

master = tkinter.Tk()
master.mainloop()
x = input()
print(x)

Прежде, чем
писать
программу, по - настоящему
взаимодействующую
с
пользователем, мы
научимся
рисовать.Для
начала
нужно
создать
холст(canvas), на
котором
потом
будут
располагаться
картинки:

import tkinter

master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='black', height=600, width=600)
canvas.pack()
master.mainloop()
Команда
сanvas.pack()
добавляет
в
окно
объект
canvas.То
же
самое
можно
сделать
командой
canvas.grid(), но
работают
они
немного
по - разному: grid
располагает
объекты
на
сетке, а
pack
пытается
их «упаковать».

Попробуйте
поменять
параметры
bg(сокращение
для
background), height
и
width.Посмотрите, что
меняется, если
заменить
canvas.pack()
на
canvas.grid().Цвет
может
быть
либо
фиксированным
названием
цвета(white, black, red, green, blue, cyan, yellow, magenta)
либо
строкой
вида
'#RRGGBB'.RR, GG
и
BB — значения
красной, синей
и
зелёной
компоненты
в
диапазоне
от
0
до
255, записанные
в
шестнадцатеричной
системе
счисления.Поэкспериментируйте
с
этим.

Необязательная
задача.Напишите
функцию, которая
принимает
на
вход
три
числа(красную, зеленую
и
синюю
компоненту) и
выдает
цвет
в
описанном
выше
формате.

Теперь
пора
что - нибудь
нарисовать.

import tkinter

master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='white', height=600, width=600)
canvas.create_line((0, 0), (600, 600), fill='red')
canvas.pack()
master.mainloop()
Команде
create_line
можно
задать
больше
точек — тогда
получится
ломаная:

import tkinter

master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='white', height=600, width=600)
canvas.create_line((0, 0), (300, 200), (600, 600), (200, 300), (0, 0), fill='red')
c.pack()
master.mainloop()
Задача: Посмотрите, что
выводит
следующая
программа
и
исправьте
ее
так, чтобы
получилась
пятиконечная
звезда:

import tkinter

master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='white', height=600, width=600)
p1 = (400.0, 300.0),
p2 = (331, 395)
p3 = (219, 359)
p4 = (200, 241)
p5 = (330, 205)
canvas.create_line(p1, p3, p5, p4, p2, p1, fill='red')
canvas.pack()
master.mainloop()
Необязательная
домашняя
задача
со
звездочкой.Напишите
программу, которая
получает
на
вход
число
n
и
рисует
n - конечную
звезду.

(Подсказка
 : координаты вершин правильного n-угольника с центром в 0 -- \cos\left(\frac{2\pi k}{n}\right),\:\sin\left(\frac
{2\pi
k}{n}\right),  \:k\ :=  \:1...n ).Чтобы
получилась
звезда, нужно
обойти
вершины
этого
многоугольника
в
правильном
порядке.

Задача.Напишите
программу, которая
рисует
на
холсте
сетку
8
на
8.

Теперь
научимся
рисовать
круг
или
эллипс:

import tkinter

master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='white', height=600, width=600)
canvas.create_oval((0, 0), (100, 100), fill='red')
canvas.create_oval((200, 200), (300, 400), fill='green')
canvas.pack()
master.mainloop()
Если
нужно
нарисовать
много
эллипсов, можно
использовать
цикл:

import tkinter

master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='white', height=600, width=600)
for x in range(0, 600, 20):
    canvas.create_oval((x, x), (x + 20, x + 20), fill='red')
canvas.pack()
master.mainloop()

Задача.Нарисуйте
доску
с
расставленными
шашками(постарайтесь
сделать
это
как
можно
эффективнее, не
рисуя
каждую
по
отдельности).

Задача
на
дом.Найдите
в
интернете, какие
еще
команды
рисования
есть
у
tkinter.Canvas
и
поэкспериментируйте
с
ними.

Теперь
пришло
время
научить
нашу
программу
взаимодействовать
с
пользователем.Для
этого
нужно
связать
каждое
его
действие
с
функцией, которая
будет
выполняться
после
этого
действия.
Это
делается
с
помощью
команды
bind.Эта
функция
получает
на
вход
название
события
и
функцию, которую
нужно
выполнить, когда
событие
происходит:

import tkinter


def draw(event):
    canvas.create_oval((100, 100), (300, 300), fill='red')
    return


master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='blue', height=600, width=600)
canvas.pack()
master.bind("<KeyPress>", draw)
master.mainloop()

В
данном
случае
мы
обрабатываем
событие < KeyPressed >: нажатие
любой
клавиши.Tkinter
знает
много
разных
событий, вы
можете
самостоятельно
прочитать
про
них
в
документации.В
этом
уроке
прочие
события
нам
не
понадобятся.

Команда
master.bind("<KeyPress>", draw)
означает, что
каждый
раз, когда
пользователь
нажимает
клавишу, вызывается
функция
draw.В
качестве
аргумента
этой
функции
передается
переменная
event, в
которой
содержится
описание
события.

Задача.Измените
программу
так, чтобы
она
рисовала
круг
случайного
размера
в
случайном
месте.

(Вредный
 совет: теперь вы тоже можете сделать так, чтобы ваша программа «не отвечала».Для этого нужно добавить в обработку события бесконечный цикл.)

Обратите
внимание, что
функция
получает
на
вход
один
аргумент — описание
события, которое
её
вызывает.В
этой
переменной
хранится
вся
возможная
информация
о
событии.

В
частности, можно
узнать, какая
клавиша
была
нажата:

import tkinter


def draw(event):
    if event.char == 'r':
        canvas.create_oval((100, 100), (300, 300), fill='red')
    if event.char == 'g':
        canvas.create_oval((100, 100), (300, 300), fill='green')
    if event.char == 'b':
        canvas.create_oval((100, 100), (300, 300), fill='blue')


master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='blue', height=600, width=600)
canvas.pack()
master.bind("<KeyPress>", draw)
master.mainloop()
На
самом
деле, информация
о
том, какая
клавиша
нажата, хранится
сразу
в
нескольких
полях:

char — символ, который
появляется
при
нажатии
клавиши.Однако
это
поле
определено
не
всегда: например, когда
вы
нажимаете
Shift, никакого
символа
не
появляется.
keysym — символическое
описание
нажатой
клавиши(например, Return, Shift_L(левый
шифт), Alt_R
и
т.п.).
keysym_num — число, соответствующее
этому
описанию.
keycode — код
нажатой
клавиши.Клавиши
могут
иметь
одинаковый
код, но
разный
keysym, мы
встретимся
с
таким
случаем
чуть
дальше.
Как
узнать
keysym
нужной
вам
клавиши? Можно
посмотреть
в
интернете, но
интереснее
написать
программу, которая
их
выводит.

Для
этого
нам
понадобится
новый
инструмент — поле
с
текстом.Этот
инструмент
называется
Label:

import tkinter

master = tkinter.Tk()
label = tkinter.Label(master, text="Hello world!")
label.pack()
master.mainloop()
Давайте
напишем
программу, которая
выводит
keysym
для
нажатой
клавиши:

import tkinter


def show_key(event):
    label.config(text=event.keysym)


master = tkinter.Tk()
label = tkinter.Label(master, text="Hello world!")
label.pack()
master.bind("<KeyPress>", show_key)
master.mainloop()
Задача.Переделайте
программу
так, чтобы
она
выводила
не
только
keysym, но
и
char, keysym_num
и
keycode.Найдите, в
каких
случаях
keysym
различается
у
клавиш
с
одинаковым
keycode.

Label — ещё
один
инструмент
отображения
данных
в
tkinter.Такие
инструменты
принято
называть
виджетами(widgets).Их
можно
комбинировать
в
одном
окне, например
так:

import tkinter


def key_pressed(event):
    label.config(text=event.keysym)
    canvas.create_oval((100, 100), (300, 300), fill='green')


master = tkinter.Tk()
label = tkinter.Label(master, text="Hello world!")
label.pack()
canvas = tkinter.Canvas(master, bg='blue', height=600, width=600)
canvas.pack()
master.bind("<KeyPress>", key_pressed)
master.mainloop()
Задача
на
дом.Найдите
в
интернете
информацию
в
интернете
о
том, как
используются
функции
pack
и
grid
и
поэкспериментируйте
с
ними.

В
этом
уроке
мы
напишем
простую
игру.Для
начала
давайте
научимся
двигать
объекты.Важная
особенность
холста(Canvas)
в
tkinter
заключается
в
том, что
нарисованный
объект
всегда
остается
единым — с
ним
можно
выполнять
разные
операции.

Все
функции
canvas.create_ * возвращают
целое
число — номер
объекта
на
холсте.Зная
это
число, можно, например, двигать
объект:

import tkinter


def key_pressed(event):
    canvas.move(oval, 10, 10)


master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='blue', height=600, width=600)
oval = canvas.create_oval((300, 300), (310, 310), fill='red')
canvas.pack()
master.bind("<KeyPress>", key_pressed)
master.mainloop()

Чтобы
передвинуть
объект, нужно
передать
функции
canvas.move
номер
объекта
и
два
числа: изменение
координаты
x
и
изменение
координаты
y.

Задача.Допишите
следующую
программу
так, чтобы
она «правильно» реагировала
на
нажатия
стрелок.

import tkinter


def key_pressed(event):
    if event.keysym == 'Up':
        canvas.move(oval, 0, -10)
    # Add something here


master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='blue', height=600, width=600)
oval = canvas.create_oval((300, 300), (310, 310), fill='red')
canvas.pack()
master.bind("<KeyPress>", key_pressed)
master.mainloop()
Объекты
можно
не
только
двигать, но
и
произвольно
менять
их
положения
и
свойства:
canvas.coords(object) — узнать
координаты
объекта(для
овала
это
будет
четверка
координат, для
линии — все
координаты, с
которыми
она
создавалась).
canvas.coords(object, new_coordinates) — задать
объекту
новые
координаты.
canvas.itemconfig(object, ...) — задать
любые
свойства
объекта.Например, canvas.itemconfig(object, fill='red') — изменить
цвет
объекта
на
красный.
Например:

import tkinter


def key_pressed(event):
    if event.keysym == 'space':
        canvas.coords(oval, (300, 300, 310, 310))
    if event.keysym == 'Up':
        canvas.move(oval, 0, -10)
    if canvas.coords(oval)[1] < 50:
        canvas.itemconfig(oval, fill='red')

    # Add something here


master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='blue', height=600, width=600)
oval = canvas.create_oval((300, 300), (310, 310), fill='green')
canvas.pack()
master.bind("<KeyPress>", key_pressed)
master.mainloop()

Задача.Исправьте
программу
выше
так, чтобы
кружок
при
возвращении
к
началу
снова
становился
зеленым.

Задача
на
дом.Исправьте
программу
выше
так, чтобы
кружок
становился
красным
при
удалении
от
начальной
точки
на
100
в
любом
направлении.

Задача.Сделайте
так, чтобы
при
выходе
за
правую
границу
холста
кружок
появлялся
слева, а
при
выходе
за
нижнюю
границу — сверху.Напишите
функцию, которая
двигает
объект
таким
образом.


def move_wrap(canvas, obj, move):
    canvas.move(obj, move[0], move[1])
    # тут нужно что-то добавить


Теперь
приступим
к
игре.Игрок
в
ней
ходит
по
сетке
размером
N_X
на
N_Y
с
шагом
step.Ему
нужно
добраться
до
выхода, причём
начальное
положение
игрока
и
выхода
определяется
случайно.

Шаблон
программы
у
нас
уже
есть:

import tkinter
import random


def move_wrap(canvas, obj, move):
    canvas.move(obj, move[0], move[1])
    # Здесь нужно сделать так, чтобы ушедший "за экран" игрок выходил с другой стороны


def check_move():
    if canvas.coords(player) == canvas.coords(exit):
        label.config(text="Победа!")


def key_pressed(event):
    if event.keysym == 'Up':
        move_wrap(canvas, player, (0, -step))
    # Здесь нужно дописать то, что нужно, чтобы все остальные клавиши работали
    check_move()


master = tkinter.Tk()

step = 60
N_X = 10
N_Y = 10
canvas = tkinter.Canvas(master, bg='blue', height=step * N_X, width=step * N_Y)

player_pos = (random.randint(1, N_X - 1) * step, random.randint(1, N_Y - 1) * step)
exit_pos = (random.randint(1, N_X - 1) * step, random.randint(1, N_Y - 1) * step)

player = canvas.create_oval((player_pos[0], player_pos[1]), (player_pos[0] + step, player_pos[1] + step), fill='green')
exit = canvas.create_oval((exit_pos[0], exit_pos[1]), (exit_pos[0] + step, exit_pos[1] + step), fill='yellow')

label = tkinter.Label(master, text="Найди выход")
label.pack()
canvas.pack()
master.bind("<KeyPress>", key_pressed)
master.mainloop()
Пока
есть
одна
проблема: когда
игрок
находит
выход, ничего
не
происходит.Он
может
гулять
и
дальше.Чтобы
исправить
это, можно
связать
с
событием < KeyPress > какую - нибудь
другую
функцию.Пусть
эта
функция
ничего
не
делает.Определим
её
и
добавим
в
функцию
check_move
одну
строчку:


def do_nothing(x):
    return


def check_move():
    if canvas.coords(player) == canvas.coords(exit):
        label.config(text="Победа!")
        master.bind("<KeyPress>", do_nothing)


Обратите
внимание, что
функция
do_nothing
принимает
на
вход
один
аргумент.Функции, которые
используются
в
команде
bind, всегда
получают
на
вход
один
аргумент — описание
события.Если
бы
мы
определили
функцию


def do_nothing(),


то
в
процессе
выполнения
программы
получили
бы
ошибку.

Теперь, попадая
к
выходу, игрок «теряет
управление» и
может
только
закрыть
окно.Наверное, стоит
добавить
кнопку, которая
позволит
ему
начать
сначала.

Кнопка
создается
командой
tkinter.Button(...)

Ей
нужно
передать
окно, в
котором
будет
создаваться
кнопка;
текст, который
будет
написан
на
кнопке
и
функцию, которая
вызывается
при
её
нажатии.Например
так:

restart = tkinter.Button(master, text="Начать заново", command=prepare_and_start)
restart.pack()
Теперь
стоит
перенести
в
отдельную
функцию
код, подготавливающий
игровое
поле:


def prepare_and_start():
    global player, exit
    player_pos = (random.randint(1, N_X - 1) * step, random.randint(1, N_Y - 1) * step)
    exit_pos = (random.randint(1, N_X - 1) * step, random.randint(1, N_Y - 1) * step)
    player = canvas.create_oval((player_pos[0], player_pos[1]), (player_pos[0] + step, player_pos[1] + step),
                                fill='green')
    exit = canvas.create_oval((exit_pos[0], exit_pos[1]), (exit_pos[0] + step, exit_pos[1] + step), fill='yellow')
    label.config(text="Найди выход!")
    master.bind("<KeyPress>", key_pressed)


Обратите
внимание
на
строчку
global
...
Без
неё
компьютер
считал
бы
player
и
exit
локальными
переменными
данной
функции.Если
бы
другие
функции
попытались
к
ним
обратиться, произошла
бы
ошибка.Вообще
говоря, использовать
глобальные
переменные
не
рекомендуется: с
ними
сложнее
следить
за
выполнением
программы.

Однако
в
нашем
случае
без
глобальных
переменных
трудно
обойтись: информацию
об
игроке, выходе, холсте
и
пр.пришлось
бы
передавать
во
все
функции
в
качестве
параметров.Это
неудобно, а
иногда
и
вовсе
невозможно.Например, команда
bind
работает
с
функциями, получающими
ровно
один
аргумент — событие.Поскольку
наша
программа
невелика, мы
решим
эту
проблему
за
счёт
глобальных
переменных.В
реальных(больших)
программах
для
этого
используют
классы, с
которыми
вы
познакомитесь
немного
позже.

Основной
код
нашей
программы
теперь
выглядит
как - то
так:

step = 60  # Размер клетки
N_X = 10
N_Y = 10  # Размер сетки
master = tkinter.Tk()
label = tkinter.Label(master, text="Найди выход")
label.pack()
canvas = tkinter.Canvas(master, bg='blue', height=N_X * step, width=N_Y * step)
canvas.pack()
restart = tkinter.Button(master, text="Начать заново", command=prepare_and_start)
restart.pack()
prepare_and_start()
master.mainloop()
При
попытке
запустить
новую
программу
вы
сразу
столкнетесь
с
новой
проблемой: после
нажатия «Начать
заново» игрок
и
выход
не
исчезают.Нужно
добавить
в
функцию
prepare_and_start
удаление
всех
старых
объектов.К
счастью, это
можно
сделать
одной
командой: canvas.delete("all").Добавьте
ее
в
вашу
программу.

В
нашу
игру
уже
можно
играть, но
игроку
чересчур
легко
живется: он
даже
проиграть
не
может! Давайте
добавим
препятствия: например, огонь, в
который
нельзя
наступать.

Для
этого
придётся
переписать
функцию
prepare_and_start:


def prepare_and_start():
    global player, exit, fires
    player_pos = (random.randint(1, N_X - 1) * step, random.randint(1, N_Y - 1) * step)
    exit_pos = (random.randint(1, N_X - 1) * step, random.randint(1, N_Y) * step)
    player = canvas.create_oval((player_pos[0], player_pos[1]), (player_pos[0] + step, player_pos[1] + step),
                                fill='green')
    exit = canvas.create_oval((exit_pos[0], exit_pos[1]), (exit_pos[0] + step, exit_pos[1] + step), fill='yellow')
    N_FIRES = 6  # Число клеток, заполненных огнем
    fires = []
    for i in range(N_FIRES):
        fire_pos = (random.randint(1, N_X - 1) * step, random.randint(1, N_Y - 1) * step)
        fire = canvas.create_oval((fire_pos[0], fire_pos[1]), (fire_pos[0] + step, fire_pos[1] + step), fill='red')
        fires.append(fire)
    label.config(text="Найди выход!")
    master.bind("<KeyPress>", key_pressed)


И
функцию, проверяющую
результат
хода:


def check_move():
    if canvas.coords(player) == canvas.coords(exit):
        label.config(text="Победа!")
        master.bind("<KeyPress>", lambda x: None)
    for f in fires:
        if canvas.coords(player) == canvas.coords(f):
            label.config(text="Ты проиграл!")
        master.bind("<KeyPress>", lambda x: None)


Игра
уже
почти
как
настоящая.Осталось
два
штриха: улучшить
графику
и
добавить
еще
врагов.Начнем
с
графики.

На
холст(Canvas)
можно
добавить
любую
картинку.Сначала
её
нужно
загрузить
с
помощью
функции
tkinter.PhotoImage, а
затем
создать
на
холсте:

player_pic = tkinter.PhotoImage(file="doctor.png")
player = canvas.create_image((player_pos[0], player_pos[1]), image=player_pic, anchor='nw'
anchor = 'nw'
означает, что
картинка
помещается
в
левый
верхний(буквально — северо - западный, по - английски — north - west) угол
холста.
Можно
добавить
картинки
для
всех
трёх
объектов.

В
основную
часть
кода:

...
master = tkinter.Tk()

player_pic = tkinter.PhotoImage(file="Doctor1.png")
exit_pic = tkinter.PhotoImage(file="tardis.png")
fire_pic = tkinter.PhotoImage(file="fire.png")
enemy_pic = tkinter.PhotoImage(file="dalek.png")


def prepare_and_start():
    global player, exit, fires
    player_pos = (random.randint(1, N_X - 1) * step, random.randint(1, N_Y - 1) * step)
    player = canvas.create_image((player_pos[0], player_pos[1]), image=player_pic, anchor='nw')
    exit_pos = (random.randint(1, N_X - 1) * step, random.randint(1, N_Y - 1) * step)
    exit = canvas.create_image((exit_pos[0], exit_pos[1]), image=exit_pic, anchor='nw')
    N_FIRES = 6  # Число клеток, заполненных огнем
    fires = []
    for i in range(N_FIRES):
        fire_pos = (random.randint(1, N_X - 1) * step, random.randint(1, N_Y - 1) * step)
        fire = canvas.create_image((fire_pos[0], fire_pos[1]), image=fire_pic, anchor='nw')
        fires.append(fire)
    master.bind("<KeyPress>", key_pressed)


def always_right():
    return (step, 0)


def random_move():
    return random.choice([(step, 0), (-step, 0), (0, step), (0, -step)])


def key_pressed(event):
    if event.keysym == 'Up':
        move_wrap(canvas, player, (0, -step))
    # Добавьте другие клавиши
    for enemy in enemies:
        direction = enemy[1]()  # вызвать функцию перемещения у "врага"
        move_wrap(canvas, enemy[0], direction)  # произвести  перемещение.
    check_move()


def check_move():
    if canvas.coords(player) == canvas.coords(exit):
        label.config(text="Победа!")
        master.bind("<KeyPress>", lambda x: None)
    for f in fires:
        if canvas.coords(player) == canvas.coords(f):
            label.config(text="Ты проиграл!")
            master.bind("<KeyPress>", lambda x: None)
    for e in enemies:
        if canvas.coords(player) == canvas.coords(e[0]):
            label.config(text="Ты проиграл!")
            master.bind("<KeyPress>", lambda x: None)


def prepare_and_start():
    global player, exit, fires, enemies
    canvas.delete("all")
    player_pos = (random.randint(1, N_X - 1) * step, random.randint(1, N_Y - 1) * step)
    player = canvas.create_image((player_pos[0], player_pos[1]), image=player_pic, anchor='nw')
    exit_pos = (random.randint(1, N_X - 1) * step, random.randint(1, N_Y - 1) * step)
    exit = canvas.create_image((exit_pos[0], exit_pos[1]), image=exit_pic, anchor='nw')
    N_FIRES = 6  # Число клеток, заполненных огнем
    fires = []
    for i in range(N_FIRES):
        fire_pos = (random.randint(1, N_X - 1) * step, random.randint(1, N_Y - 1) * step)
        fire = canvas.create_image((fire_pos[0], fire_pos[1]), image=fire_pic, anchor='nw')
        fires.append(fire)
        N_ENEMIES = 4  # Число врагов
    enemies = []
    for i in range(N_ENEMIES):
        enemy_pos = (random.randint(1, N_X - 1) * step, random.randint(1, N_Y - 1) * step)
        enemy = canvas.create_image((enemy_pos[0], enemy_pos[1]), image=enemy_pic, anchor='nw')
        enemies.append((enemy, random.choice([always_right, random_move])))
    # Враги -- это пары ("объект на Canvas", "функция, которая вызывается, чтобы сделать ход")
    master.bind("<KeyPress>", key_pressed)
