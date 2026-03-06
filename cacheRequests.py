capacity = 3
requests = [1, 2, 3, 1, 1, 3, 4, 5, 2, 1]


def fifo(capacity, requests):
    cache = []
    fifo = []
    fifo_misses = 0

    for id in requests:
        if len(cache) < capacity and id not in cache:
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
    return fifo_misses

def lru(capacity, requests):
    cache = []
    lru = []
    lru_misses = 0

    for id in requests:
        if len(cache) < capacity and id not in cache:
            cache.append(id)
            lru.append(id)
            continue

        if id in cache:
            lru.remove(id)
            lru.append(id)
            continue

        if id not in cache:
            last_used = lru.pop(0)
            cache.remove(last_used)
            cache.append(id)
            lru.append(id)
            lru_misses += 1
    return lru_misses

print(f"FIFO\t: {fifo(capacity, requests)}")
print(f"LRU\t: {lru(capacity, requests)}")