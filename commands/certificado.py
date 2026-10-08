import json
import os
from datetime import date


def carregar_trilhas():
    caminho = os.path.join(os.path.dirname(__file__), "..", "data", "trilhas.json")
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)["trilhas"]


def gerar_certificado(nome: str, tecnologia: str):
    trilhas = carregar_trilhas()
    tecnologia = tecnologia.lower()

    trilha = next((t for t in trilhas if t["id"] == tecnologia), None)

    if not trilha:
        disponiveis = ", ".join(t["id"] for t in trilhas)
        print(f"Trilha '{tecnologia}' não encontrada.")
        print(f"Trilhas disponíveis: {disponiveis}")
        return

    hoje = date.today().strftime("%d/%m/%Y")

    print(f"\n{'*'*60}")
    print(f"{'*'*60}")
    print(f"")
    print(f"        🏆  CERTIFICADO DE CONCLUSÃO  🏆")
    print(f"")
    print(f"  Certificamos que")
    print(f"")
    print(f"        ✨  {nome.upper()}  ✨")
    print(f"")
    print(f"  concluiu com êxito a trilha:")
    print(f"")
    print(f"        {trilha['certificado']}")
    print(f"")
    print(f"  Módulos concluídos: {len(trilha['modulos'])}")
    print(f"  Data de conclusão:  {hoje}")
    print(f"")
    print(f"  GEO-EXPLORER — Bootcamp IBM Bob | DIO")
    print(f"")
    print(f"{'*'*60}")
    print(f"{'*'*60}\n")
