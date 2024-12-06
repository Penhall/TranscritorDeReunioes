## BIBLIOTECAS, LLM´S E OUTRAS FERRAMENTAS NECESSÁRIAS AO FUNCIONAMENTO DA APLICAÇÃO
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from crewai_tools import FileReadTool, tool
import whisper
from langchain_openai import ChatOpenAI
from pydub import AudioSegment
from pydub.effects import normalize
import os
import sys
from pathlib import Path

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Obter diretório base da aplicação
BASE_DIR = Path(__file__).resolve().parent

# DEFINIÇÃO DE FERRAMENTAS
@tool
def audio_toolkit(file_path: str, output_format: str = "wav", segment_duration: int = 600) -> str:
    """
    Prepara o arquivo de áudio para transcrição.
    Args:
        file_path: Caminho para o arquivo de áudio
        output_format: Formato de saída (padrão: wav)
        segment_duration: Duração de cada segmento em segundos (padrão: 600)
    Returns:
        str: Mensagem indicando sucesso e localização dos segmentos
    Raises:
        FileNotFoundError: Se o arquivo não for encontrado
        Exception: Para outros erros de processamento
    """
    try:
        # Validar e resolver o caminho do arquivo
        file_path = str(Path(file_path).resolve())
        print(f"Processando arquivo de áudio: {file_path}")

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
        
        # Preparar diretório de saída
        output_dir = Path(file_path).parent / "segments"
        output_dir.mkdir(exist_ok=True)
        print(f"Diretório de segmentos: {output_dir}")

        # Carregar e normalizar o áudio
        print("Carregando e normalizando áudio...")
        audio = AudioSegment.from_file(file_path)
        normalized_audio = normalize(audio)
        
        # Segmentar o áudio
        print("Segmentando áudio...")
        segment_count = 0
        for i in range(0, len(normalized_audio), segment_duration * 1000):
            segment = normalized_audio[i:i + segment_duration * 1000]
            segment_path = output_dir / f"segment_{segment_count}.{output_format}"
            segment.export(str(segment_path), format=output_format)
            print(f"Segmento {segment_count} criado: {segment_path}")
            segment_count += 1

        return f"Áudio processado com sucesso. {segment_count} segmentos salvos em: {output_dir}"
    
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Erro de arquivo: {str(e)}")
    except Exception as e:
        raise Exception(f"Erro no processamento do áudio: {str(e)}")

@tool
def transcribe_audio(file_path: str, output_dir: str = "./output") -> str:
    """
    Transcreve um arquivo de áudio para texto usando Whisper e salva em Markdown.
    Após a conclusão, exclui os segmentos gerados.
    Args:
        file_path: Caminho do arquivo de áudio original.
        output_dir: Diretório onde o arquivo será salvo (padrão: ./output).
    Returns:
        str: Caminho do arquivo Markdown gerado.
    """
    try:
        # Inicializar modelo
        print("Inicializando modelo Whisper...")
        model = whisper.load_model("base")
        
        # Localizar segmentos
        segments_dir = Path(file_path).parent / "segments"
        segments = sorted(segments_dir.glob("segment_*.wav"))
        
        if not segments:
            raise FileNotFoundError(f"Nenhum segmento encontrado em: {segments_dir}")
        
        # Transcrever cada segmento
        print(f"Iniciando transcrição de {len(segments)} segmentos...")
        transcribed_texts = []
        
        for i, segment in enumerate(segments, 1):
            print(f"Transcrevendo segmento {i}/{len(segments)}: {segment.name}")
            result = model.transcribe(str(segment))
            transcribed_texts.append(result["text"].strip())
            print(f"Segmento {i} transcrito com sucesso")

        # Combinar resultados
        full_transcription = " ".join(transcribed_texts)
        
        # Salvar no arquivo Markdown
        output_path = Path(output_dir) / "transcricao.md"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(full_transcription)
        
        print(f"Transcrição salva em: {output_path}")
        
        # Excluir segmentos
        print(f"Excluindo segmentos em: {segments_dir}")
        for segment in segments:
            segment.unlink()
        segments_dir.rmdir()  # Remove o diretório vazio

        print("Segmentos excluídos com sucesso.")
        return str(output_path)

    except FileNotFoundError as e:
        raise FileNotFoundError(f"Erro de arquivo: {str(e)}")
    except Exception as e:
        raise Exception(f"Erro na transcrição: {str(e)}")

@tool
def speaker_identification_tool(transcription: str) -> str:
    """
    Identifica diferentes palestrantes no texto transcrito.
    Args:
        transcription: Texto transcrito para identificar palestrantes
    Returns:
        str: Texto com identificação de palestrantes
    Raises:
        ValueError: Se não houver texto para processar
    """
    try:
        if not transcription or not isinstance(transcription, str):
            raise ValueError("Texto inválido para identificação de palestrantes")
        
        print("Identificando palestrantes no texto...")
        
        # Aqui seria implementada a lógica real de identificação de palestrantes
        # Por ora, fazemos uma marcação simples de exemplo
        sentences = transcription.split(". ")
        current_speaker = 1
        marked_sentences = []
        
        for sentence in sentences:
            if sentence.strip():
                marked_sentences.append(f"[Palestrante {current_speaker}] {sentence.strip()}")
                current_speaker = 1 if current_speaker == 2 else 2

        result = ". ".join(marked_sentences)
        print("Identificação de palestrantes concluída")
        return result

    except ValueError as e:
        raise ValueError(f"Erro no texto: {str(e)}")
    except Exception as e:
        raise Exception(f"Erro na identificação de palestrantes: {str(e)}")

@tool
def text_editing_tool(text: str) -> str:
    """
    Revisa e corrige o texto transcrito.
    Args:
        text: Texto para revisar e corrigir
    Returns:
        str: Texto revisado e corrigido
    Raises:
        ValueError: Se não houver texto para processar
    """
    try:
        if not text or not isinstance(text, str):
            raise ValueError("Texto inválido para revisão")
        
        print("Iniciando revisão do texto...")
        
        # Aplicar correções básicas
        edited_text = text.strip()
        # Garantir pontuação correta
        edited_text = ". ".join(s.strip().capitalize() for s in edited_text.split(". "))
        # Corrigir espaços múltiplos
        edited_text = " ".join(edited_text.split())
        
        print("Revisão do texto concluída")
        return edited_text

    except ValueError as e:
        raise ValueError(f"Erro no texto: {str(e)}")
    except Exception as e:
        raise Exception(f"Erro na revisão do texto: {str(e)}")

@tool
def report_generation_tool(summary: str, insights: str = "", output_dir: str = "./output") -> str:
    """
    Gera um relatório formatado da transcrição e salva no diretório output.
    Args:
        summary: Resumo principal do conteúdo.
        insights: Insights adicionais (opcional).
        output_dir: Diretório onde o arquivo será salvo (padrão: ./output).
    Returns:
        str: Caminho do arquivo Markdown gerado.
    """
    try:
        if not summary:
            raise ValueError("Resumo não fornecido para o relatório")
        
        print("Gerando relatório...")
        
        # Estrutura do relatório
        report_sections = [
            "# Relatório da Transcrição",
            "## Resumo",
            summary,
            "",
        ]
        
        if insights:
            report_sections.extend([
                "## Insights",
                insights,
                ""
            ])
        
        # Adicionar título e seções finais
        report_sections.append("# Fim do Relatório")
        report = "\n".join(report_sections)
        
        # Salvar no arquivo Markdown
        output_path = Path(output_dir) / "relatorio_transcricao.md"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(report)
        
        print(f"Relatório salvo em: {output_path}")
        return str(output_path)

    except ValueError as e:
        raise ValueError(f"Erro no conteúdo: {str(e)}")
    except Exception as e:
        raise Exception(f"Erro na geração do relatório: {str(e)}")




# Inicializar o modelo OpenAI
try:
    gpt_model = ChatOpenAI(model_name='gpt-4')
except Exception as e:
    print(f"Erro ao inicializar o modelo OpenAI: {e}")
    print("Verifique se sua OPENAI_API_KEY está configurada corretamente no arquivo .env")
    sys.exit(1)
    
    # DEFINIÇÃO DE AGENTES
preparador_audio = Agent(
    role='Preparador de Áudio',
    goal='Preparar o arquivo de áudio para transcrição, incluindo normalização e segmentação',
    backstory="Você é um especialista em manipulação de áudio, com habilidade para melhorar a qualidade e preparar o arquivo para processamento.",
    verbose=True,
    tools=[audio_toolkit],
    llm=gpt_model
)

transcritor = Agent(
    role='Transcritor',
    goal='Converter áudio em texto utilizando ferramentas avançadas de transcrição',
    backstory="Você é um especialista em transformar áudio em texto preciso, com foco em eficiência e qualidade.",
    verbose=True,
    tools=[transcribe_audio],
    llm=gpt_model
)

identificador_palestrantes = Agent(
    role='Identificador de Palestrantes',
    goal='Identificar e diferenciar os palestrantes na transcrição',
    backstory="Você é um especialista em reconhecimento de voz, capaz de diferenciar palestrantes e rotular falas com precisão.",
    verbose=True,
    tools=[speaker_identification_tool],
    llm=gpt_model
)

revisor_texto = Agent(
    role='Revisor de Texto',
    goal='Revisar a transcrição e corrigir erros ortográficos e estruturais',
    backstory="Você é um especialista em revisar e ajustar textos, garantindo a precisão e fluidez do conteúdo.",
    verbose=True,
    tools=[text_editing_tool],
    llm=gpt_model
)

resumidor = Agent(
    role='Resumidor',
    goal='Gerar resumos detalhados e categorizados a partir da transcrição',
    backstory="Você é um especialista em análise textual, capaz de criar resumos que destacam os pontos principais e organizam informações de forma clara.",
    verbose=True,
    llm=gpt_model
)

gerador_insights = Agent(
    role='Gerador de Insights',
    goal='Analisar o conteúdo da reunião para identificar padrões e oportunidades',
    backstory="Você é um especialista em análise de dados qualitativos, capaz de identificar tendências e fornecer insights valiosos.",
    verbose=True,
    llm=gpt_model
)

formulador_relatorios = Agent(
    role='Formulador de Relatórios',
    goal='Criar relatórios formatados e prontos para apresentação',
    backstory="Você é um especialista em estruturação e formatação de relatórios, garantindo que os dados sejam apresentados de forma clara e visualmente atraente.",
    verbose=True,
    tools=[report_generation_tool],
    llm=gpt_model
)

# DEFINIÇÃO DE TAREFAS

tarefa_preparacao_audio = Task(
    description=f"""
    Realizar verificação do formato do áudio, normalização e segmentação.
    O arquivo de áudio está em: {{file_path}}
    Use exatamente este caminho ao chamar audio_toolkit.
    """,
    expected_output="Arquivo de áudio preparado e segmentado.",
    agent=preparador_audio
)

tarefa_transcricao = Task(
    description="Converter os segmentos de áudio em texto, garantindo que estejam sincronizados com as marcações temporais.",
    expected_output="Texto transcrito com marcações temporais.",
    agent=transcritor
)

tarefa_identificacao_palestrantes = Task(
    description="Identificar os palestrantes na transcrição e atribuir rótulos provisórios com base nas mudanças de voz.",
    expected_output="Transcrição rotulada com identificação de palestrantes.",
    agent=identificador_palestrantes
)

tarefa_revisao_texto = Task(
    description="Revisar a transcrição, corrigindo erros de ortografia, gramática e estrutura, para garantir consistência e clareza.",
    expected_output="Texto revisado e ajustado, pronto para análise.",
    agent=revisor_texto
)

tarefa_resumo = Task(
    description="Analisar a transcrição e gerar um resumo categorizado, incluindo pontos principais, decisões e tarefas atribuídas.",
    expected_output="Resumo detalhado e organizado da reunião.",
    agent=resumidor
)

tarefa_insights = Task(
    description="Analisar o conteúdo da transcrição para identificar padrões, tendências e insights úteis.",
    expected_output="Lista de insights e análises identificadas.",
    agent=gerador_insights
)

tarefa_relatorio = Task(
    description="Organizar o resumo e os insights em um relatório formatado.",
    expected_output="Relatório completo formatado e pronto para entrega.",
    agent=formulador_relatorios
)

# DEFINIÇÃO DO FLUXO
crew_audio_para_relatorio = Crew(
    agents=[
        preparador_audio,
        transcritor,
        identificador_palestrantes,
        revisor_texto,
        resumidor,
        gerador_insights,
        formulador_relatorios
    ],
    tasks=[
        tarefa_preparacao_audio,
        tarefa_transcricao,
        tarefa_identificacao_palestrantes,
        tarefa_revisao_texto,
        tarefa_resumo,
        tarefa_insights,
        tarefa_relatorio
    ],
    process=Process.sequential
)

# RODANDO A APLICAÇÃO
if __name__ == "__main__":


##Alterações para encaminhar para o github
    # Configurar diretórios
    audio_dir = BASE_DIR / "data" / "audio"
    audio_dir.mkdir(parents=True, exist_ok=True)
    
    # Configuração inicial dos diretórios
    output_dir = BASE_DIR / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    
    # Listar arquivos WAV
    arquivos_wav = list(audio_dir.glob("*.wav"))
       
    
    if not arquivos_wav:
        print(f"\nNenhum arquivo .wav encontrado em: {audio_dir}")
        print("Coloque seus arquivos de áudio WAV neste diretório.")
        sys.exit(1)
    
    # Mostrar arquivos disponíveis
    print("\nArquivos disponíveis:")
    for i, arquivo in enumerate(arquivos_wav, 1):
        print(f"{i}. {arquivo.name}")
    
    # Seleção do arquivo
    escolha = input("\nEscolha o número do arquivo (Enter para o primeiro): ").strip()
    
    try:
        if not escolha:
            arquivo_selecionado = arquivos_wav[0]
        else:
            indice = int(escolha) - 1
            arquivo_selecionado = arquivos_wav[indice]
    except (ValueError, IndexError):
        print("Escolha inválida. Usando o primeiro arquivo.")
        arquivo_selecionado = arquivos_wav[0]
    
    # Garantir caminho absoluto
    caminho_arquivo = str(arquivo_selecionado.resolve())
    print(f"\nProcessando: {arquivo_selecionado.name}")
    
    # Executar o processo
    try:
        print(f"Iniciando processamento do arquivo: {caminho_arquivo}")
        
        result = crew_audio_para_relatorio.kickoff(
            inputs={
                "file_path": caminho_arquivo,
                "input_file": caminho_arquivo
            }
        )
        print("\nProcessamento concluído com sucesso.")
        print(result)
    except Exception as e:
        print(f"\nErro durante a execução: {e}")
        sys.exit(1)
    # Configurar diretórios
    audio_dir = BASE_DIR / "data" / "audio"
    audio_dir.mkdir(parents=True, exist_ok=True)
    
    # Listar arquivos WAV
    arquivos_wav = list(audio_dir.glob("*.wav"))
    
    if not arquivos_wav:
        print(f"\nNenhum arquivo .wav encontrado em: {audio_dir}")
        print("Coloque seus arquivos de áudio WAV neste diretório.")
        sys.exit(1)
    
    # Mostrar arquivos disponíveis
    print("\nArquivos disponíveis:")
    for i, arquivo in enumerate(arquivos_wav, 1):
        print(f"{i}. {arquivo.name}")
    
    # Seleção do arquivo
    escolha = input("\nEscolha o número do arquivo (Enter para o primeiro): ").strip()
    
    try:
        arquivo_escolhido = str(arquivo_escolhido.resolve())  # Garante caminho absoluto
        print(f"Iniciando processamento do arquivo: {arquivo_escolhido}")
        
        context = {
            "file_path": arquivo_escolhido,
            "input_file": arquivo_escolhido  # redundância para garantir
        }
        
        result = crew_audio_para_relatorio.kickoff(inputs=context)
        print("\nProcessamento concluído com sucesso.")
        print(result)
    except Exception as e:
        print(f"\nErro durante a execução: {e}")
        sys.exit(1)