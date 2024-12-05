import pytest
from pathlib import Path
from crewai_tools import Tool
from tools.transcription_tools import transcribe_audio

def test_transcribe_audio_is_tool():
    """Verifica se transcribe_audio é uma Tool do CrewAI"""
    assert isinstance(transcribe_audio, Tool)

def test_transcribe_audio_no_segments():
    """Testa se a função retorna erro quando não há segmentos"""
    result = transcribe_audio.run("./nonexistent/path/audio.wav")
    assert "Erro: Nenhum segmento encontrado" in result

# Poderíamos adicionar mais testes quando tivermos arquivos de áudio de exemplo
