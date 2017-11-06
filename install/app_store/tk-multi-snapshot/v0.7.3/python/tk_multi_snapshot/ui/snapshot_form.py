# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'snapshot_form.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_SnapshotForm(object):
    def setupUi(self, SnapshotForm):
        SnapshotForm.setObjectName("SnapshotForm")
        SnapshotForm.resize(500, 316)
        SnapshotForm.setMinimumSize(QtCore.QSize(500, 0))
        SnapshotForm.setFocusPolicy(QtCore.Qt.TabFocus)
        self.verticalLayout = QtGui.QVBoxLayout(SnapshotForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.page_stack = QtGui.QStackedWidget(SnapshotForm)
        self.page_stack.setObjectName("page_stack")
        self.snapshot_page = QtGui.QWidget()
        self.snapshot_page.setObjectName("snapshot_page")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.snapshot_page)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.header_frame = QtGui.QFrame(self.snapshot_page)
        self.header_frame.setStyleSheet("#header_frame {\n"
"border-style: solid;\n"
"border-radius: 3;\n"
"border-width: 1;\n"
"border-color: rgb(32,32,32);\n"
"}")
        self.header_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.header_frame.setObjectName("header_frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(self.header_frame)
        self.label_2.setMinimumSize(QtCore.QSize(80, 80))
        self.label_2.setMaximumSize(QtCore.QSize(80, 80))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/res/clock.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label = QtGui.QLabel(self.header_frame)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.header_frame)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setVerticalSpacing(4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comment_edit = QtGui.QTextEdit(self.snapshot_page)
        self.comment_edit.setMinimumSize(QtCore.QSize(0, 0))
        self.comment_edit.setMaximumSize(QtCore.QSize(16777215, 120))
        self.comment_edit.setTabChangesFocus(True)
        self.comment_edit.setObjectName("comment_edit")
        self.gridLayout_2.addWidget(self.comment_edit, 1, 0, 1, 1)
        self.thumbnail_frame = QtGui.QFrame(self.snapshot_page)
        self.thumbnail_frame.setMinimumSize(QtCore.QSize(200, 120))
        self.thumbnail_frame.setMaximumSize(QtCore.QSize(200, 120))
        self.thumbnail_frame.setStyleSheet("#thumbnail_frame {\n"
"border-style: solid;\n"
"border-color: rgb(32,32,32);\n"
"border-width: 1px;\n"
"border-radius: 3px;\n"
"background: rgb(117,117,117);\n"
"}")
        self.thumbnail_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.thumbnail_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.thumbnail_frame.setObjectName("thumbnail_frame")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.thumbnail_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.thumbnail_widget = ThumbnailWidget(self.thumbnail_frame)
        self.thumbnail_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.thumbnail_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.thumbnail_widget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.thumbnail_widget.setStyleSheet("")
        self.thumbnail_widget.setObjectName("thumbnail_widget")
        self.horizontalLayout_3.addWidget(self.thumbnail_widget)
        self.gridLayout_2.addWidget(self.thumbnail_frame, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.snapshot_page)
        self.label_3.setIndent(2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.snapshot_page)
        self.label_4.setIndent(2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        spacerItem = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.cancel_btn = QtGui.QPushButton(self.snapshot_page)
        self.cancel_btn.setMinimumSize(QtCore.QSize(90, 0))
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_5.addWidget(self.cancel_btn)
        self.snapshot_btn = QtGui.QPushButton(self.snapshot_page)
        self.snapshot_btn.setMinimumSize(QtCore.QSize(145, 0))
        self.snapshot_btn.setDefault(True)
        self.snapshot_btn.setObjectName("snapshot_btn")
        self.horizontalLayout_5.addWidget(self.snapshot_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.page_stack.addWidget(self.snapshot_page)
        self.status_page = QtGui.QWidget()
        self.status_page.setObjectName("status_page")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.status_page)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem2 = QtGui.QSpacerItem(20, 61, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.status_icon = QtGui.QLabel(self.status_page)
        self.status_icon.setMinimumSize(QtCore.QSize(80, 80))
        self.status_icon.setMaximumSize(QtCore.QSize(80, 80))
        self.status_icon.setText("")
        self.status_icon.setPixmap(QtGui.QPixmap(":/res/success.png"))
        self.status_icon.setScaledContents(True)
        self.status_icon.setObjectName("status_icon")
        self.verticalLayout_4.addWidget(self.status_icon)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.horizontalLayout_8.addLayout(self.verticalLayout_4)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setSpacing(-1)
        self.verticalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.status_title = QtGui.QLabel(self.status_page)
        self.status_title.setStyleSheet("#status_title {\n"
"font-size: 24px;\n"
"}")
        self.status_title.setObjectName("status_title")
        self.verticalLayout_6.addWidget(self.status_title)
        self.status_details = QtGui.QLabel(self.status_page)
        self.status_details.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.status_details.setWordWrap(False)
        self.status_details.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.status_details.setObjectName("status_details")
        self.verticalLayout_6.addWidget(self.status_details)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.history_btn = QtGui.QPushButton(self.status_page)
        self.history_btn.setMinimumSize(QtCore.QSize(195, 0))
        self.history_btn.setObjectName("history_btn")
        self.horizontalLayout_7.addWidget(self.history_btn)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.horizontalLayout_7.setStretch(1, 1)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem6)
        self.horizontalLayout_8.addLayout(self.verticalLayout_6)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        spacerItem8 = QtGui.QSpacerItem(20, 61, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem8)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.close_btn = QtGui.QPushButton(self.status_page)
        self.close_btn.setMinimumSize(QtCore.QSize(80, 0))
        self.close_btn.setDefault(True)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout_6.addWidget(self.close_btn)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.page_stack.addWidget(self.status_page)
        self.verticalLayout.addWidget(self.page_stack)

        self.retranslateUi(SnapshotForm)
        self.page_stack.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(SnapshotForm)
        SnapshotForm.setTabOrder(self.comment_edit, self.cancel_btn)
        SnapshotForm.setTabOrder(self.cancel_btn, self.snapshot_btn)
        SnapshotForm.setTabOrder(self.snapshot_btn, self.close_btn)
        SnapshotForm.setTabOrder(self.close_btn, self.history_btn)

    def retranslateUi(self, SnapshotForm):
        SnapshotForm.setWindowTitle(QtGui.QApplication.translate("SnapshotForm", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SnapshotForm", "A Snapshot creates a quick backup of your current\n"
"scene that you can easily go back to later.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("SnapshotForm", "Type in a Description:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("SnapshotForm", "Take a Screenshot:", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_btn.setText(QtGui.QApplication.translate("SnapshotForm", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.snapshot_btn.setText(QtGui.QApplication.translate("SnapshotForm", "Create Snapshot", None, QtGui.QApplication.UnicodeUTF8))
        self.status_title.setText(QtGui.QApplication.translate("SnapshotForm", "Success!", None, QtGui.QApplication.UnicodeUTF8))
        self.status_details.setText(QtGui.QApplication.translate("SnapshotForm", "Snapshot Successfully Created.", None, QtGui.QApplication.UnicodeUTF8))
        self.history_btn.setText(QtGui.QApplication.translate("SnapshotForm", "View Snapshot History...", None, QtGui.QApplication.UnicodeUTF8))
        self.close_btn.setText(QtGui.QApplication.translate("SnapshotForm", "Close", None, QtGui.QApplication.UnicodeUTF8))

from ..snapshot_form import ThumbnailWidget
from . import resources_rc
from . import resources_rc