import pyautogui
from PIL import Image, ImageChops

import os.path
import numpy as np
import time
import keyboard

# Данный класс содержит последовательность проверок Ведомости.
# для его работы надо иметь в корне проекта папку sample_Vedomost

class TestVedomost:


    def __init__(self):
        self


    result = {} # Результаты теста
    # pyautogui.PAUSE = 1  # 2.5


    def __printsrceen(self, name: str, name_folder: str) -> None:
        time.sleep(0.2)
        name_full = name_folder + name
        screen = pyautogui.screenshot(name_full, region=(385, 100, 1000, 600))

        if not os.path.exists('sample_Vedomost' + name): # проверяем есть ли файл
            dif = 3                                     # Если нет, то результат сравнения, например 3
        else:
            screen_sample = Image.open('sample_Vedomost' + name)
            dif = ImageChops.difference(screen, screen_sample)
        g = np.mean(np.array(dif))
        print(g)
        if g < 0.3:
            self.result[name] = 'да'
        else:
            self.result[name] = 'нет'

        path = str(name_folder + '\результат_ведомость.txt')
        with open(path, 'w') as f:
            for key, val in self.result.items():
                f.write('{}:{}\n'.format(key, val))
        time.sleep(0.2)

    def __open_file(self):                                                  # открываем тестовый файл перед каждым тестом
        time.sleep(6)                                                      #  надо сделать предупреждение
        pyautogui.click(415, 145, button='right', clicks=2, interval=0.3)  # открыть файл
        pyautogui.click(440, 210, clicks=2, interval=0.3)
        pyautogui.click(700, 440, clicks=2, interval=0.3)
        pyautogui.click(960, 530, clicks=3, interval=0.3)
        pyautogui.click(1150, 700, clicks=3, interval=0.3)
        pyautogui.click(950, 530, clicks=2, interval=0.3)

    def file(self, name_folder):
        scr1 = '\Ведомость_тест1_1_файл_создать.png'
        scr2 = '\Ведомость_тест1_2_файл_открыть.png'
        scr3 = '\Ведомость_тест1_3_файл_сохранить.png'
        scr4 = '\Ведомость_тест1_4_файл_сохранить_как.png'
        scr6 = '\Ведомость_тест1_5_файл_печать.png'
        scr7 = '\Ведомость_тест1_6_файл_эцп.png'
        scr8 = '\Ведомость_тест1_7_файл_настройки.png'
        pyautogui.click(415, 145, button='right', clicks=2, interval=0.3)  # создать файл
        pyautogui.click(415, 165, clicks=2, interval=0.3)
        pyautogui.click(960, 555, clicks=2, interval=0.3)
        self.__printsrceen(scr1, name_folder)
        self.__open_file()
        self.__printsrceen(scr2, name_folder)
        pyautogui.click(415, 145, button='right', clicks=2, interval=0.3)  # сохранить файл
        pyautogui.click(415, 235, clicks=3, interval=0.3)
        self.__printsrceen(scr3, name_folder)
        pyautogui.click(415, 145, button='right', clicks=2, interval=0.3)  # сохранить файл как
        pyautogui.click(415, 320, clicks=3, interval=0.3)
        pyautogui.click(1150, 700, clicks=2, interval=0.3)
        pyautogui.click(890, 563, clicks=2, interval=0.3)
        self.__printsrceen(scr4, name_folder)
        pyautogui.click(415, 145, button='right', clicks=2, interval=0.3)  # печать
        pyautogui.click(415, 365, clicks=2, interval=0.3)
        self.__printsrceen(scr6, name_folder)
        pyautogui.click(1150, 650, clicks=2, interval=0.3)
        pyautogui.click(415, 145, button='right', clicks=2, interval=0.3)  # эцп
        pyautogui.click(415, 350, clicks=2, interval=0.3)
        self.__printsrceen(scr7, name_folder)
        pyautogui.click(1240, 700, clicks=2, interval=0.3)
        pyautogui.click(415, 145, button='right', clicks=2, interval=0.3)  # закрыть
        pyautogui.click(415, 390, clicks=2, interval=0.3)
        self.__printsrceen(scr8, name_folder)
        pyautogui.click(415, 145, button='right', clicks=2, interval=0.3)  # последние документы
        pyautogui.click(415, 430, clicks=2, interval=0.3)
        pyautogui.click(700, 430, clicks=2, interval=0.3)
        self.__printsrceen(scr8, name_folder)
        time.sleep(6)

    def maj_font(self, name_folder):
        scr1 = '\Ведомость_тест3_1_Главная_шрифт.png'
        scr2 = '\Ведомость_тест3-2_Главная_размер_шрифта.png'
        scr3 = '\Ведомость_тест3_3_Главная_размер_шрифта1.png'
        scr4 = '\Ведомость_тест3_4_Главная_размер_шрифта2.png'
        scr6 = '\Ведомость_тест3_6_Главная_жирный_шрифт.png'
        scr7 = '\Ведомость_тест3_7_Главная_наклонный_шрифт.png'
        scr8 = '\Ведомость_тест3_8_Главная_подчеркивание.png'
        scr9 = '\Ведомость_тест3_9_Главная_граница.png'
        scr10 = '\Ведомость_тест3_10_Главная_заливка.png'
        scr11 = '\Ведомость_тест3_11_Главная_цвет_шрифта.png'
        self.__open_file()

        pyautogui.click(500, 320, clicks=2, interval=0.3) # шрифт
        pyautogui.click(515, 170, clicks=2, interval=0.3)
        pyautogui.click(440, 415, clicks=2, interval=0.3)
        self.__printsrceen(scr1, name_folder)
        pyautogui.click(560, 170, clicks=2, interval=0.3)
        pyautogui.click(535, 305, clicks=2, interval=0.3)  # высота из колонки
        self.__printsrceen(scr2, name_folder)
        pyautogui.click(580, 170, clicks=6, interval=0.3)  # увеличение А+
        self.__printsrceen(scr3, name_folder)
        pyautogui.click(610, 170, clicks=8, interval=0.3)  # уменьшение А-
        self.__printsrceen(scr4, name_folder)
        pyautogui.click(410, 190, clicks=2, interval=0.3)  # жирный
        self.__printsrceen(scr6, name_folder)
        pyautogui.click(435, 190, clicks=2, interval=0.3)  # италик
        self.__printsrceen(scr7, name_folder)
        pyautogui.click(460, 190, clicks=2, interval=0.3) # подчеркнутый
        self.__printsrceen(scr8, name_folder)
        pyautogui.click(670, 365, clicks=2, interval=0.3)  # границы верх
        pyautogui.click(490, 195, clicks=2, interval=0.3)
        pyautogui.click(490, 225, clicks=2, interval=0.3)
        pyautogui.click(670, 430, clicks=2, interval=0.3)
        pyautogui.click(670, 365, clicks=2, interval=0.3)  # границы право
        pyautogui.click(490, 195, clicks=2, interval=0.3)
        pyautogui.click(490, 240, clicks=2, interval=0.3)
        pyautogui.click(670, 430, clicks=2, interval=0.3)
        pyautogui.click(670, 365, clicks=2, interval=0.3)  # границы низ
        pyautogui.click(490, 195, clicks=2, interval=0.3)
        pyautogui.click(490, 270, clicks=2, interval=0.3)
        pyautogui.click(670, 430, clicks=2, interval=0.3)
        pyautogui.click(670, 365, clicks=2, interval=0.3)  # границы лево
        pyautogui.click(490, 195, clicks=2, interval=0.3)
        pyautogui.click(490, 295, clicks=2, interval=0.3)
        pyautogui.click(670, 430, clicks=2, interval=0.3)
        pyautogui.mouseDown(570, 360)                       # границы все границы
        pyautogui.mouseUp(935, 505)
        pyautogui.click(490, 195, clicks=2, interval=0.3)
        pyautogui.click(490, 350, clicks=2, interval=0.3)
        pyautogui.click(490, 195, clicks=2, interval=0.3)   # нет границ
        pyautogui.click(490, 320, clicks=2, interval=0.3)
        pyautogui.click(670, 430, clicks=2, interval=0.3)
        pyautogui.mouseDown(570, 360)                       # внешние границы
        pyautogui.mouseUp(935, 505)
        pyautogui.click(490, 195, clicks=2, interval=0.3)
        pyautogui.click(490, 531, clicks=2, interval=0.3)
        pyautogui.click(670, 430, clicks=2, interval=0.3)
        pyautogui.mouseDown(570, 360)                       # толстые границы
        pyautogui.mouseUp(935, 505)
        pyautogui.click(490, 195, clicks=2, interval=0.3)
        pyautogui.click(490, 531, clicks=2, interval=0.3)
        pyautogui.click(670, 430, clicks=2, interval=0.3)
        self.__printsrceen(scr9, name_folder)
        pyautogui.mouseDown(570, 360)                       # заливка
        pyautogui.mouseUp(935, 505)
        pyautogui.click(535, 195, clicks=2, interval=0.3)
        pyautogui.click(560, 265, clicks=2, interval=0.3)
        pyautogui.mouseDown(725, 365)
        pyautogui.mouseUp(725, 525)
        pyautogui.click(535, 195, clicks=2, interval=0.3)
        pyautogui.click(595, 335, clicks=2, interval=0.3)
        pyautogui.mouseDown(775, 440)
        pyautogui.mouseUp(945, 465)
        pyautogui.click(535, 195, clicks=2, interval=0.3)
        pyautogui.click(630, 390, clicks=2, interval=0.3)
        self.__printsrceen(scr10,name_folder)
        pyautogui.click(740, 430, 2, 0.3)   # Цвет шрифта
        keyboard.send('t')
        keyboard.send('e')
        keyboard.send('x')
        keyboard.send('t')
        pyautogui.click(1000, 430, clicks=2, interval=0.3)
        pyautogui.click(740, 430, clicks=2, interval=0.3)
        pyautogui.click(588, 390, clicks=2, interval=0.3)
        self.__printsrceen(scr11, name_folder)

    def maj_alignment(self, name_folder):
        scr1 = '\Ведомость_тест5_1_Главная_вырав_вверх.png'
        scr2 = '\Ведомость_тест5_2_Главная_вырав_середина.png'
        scr3 = '\Ведомость_тест5_3_Главная_вырав_низ.png'
        scr4 = '\Ведомость_тест5_4_Главная_вырав_лев.png'
        scr5 = '\Ведомость_тест5_5_Главная_вырав_центр.png'
        scr6 = '\Ведомость_тест5_6_Главная_вырав_прав.png'
        scr7 = '\Ведомость_тест5_8_Главная_перенос.png'
        self.__open_file()
        pyautogui.click(885, 660, clicks=2, interval=0.3)
        pyautogui.mouseDown(425, 673)
        pyautogui.mouseUp(425, 773)
        pyautogui.mouseDown(885, 660)
        pyautogui.mouseUp(770, 710)
        pyautogui.click(745, 170, clicks=2, interval=0.3) # объединяем
        pyautogui.click(885, 660, clicks=2, interval=0.3)
        keyboard.send('n')
        keyboard.send('t')
        keyboard.send('r')
        keyboard.send('c')
        keyboard.send('n')
        pyautogui.click(885, 660, clicks=2, interval=0.3)  # чтобы форматировать надо выйти из редактирования ячейки
        pyautogui.click(1000, 660, clicks=2, interval=0.3)
        pyautogui.click(885, 660, clicks=2, interval=0.3)
        pyautogui.click(660, 170, clicks=2, interval=0.3)  # выравнивание верх
        self.__printsrceen(scr1, name_folder)
        pyautogui.click(690, 170, clicks=2, interval=0.3)  # выравнивание центр
        self.__printsrceen(scr2, name_folder)
        pyautogui.click(715, 170, clicks=2, interval=0.3)  # выравнивание низ
        self.__printsrceen(scr3, name_folder)
        pyautogui.click(660, 190, clicks=2, interval=0.3)  # выравнивание по левому краю
        self.__printsrceen(scr4, name_folder)
        pyautogui.click(690, 190, clicks=2, interval=0.3)  # форматирование по центру
        self.__printsrceen(scr5, name_folder)
        pyautogui.click(715, 190, clicks=2, interval=0.3)  # форматирование по правому краю
        self.__printsrceen(scr6, name_folder)
        pyautogui.click(885, 660, clicks=2, interval=0.3)
        keyboard.send('n')
        keyboard.send('t')
        keyboard.send('r')
        keyboard.send('c')
        keyboard.send('n')
        keyboard.send('n')
        keyboard.send('t')
        keyboard.send('r')
        keyboard.send('c')
        keyboard.send('n')
        keyboard.send('n')
        keyboard.send('t')
        keyboard.send('r')
        keyboard.send('c')
        keyboard.send('n')
        keyboard.send('n')
        keyboard.send('t')
        keyboard.send('r')
        keyboard.send('c')
        keyboard.send('n')
        keyboard.send('n')
        keyboard.send('t')
        keyboard.send('r')
        keyboard.send('c')
        keyboard.send('n')
        keyboard.send('n')
        keyboard.send('t')
        keyboard.send('r')
        keyboard.send('c')
        keyboard.send('n')
        keyboard.send('n')
        keyboard.send('t')
        keyboard.send('r')
        keyboard.send('c')
        keyboard.send('n')
        keyboard.send('n')
        keyboard.send('t')
        keyboard.send('r')
        keyboard.send('c')
        keyboard.send('n')
        keyboard.send('n')
        keyboard.send('t')
        keyboard.send('r')
        keyboard.send('c')
        keyboard.send('n')
        keyboard.send('n')
        keyboard.send('t')
        keyboard.send('r')
        keyboard.send('c')
        keyboard.send('n')
        keyboard.send('n')
        keyboard.send('t')
        keyboard.send('r')
        keyboard.send('c')
        keyboard.send('n')
        keyboard.send('n')
        keyboard.send('t')
        keyboard.send('r')
        keyboard.send('c')
        keyboard.send('n')
        pyautogui.click(1000, 660, clicks=2, interval=0.3)
        pyautogui.click(885, 660, clicks=2, interval=0.3)
        pyautogui.click(770, 170, clicks=2, interval=0.3)  # перенос
        self.__printsrceen(scr7, name_folder)

    def maj_serch(self, name_folder):
        scr1 = '\Ведомость_тест6_1_Главная_найти.png'
        scr2 = '\Ведомость_тест6_2_Главная_заменить.png'
        self.__open_file()

        pyautogui.click(840, 190, clicks=2, interval=0.3)  # Найти
        pyautogui.click(960, 505, clicks=2, interval=0.3)
        keyboard.send('n')
        keyboard.send('t')
        keyboard.send('r')
        keyboard.send('c')
        keyboard.send('n')
        pyautogui.click(1030, 560, clicks=2, interval=0.3)
        self.__printsrceen(scr1, name_folder)
        pyautogui.click(970, 535, clicks=2, interval=0.3) # кликаем на кнопку отменить если ничего не найдено
        pyautogui.click(920, 460, clicks=2, interval=0.3)  # заменить
        pyautogui.click(960, 505, clicks=2, interval=0.3)
        pyautogui.click(960, 530, clicks=2, interval=0.3)
        keyboard.send('r')
        keyboard.send('h')
        keyboard.send('b')
        keyboard.send('g')
        keyboard.send('n')
        keyboard.send('j')
        keyboard.send('c')
        keyboard.send('j')
        keyboard.send('a')
        keyboard.send('n')
        pyautogui.click(960, 560, clicks=2, interval=0.3)
        self.__printsrceen(scr2, name_folder)
        pyautogui.click(970, 535, clicks=2, interval=0.3)  # кликаем на кнопку отменить если ничего не найдено
        pyautogui.click(1120, 565, clicks=2, interval=0.3)  # кликаем на кнопку отменить если ничего не найдено

    def maj_number(self, name_folder):
        scr1 = '\Ведомость_тест7_1_типы_данных.png'
        scr2 = '\Ведомость_тест7_2_валюта.png'
        scr3 = '\Ведомость_тест7_3_процент.png'
        scr4 = '\Ведомость_тест7_4_нули.png'
        scr5 = '\Ведомость_тест7_5_знаки_после.png'
        scr6 = '\Ведомость_тест7_2_знаки_убрать.png'
        self.__open_file()

        pyautogui.click(660, 520, clicks=1, interval=0.3)
        pyautogui.mouseDown()
        pyautogui.mouseUp(960, 520)
        pyautogui.click(940, 170, clicks=2, interval=0.3)  # числовой
        pyautogui.click(940, 230, clicks=2, interval=0.3)
        pyautogui.click(940, 170, clicks=2, interval=0.3)  # денежный
        pyautogui.click(940, 270, clicks=2, interval=0.3)
        pyautogui.click(940, 170, clicks=2, interval=0.3)  # финансовый
        pyautogui.click(940, 305, clicks=2, interval=0.3)
        pyautogui.click(940, 170, clicks=2, interval=0.3)  # краткий формат даты
        pyautogui.click(940, 335, clicks=2, interval=0.3)
        pyautogui.click(940, 170, clicks=2, interval=0.3)  # длинный формат даты
        pyautogui.click(940, 370, clicks=2, interval=0.3)
        pyautogui.click(940, 170, clicks=2, interval=0.3)  # время
        pyautogui.click(940, 400, clicks=2, interval=0.3)
        pyautogui.click(940, 170, clicks=2, interval=0.3)  # процентный
        pyautogui.click(940, 440, clicks=2, interval=0.3)
        pyautogui.click(940, 170, clicks=2, interval=0.3)  # дробный
        pyautogui.click(940, 480, clicks=2, interval=0.3)
        pyautogui.click(940, 170, clicks=2, interval=0.3)  # экспоненциальный
        pyautogui.click(940, 510, clicks=2, interval=0.3)
        pyautogui.click(940, 170, clicks=2, interval=0.3)  # текстовый
        pyautogui.click(940, 550, clicks=2, interval=0.3)
        pyautogui.click(940, 170, clicks=2, interval=0.3)  # друге
        pyautogui.click(940, 570, clicks=2, interval=0.3)
        pyautogui.click(700, 340, clicks=2, interval=0.3)
        pyautogui.click(1140, 720, clicks=2, interval=0.3)
        self.__printsrceen(scr1, name_folder)

        pyautogui.click(900, 190, clicks=2, interval=0.3) # Валюта
        pyautogui.click(900, 220, clicks=2, interval=0.3)  # русский
        pyautogui.click(900, 190, clicks=2, interval=0.3)
        pyautogui.click(900, 250, clicks=2, interval=0.3)  # английский
        pyautogui.click(900, 190, clicks=2, interval=0.3)
        pyautogui.click(900, 270, clicks=2, interval=0.3)  # евро
        pyautogui.click(900, 190, clicks=2, interval=0.3)
        pyautogui.click(900, 290, clicks=2, interval=0.3)  # английский 2
        pyautogui.click(900, 190, clicks=2, interval=0.3)
        pyautogui.click(900, 320, clicks=2, interval=0.3)  # другие
        pyautogui.click(1140, 720, clicks=2, interval=0.3)
        pyautogui.click(1140, 720, clicks=2, interval=0.3)
        self.__printsrceen(scr2, name_folder)

    def maj_sort(self, name_folder):
        scr1 = '\Ведомость_тест8_1_сортировка.png'

        self.__open_file()

        pyautogui.click(660, 520, clicks=1, interval=0.3)
        pyautogui.mouseDown()
        pyautogui.mouseUp(960, 520)
        pyautogui.click(1130, 190, clicks=2, interval=0.3)      # по убыванию
        pyautogui.click(1130, 270, clicks=2, interval=0.3)
        pyautogui.click(1130, 190, clicks=2, interval=0.3)     # по возрастанию
        pyautogui.click(1139, 240, clicks=2, interval=0.3)
        time.sleep(0.2)
        self.__printsrceen(scr1, name_folder)

    def insert_img(self, name_folder):
        scr1 = '\Ведомость_тест9_1_изображения.png'
        scr2 = '\Ведомость_тест9_2_ссылка.png'
        scr3 = '\Ведомость_тест9_3_диаграммы.png'
        self.__open_file()

        pyautogui.click(580, 140, clicks=2, interval=0.3)   # png
        pyautogui.click(450, 190, clicks=2, interval=0.3)
        pyautogui.click(700, 440, clicks=2, interval=0.3)
        pyautogui.click(1150, 700, clicks=2, interval=0.3)
        pyautogui.click(650, 650, clicks=2, interval=0.3)
        pyautogui.click(580, 140, clicks=2, interval=0.3)  # jpg
        pyautogui.click(450, 190, clicks=2, interval=0.3)
        pyautogui.click(700, 465, clicks=2, interval=0.3)
        pyautogui.click(1150, 700, clicks=2, interval=0.3)
        self.__printsrceen(scr1, name_folder)

        pyautogui.click(1090, 385, clicks=2, interval=0.3)  # link
        pyautogui.mouseDown(660, 270)
        pyautogui.mouseUp(505, 270)
        pyautogui.click(525, 270, button='right', clicks=2, interval=0.3)
        pyautogui.click(570, 305, clicks=2, interval=0.3)
        pyautogui.click(725, 425, clicks=2, interval=0.3)
        pyautogui.click(580, 140, clicks=2, interval=0.3)
        pyautogui.click(760, 190, clicks=2, interval=0.3)
        pyautogui.click(870, 495, button='right', clicks=2, interval=0.3)
        pyautogui.click(880, 505, clicks=2, interval=0.3)
        pyautogui.click(870, 525, button='right', clicks=2, interval=0.3)
        pyautogui.click(880, 535, clicks=2, interval=0.3)
        pyautogui.click(1010, 550, clicks=2, interval=0.3)
        pyautogui.click(725, 425, clicks=2, interval=0.3)
        pyautogui.click(950, 530, clicks=2, interval=0.3)

    def insert_diogramm(self, name_folder):
        scr1 = '\Ведомость_тест10_1_диограммы.png'
        self.__open_file()

        pyautogui.click(870, 560, clicks=2, interval=0.3)
        pyautogui.click(610, 140, clicks=2, interval=0.3)
        pyautogui.click(610, 190, clicks=2, interval=0.3)
        pyautogui.click(940, 620, button='right', clicks=2, interval=0.3)
        pyautogui.click(1020, 685, clicks=2, interval=0.3)
        pyautogui.click(700, 450, clicks=2, interval=0.3)
        pyautogui.click(810, 615, clicks=2, interval=0.3)
        keyboard.send('2')
        pyautogui.click(1020, 645, clicks=2, interval=0.3)
        pyautogui.click(700, 450, clicks=2, interval=0.3)
        pyautogui.click(810, 615, clicks=2, interval=0.3)
        keyboard.send('4')
        pyautogui.click(1020, 645, clicks=2, interval=0.3)
        pyautogui.click(700, 450, clicks=2, interval=0.3)
        pyautogui.click(810, 615, clicks=2, interval=0.3)
        keyboard.send('9')
        pyautogui.click(1020, 645, clicks=2, interval=0.3)
        pyautogui.click(1200, 726, clicks=2, interval=0.3)
        pyautogui.click(750, 140, clicks=2, interval=0.3) # макет
        pyautogui.click(430, 180, clicks=2, interval=0.3)
        pyautogui.click(430, 260, clicks=2, interval=0.3)

        pyautogui.click(510, 180, clicks=2, interval=0.3) # ось 1
        pyautogui.click(500, 240, clicks=2, interval=0.3)
        pyautogui.click(670, 265, clicks=2, interval=0.3)

        pyautogui.click(510, 180, clicks=2, interval=0.3) # ось 2
        pyautogui.click(500, 260, clicks=2, interval=0.3)
        pyautogui.click(670, 290, clicks=2, interval=0.3)

        pyautogui.click(580, 180, clicks=2, interval=0.3) # легенда
        pyautogui.click(570, 310, clicks=2, interval=0.3)

        pyautogui.click(650, 180, clicks=2, interval=0.3) # подписи
        pyautogui.click(680, 290, clicks=2, interval=0.3)

        pyautogui.click(810, 180, clicks=2, interval=0.3) # сетка

        pyautogui.click(875, 565, button='right', clicks=2, interval=0.3) # тип лин
        pyautogui.click(915, 600, clicks=2, interval=0.3)
        pyautogui.click(880, 415, clicks=2, interval=0.3)
        pyautogui.click(1115, 635, clicks=2, interval=0.3)

        pyautogui.click(875, 565, button='right', clicks=2, interval=0.3) # тип круг
        pyautogui.click(915, 600, clicks=2, interval=0.3)
        pyautogui.click(800, 415, clicks=2, interval=0.3)
        pyautogui.click(1115, 635, clicks=2, interval=0.3)

        pyautogui.click(875, 565, button='right', clicks=2, interval=0.3) # тип гист
        pyautogui.click(915, 600, clicks=2, interval=0.3)
        pyautogui.click(720, 415, clicks=2, interval=0.3)
        pyautogui.click(1115, 635, clicks=2, interval=0.3)
        self.__printsrceen(scr1, name_folder)

    def formula(self, name_folder):
        scr1 = '\Ведомость_тест11_1_формула.png'

        self.__open_file()

        pyautogui.click(915, 170, clicks=2, interval=0.3) # отбразить все знаки
        pyautogui.click(680, 145, clicks=2, interval=0.3)  # вставка
        pyautogui.click(420, 180, clicks=2, interval=0.3) # разрыв
        time.sleep(0.2)
        self.__printsrceen(scr1, name_folder)


