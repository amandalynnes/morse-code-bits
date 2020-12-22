#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Morse Code Decoder

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
"""
__author__ = 'Amanda Simmons, Pete M'
# https://stackoverflow.com/questions/2664150/counting-longest-occurrence-of-repeated-sequence-in-python

from morse_dict import MORSE_2_ASCII
import itertools

# count num of zeroes between words
# divide the num by 7


def decode_bits(bits):
    bits = bits.strip('0')
    num_ones = 99
    num_zeroes = 99
    if '1' in bits:
        num_ones = min(len(list(y)) for (c, y) in itertools.groupby(bits) if c == '1')
    if '0' in bits:
        num_zeroes = min(len(list(y)) for (c, y) in itertools.groupby(bits) if c == '0')
    transmission_rate = min(num_ones, num_zeroes)
    print(num_ones)
    print(bits)
    # transmission_rate = num_ones
    print(transmission_rate)
    # bit_test = bits.split('1')
    bit_words = bits.split('0'*(transmission_rate*7))
    decoded_letters = []
    for word in bit_words:
        letters = word.split('0'*(transmission_rate*3))
        for letter in letters:
            letter = letter.replace('1'*(transmission_rate*3), '-')
            letter = letter.replace('1'*transmission_rate, '.')
            letter = letter.replace('0'*transmission_rate, '')
            decoded_letters.append(letter)
        decoded_letters.append(' ')
    str_morse_characters = ' '.join(decoded_letters).strip()
    print(str_morse_characters)
    # print(bit_test)
    return str_morse_characters


def decode_morse(morse):
    morse_words = morse.split('   ')
    decoded_letters = []
    for word in morse_words:
        letters = word.split()
        for letter in letters:
            decoded_letters.append(MORSE_2_ASCII[letter])
        decoded_letters.append(' ')

    return ''.join(decoded_letters).strip()


if __name__ == '__main__':
    hey_jude_morse = ".... . -.--   .--- ..- -.. ."
    hey_jude_bits = "1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011" # noqa

    # Be sure to run all included unit tests, not just this one.
    print("Morse Code decoder test")
    print("Part A:")
    print(f"'{hey_jude_morse}' -> {decode_morse(hey_jude_morse)}")
    print()
    print("Part B:")
    print(f"'{hey_jude_bits}' -> {decode_morse(decode_bits(hey_jude_bits))}")

    print("\nCompleted.")
