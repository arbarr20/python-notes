# genlog.py
#
# Sume los bytes transferidos en un registro del servidor Apache usando
# expresión generadora

with open("access-log") as wwwlog:
    # recuerde que las siguietes 2 lines esta en formato "gen conprehension()"
    bytecolumn = (line.rsplit(None,1)[1] for line in wwwlog)
    bytes_sent = (int(x) for x in bytecolumn if x != '-')
    print("Total", sum(bytes_sent))