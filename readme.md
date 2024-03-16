# Optical Character Recognition(OCR)

# Project Overview
This project focuses on developing a robust `Optical Character Recognition (OCR)` tool using the `EasyOCR` library. The tool is designed to accurately `extract text` from various file formats, including `images (PNG, JPG, JPEG) and PDF documents`. Leveraging the power of EasyOCR, the implementation utilizes the craft_mlt_25k.pth model for text detection and the english_g2.pth model for English text recognition.

## Working !!!
## File Upload:
Users can upload files through the Streamlit web interface. Supported file types include PNG, JPG, JPEG, and PDF.

## Text Detection:
For PDF files, the craft_mlt_25k.pth model is employed for text detection. This model excels at identifying text regions within the document. The text detection phase involves:

  Page Segmentation: Each page of the PDF is segmented into distinct regions containing text.
  Bounding Boxes: The model outputs bounding boxes that enclose the detected text regions.

## Text Recognition:
For both images and PDFs, the english_g2.pth model is utilized for text recognition. This model excels at recognizing English text within the detected regions. The text recognition phase involves:

  Character Recognition: The model identifies individual characters within each bounding box.
  Word Formation: Recognized characters are combined to form words.
  Language Understanding: English text is accurately recognized and converted into machine-readable text.

## Evaluation Metrics

The effectiveness of our OCR (Optical Character Recognition) tool can be evaluated using the Word Error Rate (WER). WER is a common metric used to measure the accuracy of OCR systems by comparing the output text with the ground truth.

### Word Error Rate (WER)

Word Error Rate measures the difference between the recognized text and the ground truth text. It is calculated as the ratio of the total number of insertions, deletions, and substitutions required to convert the recognized text into the ground truth text, to the total number of words in the ground truth text.

The formula for calculating WER is as follows:
Where:
- I = Number of insertions (words present in ground truth but not in recognized text)
- D = Number of deletions (words present in recognized text but not in ground truth)
- S = Number of substitutions (words in recognized text that are different from words in ground truth)
- N = Total number of words in ground truth

Levenshtein Distance, often used to calculate the number of insertions, deletions, and substitutions, can be utilized to calculate the numerator of WER.

### Levenshtein Distance

Levenshtein Distance is the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one word into another. It is used to quantify the similarity between two strings.

For our OCR evaluation, Levenshtein Distance can be applied to compute the number of insertions, deletions, and substitutions between the recognized text and the ground truth text, which are then used to calculate the WER.

By analyzing the WER, we can assess the accuracy and performance of our OCR tool and identify areas for improvement.


# Clone the repository

`git clone https://github.com/yesvanthraja/OCR`

# Installation:

Install the required dependencies by running `pip install -r requirements.txt`.

# Run the Application:

Execute the application by running `streamlit run streamlit_app.py`.

# Upload Files:
Use the web interface to upload files for OCR processing.

