#[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
ol = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
result = []
sub = [ol[0]]
for i in ol[1:]:
    if i == sub[-1]:
        sub.append(i)
    else:
        result.append(sub)
        sub = [i]
print(result)
