import pytest
import clidir

def test_no_args_shows_help(capsys):
    clidir.run([])
    
    captured = capsys.readouterr()
    assert "[-h] command" in captured.out


def test_invalid_command_shows_help(capsys):
    clidir.run(['invalid', 'command'])
    
    captured = capsys.readouterr()
    assert "[-h] command" in captured.out