# !/usr/bin/env python3
# ## ###############################################
#
# webserver.py
# Starts a custom webserver and handles all requests
# 
# Autor : Luna Perez José Luis
# Version original: Mauricio Matamoros
# License: MIT
#
# ## ###############################################
# Future imports (Python 2.7 compatibility)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class GUI_Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui_app.ui", self)
        self.pgb_garage.setValue(0)
        self.pgb_cocina.setValue(0)
        self.pgb_pasillo.setValue(0)
        
    def Cambio_cocina(self,x):
        self.pgb_cocina.setValue(x)
        
    def Cambio_garage(self,x):
        self.pgb_garage.setValue(x)
    
    def Cambio_pasillo(self,x):
        self.pgb_pasillo.setValue(x)
        
    def mouseReleaseEvent(self, *args, **kwargs):
        for widget in QApplication.topLevelWidgets():
            if type(widget) == GUI_Main:
                widget.close()

def deploy(dic,GUI):
    aux=dic.get('cocina')
    GUI.Cambio_cocina(int(aux))
    aux=dic.get('garage')
    GUI.Cambio_garage(int(aux))
    aux=dic.get('pasillo')
    GUI.Cambio_pasillo(int(aux))
