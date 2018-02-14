#!/usr/bin/env python
from connect import mk_connect
from socket import inet_aton, inet_ntoa
from netaddr import IPAddress

add_ntpinfo = ("INSERT INTO ntpinfo "
              "(priv_flags_r, priv_flags_more, flags_vn, flags_mode, "
              "priv_auth, priv_seq, priv_impl, priv_reqcode, priv_numitems,"
              "priv_reserved, priv_monlist_itemsize, priv_monlist_avgint, "
              "priv_monlist_lsint, priv_monlist_restr, priv_monlist_count,"
              "priv_monlist_remote_address, priv_monlist_local_address,"
              "priv_monlist_flags, priv_monlist_port, priv_monlist_mode,"
              "priv_monlist_version, priv_monlist_ipv6)"
              "VALUES (%(priv_flags_r)s,%(priv_flags_more)s,%(flags_vn)s,"
              "%(flags_mode)s,%(priv_auth)s,%(priv_seq)s,%(priv_impl)s,"
              "%(priv_reqcode)s,%(priv_numitems)s,%(priv_reserved)s,"
              "%(priv_monlist_itemsize)s,%(priv_monlist_avgint)s,"
              "%(priv_monlist_lsint)s,%(priv_monlist_restr)s,"
              "%(priv_monlist_count)s,%(priv_monlist_remote_address)s,"
              "%(priv_monlist_local_address)s,%(priv_monlist_flags)s,"
              "%(priv_monlist_port)s,%(priv_monlist_mode)s,"
              "%(priv_monlist_version)s,%(priv_monlist_ipv6)s)")

filename = 'ntpinfo.txt'
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
            priv_flags_r, priv_flags_more, flags_vn, flags_mode,\
            priv_auth, priv_seq, priv_impl, priv_reqcode, priv_numitems,\
            priv_reserved, priv_monlist_itemsize, priv_monlist_avgints,\
            priv_monlist_lsints, priv_monlist_restrs, priv_monlist_counts,\
            priv_monlist_remote_addresss, priv_monlist_local_addresss,\
            priv_monlist_flagss, priv_monlist_ports, priv_monlist_modes,\
            priv_monlist_versions, priv_monlist_ipv6s = line.split()
        except Exception as e:
            print(e)
        ziped = zip(priv_monlist_avgints.split(','),\
        priv_monlist_lsints.split(','),priv_monlist_restrs.split(','),\
        priv_monlist_counts.split(','),priv_monlist_remote_addresss.split(','),\
        priv_monlist_local_addresss.split(','),priv_monlist_flagss.split(','),\
        priv_monlist_ports.split(','),priv_monlist_modes.split(','),\
        priv_monlist_versions.split(','), priv_monlist_ipv6s.split(','))
        data_ntpinfos = [{
          'priv_flags_r': priv_flags_r,
          'priv_flags_more': priv_flags_more,
          'flags_vn': flags_vn,
          'flags_mode': flags_mode,
          'priv_auth': priv_auth,
          'priv_seq': priv_seq,
          'priv_impl': priv_impl,
          'priv_reqcode': priv_reqcode,
          'priv_numitems': priv_numitems,
          'priv_reserved': int(priv_reserved,16),
          'priv_monlist_itemsize': int(priv_monlist_itemsize,16),
          'priv_monlist_avgint': priv_monlist_avgint,
          'priv_monlist_lsint': priv_monlist_lsint,
          'priv_monlist_restr': int(priv_monlist_restr,16),
          'priv_monlist_count': priv_monlist_count,
          'priv_monlist_remote_address': IPAddress(priv_monlist_remote_address).value,
          'priv_monlist_local_address': IPAddress(priv_monlist_local_address).value,
          'priv_monlist_flags': int(priv_monlist_flags,16),
          'priv_monlist_port': priv_monlist_port,
          'priv_monlist_mode': priv_monlist_mode,
          'priv_monlist_version': priv_monlist_version,
          'priv_monlist_ipv6': priv_monlist_ipv6
        } for priv_monlist_avgint, priv_monlist_lsint, priv_monlist_restr,\
        priv_monlist_count,priv_monlist_remote_address,\
        priv_monlist_local_address,priv_monlist_flags,priv_monlist_port,\
        priv_monlist_mode,priv_monlist_version,priv_monlist_ipv6 in ziped]
        cursor.executemany(add_ntpinfo, data_ntpinfos)
        line = f.readline()
except Exception as e:
    print(e)
finally:
    if f: f.close()
    cnx.commit()
    print("Complete.")
    cnx.close()
