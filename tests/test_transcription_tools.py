import pytest
from pathlib import Path
from crewai_tools import Tool
# Corrigindo o import para usar o caminho correto do módulo
from transcritor.tools.transcription_tools import transcribe_audio
import numpy as np
import soundfile as sf

@pytest.fixture
def sample_wav(tmp_path):
    """Cria um arquivo WAV simples para teste"""
    audio_dir = tmp_path / "audio"
    audio_dir.mkdir(parents=True)
    segments_dir = audio_dir / "segments"
    segments_dir.mkdir()
    
    # Criar dois segmentos simples
    for i in range(2):
        # Gerar 1 segundo de silêncio
        data = np.zeros(16000)  # 1 segundo a 16kHz
        sf.write(
            segments_dir / f"segment_{i:02d}.wav",
            data,
            16000
        )
    
    return audio_dir

def test_transcribe_audio_basic(sample_wav):
    """Teste básico da função de transcrição"""
    result = transcribe_audio.run(
        file_path=str(sample_wav),
        output_dir=str(sample_wav / "output")
    )
    
    assert result["success"]
    assert "file_path" in result
    assert "content" in result

def test_transcribe_audio_no_segments():
    """Testa o caso de não encontrar segmentos"""
    result = transcribe_audio.run(
        file_path="./pasta_que_nao_existe",
        output_dir="./output"
    )
    
    assert not result["success"]
    assert "error" in result

def test_transcribe_audio_is_tool():
    """Verifica se transcribe_audio é uma Tool do CrewAI"""
    assert isinstance(transcribe_audio, Tool)