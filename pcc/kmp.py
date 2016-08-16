"""
computa o comprimento da borda do prefixo 
pat[:j] por forca bruta
"""
def brd(pat, j):
    if j==0:
        return -1
    i = j-1
    while i>=0:
        if pat[:i] == pat[j-i:j]:
            return i
        i -= 1


"""
computa o comprimento da borda estrita do prefixo 
pat[:j] por forca bruta
"""
def sbrd(pat, j):
    if j==len(pat):
        return brd(pat, j)
    i = j-1
    while i>=0:
        if pat[:i] == pat[j-i:j] and pat[i]!=pat[j]:
            return i
        i -=1
    return -1


"""
computa o vetor dos comprimentos das bordas de 
pat[:j] para j=0,...,m=len(pat)
por forca-bruta
"""
def init_brd_bf(pat):
    return [brd(pat,j) for j in range(0,len(pat)+1)]


"""
computa o vetor dos comprimentos das bordas estritas de 
pat[:j] para j=0,...,m=len(pat)
por forca-bruta
"""
def init_sbrd_bf(pat):
    return [sbrd(pat,j) for j in range(0,len(pat)+1)]



"""
computa o vetor dos comprimentos das bordas de 
pat[:j] para j=0,...,m=len(pat)
utilizando o algoritmo kmp(pat, pat)
"""
def init_brd(pat, verbose=False):
    m  = len(pat)
    nxt = (m+1)*[0]
    nxt[0]=-1
    i,j = 1,0
    computed_borders = 2
    while i < m :
        old_j = j
        while i+j<m and pat[j]==pat[i+j]:
            j += 1
            nxt[i+j] = j
            computed_borders += 1
        if verbose:
            print "%si=%d"%(i*" ",i)
            print "%s"%pat
            print "%s%s%s%s"%(i*" ", old_j*".",(j-old_j)*"=","!" if i+j<m else "" )
            print "%s%s"%(i*" ",pat)
            print "=> nxt=",nxt[:i+j]
            print
        i += j - nxt[j]
        j = max(0,nxt[j])
    return nxt


"""
computa o vetor dos comprimentos das bordas estritas de 
pat[:j] para j=0,...,m=len(pat)
utilizando o algoritmo kmp(pat, pat)
"""
def init_sbrd(pat, verbose=False):
    m  = len(pat)
    nxt = (m+1)*[-1]
    if m==1 or (m>0 and pat[0]!=pat[1]):
        nxt[1] = 0
    i,j = 1,0
    computed_borders = 2
    while i < m :
        old_j = j
        while i+j<m and pat[j]==pat[i+j]:
            j += 1
            if i+j==m or (pat[j] != pat[i+j]):
                nxt[i+j] = j
                computed_borders += 1
            else:
                nxt[i+j] = nxt[j]
                computed_borders += 1
        if j==0:
            if pat[0] != pat[i+1]:
                nxt[i+1] = 0
            computed_borders += 1
        if verbose:
            print "%si=%d"%(i*" ",i)
            print "%s"%pat
            print "%s%s%s%s"%(i*" ", old_j*".",(j-old_j)*"=","!" if i+j<m else "" )
            print "%s%s"%(i*" ",pat)
            print "=> nxt=",nxt[:computed_borders]
            print
        i += j - nxt[j]
        j = max(0,nxt[j])
    return nxt


"""
retorna as posicoes das ocorrencias de pat em txt
usando o algoritmo KMP(1977)
"""
def kmp(txt, pat, verbose=False):
    n, m  = len(txt), len(pat)
    occ = []
    nxt = init_sbrd(pat, verbose)
    i,j = 0,0
    while i <= (n-m):
        old_j = j
        while j<m and pat[j]==txt[i+j]:
            #print "%s|"%((i+j)*" ")
            j += 1
        if verbose:
            print "%si=%d"%(i*" ",i)
            print "%s"%txt
            print "%s%s%s%s"%(i*" ", old_j*".",(j-old_j)*"=","!" if j<m else "" )
            print "%s%s\n"%(i*" ",pat)
        if j==m:
            occ.append(i)
        i += j - nxt[j]
        j = max(0,nxt[j])
    return occ



def main():
    txt = "abracadabra"
    pat = "abra"
    txt="babcbabcabcaabcabcabcacabc"
    pat="abcabcacab"

    print init_brd(pat)
    print init_brd_bf(pat)

    print init_sbrd(pat)
    print init_sbrd_bf(pat)
    
    #occb = brute_force(txt, pat)
    occk = kmp(txt, pat, True)
    #print occb
    #print occk
    


if __name__ == "__main__":
    main()
