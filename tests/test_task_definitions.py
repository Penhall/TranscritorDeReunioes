import pytest
from crewai import Task, Agent
from langchain_openai import ChatOpenAI
from tasks.task_definitions import create_tasks
from agents.agent_definitions import create_agents

@pytest.fixture
def gpt_model():
    return ChatOpenAI(model_name='gpt-4')

@pytest.fixture
def agents(gpt_model):
    return create_agents(gpt_model)

def test_create_tasks_returns_dict(agents):
    """Testa se create_tasks retorna um dicionário"""
    tasks = create_tasks(agents)
    assert isinstance(tasks, dict)

def test_all_tasks_created(agents):
    """Testa se todas as tarefas esperadas foram criadas"""
    tasks = create_tasks(agents)
    expected_tasks = [
        'preparacao_audio',
        'transcricao',
        'identificacao_palestrantes',
        'revisao_texto',
        'resumo',
        'insights',
        'relatorio'
    ]
    assert all(name in tasks for name in expected_tasks)

def test_tasks_are_task_instances(agents):
    """Testa se todos os valores no dicionário são instâncias de Task"""
    tasks = create_tasks(agents)
    assert all(isinstance(task, Task) for task in tasks.values())

def test_tasks_have_required_attributes(agents):
    """Testa se as tarefas têm os atributos necessários"""
    tasks = create_tasks(agents)
    for task in tasks.values():
        assert hasattr(task, 'description')
        assert hasattr(task, 'expected_output')
        assert hasattr(task, 'agent')
        assert isinstance(task.agent, Agent)
