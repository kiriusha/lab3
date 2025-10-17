import math
import collections
import matplotlib.pyplot as plt
import re


def clean_text(text):
    chars_to_remove = r'[@#$^&*{}\[\]<>/\\|=\+\-]'
    cleaned_text = re.sub(chars_to_remove, '', text)
    return cleaned_text


def calculate_entropy(text):
    char_count = collections.Counter(text)
    total_chars = len(text)

    entropy = 0
    for count in char_count.values():
        probability = count / total_chars
        entropy -= probability * math.log2(probability)

    return entropy, char_count, total_chars


def plot_histogram(char_count, total_chars, entropy):
    sorted_chars = char_count.most_common()

    characters = []
    frequencies = []

    for char, count in sorted_chars:
        if char == ' ':
            display_char = 'ПРОБЕЛ'
        else:
            display_char = char
        characters.append(display_char)
        frequencies.append(count)

    plt.figure(figsize=(15, 8))
    bars = plt.bar(characters, frequencies, color='skyblue', edgecolor='black')

    for bar, freq in zip(bars, frequencies):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + max(frequencies) * 0.01,
                 str(freq), ha='center', va='bottom', fontsize=8)

    plt.title(f'Гистограмма частоты символов\nЭнтропия: {entropy:.4f} бит/символ', fontsize=14, fontweight='bold')
    plt.xlabel('Символы', fontsize=12)
    plt.ylabel('Частота', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.show()


def analyze_text_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    cleaned_text = clean_text(text)
    entropy, char_count, total_chars = calculate_entropy(cleaned_text)

    plot_histogram(char_count, total_chars, entropy)


if __name__ == "__main__":
    analyze_text_file('lb1.txt')