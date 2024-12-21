''' Solution for Day 1 - Part 1 of Advent of code '''
''' https://adventofcode.com/2024/day/1 '''

def main():
    left, right = get_input_lists()
    distance = get_distances(left, right)
    print(f"Distance: {distance}")

def get_distances(list1, list2):
    list1 = sorted(list1)
    list2 = sorted(list2)
    
    sum = 0
    for left, right in zip(list1, list2):
        sum += abs(left - right)
    return sum

def get_input_lists():
    with open("./2024/day01/input.txt", "r") as file:
        lines = file.readlines()
        
    left = []
    right = []
    for line in lines:
        parts = line.split()
        left.append(int(parts[0]))
        right.append(int(parts[1]))
    
    return left, right

if __name__ == "__main__":
    main()