from estructuras import Node, FIFO, LIFO, Priority

from algorithms import (
    breadth_first_search,
    depth_first_search,
    uniform_cost_search,
    greedy_best_first_search,
    a_star_search,
    get_path
)
##Definimos los valores de heuristicas y el valor de las funciones de costo como listas
heuristicas = {
    'Warm-up activities': 5,
    'Skipping Rope': 16,
    'Exercise bike': 10,
    'Tread Mill': 12,
    'Step Mill': 14,
    'Dumbbell': 9,
    'Barbell': 10,
    'Cable-Crossover': 8,
    'Pulling Bars': 10,
    'Incline Bench': 8,
    'Leg Press Machine': 8,
    'Climbing Rope': 5,
    'Hammer Strength': 4,
    'Stretching': 0
}

grafo = {
    'Warm-up activities': [
        ('Skipping Rope', 10),
        ('Exercise bike', 10),
        ('Tread Mill', 10),
        ('Step Mill', 10)
    ],
    'Skipping Rope': [
        ('Dumbbell', 15),
        ('Barbell', 15)
    ],
    'Exercise bike': [
        ('Cable-Crossover', 25)
    ],
    'Tread Mill': [
        ('Pulling Bars', 20),
        ('Incline Bench', 20)
    ],
    'Step Mill': [
        ('Incline Bench', 16)
    ],
    'Dumbbell': [
        ('Leg Press Machine', 12)
    ],
    'Barbell': [
        ('Leg Press Machine', 10)
    ],
    'Cable-Crossover': [
        ('Climbing Rope', 10)
    ],
    'Pulling Bars': [
        ('Climbing Rope', 6)
    ],
    'Incline Bench': [
        ('Hammer Strength', 20)
    ],
    'Leg Press Machine': [
        ('Stretching', 11)
    ],
    'Climbing Rope': [
        ('Stretching', 10)
    ],
    'Hammer Strength': [
        ('Stretching', 8)
    ],
    'Stretching': []
}

def get_vecinos(state):
    vecinos = []
    for vecino, cost in grafo[state]:
        vecinos.append((vecino, f"{state} -> {vecino}", cost))
    return vecinos

def correr_busquedas():
    estado_inicial = 'Warm-up activities'
    estado_objetivo = 'Stretching'
    
    resultados = {}
    
    # Corremos algoritmos no informados
    busqueda_no_informada = {
        'BFS': breadth_first_search,
        'DFS': depth_first_search,
        'UCS': uniform_cost_search
    }
    
    for name, search_fn in busqueda_no_informada.items():
        resultado = search_fn(estado_inicial, estado_objetivo, get_vecinos)
        if resultado:
            path = get_path(resultado)
            resultados[name] = {
                'path': path,
                'cost': resultado.cost,
                'detailed': False
            }
    
    # corremos algoritmos informados
    resultado_greedy = greedy_best_first_search(estado_inicial, estado_objetivo, get_vecinos, heuristicas)
    if resultado_greedy:
        resultados['Greedy'] = {
            'path': get_path(resultado_greedy),
            'cost': resultado_greedy.cost,
            'detailed': True,
            'node': resultado_greedy
        }
    
    resultado_a_estrella = a_star_search(estado_inicial, estado_objetivo, get_vecinos, heuristicas)
    if resultado_a_estrella:
        resultados['A*'] = {
            'path': get_path(resultado_a_estrella),
            'cost': resultado_a_estrella.cost,
            'detailed': True,
            'node': resultado_a_estrella
        }
    
    return resultados


def print_resultados_busqueda(results):
    for algorithm, result in results.items():
        print(f"\n{'-'*50}")
        print(f"{algorithm} Resultados Busqueda:")
        print(f"{'-'*50}")
        
        if algorithm == 'Greedy':
            print("Camino tomado:")
            for state, action, _ in result['path']:
                if action:
                    print(f"  {action}")
                else:
                    print(f"  Nodo incial {state}")
            
            print("\nValores de la heuristica por paso :")
            current = result['node']
            path = []
            while current:
                path.append(current)
                current = current.parent
            path = list(reversed(path))
            
            for i, node in enumerate(path):
                print(f"Paso {i}:")
                print(f"  Estado: {node.state}")
                print(f"  h(n) = {heuristicas[node.state]}")
                if node.action:
                    print(f"  Action: {node.action}")
                print()
            
        elif algorithm == 'A*':
            print("Camino tomado:")
            for state, action, _ in result['path']:
                if action:
                    print(f"  {action}")
                else:
                    print(f"  Nodo inicial: {state}")
            
            print("\nValores función a*:")
            current = result['node']
            path = []
            while current:
                path.append(current)
                current = current.parent
            path = list(reversed(path))
            
            for i, node in enumerate(path):
                print(f"Paso {i}:")
                print(f"  Estado: {node.state}")
                f_n = node.cost + heuristicas[node.state]
                print(f"  f(n) = {f_n}")
                if node.action:
                    print(f"  Action: {node.action}")
                print()
            
        else:
            print("Camino Tomado:")
            for state, action, cost in result['path']:
                if action:
                    print(f"  {action} (Costo: {cost})")
                else:
                    print(f"  Nodo Incial {state}")
            print(f"Costo Acumulado: {result['cost']}")    

def main():
    print("Corriendo algoritmos de búsqueda: ")
    
    results = correr_busquedas()
    print_resultados_busqueda(results)
    


if __name__ == "__main__":
    main()