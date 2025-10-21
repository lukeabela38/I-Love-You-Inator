import random
from app.config import Constants

def generate_random_number() -> int:
    return random.randrange(0, Constants.HOW_MANY_DAYS_BETWEEN_EMAILS.value)

def does_she_get_an_email(comparison_number: int, generated_number: int) -> bool:
    if comparison_number == generated_number:
        return True
    return False

def main() -> int:
    random_number = generate_random_number()
    she_gets_an_email = does_she_get_an_email(Constants.COMPARISON_NUMBER.value, random_number)
    if she_gets_an_email:
        print("She gets an email!")
    else:
        print("She doesn't get an email!")

    return 0;

if __name__ == "__main__":
    main()