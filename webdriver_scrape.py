import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def scrape_flashcards(lang_pairs: list[str]):
    """
        Uses Selenium to scrape flashcards from Reverso for each language pair.
        - lang_pairs: A list of query parameters specifying language pairs,
          e.g. ["languagePairs=en-ru&", "languagePairs=ru-en&"].

        Returns:
            A list of page-source fragments (in JSON form) for each language pair.
    """
    
    flashcards_page = "https://www.reverso.net/vocabulary?utm_source=context&utm_medium=button-below-search-bar-home-page"

    # --- Paths for Windows user "PC" ---
    # Adjust if you have a different username, Chrome path, or profile name.
    USER_DATA_DIR = r"C:\Users\PC\AppData\Local\Google\Chrome\User Data"
    PROFILE_DIR = "Default"

    chrome_options = Options()

    # Specify the user data directory
    chrome_options.add_argument(f"--user-data-dir={USER_DATA_DIR}")

    # Specify which profile folder to use
    chrome_options.add_argument(f"--profile-directory={PROFILE_DIR}")

    # Remove the "Chrome is being controlled by automated test software" bar
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    # Initialize the webdriver with these options
    driver = webdriver.Chrome(options=chrome_options)

    res = []
    for pair in lang_pairs:
        favourites_url = f"https://context.reverso.net/bst-web-user/user/favourites?{pair}order=10&start=0&length=50&includeSyn=YES&includeDef=YES"

        try:
            # 1. Go to the favorites page
            driver.get(favourites_url)
            time.sleep(1)  # wait for the page to load

            page_source = driver.page_source

            # 2. Check if the page source indicates a 403
            #    In some cases, a 403 page is very short or has specific text.
            #    Here, we just check if its length is 177, which apparently
            #    indicates a 403 (this is highly site-specific).
            if len(page_source) == 177:
                print("Received 403 Forbidden. Attempting to re-authenticate...")

                # 3. Go to Manage Account page to possibly refresh the session
                driver.get(flashcards_page)
                time.sleep(1)  # wait to ensure the session is refreshed or user is logged in

                # 4. Return to favourites page
                driver.get(favourites_url)
                time.sleep(1)

            final_page_source = driver.page_source[99:-64]
            res.append(final_page_source)

        except Exception as e:
            print("An error occurred:", e)
            driver.quit()

    driver.quit()
    return res
