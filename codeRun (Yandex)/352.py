import sys

# inputed_text = sys.stdin.readlines()

jewels = sys.stdin.readline().strip()
stones = sys.stdin.readline().strip()
print(jewels, stones)

result = 0
for stone in stones:
  if stone in jewels:
    result += 1

print(result)