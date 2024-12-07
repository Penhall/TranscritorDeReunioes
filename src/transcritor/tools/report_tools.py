from pathlib import Path
from crewai_tools import tool

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
            return "Erro: Resumo não fornecido para o relatório"
        
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

    except Exception as e:
        return f"Erro na geração do relatório: {str(e)}"
