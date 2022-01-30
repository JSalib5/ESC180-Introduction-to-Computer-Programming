import urllib.request

#problem 1 a 
def word_counts(w):
    words_dict = {}
    for i in w:
        words_dict.setdefault(i,0)
        words_dict[i] += 1
    return words_dict

#problem 1 b
def top10(L):
    L.sort(reverse=True)
    return L[:10]

#problem 1 c
def find_freq(w):
    words_count = word_counts(w)
    words_count_inv = {}
    for i in words_count:
        words_count_inv.setdefault(words_count.get(i), [])
        words_count_inv[words_count.get(i)] += [i]
    words_sorted = sorted(words_count_inv.items())
    return top10(words_sorted)

#problem 3
def results_finder(term):
    f = urllib.request.urlopen("https://ca.search.yahoo.com/search?p="+term+"&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8")
    page = f.read().decode("utf-8")
    start = page.find('referrerpolicy="unsafe-url">Next<ins></ins></a><span>') + len('referrerpolicy="unsafe-url">Next<ins></ins></a><span>')
    end = page.find('results', start)
    f.close()
    return page[start:end]

def choose_varient(variants):
    result1 = int(results_finder(variants[0].replace(" ", "+")).replace(",",""))
    result2 = int(results_finder(variants[1].replace(" ", "+")).replace(",",""))
    if result1 > result2:
        return variants[0]
    else:
        return variants[1]
    

if __name__ == '__main__':
    Pride_and_Prejudice = open("text.txt", encoding="latin-1").read().split()
    print(find_freq(Pride_and_Prejudice))
    print(choose_varient(["top ranked school uoft","top ranked school waterloo"]))
    
    