class Gafanhoto:
    def __init__(self): #Método Construtor
        #Atributos de instancia 
        self.nome = ""
        self.idade = 0
        

    #Métodos de instancia
    def aniversario (self):
        self.idade += 1
    
    def mensagem (self): 
        return f"{self.nome} tem {self.idade} anos de idade."

#Declaração de objetos

g1 = Gafanhoto()
g1.nome = "Júlia Forny"
g1.idade = 21
g1.aniversario()
print (g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Leonardo"
g2.idade = 23
g2.aniversario()
print (g2.mensagem())

g3 = Gafanhoto ()
g3.idade = 56
g3.nome = "Lucas"
g3.aniversario()
print (g3.mensagem())



