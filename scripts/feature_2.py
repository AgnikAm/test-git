"""A very basic word replacement script for testing."""


def replace_word(text, old_word, new_word):
	return text.replace(old_word, new_word)


if __name__ == "__main__":
	text = input("Text: ")
	old_word = input("Word to replace: ")
	new_word = input("Replacement: ")
	print(replace_word(text, old_word, new_word))
