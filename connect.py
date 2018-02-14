#!/usr/bin/env python
import mysql.connector

## Support IPv4 only
# def ip2long(ip):
#     """
#     Convert an IP string to long
#     """
#     packedIP = socket.inet_aton(ip)
#     return struct.unpack("!L", packedIP)[0]

# def long2ip(lon):
#     """
#     Convert an long to IP string
#     """
#     tmp = struck.pack("!L", lon)
#     return socket.inet_ntoa(tmp)

# ## import netaddr

def mk_connect():
    try:
        from config import config
        cnx = mysql.connector.connect(**config)
        # print('Connect ok!')
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
        else:
                print(err)
    else:
        cnx.close()