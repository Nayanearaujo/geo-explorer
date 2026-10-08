import json
import os


def carregar_trilhas():
    caminho = os.path.join(os.path.dirname(__file__), "..", "data", "trilhas.json")
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)["trilhas"]


def exibir_trilha(tecnologia: str):
    trilhas = carregar_trilhas()
    tecnologia = tecnologia.lower()

    trilha = next((t for t in trilhas if t["id"] == tecnologia), None)

    if not trilha:
        disponiveis = ", ".join(t["id"] for t in trilhas)
        print(f"Trilha '{tecnologia}' não encontrada.")
        print(f"Trilhas disponíveis: {disponiveis}")
        return

    print(f"\n{'='*50}")
    print(f"  TRILHA: {trilha['nome']}")
    print(f"{'='*50}")
    print(f"\n{trilha['descricao']}\n")
    print("MÓDULOS:")
    for i, modulo in enumerate(trilha["modulos"], 1):
        print(f"  {i}. {modulo}")

    print("\nNÍVEIS DISPONÍVEIS:")
    for nivel, info in trilha["niveis"].items():
        print(f"  • {nivel.capitalize()}: {info['descricao']}")

    print(f"\nCertificado: {trilha['certificado']}")
    print(f"{'='*50}\n")
