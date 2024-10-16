from .homework_vectors_problem1 import calculate_similarity
from math import fabs


# Пример
# Вход: model, 'man', 'king', 'woman'
# Изход: 'queen'
#
# Пояснение: Връзката между 'man' и 'king' е същата като между 'woman' и 'queen'
def find_common_meaning(model, base_word, related_word, target_word):
    relation = calculate_similarity(model, base_word, related_word)
    key_list = list(model.keys())
    word = key_list[0]
    min_differece = fabs(relation - calculate_similarity(model, target_word, word))
    for key in key_list:
        if key != base_word and key != related_word and key != target_word:
            difference = fabs(relation - calculate_similarity(model, target_word, key))
            if difference < min_differece:
                min_differece = difference
                word = key
    return word
