# video-converter-to-mp4

Software que integra "ffmpeg" para convertir videos de cualquier formato a .mp4. El mismo no requiere de paquetes adicionales.
Se incluye un setup para poder generar un archivo ejecutable y que el programa pueda ser utilizado desde cualquier equipo.

Para generar el ejecutable para cualquier usuario se utilizó el biblioteca "cx_Freeze". La misma integra la herramienta "ffmpeg" para que no haga falta tenerla instalada.

> [!Important]
> Comando para crear archivo ejecutable a partir del código y de la configuración establecida.

```
python setup.py build
```

> [!Important]
> Paquetes utilizados para el desarrollo.

```
python -m pip install cx_Freeze

```