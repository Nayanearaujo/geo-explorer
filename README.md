# 🌍 Geo-Explorer

Plataforma CLI para exploração de trilhas de aprendizagem, com geração de desafios de código e certificados fictícios.

Projeto desenvolvido como desafio do **Bootcamp IBM Bob** na [DIO](https://dio.me).

---

## 📋 O que é o Geo-Explorer?

O Geo-Explorer é uma ferramenta de linha de comando (CLI) que simula uma plataforma de aprendizagem. A pessoa usuária pode:

- Consultar uma **trilha de estudos** com módulos e níveis
- Receber um **desafio de código** conforme a tecnologia e o nível
- Gerar um **certificado fictício** de conclusão

O projeto também expõe um **Servidor MCP**, permitindo que assistentes de IA (como o IBM Bob / Claude) acessem os recursos do Geo-Explorer como ferramentas.

---

## 🗂️ Estrutura do Projeto

```
geo-explorer/
├── data/
│   └── trilhas.json        # Base de trilhas fictícias
├── commands/
│   ├── trilha.py           # Comando: exibe trilha de estudos
│   ├── desafio.py          # Comando: gera desafio de código
│   └── certificado.py      # Comando: gera certificado fictício
├── tests/
│   └── test_commands.py    # Testes automatizados com pytest
├── docs/                   # Documentação adicional
├── main.py                 # Ponto de entrada do CLI
├── server.py               # Servidor MCP
└── requirements.txt        # Dependências
```

---

## ⚙️ Como executar o projeto

### Pré-requisitos

- Python 3.8+

### Instalação

```bash
git clone https://github.com/Nayanearaujo/geo-explorer.git
cd geo-explorer
pip install -r requirements.txt
```

---

## 🚀 Como usar os comandos

### Trilha — plano de estudos

```bash
python main.py trilha <tecnologia>
```

**Tecnologias disponíveis:** `python`, `javascript`, `dados`

**Exemplo:**
```bash
python main.py trilha python
```

---

### Desafio — desafio de código

```bash
python main.py desafio <tecnologia> <nivel>
```

**Níveis disponíveis:** `iniciante`, `intermediario`, `avancado`

**Exemplo:**
```bash
python main.py desafio javascript iniciante
```

---

### Certificado — certificado fictício

```bash
python main.py certificado "<seu nome>" <tecnologia>
```

**Exemplo:**
```bash
python main.py certificado "Nayane Araujo" dados
```

---

## 🧪 Como executar os testes

```bash
pytest tests/ -v
```

Resultado esperado: **11 testes passando**.

---

## 🔌 Servidor MCP

O `server.py` expõe os três comandos como ferramentas MCP, permitindo integração com assistentes de IA compatíveis com o protocolo MCP (como o IBM Bob e o Claude).

Para executar o servidor:

```bash
python server.py
```

---

## ✨ Melhorias realizadas

- Base de trilhas com **3 tecnologias**: Python, JavaScript e Ciência de Dados
- Cada trilha possui **8 módulos** e **3 níveis** (iniciante, intermediário e avançado)
- Desafios com enunciado claro e dica de resolução
- Certificado com nome em destaque, data e contagem de módulos
- 11 testes automatizados cobrindo casos de sucesso e de erro
- Servidor MCP integrado aos mesmos comandos do CLI

---

## 📚 O que aprendi

- Como estruturar um projeto Python com separação de responsabilidades
- Como criar uma CLI com `argparse`
- Como usar JSON como base de dados simples
- Como escrever testes automatizados com `pytest` e `capsys`
- Como criar um Servidor MCP com `FastMCP` para expor ferramentas a assistentes de IA
- A importância de testar casos de erro, não só os casos de sucesso

---

## 👩‍💻 Autora

**Nayane Araujo** — [GitHub](https://github.com/Nayanearaujo)

Desenvolvido durante o **Bootcamp IBM Bob** na [DIO](https://dio.me) 🚀
