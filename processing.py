import io
import os
from preprocessing import correct_image_rotation

def process_invoice_file(file_path: str) -> io.BytesIO:
    """
    Processa o ficheiro da factura e retorna um CSV como stream BytesIO.
    Por agora, inclui pré-processamento de rotação para imagens.
    """
    ext = os.path.splitext(file_path)[1].lower()
    if ext in [".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".tif"]:
        processed_path = correct_image_rotation(file_path)
    else:
        processed_path = file_path

    # Aqui será a chamada para OCR e extração (stub para já)
    csv_content = "Vendor,Invoice Number,Invoice Date,Description,Quantity,Unit Price,Line Total,Tax Amount,Total Amount,Payment Terms,Extraction Confidence,Missing Fields\n"
    csv_content += "Example Vendor,INV123,2024-03-26,Item A,2,10.00,20.00,1.50,21.50,Net 30,0.99,None\n"
    return io.BytesIO(csv_content.encode('utf-8'))