import pytest
from pathlib import Path

import clidir


def test_no_args_shows_help(capsys):
    clidir.run(['cli'])
    
    captured = capsys.readouterr()
    assert "cli [-h] command" in captured.out


def test_invalid_command_shows_help(capsys):
    clidir.run(['cli', 'invalid', 'command'])
    
    captured = capsys.readouterr()
    assert "cli [-h] command" in captured.out


@pytest.fixture
def base_path() -> Path:
    """Get the current folder of the test"""
    return Path(__file__).parent


def test_subcommand_no_args_shows_help(base_path: Path, monkeypatch: pytest.MonkeyPatch, capsys):
    monkeypatch.chdir(base_path)
    
    clidir.run(['cli', 'hello'])
    captured = capsys.readouterr()
    assert "cli hello [-h] command" in captured.out

    clidir.run(['cli', 'hello', 'abcd'])
    captured = capsys.readouterr()
    assert "cli hello [-h] command" in captured.out

    clidir.run(['cli', 'hello', 'perso'])
    captured = capsys.readouterr()
    assert "cli hello [-h] command" in captured.out

    with pytest.raises(SystemExit) as e:
        clidir.run(['cli', 'hello', 'person'])

    assert e.type == SystemExit
    assert e.value.code == 2

    captured = capsys.readouterr()
    assert "cli hello person [-h] name" in captured.err


def test_subcommand_valid_args(base_path: Path, monkeypatch: pytest.MonkeyPatch, capsys):
    monkeypatch.chdir(base_path)
    
    clidir.run(['cli', 'hello', 'person', 'John'])
    captured = capsys.readouterr()
    assert "Hello John" in captured.out