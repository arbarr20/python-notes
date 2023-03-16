# bogus.py
#
# Bogus example of a generator that produces and receives values

def countdown(n):
    print("Cuenta Regresiva de", n)
    while n >= 0:
        newvalue = (yield n)
        # Si se envió un nuevo valor, reinicie n con él
        if newvalue is not None:
            n = newvalue
        else:
            n -= 1

c = countdown(5)
for x in c:
    print(x)
    if x == 5:
        x = c.send(3)
        print(x)



