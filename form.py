# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import time
import glagol
import vedomost

# name_prod = 1  # 1 - глагол
# 2 - ведомость
# 3 - доклад

def start(self, fol: str):  # Создаем папку и в нее копируем скриншоты
    dirs = os.path.join(fol.get())
    if not os.path.isdir(dirs):
        os.makedirs(dirs)
    print(dirs)

class Ui_MainWindow(object):
    def __init__(self):
        self

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(580, 280)
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(10, 40, 561, 31))
        self.lineEdit_name.setAutoFillBackground(False)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_name.setText("Тест")

        self.pushButton_Glagol = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Glagol.setGeometry(QtCore.QRect(10, 120, 181, 31))
        self.pushButton_Glagol.setAutoDefault(True)
        self.pushButton_Glagol.setObjectName("pushButton_Glagol")
        self.pushButton_Glagol.clicked.connect(self.on_click_glag)

        self.pushButton_Vedomost = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Vedomost.setGeometry(QtCore.QRect(200, 120, 181, 31))
        self.pushButton_Vedomost.setAutoDefault(True)
        self.pushButton_Vedomost.setObjectName("pushButton_Vedomost")
        self.pushButton_Vedomost.clicked.connect(self.on_click_ved)

        self.pushButton_Doclad = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Doclad.setGeometry(QtCore.QRect(390, 120, 181, 31))
        self.pushButton_Doclad.setAutoDefault(True)
        self.pushButton_Doclad.setObjectName("pushButton_Doclad")
        self.pushButton_Doclad.clicked.connect(self.on_click_doc)

        self.labe_infol = QtWidgets.QLabel(self.centralwidget)
        self.labe_infol.setGeometry(QtCore.QRect(10, 70, 461, 31))
        self.labe_infol.setObjectName("labe_infol")

        self.labe_infol_2 = QtWidgets.QLabel(self.centralwidget)
        self.labe_infol_2.setGeometry(QtCore.QRect(10, 10, 461, 31))
        self.labe_infol_2.setObjectName("labe_infol_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.labe_infol_3 = QtWidgets.QLabel(self.centralwidget)
        self.labe_infol_3.setGeometry(QtCore.QRect(10, 180, 520, 55))
        self.labe_infol_3.setObjectName("labe_infol_3")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Тестирование Грамоты"))
        self.pushButton_Glagol.setText(_translate("MainWindow", "Тестировать Глагол"))
        self.pushButton_Vedomost.setText(_translate("MainWindow", "Тестировать Ведомость"))
        self.pushButton_Doclad.setText(_translate("MainWindow", "Тестировать Доклад"))
        self.labe_infol.setText(_translate("MainWindow",
                                           "<html><head/><body><p><span style=\" font-size:12pt;\">Папка с результатами будет сохранена в корне проекта</span></p></body></html>"))
        self.labe_infol_2.setText(_translate("MainWindow",
                                             "<html><head/><body>"
                                             "<p><span style=\" font-size:12pt;\">Введите название папки с результатами"
                                             "</span></p></body></html>"))
        self.labe_infol_3.setText(_translate("MainWindow",
                                             "<html><head/><body>"
                                             "<p><span style=\" font-size:16pt;\">Тест начнется через 5 сек. после нажатия кнопки.<br>"
                                             "Во врем теста не трогайте мышью и клавиатуру."
                                             "</span></p></body></html>"))

    # промежуточные функции, чтобы передать - тестирование какого продукта выбрано
    def on_click_glag(self):
        self.on_click(1)
    def on_click_ved(self):
        self.on_click(2)
    def on_click_doc(self):
        self.on_click(3)

    def on_click(self, prod :int): # Тут все тесты

        name = self.lineEdit_name.text()
        dirs = os.path.join(name)
        if not os.path.isdir(dirs):
            os.makedirs(dirs)

# Все тесты Глагола
        if prod == 1:           # перечень всех тестов, как все заработает, вынесу в меню
            print("glagol")
            test_glag = glagol.TestGlagol()

            test_glag.file(dirs)  # меню Файл
            test_glag.maj_clipboard(dirs)  # меню Главная Буфер обмена
            test_glag.maj_font(dirs)  # меню Главная шрифт
            test_glag.maj_font_reg(dirs)  # меню Главная регистр
            test_glag.maj_style(dirs)  # меню Главная стиль
            test_glag.maj_format(dirs)  # меню Главная формат
            test_glag.maj_serch(dirs)  # меню Главная поиск
            test_glag.page_markup_fields(dirs)  # меню Разметка страницы Поля
            test_glag.page_markup_orientation(dirs)  # меню Разметка страницы ориентация
            test_glag.page_markup_size(dirs)  # меню Разметка размер страницы
            test_glag.insert_image(dirs)  # меню Вставка разрыв, изображение
            test_glag.insert_tabe(dirs)  # меню Вставка таблииы
            test_glag.insert_colont(dirs)  # меню Вставка ссылка, колонтитулы, оглавление
            test_glag.reviewing(dirs)  # меню Рецензирование

# Все тесты Ведомости
        if prod == 2:
            print("vedomost")
            test_ved = vedomost.TestVedomost()

            test_ved.file(dirs)
            test_ved.maj_font(dirs)
            test_ved.maj_alignment(dirs)
            test_ved.maj_serch(dirs)
            test_ved.maj_number(dirs)
            test_ved.maj_sort(dirs)
            test_ved.insert_img(dirs)
            test_ved.insert_diogramm(dirs)

# Все тесты Доклада
        if prod == 3:
            print("doclad")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())





