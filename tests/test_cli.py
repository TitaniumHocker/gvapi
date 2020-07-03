# -*- coding: utf-8 -*-
from gvapi.cli import cli
from gvapi.hero import requests


def test_help(cli_runner, mocked_get, monkeypatch):
    monkeypatch.setattr(requests, 'get', mocked_get)
    result = cli_runner.invoke(cli, ['--help'])
    assert result.exit_code == 0
    assert 'CLI-интерфейс' in result.output
