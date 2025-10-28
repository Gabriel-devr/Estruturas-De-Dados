class No:
    def __init__(self,x):
        self.dado=x
        self.prox=None

class Lista:
    def __init__(self):
        self.prim=None

    def adicionarNoInicio(self,x):
            novoNo=No(x)
            novoNo.prox= self.prim
            self.prim=novoNo

    def encontrar_menor(self):
        if self.prim is not None:
            menor=self.prim.dado
            atual=self.prim.prox

            while (atual is not None):
                if atual.dado<menor:
                    menor =atual.dado
                atual= atual.prox
            return menor

        else:
            return None
    
    def elementos_impar(self):
        if self.prim is not None:
            noAtual=self.prim
            contador=0
            while(noAtual is not None):
                if ((noAtual.dado%2)!=0):
                    contador+=1
                noAtual=noAtual.prox
            return contador
        else:
            return 0
        
    def mediaValores(self):
        if (self.prim is not None):
            noAtual=self.prim
            contador=0
            soma=0
            while(noAtual is not None):
                soma+=noAtual.dado
                contador+=1
                noAtual=noAtual.prox
            media=soma/contador
            return media
        else:
            return 0
        
    def soma(self):
        if (self.prim is not None):
            noAtual=self.prim
            soma=0
            while(noAtual is not None):
                soma+=noAtual.dado
                noAtual=noAtual.prox
            return soma
        else:
            return 0
        
    def somaDosQuadrados(self):
        if (self.prim is not None):
            noAtual=self.prim
            soma=0
            while(noAtual is not None):
                soma+=noAtual.dado**2
                noAtual=noAtual.prox
            return soma
        else:
            return 0
        
minha_lista=Lista()
minha_lista.adicionarNoInicio(1)
minha_lista.adicionarNoInicio(2)
minha_lista.adicionarNoInicio(3)
minha_lista.adicionarNoInicio(1)
minha_lista.adicionarNoInicio(5)
print(minha_lista.somaDosQuadrados())