from appJar import gui
import ShipLoad
import Simulator

class Play():
    def __init__(self, app):
        self.app = app

    def __call__(self, *args, **kwargs):
        symulation = Simulator.Simulator()
        apply_result = Apply(self.app).__call__()

        symulation.load_from_list(apply_result[0], apply_result[1])
        app.infoBox("wynik", symulation.sym_result(6))


class Apply():
    def __init__(self, app):
        self.app = app


    def __call__(self, *args, **kwargs):
        lista = []
        for i in ShipLoad.asd:
            lista.append(i[0])

        flota1 = []
        flota2 = []

        for i in lista:
            if self.app.getEntry(i + '1') != '':
                flota1.append((i, int(self.app.getEntry(i + "1"))))
            else:
                flota1.append((i, 0))

            if self.app.getEntry(i+'2') != '':
                flota2.append((i, int(self.app.getEntry(i + "2"))))
            else:
                flota2.append((i, 0))
        return flota1, flota2
wiersz = 0
kolumna1 = 0
kolumna2 = 0
app = gui("Ogame Simulator GUI", "1200x600")

app.startPanedFrame("floty1")
app.addLabel("label1", "Flota 1", wiersz, kolumna1)
app.addLabelEntry("mt1")
app.addLabelEntry("dt1")
app.addLabelEntry("lm1")
app.addLabelEntry("cm1")
app.addLabelEntry("kr1")
app.addLabelEntry("ow1")
app.addLabelEntry("sk1")
app.addLabelEntry("re1")
app.addLabelEntry("ss1")
app.addLabelEntry("b1")
app.addLabelEntry("n1")
app.addLabelEntry("gs1")
app.addLabelEntry("p1")

app.startPanedFrame("floty2")
app.addLabel("label2", "Flota 2", wiersz, kolumna2)
app.addLabelEntry("mt2")
app.addLabelEntry("dt2")
app.addLabelEntry("lm2")
app.addLabelEntry("cm2")
app.addLabelEntry("kr2")
app.addLabelEntry("ow2")
app.addLabelEntry("sk2")
app.addLabelEntry("re2")
app.addLabelEntry("ss2")
app.addLabelEntry("b2")
app.addLabelEntry("n2")
app.addLabelEntry("gs2")
app.addLabelEntry("p2")
app.stopPanedFrame()

# start additional panes inside initial pane
app.startPanedFrame("p2")
app.addLabel("l2", "Akcje")
app.addButton("uruchom symulacje", Play(app))
app.addButton("Exit", app.stop)
app.stopPanedFrame()



# stop initial pane
app.stopPanedFrame()

app.go()
