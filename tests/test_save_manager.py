import pytest
import json
from unittest.mock import mock_open, patch
from game.save_manager import SaveManager

@pytest.fixture
def mock_scores():
    """Fixture com pontuações simuladas."""
    return {"Alice": 100, "Bob": 200}

def test_save_score_creates_new_file_if_not_exists(mock_scores):
    """
    Testa se um novo arquivo é criado quando não existe e salva a pontuação corretamente.
    """
    mock_open_obj = mock_open(read_data=json.dumps({}))
    with patch("builtins.open", mock_open_obj), patch("json.dump") as mock_dump:
        SaveManager.save_score("Alice", 150)
        mock_dump.assert_called_once_with({"Alice": 150}, mock_open_obj())

def test_save_score_updates_existing_score(mock_scores):
    """
    Testa se a pontuação existente é atualizada apenas quando a nova pontuação é maior.
    """
    mock_open_obj = mock_open(read_data=json.dumps(mock_scores))
    with patch("builtins.open", mock_open_obj), patch("json.dump") as mock_dump:
        SaveManager.save_score("Alice", 120)  # Não deve atualizar, pois é menor
        SaveManager.save_score("Bob", 250)    # Deve atualizar, pois é maior

        expected_scores = {"Alice": 100, "Bob": 250}
        mock_dump.assert_called_with(expected_scores, mock_open_obj())

def test_save_score_creates_new_entry(mock_scores):
    """
    Testa se uma nova entrada é criada corretamente para um jogador inexistente.
    """
    mock_open_obj = mock_open(read_data=json.dumps(mock_scores))
    with patch("builtins.open", mock_open_obj), patch("json.dump") as mock_dump:
        SaveManager.save_score("Charlie", 300)  # Novo jogador

        expected_scores = {"Alice": 100, "Bob": 200, "Charlie": 300}
        mock_dump.assert_called_with(expected_scores, mock_open_obj())

def test_load_scores_returns_empty_if_file_not_exists():
    """
    Testa se o carregamento de pontuações retorna um dicionário vazio quando o arquivo não existe.
    """
    with patch("builtins.open", side_effect=FileNotFoundError):
        scores = SaveManager.load_scores()
    assert scores == {}, "Deveria retornar um dicionário vazio quando o arquivo não existe."

def test_load_scores_returns_correct_scores(mock_scores):
    """
    Testa se o carregamento de pontuações retorna as pontuações corretas de um arquivo existente.
    """
    mock_open_obj = mock_open(read_data=json.dumps(mock_scores))
    with patch("builtins.open", mock_open_obj):
        scores = SaveManager.load_scores()
    assert scores == mock_scores, "As pontuações carregadas estão incorretas."
