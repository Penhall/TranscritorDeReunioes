from crewai_tools import tool
import requests

@tool
def analyze_toxicity(text: str) -> dict:
    """
    Analisa o texto em busca de linguagem tóxica usando GuardRails AI.
    Args:
        text: Texto para analisar
    Returns:
        dict: Resultado da análise de toxicidade
    """
    try:
        # Endpoint da API GuardRails
        url = "https://api.guardrailsai.com/v1/analyze"
        
        # Configuração do header com sua API key
        headers = {
            "Authorization": f"Bearer {os.getenv('GUARDRAILS_API_KEY')}",
            "Content-Type": "application/json"
        }
        
        # Dados para análise
        data = {
            "text": text,
            "validator": "ToxicLanguage"
        }
        
        # Fazer requisição
        response = requests.post(url, headers=headers, json=data)
        result = response.json()
        
        # Processar resultados
        analysis_summary = {
            "toxicity_detected": result.get("toxicity_detected", False),
            "toxicity_score": result.get("toxicity_score", 0),
            "categories": result.get("categories", []),
            "recommendations": result.get("recommendations", [])
        }
        
        return {
            "success": True,
            "analysis": analysis_summary
        }

    except Exception as e:
        return {
            "success": False,
            "error": f"Erro na análise de toxicidade: {str(e)}"
        }
