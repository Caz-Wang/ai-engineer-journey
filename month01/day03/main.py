import logging

from calculator import add, subtract, multiply, divide


def main():
    logging.basicConfig(level=logging.INFO)

    a = 10
    b = 5

    logging.info("Addition: %s", add(a, b))
    logging.info("Subtraction: %s", subtract(a, b))
    logging.info("Multiplication: %s", multiply(a, b))
    logging.info("Division: %s", divide(a, b))


if __name__ == "__main__":
    main()