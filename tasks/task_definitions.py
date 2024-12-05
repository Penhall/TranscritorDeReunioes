from crewai import Task
from typing import Dict
from crewai import Agent

def create_tasks(agents: Dict[str, Agent]) -> dict:
    """
    Cria e retorna todas as tarefas do sistema.
    Args:
        agents: Dicionário com todos os agentes
    Returns:
        dict: Dicionário com todas as tarefas
    """
    tasks = {
        'preparacao_audio': Task(
            description="""
            Realizar verificação do formato do áudio, normalização e segmentação.
            O arquivo de áudio está em: {file_path}
            Use exatamente este caminho ao chamar audio_toolkit.
            """,
            expected_output="Arquivo de áudio preparado e segmentado.",
            agent=agents['preparador_audio']
        ),
        
        'transcricao': Task(
            description="""
            1. Transcrever os segmentos de áudio em texto
            2. Garantir que o conteúdo transcrito seja extraído corretamente
            3. Retornar o conteúdo transcrito para uso nas próximas tarefas
            """,
            expected_output="Texto transcrito e disponível para processamento.",
            agent=agents['transcritor']
        ),
        
        'identificacao_palestrantes': Task(
            description="Analisar o texto transcrito e identificar diferentes palestrantes.",
            expected_output="Texto com identificação clara dos palestrantes.",
            agent=agents['identificador_palestrantes']
        ),
        
        'revisao_texto': Task(
            description="Revisar o texto identificado, corrigindo erros e melhorando clareza.",
            expected_output="Texto revisado e corrigido.",
            agent=agents['revisor_texto']
        ),
        
        'resumo': Task(
            description="Criar resumo detalhado do conteúdo revisado.",
            expected_output="Resumo claro e completo.",
            agent=agents['resumidor']
        ),
        
        'insights': Task(
            description="Analisar o conteúdo e extrair insights relevantes.",
            expected_output="Lista de insights e análises.",
            agent=agents['gerador_insights']
        ),
        
        'relatorio': Task(
            description="Gerar relatório final combinando resumo e insights.",
            expected_output="Relatório formatado e completo.",
            agent=agents['formulador_relatorios']
        )
    }
    
    return tasks