import wx
from wx.lib import plot


def makeCoords():
    data1 = [156, 141, 165, 135, 169, 131, 176, 130, 187, 134, 191, 140, 191, 146, 186, 150, 179, 155, 175, 157, 168,
             157, 163, 157, 159,
             157, 158, 164, 159, 175, 159, 181, 157, 191, 154, 197, 153, 205, 153, 210, 152, 212, 147, 215, 146, 218,
             143, 220, 132, 220,
             125, 217, 119, 209, 116, 196, 115, 185, 114, 172, 114, 167, 112, 161, 109, 165, 107, 170, 99, 171, 97, 167,
             89, 164, 81, 162,
             77, 155, 81, 148, 87, 140, 96, 138, 105, 141, 110, 136, 111, 126, 113, 129, 118, 117, 128, 114, 137, 115,
             146, 114, 155, 115,
             158, 121, 157, 128, 156, 134, 157, 136, 156, 136]
    f = lambda A, n=2: [A[i:i + n] for i in range(0, len(A), n)]
    coords = f(data1)
    return coords


class MyFrame(wx.Frame):
    def __init__(self):
        self.frame1 = wx.Frame(None, title="wx.lib.plot", id=-1, size=(600, 400))
        self.panel1 = wx.Panel(self.frame1)

        if wx.VERSION[1] < 7:
            plotter = plot.PlotCanvas(self.panel1, size=(600, 400))
        else:
            plotter = plot.PlotCanvas(self.panel1)
            plotter.SetInitialSize(size=(600, 400))
        plotter.SetEnableZoom(True)

        data = makeCoords()
        line = plot.PolyLine(data, colour='red', width=1)
        gc = plot.PlotGraphics([line], '', '', '')
        plotter.Draw(gc, xAxis=(0, 600), yAxis=(0, 400))

        self.frame1.Show(True)


if __name__ == '__main__':
    app = wx.PySimpleApp()
    f = MyFrame()
    app.MainLoop()