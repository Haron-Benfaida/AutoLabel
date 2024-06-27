from utils import Utils
from PIL import Image, ImageDraw, ImageFont


class Boxer:
    @staticmethod
    def data2boxes(data, text, boxes):
        data2boxes = {}
        for key in data:
            idx = Utils.closest_finder(data[key], text)
            data2boxes[key] = boxes[idx]
        return data2boxes

    @staticmethod
    def box_all(image, data2boxes):
        canvas = ImageDraw.Draw(image)
        font = ImageFont.load_default()
        for data in data2boxes:
            box = data2boxes[data]
            canvas.rectangle(box, outline='green')
            canvas.text((box[0] + 10, box[1] - 10), text=data, fill='green', font=font)
        return image


