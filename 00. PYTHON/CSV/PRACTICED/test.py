def run_length_encoding(input_list):
    res = []
    count = 1
    sub = input_list[0]
    for i in input_list[1:]:
        if i == sub:
            count+=1
        else:
            res.append([count,sub])
            sub = i
            count = 1

    res.append([count,sub])
    return res


original_list ="prasanna"
encoded_list = run_length_encoding(original_list)
print(encoded_list)  # Expected output: [[2, 1], [1, 2], [1, 3], [1, 4], [1, 4.3], [1, 5], [1, 1]]
