#!/usr/bin/env python
from connect import mk_connect
from netaddr import EUI


add_frameinfo = ("INSERT INTO ethernetinfo "
              "(src, dst, lg, ig, type) "
              "VALUES(%(src)s, %(dst)s, %(lg)s, %(ig)s, %(type)s)")

filename = 'ethernetinfo1020.txt'
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
           src, dst, lg, ig, type_ = line.split()
        except Exception as e:
            print(e)

        data_frameinfo = {
          'src': EUI(src).value,
          'dst': EUI(dst).value,
          'lg': lg,
          'ig': ig,
          'type': int(type_,16)
        }
        cursor.execute(add_frameinfo, data_frameinfo)
        line = f.readline()
except Exception as e:
    print(e)
finally:
    if f: f.close()
    cnx.commit()
    print("Complete.")
    cnx.close()
