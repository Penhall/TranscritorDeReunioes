# Processo de Execução do Transcritor de Reuniões

## 1. Varredura de Arquivos
- O sistema inicia verificando o diretório `data/audio`
- Lista todos os arquivos com extensão `.wav`
- Se nenhum arquivo for encontrado, exibe mensagem solicitando que arquivos WAV sejam adicionados
- Apresenta lista numerada dos arquivos disponíveis

## 2. Seleção do Arquivo
- Usuário seleciona o arquivo pelo número da lista
- Sistema verifica se a escolha é válida
- Se nenhuma escolha for feita, seleciona o primeiro arquivo
- Converte o caminho do arquivo para formato absoluto

## 3. Preparação do Áudio (Preparador de Áudio)
- Valida existência e formato do arquivo
- Cria diretório temporário `segments` para armazenar partes do áudio
- Normaliza o áudio para qualidade consistente
- Segmenta o arquivo em partes de 10 minutos
- Salva segmentos em formato WAV

## 4. Transcrição (Transcritor)
- Inicializa modelo Whisper
- Processa cada segmento de áudio sequencialmente
- Combina transcrições de todos os segmentos
- Salva transcrição completa em `output/transcricao.md`
- Remove segmentos temporários

## 5. Identificação de Palestrantes
- Analisa o texto transcrito
- Identifica mudanças de palestrantes
- Marca falas com identificadores [Palestrante X]
- Mantém consistência na identificação

## 6. Revisão de Texto
- Corrige formatação e pontuação
- Ajusta capitalização de sentenças
- Remove espaços extras
- Melhora clareza e legibilidade

## 7. Geração de Resumo
- Analisa conteúdo completo
- Identifica pontos principais
- Organiza informações por categorias:
  - Pontos principais
  - Decisões tomadas
  - Tarefas atribuídas

## 8. Análise e Insights
- Identifica padrões no conteúdo
- Analisa tendências nas discussões
- Detecta pontos relevantes
- Gera recomendações

## 9. Relatório Final
- Combina todas as informações em relatório estruturado
- Inclui:
  - Resumo executivo
  - Insights principais
  - Detalhes da análise
- Salva relatório em `output/relatorio_transcricao.md`

## 10. Finalização
- Remove arquivos temporários
- Confirma salvamento dos arquivos finais
- Apresenta mensagem de conclusão
- Exibe localização dos arquivos gerados

O processo é sequencial e cada etapa depende do sucesso da anterior. Em caso de erro em qualquer etapa, o sistema fornece feedback adequado e permite correções ou ajustes conforme necessário.
