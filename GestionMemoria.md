# Gestión de memoria

http://docs.micropython.org/en/v1.9.3/pyboard/library/micropython.html#micropython.mem_info
```python
import micropython
micropython.mem_info(1)

```

[Leyenda](http://docs.micropython.org/en/v1.9.3/wipy/reference/constrained.html#reporting)

https://docs.micropython.org/en/latest/reference/constrained.html

## Optimizaci'on de memoria

[Restricciones en micropython](http://docs.micropython.org/en/latest/reference/constrained.html#)


https://forum.micropython.org/viewtopic.php?t=4813  

## Codigo precompilado

*.mpy

MicroPython has a cross compiler capable of compiling Python modules to bytecode (see the README in the mpy-cross directory). The resulting bytecode file has a .mpy extension; it may be copied to the filesystem and imported in the usual way. Alternatively some or all modules may be implemented as frozen bytecode: on most platforms this saves even more RAM as the bytecode is run directly from flash rather than being stored in RAM.

https://forum.micropython.org/viewtopic.php?t=4510

### Constantes

http://docs.micropython.org/en/latest/reference/constrained.html#execution-phase