Unsplash Image Downloader and Metadata Extractor
This repository contains a Python script that downloads images from Unsplash, extracts metadata, updates the metadata with tags from PhotoTag.ai, and compares the durations of different processing steps.

Features
Download Images: Fetch images from Unsplash and save them locally.
Metadata Extraction: Extract metadata such as format, size, and mode from the images.
Metadata Enrichment: Update the extracted metadata with tags from PhotoTag.ai.
Performance Comparison: Measure and compare the durations of different processing steps using Matplotlib.
Prerequisites
Before running the script, ensure you have the following installed:

Python 3.x
Requests
BeautifulSoup
Pillow
Matplotlib
You can install the required packages using pip:

sh
Copy code
pip install requests beautifulsoup4 pillow matplotlib
Usage
Clone the Repository:

sh
Copy code
git clone https://github.com/your-username/unsplash-image-downloader.git
cd unsplash-image-downloader
Set Up Your Environment:
Ensure you have the necessary API key for PhotoTag.ai and update the PHOTO_TAG_API_KEY variable in the script.

Run the Script:
Execute the script to download images, extract metadata, and update metadata with tags:

sh
Copy code
python script.py
View the Results:

Images and metadata files will be saved in the unsplash_images directory.
A summary report will be saved as summary_report.csv.
A bar chart comparing the durations of different processing steps will be displayed.
