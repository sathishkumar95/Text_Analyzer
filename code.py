def counter(text, char):
    count = 0
    for i in text:
        if i == char:
            count += 1
    return count


with open('text.txt') as f:
    text = f.read()
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for al in alpha:
        print("{0} count is {1}", al, counter(text, al))
