import random
from tkinter import *
from tkinter import messagebox
import logging

logging.basicConfig(filename="logfile.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(funcName)s: "
                                                                       "%(lineno)d - %(message)s")

log = logging.getLogger()


def create_random_list(Numbers):  # Рандомизация порядка чисел в списке
    random.shuffle(Numbers)
    return Numbers


Random_n = list  # Список чисел от 1 до n в случайном порядке
Check = False


def btn1click():  # Функция для первой кнопки (создаёт и сохраняет список с числами)
    try:
        global Random_n, Check
        c = int(digit.get())
        if Check:  # Проверка на нажатие  кнопки второй раз
            log.info("Уведомление о перезапуске программы")
            messagebox.showwarning("Упс!", "Похоже вы пытаетесь создать новую кучку бочонков, чтобы это сделать "
                                           "перезапустите программу!")
        if 0 < c < 291:
            Random_n = list(range(1, c + 1))
            create_random_list(Random_n)
            log.info("Создан список со случайным положением чисел от 1 до %s - %s" % (c, Random_n))
            btn2['state'] = 'active'
        else:
            log.error("Число %s не в диапазоне от 1 до 290!" % c)
            messagebox.showerror('Ошибка!', 'Число дожно быть от 1 до 290!')
        Check = True
        return Random_n, Check
    except ValueError:
        log.exception("Ошибка неверного типа данных!")
        messagebox.showerror('Ошибка!', 'Вы ввели не число!')


count = -1


def btn2click():  # Функция для второй кнопки (выводит бочонки)
    try:
        global a, count, Random_n
        count += 1
        if PlusRow() % 29 == 0:
            PlusColumn()
            a = -1
        barrelnum = Label(window, text=Random_n[count])
        barrelnum.grid(column=c, row=PlusRow())
        canvas = Canvas(window, width=50, height=50)
        img1 = PhotoImage(file='bch.png')
        canvas.create_image(0, 0, image=img1, anchor=NW)
        canvas.img1 = img1
        canvas.grid(column=c, row=PlusRow())
        return count
    except IndexError:
        log.info("Бочонки закончились!")
        messagebox.showwarning("Упс!", "Бочонки закончились!")


def btn3click():  # Функция для третьей кнопки (выход из приложения)
    log.info("Был совершен выход из программы")
    window.quit()


a = -1


def PlusRow():  # Увеличить индекс строки
    global a
    a += 1

    return a


c = 0


def PlusColumn():  # Увеличить  индекс  колонки
    global c
    c += 1
    return c


# Создание окна и кнопок на нём
window = Tk()
window.title("Мешок с бочонками")
window.geometry('1600x900')
lbl = Label(window, text="Введите кол-во бочонков")
lbl.place(x=0, y=800)
digit = Entry(window, width=800)
digit.place(x=150, y=800, width=50)
btn1 = Button(window, text='Сгенерировать случайные числа', command=btn1click)
btn1.place(x=220, y=800)
btn2 = Button(window, text='Вытащить бочонок', command=btn2click)
btn2.place(x=432, y=800)
btn2['state'] = 'disabled'
btn3 = Button(window, text='Выход', command=btn3click)
btn3.place(x=1500, y=800)
window.mainloop()
