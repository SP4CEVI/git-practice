"""Интеграционный тест: запуск калькулятора с подставленным вводом"""
import main


def test_main_multiply(monkeypatch, capsys):
    answers = iter(["3", "*", "4"])
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(answers))
    main.main()
    assert "Результат: 12.0" in capsys.readouterr().out
