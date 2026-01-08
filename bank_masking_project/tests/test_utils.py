from bank_masking_project.src.utils import load_transactions_from_json
from unittest.mock import patch


def test_file_not_found():
    """Тест случая, когда файл не существует"""
    with patch('bank_masking_project.src.utils.os.path.exists', return_value=False) as mock_exists:
        result = load_transactions_from_json("non_existent.json")

        mock_exists.assert_called_once_with("non_existent.json")
        assert result == []
