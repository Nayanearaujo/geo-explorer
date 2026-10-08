import json
import os


def carregar_trilhas():
    caminho = os.path.join(os.path.dirname(__file__), "..", "data", "trilhas.json")
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)["trilhas"]


def exibir_desafio(tecnologia: str, nivel: str):
    trilhas = carregar_trilhas()
    tecnologia = tecnologia.lower()
    nivel = nivel.lower()

    niveis_validos = ["iniciante", "intermediario", "avancado"]
    if nivel not in niveis_validos:
        print(f"Nível '{nivel}' inválido.")
        print(f"Níveis disponíveis: {', '.join(niveis_validos)}")
        return

    trilha = next((t for t in trilhas if t["id"] == tecnologia), None)

    if not trilha:
        disponiveis = ", ".join(t["id"] for t in trilhas)
        print(f"Trilha '{tecnologia}' não encontrada.")
        print(f"Trilhas disponíveis: {disponiveis}")
        return

    desafio = trilha["niveis"][nivel]["desafio"]

    print(f"\n{'='*50}")
    print(f"  DESAFIO: {desafio['titulo']}")
    print(f"  Trilha: {trilha['nome']} | Nível: {nivel.capitalize()}")
    print(f"{'='*50}")
    print(f"\n{desafio['enunciado']}\n")
    print(f"💡 Dica: {desafio['dica']}")
    print(f"\n{'='*50}\n")
