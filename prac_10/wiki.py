import wikipedia


def main():
    """Prompt for page titles and show Wikipedia information."""
    wikipedia.set_lang("en")

    user_input = input("Enter page title: ")
    while user_input != "":
        try:
            page = wikipedia.page(user_input, autosuggest=False)
            print(page.title)
            print(page.summary)
            print(page.url)
        except wikipedia.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except wikipedia.PageError:
            print(f'Page id "{user_input}" does not match any pages. Try another id!')

        user_input = input("\nEnter page title: ")

    print("Thank you.")


if __name__ == "__main__":
    main()
