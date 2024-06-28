from abc import ABC, abstractmethod


class InterfaceOCR(ABC):
    @staticmethod
    @abstractmethod
    def ocr(image):
        pass

