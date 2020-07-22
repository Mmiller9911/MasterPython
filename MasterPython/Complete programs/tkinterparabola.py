try:
    import tkinter
except ImportError:                   #python 2
    import Tkinter as tkinter

import math



def parabola(page, size):
        for x in range(size):
            y = x * x /size
            plot(page, x, y)
            plot(page, -x, y)


def circle(page, radius, g, h, colour='orange'):
    page.create_oval(g + radius, h + radius, g - radius, h - radius, outline=colour, width=2)
    # for x in range(g * 100, (g + radius) * 100):
#     #     x /= 100
#     #     print(x)
#     #     y = h + (math.sqrt(radius ** 2 - ((x-g) ** 2)))
#     #     plot(page, x, y)
#     #     plot(page, x, 2 * h - y)
#     #     plot(page, 2 * x, y)



def draw_axes(page):
    page.update()   #call this to make sure we can access the winfo width and height
    x_origin = page.winfo_width() / 2   #winfo is available for any widget (if called like above 1st)
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin)) #get the middle of the page
    page.create_line(-x_origin, 0, x_origin, 0, fill='red')
    page.create_line(0, y_origin, 0, -y_origin, fill='red')
    print(locals())


def plot(page, x, y):
    page.create_line(x, -y, x+1, -y+1, fill='blue')


mainWindow = tkinter.Tk()
mainWindow.title = 'Parabola'
mainWindow.geometry('640x480')
canvas = tkinter.Canvas(width='640', height='480')
canvas.grid(row=0, column=0)

draw_axes(canvas)

parabola(canvas, 50)
parabola(canvas, 10)
circle(canvas, 100, 100, 100, 'red')
circle(canvas, 100, -100, 100)
circle(canvas, 10, 30, 30, 'blue')
circle(canvas, 10, -30, 30, 'yellow')
mainWindow.mainloop()