import pytest

from .. import src

@pytest.mark.parametrize("word1, word2, word3, expected", [("cat", "cats", "dog", "dogs"), ("life", "death", "black", "white"), ("sky", "bird", "ocean", "fish")])
def test_find_common_meaning(word1, word2, word3, expected):
    model = src.load_model("homework_vectors_assignment/word_embeddings.json")
    assert src.find_common_meaning(model, word1, word2, word3) == expected