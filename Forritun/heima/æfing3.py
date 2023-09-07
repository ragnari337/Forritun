n1 = int(input("Number one: "))
n2 = int(input("Number two: "))
n3 = int(input("Number three: "))
if n1 < n2 and n1 < n3:
    print("The lowest value is Number one:", n1)
elif n2 < n1 and n2 < n3:
    print("The lowest value is Number two:", n2)
elif n3 < n1 and n3 < n2:
    print("The lowest value is Number three:", n3)

