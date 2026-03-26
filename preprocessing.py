import cv2
import os

def correct_image_rotation(image_path: str) -> str:
    """
    Detecta e corrige a rotação da imagem.
    Guarda a imagem corrigida num ficheiro novo e retorna o seu caminho.
    """
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Não foi possível ler a imagem para pré-processamento.")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bitwise_not(gray)

    coords = cv2.findNonZero(gray)
    angle = 0
    if coords is not None:
        rect = cv2.minAreaRect(coords)
        angle = rect[-1]
        if angle < -45:
            angle = -(90 + angle)
        else:
            angle = -angle

    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h),
                             flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    corrected_path = image_path.replace(".", "_rotated.")
    cv2.imwrite(corrected_path, rotated)
    return corrected_path