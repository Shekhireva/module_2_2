first = 12
second = 16
third = 26
if first == second and second == third and third == first:
    print(3)
elif first != second and second != third and third != first:
    print(0)
elif first == second or second == third or third == first:
    print(2)


