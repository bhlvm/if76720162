
def bad_char(pat):
    c = 256*[-1] 
    for j in range(len(pat)):
        c[ord(pat[j])] = j
    return c

def good_suffix(pat):
    return (len(pat)+1)*[1]

def boyer_moore(txt, pat, verbose=False):
    n, m = len(txt), len(pat)
    occ = []
    c = bad_char(pat)
    s = good_suffix(pat)
    i = 0
    while i <= n-m:
        j = m-1
        while j>=0 and pat[j]==txt[i+j]:
            j -= 1
        if verbose:
            print "%si=%d"%(i*" ",i)
            print "%s"%txt
            print "%s%s%s"%((i+j)*" ", "!" if j>=0 else " " , (m-j-1)*"=" )
            print "%s%s\n"%(i*" ",pat)
        if j<0:
            occ.append(i)
            i += s[0]
        else:
            i += max(s[j], j-c[ord(txt[i+j])])
    return occ



def main():
    txt="babcbabcabcaabcabcabcacabc"
    pat="abcabcacab"

    print boyer_moore(txt, pat, True)

    
if __name__ == "__main__":
    main()

