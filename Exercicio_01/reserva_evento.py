#Exercício Sistema de Reserva para um Evento

class Evento:
    #método construtor
    def __init__(self, capacidade = 10):
        
        self.lugares_disponiveis = capacidade
        

    #métodos
    def reservar(self):

        if self.lugares_disponiveis == 0:
            print("Não há lugares disponíveis para a reserva")

            return
            
        self.lugares_disponiveis -= 1
        print("Lugar reservado com sucesso")
            
    def cancelar(self):

        if self.lugares_disponiveis == 10:
            print("Não existe reservas para cancelar")

            return

        self.lugares_disponiveis += 1
        print("Reserva cancelada com sucesso !")

    def mostrar_lotacao(self):

        return f"Lugares disponíveis: {self.lugares_disponiveis}"
        
        
#Testes

evento = Evento()

evento.reservar()
evento.cancelar()
evento.cancelar()

evento.mostrar_lotacao()
