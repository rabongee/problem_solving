def stack(words):
    new_list = []
    brackets = {
        ")":"(",
        "}":"{",
        "]":"["
    }
    open_brac="({["
    for word in words:
        if word in open_brac:
            new_list.append(word)
        else:
            if not new_list:
                return "NO"
            elif brackets[word] != new_list.pop():
                return "NO"
    return "YES" if not new_list else "NO"

n = int(input())
word_list = []
for i in range(n):
    word_list.append(input())
for word in word_list:
    print(stack(word))