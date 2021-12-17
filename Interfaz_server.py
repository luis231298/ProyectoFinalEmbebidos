# !/usr/bin/env python3
# ## ###############################################
#
# Interfaz_server.py
# Generate the necesary functions to modify the GUI with values of an HTML file 
# 
# Autor : Luna Perez José Luis
# Version original of mouseReleaseEvent: Christopher Vivar Vivar in stackoverflow
# License: MIT
#
# ## ###############################################
# Future imports (Python 2.7 compatibility)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

#importacion de librerias necesarias de PyQt5
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

#Creacion de una clase que sera usada para contener la ventana
class GUI_Main(QMainWindow):
    #Instanciacion de la ventana, carga la interfaz desde un archivo .ui
    #e inicializa en 0 nuestros focos
    def __init__(self):
        super().__init__()
        uic.loadUi("gui_app.ui", self)
        self.pgb_garage.setValue(0)
        self.pgb_cocina.setValue(0)
        self.pgb_pasillo.setValue(0)
    
    #Metodos que nos permitiran modificar el valor
    def Cambio_cocina(self,x):
        self.pgb_cocina.setValue(x)
        
    def Cambio_garage(self,x):
        self.pgb_garage.setValue(x)
    
    def Cambio_pasillo(self,x):
        self.pgb_pasillo.setValue(x)
    
    #Metodo que permite cerrar la ventana al dar click en ella
    def mouseReleaseEvent(self, *args, **kwargs):
        for widget in QApplication.topLevelWidgets():
            if type(widget) == GUI_Main:
                widget.close()
#Funcion que recibe un diccionario que trae como llave el cuarto y su valor representa 
#la iluminación que tendra el foco a usar
def deploy(dic,GUI):
    aux=dic.get('cocina')
    GUI.Cambio_cocina(int(aux))
    aux=dic.get('garage')
    GUI.Cambio_garage(int(aux))
    aux=dic.get('pasillo')
    GUI.Cambio_pasillo(int(aux))
