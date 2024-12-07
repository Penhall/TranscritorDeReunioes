# Transcritor de Reuniões

Aplicação Python para transcrição automática de reuniões com identificação de palestrantes, geração de resumos e insights. Desenvolvido como parte de projeto acadêmico.

## Recursos

- 🎵 Processamento automático de arquivos de áudio
- 📝 Transcrição usando modelo Whisper
- 👥 Identificação automática de palestrantes
- ✍️ Revisão e correção do texto transcrito
- 📊 Geração de resumos e insights
- 📋 Geração de relatórios formatados

## Pré-requisitos

- Python 3.8 ou superior
- FFmpeg instalado no sistema
- Chave de API da OpenAI
- 4GB+ de RAM recomendado

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/TranscritorDeReunioes.git
cd TranscritorDeReunioes
```

2. Instale o uv (gerenciador de pacotes):
```bash
# No Windows (PowerShell como administrador):
(Invoke-WebRequest -Uri "https://astral.sh/uv/install.ps1" -UseBasicParsing).Content | powershell -c -

# No Linux/MacOS:
curl -LsSf https://astral.sh/uv/install.sh | sh
```

3. Configure o ambiente virtual e instale as dependências:
```bash
uv venv
# Windows:
.venv\Scripts\activate
# Linux/MacOS:
source .venv/bin/activate

uv pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
   - Crie um arquivo `.env` na raiz do projeto
   - Adicione sua chave da API OpenAI:
   ```
   OPENAI_API_KEY=sua-chave-aqui
   ```


5. Configure o Whisper.
O whisper pode ser um pouco complicado de instalar. Vamos fazer passo a passo:

   1) Primeiro, vamos garantir que você tem o Torch instalado (pré-requisito do whisper):
     ```
         uv pip install torch torchvision torchaudio
      ```
   2) Depois, instalar o whisper diretamente do repositório OpenAI:
 ```
      uv pip install git+https://github.com/openai/whisper.git

   3) Instalar as Dependências Necessárias.  Instale o Whisper da OpenAI ou o SpeechRecognition com uma ferramenta como PyDub para lidar com arquivos de áudio.
      ``` 
      pip install openai-whisper pydub SpeechRecognition
      ```


## Estrutura do Projeto

```
TranscritorDeReunioes/
├── tools/              # Ferramentas modulares
├── agents/             # Definições dos agentes
├── tasks/              # Definições das tarefas
├── tests/              # Testes automatizados
├── data/
│   └── audio/         # Diretório para arquivos de áudio
├── output/            # Diretório para arquivos gerados
├── main.py            # Script principal
└── requirements.txt   # Dependências do projeto
```

## Uso

1. Coloque seu arquivo de áudio (.wav) na pasta `data/audio/`

2. Execute o script:
```bash
python main.py
```

3. Selecione o arquivo quando solicitado

4. Os resultados serão salvos na pasta `output/`:
   - `transcricao.md`: Transcrição completa
   - `relatorio_transcricao.md`: Relatório com resumo e insights

## Desenvolvimento

Para executar os testes:
```bash
pytest
```

## Sincronização com Git

- Os arquivos de áudio (.wav) não são sincronizados com o Git
- Mantenha seus arquivos de áudio em backup local
- Não commit arquivos sensíveis ou chaves de API

## Solução de Problemas

1. Erro de API OpenAI:
   - Verifique se a chave está corretamente configurada no arquivo `.env`
   - Verifique se sua chave tem créditos disponíveis

2. Erro de FFmpeg:
   - Certifique-se que o FFmpeg está instalado e acessível no PATH do sistema

3. Erro de memória:
   - Tente com arquivos de áudio menores
   - Verifique a disponibilidade de RAM

## Contribuindo

1. Faça um Fork do projeto
2. Crie sua Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## Créditos

Desenvolvido utilizando:
- OpenAI Whisper para transcrição
- CrewAI para orquestração de agentes
- OpenAI GPT-4 para processamento de linguagem natural