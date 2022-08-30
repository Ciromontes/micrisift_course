#!/usr/bin/env python3
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntaje = 0
        self.eligio = ""
    def elegir(self):
        self.eligio = input("{nombre}, seleccione piedra, papel o tijera: ".format(nombre= self.nombre))
        print("{nombre} seleccion {eligio}".format(nombre=self.nombre, eligio = self.eligio))
    def aEleccionNumerica(self):
        switcher = {
            "piedra": 0,
            "papel": 1,
            "tijera": 2
        }
        return switcher[self.eligio]
    def incrementaPuntaje(self):
        self.puntaje += 1

class Rondajuego:
    def __init__(self, p1, p2):
        self.rules = [
            [0, -1, 1],
            [1, 0, -1],
            [-1, 1, 0]
        ]

        p1.elegir()
        p2.elegir()
        result = self.compareEleccion(p1,p2)
        if result > 0:
            p1.incrementaPuntaje()
        elif result < 0:
            p2.incrementaPuntaje()    
        print("la Ronda resulto en que Spock {result}".format(result = self.obtieneResultadoCadena(result) ))

    def compareEleccion(self, p1, p2):
        return self.rules[p1.aEleccionNumerica()][p2.aEleccionNumerica()]
    def puntajes(self):
        print("implementar")
    def obtieneResultadoCadena(self, result):
        res = {
            0: "empata",
            1: "gana",
            -1: "pierde"
        }       
        return res[result]


class Juego:
    def __init__(self):
        self.finalizarJuego = False
        self.jugador = Jugador("Spock")
        self.segundoJugador = Jugador("Kirk")
    def comenzar(self):
        while not self.finalizarJuego:
            Rondajuego(self.jugador, self.segundoJugador)
            self.revisarcondicionfinalde()

    def revisarcondicionfinalde(self):
        respuesta = input("Continue game y/n: ")
        if respuesta == 'y':
            Rondajuego(self.jugador, self.segundoJugador)
            self.revisarcondicionfinalde()
        else:
            print("juego terminado, {j1nombre} tiene {j1puntaje}, y {j2nombre} tiene {j2puntaje}".format(j1nombre = self.jugador.nombre, j1puntaje= self.jugador.puntaje, j2nombre=self.segundoJugador.nombre, j2puntaje=self.segundoJugador.puntaje))
            self.quiengano()
            self.finalizarJuego = True
    def quiengano(self):
        resultadocadena = "It's a Draw"
        if self.jugador.puntaje > self.segundoJugador.puntaje:
            resultadocadena = "El ganador es {name}".format(name=self.jugador.nombre)
        elif self.jugador.puntaje < self.segundoJugador.puntaje:
            resultadocadena = "El ganador es {name}".format(name=self.segundoJugador.nombre)
        print(resultadocadena)
    
juego = Juego()
juego.comenzar()