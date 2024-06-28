import ocr
from datasets import load_dataset
from utils.str_utils import Utils
from llm.EngineLLM import LLMEngine
from visualization.drawer import Drawer

CONFIG = {
    "ocr_engine": "tesseract",
    "model": "llama3 70b",
    "dataset": "ayoub999/dataset_for_orange_factures"
}


def init_components(config):
    ocr_engine = ocr.OCRManager.get_ocr_engine(config["ocr_engine"])
    llm_engine = LLMEngine(config["model"])
    drawer = Drawer()
    dataset = load_dataset(config["dataset"])
    return ocr_engine, llm_engine, drawer, dataset


def main():
    ocr_engine, llm_engine, drawer, dataset = init_components(CONFIG)
    example = dataset['train'][4]['image']
    words, boxes = ocr_engine.ocr(example)
    response = Utils.query_to_dict(llm_engine.ocr_to_llm(words))
    data2boxes = Drawer.data2boxes(response, words, boxes)
    boxed_image = Drawer.box_all(example, data2boxes)
    Drawer.show_image(boxed_image)


if __name__ == '__main__':
    main()



