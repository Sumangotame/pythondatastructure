sentence="this is a sentence"
arrayed_sentence=sentence.split()
print(arrayed_sentence)
letter_counts = {}
for a in arrayed_sentence:
    for b in a:
        if b in letter_counts:
            letter_counts[b] += 1
        else:
            letter_counts[b] = 1
max_count=max(letter_counts.values())
max_letters=[ letter for letter,count in letter_counts.items() if count==max_count]


print(f"the character with highest count are: { ' ,'.join(max_letters)}:{max_count} ")


