# -*- coding: utf-8 -*-

from pathlib import Path
from faster_whisper import WhisperModel
from crewai_tools import tool

@tool
def transcribe_audio(file_path: str, output_dir: str = "./output") -> dict:
    """
    Transcreve um arquivo de audio para texto usando Faster Whisper.
    Args:
        file_path: Caminho do arquivo de audio original.
        output_dir: Diretorio onde o arquivo sera salvo.
    Returns:
        dict: Dicionario contendo o caminho do arquivo e o texto transcrito.
    """
    try:
        print("Inicializando modelo Faster Whisper...")
        model = WhisperModel("base", device="cpu", compute_type="int8")
        
        segments_dir = Path(file_path).parent / "segments"
        segments = sorted(segments_dir.glob("segment_*.wav"))
        
        if not segments:
            return {"error": f"Nenhum segmento encontrado em: {segments_dir}"}
        
        print(f"Iniciando transcricao de {len(segments)} segmentos...")
        transcribed_texts = []
        
        for i, segment in enumerate(segments, 1):
            print(f"Transcrevendo segmento {i}/{len(segments)}: {segment.name}")
            segments, info = model.transcribe(str(segment))
            segment_text = " ".join([seg.text for seg in segments])
            transcribed_texts.append(segment_text.strip())
            print(f"Segmento {i} transcrito com sucesso")

        full_transcription = " ".join(transcribed_texts)
        
        output_path = Path(output_dir) / "transcricao.md"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(full_transcription)
        
        print(f"Transcricao salva em: {output_path}")
        
        for segment in segments:
            segment.unlink()
        segments_dir.rmdir()
        print("Segmentos excluidos com sucesso.")

        return {
            "file_path": str(output_path),
            "content": full_transcription,
            "success": True
        }

    except Exception as e:
        return {
            "error": f"Erro na transcricao: {str(e)}",
            "success": False
        }