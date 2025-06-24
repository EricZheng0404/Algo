import collections
cache = collections.OrderedDict()

cache["a"] = 1
cache["b"] = 2
cache["c"] = 3
cache["d"] = 4

cache.move_to_end("a")
print(cache)