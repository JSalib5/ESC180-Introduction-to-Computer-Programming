
#problem 2
def dict_to_str(d):
    dictionary_string = " "
    for i in range(len(list(d.keys()))):
        dictionary_string += str(list(d.keys())[i])+","+str(list(d.values())[i])+"\n"


#problem 3
def dict_to_str_sorted(d):
    sorted_keys = sorted(list(d.keys()))
    for key in sorted_keys:print(key,",",d[key],"\n")

#problem 4 c
def vowel_finder(word, d1, d2):
    codes = d1.get(word)
    phones = list(d2.keys())
    means = list(d2.values())
    vowels = []
    phone = d1[word]
    vowel_count = 0
    for i in phone:
        if d2[i] == 'vowel':
            vowel_count += 1
    '''
    for i in range(len(means)):
        if means[i] == "vowel":
            vowels.append(phones[i])

    for i in range(len(codes)):
        for j in range(len(vowels)):
            for k in range(9):
                if codes[i] == (vowels[j] + str(k)):
                    vowel_count += (k+1)
    '''
    return vowel_count

if __name__ == '__main__':

    #problem 1
    f = open("data2.txt")
    text = f.read()
    print(text)
    lines = text.split("\n")
    text_lowercase = text.lower()
    lines_lowercase = text_lowercase.split("\n")
    for i in range(len(lines_lowercase)):
        if lines_lowercase[i].find("lol") > -1:
            print(lines[i])

    dict_to_str({1:2, 0:3, 10:5})

    #problem 4 a
    f = open("dict_file.txt")
    text = f.read()
    lines = text.split("\n")
    dictionary = {}
    for i in range(len(lines)):
        small_list = lines[i].split("  ")
        dictionary[small_list[0]] = small_list[1].split(" ")
    print(dictionary['WATER'])
    #problem 4 b
    g = open("phones.txt")
    text2 = g.read()
    lines2 = text2.split("\n")
    distinctions = {}
    for i in range(len(lines2)):
        small_list2 = lines2[i].split("\t")
        distinctions[small_list2[0]] = small_list2[1]

    print(vowel_finder("CAR", dictionary, distinctions))

