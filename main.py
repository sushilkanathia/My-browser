import sys
#The python sys module provides functions and variables which are used to manipulate different parts of the Python Runtime Environment

from PyQt5.QtCore import *
#PyQt5 is a python module used for working with Application Toolkit.The QtCore module contains the core classes, including the event loop and Qt’s signal and slot mechanism.

from PyQt5.QtWidgets import *
#Using Qt5's library of built-in widgets to build your applications

from PyQt5.QtWebEngineWidgets import *
#is function is used for use search engine in your browser.


class MainWindow(QMainWindow):
#Creating a class as MainWindow.

    def __init__(self):
    # define a function for make a Constructor
        super(MainWindow,self).__init__()
        self.browser = QWebEngineView()

        # Here we use a bing search engine.
        self.browser.setUrl(QUrl("http://bing.com"))
        self.setCentralWidget(self.browser)

        #We can also use the Google engine in our browser.
        # self.browser.setUrl(QUrl('http://google.com'))
        # self.setCentralWidget(self.browser)
        self.showMaximized()
        # This function is used to maximize our browser screen.

         # here we create a navigation keys.
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Add a back button in our browser.
        back_btn = QAction('<',self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)


        # Add a forward button in our browser.
        forward_btn = QAction('>',self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)


        # Add a reload button in our browser.
        reoload_btn = QAction("Reload",self)
        reoload_btn.triggered.connect(self.browser.forward)
        navbar.addAction(reoload_btn)


        # Add a home button in our browser.
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)


        # This self fuction is used for change url in urlbar while we shift to  the other site.
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    # Here we define a function name navigate_home for home button.
    def navigate_home(self):
        self.browser.setUrl(QUrl('http://bing.com'))

    # Here we define a function name navigate_to_url for url bar in our browser.
    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(Qurl(url))

    # Here we declare a function name update_url for name our url according to our url.
    def update_url(self,q):
        self.url_bar.setText(q.toString())

# store a argument in a app variable.
app = QApplication(sys.argv)

# Here we set a Application Name
QApplication.setApplicationName("My Browser")
window = MainWindow()
app.exec()

