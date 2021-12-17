#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ###############################################
#
# smarthome.py
# Controls leds in the GPIO
# Autor: Luis Enrique Méndez Cabrera
# License: MIT
#
# ## ###############################################

from atexit import register
from threading import Thread
from interfaz import Interfaz
from tkinter import mainloop
import RPi.GPIO as GPIO
import tkinter as tk

def exit_handler():
	print('Shutting down board GUI')
	if _async_board_thread:
		_async_board_thread.join()

def _async_board_worker():
	global _async_board_thread
    root = tk.Tk()
    root.title("Smart Home Raspbery Pi")
    root.geometry('1070x720')
    root.resizable(False,False)
    app = Interfaz(master = root)
    app.connect(GPIO._io_pins)
	try:
		mainloop()
	except:
		pass
	_async_board_thread = None

_async_board_thread = Thread(target=_async_board_worker)
register(exit_handler)
_async_board_thread.start()
