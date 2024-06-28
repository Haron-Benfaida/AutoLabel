class OCRManager:
    _ocr_classes = {}

    @classmethod
    def register_ocr_engine(cls, ocr_name, ocr_class):
        cls._ocr_classes[ocr_name] = ocr_class

    @classmethod
    def get_ocr_engine(cls, ocr_name):
        engine = cls._ocr_classes.get(ocr_name)()
        return engine




