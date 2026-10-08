import json
import os
import sys
from datetime import date

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("geo-explorer")


def carregar_trilhas():
    caminho = os.path.join(os.path.dirname(__file__), "data", "trilhas.json")
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)["trilhas"]


@mcp.tool()
def trilha(tecnologia: str) -> str:
    """Retorna o plano de estudos de uma trilha de aprendizagem."""
    trilhas = carregar_trilhas()
    tecnologia = tecnologia.lower()

    trilha_encontrada = next((t for t in trilhas if t["id"] == tecnologia), None)

    if not trilha_encontrada:
        disponiveis = ", ".join(t["id"] for t in trilhas)
        return f"Trilha '{tecnologia}' não encontrada. Disponíveis: {disponiveis}"

    modulos = "\n".join(f"  {i+1}. {m}" for i, m in enumerate(trilha_encontrada["modulos"]))
    niveis = "\n".join(
        f"  • {n.capitalize()}: {info['descricao']}"
        for n, info in trilha_encontrada["niveis"].items()
    )

    return (
        f"TRILHA: {trilha_encontrada['nome']}\n\n"
        f"{trilha_encontrada['descricao']}\n\n"
        f"MÓDULOS:\n{modulos}\n\n"
        f"NÍVEIS:\n{niveis}\n\n"
        f"Certificado: {trilha_encontrada['certificado']}"
    )


@mcp.tool()
def desafio(tecnologia: str, nivel: str) -> str:
    """Gera um desafio de código para uma tecnologia e nível informados."""
    trilhas = carregar_trilhas()
    tecnologia = tecnologia.lower()
    nivel = nivel.lower()

    niveis_validos = ["iniciante", "intermediario", "avancado"]
    if nivel not in niveis_validos:
        return f"Nível '{nivel}' inválido. Disponíveis: {', '.join(niveis_validos)}"

    trilha_encontrada = next((t for t in trilhas if t["id"] == tecnologia), None)

    if not trilha_encontrada:
        disponiveis = ", ".join(t["id"] for t in trilhas)
        return f"Trilha '{tecnologia}' não encontrada. Disponíveis: {disponiveis}"

    d = trilha_encontrada["niveis"][nivel]["desafio"]

    return (
        f"DESAFIO: {d['titulo']}\n"
        f"Trilha: {trilha_encontrada['nome']} | Nível: {nivel.capitalize()}\n\n"
        f"{d['enunciado']}\n\n"
        f"💡 Dica: {d['dica']}"
    )


@mcp.tool()
def certificado(nome: str, tecnologia: str) -> str:
    """Gera um certificado fictício de conclusão de trilha."""
    trilhas = carregar_trilhas()
    tecnologia = tecnologia.lower()

    trilha_encontrada = next((t for t in trilhas if t["id"] == tecnologia), None)

    if not trilha_encontrada:
        disponiveis = ", ".join(t["id"] for t in trilhas)
        return f"Trilha '{tecnologia}' não encontrada. Disponíveis: {disponiveis}"

    hoje = date.today().strftime("%d/%m/%Y")

    return (
        f"🏆 CERTIFICADO DE CONCLUSÃO 🏆\n\n"
        f"Certificamos que {nome.upper()} concluiu com êxito a trilha:\n\n"
        f"{trilha_encontrada['certificado']}\n\n"
        f"Módulos concluídos: {len(trilha_encontrada['modulos'])}\n"
        f"Data de conclusão: {hoje}\n\n"
        f"GEO-EXPLORER — Bootcamp IBM Bob | DIO"
    )


if __name__ == "__main__":
    mcp.run()
