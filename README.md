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

    usage: cassandra_importer [-h] -s SOURCE -d DESTINATION -ks KEYSPACE -cf
                              COLUMN_FAMILY [-k KEY] [-c COUNT] [-a]
    
    Process some integers.
    
    optional arguments:
      -h, --help            show this help message and exit
      -s SOURCE, --source SOURCE
                            Generally the prod cassandra path: localhost:9161
      -d DESTINATION, --destination DESTINATION
                            Cassandra path where you need your data:
                            localhost:9160
      -ks KEYSPACE, --keyspace KEYSPACE
                            The keyspace: myks
      -cf COLUMN_FAMILY, --column_family COLUMN_FAMILY
                            The Column family: mycf
      -k KEY, --key KEY     A specific key to be imported
      -c COUNT, --count COUNT
                            Total count of keys to be imported
      -a, --all             Get all. Not recommended!
    
      
    (-k, -c and -a are optional, you need to pass any one of those. Use -a with extreme caution)

Example: 
`cassandra_importer -s cassandra_server:9161 -d localhost:9160 -ks myks -cf mycf -c 100`

`cassandra_importer -s localhost:9161 -d localhost:9160 -ks myks -cf mycf -a`

Note: Make sure you have the keyspace (myks) and column family (mycf) with the same name created in the destination.

If your prod cassandra cannot be accessed directly, you can tunnel in:
`ssh -i key.pem -L 9161:localhost:9160 user@remote_cassandra_server -N`
This will port forward the remote cassandra 9160 port to your local 9161.


  [1]: http://www.datastax.com/dev/blog/bulk-loading
  [2]: http://www.datastax.com/docs/0.7/utilities/sstable2json

