# import src
import tests

# word1 = "human"
# word2 = "animal"

# model = src.load_model("homework_vectors_assignment/word_embeddings.json")
# print(src.calculate_similarity(model, word1, word2))

# word1 = "school"
# target_words = ["sky", "building", "road"]
# print(src.find_most_similar_to_given(model, word1, target_words))

# given_words = ["lunch", "breakfast", "dinner", "homework"]
# print(src.doesnt_match(model, given_words))

# word1 = "sky"
# word2 = "bird"
# target_word = "ocean"
# print(src.find_common_meaning(model, word1, word2, target_word))

tests.run_tests()