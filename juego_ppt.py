#jugador1 = input(str('elige una opcion, piedra, papel, tijera'))
  
# class Jugador:
# class Rondajuego:
# class Juego:

class Jugador:
    def __init__(self):
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
        return switcher[self.choice]
class Rondajuego:
    def __init__(self, p1, p2):
        p1.elegir()
        p2.elegir()
    def compareEleccion(self, p1, p2):
        return self.rules[p1.aEleccionNumerica()][p2.aEleccionNumerica()]
    def puntajes(self):
        print("implementar")

class juego:
    def __init__(self):
        self.finalizarJuego = False
        self.Jugador = Jugador("Spock")
        self.segundoJugador = Jugador("Kirk")
    def start(selft):
        juego_ronda = Rondajuego(self.jugador, self.segundojugador)

    def revisarcondicionfinal(self):
#class Rondajuego:

# class Juego:
#     def __init__(self):
#         self.finalizarJuego = False
#         self.Jugador = Jugador()
#         self.secondJugador = Jugador()
# _________________________
# class Participant:
#     def __init__(self, name):
#         self.name = name
#         self.points = 0
#         self.choice = ""
#     def choose(self):
#         self.choice = input("{name}, select rock, paper or scissor: ".format(name= self.name))
#         print("{name} selects {choice}".format(name=self.name, choice = self.choice))

# class GameRound:
#     def __init__(self, p1, p2):
#         p1.choose()
#         p2.choose()
#     def compareChoices(self):
#         print("implement")
#     def awardPoints(self):
#         print("implement")

# class Game:
#     def __init__(self):
#         self.endGame = False
#         self.participant = Participant("Spock")
#         self.secondParticipant = Participant("Kirk")
#     def start(self):
#         game_round = GameRound(self.participant, self.secondParticipant)

#     def checkEndCondition(self):
#         print("implement")
#     def determineWinner(self):
#         print("implement")

# game = Game()
# game.start()