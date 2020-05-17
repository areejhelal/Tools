# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PinConfig.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt,SIGNAL)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.Pin0_groupBox = QGroupBox(Form)
        self.Pin0_groupBox.setObjectName(u"Pin0_groupBox")
        self.Pin0_groupBox.setGeometry(QRect(10, 50, 371, 181))
        self.Mode_groupBox = QGroupBox(self.Pin0_groupBox)
        self.Mode_groupBox.setObjectName(u"Mode_groupBox")
        self.Mode_groupBox.setGeometry(QRect(10, 30, 111, 81))
        self.Mode_groupBox.setCheckable(False)
        self.Output_radioButton = QRadioButton(self.Mode_groupBox)
        self.Output_radioButton.setObjectName(u"Output_radioButton")
        self.Output_radioButton.setEnabled(True)
        self.Output_radioButton.setGeometry(QRect(10, 30, 83, 21))
        self.Input_radioButton = QRadioButton(self.Mode_groupBox)
        self.Input_radioButton.setObjectName(u"Input_radioButton")
        self.Input_radioButton.setEnabled(True)
        self.Input_radioButton.setGeometry(QRect(10, 60, 83, 21))
        self.Input_radioButton.setChecked(True)
        self.OutputConfig_groupBox = QGroupBox(self.Pin0_groupBox)
        self.OutputConfig_groupBox.setObjectName(u"OutputConfig_groupBox")
        self.OutputConfig_groupBox.setEnabled(False)
        self.OutputConfig_groupBox.setGeometry(QRect(140, 40, 221, 31))
        self.High_radioButton = QRadioButton(self.OutputConfig_groupBox)
        self.High_radioButton.setObjectName(u"High_radioButton")
        self.High_radioButton.setGeometry(QRect(10, 10, 83, 18))
        self.Low_radioButton = QRadioButton(self.OutputConfig_groupBox)
        self.Low_radioButton.setObjectName(u"Low_radioButton")
        self.Low_radioButton.setGeometry(QRect(90, 10, 111, 18))
        self.InputConfig_groupBox = QGroupBox(self.Pin0_groupBox)
        self.InputConfig_groupBox.setObjectName(u"InputConfig_groupBox")
        self.InputConfig_groupBox.setGeometry(QRect(140, 80, 221, 31))
        self.PullUp_radioButton = QRadioButton(self.InputConfig_groupBox)
        self.PullUp_radioButton.setObjectName(u"PullUp_radioButton")
        self.PullUp_radioButton.setGeometry(QRect(10, 10, 83, 18))
        self.HighImp_radioButton = QRadioButton(self.InputConfig_groupBox)
        self.HighImp_radioButton.setObjectName(u"HighImp_radioButton")
        self.HighImp_radioButton.setGeometry(QRect(100, 10, 111, 18))
        self.HighImp_radioButton.setChecked(True)
        self.PinName_lineEdit = QLineEdit(self.Pin0_groupBox)
        self.PinName_lineEdit.setObjectName(u"PinName_lineEdit")
        self.PinName_lineEdit.setEnabled(False)
        self.PinName_lineEdit.setGeometry(QRect(20, 130, 113, 20))
        self.DefaultName_checkBox = QCheckBox(self.Pin0_groupBox)
        self.DefaultName_checkBox.setObjectName(u"DefaultName_checkBox")
        self.DefaultName_checkBox.setGeometry(QRect(150, 130, 111, 18))
        self.DefaultName_checkBox.setChecked(True)
        self.OutputPath_lineEdit = QLineEdit(Form)
        self.OutputPath_lineEdit.setObjectName(u"OutputPath_lineEdit")
        self.OutputPath_lineEdit.setGeometry(QRect(30, 240, 221, 20))
        self.Generate_pushButton = QPushButton(Form)
        self.Generate_pushButton.setObjectName(u"Generate_pushButton")
        self.Generate_pushButton.setGeometry(QRect(290, 240, 75, 23))
        self.comboBox = QComboBox(Form)
        self.comboBox.addItems(['Pin 0','Pin 1','Pin 2','Pin 3','Pin 4','Pin 5','Pin 6','Pin 7','Pin 8','Pin 9','Pin 10','Pin 11','Pin 12','Pin 13','Pin 14','Pin 15','Pin 16','Pin 17','Pin 18','Pin 19','Pin 20','Pin 21','Pin 22','Pin 23','Pin 24','Pin 25','Pin 26','Pin 27','Pin 28','Pin 29','Pin 30','Pin 31'])
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(90, 20, 62, 22))
        self.retranslateUi(Form)
        '''
        self.Output_radioButton.clicked.connect(self.OutputConfig_groupBox.setEnabled)
        self.Output_radioButton.clicked.connect(self.InputConfig_groupBox.setDisabled)
        self.Input_radioButton.clicked.connect(self.InputConfig_groupBox.setEnabled)
        self.Input_radioButton.clicked.connect(self.OutputConfig_groupBox.setDisabled)
        self.DefaultName_checkBox.clicked.connect(self.PinName_lineEdit.setDisabled)'''
        QObject.connect(self.DefaultName_checkBox,SIGNAL("clicked(bool)"),self.PinName_lineEdit.setDisabled)
        QObject.connect(self.Input_radioButton,SIGNAL("clicked(bool)"),self.OutputConfig_groupBox.setDisabled)
        QObject.connect(self.Input_radioButton,SIGNAL("clicked(bool)"),self.InputConfig_groupBox.setEnabled)
        QObject.connect(self.Output_radioButton,SIGNAL("clicked(bool)"),self.InputConfig_groupBox.setDisabled)
        QObject.connect(self.Output_radioButton,SIGNAL("clicked(bool)"),self.OutputConfig_groupBox.setEnabled)
        self.Generate_pushButton.clicked.connect(self.GenerateFunction)
        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def GenerateFunction(self):
        MFIC_Handler = open(self.OutputPath_lineEdit.text()+r'\MFIC.h','a+')
        DIO_Handler = open(self.OutputPath_lineEdit.text()+r'\DIO_Config.h','a+')
        
        if self.Output_radioButton.isChecked():
            if self.High_radioButton.isChecked():
                DIO_Handler.write('\n#define DIO_u8'+self.comboBox.currentText()+'_Mode  DIO_u8OUTPUT_HIGH')
            else :
                DIO_Handler.write('\n#define DIO_u8'+self.comboBox.currentText()+'_Mode  DIO_u8OUTPUT_LOW')
        else:
            if self.PullUp_radioButton.isChecked():
                DIO_Handler.write('\n#define DIO_u8'+self.comboBox.currentText()+'_Mode  DIO_u8INPUT_PULLUP')
            else :
                DIO_Handler.write('\n#define DIO_u8'+self.comboBox.currentText()+'_Mode  DIO_u8HIGH_IMPEDANCE')
        if self.DefaultName_checkBox.isChecked():
            MFIC_Handler.write('\n#define DIO_u8'+self.comboBox.currentText()+'_Mode  0')
        else :
            MFIC_Handler.write('\n#define '+ self.PinName_lineEdit.text()+'   0')
        MFIC_Handler.close()
        DIO_Handler.close()
        
    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Pin0_groupBox.setTitle(QCoreApplication.translate("Form", u"Pin Configuration", None))
        self.Mode_groupBox.setTitle(QCoreApplication.translate("Form", u"Mode", None))
        self.Output_radioButton.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_radioButton.setText(QCoreApplication.translate("Form", u"Input", None))
        self.OutputConfig_groupBox.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.High_radioButton.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_radioButton.setText(QCoreApplication.translate("Form", u"Low", None))
        self.InputConfig_groupBox.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PullUp_radioButton.setText(QCoreApplication.translate("Form", u"Pull Up", None))
        self.HighImp_radioButton.setText(QCoreApplication.translate("Form", u"High Impedence", None))
        self.PinName_lineEdit.setText(QCoreApplication.translate("Form", u"Enter Pin Name", None))
        self.DefaultName_checkBox.setText(QCoreApplication.translate("Form", u"Use Default Name", None))
        self.OutputPath_lineEdit.setText(QCoreApplication.translate("Form", u"Enter Output Path", None))
        self.Generate_pushButton.setText(QCoreApplication.translate("Form", u"Generate", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Pin 0", None))

    # retranslateUi

app = QApplication(sys.argv)
widget = QWidget()
Form = Ui_Form()
Form.setupUi(widget)
widget.show()
app.exec_()