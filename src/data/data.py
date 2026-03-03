class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):


        """
        Invierte el orden de los elementos en una lista sin usar reversed() o lista[::-1].
        
        Args:
            lista (list): Lista a invertir
            
        Returns:
            list: Lista con los elementos en orden inverso
        """
        lista_invertida = []

        for i in range(len(lista) - 1, -1, -1):
            lista_invertida.append(lista[i])

        return lista_invertida
        
    
    def buscar_elemento(self, lista, elemento):

        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
            
        return -1

        """
        Busca un elemento en una lista y devuelve su índice (o -1 si no existe).
        Implementación manual sin usar index().
        
        Args:
            lista (list): Lista donde buscar
            elemento: Elemento a buscar
            
        Returns:
            int: Índice del elemento o -1 si no se encuentra
        """
        
    
    def eliminar_duplicados(self, lista):
        lista_nueva= []

        for elemento in lista:
            if elemento not in lista_nueva:
                lista_nueva.append(elemento)
        return lista_nueva
        """
        Elimina elementos duplicados de una lista sin usar set().
        Mantiene el orden original de aparición.
        
        Args:
            lista (list): Lista con posibles duplicados
            
        Returns:
            list: Lista sin elementos duplicados
        """
        
    
    def merge_ordenado(self, lista1, lista2):
        
        lista3 = lista1 + lista2

        
        for i in range(len(lista3)):
            for j in range(0, len(lista3) - i - 1):
                if lista3[j] > lista3[j + 1]:
                    
                    lista3[j], lista3[j + 1] = lista3[j + 1], lista3[j]

       
        return lista3



        """
        Combina dos listas ordenadas en una sola lista ordenada.
        
        Args:
            lista1 (list): Primera lista ordenada
            lista2 (list): Segunda lista ordenada
            
        Returns:
            list: Lista combinada y ordenada
        """
    
    
    def rotar_lista(self, lista, k):

       
        n = len(lista)
        
        if n == 0:
            return lista
        
        k = k % n
        
        for _ in range(k):
            ultimo = lista.pop()
            lista.insert(0, ultimo)
        
        return lista
        """
        Rota los elementos de una lista k posiciones a la derecha.
        
        Args:
            lista (list): Lista a rotar
            k (int): Número de posiciones a rotar
            
        Returns:
            list: Lista rotada
        """
        
    
    def encuentra_numero_faltante(self, lista):
        n = len(lista) + 1
        suma_esperada = n * (n + 1) // 2
        suma_real = sum(lista)
            
        return suma_esperada - suma_real
        """
        Encuentra el número faltante en una lista de enteros del 1 al n.
        
        Args:
            lista (list): Lista de enteros del 1 al n con un número faltante
            
        Returns:
            int: El número que falta en la secuencia
        """
        
    
    def es_subconjunto(self, conjunto1, conjunto2):
        """
        Verifica si conjunto1 es subconjunto de conjunto2 sin usar set.
        
        Args:
            conjunto1 (list): Posible subconjunto
            conjunto2 (list): Conjunto principal
            
        Returns:
            bool: True si conjunto1 es subconjunto de conjunto2, False en caso contrario
        """
        pass
    
    def implementar_pila(self):
        """
        Implementa una estructura de datos tipo pila (stack) usando listas.
        
        Returns:
            dict: Diccionario con métodos push, pop, peek y is_empty
        """
        pass
    
    def implementar_cola(self):
        """
        Implementa una estructura de datos tipo cola (queue) usando listas.
        
        Returns:
            dict: Diccionario con métodos enqueue, dequeue, peek y is_empty
        """
        pass
    
    def matriz_transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz.
        
        Args:
            matriz (list): Lista de listas que representa una matriz
            
        Returns:
            list: Matriz transpuesta
        """
        pass