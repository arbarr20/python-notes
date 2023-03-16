# nongenlog.py
#
# Suma la cantidad de bytes transferidos en un archivo de registro de Apache
# usando un bucle for simple. No usamos generadores aquí.

with open("access-log") as wwwlog:
    total = 0
    for line in wwwlog:
        bytes_sent = line.rsplit(None,1)[1]
        if bytes_sent != '-':
            # se debe convertir a int para sumarlos ademas  por que viene de ser una cadena,
            total += int(bytes_sent)
    print("Total", total)