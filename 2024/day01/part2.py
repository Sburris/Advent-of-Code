''' Solution for Day 1 - Part 1 of Advent of code '''
''' https://adventofcode.com/2024/day/1 '''

def main():
    left, right = get_input_lists()
    distance = get_similarity_score(left, right)
    print(f"Similarity Score: {distance}")

def get_similarity_score(list1, list2):
    list1 = sorted(list1)
    
    lookup = {}
    for num in list2:
        lookup[num] = lookup.get(num, 0) + 1
    
    sum = 0
    for num in list1:
        sum += num * lookup.get(num, 0)
        
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