# countdown.py
#
# A simple generator function

def countdown(n):
    print ("Counting down from", n)
    while n > 0:
        yield n
        n -= 1
    print ("Done counting down")

# Example use
if __name__ == '__main__':
    genreador = countdown(2)
    print (next(genreador))
    print (next(genreador))
    print (next(genreador))
""" Salida
2
1
Done counting down
Traceback (most recent call last):  
    print (next(genreador))
StopIteration """
    
    
