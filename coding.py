def union(A,B):
    U = []
    [U.append(x) for x in A if x not in U]
    [U.append(x) for x in B if x not in U]
    return U

def intersection(A,B):
    I = []
    [I.append(x) for x in A if x in B and x not in I]
    return I
    
def set_diff(A,B):
    D = []
    [D.append(x) for x in A if x not in B and x not in D]
    return D

def symm_diff(A,B):
    u = union(A,B)
    i = intersection(A,B)
    return set_diff(u,i)

def cartes_prod(A,B):
    P = []
    [P.append((x,y)) for x in A for y in B if (x,y) not in P]
    return P


print union([1,2,3,5,5,7],[2,4,4,5,10,11])
print intersection([8,9,3,5,2,2],[4,6,10,3,3,8])
print set_diff([8,9,3,5,2,2],[4,6,10,3,3,8])
print symm_diff([1,2,3],[2,3,4])
print cartes_prod([2,'white'],[9,'red',67,'tom','tom'])
