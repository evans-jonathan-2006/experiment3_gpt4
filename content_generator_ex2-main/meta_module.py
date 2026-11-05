from utils import ask_ollama


def generate_meta(blog):

    prompt = f"""
Create an SEO-friendly meta description for the following blog.

Blog:
{blog}

Requirements:
- Maximum 160 characters.
- Attractive and informative.
- Include important keywords.
- Return only the meta description.
"""

    result = ask_ollama(prompt)

    print("\nMeta Description")
    print("----------------------------------------")
    print(result)

    return result