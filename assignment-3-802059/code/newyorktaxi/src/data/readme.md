Field Name
__
Description
VendorID
A code indicating the TPEP provider that provided the record.
1= Creative Mobile Technologies, LLC; 2= VeriFone Inc.
tpep_pickup_datetime tpep_dropoff_datetime
Trip_distance PULocationID DOLocationID
The date and time when the meter was engaged. The date and time when the meter was disengaged.
The elapsed trip distance in miles reported by the taximeter. TLC Taxi Zone in which the taximeter was engaged
TLC Taxi Zone in which the taximeter was disengaged
  
Passenger_count
The number of passengers in the vehicle. This is a driver-entered value.
    
RateCodeID
The final rate code in effect at the end of the trip.
1= Standard rate
2=JFK
3=Newark
4=Nassau or Westchester 5=Negotiated fare 6=Group ride
Store_and_fwd_flag
This flag indicates whether the trip record was held in vehicle memory before sending to the vendor, aka “store and forward,” because the vehicle did not have a connection to the server.
Y= store and forward trip
N= not a store and forward trip
Payment_type
A numeric code signifying how the passenger paid for the trip.
1= Credit card 2= Cash
3= No charge 4= Dispute
5= Unknown 6= Voided trip
Fare_amount Extra
MTA_tax Improvement_surcharge Tip_amount
Tolls_amount Total_amount
The time-and-distance fare calculated by the meter.
Miscellaneous extras and surcharges. Currently, this only includes the $0.50 and $1 rush hour and overnight charges.
$0.50 MTA tax that is automatically triggered based on the metered rate in use.
$0.30 improvement surcharge assessed trips at the flag drop. The improvement surcharge began being levied in 2015.
Tip amount – This field is automatically populated for credit card tips. Cash tips are not included.
Total amount of all tolls paid in trip.
The total amount charged to passengers. Does not include cash tips.