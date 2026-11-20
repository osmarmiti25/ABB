class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None


class ABB:
    def __init__(self):
        self.raiz = None

    # ---------- INSERCIÓN ----------
    def insertar(self, valor):
        self.raiz = self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if nodo is None:              # lugar vacío: aquí va el nuevo nodo
            return Nodo(valor)
        if valor < nodo.valor:
            nodo.izq = self._insertar(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der = self._insertar(nodo.der, valor)
        return nodo                   # si es igual, no se repite

    # ---------- BÚSQUEDA ----------
    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, nodo, valor):
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        if valor < nodo.valor:
            return self._buscar(nodo.izq, valor)
        return self._buscar(nodo.der, valor)

    # ---------- RECORRIDOS ----------
    def preorden(self, nodo):
        if nodo:
            print(nodo.valor, end=" ")
            self.preorden(nodo.izq)
            self.preorden(nodo.der)

    def inorden(self, nodo):
        if nodo:
            self.inorden(nodo.izq)
            print(nodo.valor, end=" ")
            self.inorden(nodo.der)

    def postorden(self, nodo):
        if nodo:
            self.postorden(nodo.izq)
            self.postorden(nodo.der)
            print(nodo.valor, end=" ")


# ---------- PRUEBA ----------
arbol = ABB()
for n in [50, 30, 70, 20, 40, 60, 80]:
    arbol.insertar(n)

print("Preorden:  ", end="")
arbol.preorden(arbol.raiz)

print("\nInorden:   ", end="")
arbol.inorden(arbol.raiz)

print("\nPostorden: ", end="")
arbol.postorden(arbol.raiz)

print("\n\n¿Existe el 40?", arbol.buscar(40))
print("¿Existe el 99?", arbol.buscar(99))
