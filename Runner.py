# !/usr/bin/env python3
# ## ###############################################
#
# runner.py
# Starts threads to schedule automation of activities
#
# Autor : Luis Enrique Méndez Cabrera
# Version original: FJSevilla
# License: MIT
#
# ## ###############################################
from datetime import datetime, timedelta
from threading import Thread
from time import sleep

class Runner(Thread):
    """ As seen at: https://es.stackoverflow.com/questions/38195/ejecutar-fragmento-de-c%C3%B3digo-a-una-hora-fecha-determinada-en-un-script-en-ejecuc
    Clase que crea un Runner para procesar las actividades programadas por medio de hilos y realizarlas en el tiempo especificado"""

    def __init__(self, fecha, delay, funcion):
        """ Constructor de un proceso
            fecha, Array con hora y día de la actividad
            delay,
            funcion, funcion a realizar
        """
        super(Runner, self).__init__()
        self._estado = True
        self.hora = fecha['tiempo']
        self.fecha = fecha['fecha']
        self.delay = delay
        self.funcion = funcion

    def stop(self):
        """ Función que detiene el proceso del hilo """
        self._estado = False

    def run(self):
        """ Función que se mantiene latente hasta que el estado sea falso luego de haber realizado la función"""
        aux = datetime.strptime(self.hora, '%H:%M')
        hora = datetime.now()
        hora = hora.replace(hour = aux.hour, minute=aux.minute, second=aux.second, microsecond = 0)
        if hora <= datetime.now():
            hora += timedelta(days=1)

        while self._estado:
            if hora <= datetime.now():
                self.funcion()
                self.stop()
            sleep(self.delay)