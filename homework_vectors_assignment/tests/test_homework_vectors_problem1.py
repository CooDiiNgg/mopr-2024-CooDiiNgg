import pytest
from .. import src

@pytest.mark.parametrize("word1, word2, expected", [("cat", "dog", 0.9218), ("cat", "cat", 1.0), ("cat", "cats", 0.7865), ("human", "machine", 0.2991), ("human", "animal", 0.7725)])
def test_calculate_similarity(word1, word2, expected):
    model = src.load_model("homework_vectors_assignment/word_embeddings.json")
    assert src.calculate_similarity(model, word1, word2) == expected

@pytest.mark.parametrize("word1, target_words, expected", [("bridge", ["car", "man", "arch"], "arch"), ("school", ["sky", "building", "teacher"], "teacher"), ("school", ["sky", "building", "teacher", "student"], "student"), ("school", ["sky", "building", "road"], "building")])
def test_find_most_similar_to_given(word1, target_words, expected):
    model = src.load_model("homework_vectors_assignment/word_embeddings.json")
    assert src.find_most_similar_to_given(model, word1, target_words) == expected

@pytest.mark.parametrize("given_words, expected", [(["lunch", "breakfast", "dinner", "homework"], "homework"), (["lunch", "food", "dinner", "homework", "human"], "homework"), (["car", "machine", "plane", "animal"], "animal")])
def test_doesnt_match(given_words, expected):
    model = src.load_model("homework_vectors_assignment/word_embeddings.json")
    assert src.doesnt_match(model, given_words) == expected