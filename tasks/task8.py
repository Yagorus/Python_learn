def count_positives_sum_negatives(arr):
    result =[]
    if len(arr) != 0:
        result.append(len([count for count in arr if count > 0]))
        result.append(sum([neg for neg in arr if neg < 0]))
    return result

print(count_positives_sum_negatives([0, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
print(count_positives_sum_negatives([]))
print(count_positives_sum_negatives([0,0]))


def count_positives_sum_negatives2(arr):
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []


print(count_positives_sum_negatives2([0, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
print(count_positives_sum_negatives2([]))
print(count_positives_sum_negatives2([0,0]))
        

def count_positives_sum_negatives3(arr):
    return [len([x for x in arr if x > 0])] + [sum(y for y in arr if y < 0)] if arr else []