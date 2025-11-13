import subprocess
import os

# Caminho do arquivo original
input_file = input("Insira o nome do arquivo .mp4: ").strip()

# Arquivo de saída (mesmo nome + sufixo)
output_file = input_file.rsplit(".", 1)[0] + "_convertido.mp4"

# Tamanho máximo em MB
max_size_mb = 10

# Obter a duração do vídeo em segundos usando ffprobe
def get_duration(file_path):
    cmd = [
        "ffprobe", "-v", "error", "-show_entries",
        "format=duration", "-of",
        "default=noprint_wrappers=1:nokey=1", file_path
    ]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return float(result.stdout.strip())

duration = get_duration(input_file)

# Calcular bitrate alvo (em kbps)
# 1 MB = 8192 kb; (MB * 8192) / duração (segundos) = kbps
target_bitrate = int((max_size_mb * 8192) / duration)

# Comprimir usando ffmpeg (sempre gera .mp4 final)
cmd = [
    "ffmpeg",
    "-i", input_file,
    "-c:v", "libx264",        # codec de vídeo h.264
    "-b:v", f"{target_bitrate}k",
    "-c:a", "aac",            # codec de áudio AAC
    "-b:a", "128k",           # áudio fixo em 128 kbps
    "-movflags", "+faststart",  # otimiza streaming
    output_file
]

subprocess.run(cmd)

# Verificar tamanho final
final_size = os.path.getsize(output_file) / (1024 * 1024)
print(f"Tamanho final: {final_size:.2f} MB")
print(f"Vídeo convertido salvo em: {output_file}")

