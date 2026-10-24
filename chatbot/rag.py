from pathlib import Path
from collections import Counter
import math


# Load agriculture knowledge
knowledge_path = Path("data/agriculture_knowledge.txt")

with open(knowledge_path, "r", encoding="utf-8") as file:
    knowledge = file.read()


# Split knowledge into sections
sections = knowledge.split("\n\n")

# Remove empty sections
sections = [section.strip() for section in sections if section.strip()]


def tokenize(text):
    """
    Convert text into simple lowercase words.
    """
    words = text.lower().split()

    cleaned_words = []

    for word in words:
        word = word.strip(".,!?;:()[]{}\"'")

        if word:
            cleaned_words.append(word)

    return cleaned_words


def cosine_similarity(text1, text2):
    """
    Calculate similarity between two pieces of text.
    """

    words1 = Counter(tokenize(text1))
    words2 = Counter(tokenize(text2))

    common_words = set(words1) & set(words2)

    numerator = sum(
        words1[word] * words2[word]
        for word in common_words
    )

    magnitude1 = math.sqrt(
        sum(value ** 2 for value in words1.values())
    )

    magnitude2 = math.sqrt(
        sum(value ** 2 for value in words2.values())
    )

    if magnitude1 == 0 or magnitude2 == 0:
        return 0

    return numerator / (magnitude1 * magnitude2)


def search_knowledge(question, number_of_results=2):

    scores = []

    for section in sections:

        score = cosine_similarity(
            question,
            section
        )

        scores.append(score)

    # Sort sections by similarity
    best_indexes = sorted(
        range(len(scores)),
        key=lambda index: scores[index],
        reverse=True
    )[:number_of_results]

    results = []

    for index in best_indexes:
        results.append(sections[index])

    return results