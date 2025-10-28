#Duplamente Encadeada
class No:
    def __init__ (self,x):
        self.dado=x
        self.prox=None
        self.prev=None

class Lista:
    def __init__ (self):
        self.prim=None
        self.ult=None

    def inserirNaCabeca(self,x):
        novoNo=No(x)
        if (self.prim is None):
            self.prim=novoNo
            self.ult=novoNo
        else:
            novoNo.prox=self.prim
            self.prim.prev=novoNo
            self.prim=novoNo
        return 

    def inserirNaCauda(self,x):
        novoNo=No(x)
        if (self.prim is None):
            self.prim=novoNo
            self.ult=novoNo
        else:
            novoNo.prev=self.ult
            self.ult.prox=novoNo
            self.ult=novoNo
        return True

    def impressaoElementos(self):
        if self.prim is not None:
            atual=self.prim
            while(atual is not None):
                print(atual.dado)
                atual=atual.prox
            return True
        
    def impressaoElementosInvertido(self):
        if self.ult is not None:
            atual=self.ult
            while(atual is not None):
                print(atual.dado)
                atual=atual.prev
            return True
        
    def remocaoElemento(self,x):#tá errado veja
        if(self.prim is not None):
            if (self.prim.dado==x):
                if (self.prim==self.ult):
                    self.prim=None
                    self.ult=None
            atual=self.prim
            while(atual.dado!=x and atual is not None):
                atual=atual.prox
            if (atual.dado==x):
                atual.prev.prox=atual.prox
                atual.prox.prev=atual.prev
                return True
            else:
                return False
        
minhaLista = Lista()
minhaLista.inserirNaCabeca(10)
minhaLista.inserirNaCabeca(20)
minhaLista.inserirNaCabeca(30)
minhaLista.inserirNaCabeca(40)
minhaLista.remocaoElemento(20)
minhaLista.impressaoElementos()