## fei.liang ##
import os

import tkinter

from tkinter import messagebox

import qrcode

if __name__=='__main__':

    root = tkinter.Tk()

    root.geometry('550x318+600+200')

    root.title ('QRprintTool')

    ## LB label 控件 （**控件的宽度跟随窗口的宽度）
    LB = tkinter.Label(

        root,
        
        text = 'Please input QR',
        
        bg = 'Snow',
        
        font = ('Arial',18),

        fg = "#00BFFF",

        width = 60, height = 2
        
        )

    LB.pack()

    ## ET entry输入框 （**输入框的宽度跟随窗口的宽度）
    ET = tkinter.Entry(
        
        root,

        width = 56,

        font = ('Arial',20),

        validate = 'all'
        
        )

    ET.pack()

    ## 二维码的生成 (**对输入的QR码长度进行校验)
    def sccode():

        fn = 'code.png'

        qrc = ET.get().strip()

        if len(qrc) == 100 :

            img = qrcode.make(ET.get())

            img.save(fn)

            os.system(fn)

        else:

            tkinter.messagebox.askquestion(message = 'QR 长度校验失败')

    ## BT button 按钮 （**按钮的宽度跟随窗口的宽度）
    BT = tkinter.Button(

        root,

        text = '生成二维码',

        width = 70,height = 1,

        bg = 'Snow',

        font = ('Arial',16),

        fg = "#00BFFF",

        command = sccode
    )

    BT.pack()

    root.mainloop()

