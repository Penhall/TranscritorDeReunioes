from crewai_tools import tool

@tool
def speaker_identification_tool(transcription: str) -> str:
    """
    Identifica diferentes palestrantes no texto transcrito.
    Args:
        transcription: Texto transcrito para identificar palestrantes
    Returns:
        str: Texto com identificação de palestrantes
    """
    try:
        if not transcription or not isinstance(transcription, str):
            return "Erro: Texto inválido para identificação de palestrantes"
        
        print("Identificando palestrantes no texto...")
        
        # Aqui seria implementada a lógica real de identificação de palestrantes
        # Por ora, fazemos uma marcação simples de exemplo
        sentences = transcription.split(". ")
        current_speaker = 1
        marked_sentences = []
        
        for sentence in sentences:
            if sentence.strip():
                marked_sentences.append(f"[Palestrante {current_speaker}] {sentence.strip()}")
                current_speaker = 1 if current_speaker == 2 else 2

        result = ". ".join(marked_sentences)
        print("Identificação de palestrantes concluída")
        return result

    except Exception as e:
        return f"Erro na identificação de palestrantes: {str(e)}"
