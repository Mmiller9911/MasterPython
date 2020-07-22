try:
    import tkinter
except ImportError:                   #python 2
    import Tkinter as tkinter

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)

# tkinter._test()

mainWindow = tkinter.Tk()
mainWindow.title('hello world')
mainWindow.geometry('640x480+80+400')

label = tkinter.Label(mainWindow, text='hello world')
label.pack(side='top')

leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side='left',anchor='n',fill=tkinter.Y, expand='False')

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth='1')
canvas.pack(side='left',anchor='n')

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='right',anchor='n',fill=tkinter.Y, expand='True')

button1 = tkinter.Button(rightFrame, text='button1')
button2 = tkinter.Button(rightFrame, text='button2')
button3 = tkinter.Button(rightFrame, text='button3')
button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')
#canvas.pack(side='top', fill=tkinter.BOTH, expand='True')


mainWindow.mainloop()


#  ============================================================================================
# GRIDS
# unless the columns have weights they will not be positioned correctly
# it is a lot easier to create the apps if you draw the layout out first

# Here is the list of possible options −
#
# column − The column to put widget in; default 0 (leftmost column).
#
# columnspan − How many columns widgetoccupies; default 1.
#
# ipadx, ipady − How many pixels to pad widget, horizontally and vertically, inside widget's borders.
#
# padx, pady − How many pixels to pad widget, horizontally and vertically, outside v's borders.
#
# row − The row to put widget in; default the first row that is still empty.
#
# rowspan − How many rowswidget occupies; default 1.
#
# sticky − What to do if the cell is larger than widget. By default,
# with sticky='', widget is centered in its cell. sticky may be the string concatenation of zero or more of N, E, S, W, NE, NW, SE,
# and SW, compass directions indicating the sides and corners of the cell to which widget sticks.

#  ============================================================================================