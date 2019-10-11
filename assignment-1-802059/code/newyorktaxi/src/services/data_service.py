from typing import List, Optional

import datetime

import bson

from data.trips import Trip
from data.owners import Owner


def create_account(name: str, email: str) -> Owner:
    owner = Owner()
    owner.name = name
    owner.email = email

    owner.save()

    return owner


def find_account_by_email(email: str) -> Owner:
    owner = Owner.objects(email=email).first()
    return owner

def register_trip(active_account: Owner
                  , tpep_pickup_datetime,
                  tpep_dropoff_datetime, vendorid, passenger_count, trip_distance, ratecodeid, store_and_fwd_flag,
                  pulocationid, dolocationid, payment_type, fare_amount, extra, mta_tax, tip_amount, tolls_amount,
                  total_amount) -> Trip:
    trip = Trip()
    trip.tpep_pickup_datetime = tpep_pickup_datetime
    trip.tpep_dropoff_datetime = tpep_dropoff_datetime
    trip.vendorid = vendorid
    trip.passenger_count =passenger_count
    trip.trip_distance =trip_distance
    trip.ratecodeid = ratecodeid
    trip.store_and_fwd_flag = store_and_fwd_flag
    trip.pulocationid = pulocationid
    trip.dolocationid = dolocationid
    trip.payment_type = payment_type
    trip.fare_amount = fare_amount
    trip.extra = extra
    trip.mta_tax = mta_tax
    trip.tip_amount = tip_amount
    trip.tolls_amount = tolls_amount
    trip.total_amount = total_amount

    trip.save()

    account = find_account_by_email(active_account.email)
    account.trip_ids.append(trip.id)
    account.save()

    return trip


def find_trips_for_user(account:Owner) -> List[Trip]:
    query = Trip.objects(id__in=account.trip_ids)
    trips = list(query)
    return trips
