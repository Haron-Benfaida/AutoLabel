import easyocr
from ocr.InterfaceOCR import InterfaceOCR
from ocr.ManagerOCR import OCRManager


class EasyOCR(InterfaceOCR):
    @staticmethod
    def ocr(image):
        reader = easyocr.Reader(['fr'])
        data = reader.readtext(image)
        words = [i[1] for i in data]
        boxes = [j[0][0] + j[0][2] for j in data]
        return words, boxes


OCRManager.register_ocr_engine('easyocr', EasyOCR)
