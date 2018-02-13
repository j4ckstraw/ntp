#!/usr/bin/env python
from connect import mk_connect
from socket import inet_aton, inet_ntoa
from netaddr import IPAddress


add_ipinfo = ("INSERT INTO ipinfo "
              "(version, hdr_len, dsfield_dscp, dsfield_ecn,"
              " len, id, flags_rb, flags_df, flags_mf, frag_offset,"
              " ttl, proto, checksum, src, dst) "
              "VALUES (%(version)s, %(hdr_len)s, %(dsfield_dscp)s,"
              " %(dsfield_ecn)s, %(len)s, %(id)s, %(flags_rb)s,"
              " %(flags_df)s, %(flags_mf)s, %(frag_offset)s, %(ttl)s,"
              " %(proto)s, %(checksum)s, %(src)s, %(dst)s)")

filename = 'ipinfo.txt'
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
            version, hdr_len, dsfield_dscp, dsfield_ecn, len_, id_, flags_rb, \
            flags_df, flags_mf, frag_offset, ttl, proto, checksum, src, dst = line.split()
        except Exception as e:
            print(e)

        data_ipinfo = {
          'version': version,
          'hdr_len': hdr_len,
          'dsfield_dscp': dsfield_dscp,
          'dsfield_ecn': dsfield_ecn,
          'len': len_,
          'id': int(id_,16),
          'flags_rb': flags_rb,
          'flags_df': flags_df,
          'flags_mf': flags_mf,
          'frag_offset': frag_offset,
          'ttl': ttl,
          'proto': proto,
          'checksum': int(checksum,16),
          'src': IPAddress(src).value,
          'dst': IPAddress(dst).value
        }
        cursor.execute(add_ipinfo, data_ipinfo)
        line = f.readline()
except Exception as e:
    print(e)
finally:
    if f: f.close()
    cnx.commit()
    print("Complete.")
    cnx.close()
