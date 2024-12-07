# Transcritor de Reuniões

Aplicação Python para transcrição automática de reuniões com identificação de palestrantes, geração de resumos e insights. Desenvolvido como parte de projeto acadêmico.

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
   - Adicione sua chave da API OpenAI:
   ```
   OPENAI_API_KEY=sua-chave-aqui
   ```

4. Instale as dependências adicionais:
```bash
pip install crewai dotenv langchain-openai faster-whisper
```

5. Certifique-se de que o FFmpeg está instalado e configurado no PATH do sistema.

## Estrutura do Projeto

```
TranscritorDeReunioes/
├── src/                # Código-fonte principal
├── tools/              # Ferramentas modulares
├── agents/             # Definições dos agentes
├── tasks/              # Definições das tarefas
├── data/
│   └── audio/         # Diretório para arquivos de áudio
├── output/            # Diretório para arquivos gerados
├── main.py            # Script principal
└── requirements.txt   # Dependências do projeto
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
   - `relatorio_transcricao.md`: Relatório com resumo e insights

## Desenvolvimento

Para executar os testes:
```bash
pytest
```

## Solução de Problemas

1. **Erro de API OpenAI:**
   - Verifique se a chave está corretamente configurada no arquivo `.env`.
   - Verifique se sua chave tem créditos disponíveis.

2. **Erro de FFmpeg:**
   - Certifique-se de que o FFmpeg está instalado e acessível no PATH do sistema.

3. **Erro de memória:**
   - Tente com arquivos de áudio menores.
   - Verifique a disponibilidade de RAM.

4. **Erro de dependências:**
   - Garanta que o ambiente virtual está ativado e que todas as dependências foram instaladas corretamente.

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

