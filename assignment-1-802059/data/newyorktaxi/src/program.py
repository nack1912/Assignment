from colorama import Fore
import program_hosts
import data.mongo_setup as mongo_setup


def main():
    mongo_setup.global_init()

    print_header()

    program_hosts.run()


def print_header():

    print(Fore.WHITE + '****************  taxi New York city  ****************')
    print()
    print("Welcome to taxi app!")
    print("Why are you here?")
    print()


def find_user_intent():
    print("[g] Book a cage for your snake")
    print("[h] Offer extra cage space")
    print()
    choice = input("Are you a [g]uest or [h]ost? ")
    if choice == 'h':
        return 'offer'

    return 'book'


if __name__ == '__main__':
    main()
