# Optical Character Recognition (OCR) with EasyOCR

# Project Overview
This project focuses on developing a robust `Optical Character Recognition (OCR)` tool using the `EasyOCR` library. The tool is designed to accurately `extract text` from various file formats, including `images (PNG, JPG, JPEG) and PDF documents`. Leveraging the power of EasyOCR, the implementation utilizes the craft_mlt_25k.pth model for text detection and the english_g2.pth model for English text recognition.

# How It Works
# 1. File Upload:
Users can upload files through the Streamlit web interface. Supported file types include PNG, JPG, JPEG, and PDF.

# 2. Text Detection:
For PDF files, the craft_mlt_25k.pth model is employed for text detection. This model excels at identifying text regions within the document. The text detection phase involves:

Page Segmentation: Each page of the PDF is segmented into distinct regions containing text.
Bounding Boxes: The model outputs bounding boxes that enclose the detected text regions.

# 3. Text Recognition:
For both images and PDFs, the english_g2.pth model is utilized for text recognition. This model excels at recognizing English text within the detected regions. The text recognition phase involves:

Character Recognition: The model identifies individual characters within each bounding box.
Word Formation: Recognized characters are combined to form words.
Language Understanding: English text is accurately recognized and converted into machine-readable text.

# 4. Efficiency:
Pre-Trained Models: EasyOCR's pre-trained models, craft_mlt_25k.pth and english_g2.pth, eliminate the need for extensive training on custom datasets.
Streamlit Interface: The tool leverages Streamlit to provide an intuitive and user-friendly web interface for uploading files and viewing results.

# Evaluation Metrics
The effectiveness of the OCR tool can be evaluated using the following metrics:

1. Accuracy:
Text Detection Accuracy: Evaluate how well the craft_mlt_25k.pth model identifies text regions in PDFs.
Text Recognition Accuracy: Assess the accuracy of the english_g2.pth model in recognizing English text.
2. Processing Time:
File Type Processing Time: Measure the time taken to process different file types (images, PDFs).
File Size Processing Time: Evaluate how processing time scales with various file sizes.
3. Resource Usage:
Memory Consumption: Monitor memory usage during OCR processing.
CPU Utilization: Assess the CPU usage for optimal performance.
4. User Feedback:
Usability: Collect user feedback on the ease of use and overall experience with the tool.
Accuracy Validation: Encourage users to validate the accuracy of the extracted text against ground truth data.


# Installation:

Install the required dependencies by running `pip install -r requirements.txt`.

# Run the Application:

Execute the application by running `streamlit run streamlit_app.py`.

# Upload Files:
Use the web interface to upload files for OCR processing.

