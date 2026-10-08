import pytest
import sys
import os
from io import StringIO

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from commands.trilha import exibir_trilha
from commands.desafio import exibir_desafio
from commands.certificado import gerar_certificado


# ──────────────────────────────────────────────
# Testes: comando trilha
# ──────────────────────────────────────────────

def test_trilha_python(capsys):
    exibir_trilha("python")
    captured = capsys.readouterr()
    assert "Python" in captured.out
    assert "MÓDULOS" in captured.out


def test_trilha_javascript(capsys):
    exibir_trilha("javascript")
    captured = capsys.readouterr()
    assert "JavaScript" in captured.out
    assert "MÓDULOS" in captured.out


def test_trilha_dados(capsys):
    exibir_trilha("dados")
    captured = capsys.readouterr()
    assert "Ciência de Dados" in captured.out


def test_trilha_inexistente(capsys):
    exibir_trilha("ruby")
    captured = capsys.readouterr()
    assert "não encontrada" in captured.out
    assert "disponíveis" in captured.out


# ──────────────────────────────────────────────
# Testes: comando desafio
# ──────────────────────────────────────────────

def test_desafio_python_iniciante(capsys):
    exibir_desafio("python", "iniciante")
    captured = capsys.readouterr()
    assert "DESAFIO" in captured.out
    assert "Dica" in captured.out


def test_desafio_javascript_avancado(capsys):
    exibir_desafio("javascript", "avancado")
    captured = capsys.readouterr()
    assert "DESAFIO" in captured.out


def test_desafio_nivel_invalido(capsys):
    exibir_desafio("python", "expert")
    captured = capsys.readouterr()
    assert "inválido" in captured.out


def test_desafio_trilha_inexistente(capsys):
    exibir_desafio("cobol", "iniciante")
    captured = capsys.readouterr()
    assert "não encontrada" in captured.out


# ──────────────────────────────────────────────
# Testes: comando certificado
# ──────────────────────────────────────────────

def test_certificado_nome_aparece(capsys):
    gerar_certificado("Nayane Araujo", "python")
    captured = capsys.readouterr()
    assert "NAYANE ARAUJO" in captured.out


def test_certificado_trilha_aparece(capsys):
    gerar_certificado("Nayane Araujo", "dados")
    captured = capsys.readouterr()
    assert "Ciência de Dados" in captured.out


def test_certificado_trilha_inexistente(capsys):
    gerar_certificado("Nayane Araujo", "ruby")
    captured = capsys.readouterr()
    assert "não encontrada" in captured.out
