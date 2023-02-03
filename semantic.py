import spacy
nlp = spacy.load('en_core_web_md')


word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# What I found interesting about the similarities between cat, monkey and banana is that it recognized that
# monkeys eat banana, or at least it knows there is a strong link between the 2.
# I'm also surprised by the score of cat and banana that as no link from what I know. 0.22 seems high to me.
print('\n')
# MY EXAMPLE

word1 = nlp("wheel")
word2 = nlp("car")
word3 = nlp("bicycle")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
# I'm not sure if a note is required but the results are very surprising to me.
# Car and bicycle scores higher than wheel and bicycle. Bicycle and wheel actually scores less than car and wheel!!!

print('\n\n')

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
print('\n\n')



sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my cat in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)


# Here is my note about running the example file with the language model 'en_core_web_sm' as I didn't know where I had to write it.
# It gives me some scores but also tells me:
# "you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors."
# The result will then not be as precise and reliable as with the larger language model that was used before 'md'