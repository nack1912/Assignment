import datetime
import mongoengine


class Trip(mongoengine.Document):

    tpep_pickup_datetime = mongoengine.DateTimeField(default=datetime.datetime.now)
    tpep_dropoff_datetime = mongoengine.DateTimeField(default=datetime.datetime.now)
    vendorid = mongoengine.IntField(required=True)
    passenger_count = mongoengine.IntField(required=True)
    trip_distance = mongoengine.FloatField(required=True)
    ratecodeid = mongoengine.IntField(default=1)
    store_and_fwd_flag = mongoengine.StringField(default= "N")
    pulocationid = mongoengine.IntField(required=True)
    dolocationid = mongoengine.IntField(required=True)

    payment_type = mongoengine.IntField(required=True)
    #1= Credit card, 2= Cash, 3= No charge, 4= Dispute, 5= Unknown, 6= Voided trip
    fare_amount = mongoengine.FloatField(required=True)
    extra = mongoengine.FloatField(default=0)
    mta_tax = mongoengine.FloatField(default=0.5)
    tip_amount = mongoengine.FloatField(default=0)
    tolls_amount = mongoengine.FloatField(default=0)
    improvement_surcharge = mongoengine.FloatField(default=0.3)
    total_amount = mongoengine.FloatField(required=True)

    meta = {
        'db_alias': 'core',
        'collection': 'cages'
    }
