from random import choice


def get_jokes(time, repeat_words=True):
    """ Composes "jokes" from random words from lists """

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    joke = []
    jokes = []

    if repeat_words:
        nouns_copy = nouns[:]
        adverbs_copy = adverbs[:]
        adjectives_copy = adjectives[:]

        while time != 0:
            word_1 = choice(nouns_copy)
            word_2 = choice(adverbs_copy)
            word_3 = choice(adjectives_copy)
            joke.append(word_1)
            joke.append(word_2)
            joke.append(word_3)
            time -= 1
            jokes.append(' '.join(joke))

            nouns_copy.remove(word_1)
            adverbs_copy.remove(word_2)
            adjectives_copy.remove(word_3)

            joke = []
        print(jokes)

    else:
        while time != 0:
            joke.append(choice(nouns))
            joke.append(choice(adverbs))
            joke.append(choice(adjectives))
            time -= 1
            jokes.append(' '.join(joke))
            joke = []
        print(jokes)


get_jokes(5)
get_jokes(5)
get_jokes(5)
get_jokes(5, False)
