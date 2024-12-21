# Versão 2 - Intermediária
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
    agents = {
        'preparador_audio': Agent(
            role='Preparador de Áudio',
            goal='Otimizar a qualidade do áudio através de normalização, segmentação e redução de ruídos, garantindo a melhor entrada possível para transcrição',
            backstory="Engenheiro de áudio com 15 anos de experiência em processamento digital de sinais e otimização de qualidade sonora para sistemas de reconhecimento de fala",
            temperature=0.3,
            tools=[audio_toolkit],
            llm=gpt_model
        ),
        
        'transcritor': Agent(
            role='Transcritor',
            goal='Converter áudio em texto com precisão superior a 95%, mantendo pontuação adequada e identificando nuances de fala como pausas e ênfases',
            backstory="Linguista computacional especializado em sistemas de reconhecimento de fala, com profundo conhecimento em modelos de linguagem e processamento de áudio",
            temperature=0.2,
            tools=[transcribe_audio],
            llm=gpt_model
        ),
        
        'identificador_palestrantes': Agent(
            role='Identificador de Palestrantes',
            goal='Identificar palestrantes com base em padrões de fala, vocabulário e contexto, mantendo consistência nas atribuições ao longo do texto',
            backstory="Pesquisador em reconhecimento de padrões vocais com experiência em análise forense de áudio e identificação de falantes",
            temperature=0.4,
            tools=[speaker_identification_tool],
            llm=gpt_model
        ),
        
        'revisor_texto': Agent(
            role='Revisor de Texto',
            goal='Aperfeiçoar o texto mantendo a fidelidade ao original, corrigindo erros e melhorando a clareza sem alterar o significado das falas',
            backstory="Editor profissional com especialização em revisão de transcrições e documentos técnicos, focado em manter a autenticidade do discurso",
            temperature=0.3,
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
            temperature=0.4,  # Baixa temperatura para análises mais precisas
            llm=gpt_model
        ),
        
        'resumidor': Agent(
            role='Resumidor',
            goal='Criar resumos que capturam os pontos principais, decisões e ações definidas, organizando as informações em uma estrutura clara e acessível',
            backstory="Analista de informações com experiência em documentação executiva e síntese de reuniões corporativas de alto nível",
            temperature=0.6,
            llm=gpt_model
        ),
        
        'gerador_insights': Agent(
            role='Gerador de Insights',
            goal='Analisar profundamente o conteúdo para identificar tendências, padrões de comportamento e oportunidades de melhoria não evidentes',
            backstory="Consultor estratégico com background em análise comportamental e tomada de decisão em ambientes corporativos",
            temperature=0.7,
            llm=gpt_model
        ),
        
        'formulador_relatorios': Agent(
            role='Formulador de Relatórios',
            goal='Sintetizar todas as análises em um relatório coeso, bem estruturado e acionável, com seções claras e recomendações práticas',
            backstory="Especialista em comunicação executiva com experiência em documentação de projetos complexos e relatórios estratégicos",
            temperature=0.4,
            tools=[report_generation_tool],
            llm=gpt_model
        )
        

    }
    return agents