# Homework Vectors Assignment

## Purpose of the Project

The purpose of this project is to implement various functions that work with words, using a similarity measure between vectors. The project includes the following functions:

1. **calculate_similarity**: Calculates the similarity between two vectors using the cosine similarity formula.

2. **find_most_similar_to_given**: Finds the most similar word to a given word using the cosine similarity formula.

3. **doesnt_match**: Finds the word that doesn't match the others in a list of words.

4. **find_common_meaning**: Finds the word that has the same relationship to the third word as the first word has to the second word.

## Formulas Used

1. **Cosine Similarity**: Measures the cosine of the angle between two vectors.

    $$ \text{cosine similarity}(A, B) = \frac{A \cdot B}{\|A\| \|B\|} $$ 

    Source: [Wikipedia - Cosine Similarity](https://en.wikipedia.org/wiki/Cosine_similarity)

2. **Analogy**: Calculates D, when A is to B as C is to D.

    $$ D = B - A + C $$

    Source: [Wikipedia - Analogy](https://en.wikipedia.org/wiki/Analogy_(linguistics))

3. **Dot Product**: Calculates the dot product of two vectors.

    $$ A \cdot B = \sum_{i=1}^{n} A_i B_i $$

    Source: [Wikipedia - Dot Product](https://en.wikipedia.org/wiki/Dot_product)

4. **Magnitude**: Calculates the magnitude of a vector.

    $$ \|A\| = \sqrt{\sum_{i=1}^{n} A_i^2} $$

    Source: [Wikipedia - Euclidean Norm](https://en.wikipedia.org/wiki/Norm_(mathematics)#Euclidean_norm)

## Running the Tests

To run the tests, navigate to the project directory and use the following command:
```bash
python main.py
```
Alternatively, you can import the `tests` module and run the tests from there.

## Using the `tests` Module

The `tests` module contains all the necessary tests for the implemented functions. Here is an example of how to use it:

```python
import tests

tests.run_tests()
```

## Using the `src` Module

The `src` module contains all the necessary functions to work with words. Here is an example of how to use it:

```python
from src import *

model = load_model("homework_vectors_assignment/word_embeddings.json")

word1 = "king"
word2 = "queen

similarity = calculate_similarity(model, word1, word2) # result is from -1 to 1
print(f"The similarity between {word1} and {word2} is {similarity}")

word = "king"
words = ["queen", "prince", "dog", "car"]

most_similar = find_most_similar_to_given(model, word, words) # result is the most similar word
print(f"The most similar word to {word} is {most_similar}")

words = ["apple", "banana", "cherry", "dog"]

doesnt_match = doesnt_match(model, words) # result is the word that doesn't match the others
print(f"The word that doesn't match the others is {doesnt_match}")

word1 = "man"
word2 = "king"
word3 = "woman"

common_meaning = find_common_meaning(model, word1, word2, word3) # result is the word that has the same relationship to the third word as the first word has to the second word
print(f"The word that has the same relationship to {word3} as {word1} has to {word2} is {common_meaning}")
```
