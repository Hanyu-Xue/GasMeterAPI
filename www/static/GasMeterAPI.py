import sys
import os
base_dir = os.path.dirname(os.path.realpath('__file__'))
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import GasTemplatesMatching as GM
import numpy as np
import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web


Main_window = Tk()
Main_window.title('GasMeterAPP')
template_dir = base_dir+'/templates.npy'
var = StringVar()
def sel_img():
    img_sel = Toplevel(Main_window)
    img_sel.withdraw()
    file_path = filedialog.askopenfilename()
    PredictNumber = GM.read_gas_meter(file_path,template_dir)
    B = np.array2string(PredictNumber)
    var.set(B)
#    print(PredictNumber)
    img_window = Toplevel(Main_window)
    img_window.title('Image')
    img = Image.open(file_path)
    #     plt.figure(figsize=(10,8))
    #     plt.imshow(img)
    #     plt.axis('off')
    #     plt.show()
    photo = ImageTk.PhotoImage(img)
    image_label = Label(img_window, image=photo).pack()
    image_label.image=photo
    print(type(photo))



img_path_label = Label(Main_window, text='Input the Gas image').pack()
img_button = Button(Main_window, text='Select', command=sel_img).pack()
predict_label = Label(Main_window, text='The number on the Gas meter are:').pack()
textLabel = Label(Main_window,textvariable=var,justify=LEFT).pack()

Main_window.mainloop()

#This script mainly run the recognition process
#show the results by the command "d1-d8" and "PredictNumber"
#e.g. "print(PredictNumber)"

