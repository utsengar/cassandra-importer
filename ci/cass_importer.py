#!/usr/bin/python

from pycassa import ConnectionPool, ColumnFamily, InvalidRequestException
import argparse
import sys


class CassandraImporter:
    def __init__(self):
        parser = argparse.ArgumentParser(description='Process some integers.')
        parser.add_argument('-s', '--source',
                            help='Generally the prod cassandra path: \
                            localhost:9161',
                            required=True)
        parser.add_argument('-d', '--destination',
                            help='Cassandra path where you need your data: \
                            localhost:9160',
                            required=True)
        parser.add_argument('-ks', '--keyspace',
                            help='The keyspace: myks',
                            required=True)
        parser.add_argument('-cf', '--column_family',
                            help='The Column family: mycf',
                            required=True)
        parser.add_argument('-k', '--key',
                            help='A specific key to be imported',
                            required=False)
        parser.add_argument('-c', '--count',
                            help='Total count of keys to be imported',
                            required=False)
        parser.add_argument('-a', '--all',
                            action='store_true',
                            help='Get all. Not recommended!',
                            required=False)
        args = vars(parser.parse_args())

        """Connection setting with cassandra
        The script is meant to sync data. So source and destination KS
        and CF shold be the same."""

        try:
            source_pool = ConnectionPool(args["keyspace"],
                                         [args["source"]])
            destination_pool = ConnectionPool(args["keyspace"],
                                              [args["destination"]])
            self.source_cf = ColumnFamily(source_pool,
                                          args["column_family"])
            self.destination_cf = ColumnFamily(destination_pool,
                                               args["column_family"])
        except Exception as e:
            print "ERROR: The keyspace or the column family does not \
                    exist or request is timing out!"
            sys.exit()

        #Optional data
        self.count = args["count"]
        if self.count:
            self.count = int(self.count)
        self.key = args["key"]
        self.all = args["all"]

    def importData(self):
        data = dict()
        #Get columns for a key
        if self.key:
            column_data = self.source_cf.get(self.key)
            data[self.key] = column_data

        #Get last 100 keys and their columns
        elif self.count:
            counter = 0
            for value in self.source_cf.get_range(column_count=0,
                                                  filter_empty=False):
                if(counter < self.count):
                    column_data = self.source_cf.get(value[0])
                    data[value[0]] = column_data
                    counter += 1
                else:
                    break

        #Get All, Not recommended
        elif self.all:
            for value in self.source_cf.get_range(column_count=0,
                                                  filter_empty=False):
                column_data = self.source_cf.get(value[0])
                data[value[0]] = column_data
        else:
            print "Please pass -c or -k or -a arguments!"

        return data

    def insertData(self, data):
        for key, value in data.iteritems():
            self.destination_cf.insert(key, value)

    def run(self):
        self.update_progress(0)
        data = self.importData()
        self.update_progress(50)

        self.insertData(data)
        self.update_progress(100)
        print "Import complete!"

    def update_progress(self, progress):
        print '\r[{0}] {1}%'.format('#' * (progress / 10), progress)


def runner():
    importer = CassandraImporter()
    importer.run()
