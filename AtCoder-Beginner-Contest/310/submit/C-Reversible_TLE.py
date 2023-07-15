def count_unique_sticks(sticks):
    unique_sticks = [sticks[0]]
    for v in sticks:
        if v in unique_sticks or v[::-1] in unique_sticks:
            continue
        unique_sticks.append(v)
    return len(unique_sticks)
 
N = int(input())  
sticks = [input() for _ in range(N)]
result = count_unique_sticks(sticks)
print(result)
