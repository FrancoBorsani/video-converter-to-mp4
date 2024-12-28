from cx_Freeze import setup, Executable

# Archivos adicionales que deben incluirse
include_files = ["ffmpeg/bin/ffmpeg.exe"]

# Configuración del programa
setup(
    name="VideoConverter",
    version="1.0",
    description="Conversor de videos a formato MP4",
    executables=[Executable("video_converter.py")],
    options={
        "build_exe": {
            "include_files": include_files
        }
    }
)