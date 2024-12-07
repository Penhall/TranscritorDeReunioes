from pathlib import Path
from pydub import AudioSegment
from pydub.effects import normalize
from crewai_tools import tool
import os

@tool
def audio_toolkit(file_path: str, output_format: str = "wav", segment_duration: int = 300) -> str:
    """
    Prepara o arquivo de áudio para transcrição.
    Args:
        file_path: Caminho para o arquivo de áudio
        output_format: Formato de saída (padrão: wav)
        segment_duration: Duração de cada segmento em segundos (padrão: 300)
    Returns:
        str: Mensagem indicando sucesso e localização dos segmentos
    """
    try:
        # Validar e resolver o caminho do arquivo
        file_path = str(Path(file_path).resolve())
        print(f"Processando arquivo de áudio: {file_path}")

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
        
        # Preparar diretório de saída
        output_dir = Path(file_path).parent / "segments"
        output_dir.mkdir(exist_ok=True)
        print(f"Diretório de segmentos: {output_dir}")

        # Carregar e normalizar o áudio
        print("Carregando e normalizando áudio...")
        audio = AudioSegment.from_file(file_path)
        normalized_audio = normalize(audio)
        
        # Segmentar o áudio
        print("Segmentando áudio...")
        segment_count = 0
        for i in range(0, len(normalized_audio), segment_duration * 1000):
            segment = normalized_audio[i:i + segment_duration * 1000]
            # Formato padronizado: segment_XX.wav (com dois dígitos)
            segment_path = output_dir / f"segment_{segment_count:02d}.{output_format}"
            segment.export(str(segment_path), format=output_format)
            print(f"Segmento {segment_count:02d} criado: {segment_path}")
            segment_count += 1

        return f"Áudio processado com sucesso. {segment_count} segmentos salvos em: {output_dir}"
    
    except FileNotFoundError as e:
        return f"Erro de arquivo: {str(e)}"
    except Exception as e:
        return f"Erro no processamento do áudio: {str(e)}"