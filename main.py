#! /usr/bin/env python3

# Import the nessesary modules
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import spiral
from functions import *
import threading
import time
# Maim Window class
class Spiral(QtWidgets.QMainWindow, spiral.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Spiral, self).__init__(parent)

        # Set up the UI
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowStaysOnTopHint| QtCore.Qt.FramelessWindowHint)
        self.setupUi(self)
        self.setProperty('windowOpacity',0.1)
        self.screen_width = QtWidgets.QDesktopWidget().screenGeometry().width()
        self.move(self.screen_width/2 - self.width()/2, 0)

        # Set up chrome browser
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--incognito')
        self.chrome_options.add_argument('--start-maximized')
        self.webpage = webdriver.Chrome(chrome_options=self.chrome_options)

        # Declare Variables
        self.all_interests = {}
        self.all_links = []
        self.interests = []

        # Get the list of interets from interests.txt file
        self.get_interests()

        # Add 'all interests' to QComboBox at position 0
        self.interests_combo_box.addItem('All Interests')

        # Connect the button events
        self.next_button.clicked.connect(lambda: self.next_page())
        self.add_button.clicked.connect(lambda: self.add_interest())
        self.remove_button.clicked.connect(lambda: self.remove_interest())

        # Start a new thread for loading interests
        self.t1 = threading.Thread(target=lambda: self.background_load())
        self.t1.start()

    # Function to load all interests on start
    def background_load(self):
        threads = []
        for i in self.interests:
            t = threading.Thread(target=lambda: self.load_interest(i))
            t.start()

    # Function to load the next page
    def next_page(self):
        interest = self.interests_combo_box.currentIndex() # Get the chosen interest
        if interest == 0:                                  # index 0 is always 'all interests'
            page = load_page(self.all_links)
        else:
            page = load_page(self.all_interests[self.interests_combo_box.itemText(self.interests_combo_box.currentIndex())])
        try:
            self.webpage.get(page)
        except:
            self.next_page()

    # Function to add a new interest from the add item box
    def add_interest(self):
        if self.add_item_box.text() and self.add_item_box.text() not in self.interests:
            t = threading.Thread(target=lambda: self.load_interest(self.add_item_box.text()))
            t.start()
            self.interests.append(self.add_item_box.text())
            self.save_interests()

    # Function to remove and interest from everywhere
    def remove_interest(self):
        try:
            del self.all_interests[self.interests_combo_box.currentText()]
        except KeyError:
                print('key error')
                return
        self.interests.remove(self.interests_combo_box.currentText())
        self.interests_combo_box.removeItem(self.interests_combo_box.currentIndex())
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
        self.interests_combo_box.addItem(interest)
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

    def eventFilter(self,obj, event):
        if event.type() == QtCore.QEvent.HoverEnter:
            self.setProperty('windowOpacity',1)
            return True

        if event.type() == QtCore.QEvent.HoverLeave:
            self.setProperty('windowOpacity', 0.1)
            return True
        if event.type() == QtCore.QEvent.KeyPress:
            self.add_interest()
            print('key')
            return True


        else:
            return False

def main():
    app = QApplication(sys.argv)
    form = Spiral()
    form.installEventFilter(form)
    form.show()
    app.exec_()
if __name__ == '__main__':
    main()
