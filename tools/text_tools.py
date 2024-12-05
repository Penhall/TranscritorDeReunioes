from crewai_tools import tool

@tool
def text_editing_tool(text: str) -> str:
    """
    Revisa e corrige o texto transcrito.
    Args:
        text: Texto para revisar e corrigir
    Returns:
        str: Texto revisado e corrigido
    """
    try:
        if not text or not isinstance(text, str):
            return "Erro: Texto inválido para revisão"
        
        print("Iniciando revisão do texto...")
        
        # Remove espaços extras e quebras de linha
        text = " ".join(text.split())
        
        # Divide o texto em sentenças preservando a pontuação original
        sentences = []
        current = ""
        for char in text:
            current += char
            if char in ".?" and current.strip():
                sentences.append(current.strip())
                current = ""
        if current.strip():
            sentences.append(current.strip())

        # Processa cada sentença mantendo a pontuação original
        processed_sentences = []
        for i, sentence in enumerate(sentences):
            if sentence:
                # Mantém a pontuação original
                punctuation = sentence[-1] if sentence[-1] in ".?" else ""
                # Remove pontuação temporariamente
                clean_sentence = sentence.rstrip('.?')
                # Capitaliza primeira letra
                processed = clean_sentence[0].upper() + clean_sentence[1:]
                # Se não for a última sentença, adiciona a pontuação original
                if i < len(sentences) - 1:
                    processed += punctuation
                processed_sentences.append(processed)
        
        # Junta as sentenças
        edited_text = " ".join(processed_sentences)
        
        print("Revisão do texto concluída")
        return edited_text

    except Exception as e:
        return f"Erro na revisão do texto: {str(e)}"