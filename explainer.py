from llm import get_llm
from langchain_core.prompts import PromptTemplate

template = """
You are a university professor who explains difficult research papers clearly.

The student is an undergraduate in computer science.
They want understanding, not oversimplification.

IMPORTANT:
• First give intuition
• Then give the correct technical explanation
• Keep clarity but DO NOT remove real concepts
• You may use proper terms, but always explain them

Write clean, readable notes using headings and bullet points.

----------------------------------

FORMAT:

1) PREREQUISITES
What background knowledge is required (brief explanations)

2) KEY TERMS (Explain in simple words but keep technical meaning)
For each:
Term:
Technical meaning:
Simple intuition:

3) THE PROBLEM THE PAPER SOLVES
Explain the research problem and why it matters.

4) CORE IDEA (INTUITIVE)
Explain the idea conceptually in plain language.

5) CORE IDEA (TECHNICAL)
Now explain the actual mechanism:
- algorithm
- model
- mathematical idea
- workflow
Do NOT skip real workings.

6) STEP-BY-STEP HOW IT WORKS
Numbered steps of the method or algorithm.

7) REAL WORLD ANALOGY
One analogy that matches the mechanism.

8) RESULTS / CONTRIBUTION
What new thing did the authors achieve?

9) KEY TAKEAWAYS
Concise revision points.

----------------------------------

Content:
{context}
"""

def generate_notes(context):
    llm = get_llm()
    prompt = PromptTemplate.from_template(template)
    chain = prompt | llm
    return chain.invoke({"context": context}).content
