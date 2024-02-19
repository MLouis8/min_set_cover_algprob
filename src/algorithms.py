import random

def naive_approx(u_size, S, s_size, seq):
    """
    implementation of a naive algo for solving minimum set cover problem

    Takes the biggest set that adds the most uncovered elements.
    If there are multiple max sized sets then choose one at random.


    Performs well on instance_1y and taking the smallest set performs well on instance_1x
    """
    cover = set() # set containing S_i
    cover_union = set()
    S =  list(S.items())
    for sigma_i in seq:
        if sigma_i in cover_union:
            break
        else:
            max_discovery = 0
            choose_S_i = []
            for i, S_i in enumerate(S):
                S_i = S_i[1]
                #print("sigma_i", sigma_i, "i", i,"S_i", S_i)
                if sigma_i in S_i:
                    #print("sigma_i in S_i:", sigma_i, S_i)
                    discovery_size = len(S_i) - len(S_i.intersection(cover_union))
                    if  discovery_size < max_discovery:
                        choose_S_i = [i]
                        max_discovery = discovery_size 
                    if discovery_size == max_discovery:
                        choose_S_i.append(i)

            cover.add(choose_S_i[0])
            #cover.add(random.choice(choose_S_i))
            cover_union.union(S[i][1])

    return cover
