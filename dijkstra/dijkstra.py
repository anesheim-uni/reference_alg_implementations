'''Module that contains the dijkstra's shortest path implementation'''
import json

def main():
    '''Function main, runs the module'''
    # Read in the graph
    with open("./graphs/A-E.json", "r") as read_file:
        data = json.load(read_file)
    print(data)

if __name__ != "main":
    main()
