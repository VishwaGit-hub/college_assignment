import re
from collections import Counter

def extract_keywords(text):
    text = text.lower().split("references")[0]

    words = re.findall(r'\b[a-z]{6,}\b', text)

    stopwords = {
        "method","result","paper","system","model",
        "using","based","different","analysis",
        "approach","performance","dataset"
    }

    filtered = [w for w in words if w not in stopwords]

    freq = Counter(filtered)
    return [w for w,_ in freq.most_common(10)]
