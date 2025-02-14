from estructuras import Node, FIFO, LIFO, Priority

# Defininimos los 5 algoritmos de búsqueda con su frontera y nodos explorados

def breadth_first_search(estado_inicial, estado_meta, get_vecinos):
    frontera = FIFO()
    explorado = set()
    
    nodo_inicial = Node(estado_inicial)
    frontera.add(nodo_inicial)
    
    while not frontera.isEmpty():
        current = frontera.pop()
        
        if current.state == estado_meta:
            return current
            
        explorado.add(current.state)
        
        for vecino, action, cost in get_vecinos(current.state):
            if vecino not in explorado:
                hijo = Node(vecino, current, action, current.cost + cost)
                frontera.add(hijo)
    
    return None

def depth_first_search(estado_inicial, estado_meta, get_vecinos):
    frontera = LIFO()
    explorado = set()
    
    nodo_inicial = Node(estado_inicial)
    frontera.add(nodo_inicial)
    
    while not frontera.isEmpty():
        current = frontera.pop()
        
        if current.state == estado_meta:
            return current
            
        explorado.add(current.state)
        
        for vecino, action, cost in get_vecinos(current.state):
            if vecino not in explorado:
                hijo = Node(vecino, current, action, current.cost + cost)
                frontera.add(hijo)
    
    return None

def uniform_cost_search(estado_incial, estado_meta, get_vecinos):
    frontera = []  
    explorado = set()
    
    nodo_inicial = Node(estado_incial)
    frontera.append((0, nodo_inicial))  
    
    while frontera:
        frontera.sort(key=lambda x: x[0])
        current_cost, current = frontera.pop(0)
        
        if current.state == estado_meta:
            return current
            
        explorado.add(current.state)
        
        for vecino, action, paso_cost in get_vecinos(current.state):
            nuevo_costo = current.cost + paso_cost
            
            estados_frontera = {node.state: (c, node) for c, node in frontera}
            
            if vecino not in explorado and vecino not in estados_frontera:
                hijo = Node(vecino, current, action, nuevo_costo)
                frontera.append((nuevo_costo, hijo))
            elif vecino in estados_frontera:
                if nuevo_costo < estados_frontera[vecino][0]:
                    frontera.remove(estados_frontera[vecino])
                    hijo = Node(vecino, current, action, nuevo_costo)
                    frontera.append((nuevo_costo, hijo))
    
    return None

def greedy_best_first_search(estado_inicial, estado_meta, get_vecinos, heuristica):
    frontera = []  
    explorado = set()
    
    nodo_incial = Node(estado_inicial)
    frontera.append((heuristica[estado_inicial], nodo_incial))
    
    while frontera:
        frontera.sort(key=lambda x: x[0])
        _, current = frontera.pop(0)
        
        if current.state == estado_meta:
            return current
            
        explorado.add(current.state)
        
        for vecino, action, step_cost in get_vecinos(current.state):
            if vecino not in explorado and not any(n.state == vecino for _, n in frontera):
                hijo = Node(vecino, current, action, current.cost + step_cost)
                frontera.append((heuristica[vecino], hijo))
    
    return None

def a_star_search(estado_inicial, estado_meta, get_vecinos, heuristica):
    frontera = []  
    explorado = set()
    
    nodo_inicial = Node(estado_inicial)
    frontera.append((heuristica[estado_inicial], nodo_inicial))
    
    while frontera:
        frontera.sort(key=lambda x: x[0])
        _, current = frontera.pop(0)
        
        if current.state == estado_meta:
            return current
            
        explorado.add(current.state)
        
        for vecino, action, step_cost in get_vecinos(current.state):
            if vecino not in explorado and not any(n.state == vecino for _, n in frontera):
                hijo = Node(vecino, current, action, current.cost + step_cost)
                f_value = hijo.cost + heuristica[vecino]
                frontera.append((f_value, hijo))
            elif any(n.state == vecino for _, n in frontera):
                for i, (f_val, node) in enumerate(frontera):
                    if node.state == vecino:
                        new_cost = current.cost + step_cost
                        if new_cost < node.cost:
                            hijo = Node(vecino, current, action, new_cost)
                            f_value = new_cost + heuristica[vecino]
                            frontera[i] = (f_value, hijo)
                        break
    
    return None

def get_path(node):
    path = []
    current = node
    while current:
        path.append((current.state, current.action, current.cost))
        current = current.parent
    return list(reversed(path))