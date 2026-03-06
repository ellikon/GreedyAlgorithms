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
            fifo_misses += 1
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
            lru_misses += 1
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


def OPTFF(capacity, requests):
    size = len(requests)

    next_time = [float('inf')]* size
    seen = {}

    for i in range(size-1, -1, -1):
        item = requests[i]
        if item in seen:
            next_time[i] = seen[item]
        seen[item] = i

    cache = []
    next_in_cache = {}
    misses = 0

    for i, item in enumerate(requests):
        if item in cache:
            next_in_cache[item] = next_time[i]
            continue

        misses += 1

        if len(cache) < capacity:
            cache.append(item)
            next_in_cache[item] = next_time[i]
        else:
            eviction = None
            farthest = -1

            for cached in cache:
                far = next_in_cache[cached]
                if far > farthest:
                    farthest = far
                    eviction = cached

            cache.remove(eviction)
            del next_in_cache[eviction]

            cache.append(item)
            next_in_cache[item] = next_time[i]

    return misses

print(f"FIFO\t: {fifo(capacity, requests)}")
print(f"LRU\t: {lru(capacity, requests)}")
print(f"OPTFF\t: {OPTFF(capacity, requests)}")