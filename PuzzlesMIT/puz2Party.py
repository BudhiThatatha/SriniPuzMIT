## Given a set of subsets, maximize the conjunction of a subset of a element and all the subsets.

##Declaring the subsets
import operator
beyonce, taylor, brad, katy, tom, drake, alicia = set(), set(), set(), set(), set(), set(), set()

beyonce = set(range(6,7))
taylor = taylor.union((7,8))
brad = {10}
katy = katy.union((10, 11))
tom = tom.union((8,9))
drake = set([9,10,11])
alicia = alicia.union((6,7))

##Set of all sets

S = [beyonce, taylor, brad, katy, tom, drake, alicia]

## The maximum subset on S

def best(S):

    Union = set()
    count = {}
    
    for st in S:
        Union = set.union(Union,st) ## We have all possible hours, now

    for st in S:                   ## We selet a set "st" in S, that is, a Celebrity
        for hr in Union:           ## we, then, take a given time in the set "Union", of all times of the party with Celebrities

           if hr in st:                                 ##If the "hr" is in the Celebrity Schedule's, then, we count
               previous_count = count.get(hr,0)         ##Debugger if the hr count of celebrities is zero
               count[hr] = previous_count + 1        

               print(count.items())                         ## Watching the process from Beyonce, Taylor, Brad, ...,  Alicia order.
           else:
               print('no ', hr,' in ',st)
               
        print('The best hour to party is: ', max(count.items(), key=operator.itemgetter(1)))    ##Finally, we get our anwser of the Best Hour to Party, with the max of celebrities.
        ##if you don't want to import, we can do
        ##inverse = [(value, key) for key, value in count.items()]
        ##print max(inverse)
        
