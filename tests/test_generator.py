import unittest

from buzz import generator


def test_sample_single_word():
    words = ('foo', 'bar', 'foobar')
    word = generator.sample(words)
    assert word in words


def test_sample_multiple_words():
    words = ('foo', 'bar', 'foobar')
    word = generator.sample(l, 2)
    assert len(words) == 2
    assert word[0] in words
    assert word[1] in words
    assert word[0] is not word[1]


def test_generate_buzz_of_at_least_five_words():
    phrase = generator.generate_buzz()
    assert len(phrase.split()) >= 5
