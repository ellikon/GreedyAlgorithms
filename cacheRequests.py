capacity = 3
requests = [1, 2, 3, 1, 1, 3, 4, 5, 2, 1]

cache = []


fifo = []
fifo_misses = 0

for id in requests:
    if len(cache) < 3:
        cache.append(id)
        fifo.append(id)
        continue

    if id in cache:
        continue

    if id not in cache:
        first = fifo.pop(0)
        cache.remove(first)
        cache.append(id)
        fifo.append(id)
        fifo_misses += 1

print(f"FIFO\t: {fifo_misses}")
