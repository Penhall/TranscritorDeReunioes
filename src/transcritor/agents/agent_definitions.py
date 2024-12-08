from crewai import Agent
from langchain_openai import ChatOpenAI

# Importando tools da nova estrutura
from transcritor.tools.audio_tools import audio_toolkit
from transcritor.tools.transcription_tools import transcribe_audio
from transcritor.tools.speaker_tools import speaker_identification_tool
from transcritor.tools.text_tools import text_editing_tool
from transcritor.tools.report_tools import report_generation_tool
from transcritor.tools.toxic_tools import analyze_toxicity

def create_agents(gpt_model: ChatOpenAI) -> dict:
    """
    Cria e retorna todos os agentes do sistema.
    Args:
        gpt_model: Instância do modelo GPT configurado
    Returns:
        dict: Dicionário com todos os agentes
    """
    agents = {
        'preparador_audio': Agent(
            role='Preparador de Ýudio',
            goal='Preparar o arquivo de áudio para transcrição, incluindo normalização e segmentação',
            backstory="Especialista em manipulação de áudio, com habilidade para melhorar a qualidade e preparar o arquivo para processamento.",
            verbose=True,
            tools=[audio_toolkit],
            llm=gpt_model
        ),
        
        'transcritor': Agent(
            role='Transcritor',
            goal='Converter áudio em texto com precisão e extrair o conteúdo transcrito',
            backstory="Especialista em transformar áudio em texto, com foco em qualidade e extração precisa do conteúdo.",
            verbose=True,
            tools=[transcribe_audio],
            allow_delegation=False,
            llm=gpt_model
        ),
        
        'identificador_palestrantes': Agent(
            role='Identificador de Palestrantes',
            goal='Identificar e diferenciar os palestrantes no texto transcrito',
            backstory="Especialista em análise de diálogo e identificação de palestrantes em transcrições.",
            verbose=True,
            tools=[speaker_identification_tool],
            llm=gpt_model
        ),
        
        'revisor_texto': Agent(
            role='Revisor de Texto',
            goal='Revisar e corrigir o texto transcrito',
            backstory="Especialista em revisão textual, garantindo clareza e correção.",
            verbose=True,
            tools=[text_editing_tool],
            llm=gpt_model
        ),
             
        'analisador_toxicidade': Agent(
            role='Analisador de Toxicidade',
            goal='Analisar o conteúdo transcrito em busca de linguagem tóxica ou inapropriada',
            backstory="""Especialista em análise de discurso e moderação de conteúdo. 
            Utiliza tecnologia avançada para identificar e classificar linguagem potencialmente 
            tóxica ou prejudicial, fornecendo recomendações para melhorar a comunicação.""",
            tools=[analyze_toxicity],
            temperature=0.2,  # Baixa temperatura para análises mais precisas
            llm=gpt_model
        ),        
        
        'resumidor': Agent(
            role='Resumidor',
            goal='Criar resumo detalhado do conteúdo transcrito',
            backstory="Especialista em análise textual e síntese de informações.",
            verbose=True,
            llm=gpt_model
        ),
        
        'gerador_insights': Agent(
            role='Gerador de Insights',
            goal='Analisar o conteúdo e identificar padrões importantes',
            backstory="Especialista em análise de dados qualitativos e identificação de tendências.",
            verbose=True,
            llm=gpt_model
        ),
        
        'formulador_relatorios': Agent(
            role='Formulador de Relatórios',
            goal='Criar relatório final organizado e completo',
            backstory="Especialista em formatação de relatórios e apresentação clara de informações.",
            verbose=True,
            tools=[report_generation_tool],
            llm=gpt_model
        )
        
   
    }
    
    return agents