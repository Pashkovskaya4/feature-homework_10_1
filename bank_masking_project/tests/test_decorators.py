from bank_masking_project.src.decorators import log


def test_log_decorator_stdout(capsys):
    """Тест декоратора log: проверка вывода в stdout при успешном выполнении функции"""
    @log()
    def test_func(a, b):
        return a + b
    result = test_func(2, 3)

    assert result == 5

    captured = capsys.readouterr()
    output = captured.out

    assert "test_func started" in output
    assert "test_func finished" in output
    assert "test_func ok" in output
    assert "error" not in output

