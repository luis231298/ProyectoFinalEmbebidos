import tkinter as tk
from os.path import exists
from tkinter import PhotoImage, Scrollbar, ttk
from tkinter.constants import DISABLED 
from PIL import ImageTk,Image

class Interfaz(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.light = []
        self.camera = []
        self.doors = []
        self.rooms = ["habitacion1","habitacion2","habitacion3",
                      "pasillo","cocina","garage","comedor","sala",
                      "puerta", "timbre"]
        self.fillWidgetsPanel()

    def fillWidgetsPanel(self):
        panel = ttk.PanedWindow()
        row=0
        col=0
        for room in self.rooms:
            pane = ttk.PanedWindow(panel,width=250)
            if(col==3):
                if(room != "Timbre"):
                    col+=1                
                    pane.grid(row=row,column=col)
                    panel.add(pane)
                    col=0
                    row+=1
            label = ttk.Label(pane,text=room)
            #Para Luces
            Light = ttk.Progressbar(pane)
            Light.step(50)
            #Para cámara
            path = "assets/"+str(room)+".png"
            if(exists(path)):
                my_img = Image.open(path).convert("RGB")
            else:
                my_img = Image.open("assets/NoSignal.png").convert("RGB")
            my_img = my_img.resize((250,180),Image.ANTIALIAS)
            img = ImageTk.PhotoImage(my_img)
            display = ttk.Label(image=img,width=250)
            display.config(background="white")
            label.image = img
            pane.add(label)
            pane.add(display)
            pane.add(Light)
            
            self.camera.append(display)
            self.light.append(Light)
            pane.grid(row=row,column=col)
            col+=1
            
        panel.pack()
  
    def getLights(self,rooms):
        return self.light
    
    def getCams(self,rooms):
        return self.camera
    
    def getDoors(self,rooms):
        return self.doors

root = tk.Tk()
root.title("Smart Home Raspbery Pi")
root.geometry('1070x720')
root.resizable(False,False)
app = Interfaz(master = root)
app.mainloop()

def lights():
    app.getLights
    
def cams():
    app.getCams
    
def doors():
    app.getDoors