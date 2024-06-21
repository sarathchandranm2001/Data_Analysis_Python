def set_operations():
    elements_A = input("Enter elements of set A separated by spaces: ").split()
    set_A = set(elements_A)
    
    
    elements_B = input("Enter elements of set B separated by spaces: ").split()
    set_B = set(elements_B)
    
    
    union_set = set_A.union(set_B)
    intersection_set = set_A.intersection(set_B)
    difference_AB = set_A.difference(set_B)
    difference_BA = set_B.difference(set_A)
    
    
    print(f"\nSet A: {set_A}")
    print(f"Set B: {set_B}")
    print(f"\n1. Set Union (A union B): {union_set}")
    print(f"2. Set Intersection (A intersection B): {intersection_set}")
    print(f"3. Set Difference (A - B): {difference_AB}")
    print(f"4. Set Difference (B - A): {difference_BA}")


set_operations()
