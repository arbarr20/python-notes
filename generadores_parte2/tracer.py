import tracemalloc
# para aplicar con slots ver https://www.youtube.com/watch?v=AR3hD43HLNE
class Tracer:
    def __enter__(self):
        if tracemalloc.is_tracing():
            raise ValueError ("No se puede anidar trazadores")
        self.bytes_allocated =None
        tracemalloc.start()
        return self

    def __exit__(self,exc_type,exc_value,exc_traceback):
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        self.bytes_allocated =current

def medir (cls,isntancias):
    with Tracer() as t:
        obj = [cls(1,2)for _ in range(isntancias)]
    return t.bytes_allocated


    

