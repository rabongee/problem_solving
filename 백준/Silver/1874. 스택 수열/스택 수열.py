import sys

n = int(input())
numbers = []
calc = []
i = 1
for _ in range(n):
    number = int(sys.stdin.readline())
    while i <= number:
        numbers.append(i)
        calc.append("+")
        i += 1
    if numbers.pop() == number:
        calc.append("-")
    else:
        print("NO")
        break
if not numbers:
   print("\n".join(calc))