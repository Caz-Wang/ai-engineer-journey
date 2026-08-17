import logging

from config import APP_ENV, APP_NAME


def main():
    logging.basicConfig(level=logging.INFO)

    logging.info("Application: %s", APP_NAME)
    logging.info("Environment: %s", APP_ENV)


if __name__ == "__main__":
    main()