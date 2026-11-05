from utils import ask_ollama


def generate_titles(topic):

    prompt = f"""
Generate 5 attractive and engaging blog titles for the topic:

{topic}

Requirements:
- Generate exactly 5 titles.
- Make them interesting and professional.
- Avoid duplicate titles.
- Number the titles from 1 to 5.
"""

    result = ask_ollama(prompt)

    print("\nSuggested Titles")
    print("----------------------------------------")
    print(result)

    return result