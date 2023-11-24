def is_valid(arr, s, mapping):
    sum_val = 0
    for word in arr:
        val = 0
        for char in word:
            val = val * 10 + mapping.get(char, -1)
            if val == -1:
                return False
        sum_val += val
    target = 0
    for char in s:
        target = target * 10 + mapping.get(char, -1)
        if target == -1:
            return False
    return sum_val == target

def map_strings(arr, s, mapping, idx):
    if idx == len(arr):
        return is_valid(arr, s, mapping)

    for i in range(10):
        if i not in mapping.values():
            mapping[arr[idx][0]] = i
            if map_strings(arr, s, mapping, idx + 1):
                return True
            mapping[arr[idx][0]] = -1

    return False

def can_map_strings(arr, s):
    mapping = {char: -1 for word in arr for char in word}
    return map_strings(arr, s, mapping, 0)

# Example
arr = ["SEND", "MORE"]
s = "MONEY"
result = can_map_strings(arr, s)
if result:
    print("Yes")
else:
    print("No")
