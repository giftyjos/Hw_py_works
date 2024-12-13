def lexical_order(n):
    def dfs(current):
        if current > n:
            return
        result.append(current)
        for i in range(10):
            next_num = current * 10 + i
            if next_num > n:
                return
            dfs(next_num)

    result = []
    for i in range(1, 10):
        dfs(i)

    return result


n = 13
print(lexical_order(n)) 
n = 2
print(lexical_order(n))  