# Projeto de Processamento de Imagens: Grayscale e Binarização (Bootcamp DIO)

Este projeto implementa algoritmos em Python para converter imagens coloridas para tons de cinza e para imagens binarizadas (preto e branco). Estes são passos comuns no pré-processamento para redução de dimensionalidade em imagens, por exemplo, para uso em Redes Neurais.

## Funcionalidades

- Conversão de imagem colorida para tons de cinza (0-255).
- Conversão de imagem em tons de cinza para binarizada (0 e 255) usando um limiar (threshold).
- Implementações manuais (pixel a pixel) e utilizando a biblioteca Pillow.

## Estrutura do Projeto


```  <-- INÍCIO DO BLOCO DE CÓDIGO
dio-processamento-imagens-rn/
├── image_processor.py        # Script principal
├── .gitignore                # Arquivos ignorados pelo Git
├── README.md                 # Este arquivo
├── images/                   # Pasta para imagens de entrada
│   └── minha_imagem.jpg      # Coloque sua imagem de exemplo aqui
└── output_images/            # Pasta onde as imagens processadas são salvas (criada pelo script)
```

## Como Usar Localmente

1.  **Pré-requisitos:**
    - Python 3.x
    - Bibliotecas (instale via pip se necessário):
      ```bash
      pip install Pillow matplotlib
      ```

2.  **Configuração:**
    - Clone este repositório (ou baixe os arquivos).
    - Coloque a imagem que deseja processar (ex: `minha_imagem.jpg`) dentro da pasta `images/`.
    - Se o nome da sua imagem não for `minha_imagem.jpg`, ajuste a variável `input_filename` no script `image_processor.py`.

3.  **Execução:**
    Navegue até a pasta raiz do projeto (`dio-processamento-imagens-rn`) no terminal e execute:
    ```bash
    python image_processor.py
    ```
    As imagens processadas serão salvas na pasta `output_images/`. Uma janela do Matplotlib também deve exibir os resultados.

## Autor

- Tony C. Cintra (TonyCCintra)