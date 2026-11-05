from utils import ask_ollama


def generate_keywords(blog):

    prompt = f"""
Analyze the following blog and generate SEO-friendly keywords.

Blog:
{blog}

Requirements:
- Generate 10 relevant keywords.
- Include short and long-tail keywords.
- Do not add explanations.
- Return keywords as a simple list.
"""

    result = ask_ollama(prompt)

    print("\nSEO Keywords")
    print("----------------------------------------")
    print(result)

    return result