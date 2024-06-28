import pytesseract
from ocr.InterfaceOCR import InterfaceOCR
from ocr.ManagerOCR import OCRManager


class TesseractOCR(InterfaceOCR):

    @staticmethod
    def ocr(image):
        ocr_data = pytesseract.image_to_data(image, lang='fra', output_type=pytesseract.Output.DICT)

        words = ocr_data['text']
        boxes = [
            [
                ocr_data['left'][i],
                ocr_data['top'][i],
                ocr_data['left'][i] + ocr_data['width'][i],
                ocr_data['top'][i] + ocr_data['height'][i],
            ]
            for i in range(len(ocr_data['text']))
        ]
        return words, boxes


OCRManager.register_ocr_engine('tesseract', TesseractOCR)
