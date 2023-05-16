#from range to range
def fromRangeToRange(x, in_min, in_max, out_min, out_max):
    return ((x - in_min) * (out_max - out_min) / (in_max - in_min) )+ out_min

print(fromRangeToRange(0.5, 0, 1, 0, 100))