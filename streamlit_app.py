from PIL import Image
import streamlit as st
import easyocr as ocr
import fitz
import numpy as np
import tempfile
import os
from langdetect import detect
from googletrans import Translator

def process_pdf(file_upload):
    temp_filename = None
    try:
        temp = tempfile.NamedTemporaryFile(delete=False)
        temp.write(file_upload.read())
        temp.close()
        temp_filename = temp.name

        extracted_text = []
        with fitz.open(temp_filename) as doc:
            for page_num in range(doc.page_count):
                page = doc[page_num]
                text = page.get_text()
                extracted_text.append(text)

        return extracted_text

    except Exception as e:
        st.error(f"Error processing PDF: {e}")
        return None

    finally:
        if temp_filename:
            os.remove(temp_filename)

def process_image(file_upload, model):
    try:
        image = Image.open(file_upload)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        result = model.readtext(np.array(image))
        extracted_text = [text[1] for text in result]

        return extracted_text

    except Exception as e:
        st.error(f"Error processing image: {e}")
        return None

def translate_text(text, target_lang='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_lang)
    return translation.text

def main():
    st.title("Optical Character Recognition - OCR")
    st.markdown("`Extract text by uploading file`")

    file_upload = st.file_uploader(label="Upload your files here", type=['png', 'jpg', 'jpeg', 'pdf'])

    model = ocr.Reader(['en'], model_storage_directory='.')

    if file_upload:
        with st.spinner(f"Processing {file_upload.name} ..."):
            if file_upload.type == 'application/pdf':
                extracted_text = process_pdf(file_upload)
            else:
                extracted_text = process_image(file_upload, model)

            if extracted_text is not None:
                st.write(extracted_text)
                language = detect(extracted_text[0]) if extracted_text else 'en'
                st.write(f"Detected Language: {language}")
                if language != 'en':
                    translate_button = st.button("Translate to English")
                    if translate_button:
                        translated_text = translate_text(extracted_text[0], target_lang='en')
                        st.write(f"Translated Text: {translated_text}")

    else:
        st.write("")

if __name__ == "__main__":
    main()
