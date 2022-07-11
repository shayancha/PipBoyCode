import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Win(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PipBoy'
        self.setWindowTitle(self.title)
        self.setFixedWidth(800)
        self.setFixedHeight(480)

        self.table_widget = StatsTabs(self)
        self.setCentralWidget(self.table_widget)

        self.setStyleSheet("background:#141A15 ; color:#65F68C")


class StatsTabs(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.layout = QGridLayout()

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()

        self.tabs.resize(800, 480)

        # Add tabs
        self.tabs.addTab(self.tab1, "Status")
        self.tabs.addTab(self.tab2, "S.P.E.C.I.A.L.")
        self.tabs.addTab(self.tab3, "Skills")
        self.tabs.addTab(self.tab4, "Perks")
        self.tabs.addTab(self.tab5, "General")

        # Create first tab
        self.setTab1()

        self.setTab2()

        self.setTab3()

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

        self.uni_font = QFont("Monofonto", 14)
        self.setStyleSheet("background:#141A15 ; color:#65F68C")
        self.setStyleSheet(
            "QPushButton{border-color:#65F68C}")
        self.setStyleSheet(
            "QTabWidget{border-color:#65F68C; background:#141A15}")
        self.setStyleSheet("QCheckBox::indicator{}")

        QApplication.setFont(self.uni_font)

    def setTab1(self):
        self.tab1.layout = QVBoxLayout()
        self.label1 = QLabel("")
        self.tab1.layout.addWidget(self.label1)
        self.tab1.setLayout(self.tab1.layout)

    def show_special_desc(self, index):
        self.special_desc.setText(self.lines2[index])

        self.specialpic = QPixmap("specialimgs/" + str(index) + ".png")
        self.specialpiclabel.setPixmap(self.specialpic)

        self.special_desc.setStyleSheet(
            "border:1px solid;border-color:#65F68C;padding-left:3px")

        for i in range(7):
            if self.button_list2[i].isChecked():
                self.button_list2[i].setStyleSheet(
                    "border:1px solid;border-color:#65F68C")
            else:
                self.button_list2[i].setStyleSheet(
                    "")

    def setTab2(self):
        self.tab2.layout = QGridLayout()
        special_list = ["Strength", "Perception", "Endurance",
                        "Charisma", "Intelligence", "Agility", "Luck"]
        self.button_list2 = []

        self.special_desc = QLabel("")
        self.special_desc.setWordWrap(True)
        self.special_desc.setGeometry(0, 0, 480, 240)
        self.special_desc.setFixedWidth(480)
        self.special_desc.setFixedHeight(100)

        self.specialpiclabel = QLabel()
        self.specialpiclabel.setFixedWidth(200)
        self.specialpiclabel.setFixedHeight(200)
        self.specialpiclabel.setScaledContents(True)
        self.specialpiclabel.setAlignment(Qt.AlignCenter)

        tab_label = QLabel("STATS")
        self.tab2.layout.addWidget(tab_label, 0, 0)

        with open("special.txt") as f:
            self.lines2 = f.readlines()

        self.special_group = QButtonGroup(self.tab2)
        self.special_group.setExclusive(True)

        for i, skill in enumerate(special_list):
            button = QPushButton(skill)
            button.setCheckable(True)
            button.toggle()

            button.setFixedHeight(23)

            self.button_list2.append(button)
            self.special_group.addButton(button)
            self.tab2.layout.addWidget(button, i+1, 0)

            button.clicked.connect(
                lambda checked, c=i: self.show_special_desc(int(c)))

        self.tab2.layout.addWidget(self.specialpiclabel, 1, 1, 7, 1)

        self.tab2.layout.addWidget(self.special_desc, 7, 1, 6, 1)

        self.tab2.setLayout(self.tab2.layout)

    def show_skills_desc(self, index):
        self.skill_desc.setText(self.lines3[index])

        self.skillspic = QPixmap("statsimgs/" + str(index) + ".png")
        self.skillspiclabel.setPixmap(self.skillspic)

        self.skill_desc.setStyleSheet(
            "border:1px solid;border-color:#65F68C;padding-left:3px")

        for i in range(13):
            if self.button_list3[i].isChecked():
                self.button_list3[i].setStyleSheet(
                    "border:1px solid;border-color:#65F68C")
            else:
                self.button_list3[i].setStyleSheet(
                    "")

    def setTab3(self):
        self.tab3.layout = QGridLayout()
        skills_list = ["Barter", "Big Guns", "Energy Weapons", "Explosives", "Lockpick", "Medicine",
                       "Melee Weapons", "Repair", "Science", "Small Guns", "Sneak", "Speech", "Unarmed"]
        self.button_list3 = []

        self.skill_desc = QLabel("")
        self.skill_desc.setWordWrap(True)
        self.skill_desc.setGeometry(0, 0, 480, 240)
        self.skill_desc.setFixedWidth(480)
        self.skill_desc.setFixedHeight(100)

        self.skillspiclabel = QLabel()
        self.skillspiclabel.setFixedWidth(200)
        self.skillspiclabel.setFixedHeight(200)
        self.skillspiclabel.setScaledContents(True)
        self.skillspiclabel.setAlignment(Qt.AlignCenter)

        tab_label = QLabel("STATS")
        self.tab3.layout.addWidget(tab_label, 0, 0)

        with open("skills.txt") as f:
            self.lines3 = f.readlines()

        self.skills_group = QButtonGroup(self.tab3)
        self.skills_group.setExclusive(True)

        for i, skill in enumerate(skills_list):
            button = QPushButton(skill)
            button.setCheckable(True)
            button.toggle()

            button.setFixedHeight(23)

            self.button_list3.append(button)
            self.skills_group.addButton(button)
            self.tab3.layout.addWidget(button, i+1, 0)

            button.clicked.connect(
                lambda checked, c=i: self.show_skills_desc(int(c)))

        self.tab3.layout.addWidget(self.skillspiclabel, 1, 1, 7, 1)

        self.tab3.layout.addWidget(self.skill_desc, 7, 1, 6, 1)

        self.tab3.setLayout(self.tab3.layout)


def show_window():
    app = QApplication(sys.argv)
    root = Win()

    root.show()

    sys.exit(app.exec_())


show_window()
