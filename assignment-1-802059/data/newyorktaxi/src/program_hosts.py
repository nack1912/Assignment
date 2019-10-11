import datetime
from colorama import Fore
from dateutil import parser

from infrastructure.switchlang import switch
import infrastructure.state as state
import services.data_service as svc


def run():
    print(' ****************** Welcome driver **************** ')
    print()

    show_commands()

    while True:
        action = get_action()

        with switch(action) as s:
            s.case('c', create_account)
            s.case('a', create_account)
            s.case('l', log_into_account)
            s.case('y', list_trips)
            s.case('r', register_trip)
            s.case(['x', 'bye', 'exit', 'exit()'], exit_app)
            s.case('?', show_commands)
            s.case('', lambda: None)
            s.default(unknown_command)

        if action:
            print()

        if s.result == 'change_mode':
            return


def show_commands():
    print('What action would you like to take:')
    print('[C]reate an [a]ccount')
    print('[L]ogin to your account')
    print('List [y]our trips')
    print('[R]egister a trip')
    print('e[X]it app')
    print('[?] Help (this info)')
    print()


def create_account():
    print(' ****************** REGISTER **************** ')

    name = input('What is your name? ')
    email = input('What is your email? ').strip().lower()

    old_account = svc.find_account_by_email(email)
    if old_account:
        error_msg(f"ERROR: Account with email {email} already exists.")
        return

    state.active_account = svc.create_account(name, email)
    success_msg(f"Created new account with id {state.active_account.id}.")


def log_into_account():
    print(' ****************** LOGIN **************** ')

    email = input('What is your email? ').strip().lower()
    account = svc.find_account_by_email(email)

    if not account:
        error_msg(f'Could not find account with email {email}.')
        return

    state.active_account = account
    success_msg('Logged in successfully.')

def register_trip():
    print(' ****************** REGISTER TRIP **************** ')

    if not state.active_account:
        error_msg('You must login first to register a cage.')
        return

    tpep_pickup_datetime = (input("Time pick up: "))
    tpep_dropoff_datetime = (input("Time drop off: "))
    vendorid = int(input("Which provider ? [1= Creative Mobile Technologies, LLC; 2= VeriFone Inc] "))
    passenger_count = int(input("How many passengers? "))
    trip_distance = float(input("How many miles was the trip?"))
    ratecodeid = int(input("The final ratecode is "))
    store_and_fwd_flag = input("Trip record was held in vehicle [Y, N]? ")
    pulocationid = int(input("The initial area code was "))
    dolocationid = int(input("The final area code is "))
    payment_type = int(input("How was paid? [1=Credit card, 2=Cash, 3=No charge, 4=Dispute, 5=Unknown, 6=Voided trip] "))
    fare_amount =float(input("Time and distance fare by meter is "))
    extra = float(input("Surcharge extra"))
    mta_tax = float(input("MTA tax "))
    tip_amount = float(input("Tip amount ")) if payment_type==1 else 0
    tolls_amount = float(input("Toll price was "))
    total_amount = float(input("The price charged to passaengers was "))

    trip = svc.register_trip(
        state.active_account, tpep_pickup_datetime,
        tpep_dropoff_datetime, vendorid, passenger_count, trip_distance, ratecodeid, store_and_fwd_flag,
        pulocationid, dolocationid,payment_type,fare_amount,extra,mta_tax,tip_amount, tolls_amount, total_amount
    )

    state.reload_account()
    success_msg(f'Register new trip with id {trip.id}.')




def list_trips(suppress_header=False):
    if not suppress_header:
        print(' ******************     Your trips     **************** ')

    if not state.active_account:
        error_msg('You must login first to register a cage.')
        return

    trips = svc.find_trips_for_user(state.active_account)
    print(f"You have {len(trips)} cages.")
    for idx, c in enumerate(trips):
        print(f' {idx + 1}. {c.trip_distance} is {c.total_amount} dolars.')


def exit_app():
    print()
    print('bye')
    raise KeyboardInterrupt()


def get_action():
    text = '> '
    if state.active_account:
        text = f'{state.active_account.name}> '

    action = input(Fore.YELLOW + text + Fore.WHITE)
    return action.strip().lower()


def unknown_command():
    print("Sorry we didn't understand that command.")


def success_msg(text):
    print(Fore.LIGHTGREEN_EX + text + Fore.WHITE)


def error_msg(text):
    print(Fore.LIGHTRED_EX + text + Fore.WHITE)
