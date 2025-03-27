import json
import os

def load_cities_data():
    file_path = os.path.join(os.path.dirname(__file__), 'cidadesSCDistâncias.json')
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def find_greedy_path(start, destination, cities_data):
    current_city = start
    visited = set()
    path = []
    total_distance = 0
    logs = []

    logs.append(f"Iniciando busca gulosa de '{start}' para '{destination}'")
    
    while current_city != destination:
        visited.add(current_city)
        path.append(current_city)
        logs.append(f"\nVisitando cidade: {current_city}")
        
        neighbors = [(city, dist) for city, dist in cities_data.get(current_city, {}).items() if city not in visited]
        
        if not neighbors:
            logs.append("Nenhum vizinho disponível - caminho impossível!")
            return {"path": path, "total_distance": total_distance, "message": "Percurso encerrado, impossível continuar", "logs": logs}
        
        next_city, distance = min(neighbors, key=lambda x: x[1])
        total_distance += distance
        logs.append(f"Decisão gulosa: escolhendo {next_city} (menor distância: {distance} km)")
        logs.append(f"Distância parcial acumulada: {total_distance} km")
        
        current_city = next_city
    
    path.append(destination)
    logs.append(f"\nPercurso concluído com sucesso!")
    logs.append(f"Caminho final: {' -> '.join(path)}")
    logs.append(f"Distância total percorrida: {total_distance} km")
    
    return {"path": path, "total_distance": total_distance, "message": "Percurso concluído com sucesso", "logs": logs}

def main():
    cities_data = load_cities_data()
    
    start = input('Digite a cidade de origem: ').strip()
    destination = input('Digite a cidade de destino: ').strip()
    
    if start not in cities_data or destination not in cities_data:
        print('Cidade inválida! Verifique o nome digitado.')
        return
    
    result = find_greedy_path(start, destination, cities_data)
    
    print("\n=== LOG DE DECISÕES ===")
    for log in result["logs"]:
        print(log)
    
    print("\n=== RESUMO DO PERCURSO ===")
    print(f"Caminho percorrido: {' -> '.join(result['path'])}")
    print(f"Distância total: {result['total_distance']} km")
    print(result["message"])

if __name__ == "__main__":
    main()
