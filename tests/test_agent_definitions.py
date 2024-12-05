import pytest
from crewai import Agent
from langchain_openai import ChatOpenAI
from agents.agent_definitions import create_agents

@pytest.fixture
def gpt_model():
    return ChatOpenAI(model_name='gpt-4')

def test_create_agents_returns_dict(gpt_model):
    """Testa se create_agents retorna um dicionário"""
    agents = create_agents(gpt_model)
    assert isinstance(agents, dict)

def test_all_agents_created(gpt_model):
    """Testa se todos os agentes esperados foram criados"""
    agents = create_agents(gpt_model)
    expected_agents = [
        'preparador_audio',
        'transcritor',
        'identificador_palestrantes',
        'revisor_texto',
        'resumidor',
        'gerador_insights',
        'formulador_relatorios'
    ]
    assert all(name in agents for name in expected_agents)

def test_agents_are_agent_instances(gpt_model):
    """Testa se todos os valores no dicionário são instâncias de Agent"""
    agents = create_agents(gpt_model)
    assert all(isinstance(agent, Agent) for agent in agents.values())

def test_agents_have_required_attributes(gpt_model):
    """Testa se os agentes têm os atributos necessários"""
    agents = create_agents(gpt_model)
    for agent in agents.values():
        assert hasattr(agent, 'role')
        assert hasattr(agent, 'goal')
        assert hasattr(agent, 'backstory')
        assert hasattr(agent, 'llm')
