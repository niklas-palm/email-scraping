import requests
from bs4 import BeautifulSoup
import re
import csv


def get_emails(urls, depth):
    # A set to store unique emails
    emails = set()
    # A set to store unique URLs to scrape
    urls_to_scrape = set()
    # A set to store unique URLs already scraped
    urls_scraped = set()

    # Adding the initial URLs to urls_to_scrape
    urls_to_scrape |= set(urls)

    # Looping over each depth level
    for i in range(depth):
        # A set to store unique URLs found on this depth level
        urls_on_this_level = set()

        # Looping over each URL on this level
        for url in urls_to_scrape:
            # Skip URLs that have already been scraped
            if url in urls_scraped:
                continue

            try:
                # Sending a GET request to the URL
                response = requests.get(url)
                # Parsing the HTML content using BeautifulSoup
                soup = BeautifulSoup(response.text, "html.parser")
                # Finding all email addresses on this page using regex
                email_addresses = set(
                    re.findall(
                        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", response.text
                    )
                )
                # Adding found email addresses to the main email set
                emails |= email_addresses

                # Finding all links on this page
                for link in soup.find_all("a"):
                    # Getting the href attribute of the link
                    href = link.get("href")
                    # Checking if the href attribute is a valid URL
                    if href is not None and href.startswith("http"):
                        # Adding the URL to urls_on_this_level
                        urls_on_this_level.add(href)

            except:
                # Ignore any errors and continue to the next URL
                pass

            # Adding this URL to urls_scraped
            urls_scraped.add(url)

        # Setting urls_to_scrape to urls_on_this_level for the next depth level
        urls_to_scrape = urls_on_this_level

    # Writing the emails to a CSV file
    with open("emails.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Emails"])
        for email in emails:
            writer.writerow([email])

    return emails


if __name__ == "__main__":

    with open("config.json") as f:
        config = json.load(f)

    emails = get_emails(config["urls"], config["depth"])

    print(f"found {len(emails)} emails")
