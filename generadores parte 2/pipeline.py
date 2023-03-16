# pipeline.py
#
# Un ejemplo de configuración de una tubería de procesamiento con generadores

def grep(pattern, lines):
    for line in lines:
        if pattern in line:
            print (line)
            yield line


if __name__ == '__main__':
    from follow import follow

    # Configure una tubería de procesamiento: tail -f | python 
    logfile = open("access-log")
    loglines = follow(logfile)
    pylines = grep("python", loglines)

    # Extraiga los resultados del pipeline
    for line in pylines:
        print ("\n",line,)
    
    
        