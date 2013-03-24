Cassandra Data Impoter
===============

Moves casandra data from one cluster to another. I primiarly use to move some chunks of production data in cassandra to local cassandra instance for testing.

There are other ways you can achive it:   
	1. [Use cassandra bulk loader][1]  
	2. [Use sstable2json][2]



How to install cassandra-importer
------------------
1. Clone or download the project: `git clone https://github.com/utkarsh2012/cassandra-importer.git`
2. Go to the directory: `python setup.py install'
3. Run `cassandra_importer` with the required flags


How to use cassandra-importer?
---------------
    ./cass_importer.py -s localhost:9161
                       -d localhost:9160
                       -ks myks
                       -cf mycf
                       -k 361115111934
                       -c 100
                       -a 
(where -k, -c and -a are optional)

Example: `./cass_importer.py -s localhost:9161 -d localhost:9160 -ks myks -cf mycf -a`

Note: Make sure you have the keyspace (myks) and column family (mycf) with the same name created in the destination.

  [1]: http://www.datastax.com/dev/blog/bulk-loading
  [2]: http://www.datastax.com/docs/0.7/utilities/sstable2json