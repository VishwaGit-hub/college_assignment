def build_context(sections, wiki_context):

    context = "RESEARCH PAPER:\n"

    for name, content in sections.items():
        context += f"\n[{name.upper()}]\n"
        context += content[:2000]

    context += "\n\nBACKGROUND KNOWLEDGE (Wikipedia):\n"
    context += wiki_context

    return context
