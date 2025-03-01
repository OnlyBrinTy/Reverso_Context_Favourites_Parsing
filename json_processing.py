from webdriver_scrape import scrape_flashcards
import json
import html

# WARNING! The language preference is set to Russian (e. g. ru-en)

# Predefined lists of language pair query parameters
LANGUAGE_PAIRS = [[''], ['languagePairs=en-ru&', 'languagePairs=ru-en&'], ['languagePairs=nl-en&', 'languagePairs=en-nl&']]
CHOICE2IDX = {'': 1, '1': 2, '0': 0}


def main():
    """
    Prints out json data into the terminal.
    The output format is suited for Quizlet and Anki
    """
    print('Choose flashcards options:')
    print('ENTER: EN')
    print('1: NL')
    print('0: ALL')

    print()
    user_choice = input(' ---> ')

    lang = CHOICE2IDX[user_choice]
    lang_pairs = LANGUAGE_PAIRS[lang]
    for i, res in enumerate(scrape_flashcards(lang_pairs)):
        json_res = json.loads(res)

        # Extract results
        results = json_res["results"]

        for result in results:
            # The flashcards are based on context purely (use trgText and srcText for the word itself)
            q_c, a_c = result.get("trgContext", ''), result.get("srcContext", '')
            q_t, a_t = result.get("trgText", ''), result.get("srcText", '')

            if lang == 1 and result.get("trgLang", None) == 'en' or lang == 2 and result.get("trgLang", None) == 'nl':
                q_c, a_c = a_c, q_c
                q_t, a_t = a_t, q_t

            q = q_c if q_c else q_t
            a = a_c if a_c else a_t

            print(html.unescape(q).replace('em>', 'strong>'), end='\t')
            print(html.unescape(a).replace('em>', 'strong>'))


if __name__ == '__main__':
    main()
