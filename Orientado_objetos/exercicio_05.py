class Televisao:

    def __init__(self):
        self.volume = 0
        self.canal  = 0

    def Volume(self):
        return self.volume

    def Canal(self):
        return self.canal


class Controle:

    def Aumenta(self,televisao):
        if televisao.volume >= 0 and televisao.volume < 10:
            televisao.volume += 1

    def Diminui(self, televisao):
        if televisao.volume -1 >= 0:
            televisao.volume -= 1

    def Escolhe_canal(self,televisao):
        televisao.canal = (int(input('digite o canal desejado')))

    def Aumenta_canal(self, televisao):
        if televisao.canal + 1 > 999:
            televisao.canal = 0
        else:
            televisao.canal += 1

    def Diminui_canal(self, televisao):
        if televisao.canal - 1 == -1:
            televisao.canal = 1000

        else:
            televisao.canal -= 1

tv = Televisao()
control = Controle()

control.Aumenta(tv)
print(tv.volume)
control.Diminui(tv)
print(tv.volume)

control.Escolhe_canal(tv)
print(tv.canal)
control.Aumenta_canal(tv)
print(tv.canal)
control.Diminui_canal(tv)
print(tv.canal)





