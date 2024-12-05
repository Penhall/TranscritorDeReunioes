import pytest
from pathlib import Path
from crewai_tools import Tool
from tools.report_tools import report_generation_tool

def test_report_generation_is_tool():
    """Verifica se report_generation_tool é uma Tool do CrewAI"""
    assert isinstance(report_generation_tool, Tool)

def test_report_generation_no_summary():
    """Testa resposta quando não há resumo"""
    result = report_generation_tool.run("")
    assert "Erro: Resumo não fornecido" in result

def test_report_generation_with_summary(tmp_path):
    """Testa geração de relatório com apenas resumo"""
    test_summary = "Este é um resumo de teste."
    result = report_generation_tool.run(test_summary, output_dir=str(tmp_path))
    
    # Verifica se o arquivo foi criado
    report_path = Path(result)
    assert report_path.exists()
    
    # Verifica conteúdo do relatório
    content = report_path.read_text(encoding='utf-8')
    assert "# Relatório da Transcrição" in content
    assert "## Resumo" in content
    assert test_summary in content
    assert "## Insights" not in content

def test_report_generation_with_insights(tmp_path):
    """Testa geração de relatório com resumo e insights"""
    test_summary = "Este é um resumo de teste."
    test_insights = "Estes são alguns insights."
    result = report_generation_tool.run(
        test_summary, 
        insights=test_insights,
        output_dir=str(tmp_path)
    )
    
    # Verifica se o arquivo foi criado
    report_path = Path(result)
    assert report_path.exists()
    
    # Verifica conteúdo do relatório
    content = report_path.read_text(encoding='utf-8')
    assert "# Relatório da Transcrição" in content
    assert "## Resumo" in content
    assert test_summary in content
    assert "## Insights" in content
    assert test_insights in content
