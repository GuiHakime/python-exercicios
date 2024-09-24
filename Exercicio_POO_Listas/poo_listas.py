#Exercíio Manipulador de Listas em Python

class ManipuladorDeLista:

    def __init__(self):
        self.lista = []

    #Operaçoes

    def adicionar_elemento(self, elemento):
        
        self.lista.append(elemento)

    def remover_elemento(self, elemento):

        self.lista.remove(elemento)

    def maior_elemento(self):

        if self.lista:

            return max(self.lista)

        else:

            return "A lista está vazia"

    def menor_elemento(self):

        if self.lista:

            return min(self.lista)

        else:

            return "A lista está vazia"

    def mostrar_media(self):

        if self.lista:

            return sum(self.lista) / len(self.lista)
        

        else: 

            return "A lista está vazia"
            
    def mostrar_lista(self):

        return self.lista

def menu():
    #Criar nova instância da classe ManipuladorDeLista
    manipulador = ManipuladorDeLista()
    
    print("\nBem vindo ao MENU, escolha uma opção: ")

    while True:
        

        print("\nEscolha uma opção para formatar a sua frase:")
        print("1. Adicionar Elemento")
        print("2. Remover Elemento")
        print("3. Encontrar Maior")
        print("4. Encontrar Menor")
        print("5. Calcular Média")
        print("6. Mostrar Lista")
        print("7. SAIR")
        
        escolha = input("\nDigite o  número da sua escolha: ")

        if escolha == "1":

            try:

                elemento = int(input("Digite o elemento para adicionar"))

                manipulador.adicionar_elemento(elemento)
            
            except ValueError:

                print("Entrada inválida. Por favor, insira um número inteiro")

        elif escolha == "2":

            try:

                elemento = int(input("Digite o elemento para remover da lista: "))

                if elemento in manipulador.lista:

                    manipulador.remover_elemento(elemento)

                else:
                    
                     print("Elemento não está nalista para ser removido !!!")

            except ValueError:

                print("Entrada inválida. Por favor, insira um número inteiro")

        elif escolha == "3":

            print(f"O maior elemento da lista é : {manipulador.maior_elemento()}")

        elif escolha == "4":

             print(f"O menor elemento da lista é : {manipulador.menor_elemento()}")
           
                    
        elif escolha == "6":

            print(f"A lista atual é: {manipulador.mostrar_lista()}")

        elif escolha == "5":

            print(f"A média da lista é: {manipulador.mostrar_media()}")
            
        elif escolha == "7":

            print("Saindo do programa !")

            break

        else:

            print("Escolha inválida, tente novamnete !")
            
if __name__ == "__main__": # Verifica se o script está sendo executado como programa principal e chama menu

    menu()
