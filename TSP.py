'''import itertools

def tsp():
    cities = ['A', 'B', 'C', 'D', 'E']
    num_cities = int(input("Enter the number of cities: "))
    distances = {}
    for i in range(len(num_cities)):
        for j in range(i+1, len(num_cities)):
            distance = input(f"Enter distance between {cities[i]} and {cities[j]}: ")
            distances[(cities[i], cities[j])] = int(distance)
            distances[(cities[j], cities[i])] = int(distance)

    min_distance = float('inf')
    min_path = None
    for path in itertools.permutations(cities):
        distance = 0
        for i in range(len(path)-1):
            distance += distances[(path[i], path[i+1])]
        if distance < min_distance:
            min_distance = distance
            min_path = path

    print(f"The shortest possible route is {min_path} with a distance of {min_distance} units.")

if __name__ == '__main__':
    tsp()'''


import itertools

def calculate_distance(distances, path):
    return sum(distances[path[i-1]][path[i]] for i in range(len(path)))

def tsp(distances):
    n = len(distances)
    cities = range(n)
    shortest_path = None
    min_distance = float('inf')

    for path in itertools.permutations(cities):
        path_distance = calculate_distance(distances, path)
        if path_distance < min_distance:
            min_distance = path_distance
            shortest_path = path

    return shortest_path, min_distance

# Get the number of cities from the user
n = int(input("Enter the number of cities: "))

# Initialize the distances matrix
distances = [[0]*n for _ in range(n)]

# Get the distances from the user
for i in range(n):
    for j in range(i+1, n):
        distances[i][j] = distances[j][i] = int(input(f"Enter the distance from city {i} to city {j}: "))

path, distance = tsp(distances)
print(f"The shortest path is {path} with total distance {distance}")
