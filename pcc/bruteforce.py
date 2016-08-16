def brute_force(txt, pat, verbose=False):
    n, m  = len(txt), len(pat)
    occ = []
    i = 0
    while i <= (n-m) :
        j = 0
        while j<m and pat[j]==txt[i+j]:
            j += 1
        if verbose:
            print "%si=%d"%(i*" ",i)
            print "%s"%txt
            print "%s%s%s"%(i*" ", j*"=","!" if j<m else "" )
            print "%s%s\n"%(i*" ",pat)
        if j==m:
            occ.append(i)
        i += 1
    return occ



def main():
    txt="babcbabcabcaabcabcabcacabc"
    pat="abcabcacab"
    occ = brute_force(txt, pat, True)
    

if __name__ == "__main__":
    main()
