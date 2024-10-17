from .homework_vectors_problem1 import calculate_similarity
from math import fabs


# Пример
# Вход: model, 'man', 'king', 'woman'
# Изход: 'queen'
#
# Пояснение: Връзката между 'man' и 'king' е същата като между 'woman' и 'queen'
def find_common_meaning(model, base_word, related_word, target_word):
    # The connection between the base_word and the related_word is the same as between the target_word and the result
    # A is to B as C is to D => D = C + (B - A)
    # source: https://www.wikipedia.org/wiki/Analogy
    D = [model[target_word][i] + (model[related_word][i] - model[base_word][i]) for i in range(len(model[base_word]))]
    word_list = list(model.keys())
    max_similarity = -1
    result = ""
    for word in word_list:
        if word != base_word and word != related_word and word != target_word:
            similarity = calculate_similarity(model, word, D)
            if similarity > max_similarity:
                max_similarity = similarity
                result = word
    return result
