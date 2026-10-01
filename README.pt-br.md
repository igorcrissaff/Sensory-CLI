# Sensory CLI

[![Ingles](https://img.shields.io/badge/README-English-blue?style=flat-square)](README.md)
[![Portugues](https://img.shields.io/badge/README-Portuguese-green?style=flat-square)](README.pt-br.md)
---

## Sobre

**Sensory CLI** é um kit de ferramentas de acessibilidade de código aberto para linha de comando, desenvolvido com o objetivo de transformar informações digitais entre diferentes modalidades.

O projeto traz recursos voltados à acessibilidade diretamente para o terminal, permitindo que usuários processem imagens, documentos, textos, áudios e outros tipos de conteúdo digital sem depender de uma interface gráfica.

O objetivo de longo prazo é criar um kit de ferramentas de acessibilidade modular, capaz de conectar diferentes tecnologias de percepção e saída por meio de uma interface de linha de comando unificada.

```text
                     ┌─────────────────┐
                     │   SENSORY CLI   │
                     └────────┬────────┘
                              │
              ┌───────────────┼───────────────┐
              │               │               │
            Visão            Texto           Áudio
              │               │               │
          ┌───┴───┐       ┌───┴───┐       ┌───┴───┐
          │       │       │       │       │       │
        Imagem   OCR   Traduzir  Resumir  STT     TTS
              │               │               │
              └───────────────┼───────────────┘
                              │
                    ┌─────────┴─────────┐
                    │    Acessibilidade │
                    │      Saída        │
                    └─────────┬─────────┘
                              │
                 ┌────────────┼────────────┐
                 │            │            │
               Texto         Áudio       Braille

```

---

## Funcionalidades

O Sensory CLI foi projetado em torno de um conjunto modular de recursos de acessibilidade.

### Visão

Processamento e interpretação de informações visuais.

* Descrição de imagens
* Análise de imagens
* Reconhecimento de objetos
* Extração de conteúdo visual
* Detecção de cores e atributos visuais

### OCR

Extração de texto de imagens e documentos digitalizados.

* Reconhecimento Óptico de Caracteres
* Extração de texto de fotografias
* Processamento de documentos digitalizados
* Integração com pipelines de processamento de imagens

### Reconhecimento de Fala

Conversão de linguagem falada em texto.

* Transcrição de áudio
* Fala para texto
* Entrada por microfone
* Processamento de arquivos de áudio

### Texto para Fala

Conversão de informações textuais em saída falada.

* Texto para fala
* Leitura de documentos
* Narração da saída de comandos
* Vozes e idiomas configuráveis

### Braille

Processamento e saída de texto orientados a Braille.

* Tradução de texto para Braille
* Saída preparada para Braille
* Integração com displays Braille
* Suporte futuro a hardware tátil

### Documentos

Facilitação do acesso a documentos digitais.

* Extração de texto de PDFs
* Processamento de documentos baseado em OCR
* Sumarização de documentos
* Leitura de texto por síntese de voz
* Extração de conteúdo estruturado

### Idiomas

Recursos para acessibilidade multilíngue.

* Tradução
* Detecção de idioma
* Normalização de texto
* Processamento de fala multilíngue

### Assistência por IA

Interpretação de alto nível de conteúdo acessível.

* Sumarização de conteúdo
* Compreensão de imagens
* Descrições contextuais
* Interação em linguagem natural
* Perguntas e respostas sobre documentos

---

# Instalação

O Sensory CLI é desenvolvido em **Python** e utiliza o **uv** para gerenciamento do ambiente Python e das dependências.

## Requisitos

Antes de instalar o Sensory CLI, certifique-se de possuir:

* Python 3.11 ou superior
* [uv](https://docs.astral.sh/uv/)
* Git

Verifique seu ambiente:

```bash
python --version
uv --version
git --version
```

## Clonar o repositório

```bash
git clone https://github.com/igorcrissaff/sensory-cli.git
cd sensory-cli
```

## Instalar as dependências

Crie o ambiente virtual do projeto e instale suas dependências com:

```bash
uv sync
```

O `uv` cria e gerencia automaticamente o ambiente virtual do projeto.

## Executar a CLI

Durante o desenvolvimento, a CLI pode ser executada com:

```bash
uv run sensory --help
```

ou:

```bash
uv run sensory
```

---

# Uso

Após a instalação, o Sensory CLI foi projetado para ser utilizado por meio do comando `sensory`.

```bash
sensory <comando> [opções]
```

Para visualizar todos os comandos disponíveis:

```bash
sensory --help
```

Para obter ajuda sobre um comando específico:

```bash
sensory <comando> --help
```

> Os comandos abaixo representam a interface planejada e podem sofrer alterações conforme o projeto evolui.

---

## Descrição de Imagens

Descreva uma imagem utilizando o módulo de visão:

```bash
sensory describe image.jpg
```

Durante o desenvolvimento:

```bash
uv run sensory describe image.jpg
```

Exemplo:

```text
◉ Visão

Analisando imagem...
✓ Imagem processada

Descrição:
Uma pessoa sentada em uma mesa utilizando um laptop.
```

---

## OCR

Extraia texto de uma imagem:

```bash
sensory ocr document.png
```

Exemplo:

```text
[T] OCR

Processando imagem...
✓ Texto extraído

Olá, mundo!
```

Salve o texto extraído em um arquivo:

```bash
sensory ocr document.png > output.txt
```

---

## Fala para Texto

Transcreva um arquivo de áudio:

```bash
sensory transcribe recording.wav
```

Exemplo:

```text
))) Reconhecimento de Fala

Processando áudio...
✓ Transcrição concluída

"Bem-vindo ao Sensory CLI."
```

---

## Texto para Fala

Converta texto em fala:

```bash
sensory speak "Bem-vindo ao Sensory CLI."
```

O texto também pode ser lido a partir de um arquivo:

```bash
sensory speak --file document.txt
```

---

## Braille

Traduza texto para Braille:

```bash
sensory braille "Olá, mundo!"
```

Exemplo:

```text
⠕⠇⠷⠂⠀⠍⠥⠝⠙⠕⠖
```

Uma versão futura poderá oferecer comunicação direta com displays Braille atualizáveis:

```bash
sensory braille output document.txt --device <device>
```

---

## Leitura de Documentos

Processe e leia um documento:

```bash
sensory read document.pdf
```

O pipeline de processamento de documentos poderá combinar diferentes recursos de acessibilidade:

```text
PDF
 │
 ▼
Extração de Texto
 │
 ├──► Terminal
 │
 ├──► OCR
 │
 ├──► Sumarização
 │
 ├──► Texto para Fala
 │
 └──► Braille
```

---

## Tradução

Traduza textos entre diferentes idiomas:

```bash
sensory translate "Hello, world!" --to pt-BR
```

Para arquivos:

```bash
sensory translate document.txt --to pt-BR
```

---

# Desenvolvimento

O Sensory CLI utiliza o **uv** como principal ferramenta de desenvolvimento e gerenciamento de dependências.

## Criar o ambiente de desenvolvimento

Após clonar o repositório:

```bash
uv sync
```

Ative o ambiente virtual caso queira trabalhar diretamente dentro dele:

### Linux/macOS

```bash
source .venv/bin/activate
```

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Como alternativa, é possível evitar a ativação do ambiente e utilizar:

```bash
uv run <comando>
```

Por exemplo:

```bash
uv run python --version
```

---

## Adicionar uma dependência

Adicione uma dependência de execução:

```bash
uv add package-name
```

Para uma dependência de desenvolvimento:

```bash
uv add --dev package-name
```

Por exemplo:

```bash
uv add requests
```

ou:

```bash
uv add --dev pytest
```

Remova uma dependência com:

```bash
uv remove package-name
```

Após modificar as dependências:

```bash
uv sync
```

---

## Executar os testes

Os testes podem ser executados com:

```bash
uv run pytest
```

Para obter uma saída mais detalhada:

```bash
uv run pytest -v
```

---

## Qualidade do código

Quando configuradas no projeto, as ferramentas de formatação e análise podem ser executadas com:

```bash
uv run ruff format .
```

```bash
uv run ruff check .
```

Essas ferramentas ajudam a manter uma base de código consistente e confiável.

---

# Configuração

O Sensory CLI foi projetado para oferecer suporte à configuração por meio de variáveis de ambiente e/ou um arquivo de configuração.

Uma configuração futura poderá ser semelhante a:

```env
SENSORY_LANGUAGE=pt-BR

SENSORY_OCR_ENGINE=tesseract
SENSORY_SPEECH_ENGINE=local
SENSORY_TTS_ENGINE=local

SENSORY_AI_PROVIDER=local
```

Credenciais sensíveis nunca devem ser adicionadas ao repositório.

Utilize um arquivo de ambiente para desenvolvimento local quando necessário:

```text
.env
```

e mantenha-o fora do controle de versão:

```text
.gitignore
```

---

# Estrutura de Comandos

O Sensory CLI foi projetado para permanecer simples nas operações mais comuns, permitindo funcionalidades mais avançadas por meio de subcomandos.

```text
sensory
├── vision
│   ├── describe
│   ├── analyze
│   └── objects
│
├── text
│   ├── ocr
│   ├── translate
│   └── summarize
│
├── audio
│   ├── transcribe
│   └── speak
│
├── braille
│   ├── translate
│   └── output
│
└── document
    ├── read
    ├── extract
    └── summarize
```

O projeto também pode disponibilizar operações frequentemente utilizadas como comandos de nível superior:

```bash
sensory ocr image.png
sensory describe image.jpg
sensory transcribe audio.wav
sensory speak "Olá"
sensory braille "Olá"
```

Isso permite que a interface permaneça conveniente tanto para uso interativo quanto para automação.

---

# Arquitetura

O Sensory CLI foi projetado com uma arquitetura modular.

```text
                         ┌───────────────┐
                         │  Sensory CLI  │
                         └───────┬───────┘
                                 │
                         ┌───────▼───────┐
                         │  Interface de │
                         │    Comandos   │
                         └───────┬───────┘
                                 │
                         ┌───────▼───────┐
                         │ Sensory Core  │
                         └───────┬───────┘
                                 │
             ┌───────────────────┼───────────────────┐
             │                   │                   │
       ┌─────▼─────┐       ┌─────▼─────┐       ┌─────▼─────┐
       │    Visão  │       │   Texto   │       │   Áudio   │
       └─────┬─────┘       └─────┬─────┘       └─────┬─────┘
             │                   │                   │
       ┌─────▼─────┐       ┌─────▼─────┐       ┌─────▼─────┐
       │ Análise   │       │ OCR       │       │ STT       │
       │ de Imagem │       │ Traduzir  │       │ TTS       │
       │ Detecção  │       │ Resumir   │       │ Processar │
       └───────────┘       └───────────┘       └───────────┘
                                 │
                         ┌───────▼───────┐
                         │ Acessibilidade│
                         │     Saídas    │
                         └───────┬───────┘
                                 │
                    ┌────────────┼────────────┐
                    │            │            │
                   Texto        Áudio        Braille
```

A abordagem modular permite que componentes individuais sejam substituídos ou estendidos sem a necessidade de reprojetar toda a aplicação.

---

# Estrutura do Projeto

O projeto é organizado em módulos independentes:

```text
sensory-cli/
│
├── sensory/
│   ├── cli/
│   ├── core/
│   ├── vision/
│   ├── text/
│   ├── audio/
│   ├── braille/
│   ├── documents/
│   └── accessibility/
│
├── tests/
│
├── docs/
│
├── examples/
│
├── assets/
│   └── logo.png
│
├── pyproject.toml
├── uv.lock
├── README.md
├── LICENSE
└── CONTRIBUTING.md
```

A estrutura poderá evoluir conforme novas funcionalidades sejam introduzidas.

---

# Saídas de Acessibilidade

Um conceito central do Sensory CLI é que a informação não deve ficar restrita a um único formato de saída.

A mesma entrada pode potencialmente ser transformada em diferentes representações acessíveis:

```text
              ENTRADA
                 │
       ┌─────────┼─────────┐
       │         │         │
     Imagem    Áudio    Documento
       │         │         │
       └─────────┼─────────┘
                 │
           SENSORY CORE
                 │
       ┌─────────┼─────────┐
       │         │         │
      Texto     Áudio    Braille
```

Por exemplo:

```bash
sensory describe image.jpg --output text
sensory describe image.jpg --output speech
sensory ocr document.png --output braille
```

Essa abstração tem como objetivo tornar o kit de ferramentas útil para diferentes necessidades de acessibilidade e ambientes de hardware.

---

# Automação

Como o Sensory CLI é uma aplicação de linha de comando, suas operações podem ser combinadas com ferramentas e scripts existentes do shell.

Por exemplo:

```bash
sensory ocr document.png > output.txt
```

Processando a saída:

```bash
sensory ocr document.png | sensory summarize
```

Convertendo o conteúdo extraído em fala:

```bash
sensory ocr document.png | sensory speak
```

Ou criando um pipeline completo de acessibilidade:

```text
Imagem
  │
  ▼
 OCR
  │
  ▼
 Texto
  │
  ├──────► Terminal
  │
  ├──────► Resumo
  │
  ├──────► Fala
  │
  └──────► Braille
```

Essa capacidade de composição é uma das principais vantagens da abordagem baseada em CLI.

---

# Integrações Planejadas

Possíveis integrações incluem:

* Mecanismos de OCR
* Modelos de visão computacional
* Mecanismos de reconhecimento de fala
* Mecanismos de texto para fala
* Sistemas de tradução automática
* Modelos de linguagem de grande escala (LLMs)
* Bibliotecas de tradução para Braille
* Displays Braille atualizáveis
* Leitores de tela
* Hardware assistivo
* APIs de acessibilidade

O projeto priorizará tecnologias abertas e interoperáveis sempre que possível.

---

# Privacidade

Ferramentas de acessibilidade frequentemente processam informações sensíveis, como documentos, imagens, conversas e gravações de áudio.

O Sensory CLI busca tornar explícito como o processamento ocorre e oferecer aos usuários controle sobre onde seus dados são processados.

Sempre que serviços externos ou modelos de IA baseados em nuvem forem utilizados, o projeto deverá informar claramente:

* Quais dados são transmitidos
* Qual serviço recebe os dados
* Se os dados são armazenados
* Quais credenciais são necessárias
* Se existem alternativas locais

A privacidade é considerada uma parte importante da acessibilidade.

---

# Roadmap

## Fase 1 — CLI Principal

* Arquitetura da CLI
* Sistema de comandos
* Gerenciamento de configurações
* Sistema de logs
* Sistema de plugins/módulos
* Abstração básica de saída de acessibilidade

## Fase 2 — Texto e OCR

* Integração com OCR
* Extração de texto
* Normalização de texto
* Processamento de documentos

## Fase 3 — Áudio

* Fala para texto
* Texto para fala
* Processamento de arquivos de áudio
* Entrada por microfone

## Fase 4 — Visão

* Descrição de imagens
* Reconhecimento de objetos
* Extração de atributos visuais
* Análise contextual de imagens

## Fase 5 — Braille

* Tradução para Braille
* Saída em Braille
* Abstração para displays Braille
* Integração com hardware

## Fase 6 — Acessibilidade Inteligente

* Sumarização de documentos
* IA multimodal
* Descrições contextuais
* Interação em linguagem natural
* Automação de fluxos de trabalho

---

# Contribuição

Contribuições são bem-vindas.

Você pode contribuir por meio de:

* Implementação de novos módulos de acessibilidade
* Melhorias nas integrações existentes
* Adição de testes
* Melhorias na documentação
* Relato de bugs
* Sugestões de melhorias de acessibilidade
* Desenvolvimento de integrações com hardware
* Melhorias na usabilidade da CLI

Antes de enviar uma contribuição, certifique-se de que o ambiente do projeto esteja sincronizado:

```bash
uv sync
```

Execute a suíte de testes:

```bash
uv run pytest
```

E, quando configurados:

```bash
uv run ruff check .
uv run ruff format .
```

Uma boa contribuição deve preservar a arquitetura modular do projeto e seus princípios de acessibilidade em primeiro lugar.

---

# Licença

Este projeto está licenciado sob a **Licença MIT**.

Consulte o arquivo [`LICENSE`](LICENSE) para mais informações.

---

# Visão

O Sensory CLI busca tornar a linha de comando mais do que uma interface para desenvolvedores.

Seu objetivo é transformá-la em uma **interface acessível para interação com informações digitais**.

```text
       VER        OUVIR       LER
        │           │          │
        └───────────┼──────────┘
                    │
               ┌────▼────┐
               │ SENSORY │
               │   CLI   │
               └────┬────┘
                    │
           ┌────────┼────────┐
           │        │        │
         TEXTO     ÁUDIO   BRAILLE
```

> **Sensory CLI — Acessibilidade multimodal através da linha de comando.**
