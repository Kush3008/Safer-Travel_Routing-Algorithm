from graph import *
import dijkstra
import draw_map
import time


def main():
    paths = []

    paths.append(path_generator(1, (-75.5790173, 6.1971336), (-75.5762232, 6.266327)))

    paths.append(path_generator(2, (77.229446, 28.6128946), (77.2410456, 28.6562456)))

    paths.append(path_generator(3, (-75.5790173, 6.1971336), (-75.5762232, 6.266327)))

    draw_map.draw_map(*paths)
    paths.clear()

def path_generator(type_weight_harassment, start, target):
    print("Starting the timer")
    start_time = time.time()

    print('Loading graph...')
    graph = create_graph(type_weight_harassment)

    path, path_names, distance, distance_harassment = dijkstra.shortest_safest_path(graph, start, target)
    print("+----------------------------------------+")
    print("Path: ", path)
    print("Path names: ", path_names)
    print("+----------------------------------------+")
    print(f"Distance: {distance} m")
    print("Distance-harassment: ", distance_harassment)
    print("+----------------------------------------+")
    print(f"Time: {round(time.time() - start_time, 3)} seconds")
    print("+----------------------------------------+")

    return path


if __name__ == '__main__':
    main()