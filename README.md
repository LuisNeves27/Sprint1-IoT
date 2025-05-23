# 🧠 SysTrack Vision: Identificação Automatizada de Motos via Visão Computacional

---

## 🎓 Curso & Sprint

📚 FIAP — Análise e Desenvolvimento de Sistemas  
📦 Sprint 1 — Disruptive Architectures: IoT, IoB & Generative AI  
🏁 Tema: Visão Computacional aplicada ao controle de frotas


---

## 👨‍💻 Nossa Equipe

**Luis Felippe Morais RM558127**  
💼 Estudante de Análise e Desenvolvimento de Sistemas na FIAP  
🔗 [linkedin.com/in/luis-felippe-morais-das-neves-16219b2b9](https://linkedin.com/in/luis-felippe-morais-das-neves-16219b2b9)

**Gustavo Rangel RM559168**  
💼 Estudante de Análise e Desenvolvimento de Sistemas na FIAP  
🔗 [linkedin.com/in/gustavoorangel](https://linkedin.com/in/gustavoorangel)

**David Rapeckman RM556607**  
💼 Estudante de Análise e Desenvolvimento de Sistemas na FIAP  
🔗 [linkedin.com/in/davidrapeckman](https://linkedin.com/in/davidrapeckman)

---

## 📘 Descrição

O **SysTrack Vision** é uma prova de conceito desenvolvida como parte da Sprint 1 da FIAP. A proposta visa aplicar **Visão Computacional** para identificar e numerar automaticamente motos estacionadas em um pátio, simulando o ambiente real da **Mottu**.

A solução utiliza imagens reais, anotadas no **Roboflow**, e processadas com **Python + OpenCV**, permitindo a visualização das motos com etiquetas como `moto_1`, `moto_2` etc., sem a necessidade de sensores físicos.

---

## 🛠️ Tecnologias Utilizadas

- **Roboflow** – Criação e anotação do dataset (formato COCO)
- **Python 3.10+**
- **OpenCV** – Processamento de imagem e desenho de caixas
- **Matplotlib** – Visualização dos resultados
- **Formato COCO JSON** – Anotações de objetos
- **Jupyter / VS Code** – Ambiente de desenvolvimento

---

## 🖥️ Funcionalidades

✅ Leitura automática de anotações no formato COCO  
✅ Detecção e numeração individual de motos nas imagens  
✅ Lógica de posicionamento do texto para evitar sobreposição  
✅ Visualização em tela com Matplotlib  
✅ Exportação da imagem final com as motos numeradas

---

## 🧠 Conceitos Utilizados

- Visão Computacional aplicada ao contexto logístico da Mottu  
- Processamento de anotações COCO via Python  
- Bounding boxes com `cv2.rectangle`  
- Renderização com `matplotlib.pyplot`  
- Alternância de texto para legibilidade visual

---


## 🔮 Possibilidades Futuras

- 📡 Integração com sensores IoT para presença/vagas  
- 📹 Processamento de vídeo em tempo real (streaming)  
- ☁️ Envio automático de logs e contagens para a nuvem  
- 🖥️ Dashboard web para visualização em tempo real  
- 📱 App mobile integrado ao backend com IA embarcada  
- 🧠 Treinamento com modelos avançados como YOLOv8

---

## 🧩 Estrutura do Projeto

SysTrack-Vision/
│
├── valid/                          # Pasta com imagens e anotações
│   ├── _annotations.coco.json      # Anotações no formato COCO
│   └── imagem1.jpg                 # Imagens reais do pátio com motos
│   └── imagem2.jpg                 # (outras imagens utilizadas)
│
├── Iot.py                          # Script principal em Python
│                                   # - Processa as imagens
│                                   # - Desenha caixas e numera motos
│
├── resultado_numerado.png          # Saída gerada pelo script
│                                   # - Imagem com motos numeradas

---

## 🧪 Como Rodar o Projeto Localmente

1. Instale as dependências:

```bash
pip install opencv-python matplotlib
```

2. Certifique-se de ter a pasta `valid/` com imagens e `_annotations.coco.json`

3. Execute:

```bash
python Iot.py
```

4. O script exibirá as imagens com as motos numeradas.
A imagem final será salva como `resultado_numerado.png`.


