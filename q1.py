def solution(lottos, win_nums):
    rate = [6,6,5,4,3,2,1]
    answer = []
    good_match = 0
    match = 0
    
    for i in lottos:
        if i == 0:
            good_match += 1
        elif i in win_nums:
            match += 1
    
    answer = [rate[match+good_match], rate[match]]
    return answer
