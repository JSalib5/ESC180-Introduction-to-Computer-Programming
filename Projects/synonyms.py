
import math

def norm(vec):   
    sum_of_squares = 0.0  
    for x in vec:
        sum_of_squares += vec[x] * vec[x]  
    return math.sqrt(sum_of_squares)


#PART A
def cosine_similarity(vec1, vec2):
    numerator = 0.0
    denominator = 0.0
    for i in vec1:
        for j in vec2:
            if i == j:
                numerator += vec1.get(i) * vec2.get(j)
    denominator = norm(vec1)*norm(vec2)
    return (numerator / denominator)


#PART B
def build_semantic_descriptors(sentences):
    small_boi = {}
    for i in range(len(sentences)):
        for j in range(len(sentences[i])):
            sentences[i][j] = sentences[i][j].lower()
        sentences[i] = list(set(sentences[i]))
    for i in range(len(sentences)):
        for j in range(len(sentences[i])):
            if sentences[i][j] in small_boi:
                for k in range(len(sentences[i])):
                    if sentences[i][k] in small_boi[sentences[i][j]] and sentences[i][k] != sentences[i][j]:
                        small_boi[sentences[i][j]][sentences[i][k]] += 1
                    elif sentences[i][k] != sentences[i][j]:
                        small_boi[sentences[i][j]][sentences[i][k]] = 1  
            else:                  
                smaller_boi = {}
                for k in range(len(sentences[i])):
                    if sentences[i][k] not in smaller_boi and sentences[i][k] != sentences[i][j]:
                        smaller_boi[sentences[i][k]] = 1        
                small_boi[sentences[i][j]] = smaller_boi    
    return small_boi


#PART C
def build_semantic_descriptors_from_files(filenames):
    text = ""
    for i in range(len(filenames)):
        f = open(filenames[i], "r", encoding="latin1")
        text += f.read()
    cur_text = ""
    for i in range(len(text)):
        if(text[i] == '\n' or text[i] == ',' or text[i] == '-' or text[i] == ':' or text[i] == ';'):
            cur_text += ' '
        elif(text[i] == '?' or text[i] == '!'):
            cur_text += '.'
        else:
            cur_text += text[i]
    sentences = [[word for word in sentence.split(' ') if word] for sentence in cur_text.split('.') if len(sentence) != 0]   
    return build_semantic_descriptors(sentences) 

#PART D
def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    values = []
    word_similarities = semantic_descriptors[word]
    for i in choices:
        if word in semantic_descriptors and i in semantic_descriptors:
            choice_similarities = semantic_descriptors[i]
            values.append(similarity_fn(word_similarities, choice_similarities))
        else:
            values.append(-1)
    return choices[values.index(max(values))]


#PART E
def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    numerator = 0.0
    f = open(filename)
    text = f.read()
    lines = text.split("\n")
    for i in range(len(lines)):
        if len(lines[i]) == 0:
            del lines[i]
    denominator = len(lines)
    words = [[]]*(len(lines))
    for i in range(len(lines)):
        words[i] = lines[i].split(" ")
    for i in range(len(words)):
        if most_similar_word(words[i][0], words[i][2:(len(words[i]))], semantic_descriptors, similarity_fn) == words[i][1]:
            numerator += 1
    return numerator / denominator * 100

  
if __name__ == '__main__':
    sem_descriptors = build_semantic_descriptors_from_files(["text1.txt","text2.txt"])
    