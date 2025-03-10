corpus = """Project Gutenberg EBooks, Google Books Ngrams, and arXiv Bulk Data Access. There are many text corpora from newswire. Random's"""
long_corpus = """Introduction
Natural Language Processing (NLP) is a field of machine learning where models learn to understand and derive meaning from human languages. NLP transforms unstructured data, like text and speech, into a structured format that can be used in classification tasks, summarization, machine translation, sentiment analysis, and many other applications.
Training models to perform these tasks requires large amounts of data. The more capable you want your model to be, the more data it needs. Fortunately, repositories like Hugging Face, Kaggle, GitHub, and Papers with Code offer vast, varied datasets that are readily available for public use.
In this post, we've compiled 20 of the most popular NLP datasets, categorized into general NLP tasks, sentiment analysis, text-based tasks, and speech recognition. We also explore the key criteria for selecting the ideal dataset for your project.
"""
# Words by type
inflected_forms = ["playing", "played", "plays", "player", "running", "runner", "runs", "walked", "walking"]
plurals = ["cats", "dogs", "boxes", "flies", "babies", "leaves", "wolves"]
prefixes = ["undo", "undone", "unlikely", "disconnected", "misaligned", "pretest"]
suffixes = ["happiness", "quickly", "carefulness", "nationalization", "arguing", "organization"]
derived_words = ["enjoying", "enjoyment", "beautiful", "beautify", "beautifully"]
irregulars = ["went", "gone", "goes", "better", "best", "children", "feet", "mice"]
others = ["History", "eat", "ate", "eaten", "eats", "eating",
               "History", "historical", "historically", "historian",
               "historians", "histories", "history", "history's", "unhistorical", "unhistorically", "Congratulation"
               ]

# Final list
all_words = inflected_forms + plurals + prefixes + suffixes + derived_words + irregulars + others

# stemming
stemming_regex = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$'
stemming_min = 4
