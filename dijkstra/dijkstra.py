'''Module that contains the dijkstra's shortest path implementation'''
import json


def find_candidate(shortest_path: dict[str, tuple[int, str]], unvisited: list[str]) -> str:
    """
    Find the node with the lowest cost currently
    Args:
        shortest_path (dict[str, tuple[int, str]]): shortest path table (dist and prev)
        unvisited (list[str]): list of not-yet visited nodes
    Returns:
        str: the node (candidate) with the lowest cost
    """
    minimum: int = 1000
    smallest_key: str = "null"
    for elem in unvisited:
        if shortest_path[elem][0] < minimum:
            minimum = shortest_path[elem][0]
            smallest_key = elem

    return smallest_key


def update_shortest_path(selected_node: str,
                         neighbors: dict[str, int],
                         shortest_path: dict[str, tuple[int, str]]) -> dict[str, tuple[int, str]]:
    """
    Updates the shortest path of the candidate node if a better alternative is found
    Args:
        selected_node (str): the candidate node under consideration
        neighbors (dict[str, int]): immediate neighbors to th candidate node
        shortest_path (dict[str, tuple[int, str]]): shortest path table (dist and prev)

    Returns:
        dict[str, tuple[int, str]]: updated shortest path table (dist and prev)
    """
    for key, value in neighbors.items():
        if value + shortest_path[selected_node][0] < shortest_path[key][0]:
            shortest_path[key] = value + shortest_path[selected_node][0], selected_node
    return shortest_path


def dijkstra(graph: dict[str, dict[str, int]],
             source: str) -> dict[str, tuple[int, str]]:
    """
    Calculates the single source shortest path according to the dijkstra algorithm
    Args:
        graph (dict[str, dict[str, int]]): The input graph consisting of nodes and connecting edges
        source (str): The source node, used as basis for the dijkstra run
    Returns:
        dict[str, tuple[int, str]: Updated shortest path matrix consisting of dist and prev columns
    """
    unvisited: list[str] = []
    shortest_path: dict[str, tuple[int, str]] = {}

    # Init
    for key in graph:
        unvisited.append(key)
        if key != source:
            shortest_path[key] = (1000, "null")
        else:
            shortest_path[key] = (0, "source")

    # Continue as long as we are not done
    while len(unvisited) > 0:
        selected_node = find_candidate(shortest_path, unvisited)
        unvisited.remove(selected_node)

        # Relax/Update weights
        shortest_path = update_shortest_path(selected_node,
                                             graph[selected_node],
                                             shortest_path)

    return shortest_path


def main():
    '''
    Function main, runs the module
    Returns:
        None: None
    '''
    # Read in the graph
    with open("../graphs/A-O.json", "r", encoding="utf-8") as read_file:
        data: dict[str, dict[str, int]] = json.load(read_file)

    source = "A"
    dijkstra_res = dijkstra(data, source)
    print(dijkstra_res)



if __name__ != "main":
    main()
