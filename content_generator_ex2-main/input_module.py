def get_blog_input():

    print("\nEnter Blog Details")
    print("----------------------------------")

    topic = input("Enter Blog Topic : ")
    style = input("Writing Style : ")
    tone = input("Tone : ")
    word_count = input("Word Count : ")

    print("\n----------------------------------")
    print("Blog Topic :", topic)
    print("Style :", style)
    print("Tone :", tone)
    print("Words :", word_count)
    print("----------------------------------")

    return topic, style, tone, word_count