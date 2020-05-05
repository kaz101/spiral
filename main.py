#! /usr/bin/env python3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import spiral
from functions import *
import threading

class Spiral(QtWidgets.QMainWindow, spiral.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Spiral, self).__init__(parent)
        self.setupUi(self)
        self.all_interests = {}
        self.all_links = []
        self.interests = []
        self.get_interests()
    #self.webview.setUrl(QtCore.QUrl('https://google.com'))
        self.next_button.clicked.connect(lambda: self.next_page())
        self.interests_list_box.addItem('All Interests')
        self.interests_list_box.setCurrentRow(0)
        self.add_button.clicked.connect(lambda: self.add_interest())
        self.remove_button.clicked.connect(lambda: self.remove_interest())
        self.t1 = threading.Thread(target=lambda: self.background_load())
        self.webpage = webdriver.Chrome()
        self.t1.start()

    def background_load(self):
        threads = []
        for i in self.interests:
            t = threading.Thread(target=lambda: self.load_interest(i))
            t.start()

    def next_page(self):
        interest = self.interests_list_box.currentRow()
        if interest == 0:
            page = load_page(self.all_links)
        else:
            print (self.interests_list_box.currentItem().text())
            page = load_page(self.all_interests[self.interests_list_box.currentItem().text()])
        try:
            print('webpage')
            self.webpage.get(page)

        #    self.webview.setUrl(QtCore.QUrl(page))
        except:
            next_page()



    def add_interest(self):
        if self.add_item_box.text() and self.add_item_box.text() not in self.interests:
            t = threading.Thread(target=lambda: self.load_interest(self.add_item_box.text()))
            t.start()
            self.interests.append(self.add_item_box.text())
            self.save_interests()

    def remove_interest(self):
        try:
            del self.all_interests[self.interests_list_box.currentItem().text()]
        except KeyError:
                return
        self.interests.pop(self.interests_list_box.currentRow()-1)
        self.interests_list_box.takeItem(self.interests_list_box.currentRow())
        self.all_links.clear()
        for key, value in self.all_interests.items():
            self.all_links.extend(value)
        self.save_interests()

    def load_interest(self,interest):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(options=options)
        driver, list = search_google_images(interest,driver)
        self.all_interests[interest] = list
        self.all_links.extend(list)
        self.interests_list_box.addItem(interest)
        self.add_item_box.clear()
        driver.close()

    def save_interests(self):
        save_file = open('interests.txt','w')
        for i in self.interests:
            save_file.write(i)
            save_file.write('\n')
        save_file.close()

    def get_interests(self):
        save_file = open('interests.txt','r')
        self.interests = save_file.readlines()
        for i in range(len(self.interests)):
            self.interests[i] = self.interests[i].rstrip()
        save_file.close()

def main():
    app = QApplication(sys.argv)
    form = Spiral()
    form.show()
    app.exec_()
if __name__ == '__main__':
    main()
