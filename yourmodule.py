def rank(scores):
    # avg_scores = []
    # for i in scores:
    #     avg_scores.append(sum(i)/len(i))
    # avg_scores = list(map(lambda x : sum(x)/len(x), scores)) # 람다
    avg_scores = [sum(i)/len(i) for i in scores] # 리스트 컴프리헨션
    rank_scores = sorted(avg_scores, reverse=True)
    # rst = []
    # for score in avg_scores:
    #     rst.append(rank_scores.index(score)+1)
    # rst = list(map(lambda x : rank_scores.index(x) + 1, avg_scores))
    rst = [(rank_scores.index(s)+1) for s in avg_scores] # 리스트 컴프리헨션
    return rst 


def is_prime_num(num_list):
    result = []
    for num in num_list: 
        isprime = True
        for i in range(2, num):
            if num % i == 0:
                isprime = False
                break
        result.append(isprime)
    return result


