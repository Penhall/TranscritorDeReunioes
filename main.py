import sys
from pathlib import Path
import shutil

# Adicionar o diretório src ao PYTHONPATH
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR / "src"))

from dotenv import load_dotenv
from crewai import Crew, Process
from langchain_openai import ChatOpenAI
import os

# Importando as definições modularizadas
from transcritor.agents.agent_definitions6 import create_agents
from transcritor.tasks.task_definitions import create_tasks

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

def initialize_model():
    """Inicializa o modelo OpenAI"""
    try:
        return ChatOpenAI(model_name='gpt-4')
    except Exception as e:
        print(f"Erro ao inicializar o modelo OpenAI: {e}")
        print("Verifique se sua OPENAI_API_KEY está configurada corretamente no arquivo .env")
        sys.exit(1)

def create_crew(agents_dict, tasks_dict):
    """Cria a crew com os agentes e tarefas"""
    return Crew(
        agents=list(agents_dict.values()),
        tasks=list(tasks_dict.values()),
        process=Process.sequential
    )

def cleanup_segments(audio_dir: Path) -> None:
    """
    Remove o diretório de segmentos e seus arquivos.
    Args:
        audio_dir: Diretório base de áudio
    """
    try:
        segments_dir = audio_dir / "segments"
        if segments_dir.exists():
            shutil.rmtree(segments_dir)
            print(f"\nDiretório de segmentos removido com sucesso: {segments_dir}")
    except Exception as e:
        print(f"\nErro ao remover diretório de segmentos: {e}")

def main():
    try:
        # Inicialização
        gpt_model = initialize_model()
        agents = create_agents(gpt_model)
        tasks = create_tasks(agents)
        crew = create_crew(agents, tasks)
        
        # Configurar diretórios
        audio_dir = BASE_DIR / "data" / "audio"
        audio_dir.mkdir(parents=True, exist_ok=True)
        
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
        print(f"Iniciando processamento do arquivo: {caminho_arquivo}")
        
        result = crew.kickoff(
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
    
    finally:
        # Limpar segmentos no final da execução, independentemente do resultado
        cleanup_segments(audio_dir)

if __name__ == "__main__":
    main()