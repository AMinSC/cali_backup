"""이미지 전처리, OCR, 크롭 등의 이미지 처리 기능이 정의된 모듈입니다."""

import io

import pytesseract
from PIL import Image


def preprocess_image_to_ocr(image: Image) -> Image:
    """이미지 OCR의 성능 향상을 위해 이미지를 전처리합니다.

    TODO: 현재는 입력값을 그대로 반환하는 로직이며, 향후 실제 전처리 로직이 추가될 예정입니다.

    Args:
        image: 전처리할 이미지입니다.

    Returns:
        전처리된 이미지를 반환합니다.
    """

    return image


def recognize_optical_character(image: Image, lang: str) -> str:
    """원본 이미지를 전처리하고 Tesseract를 활용해 OCR 하여 인식된 문자를 반환합니다.

    Args:
        image: 전처리하고 문자를 인식할 이미지입니다.
        lang: Tesseract에서 사용할 언어 모델입니다.

    Returns:
        이미지에서 식별된 문자와 그 좌표값이 포함된 문자열입니다.
        문자열의 예시는 다음과 같습니다.

        '''
        e 334 126 349 144 0
        r 351 126 379 144 0
        t 388 126 397 149 0
        '''

        문자는 개행문자를 기준으로 구분되며, 각 문자의 정보는 아래와 같이 구성됩니다.
        '문자, left, bottom, right, top, page_num'
    """

    preprocessed_image = preprocess_image_to_ocr(image)
    boxes = pytesseract.image_to_boxes(preprocessed_image, lang=lang)

    return boxes


def crop_image_to_box(image: Image, coords: list[int]) -> Image:
    """주어진 좌표를 활용하여 이미지를 Box 형태로 편집하여 반환합니다.

    TODO: 로직 구현 (현재는 원본 이미지를 그대로 반환)

    Args:
        image: 편집할 원본 이미지입니다.
        coords: Box 이미지를 만들 때 사용하는 좌표값입니다.

    Returns:
        원본 이미지를 좌표값을 기준으로 편집한 이미지입니다.
    """

    return image


def convert_stream_to_webp(file_stream: io.BytesIO) -> io.BytesIO:
    image = Image.open(file_stream)
    output_file_stream = io.BytesIO()

    image.save(output_file_stream, format='WEBP')

    return output_file_stream
