import math
import json

# Util functions

def dot_product(v1, v2):
    return sum([v1[i] * v2[i] for i in range(len(v1))])

def magnitude(v):
    return math.sqrt(sum([math.pow(x, 2) for x in v]))

def load_model(file_path):
    with open(file_path, 'r') as file:
        dictionary = json.load(file)
    return dictionary

# Functions

def calculate_similarity(model, base_word, target_word):
    # Returns the cos of the angle between the two vectors
    # cos(theta) = (A . B) / (|A| * |B|), source: https://en.wikipedia.org/wiki/Cosine_similarity
    result = dot_product(model[base_word], model[target_word]) / (magnitude(model[base_word]) * magnitude(model[target_word]))
    result = round(result, 4)
    return result
    
# Пример
# Вход: model, 'bridge', ['car', 'man', 'arch']
# Изход: 'arch'
def find_most_similar_to_given(model, given_word, target_words):
    word = target_words[0]
    max_similarity = calculate_similarity(model, given_word, word)
    for target_word in target_words[1:]:
        similarity = calculate_similarity(model, given_word, target_word)
        if similarity > max_similarity:
            max_similarity = similarity
            word = target_word
    return word

# Пример
# Вход: model, ['lunch', 'breakfast', 'dinner', 'homework']
# Изход: 'homework'
def doesnt_match(model, given_words):
    word = given_words[0]
    min_similarity = sum([calculate_similarity(model, word, given_words[i]) for i in range(len(given_words)) if given_words[i] != word])
    for given_word in given_words[1:]:
        similarity = sum([calculate_similarity(model, given_word, given_words[i]) for i in range(len(given_words)) if given_words[i] != given_word])
        if similarity < min_similarity:
            min_similarity = similarity
            word = given_word
    return word
