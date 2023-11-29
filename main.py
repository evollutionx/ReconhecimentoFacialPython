import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime

# Caminho para a pasta com as imagens
pasta_imagens = 'C:/Reconhecimento/ReconhecimentoFacialPython\imagens'

# Caminho para o arquivo de log
caminho_log = 'C:/Reconhecimento/ReconhecimentoFacialPython\log.txt'

# Carrega as imagens da pasta
lista_imagens = []
lista_nomes = []
faces_conhecidas = []

for nome_arquivo in os.listdir(pasta_imagens):
    caminho_imagem = os.path.join(pasta_imagens, nome_arquivo)
    if nome_arquivo.lower().endswith(('.png', '.jpg', '.jpeg')):
        imagem = face_recognition.load_image_file(caminho_imagem)
        face_encoding_list = face_recognition.face_encodings(imagem)
        if len(face_encoding_list) > 0:
            lista_imagens.append(face_encoding_list[0])
            lista_nomes.append(os.path.splitext(nome_arquivo)[0])
            faces_conhecidas.append([])  # Lista para rastrear as faces conhecidas
        else:
            print(f"Aviso: Nenhuma face detectada em {nome_arquivo}")

# Inicializa a câmera
cap = cv2.VideoCapture(0)

while True:
    # Captura um frame da câmera
    ret, frame = cap.read()

    # Encontra todas as faces no frame
    faces = face_recognition.face_locations(frame)
    encodings = face_recognition.face_encodings(frame, faces)

    # Atualiza as faces conhecidas com as novas faces detectadas
    for i, (face_location, face_encoding) in enumerate(zip(faces, encodings)):
        matches = face_recognition.compare_faces(lista_imagens, face_encoding)
        nome_pessoa = "Desconhecido"

        if True in matches:
            first_match_index = matches.index(True)
            nome_pessoa = lista_nomes[first_match_index]

            # Converte face_location para array NumPy
            face_location_array = np.array([face_location])

            # Verifica se a face é próxima de uma face conhecida
            for j, known_face_location in enumerate(faces_conhecidas[first_match_index]):
                # Converte known_face_location para array NumPy
                known_face_location_array = np.array([known_face_location])

                # Calcula a distância mínima
                min_distance = np.min(face_recognition.face_distance([known_face_location_array], face_location_array))

                if min_distance < 0.6:
                    # Atualiza a posição da face conhecida
                    faces_conhecidas[first_match_index][j] = face_location
                    break
            else:
                # Adiciona uma nova face conhecida
                faces_conhecidas[first_match_index].append(face_location)

            # Registra no arquivo de log
            with open(caminho_log, 'a') as log_file:
                now = datetime.now()
                data_hora = now.strftime("%Y-%m-%d %H:%M:%S")
                log_file.write(f"{nome_pessoa} reconhecido em {data_hora}\n")

        # Exibe o nome da pessoa na tela
        fonte = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, nome_pessoa, (face_location[3] + 6, face_location[0] - 6), fonte, 0.5, (255, 255, 255), 1)

    # Exibe o frame com o nome da pessoa
    cv2.imshow('Reconhecimento Facial', frame)

    # Encerra o programa ao pressionar a tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera os recursos
cap.release()
cv2.destroyAllWindows()
