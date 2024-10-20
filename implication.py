def implication(p, q):
    # p → q is equivalent to (not p) or q
    return (not p) or q

def print_truth_table():
    print("Truth Table for Logical Implication (p → q)")
    print("--------------------------------------------")
    print("| p | q | p → q |")
    print("--------------------------------------------")
    for p in [False, True]:
        for q in [False, True]:
            result = implication(p, q)
            print(f"| {int(p)} | {int(q)} |   {int(result)}   |")
    print("--------------------------------------------")

if __name__ == "__main__":
    print_truth_table()
#Implication Luis Alfonso