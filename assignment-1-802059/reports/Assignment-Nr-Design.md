# This your assignment design report

1.	Design and explain interactions between main components in your architecture of mysimbdp (1 point)
The mysimpbdp-coredms is MongoDB. For mysimbdp-daas, the producers availability of the data I used mongo engine and pymongo. In mysimbdp-dataingest I used Studio3T.

2.	Explain how many nodes are needed in the deployment of my simbdp-coredms so that this component can work property (theoretically based on the selected technology ) (1 point)

A replica set is a group of mongod instances that maintain the same data set. A replica set contains several data bearing nodes and optionally one arbiter node. Of the data bearing nodes, one and only one member is deemed the primary node, while the other nodes are deemed secondary nodes.

The primary node receives all write operations. A replica set can have only one primary capable of confirming writes with write concern; although in some circumstances, another mongod instance may transiently believe itself to also be primary. The primary records all changes to its data sets in its operation log, i.e. oplog. For more information on primary node operation, see Replica Set Primary.
 
