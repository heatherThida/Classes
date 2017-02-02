def partition(ll):
  pivot = ll[0]
  a = []
  b = []
  for x in ll[1:]:
    if x < pivot:
      a.append(x)
    else:
      b.append(x)
  return pivot, a, b

def quicksort(ll):
  if len(ll) in [ 0, 1 ]:
    return ll
  else:
    pivot, a, b = partition(ll)
    a_sorted = quicksort(a)
    b_sorted = quicksort(b)
    return a_sorted + [ pivot ] + b_sorted

print (quicksort([500, 700, 800, 100, 300, 200, 900, 400, 1000, 600]))
