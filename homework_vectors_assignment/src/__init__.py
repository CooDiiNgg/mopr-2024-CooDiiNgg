from . import homework_vectors_problem1
from . import homework_vectors_problem2
import os

def calculate_similarity(model, base_word, target_word):
    return homework_vectors_problem1.calculate_similarity(model, base_word, target_word)

def find_most_similar_to_given(model, given_word, target_words):
    return homework_vectors_problem1.find_most_similar_to_given(model, given_word, target_words)

def doesnt_match(model, given_words):
    return homework_vectors_problem1.doesnt_match(model, given_words)

def find_common_meaning(model, base_word, related_word, target_word):
    return homework_vectors_problem2.find_common_meaning(model, base_word, related_word, target_word)

def load_model(file_path):
    file_path = "../../" + file_path
    file_path = os.path.join(os.path.dirname(__file__), file_path)
    file_path = os.path.abspath(file_path)
    return homework_vectors_problem1.load_model(file_path)

