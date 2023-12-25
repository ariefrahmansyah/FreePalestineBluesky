import os

from atproto import Client, client_utils


def main():
    BSKY_USERNAME = os.getenv("BSKY_USERNAME")
    BSKY_PASSWORD = os.getenv("BSKY_PASSWORD")

    client = Client()
    client.login(BSKY_USERNAME, BSKY_PASSWORD)

    text = client_utils.TextBuilder().text("🇵🇸 #FreePalestine")
    client.send_post(text)


if __name__ == "__main__":
    main()
