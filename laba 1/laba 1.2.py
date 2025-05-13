candidates = [2,5,2,1,2]
target = 5
result = []
def combination(comb, index, cur_sum):
    if cur_sum == target:
        result.append(list(comb))
        return
    if cur_sum > target:
        return
    for num in range(index, len(candidates)):
        combination(comb + [candidates[num]], num + 1, cur_sum + candidates[num])
candidates.sort()
combination([], 0, 0)
result = [list(combination) for combination in {tuple(combination) for combination in result}]
print(result)


