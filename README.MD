## 🙋‍♂️ Equipe de desenvolvedores
<table align='center'>
  <tr>
    <td align="center">
        <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/101208372?v=4" width="100px;" alt=""/><br /><sub><b><a href="https://github.com/Y4nnLS">Yann Lucas</a></b></sub></a><br />🤓☝</a></td>
    <td align="center">
        <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/123337250?v=4" width="100px;" alt=""/><br /><sub><b><a href="https://github.com/kauegalons">Kaue Galon</a></b></sub></a><br />🤠✊</td>
  </table>

# 🎮 Extrator de Sprites com OpenCV

Este projeto em Python utiliza a biblioteca OpenCV para **detectar bordas com o algoritmo Canny** e extrair **sprites** (personagens, objetos, blocos, etc.) de imagens de jogos clássicos como Space Invaders, Mario, Pac-Man e Celeste.

---

## 📌 Funcionalidades

- Conversão de imagens coloridas para escala de cinza.
- Suavização com **Gaussian Blur** para redução de ruído.
- Detecção de bordas com o algoritmo **Canny**.
- Extração de contornos com `cv2.findContours`.
- Recorte automático de cada sprite detectado.
- Geração de uma **pasta separada** para cada imagem, com os sprites exportados.

---

## 🖼️ Imagens Suportadas

A lista de imagens é configurada no próprio script:

```python
imagens_entrada = [
    "spaceinvaders.png",
    "mario.jpg",
    "pacman.png",
    "celeste.jpg"
]
