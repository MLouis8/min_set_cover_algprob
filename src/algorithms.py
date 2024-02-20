import random
import math

def naive_approx(S, seq, min=False, rdm=True):
    """
    Online approximation that solves minimum set cover problem by taking the set that adds the most uncovered elements.
    
    Keyword arguments:
    S   -- the collection of sets
    seq -- the sequence to cover
    min -- selects the smallest set (default False)
    rdm -- select a random set among the best (default True)

    Comments:
    Performs well on instance_1y and taking the smallest set performs well on instance_1x
    """
    if min:
        compare = lambda a, b: a < b
    else:
        compare = lambda a, b: a > b
    if rdm:
        choice = lambda x: random.choice(x)
    else:
        choice = lambda x: x[0]
    cover = set() # set containing S_i
    cover_union = set()
    S =  list(S.items())
    for sigma_i in seq:
        if sigma_i in cover_union:
            break
        else:
            max_discovery = math.inf if min else 0 
            choose_S_i = []
            for i, S_i in enumerate(S):
                S_i = S_i[1]
                #print("sigma_i", sigma_i, "i", i,"S_i", S_i)
                if sigma_i in S_i:
                    #print("sigma_i in S_i:", sigma_i, S_i)
                    discovery_size = len(S_i) - len(S_i.intersection(cover_union))
                    if compare(discovery_size, max_discovery):
                        choose_S_i = [i]
                        max_discovery = discovery_size 
                    if discovery_size == max_discovery:
                        choose_S_i.append(i)

            cover.add(choice(choose_S_i))
            cover_union.union(S[i][1])

    return cover
