import nltk

# Ensure punkt resources are available
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)

sample_text = "Hello world! This is a test."
tokens = nltk.word_tokenize(sample_text.lower())
print(tokens)


