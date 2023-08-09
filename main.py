import cv2
import mediapipe as mp
import pyautogui

pyautogui.FAILSAFE = False
SENSIBILIDADE_DO_MODELO = 3

# Lê a câmera e inicializa a solução
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

# Pega o tamanho da nossa tela
screen_w, screen_h = pyautogui.size()

# Coletando as especificações da câmera
_, frame = cam.read()
frame_h, frame_w, _ = frame.shape

# Loop principal
while True:
    _, img = cam.read()
    img = cv2.flip(img, 1)
    rgb_frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb_frame)
    landmark_points = results.multi_face_landmarks

    # Checando se os landmarks de fato existem
    if landmark_points:
        landmarks = landmark_points[0].landmark     # index zero por que a gente só tem uma face

        iris_and_mouth = [landmarks[145], landmarks[159], landmarks[14], landmarks[13]]

        # Checa se a boca esta aberta, o que "desabilita todo o sistema"
        distancia_da_boca = iris_and_mouth[-2].y - iris_and_mouth[-1].y     
        # print(distancia_da_boca)        # test
        if distancia_da_boca > 0.05:
            pass
        else:
            for id, landmark in enumerate(iris_and_mouth[0:2]):
                # Adaptando o x e y para pixels
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                # Desenhando na coord
                cv2.circle(img, (x, y), 3, (255, 0, 0))
                # Lógica de mover o mouse
                if id == 0:
                    screen_x = screen_w * landmark.x * SENSIBILIDADE_DO_MODELO
                    # screen_x = screen_w if screen_x > screen_w else screen_x

                    screen_y = screen_h * landmark.y * SENSIBILIDADE_DO_MODELO
                    # screen_y = screen_h if screen_y > screen_h else screen_y
                    
                    pyautogui.moveTo(screen_x, screen_y)

            # Desenho das landmarks
            for landmark in landmarks:
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(img, (x, y), 3, (255, 255, 0))

            # Lógica de clique
            distancia_dos_olhos = iris_and_mouth[0].y - iris_and_mouth[1].y 
            # print(distancia_dos_olhos)      # test
            if distancia_dos_olhos < 0.012:
                pyautogui.click()
                pyautogui.sleep(1)
                pass

    # Image show + pause + lógica de quit
    cv2.imshow('Eye Controlled Mouse', img)
    cv2.waitKey(1)
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break