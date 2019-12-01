import math 

def main():
    with open("input_day1.txt") as f:
        lst = [int(x) for x in f.read().split()]
    print("part 1 sum : " + str(sum([fuel_req(x) for x in lst])))
    print("part 2 sum : " + str(sum([rec_fuel_req(x) for x in lst])))
"""
Part 2 Solution
"""
def rec_fuel_req(mass):
    if fuel_req(mass) <= 0:
        return 0
    return rec_fuel_req(fuel_req(mass)) + fuel_req(mass)
"""
Part 1 Solution 
"""
def fuel_req(mass):
    return (math.floor(mass / 3) - 2)
if __name__ == "__main__":
    main()