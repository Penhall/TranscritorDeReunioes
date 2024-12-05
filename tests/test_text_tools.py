import pytest
from crewai_tools import Tool
from tools.text_tools import text_editing_tool

def test_text_editing_is_tool():
    """Verifica se text_editing_tool é uma Tool do CrewAI"""
    assert isinstance(text_editing_tool, Tool)

def test_text_editing_empty_text():
    """Testa resposta para texto vazio"""
    result = text_editing_tool.run("")
    assert "Erro: Texto inválido" in result

def test_text_editing_valid_text():
    """Testa edição de texto válido"""
    test_text = "  olá,   mundo.    como vai você?   tudo bem  "
    result = text_editing_tool.run(test_text)
    assert "Olá, mundo. Como vai você? Tudo bem" == result

def test_text_editing_capitalization():
    """Testa capitalização de sentenças"""
    test_text = "primeira frase. segunda frase. terceira frase."
    result = text_editing_tool.run(test_text)
    assert "Primeira frase. Segunda frase. Terceira frase" == result
