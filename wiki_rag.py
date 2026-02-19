import wikipedia

def fetch_wiki_context(keywords):

    context = ""

    for word in keywords[:5]:
        try:
            summary = wikipedia.summary(word, sentences=3)
            context += f"\n{word.upper()}:\n{summary}\n"
        except:
            pass

    return context
