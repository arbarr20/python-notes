# grep.py
#
# Una simple coorrutina

def grep(pattern):
    print (f"Buscando el Patron: {pattern}")
    while True:
        line = (yield)
        if pattern in line:
            print (line,)

# Ejemplo de Uso
if __name__ == '__main__':
    g = grep("python")
    next(g)
    g.send("Yeah, but no, but yeah, but no")
    g.send("A series of tubes")
    g.send("python generators rock!")
