import re

def split_sections(text):

    sections = {}
    titles = ["abstract","introduction","method","results","conclusion"]

    lower = text.lower()

    for i, title in enumerate(titles):
        match = re.search(title, lower)
        if not match:
            continue

        start = match.start()
        end = len(text)

        for next_title in titles[i+1:]:
            nxt = re.search(next_title, lower)
            if nxt:
                end = nxt.start()
                break

        sections[title] = text[start:end]

    return sections
