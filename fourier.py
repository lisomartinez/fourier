import matplotlib.pyplot as plt
import numpy as np
import gi
import sys
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from matplotlib.backends.backend_gtk3agg import (
    FigureCanvasGTK3Agg as FigureCanvas)
from matplotlib.figure import Figure
sys.setrecursionlimit(15000)


#función para calcular el valor de las y en base al numero de armonicas.
#se llama a la función con la frencuencia como parametro.
#devuelve una funcion calc para calcular el valor de la y.
def generador_armonicas(f):
    w = 2 * np.pi * f

    # n = cantidad de armonicas
    # x = valor de la x del plot
    # accum = acumulado (solo a los fines de la recursividad del algoritmo)
    def calc(n, x, accum=0):
        assert n % 2 != 0

        #caso base: si la cantidad de armonicas es igual a uno, devuelve el acumulado
        if n < 1:
            return accum
        else:
            # calcula recursivamente el valor de la armonica numero n para ese valor de x y los suma al acumulado.
            return calc(n - 2, x, 1 / n * np.sin(w * n * x) + accum)

    return calc


#ingreso de datos
def mostrar_plot():
    armonicas = 0
    fr = 0
    xl = -1
    xu = 0
    while fr <= 0:
        fr = int(input("Ingrese frencuencia (mayor que cero): "))
    while armonicas <= 1:
        armonicas = int(input("Ingrese cantidad de armónicas(1 = 1era armonica, 2 = 3era armonica, etc.): "))
    while xl < 0:
        xl = int(input("Ingrese limite inferior eje x: "))
    while xu <= 0:
        xu = int(input("Ingrese limite superior eje x: "))
    show_fourier(fr, armonicas, xl, xu)


def show_fourier(fr, armonicas, xl, xu):

    #cantidad de armonicas al numero de armonica a calcular
    cant_armo = armonicas + (armonicas - 1)

    #preparar ventana para mostrar resultado
    win = Gtk.Window()
    win.connect("delete-event", Gtk.main_quit)
    win.set_default_size(800, 600)
    win.set_title("Embedding in GTK")
    f = Figure(figsize=(800 / 96, 800 / 96), dpi=96)
    a = f.add_subplot(111)

    #algoritmo para generar series de fourier
    xs = np.arange(xl, xu, 0.001)
    generar = generador_armonicas(fr)
    ys = [generar(cant_armo, x) for x in xs]
    a.plot(xs, ys)

    #mostrar resultados
    sw = Gtk.ScrolledWindow()
    win.add(sw)
    sw.set_border_width(10)
    canvas = FigureCanvas(f)  # a Gtk.DrawingArea
    canvas.set_size_request(800, 600)
    sw.add_with_viewport(canvas)
    win.show_all()
    Gtk.main()


if __name__ == '__main__':
    mostrar_plot()
