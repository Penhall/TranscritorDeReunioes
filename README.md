# Transcritor de Reuniões

Aplicação Python para transcrição automática de reuniões com identificação de palestrantes, análise de toxicidade, geração de resumos e insights. Desenvolvido como parte de projeto acadêmico.

## Autores

Os seguintes autores contribuíram para o desenvolvimento deste projeto:

- **Nome**: Filipe Maruyama Cardili  
  **Email**: filipe.cardili@gmail.com

- **Nome**: Flavio Eustáquio de Oliveira  
  **Email**: flaeuso@hotmail.com

- **Nome**: Reginaldo Santos  
  **Email**: reginaldo.santos@id.uff.br

- **Nome**: Wemerson G. Souza  
  **Email**: wemerson.souza@wganalytics.com.br

---

## Informações do Curso

**Nome do curso**: ePrompts – Engenharia de Prompts  
**Data**: Dezembro 2024

---

## Recursos

- 🎵 Processamento automático de arquivos de áudio
- 🗒 Transcrição usando modelo Faster Whisper
- 👥 Identificação automática de palestrantes
- ✍️ Revisão e correção do texto transcrito
- 🛡️ Análise de toxicidade e moderação de conteúdo usando Guard Rails
- 📊 Geração de resumos e insights
- 📋 Geração de relatórios formatados
- 🔄 Processamento em tempo real
- 📈 Análise de sentimentos e tendências
- 🎯 Detecção de tópicos principais

## Análise de Toxicidade com Guard Rails

O sistema integra a biblioteca Guard Rails para análise avançada de toxicidade e moderação de conteúdo, oferecendo:

- Detecção em tempo real de conteúdo inapropriado
- Análise multicategoria (discurso de ódio, profanidade, assédio)
- Sugestões automáticas de linguagem alternativa
- Relatórios detalhados de análise
- Configurações personalizáveis de moderação
- Integração com fluxo de trabalho existente

## Pré-requisitos

- Python 3.8 ou superior
- FFmpeg instalado no sistema
- Chave de API da OpenAI
- Guard Rails instalado para análise de toxicidade
- 4GB+ de RAM recomendado
- Espaço em disco para modelos de ML

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/TranscritorDeReunioes.git
cd TranscritorDeReunioes
```

2. Configure o ambiente virtual e instale as dependências:
```bash
# Windows:
python -m venv .venv
.venv\Scripts\activate

# Linux/MacOS:
python3 -m venv .venv
source .venv/bin/activate

# Instale as dependências:
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente:
   - Crie um arquivo `.env` na raiz do projeto
   - Adicione suas chaves de API:
   ```
   OPENAI_API_KEY=sua-chave-aqui
   GUARDRAILS_API_KEY=sua-chave-aqui  # Se necessário
   ```

4. Instale as dependências adicionais:
```bash
pip install crewai dotenv langchain-openai faster-whisper guard-rails-ml
```

5. Configure o Guard Rails:
   - Crie um arquivo `guardrails_config.yml` na raiz do projeto:
   ```yaml
   policies:
     toxicity:
       threshold: 0.7
       categories:
         - hate_speech
         - profanity
         - harassment
         - discrimination
     content_quality:
       professional_language: true
       business_appropriate: true
   actions:
     flag_content: true
     suggest_alternatives: true
     provide_explanation: true
   ```

6. Certifique-se de que o FFmpeg está instalado e configurado no PATH do sistema.

## Estrutura do Projeto

```
TranscritorDeReunioes/
├── src/                # Código-fonte principal
├── tools/              # Ferramentas modulares
│   ├── audio_tools/    # Processamento de áudio
│   ├── toxic_tools/    # Análise de toxicidade
│   └── report_tools/   # Geração de relatórios
├── agents/             # Definições dos agentes
├── tasks/              # Definições das tarefas
├── configs/            # Arquivos de configuração
│   └── guardrails/     # Configurações do Guard Rails
├── data/
│   └── audio/         # Diretório para arquivos de áudio
├── output/            # Diretório para arquivos gerados
├── tests/             # Testes automatizados
├── main.py            # Script principal
├── requirements.txt   # Dependências do projeto
└── guardrails_config.yml  # Configuração do Guard Rails
```

## Uso

1. Coloque seus arquivos de áudio (.wav) na pasta `data/audio/`.

2. Execute o script principal:
```bash
python main.py
```

3. O programa listará os arquivos disponíveis na pasta e permitirá que você escolha qual processar.

4. Os resultados serão salvos na pasta `output/`:
   - `transcricao.md`: Transcrição completa
   - `analise_toxicidade.md`: Relatório de análise de toxicidade
   - `relatorio_transcricao.md`: Relatório com resumo e insights

## Configuração do Guard Rails

### Níveis de Sensibilidade

O Guard Rails pode ser configurado com diferentes níveis de sensibilidade:

```python
# Exemplo de configuração no código
toxicity_guard = Guard.from_config({
    "policies": {
        "toxicity": {
            "threshold": 0.7,  # Ajuste conforme necessário (0.0 a 1.0)
            "categories": ["hate_speech", "profanity", "harassment"]
        }
    }
})
```

### Categorias de Análise

- Discurso de ódio
- Profanidade
- Assédio
- Discriminação
- Linguagem inapropriada
- Tons agressivos

### Personalização

Você pode personalizar as políticas de moderação editando o arquivo `guardrails_config.yml`.

## Desenvolvimento

Para executar os testes:
```bash
pytest
```

Para adicionar novos tipos de análise:
1. Crie uma nova política no arquivo de configuração
2. Implemente a lógica de análise correspondente
3. Atualize o agente de toxicidade conforme necessário

## Solução de Problemas

1. **Erro de API OpenAI:**
   - Verifique se a chave está corretamente configurada no arquivo `.env`
   - Verifique se sua chave tem créditos disponíveis

2. **Erro de FFmpeg:**
   - Certifique-se de que o FFmpeg está instalado e acessível no PATH do sistema

3. **Erro de memória:**
   - Tente com arquivos de áudio menores
   - Verifique a disponibilidade de RAM

4. **Erro de dependências:**
   - Garanta que o ambiente virtual está ativado
   - Todas as dependências foram instaladas corretamente

5. **Erros do Guard Rails:**
   - Verifique se o arquivo de configuração está corretamente formatado
   - Confirme se todas as dependências do Guard Rails estão instaladas
   - Verifique os logs para mensagens de erro específicas

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
- Faster Whisper para transcrição
- CrewAI para orquestração de agentes e tarefas
- OpenAI GPT-4 para processamento de linguagem natural
- Guard Rails para análise de toxicidade e moderação de conteúdo
- FFmpeg para processamento de áudio

## Versão

Versão atual: 1.0.0

## Suporte

Para suporte, por favor abra uma issue no repositório do projeto.
