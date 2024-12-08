# Versão 1 - Básica com temperaturefrom crewai import Agent
from langchain_openai import ChatOpenAI

# Importando tools da nova estrutura
from transcritor.tools.audio_tools import audio_toolkit
from transcritor.tools.transcription_tools import transcribe_audio
from transcritor.tools.speaker_tools import speaker_identification_tool
from transcritor.tools.text_tools import text_editing_tool
from transcritor.tools.report_tools import report_generation_tool
from transcritor.tools.toxic_tools import analyze_toxicity

def create_agents(gpt_model: ChatOpenAI) -> dict:
    agents = {
        'preparador_audio': Agent(
            role='Preparador de Audio',
            goal='Processar e preparar arquivos de áudio para transcrição eficiente',
            backstory="Especialista em processamento de áudio com foco em qualidade de som",
            temperature=0.3,  # Baixa - precisão no processamento
            tools=[audio_toolkit],
            llm=gpt_model
        ),
        
        'transcritor': Agent(
            role='Transcritor',
            goal='Transformar áudio em texto com alta precisão e clareza',
            backstory="Especialista em reconhecimento de fala e transcrição automática",
            temperature=0.2,  # Muito baixa - máxima precisão
            tools=[transcribe_audio],
            llm=gpt_model
        ),
        
        'identificador_palestrantes': Agent(
            role='Identificador de Palestrantes',
            goal='Identificar e marcar diferentes vozes na transcrição',
            backstory="Especialista em análise de padrões de fala e reconhecimento de vozes",
            temperature=0.4,  # Média-baixa - equilíbrio
            tools=[speaker_identification_tool],
            llm=gpt_model
        ),
        
        'revisor_texto': Agent(
            role='Revisor de Texto',
            goal='Aprimorar a qualidade e clareza do texto transcrito',
            backstory="Especialista em revisão e formatação de textos",
            temperature=0.3,  # Baixa - precisão na revisão
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
            temperature=0.3,  # Baixa temperatura para análises mais precisas
            llm=gpt_model
        ),
        
        'resumidor': Agent(
            role='Resumidor',
            goal='Criar resumos concisos e informativos',
            backstory="Especialista em síntese de informações e análise textual",
            temperature=0.6,  # Média-alta - criatividade na síntese
            llm=gpt_model
        ),
        
        'gerador_insights': Agent(
            role='Gerador de Insights',
            goal='Extrair padrões e informações relevantes do texto',
            backstory="Especialista em análise de dados e identificação de padrões",
            temperature=0.7,  # Alta - criatividade nos insights
            llm=gpt_model
        ),
        
        'formulador_relatorios': Agent(
            role='Formulador de Relatórios',
            goal='Criar relatórios estruturados e informativos',
            backstory="Especialista em documentação e formatação de relatórios",
            temperature=0.4,  # Média-baixa - equilíbrio
            tools=[report_generation_tool],
            llm=gpt_model
        )      
          
    }
    return agents