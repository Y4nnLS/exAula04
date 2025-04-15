import cv2
import numpy as np
import os

# Lista de arquivos de imagem de entrada
imagens_entrada = [
    "spaceinvaders.png",
    "mario.jpg",
    "pacman.png",
    "celeste.jpg"
]

# Diretório base para salvar os sprites extraídos
output_base_dir = "sprites_extraidos"
os.makedirs(output_base_dir, exist_ok=True)

def extrair_sprites(caminho_imagem):
    # Nome do arquivo sem extensão
    nome_base = os.path.splitext(os.path.basename(caminho_imagem))[0]
    pasta_saida = os.path.join(output_base_dir, nome_base)
    os.makedirs(pasta_saida, exist_ok=True)

    # Carregar imagem
    imagem = cv2.imread(caminho_imagem)
    if imagem is None:
        print(f"[ERRO] Não foi possível abrir {caminho_imagem}")
        return

    # Pré-processamento
    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    suave = cv2.GaussianBlur(cinza, (3, 3), 0)
    bordas = cv2.Canny(suave, 50, 150)

    # Encontrar contornos
    contornos, _ = cv2.findContours(bordas, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Recortar sprites detectados
    contador = 0
    for c in contornos:
        x, y, w, h = cv2.boundingRect(c)
        if w > 10 and h > 10:  # Ignorar fragmentos pequenos
            sprite = imagem[y:y+h, x:x+w]
            caminho_sprite = os.path.join(pasta_saida, f"{nome_base}_sprite_{contador}.png")
            cv2.imwrite(caminho_sprite, sprite)
            contador += 1

    print(f"[OK] {contador} sprites extraídos de '{nome_base}'")

# Processar todas as imagens
for imagem_path in imagens_entrada:
    extrair_sprites(imagem_path)
