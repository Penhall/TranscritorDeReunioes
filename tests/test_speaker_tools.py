import pytest
from crewai_tools import Tool
from tools.speaker_tools import speaker_identification_tool

def test_speaker_identification_is_tool():
    """Verifica se speaker_identification_tool é uma Tool do CrewAI"""
    assert isinstance(speaker_identification_tool, Tool)

def test_speaker_identification_empty_text():
    """Testa resposta para texto vazio"""
    result = speaker_identification_tool.run("")
    assert "Erro: Texto inválido" in result

def test_speaker_identification_valid_text():
    """Testa identificação de palestrantes com texto válido"""
    test_text = "Olá, como vai? Tudo bem com você. Sim, estou bem."
    result = speaker_identification_tool.run(test_text)
    assert "[Palestrante 1]" in result
    assert "[Palestrante 2]" in result
