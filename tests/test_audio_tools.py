import pytest
from crewai_tools import Tool
from tools.audio_tools import audio_toolkit

def test_audio_toolkit_file_not_found():
    """Testa se a função levanta exceção quando arquivo não existe"""
    result = audio_toolkit.run("arquivo_inexistente.wav")
    assert "Erro de arquivo" in result

def test_audio_toolkit_is_tool():
    """Verifica se audio_toolkit é uma Tool do CrewAI"""
    assert isinstance(audio_toolkit, Tool)