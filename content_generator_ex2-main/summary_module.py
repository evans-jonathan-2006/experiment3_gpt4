from utils import ask_ollama


def generate_summary(blog):

    prompt = f"""
Summarize the following blog in approximately 100 words.

Blog:
{blog}

Requirements:
- Keep the important points.
- Use clear and simple language.
- Do not add information that is not present in the blog.
"""

    result = ask_ollama(prompt)

    print("\nSummary")
    print("----------------------------------------")
    print(result)

    return result