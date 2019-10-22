import matplotlib.pyplot as plt
import numpy as np
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from matplotlib.backends.backend_gtk3agg import (
    FigureCanvasGTK3Agg as FigureCanvas)
from matplotlib.figure import Figure


def generador_armonicas(f):
    w = 2 * np.pi * f

    def calc(n, x, accum=0):
        assert n % 2 != 0
        if n < 1:
            return accum
        else:
            return calc(n - 2, x, 1 / n * np.sin(w * n * x) + accum)

    return calc


def mostrar_plot():
    armonicas = 0
    # fr = int(input("Ingrese frencuencia"))
    # while armonicas % 2 == 0:
    #     armonicas = int(input("Ingrese cantidad de armónicas:"))
    show_fourier(1, 7)

def show_fourier(fr, cant_armo):

    #preparar ventana para mostrar resultado
    win = Gtk.Window()
    win.connect("delete-event", Gtk.main_quit)
    win.set_default_size(800, 600)
    win.set_title("Embedding in GTK")
    f = Figure(figsize=(800 / 96, 800 / 96), dpi=96)
    a = f.add_subplot(111)

    #algoritmo para generar series de fourier
    xs = np.arange(0, 1, 0.001)
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
