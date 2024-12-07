from pathlib import Path
import whisper
from crewai_tools import tool

@tool
def transcribe_audio(file_path: str, output_dir: str = "./output") -> dict:
    """
    Transcreve um arquivo de audio para texto usando Whisper.
    Args:
        file_path: Caminho do arquivo de audio original ou diretório de segmentos.
        output_dir: Diretório onde o arquivo será salvo.
    Returns:
        dict: Dicionário contendo o caminho do arquivo e o texto transcrito.
    """
    try:
        # Converter caminhos para objetos Path
        input_path = Path(file_path)
        output_path = Path(output_dir)

        # Validar existência do diretório de segmentos
        segments_dir = input_path
        if not segments_dir.exists() or not segments_dir.is_dir():
            return {
                "error": f"Diretório de segmentos não encontrado: {segments_dir}",
                "success": False
            }

        print(f"Procurando segmentos em: {segments_dir}")

        # Procurar por segmentos no diretório
        segments = list(sorted(segments_dir.glob("segment_*.wav")))
        if not segments:
            return {
                "error": f"Nenhum segmento encontrado no diretório: {segments_dir}",
                "success": False
            }

        print(f"Segmentos encontrados: {[seg.name for seg in segments]}")

        # Inicializar o modelo Whisper
        model = whisper.load_model("base")
        full_text = []

        # Transcrição de cada segmento
        for i, segment_path in enumerate(segments):
            print(f"Transcrevendo segmento {i+1}/{len(segments)}: {segment_path.name}")
            try:
                result = model.transcribe(str(segment_path))
                segment_text = result['text'].strip()
                full_text.append(segment_text)
                print(f"Segmento {i+1} transcrito com sucesso.")
            except Exception as e:
                print(f"Erro ao transcrever o segmento {i+1}: {e}")
                full_text.append("[Erro na transcrição]")

        # Combinar todos os textos
        complete_transcription = " ".join(full_text)

        # Criar o diretório de saída
        output_path.mkdir(parents=True, exist_ok=True)
        output_file = output_path / "transcricao.md"

        # Salvar a transcrição no arquivo
        with output_file.open("w", encoding="utf-8") as f:
            f.write(complete_transcription)

        print(f"Transcrição completa salva em: {output_file}")

        return {
            "file_path": str(output_file),
            "content": complete_transcription,
            "success": True
        }

    except Exception as e:
        import traceback
        return {
            "error": f"Erro durante a transcrição: {str(e)}\n{traceback.format_exc()}",
            "success": False
        }
