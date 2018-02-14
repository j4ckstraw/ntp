#!/usr/bin/env python
from connect import mk_connect

add_frameinfo = ("INSERT INTO frameinfo "
              "(time_delta, time_delta_displayed, time_relative, "
              "number, len, cap_len) "
              "VALUES (%(time_delta)s, %(time_delta_displayed)s, "
              "%(time_relative)s, %(number)s, %(len)s, %(cap_len)s)")

filename = 'freaminfo.txt'
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
            time_delta, time_delta_displayed, time_relative, \
            number, len_, cap_len = line.split()[-6:]
        except Exception as e:
            print(e)

        data_frameinfo = {
          'time_delta': time_delta,
          'time_delta_displayed': time_delta_displayed,
          'time_relative': time_relative,
          'number': number,
          'len': len_,
          'cap_len': cap_len
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
