def solution(k, a, b):
    a.sort()
    b.sort(reverse=True)
    for i in range(k):
        a[i], b[i] = b[i], a[i]
    answer = sum(a)
    return answer


k = 3
a = [1,2,5,4,3]
b = [5,5,6,6,5]
answer = solution(k, a, b)
print(answer)
