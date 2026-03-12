#1
n = int(input())
nums = list(map(int, input().split()))

# әр санды квадратқа көтереміз
squares = map(lambda x: x*x, nums)

print(sum(squares))
#2
n = int(input())
nums = list(map(int, input().split()))

# тек жұп сандарды қалдырамыз
evens = list(filter(lambda x: x % 2 == 0, nums))

print(len(evens))
#3
n = int(input())
words = input().split()

for i, w in enumerate(words):
    print(f"{i}:{w}", end=" ")
#4
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dot = sum(x * y for x, y in zip(a, b))

print(dot)
#5
s = input()

vowels = "aeiouAEIOU"

if any(ch in vowels for ch in s):
    print("Yes")
else:
    print("No")

#6
n = int(input())
nums = list(map(int, input().split()))

if all(x >= 0 for x in nums):
    print("Yes")
else:
    print("No")

#7
n = int(input())
words = input().split()

longest = max(words, key=len)

print(longest)

#8

n = int(input())
nums = list(map(int, input().split()))

unique_nums = sorted(set(nums))

print(*unique_nums)
#9
n = int(input())
keys = input().split()
values = input().split()

d = dict(zip(keys, values))

query = input()

if query in d:
    print(d[query])
else:
    print("Not found")

#10
n = int(input())
nums = list(map(int, input().split()))

count = sum(map(bool, nums))

print(count)