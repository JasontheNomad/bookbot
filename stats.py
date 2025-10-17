def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    count = {}
    for ch in text:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1
    return count

def sorted_list(items):
    result = []
    for ch, count in items.items():
        if ch.isalpha():
            result.append({"char": ch, "num": count})

    def sort_on(d):
        return d["num"]

    result.sort(reverse=True, key=sort_on)
    return result