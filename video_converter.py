import os
import subprocess
import time

def convert_to_mp4(input_path):
    try:
        # Ruta del ejecutable de FFmpeg
        ffmpeg_path = os.path.join(os.getcwd(), 'ffmpeg.exe')
        
        # Validar que FFmpeg esté disponible
        if not os.path.exists(ffmpeg_path):
            print(ffmpeg_path)
            time.sleep(5)
            raise FileNotFoundError("El ejecutable ffmpeg.exe no se encontró en la carpeta del programa.")

        # Obtener nombre base del archivo y ruta de salida
        base_name = os.path.splitext(os.path.basename(input_path))[0]
        output_path = os.path.join(os.getcwd(), f"{base_name}.mp4")

        # Comando para convertir el video a MP4
        command = [
            ffmpeg_path,
            "-i", input_path,       # Archivo de entrada
            "-c:v", "libx264",      # Codec de video
            "-preset", "fast",      # Preset rápido
            "-c:a", "aac",          # Codec de audio
            output_path             # Archivo de salida
        ]

        # Ejecutar FFmpeg
        subprocess.run(command, check=True)
        print(f"Conversión exitosa: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error durante la conversión: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Conversor de Videos a MP4")
    input_path = input("Introduce la ruta del video a convertir: ")
    convert_to_mp4(input_path)