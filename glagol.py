import pyautogui
from PIL import Image, ImageChops

import os.path
import numpy as np
import time
import keyboard

class TestGlagol:


    def __init__(self):
        self


    result = {} # Результаты теста

    def __printsrceen(self, name, name_folder) -> None:
        time.sleep(0.2) 								# пауза потому, что виртуальная машина подтормаживает
        name_full = name_folder + name
        screen = pyautogui.screenshot(name_full, region=(385, 100, 1000, 600))

        if not os.path.exists('sample Glagol' + name): 	# проверяем есть ли файл
            dif = 3                             		# Если нет, то результат сравнения например 3
        else:
            screen_sample = Image.open('sample_Glagol' + name)
            dif = ImageChops.difference(screen, screen_sample)
        g = np.mean(np.array(dif))
        print(g)
        if g < 0.3:
            self.result[name] = 'да'
        else:
            self.result[name] = 'нет'

        path = str(name_folder + '\результат_глагол.txt')
        with open(path, 'w') as f:
            for key, val in self.result.items():
                f.write('{}:{}\n'.format(key, val))
        
    def __open_file(self):   				            # открываем тестовый файл перед каждым тестом
        time.sleep(6) 									# пауза чтобы выдернуть мышь, если что не так и в началн
        pyautogui.click(415, 145, button='right', clicks=2, interval=0.3)
        pyautogui.click(440, 210, clicks=2, interval=0.3)
        pyautogui.click(700, 420, clicks=3, interval=0.3)
        pyautogui.click(700, 440, clicks=2, interval=0.3)
        pyautogui.click(1150, 700, clicks=2, interval=0.3)

    def file(self, name_folder):
        scr1 = '\глагол_тест1_1_файл_создать.png'
        scr2 = '\глагол_тест1_2_файл_открыть.png'
        scr3 = '\глагол_тест1_3_файл_сохранить.png'
        scr4 = '\глагол_тест1_4_файл_сохранить_как.png'
        scr5 = '\глагол_тест1_4_файл_свойства_документа.png'
        scr6 = '\глагол_тест1_5_файл_печать.png'
        scr7 = '\глагол_тест1_6_файл_эцп.png'
        scr8 = '\глагол_тест1_7_файл_настройки.png'

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
        pyautogui.click(415, 270, clicks=3, interval=0.3)
        pyautogui.click(1150, 700, clicks=2, interval=0.3)
        pyautogui.click(890, 563, clicks=2, interval=0.3)
        self.__printsrceen(scr4, name_folder)
        pyautogui.click(415, 145, button='right', clicks=2, interval=0.3)  # свойства документа
        pyautogui.click(415, 335, clicks=2, interval=0.3)
        self.__printsrceen(scr5, name_folder)
        pyautogui.click(1120, 645, clicks=2, interval=0.3)
        pyautogui.click(415, 145, button='right', clicks=2, interval=0.3)  # печать
        pyautogui.click(415, 365, clicks=2, interval=0.3)
        pyautogui.click(720, 365, clicks=2, interval=0.3)
        self.__printsrceen(scr6, name_folder)
        pyautogui.click(1500, 115, clicks=2, interval=0.3)
        pyautogui.click(415, 145, button='right', clicks=2, interval=0.3)  # эцп
        pyautogui.click(415, 385, clicks=2, interval=0.3)
        self.__printsrceen(scr7, name_folder)
        pyautogui.click(1240, 700, clicks=2, interval=0.3)
        pyautogui.click(415, 145, button='right', clicks=2, interval=0.3)  # настройки
        pyautogui.click(415, 405, clicks=2, interval=0.3)
        self.__printsrceen(scr8, name_folder)
        pyautogui.click(1265, 700, clicks=2, interval=0.3)

    def maj_clipboard(self, name_folder):
        scr1 = '\глагол_тест2_1_Главная_коп_вст.png'
        scr2 = '\глагол_тест2_2_Главная_выр_вст.png'
        scr3 = '\глагол_тест2-3_Главная_формат_по_образцу.png'
        self.__open_file()

        pyautogui.click(700, 390, clicks=2, interval=0.3)
        pyautogui.mouseDown()
        pyautogui.mouseUp(x=860, y=390)  # выделяем вставляем
        pyautogui.click(420, 180, clicks=2, interval=0.3)
        pyautogui.click(490, 290, clicks=2, interval=0.3)
        pyautogui.click(725, 420, clicks=2, interval=0.3)
        pyautogui.click(420, 180, clicks=2, interval=0.3)
        pyautogui.click(420, 270, clicks=2, interval=0.3)
        self.__printsrceen(scr1, name_folder)
        pyautogui.click(700, 390, clicks=2, interval=0.3)
        pyautogui.mouseDown()
        pyautogui.mouseUp(x=860, y=390)  # выделяем вставляем
        pyautogui.click(420, 180, clicks=2, interval=0.3)
        pyautogui.click(490, 260, clicks=2, interval=0.3)
        pyautogui.click(960, 560, clicks=2, interval=0.3)
        self.__printsrceen(scr2, name_folder)
        pyautogui.click(700, 410, clicks=2, interval=0.3)
        pyautogui.mouseDown()  # нажатие правой кнопки и движение вниз
        pyautogui.mouseUp(x=860, y=410)  # выделяем вырезаем
        pyautogui.click(420, 180, clicks=2, interval=0.3)
        pyautogui.click(490, 230, clicks=2, interval=0.3)
        pyautogui.click(725, 420, clicks=2, interval=0.3)
        pyautogui.click(420, 180, clicks=2, interval=0.3)
        pyautogui.click(420, 270, clicks=2, interval=0.3)
        self.__printsrceen(scr3, name_folder)

    def maj_font(self, name_folder):
        scr1 = '\глагол_тест3_1_Главная_шрифт.png'
        scr2 = '\глагол_тест3-2_Главная_размер_шрифта.png'
        scr3 = '\глагол_тест3_3_Главная_размер_шрифта1.png'
        scr4 = '\глагол_тест3_4_Главная_размер_шрифта2.png'
        scr5 = '\глагол_тест3_5_Главная_очистить_формат.png'
        scr6 = '\глагол_тест3_6_Главная_жирный_шрифт.png'
        scr7 = '\глагол_тест3_7_Главная_наклонный_шрифт.png'
        scr8 = '\глагол_тест3_8_Главная_подчеркивание.png'
        scr9 = '\глагол_тест3_9_Главная_зачеркивание.png'
        scr10 = '\глагол_тест3_10_Главная_заливка.png'
        scr11 = '\глагол_тест3_11_Главная_цвет_шрифта.png'
        scr12 = '\глагол_тест3_12_Главная_верх_инд.png'
        scr13 = '\глагол_тест3_13_Главная_ниж_инд.png'
        self.__open_file()

        pyautogui.click(700, 390, clicks=2, interval=0.3)
        pyautogui.mouseDown()
        pyautogui.mouseUp(x=860, y=390)  # начертание
        pyautogui.click(677, 170, clicks=2, interval=0.3)
        pyautogui.click(677, 210, clicks=2, interval=0.3)
        self.__printsrceen(scr1, name_folder)
        pyautogui.click(730, 170, clicks=2, interval=0.3)
        pyautogui.click(700, 300, clicks=2, interval=0.3)  # высота из колонки
        self.__printsrceen(scr2, name_folder)
        pyautogui.click(750, 170, clicks=6, interval=0.3)  # увеличение А+
        self.__printsrceen(scr3, name_folder)
        pyautogui.click(580, 190, clicks=8, interval=0.3)  # уменьшение А-
        self.__printsrceen(scr4, name_folder)
        pyautogui.click(615, 190, clicks=2, interval=0.3)  # Очистка форматирования
        self.__printsrceen(scr5, name_folder)
        pyautogui.click(640, 190, clicks=2, interval=0.3)  # жирный
        self.__printsrceen(scr6, name_folder)
        pyautogui.click(670, 190, clicks=2, interval=0.3)  # италик
        self.__printsrceen(scr7, name_folder)
        pyautogui.click(695, 190, clicks=2, interval=0.3)
        self.__printsrceen(scr8, name_folder)
        pyautogui.click(590, 220, clicks=2, interval=0.3)  # Зачеркивание
        self.__printsrceen(scr9, name_folder)
        pyautogui.click(615, 220, clicks=2, interval=0.3)  # Заливка
        pyautogui.click(640, 280, clicks=2, interval=0.3)
        self.__printsrceen(scr10, name_folder)
        pyautogui.click(700, 390, clicks=2, interval=0.3)
        pyautogui.mouseDown()
        pyautogui.mouseUp(x=860, y=390)
        pyautogui.click(615, 220, clicks=2, interval=0.3)  # отмена заливки
        pyautogui.click(640, 365, clicks=2, interval=0.3)
        pyautogui.click(660, 220, clicks=2, interval=0.3)  # Цвет шрифта
        pyautogui.click(660, 330, clicks=2, interval=0.3)
        self.__printsrceen(scr11, name_folder)
        pyautogui.click(660, 220, clicks=2, interval=0.3)  # Цвет шрифта отмена
        pyautogui.click(660, 240, clicks=2, interval=0.3)
        pyautogui.click(700, 220, clicks=2, interval=0.3)  # верхний индекс
        self.__printsrceen(scr12, name_folder)
        pyautogui.click(725, 220, clicks=2, interval=0.3)  # верхний индекс
        self.__printsrceen(scr13, name_folder)

    def maj_font_reg(self, name_folder):
        scr1 = '\глагол_тест4_1_Изменение регистра.png'
        self.__open_file()

        pyautogui.click(700, 390, clicks=2, interval=0.3)
        pyautogui.mouseDown()
        pyautogui.mouseUp(x=860, y=390)  # начертание
        pyautogui.click(725, 195, clicks=2, interval=0.3)
        pyautogui.click(725, 215, clicks=2, interval=0.3)
        self.__printsrceen(scr1, name_folder)
        pyautogui.click(970, 555, clicks=2, interval=0.3)

    def maj_format(self, name_folder):
        scr1 = '\глагол_тест5_1_Главная_марк_спис.png'
        scr2 = '\глагол_тест5_2_Главная_нум_спис.png'
        scr3 = '\глагол_тест5_3_Главная_увел_отст.png'
        scr4 = '\глагол_тест5_4_Главная_умен_отст.png'
        scr5 = '\глагол_тест5_5_Главная_формат_по_шир.png'
        scr6 = '\глагол_тест5_6_Главная_формат_прав.png'
        scr7 = '\глагол_тест5_7_Главная_формат_центр.png'
        scr8 = '\глагол_тест5_8_Главная_формат_лев.png'
        scr9 = '\глагол_тест5_9_Главная_межстр_инт.png'
        scr10 = '\глагол_тест5_10_Главная_отобр_знак.png'
        self.__open_file()

        pyautogui.click(700, 390, clicks=2, interval=0.3)
        pyautogui.mouseDown()
        pyautogui.mouseUp(x=860, y=700)
        pyautogui.click(800, 170, clicks=2, interval=0.3)  # маркированный список
        self.__printsrceen(scr1, name_folder)
        pyautogui.click(700, 390, clicks=2, interval=0.3)
        pyautogui.mouseDown()
        pyautogui.mouseUp(x=860, y=700)
        pyautogui.click(825, 170, clicks=2, interval=0.3)  # нумерованный список
        self.__printsrceen(scr2, name_folder)
        pyautogui.click(700, 390, clicks=2, interval=0.3)  # выделяем
        pyautogui.mouseDown()
        pyautogui.mouseUp(x=860, y=700)
        pyautogui.click(855, 170, clicks=2, interval=0.3)  # уменьшить отступ
        self.__printsrceen(scr3, name_folder)
        pyautogui.click(880, 170, clicks=2, interval=0.3)  # величить отступ
        self.__printsrceen(scr4, name_folder)
        pyautogui.click(880, 190, clicks=2, interval=0.3)  # форматирование по ширине
        self.__printsrceen(scr5, name_folder)
        pyautogui.click(850, 190, clicks=2, interval=0.3)  # форматирование по правому краю
        self.__printsrceen(scr6, name_folder)
        pyautogui.click(825, 190, clicks=2, interval=0.3)  # форматирование по центру
        self.__printsrceen(scr7, name_folder)
        pyautogui.click(800, 190, clicks=2, interval=0.3)  # форматирование по левому краю
        self.__printsrceen(scr8, name_folder)
        pyautogui.click(900, 190, clicks=2, interval=0.3)  # межстрочный интервал
        pyautogui.click(900, 300, clicks=2, interval=0.3)  # межстрочный интервал
        self.__printsrceen(scr9, name_folder)
        pyautogui.click(910, 170, clicks=2, interval=0.3)  # отобразить все знаки
        self.__printsrceen(scr10, name_folder)
        pyautogui.click(910, 170, clicks=1, interval=0.3)  # убрать отобразить все знаки

    def maj_style(self, name_folder):
        scr1 = '\глагол_тест6_1_Главная_заголовок.png'
        scr2 = '\глагол_тест6_2_Главная_стиль.png'
        self.__open_file()

        pyautogui.click(700, 390, clicks=2, interval=0.3)  # выделяем
        pyautogui.mouseDown()
        pyautogui.mouseUp(x=860, y=700)
        pyautogui.click(1050, 180, clicks=2, interval=0.3)  # заголовок
        self.__printsrceen(scr1, name_folder)
        pyautogui.click(870, 390, clicks=2, interval=0.3)  # не передает клавиатуру в вм, поэтому копируем в бувер
        pyautogui.mouseDown()
        pyautogui.mouseUp(x=870, y=390)
        pyautogui.click(420, 180, clicks=2, interval=0.3)
        pyautogui.click(490, 290, clicks=2, interval=0.3)  # копируем
        pyautogui.click(1230, 180, clicks=2, interval=0.3)
        pyautogui.click(930, 385, clicks=2, interval=0.3)
        pyautogui.click(930, 385, button='right', interval=0.3)
        pyautogui.click(935, 390, clicks=2, interval=0.3)
        pyautogui.click(1050, 690, clicks=2, interval=0.3)
        pyautogui.click(1175, 185, clicks=2, interval=0.3)  # скролл вниз, чтобы увидеть созданный стиль
        pyautogui.mouseDown()
        pyautogui.mouseUp(x=1175, y=205)
        self.__printsrceen(scr2, name_folder)

    def maj_serch(self, name_folder):
        scr1 = '\глагол_тест7_1_Главная_найти.png'
        scr2 = '\глагол_тест7_2_Главная_заменить.png'
        self.__open_file()

        pyautogui.click(1330, 185, clicks=2, interval=0.3)  # Найти
        pyautogui.click(960, 500, clicks=2, interval=0.3)
        pyautogui.click(960, 500, button='right', clicks=2, interval=0.3)
        pyautogui.click(965, 505, clicks=2, interval=0.3)
        pyautogui.click(1030, 560, clicks=2, interval=0.3)
        self.__printsrceen(scr1, name_folder)
        pyautogui.click(970, 555, clicks=2, interval=0.3) # кликаем на кнопку отменить если ничего не найдено
        pyautogui.click(960, 460, clicks=2, interval=0.3)  # заменить
        pyautogui.click(960, 540, clicks=2, interval=0.3)
        pyautogui.click(960, 540, button='right', clicks=2, interval=0.3)  # вставим текст два раза
        pyautogui.click(965, 545, clicks=2, interval=0.3)
        pyautogui.click(960, 540, button='right', clicks=2, interval=0.3)
        pyautogui.click(965, 545, clicks=2, interval=0.3)
        pyautogui.click(1030, 560, clicks=2, interval=0.3)
        self.__printsrceen(scr2, name_folder)
        pyautogui.click(970, 555, clicks=2, interval=0.3)  # кликаем на кнопку отменить если ничего не найдено
        pyautogui.click(1090, 565, clicks=2, interval=0.3)  # кликаем на кнопку отменить если ничего не найдено

    def page_markup_fields(self, name_folder):
        scr1 = '\глагол_тест8_1_Разм_стр_поля_обычные.png'
        scr2 = '\глагол_тест8_2_Разм_стр_поля_узкие.png'
        scr3 = '\глагол_тест8_3_Разм_стр_поля_средние.png'
        scr4 = '\глагол_тест8_4_Разм_стр_поля_широкие.png'
        self.__open_file()

        pyautogui.click(570, 140, clicks=2, interval=0.3)   # Нажимам меню Разметка страницы
        pyautogui.click(420, 180, clicks=2, interval=0.3)
        pyautogui.click(420, 290, clicks=2, interval=0.3)   # узкие поля
        self.__printsrceen(scr2, name_folder)
        pyautogui.click(570, 140, clicks=2, interval=0.3)   # Нажимам меню Разметка страницы
        pyautogui.click(420, 180, clicks=2, interval=0.3)
        pyautogui.click(420, 360, clicks=2, interval=0.3)   # средние поля
        self.__printsrceen(scr3, name_folder)
        pyautogui.click(570, 140, clicks=2, interval=0.3)   # Нажимам меню Разметка страницы
        pyautogui.click(420, 180, clicks=2, interval=0.3)
        pyautogui.click(420, 390, clicks=2, interval=0.3)   # широкие поля
        self.__printsrceen(scr4, name_folder)
        pyautogui.click(570, 140, clicks=2, interval=0.3)   # Нажимам меню Разметка страницы
        pyautogui.click(420, 180, clicks=2, interval=0.3)
        pyautogui.click(420, 240, clicks=2, interval=0.3)   # обычные поля
        self.__printsrceen(scr1, name_folder)

    def page_markup_orientation(self, name_folder):
        scr1 = '\глагол_тест9_1_Разм_стр_ориент_альб.png'
        scr2 = '\глагол_тест9_2_Разм_стр_ориент_книж.png'
        self.__open_file()

        pyautogui.click(570, 140, clicks=2, interval=0.3)   # Нажимам меню Разметка страницы
        pyautogui.click(480, 180, clicks=2, interval=0.3)
        pyautogui.click(480, 320, clicks=2, interval=0.3)   # ориентация альбомная
        self.__printsrceen(scr1, name_folder)
        pyautogui.click(570, 140, clicks=2, interval=0.3)   # Нажимам меню Разметка страницы
        pyautogui.click(480, 180, clicks=2, interval=0.3)
        pyautogui.click(480, 250, clicks=2, interval=0.3)   # средние поля
        self.__printsrceen(scr2, name_folder)

    def page_markup_size(self, name_folder):
        scr1 = '\глагол_тест10_1_Разм_стр_letter.png'
        scr2 = '\глагол_тест10_2_Разм_стр_tabloid.png'
        scr3 = '\глагол_тест10_2_Разм_стр_statement.png'
        scr4 = '\глагол_тест10_2_Разм_стр_executive.png'
        scr5 = '\глагол_тест10_2_Разм_стр_A0.png'
        scr6 = '\глагол_тест10_2_Разм_стр_A1.png'
        scr7 = '\глагол_тест10_2_Разм_стр_A2.png'
        scr8 = '\глагол_тест10_2_Разм_стр_A3.png'
        scr9 = '\глагол_тест10_2_Разм_стр_A4.png'
        scr10 = '\глагол_тест10_2_Разм_стр_A5.png'
        scr11 = '\глагол_тест10_2_Разм_стр_B4.png'
        scr12 = '\глагол_тест10_2_Разм_стр_B5.png'
        scr13 = '\глагол_тест10_2_Разм_стр_folio.png'
        scr14 = '\глагол_тест10_2_Разм_стр_Quatro.png'
        scr15 = '\глагол_тест10_2_Разм_стр_настр.png'
        self.__open_file()

        pyautogui.click(550, 140, clicks=2, interval=0.3)   # Нажимам меню Разметка страницы
        pyautogui.click(550, 180, clicks=2, interval=0.3)
        pyautogui.click(550, 230, clicks=2, interval=0.3)   # letter
        self.__printsrceen(scr1, name_folder)
        pyautogui.click(550, 140, clicks=2, interval=0.3)   # Нажимам меню Разметка страницы
        pyautogui.click(550, 180, clicks=2, interval=0.3)
        pyautogui.click(550, 280, clicks=2, interval=0.3)   # tabloid
        self.__printsrceen(scr2, name_folder)
        pyautogui.click(550, 140, clicks=2, interval=0.3)   # Нажимам меню Разметка страницы
        pyautogui.click(550, 180, clicks=2, interval=0.3)
        pyautogui.click(550, 330, clicks=2, interval=0.3)   # statment
        self.__printsrceen(scr3, name_folder)
        pyautogui.click(550, 140, clicks=2, interval=0.3)   # Нажимам меню Разметка страницы
        pyautogui.click(550, 180, clicks=2, interval=0.3)
        pyautogui.click(550, 370, clicks=2, interval=0.3)   # executive
        self.__printsrceen(scr4, name_folder)
        pyautogui.click(550, 140, clicks=2, interval=0.3)   # Нажимам меню Разметка страницы
        pyautogui.click(550, 180, clicks=2, interval=0.3)
        pyautogui.click(550, 415, clicks=2, interval=0.3)   # A0
        self.__printsrceen(scr5, name_folder)
        pyautogui.click(550, 140, clicks=2, interval=0.3)   # Нажимам меню Разметка страницы
        pyautogui.click(550, 180, clicks=2, interval=0.3)
        pyautogui.click(550, 465, clicks=2, interval=0.3)   # A1
        self.__printsrceen(scr6, name_folder)
        pyautogui.click(550, 140, clicks=2, interval=0.3)   # Нажимам меню Разметка страницы
        pyautogui.click(550, 180, clicks=2, interval=0.3)
        pyautogui.click(550, 515, clicks=2, interval=0.3)   # A2
        self.__printsrceen(scr7, name_folder)
        pyautogui.click(550, 140, clicks=2, interval=0.3)   # Нажимам меню Разметка страницы
        pyautogui.click(550, 180, clicks=2, interval=0.3)
        pyautogui.click(550, 575, clicks=2, interval=0.3)   # A3
        self.__printsrceen(scr8, name_folder)
        pyautogui.click(550, 140, clicks=2, interval=0.3)   # Нажимам меню Разметка страницы
        pyautogui.click(550, 180, clicks=2, interval=0.3)
        pyautogui.click(550, 620, clicks=2, interval=0.3)   # A4
        self.__printsrceen(scr9, name_folder)
        pyautogui.click(550, 140, clicks=2, interval=0.3)   # Нажимам меню Разметка страницы
        pyautogui.click(550, 180, clicks=2, interval=0.3)
        pyautogui.click(550, 665, clicks=2, interval=0.3)   # A5
        self.__printsrceen(scr10, name_folder)
        pyautogui.click(550, 140, clicks=2, interval=0.3)   # Нажимам меню Разметка страницы
        pyautogui.click(550, 180, clicks=2, interval=0.3)
        pyautogui.click(550, 715, clicks=2, interval=0.3)   # B4
        self.__printsrceen(scr11, name_folder)
        pyautogui.click(550, 140, clicks=2, interval=0.3)   # Нажимам меню Разметка страницы
        pyautogui.click(550, 180, clicks=2, interval=0.3)
        pyautogui.click(550, 765, clicks=2, interval=0.3)   # B5
        self.__printsrceen(scr12, name_folder)
        pyautogui.click(550, 140, clicks=2, interval=0.3)   # Нажимам меню Разметка страницы
        pyautogui.click(550, 180, clicks=2, interval=0.3)
        pyautogui.click(550, 810, clicks=2, interval=0.3)   # Folio
        self.__printsrceen(scr13, name_folder)
        pyautogui.click(550, 140, clicks=2, interval=0.3)   # Нажимам меню Разметка страницы
        pyautogui.click(550, 180, clicks=2, interval=0.3)
        pyautogui.click(550, 860, clicks=2, interval=0.3)   # quatro
        self.__printsrceen(scr14, name_folder)
        pyautogui.click(550, 140, clicks=2, interval=0.3)   # Нажимам меню Разметка страницы
        pyautogui.click(550, 180, clicks=2, interval=0.3)
        pyautogui.click(550, 905, clicks=2, interval=0.3)   # настр
        self.__printsrceen(scr15, name_folder)
        pyautogui.click(1000, 730, clicks=2, interval=0.3) # ok

    def insert_image(self, name_folder):
        scr1 = '\глагол_тест11_1_Вставка_разрыв.png'
        scr2 = '\глагол_тест11_2_Вставка_изобр_bmp.png'
        scr3 = '\глагол_тест11_3_Вставка_изобр_gif.png'
        scr4 = '\глагол_тест11_4_Вставка_изобр_jpg.png'
        scr5 = '\глагол_тест11_5_Вставка_изобр_png.png'
        self.__open_file()

        pyautogui.click(915, 170, clicks=2, interval=0.3) # отбразить все знаки
        pyautogui.click(680, 145, clicks=2, interval=0.3)  # вставка
        pyautogui.click(420, 180, clicks=2, interval=0.3) # разрыв
        self.__printsrceen(scr1, name_folder)
        pyautogui.click(515, 190, clicks=2, interval=0.3) # вставка bmp
        pyautogui.click(700, 420, clicks=3, interval=0.3)
        pyautogui.click(665, 445, clicks=2, interval=0.3)
        pyautogui.click(1150, 700, clicks=2, interval=0.3)
        self.__printsrceen(scr2, name_folder)
        pyautogui.click(515, 190, clicks=2, interval=0.3) # вставка gif
        pyautogui.click(700, 420, clicks=3, interval=0.3)
        pyautogui.click(665, 465, clicks=2, interval=0.3)
        pyautogui.click(1150, 700, clicks=2, interval=0.3)
        self.__printsrceen(scr3, name_folder)
        pyautogui.click(515, 190, clicks=2, interval=0.3) # вставка jpg
        pyautogui.click(700, 420, clicks=3, interval=0.3)
        pyautogui.click(665, 485, clicks=2, interval=0.3)
        pyautogui.click(1150, 700, clicks=2, interval=0.3)
        self.__printsrceen(scr4, name_folder)
        pyautogui.click(515, 190, clicks=2, interval=0.3) # вставка png
        pyautogui.click(700, 420, clicks=3, interval=0.3)
        pyautogui.click(665, 505, clicks=2, interval=0.3)
        pyautogui.click(1150, 700, clicks=2, interval=0.3)
        self.__printsrceen(scr5, name_folder)
        pyautogui.click(1150, 700, clicks=2, interval=0.3) # ткнем на эран, чтобы отобразилось главно меню
        pyautogui.click(915, 170, clicks=1, interval=0.3) # убрать - отбразить все знаки

    def insert_tabe(self, name_folder):
        scr1 = '\глагол_тест12_1_Вставка_таблицы.png'
        scr2 = '\глагол_тест12_2_обьединение по горизонтали.png'
        scr3 = '\глагол_тест12_3_обьединение по вертикали.png'
        scr4 = '\глагол_тест12_4_переворот_текста.png'
        scr5 = '\глагол_тест12_5_Добавить_абзац_до.png'
        scr6 = '\глагол_тест12_6_Добавить_абзац_после.png'
        scr7 = '\глагол_тест12_7_Добавить_колонку.png'
        scr8 = '\глагол_тест12_8_Добавить_строку.png'
        scr9 = '\глагол_тест12_10_Удалить_строку.png'
        scr10 = '\глагол_тест12_10_Удалить_таблицу.png'
        self.__open_file()
        pyautogui.click(680, 140, clicks=2, interval=0.3) # вставка таблицы
        pyautogui.click(560, 170, clicks=2, interval=0.3)
        pyautogui.click(980, 550, clicks=2, interval=0.3)
        self.__printsrceen(scr1, name_folder)
        pyautogui.click(720, 410, clicks=1, interval=0.3) # объединение по горизонтали
        pyautogui.mouseDown()
        pyautogui.moveTo(1000, 410, duration=0.5)
        pyautogui.mouseUp(x=1000, y=410)
        pyautogui.click(750, 140, clicks=2, interval=0.3)
        pyautogui.click(740, 220, clicks=2, interval=0.3)
        self.__printsrceen(scr2, name_folder)
        pyautogui.click(1160, 415, clicks=3, interval=0.3) # объединение по вертикали
        pyautogui.mouseDown()
        pyautogui.moveTo(1160, 435, duration=0.5)
        pyautogui.mouseUp()
        pyautogui.click(750, 140, clicks=2, interval=0.3)
        pyautogui.click(740, 220, clicks=2, interval=0.3)
        self.__printsrceen(scr3, name_folder)
        pyautogui.click(740, 430, clicks=2, interval=0.3)
        keyboard.send('t')
        keyboard.send('e')
        keyboard.send('x')
        keyboard.send('t')
        pyautogui.click(805, 210, interval=0.3) # переворот текста
        self.__printsrceen(scr4, name_folder)
        pyautogui.click(805, 210, interval=0.3) # переворот текста назад
        pyautogui.click(805, 210, interval=0.3)
        pyautogui.click(860, 170, clicks=2, interval=0.3) # добавить абзац до
        self.__printsrceen(scr5, name_folder)
        pyautogui.click(805, 430, clicks=2, interval=0.3)
        pyautogui.click(860, 190, clicks=2, interval=0.3) # добавить абзац после
        self.__printsrceen(scr6, name_folder)
        pyautogui.click(730, 430, clicks=2, interval=0.3)
        pyautogui.click(420, 190, clicks=2, interval=0.3) # добавить колонку
        self.__printsrceen(scr7, name_folder)
        pyautogui.click(480, 190, clicks=2, interval=0.3) # добавить строку
        self.__printsrceen(scr8, name_folder)
        pyautogui.click(560, 190, clicks=2, interval=0.3) # удалить колонку
        self.__printsrceen(scr9, name_folder)
        pyautogui.click(620, 190, clicks=2, interval=0.3) # удалить строку
        self.__printsrceen(scr10, name_folder)
        pyautogui.click(680, 190, clicks=2, interval=0.3) # удалить таблицу

    def insert_colont(self, name_folder):
        scr1 = '\глагол_тест13_1_ссылка.png'
        scr2 = '\глагол_тест13_2_колонт.png'
        scr3 = '\глагол_тест13_3_номер страницы.png'
        scr4 = '\глагол_тест13_4_оглавление.png'
        self.__open_file()

        pyautogui.mouseDown(x=680, y=485)               # вставка ссылки
        pyautogui.moveTo(840, 485, duration=0.5)
        pyautogui.mouseUp()
        pyautogui.click(425, 185, clicks=2, interval=0.3)
        pyautogui.click(515, 280, clicks=2, interval=0.3)
        pyautogui.click(705, 385, clicks=2, interval=0.3)
        pyautogui.click(680, 140, clicks=2, interval=0.3)
        pyautogui.click(610, 190, clicks=2, interval=0.3)
        pyautogui.click(880, 495, clicks=2, interval=0.3)
        keyboard.send('l')
        keyboard.send('i')
        keyboard.send('n')
        keyboard.send('k')
        pyautogui.click(880, 525, clicks=2, interval=0.3)
        pyautogui.click(880, 525, button='right', interval=0.3)
        pyautogui.click(885, 530,  clicks=2, interval=0.3)
        pyautogui.click(1005, 555, clicks=2, interval=0.3)
        self.__printsrceen(scr1, name_folder)
        pyautogui.click(705, 385, clicks=2, interval=0.3)   # Вставка колонтитула
        pyautogui.click(680, 140, clicks=2, interval=0.3)
        pyautogui.click(680, 180, clicks=2, interval=0.3)
        pyautogui.click(410, 170, clicks=2, interval=0.3)
        pyautogui.click(410, 195, clicks=2, interval=0.3)
        pyautogui.click(880, 325, clicks=2, interval=0.3)
        keyboard.send('k')
        keyboard.send('o')
        keyboard.send('l')
        keyboard.send('o')
        keyboard.send('n')
        keyboard.send('t')
        pyautogui.click(760, 185, clicks=2, interval=0.3)
        self.__printsrceen(scr2, name_folder)
        pyautogui.click(705, 385, clicks=2, interval=0.3)   # Вставка номера страницы
        pyautogui.click(680, 140, clicks=2, interval=0.3)
        pyautogui.click(810, 180, clicks=2, interval=0.3)
        pyautogui.click(825, 235, clicks=2, interval=0.3)
        pyautogui.click(1125, 300, clicks=2, interval=0.3)
        pyautogui.click(810, 180, clicks=2, interval=0.3)
        pyautogui.click(860, 280, clicks=2, interval=0.3)
        pyautogui.click(810, 180, clicks=2, interval=0.3)   # удаляем
        pyautogui.click(860, 310, clicks=2, interval=0.3)
        self.__printsrceen(scr3, name_folder)
        pyautogui.click(705, 385, clicks=2, interval=0.3)# оглавление
        pyautogui.click(680, 140, clicks=2, interval=0.3)
        pyautogui.click(880, 180, clicks=2, interval=0.3)
        pyautogui.click(935, 180, clicks=2, interval=0.3)
        self.__printsrceen(scr4, name_folder)

    def reviewing(self, name_folder):
        scr1 = '\глагол_тест14_1_орфография.png'
        self.__open_file()
        pyautogui.click(780, 140, clicks=2, interval=0.3)
        pyautogui.click(770, 180, clicks=2, interval=0.3)
        pyautogui.click(780, 140, clicks=2, interval=0.3)
        pyautogui.click(440, 190, clicks=2, interval=0.3)
        pyautogui.click(1365, 365, clicks=2, interval=0.3)
        pyautogui.click(1450, 365, clicks=2, interval=0.3)
        self.__printsrceen(scr1, name_folder)
