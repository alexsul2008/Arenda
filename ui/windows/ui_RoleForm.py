# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RoleFormNIkdnD.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_RoleForm(object):
    def setupUi(self, RoleForm):
        if not RoleForm.objectName():
            RoleForm.setObjectName(u"RoleForm")
        RoleForm.setWindowModality(Qt.NonModal)
        RoleForm.resize(474, 520)
        self.verticalLayout_3 = QVBoxLayout(RoleForm)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(RoleForm)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 32))
        font = QFont()
        font.setStyleStrategy(QFont.PreferDefault)
        self.groupBox.setFont(font)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 5)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(40, 0))
        self.label.setMaximumSize(QSize(40, 16777215))
        self.label.setStyleSheet(u"padding-left: 5px;")

        self.horizontalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(70, 0))
        self.label_2.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(130, 0))
        self.label_3.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_2.addWidget(self.label_3)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(126, 0))
        self.label_7.setMaximumSize(QSize(126, 16777215))
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_7)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.scrollArea = QScrollArea(RoleForm)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 452, 414))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.add_widget_layout_role = QVBoxLayout()
        self.add_widget_layout_role.setSpacing(0)
        self.add_widget_layout_role.setObjectName(u"add_widget_layout_role")
        self.add_widget_layout_role.setSizeConstraint(QLayout.SetNoConstraint)
        self.add_widget_layout_role.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addLayout(self.add_widget_layout_role)

        self.verticalSpacer = QSpacerItem(20, 385, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.btn_add_role = QPushButton(RoleForm)
        self.btn_add_role.setObjectName(u"btn_add_role")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_add_role.sizePolicy().hasHeightForWidth())
        self.btn_add_role.setSizePolicy(sizePolicy1)
        self.btn_add_role.setMinimumSize(QSize(0, 40))

        self.verticalLayout_3.addWidget(self.btn_add_role)


        self.retranslateUi(RoleForm)

        QMetaObject.connectSlotsByName(RoleForm)
    # setupUi

    def retranslateUi(self, RoleForm):
        RoleForm.setWindowTitle(QCoreApplication.translate("RoleForm", u"\u0424\u043e\u0440\u043c\u0430 \u0440\u0430\u0431\u043e\u0442\u044b \u0441 \u043f\u0440\u0430\u0432\u0430\u043c\u0438 \u0434\u043e\u0441\u0442\u0443\u043f\u0430", None))
        self.label.setText(QCoreApplication.translate("RoleForm", u"ID", None))
        self.label_2.setText(QCoreApplication.translate("RoleForm", u"\u0420\u043e\u043b\u044c \u0434\u043e\u0441\u0442\u0443\u043f\u0430", None))
        self.label_3.setText(QCoreApplication.translate("RoleForm", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0434\u043e\u0441\u0442\u0443\u043f\u0430", None))
        self.label_7.setText(QCoreApplication.translate("RoleForm", u"\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u0435", None))
        self.btn_add_role.setText(QCoreApplication.translate("RoleForm", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u0440\u0430\u0432\u0430", None))
    # retranslateUi

