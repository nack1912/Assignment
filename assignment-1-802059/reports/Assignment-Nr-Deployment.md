# Part 2 - Development and deployment 

1.	Design and explain the data schema/structure for mysimbdp-coredms (1point)

We have the DB storage in localhost. With one collection named newyorkdata, where we ingest the json files from the new York taxi data using STUDIO 3T. 

2.	Explain how would you partition the data in mysimbdp-coredms into different shards/partitions (1 point)

I will make the partition depending on the amount of data needed to storage. After, I will make depending on the date of the trip.
3.	Write a mysimbdp-dataingest that takes data from your selected sources and stores the data into mysimbdp-coredms (1 point)

Using STUDIO 3T, it is easy to import and export data from/to the mongoDB.

4.	Given your deployment environment, show the uploading performance(response time and failure) of the tests for 1,5, 10, .., n of concurrent mysimbdp-dataingest pushing data into mysimbdp-coredms (1 point) 

5.	Observing the performance and failure problems when you push a lot of data into mysimbdp-coredms (you do not need to worry about duplicated data in mysimbdp), propose the change of your deployment to avoid such problems (or explain why you do not have any problem with your deployment) (1 point) 
