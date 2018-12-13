class Node:

    def __init__(self, parent):
        self.parent = parent
        self.children = []
        self.metadata = []
        
    def add_child(self, child):
        self.children.append(child)

    def add_metadata(self, data):
        self.metadata.append(data)

def solve(puzzle):
    puzzle.append(0)
    root = recursive_parse(puzzle, None, puzzle.pop(0), puzzle.pop(0))
    print(puzzle[-1])

def recursive_parse(puzzle, parent, child_count, meta_count):
    current_node = Node(parent)
    for i in range(child_count):
        current_node.add_child(recursive_parse(puzzle, current_node, puzzle.pop(0), puzzle.pop(0)))
    for i in range(meta_count):
        current_node.add_metadata(puzzle.pop(0))
        puzzle[-1] += current_node.metadata[-1]
    return current_node

def get_input():
    return list(map(int, open('puzzle_input.txt').read()[:-1].split()))

if __name__ == "__main__":
    puzzle = get_input()
    solve(puzzle)
