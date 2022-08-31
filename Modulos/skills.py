class Skills():
    def __init__(self, name, element, tipo, power):
        self.name = name
        self.element = element
        self.tipo = tipo
        self.power = power

#MOVIMIENTOS
Llamarada = Skills('Llamarada', 'Fuego', 'Ataque', 250)
Grunido = Skills('Grunido', 'Normal', 'Disminuyente de Ataque', 15)
CaraSusto = Skills('Cara Susto', 'Normal', 'Disminuyente de Defensa', 20)
PatadaDoble = Skills('Patada Doble', 'Lucha', 'Ataque', 300)
ShurikensAgua = Skills('Shurikens de Agua', 'Agua', 'Ataque', 250)
