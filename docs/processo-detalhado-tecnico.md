# Processo Técnico de Execução do Transcritor de Reuniões

## 1. Inicialização e Varredura (main.py)
- Função principal: `main()`
- Configuração de diretórios usando `Path` do `pathlib`:
  ```python
  audio_dir = BASE_DIR / "data" / "audio"
  output_dir = BASE_DIR / "output"
  ```
- Varredura de arquivos WAV:
  ```python
  arquivos_wav = list(audio_dir.glob("*.wav"))
  ```

## 2. Preparação do Áudio
**Agente**: `preparador_audio`
**Ferramenta**: `audio_toolkit` de `tools/audio_tools.py`
**Função Principal**: 
```python
@tool
def audio_toolkit(file_path: str, output_format: str = "wav", segment_duration: int = 600)
```
- Utiliza `pydub.AudioSegment` para carregar áudio
- `pydub.effects.normalize` para normalização
- Cria segmentos usando slice do AudioSegment

## 3. Transcrição
**Agente**: `transcritor`
**Ferramenta**: `transcribe_audio` de `tools/transcription_tools.py`
**Função Principal**:
```python
@tool
def transcribe_audio(file_path: str, output_dir: str = "./output")
```
- Usa modelo `whisper.load_model("base")`
- Processa cada segmento com `model.transcribe()`
- Salva resultado em Markdown

## 4. Identificação de Palestrantes
**Agente**: `identificador_palestrantes`
**Ferramenta**: `speaker_identification_tool` de `tools/speaker_tools.py`
**Função Principal**:
```python
@tool
def speaker_identification_tool(transcription: str)
```
- Analisa padrões de fala no texto
- Marca falas com identificadores de palestrantes

## 5. Revisão de Texto
**Agente**: `revisor_texto`
**Ferramenta**: `text_editing_tool` de `tools/text_tools.py`
**Função Principal**:
```python
@tool
def text_editing_tool(text: str)
```
- Processa texto usando string operations
- Aplica correções de formatação e capitalização

## 6. Geração de Resumo
**Agente**: `resumidor`
**Backstory**: "Especialista em análise textual e síntese de informações"
- Utiliza LLM (GPT-4) para análise
- Não possui ferramenta específica, trabalha diretamente com o texto

## 7. Geração de Insights
**Agente**: `gerador_insights`
**Backstory**: "Especialista em análise de dados qualitativos"
- Utiliza LLM (GPT-4) para análise
- Não possui ferramenta específica, trabalha com o conteúdo processado

## 8. Geração de Relatório
**Agente**: `formulador_relatorios`
**Ferramenta**: `report_generation_tool` de `tools/report_tools.py`
**Função Principal**:
```python
@tool
def report_generation_tool(summary: str, insights: str = "", output_dir: str = "./output")
```
- Combina informações em formato Markdown
- Salva relatório final

## 9. Orquestração do Processo
**Classe**: `Crew` do CrewAI
**Configuração**:
```python
crew_audio_para_relatorio = Crew(
    agents=[preparador_audio, transcritor, ...],
    tasks=[tarefa_preparacao_audio, tarefa_transcricao, ...],
    process=Process.sequential
)
```

## 10. Gestão de Erros e Logs
- Tratamento de erros com try/except em cada ferramenta
- Feedback detalhado em cada etapa
- Sistema de logging incorporado no CrewAI
- Mensagens de status em tempo real

## 11. Estrutura de Arquivos
```
TranscritorDeReunioes/
├── tools/              # Ferramentas modulares (.py)
├── agents/             # Definições dos agentes (.py)
├── tasks/              # Definições das tarefas (.py)
├── data/audio/         # Arquivos de entrada (.wav)
└── output/             # Arquivos gerados (.md)
```

## 12. Dependências Principais
- `crewai`: Orquestração de agentes
- `whisper`: Transcrição de áudio
- `pydub`: Processamento de áudio
- `langchain_openai`: Integração com GPT-4
- `pathlib`: Manipulação de caminhos
- `python-dotenv`: Gestão de variáveis de ambiente

Cada componente é modular e testável independentemente, permitindo manutenção e atualizações isoladas.
