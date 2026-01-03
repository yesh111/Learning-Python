# The process of manipulating and analyzing text data using programming.

text = "Python Programming"
print(text.upper())
print(text.lower())
print(text.title())

text = "       Hello Python     "
print(text.strip())

sentence = "Python is easy to learn"
words = sentence.split()
print(words)

words = ["Python", "is", "good"]
sentence = " ".join(words)

print(sentence)


text = "Python programming"

print("Python" in text)     # True
print(text.find("gram"))    # 10

text = "I like Java"
text = text.replace("Java", "Python")

print(text)

text = "Python is great. Python is dynamic."
count = 0
for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Vowels : ", count)