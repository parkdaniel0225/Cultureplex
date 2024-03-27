import sys
sys.path
import pandas as pd
import wikipediaapi
import time

def get_intro(page_title):
    """Fetch the introductory section of a Wikipedia page."""
    try:
        page = wiki_lang.page(page_title)
        return page.summary
    except Exception as e:
        print(f"Error fetching page for {page_title}: {e}")
        return None

if __name__ == "__main__":
    # Load the data from your CSV file
    data = pd.read_csv(r'C:\Users\parkd\OneDrive\Desktop\cultureplex/3.csv')

    # Configure the Wikipedia API with your user agent string
    wiki_lang = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI,
        user_agent='User:parkd'
    )

    # Start the timer
    start_time = time.time()

    # Apply the function to all rows in your DataFrame
    data['biography'] = data['page_title'].apply(get_intro)

    # Stop the timer and calculate the elapsed time
    elapsed_time = time.time() - start_time
    print(f"Time taken: {elapsed_time:.2f} seconds")

    # Save the updated data to a new CSV file on your desktop
    data.to_csv(r'C:\Users\parkd\OneDrive\Desktop\cultureplex\uFINAL_copy.csv', index=False)
