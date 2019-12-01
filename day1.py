import math 

def main():
    with open("input_day1.txt") as f:
        lst = [int(x) for x in f.read().split()]
    print(sum([fuel_req(x) for x in lst]))
def fuel_req(mass):
    return (math.floor(mass / 3) - 2)
if __name__ == "__main__":
    main()