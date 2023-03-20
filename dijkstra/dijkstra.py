import json

def main():
    # Read in the graph
    with open("./graphs/A-E.json", "r") as read_file:
        data = json.load(read_file)
    
    print(data)
    
if __name__ != "main":
    main()