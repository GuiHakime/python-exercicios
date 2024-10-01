#Exercício

class Pet:

    def __init__(self):

        self._nome = ""
        self._idade = 0
        self._peso = 0.0

    def get_nome(self):

        return self._nome

    def set_nome(self, novo_nome):

        if isinstance(novo_nome, str) and novo_nome != "":
            self._nome = novo_nome

        else:
            print("Nome inválido")

    def get_idade(self):

        return self._idade

    def set_idade(self, nova_idade):

        if isinstance(nova_idade, int) and nova_idade > 0:

            self._idade = nova_idade

        else:
            print("Idade inválida")

    def get_peso(self):

        return self._peso

    def set_peso(self, novo_peso):

        if isinstance(novo_peso, float) and novo_peso > 0:

            self._peso = novo_peso

        else:
            print("Peso inválido")

    def exibir_info(self):

            print(f"Nome: {self._nome}")
            print(f"Idade: {self._idade}")
            print(f"Peso:{self._peso}")

            
meu_pet = Pet()
meu_pet.set_nome("Buddy")
meu_pet.set_idade(5)
meu_pet.set_peso(9.5)
meu_pet.exibir_info()

        
        
