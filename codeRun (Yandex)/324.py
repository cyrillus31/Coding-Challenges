def qsort_up(l: list) -> list:
    if len(l) == 1 or len(l) == 0:
        return l
    pivot = len(l) // 2
    left = [element for element in l if element < l[pivot]]
    right = [element for element in l if element > l[pivot]]
    center = [element for element in l if element == l[pivot]]
    return qsort_up(left) + center + qsort_up(right)

print(qsort_up([432,423,543,41425,2]))

def qsort_down(l: list) -> list:
    if len(l) == 1 or len(l) == 0:
        return l
    pivot = len(l) // 2
    right = [element for element in l if element < l[pivot]]
    left = [element for element in l if element > l[pivot]]
    center = [element for element in l if element == l[pivot]]
    return qsort_down(left) + center + qsort_down(right)

print(qsort_down([432,423,543,41425,2]))

p, b = map(int, input().split())
prices = list(map(int, input().split()))
buyers = list(map(int, input().split()))

print(buyers, prices)
buyers = qsort_down(buyers)
prices = qsort_up(prices)
print(buyers, prices)

if p > b:
  r = range(b)
else:
  r = range(p)

results = []

for i in r:
  if prices[i] < buyers[i]:
    results.append(abs(buyers[i] - prices[i]))

print(sum(results))



# print(qsort_up([3,23,432,543,3]))