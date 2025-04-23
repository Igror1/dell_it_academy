# Startup Rush - Dell IT Academy

Startup Rush é um programa gamificado em Python que simula torneios de startups, permitindo cadastrar startups, realizar batalhas com eventos que afetam suas pontuações e determinar um vencedor. Desenvolvido como parte do processo seletivo da IT Academy 22 (2025), utiliza Tkinter para a interface gráfica e o padrão MVC para organização.

## Pré-requisitos 

- **Python 3.6+**: Necessário para a execução do programa.
- **Tkinter**: Biblioteca para interface gráfica, geralmente incluída na instalação do Python.

Nenhuma outra dependência externa é necessária.

## Uso 

Para utilizar o código, siga as instruções abaixo:

- Certifique-se de ter o Python instalado em seu sistema.

- Clone este repositório em sua máquina local.

- Navegue até o diretório onde o repositório foi clonado.

- Execute o arquivo `main.py` em um ambiente Python:

  ```bash
  python main.py
  ```

- Siga as instruções exibidas na interface do programa para interagir com ele e obter os resultados desejados.

## Exemplo de Uso 

### Tela Inicial

- Clique em "Cadastrar Startups" para começar.

### Cadastro

- Insira nome, slogan e ano de fundação de 8 startups.
- Clique em "Iniciar Torneio" quando terminar.

### Batalhas

- Escolha uma batalha (ex.: "Startup1 vs Startup2") e aplique eventos como:

  ```
  Pitch convincente (+6)
  Produto com bugs (-4)
  ```

### Campeão

- Veja o vencedor e acesse relatórios e histórico de batalhas.

## Estrutura do Projeto 

Visão geral da organização do código:

```
startup-rush/
├── main.py        # Arquivo principal que inicializa o programa
├── model.py       # Lógica do torneio (classes Startup e Torneio)
├── view.py        # Interface gráfica com Tkinter
├── controller.py  # Conecta o model e a view
└── README.md      # Documentação do projeto
```

O projeto segue o padrão MVC (Model-View-Controller) para separação de responsabilidades.