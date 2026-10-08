import argparse
from commands.trilha import exibir_trilha
from commands.desafio import exibir_desafio
from commands.certificado import gerar_certificado


def main():
    parser = argparse.ArgumentParser(
        description="Geo-Explorer: explore trilhas de aprendizagem, desafios e certificados."
    )
    subparsers = parser.add_subparsers(dest="comando", help="Comandos disponíveis")

    # Comando: trilha
    parser_trilha = subparsers.add_parser("trilha", help="Exibe uma trilha de estudos")
    parser_trilha.add_argument("tecnologia", help="Tecnologia da trilha (ex: python, javascript, dados)")

    # Comando: desafio
    parser_desafio = subparsers.add_parser("desafio", help="Gera um desafio de código")
    parser_desafio.add_argument("tecnologia", help="Tecnologia do desafio (ex: python)")
    parser_desafio.add_argument("nivel", help="Nível do desafio (iniciante, intermediario, avancado)")

    # Comando: certificado
    parser_cert = subparsers.add_parser("certificado", help="Gera um certificado fictício")
    parser_cert.add_argument("nome", help="Seu nome completo")
    parser_cert.add_argument("tecnologia", help="Tecnologia da trilha concluída (ex: python)")

    args = parser.parse_args()

    if args.comando == "trilha":
        exibir_trilha(args.tecnologia)
    elif args.comando == "desafio":
        exibir_desafio(args.tecnologia, args.nivel)
    elif args.comando == "certificado":
        gerar_certificado(args.nome, args.tecnologia)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
