from api_client import get_post


def main():
    post = get_post(1)

    if post is None:
        print("Failed to retrieve post.")
        return

    print(post)


if __name__ == "__main__":
    main()