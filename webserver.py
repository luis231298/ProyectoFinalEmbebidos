# !/usr/bin/env python3
# ## ###############################################
#
# webserver.py
# Starts a custom webserver and handles all requests
# 
# Autor : Luis Enrique Méndez Cabrera
# Version original: Mauricio Matamoros
# License: MIT
#
# ## ###############################################
# Future imports (Python 2.7 compatibility)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import sys
import json
import magic

from interfaz import lights,cams,doors
from Interfaz_server import desploy
from http.server import BaseHTTPRequestHandler, HTTPServer
from Runner import *

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

# import time
# Nombre o dirección IP del sistema anfitrión del servidor web
#address = "localhost"
address = "192.168.56.1"
# Puerto en el cual el servidor estará atendiendo solicitudes HTTP
# El default de un servidor web en produción debe ser 80
port = 80

class WebServer(BaseHTTPRequestHandler):
    """Sirve cualquier archivo encontrado en el servidor"""
 
    def _serve_file(self, rel_path):
        if not os.path.isfile(rel_path):
            self.send_error(404)
            return
        self.send_response(200)
        mime = magic.Magic(mime=True)
        self.send_header("Content-type", mime.from_file(rel_path))
        self.end_headers()
        with open(rel_path, 'rb') as file:
            self.wfile.write(file.read())


    """Sirve el archivo de interfaz de usuario"""
    def _serve_ui_file(self):
     
        if not os.path.isfile("_index.html"):
            err = "_index.html not found."
            self.wfile.write(bytes(err, "utf-8"))
            print(err)
            return
        try:
            with open("_index.html", "r") as f:
                content = "\n".join(f.readlines())
        except:
            content = "Error reading index.html"
        self.wfile.write(bytes(content, "utf-8"))

    """ Recibe e interpreta los datos del JSON envíado desde el servidor web
     Puede encontrarse con dos estructuras distintas, para las actividades programadas
      y las interacciones manipuladas de forma manual"""
    def _parse_post(self, json_obj):

        switcher = {
            'vigilancia':cams,
            'luces':lights,
            'puertas':doors
        }
        
        llaves = []
        for key in json_obj.keys():
            llaves.append(key)
        print(json_obj)
        
        if len(llaves)==2:
            r = Runner(json_obj[llaves[1]],1,switcher.get(llaves[0]))
            r.start() 

        else:
            print("Usar interfaz tkinter")
            func = switcher.get(llaves[0])
            dic = json_obj.get('luces')
            app = QApplication(sys.argv)
            GUI = GUI_Main()
            desploy(dic,GUI)
            GUI.show()
            sys.exit(app.exec_())
            
            


    """do_GET controla todas las solicitudes recibidas vía GET, es
    decir, páginas. Por seguridad, no se analizan variables que lleguen
    por esta vía"""
    def do_GET(self):
        # Revisamos si se accede a la raiz.
        # En ese caso se responde con la interfaz por defecto
        if self.path == '/':
            # 200 es el código de respuesta satisfactorio (OK)
            # de una solicitud
            self.send_response(200)
            # La cabecera HTTP siempre debe contener el tipo de datos mime
            # del contenido con el que responde el servidor
            self.send_header("Content-type", "text/html")
            # Fin de cabecera
            self.end_headers()
            # Por simplicidad, se devuelve como respuesta el contenido del
            # archivo html con el código de la página de interfaz de usuario
            self._serve_ui_file()
        # En caso contrario, se verifica que el archivo exista y se sirve
        else:
            self._serve_file(self.path[1:])

    """do_POST controla todas las solicitudes recibidas vía POST, es
    decir, envíos de formulario. Aquí se gestionan los comandos para
    la Raspberry Pi"""
    def do_POST(self):
        # Primero se obtiene la longitud de la cadena de datos recibida
        content_length = int(self.headers.get('Content-Length'))
        # Después se lee toda la cadena de datos
        post_data = self.rfile.read(content_length)
        # Finalmente, se decodifica el objeto JSON y se procesan los datos.
        # Se descartan cadenas de datos mal formados
        try:
            jobj = json.loads(post_data.decode("utf-8"))
            self._parse_post(jobj)
        except:
            print(sys.exc_info())
            print("Datos POST no recnocidos")
      
def main():
    # Inicializa una nueva instancia de HTTPServer con el
    # HTTPRequestHandler definido en este archivo
    webServer = HTTPServer((address, port), WebServer)
    print("Servidor iniciado")
    print ("\tAtendiendo solicitudes en http://{}:{}".format(address, port))

    try:
        # Mantiene al servidor web ejecutándose en segundo plano
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Maneja la interrupción de cierre CTRL+C
        pass
    except:
        print(sys.exc_info())
    # Detiene el servidor web cerrando todas las conexiones
    webServer.server_close()
    # Reporta parada del servidor web en consola
    print("Server stopped.")


# Punto de anclaje de la función main
if __name__ == "__main__":
    main()
