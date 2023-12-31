# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_docs.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_new_docs(object):
    def setupUi(self, new_docs):
        new_docs.setObjectName("new_docs")
        new_docs.resize(412, 220)
        new_docs.setStyleSheet("background-color:rgb(255, 250, 250);\n"
"font-family: Arial")
        self.add_docs = QtWidgets.QPushButton(new_docs)
        self.add_docs.setGeometry(QtCore.QRect(100, 190, 191, 16))
        self.add_docs.setStyleSheet("QPushButton {\n"
"color:black;\n"
"background-color:rgba(220, 220, 220, 30);\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius: 7px;\n"
"}")
        self.add_docs.setObjectName("add_docs")
        self.layoutWidget = QtWidgets.QWidget(new_docs)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 10, 361, 166))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.doc_1_lb = QtWidgets.QLabel(self.layoutWidget)
        self.doc_1_lb.setObjectName("doc_1_lb")
        self.verticalLayout.addWidget(self.doc_1_lb)
        self.doc_2_lb = QtWidgets.QLabel(self.layoutWidget)
        self.doc_2_lb.setObjectName("doc_2_lb")
        self.verticalLayout.addWidget(self.doc_2_lb)
        self.doc_3_lb = QtWidgets.QLabel(self.layoutWidget)
        self.doc_3_lb.setObjectName("doc_3_lb")
        self.verticalLayout.addWidget(self.doc_3_lb)
        self.doc_4_lb = QtWidgets.QLabel(self.layoutWidget)
        self.doc_4_lb.setObjectName("doc_4_lb")
        self.verticalLayout.addWidget(self.doc_4_lb)
        self.doc_5_lb = QtWidgets.QLabel(self.layoutWidget)
        self.doc_5_lb.setObjectName("doc_5_lb")
        self.verticalLayout.addWidget(self.doc_5_lb)
        self.all_type_lb = QtWidgets.QLabel(self.layoutWidget)
        self.all_type_lb.setObjectName("all_type_lb")
        self.verticalLayout.addWidget(self.all_type_lb)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.doc_1 = QtWidgets.QComboBox(self.layoutWidget)
        self.doc_1.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.doc_1.setObjectName("doc_1")
        self.doc_1.addItem("")
        self.doc_1.addItem("")
        self.doc_1.addItem("")
        self.doc_1.addItem("")
        self.doc_1.addItem("")
        self.doc_1.addItem("")
        self.verticalLayout_2.addWidget(self.doc_1)
        self.doc_2 = QtWidgets.QComboBox(self.layoutWidget)
        self.doc_2.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.doc_2.setObjectName("doc_2")
        self.doc_2.addItem("")
        self.doc_2.addItem("")
        self.doc_2.addItem("")
        self.doc_2.addItem("")
        self.doc_2.addItem("")
        self.doc_2.addItem("")
        self.verticalLayout_2.addWidget(self.doc_2)
        self.doc_3 = QtWidgets.QComboBox(self.layoutWidget)
        self.doc_3.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.doc_3.setObjectName("doc_3")
        self.doc_3.addItem("")
        self.doc_3.addItem("")
        self.doc_3.addItem("")
        self.doc_3.addItem("")
        self.doc_3.addItem("")
        self.doc_3.addItem("")
        self.verticalLayout_2.addWidget(self.doc_3)
        self.doc_4 = QtWidgets.QComboBox(self.layoutWidget)
        self.doc_4.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.doc_4.setObjectName("doc_4")
        self.doc_4.addItem("")
        self.doc_4.addItem("")
        self.doc_4.addItem("")
        self.doc_4.addItem("")
        self.doc_4.addItem("")
        self.doc_4.addItem("")
        self.verticalLayout_2.addWidget(self.doc_4)
        self.quality_level = QtWidgets.QComboBox(self.layoutWidget)
        self.quality_level.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.quality_level.setObjectName("quality_level")
        self.quality_level.addItem("")
        self.quality_level.addItem("")
        self.quality_level.addItem("")
        self.quality_level.addItem("")
        self.verticalLayout_2.addWidget(self.quality_level)
        self.all_welding_type = QtWidgets.QLineEdit(self.layoutWidget)
        self.all_welding_type.setText("")
        self.all_welding_type.setObjectName("all_welding_type")
        self.verticalLayout_2.addWidget(self.all_welding_type)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_2)

        self.retranslateUi(new_docs)
        QtCore.QMetaObject.connectSlotsByName(new_docs)

    def retranslateUi(self, new_docs):
        _translate = QtCore.QCoreApplication.translate
        new_docs.setWindowTitle(_translate("new_docs", "Dialog"))
        self.add_docs.setText(_translate("new_docs", "Сохранить"))
        self.doc_1_lb.setText(_translate("new_docs", "Документ №1           "))
        self.doc_2_lb.setText(_translate("new_docs", "Документ №2                "))
        self.doc_3_lb.setText(_translate("new_docs", "Документ №3"))
        self.doc_4_lb.setText(_translate("new_docs", "Документ №4"))
        self.doc_5_lb.setText(_translate("new_docs", "Уровень качества:"))
        self.all_type_lb.setText(_translate("new_docs", "Типы сварки:"))
        self.doc_1.setItemText(0, _translate("new_docs", "-"))
        self.doc_1.setItemText(1, _translate("new_docs", "СТО Газпром 2-2.4-083-2006"))
        self.doc_1.setItemText(2, _translate("new_docs", "СТО Газпром 2-2.2-649-2012"))
        self.doc_1.setItemText(3, _translate("new_docs", "СТО Газпром 2-2.2-136-2007"))
        self.doc_1.setItemText(4, _translate("new_docs", "ГОСТ 34347-2017"))
        self.doc_1.setItemText(5, _translate("new_docs", "СП 70.13330.2012"))
        self.doc_2.setItemText(0, _translate("new_docs", "-"))
        self.doc_2.setItemText(1, _translate("new_docs", "СТО Газпром 2-2.4-083-2006"))
        self.doc_2.setItemText(2, _translate("new_docs", "СТО Газпром 2-2.2-649-2012"))
        self.doc_2.setItemText(3, _translate("new_docs", "СТО Газпром 2-2.2-136-2007"))
        self.doc_2.setItemText(4, _translate("new_docs", "ГОСТ 34347-2017"))
        self.doc_2.setItemText(5, _translate("new_docs", "СП 70.13330.2012"))
        self.doc_3.setItemText(0, _translate("new_docs", "-"))
        self.doc_3.setItemText(1, _translate("new_docs", "СТО Газпром 2-2.4-083-2006"))
        self.doc_3.setItemText(2, _translate("new_docs", "СТО Газпром 2-2.2-649-2012"))
        self.doc_3.setItemText(3, _translate("new_docs", "СТО Газпром 2-2.2-136-2007"))
        self.doc_3.setItemText(4, _translate("new_docs", "ГОСТ 34347-2017"))
        self.doc_3.setItemText(5, _translate("new_docs", "СП 70.13330.2012"))
        self.doc_4.setItemText(0, _translate("new_docs", "-"))
        self.doc_4.setItemText(1, _translate("new_docs", "СТО Газпром 2-2.4-083-2006"))
        self.doc_4.setItemText(2, _translate("new_docs", "СТО Газпром 2-2.2-649-2012"))
        self.doc_4.setItemText(3, _translate("new_docs", "СТО Газпром 2-2.2-136-2007"))
        self.doc_4.setItemText(4, _translate("new_docs", "ГОСТ 34347-2017"))
        self.doc_4.setItemText(5, _translate("new_docs", "СП 70.13330.2012"))
        self.quality_level.setItemText(0, _translate("new_docs", "-"))
        self.quality_level.setItemText(1, _translate("new_docs", "A"))
        self.quality_level.setItemText(2, _translate("new_docs", "B"))
        self.quality_level.setItemText(3, _translate("new_docs", "C"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    new_docs = QtWidgets.QDialog()
    ui = Ui_new_docs()
    ui.setupUi(new_docs)
    new_docs.show()
    sys.exit(app.exec_())
