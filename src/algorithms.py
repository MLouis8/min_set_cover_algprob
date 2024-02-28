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
    compare = lambda a, b: a < b if min else lambda a, b: a > b
    choice = lambda x: random.choice(x) if rdm else lambda x: x[0]
    cover = set() # set containing S_i
    cover_union = set()
    S = list(S.items())
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
            chosen = choice(choose_S_i)
            cover.add(chosen)
            cover_union.union(S[chosen][1])
    return cover

def full_random_approx(S, seq):
    """
    Online approximation that solves minimum set cover problem by taking a radom set
    among the ones containing the current element of the sequence
    
    Keyword arguments:
    S   -- the collection of sets
    seq -- the sequence to cover
    """
    cover = set()
    cover_union = set()
    S = list(S.items())
    for sigma_i in seq:
        if sigma_i in cover_union:
            break
        else:
            choose_S_i = []
            for i, S_i in enumerate(S):
                S_i = S_i[1]
                if sigma_i in S_i:
                    choose_S_i.append(i)
            chosen = random.choice(choose_S_i)
            cover.add(chosen)
            cover_union.union(S[chosen][1])
    return cover

def lognlogm(S, seq):
    """
    Implements Alon, Noga, Baruch Awerbuch, Yossi Azar, and Niv Buchbinder. “The Online Set Cover Problem,” n.d.
    """
    correct_run=True

    S = list(S.items())
    cover = set()
    cover_union = set()
    weight = dict()
    universe = set()

    for s in S:
        universe = universe.union(s[1])

    for s in S:
        weight[s[0]] = 1/(2 * len(S))

    def update_element_weights(weight):
        for j in universe:
            weight[j] = 0
            for s in S:
                if j in s[1]:
                    weight[j] = weight[j]+weight[s[0]]

    def phi(weight, cover_union):
        res = 0
        for j in (universe - cover_union):
            #print("u", universe,"c", cover,"u-c", universe-cover)
            res += pow(len(universe),2*weight[j])
        return res

    update_element_weights(weight)
    for sigma_i in seq:
        if weight[sigma_i] >=1:# and sigma_i in cover_union:
            pass
        else:
            old_phi = phi(weight, cover_union)
            
            k =  math.ceil(math.log(1/weight[sigma_i])/math.log(2))
            if math.pow(2,k)*weight[sigma_i] <1:
                print("shit")
            if not math.pow(2,k-1)*weight[sigma_i] <1:
                print("shit2")
            #print(math.pow(2,k)*weight[sigma_i])
            for s_name, s in S:
                if sigma_i in s:
                    weight[s_name] = math.pow(2, k) * weight[s_name]
            update_element_weights(weight)

            chosen = 0
            
            options = []
            for i,S_i in enumerate(S):
                S_i = S_i[1]
                
                if sigma_i in S_i:
                    options.append(i)
                
            cover_union_copy = cover_union.copy()
            cover_copy = cover.copy()

            while(phi(weight, cover_union) > old_phi):
                success = False
                chosen = 0
                while(chosen < (4* math.log(len(universe)))):
                    c = random.choice(options)
                    cover.add(c)
                    cover_union = cover_union.union(S[c][1])
                    chosen +=1

                    if phi(weight, cover_union) <= old_phi:
                        success =True
                        break
                if success:
                    break
                else:
                    cover = cover_copy.copy()
                    cover_union = cover_union_copy.copy()
           
           
                    
        def in_cover(sigma):
            in_c = False
            for c in cover:
                if sigma in S[c][1]:
                    in_c = True
            if in_c:
                if sigma not in cover_union:
                    in_c=False

            return in_c
        if not in_cover(sigma_i):
            correct_run=False
    if not correct_run:
        print("Warning incorrect run.")
    # else:
    #     print("Yay!")
    return cover
