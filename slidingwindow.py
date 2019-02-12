import collections
def findAnagrams(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    lp = len(p)
    cp = collections.Counter(p)
    count = lp
    ans = []
    for i in xrange(0, len(s)):
        print cp
        
        if cp[s[i]] >= 1:
            count -= 1
        cp[s[i]] -= 1
        if i >= lp:
            if cp[s[i-lp]] >= 0:
                count += 1
            cp[s[i-lp]] += 1
        if count == 0:
            ans.append(i-lp+1)
    return ans

s= "cbaebabacd"
p = "abc"

print findAnagrams(s,p)