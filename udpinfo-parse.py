#!/usr/bin/env python
from connect import mk_connect

add_udpinfo = ("INSERT INTO udpinfo "
              "(srcport, dstport, length, checksum, stream) "
              "VALUES (%(srcport)s, %(dstport)s, %(length)s, "
              "%(checksum)s, %(stream)s)")

filename = 'udpinfo.txt'
f = None
try:
    f = open(filename,'r')
except Exception as e:
    print(e)

cnx = mk_connect()
cnx.autocommit = True
cursor = cnx.cursor()
try:
    _ = f.readline()    # discard header
    line = f.readline()
    print("Insert data, waiting...")
    while line:
        try:
            srcport, dstport, length, checksum, stream = line.split()
        except Exception as e:
            print(e)

        data_udpinfo = {
          'srcport': srcport,
          'dstport': dstport,
          'length': length,
          'checksum': int(checksum,16),
          'stream': stream
        }
        cursor.execute(add_udpinfo, data_udpinfo)
        line = f.readline()
except Exception as e:
    print(e)
finally:
    if f: f.close()
    cnx.commit()
    print("Complete.")
    cnx.close()
