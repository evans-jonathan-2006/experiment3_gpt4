from input_module import get_blog_input
from blog_module import generate_blog
from title_module import generate_titles
from keyword_module import generate_keywords
from summary_module import generate_summary
from meta_module import generate_meta
from intent_module import detect_intent


def save_blog(blog):

    with open("outputs/generated_blog.txt", "w", encoding="utf-8") as file:
        file.write(blog)

    print("\nBlog saved successfully!")


def main():

    print("==============================================")
    print("       AI-POWERED BLOG CONTENT GENERATOR")
    print("==============================================")

    blog = ""
    topic = ""

    while True:

        print("\nMAIN MENU")
        print("----------------------------------------------")
        print("1. Generate Blog")
        print("2. Generate Blog Titles")
        print("3. Generate SEO Keywords")
        print("4. Generate Summary")
        print("5. Generate Meta Description")
        print("6. Detect User Intent")
        print("7. Exit")
        print("----------------------------------------------")

        choice = input("Enter your choice: ")

        if choice == "1":

            topic, style, tone, word_count = get_blog_input()

            blog = generate_blog(
                topic,
                style,
                tone,
                word_count
            )

            save_blog(blog)

        elif choice == "2":

            if blog == "":
                print("\nPlease generate a blog first.")
            else:
                generate_titles(topic)

        elif choice == "3":

            if blog == "":
                print("\nPlease generate a blog first.")
            else:
                generate_keywords(blog)

        elif choice == "4":

            if blog == "":
                print("\nPlease generate a blog first.")
            else:
                generate_summary(blog)

        elif choice == "5":

            if blog == "":
                print("\nPlease generate a blog first.")
            else:
                generate_meta(blog)

        elif choice == "6":

            user_input = input("\nEnter your request: ")

            intent = detect_intent(user_input)

            print("\nDetected Intent :", intent)

        elif choice == "7":

            print("\nThank you for using the Blog Generator!")
            break

        else:

            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()