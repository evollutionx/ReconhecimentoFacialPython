Projeto de Reconhecimento Facial em Python

Este projeto implementa um sistema simples de reconhecimento facial em Python usando as bibliotecas OpenCV e face_recognition. O programa utiliza a câmera do computador para detectar rostos e compará-los com imagens previamente cadastradas em uma pasta. Quando uma correspondência é encontrada, o nome da pessoa é exibido na tela e registrado em um arquivo de log junto com a data e hora do reconhecimento.

Funcionalidades:

Captura de imagens da câmera para reconhecimento facial em tempo real.
Comparação de rostos detectados com imagens previamente cadastradas.
Atualização dinâmica do reconhecimento à medida que novas faces são detectadas.
Requisitos:

Python 3.x
Bibliotecas: OpenCV, face_recognition, NumPy
Instruções de Uso:

Instale as dependências executando pip install opencv-python face-recognition.
Crie uma pasta imagens em C:/Reconhecimento/ e adicione imagens de pessoas nomeadas (ex: ana.jpg, fulano.jpeg).
Execute o script main.py para iniciar o reconhecimento facial.
Este projeto é um exemplo educacional de como implementar reconhecimento facial em Python e pode ser estendido para aplicações mais complexas. Sinta-se à vontade para contribuir, sugerir melhorias ou adaptar para suas necessidades específicas.
