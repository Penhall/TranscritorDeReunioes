from pathlib import Path
import whisper
from crewai_tools import tool

@tool
def transcribe_audio(file_path: str, output_dir: str = "./output") -> dict:
    """
    Transcreve um arquivo de áudio para texto usando Whisper e salva em Markdown.
    Args:
        file_path: Caminho do arquivo de áudio original.
        output_dir: Diretório onde o arquivo será salvo.
    Returns:
        dict: Dicionário contendo o caminho do arquivo e o texto transcrito.
    """
    try:
        print("Inicializando modelo Whisper...")
        model = whisper.load_model("base")
        
        segments_dir = Path(file_path).parent / "segments"
        segments = sorted(segments_dir.glob("segment_*.wav"))
        
        if not segments:
            return {"error": f"Nenhum segmento encontrado em: {segments_dir}"}
        
        print(f"Iniciando transcrição de {len(segments)} segmentos...")
        transcribed_texts = []
        
        for i, segment in enumerate(segments, 1):
            print(f"Transcrevendo segmento {i}/{len(segments)}: {segment.name}")
            result = model.transcribe(str(segment))
            transcribed_texts.append(result["text"].strip())
            print(f"Segmento {i} transcrito com sucesso")

        # Combinar resultados
        full_transcription = " ".join(transcribed_texts)
        
        # Salvar no arquivo Markdown
        output_path = Path(output_dir) / "transcricao.md"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(full_transcription)
        
        print(f"Transcrição salva em: {output_path}")
        
        # Excluir segmentos
        for segment in segments:
            segment.unlink()
        segments_dir.rmdir()
        print("Segmentos excluídos com sucesso.")

        return {
            "file_path": str(output_path),
            "content": full_transcription,
            "success": True
        }

    except Exception as e:
        return {
            "error": f"Erro na transcrição: {str(e)}",
            "success": False
        }
