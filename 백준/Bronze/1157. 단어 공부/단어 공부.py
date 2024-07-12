import string

def is_valid(alphabet_list):
    max_count = max(alphabet_list)
    if alphabet_list.count(max_count) != 1:
        return '?'
    else:
        return chr(alphabet_list.index(max_count)+ord("A"))

s = input()
s = s.upper()
alphabet_list = [0 for i in range(len(string.ascii_uppercase))]
for c in s:
    alphabet_list[ord(c) - ord('A')] += 1
print(is_valid(alphabet_list))