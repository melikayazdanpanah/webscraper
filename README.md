# Unsplash Image Downloader and Metadata Extractor

This repository contains a Python script that downloads images from Unsplash, extracts metadata, updates the metadata with tags from PhotoTag.ai, and compares the durations of different processing steps.

## Features

- **Download Images**: Fetch images from Unsplash and save them locally.
- **Metadata Extraction**: Extract metadata such as format, size, and mode from the images.
- **Metadata Enrichment**: Update the extracted metadata with tags from PhotoTag.ai.
- **Performance Comparison**: Measure and compare the durations of different processing steps using Matplotlib.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- Requests
- BeautifulSoup
- Pillow
- Matplotlib

You can install the required packages using pip:

```sh
pip install requests beautifulsoup4 pillow matplotli
```


# How It Works
Image Download: The script fetches image URLs from Unsplash using BeautifulSoup and downloads images using the Requests library.

Metadata Extraction: Using Pillow, the script extracts image format, dimensions, and color mode.

Metadata Enrichment: It sends images to PhotoTag.ai API along with the API key, retrieves descriptive tags, and updates metadata JSON files.

Performance Analysis: The script measures and compares durations of each processing step, displaying results using Matplotlib.

#  Stored Data Structure
Directories
unsplash_images/: Root directory for downloaded images and metadata.
image_<num>/: Subdirectories for each downloaded image.
image.jpg: Image file downloaded from Unsplash.
metadata.json: JSON file containing metadata and tags.
(Optional) Other image-related files or additional metadata.
Contents of metadata.json
Each metadata.json file includes:

json
```
{
  "url": "https://unsplash.com/photo/example",
  "format": "JPEG",
  "size": [1920, 1080],
  "mode": "RGB",
  "tags": ["tag1", "tag2", "tag3"]
}
```
url: URL of the image from Unsplash.
format: Image format (e.g., JPEG, PNG).
size: Dimensions of the image (width, height).
mode: Color mode of the image (e.g., RGB, CMYK).
tags: Descriptive tags obtained from PhotoTag.ai API.


Acknowledgements
Unsplash for providing high-quality images.
PhotoTag.ai for the image tagging service.

