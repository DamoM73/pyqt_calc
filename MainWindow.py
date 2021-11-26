import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from Ui_MainWindow import Ui_MainWindow


class MainWindow:
    def __init__(self):

        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.signals()

    def signals(self):
        self.ui.clear_btn.clicked.connect(self.clear_btn_clicked)
        self.ui.backspace_btn.clicked.connect(self.backspace_btn_clicked)
        # percent btn
        # divide btn
        self.ui.seven_btn.clicked.connect(lambda: self.number_btn_clicked("7"))
        self.ui.eight_btn.clicked.connect(lambda: self.number_btn_clicked("8"))
        self.ui.nine_btn.clicked.connect(lambda: self.number_btn_clicked("9"))
        # multiply btn
        self.ui.four_btn.clicked.connect(lambda: self.number_btn_clicked("4"))
        self.ui.five_btn.clicked.connect(lambda: self.number_btn_clicked("5"))
        self.ui.six_btn.clicked.connect(lambda: self.number_btn_clicked("6"))
        # minus btn
        self.ui.one_btn.clicked.connect(lambda: self.number_btn_clicked("1"))
        self.ui.two_btn.clicked.connect(lambda: self.number_btn_clicked("2"))
        self.ui.three_btn.clicked.connect(lambda: self.number_btn_clicked("3"))
        # plus btn
        self.ui.zero_btn.clicked.connect(lambda: self.number_btn_clicked("0"))
        self.ui.decimal_btn.clicked.connect(lambda: self.number_btn_clicked("."))
        self.ui.plusminus_btn.clicked.connect(self.plusminus_btn_clicked)
        # equals button

    def show(self):
        self.main_win.show()
        
    # ---- slots ---- #
    def number_btn_clicked(self,val):
        current_val = self.ui.display_lb.text()
        if current_val == "0":
            current_val = ""
        new_val = current_val + val
        self.ui.display_lb.setText(new_val)
        
    def clear_btn_clicked(self):
        self.ui.display_lb.setText("0")
        
    def backspace_btn_clicked(self):
        current_val = self.ui.display_lb.text()
        if len(current_val) == 1:
            new_val = "0"
        else:
            new_val = current_val[:-1]
        self.ui.display_lb.setText(new_val)
        
    def plusminus_btn_clicked(self):
        curr_val = self.ui.display_lb.text()
        if curr_val[0] == "-" and curr_val != "0":
            new_val = curr_val[1:]
        elif curr_val != "0":
            new_val = "-" + curr_val
        else:
            new_val = "0"
        self.ui.display_lb.setText(new_val)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())