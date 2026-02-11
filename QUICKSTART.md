# Quickstart Guide

Get started with the Freshfood CMS Template Generator in 5 minutes!

## 1. Prerequisites
- Python 3.8 or higher
- A Groq API key ([Get one free here](https://console.groq.com/))

## 2. Installation

```bash
# Clone the repository
git clone https://github.com/aswathmantle-create/Codespace_Gro.git
cd Codespace_Gro

# Install dependencies
pip install -r requirements.txt
```

## 3. Configuration

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Edit `.env` and add your Groq API key:

```
GROQ_API_KEY=your_actual_api_key_here
```

## 4. Run the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 5. Test with Sample Images

1. Click "Browse files" or drag & drop product images
2. Upload images in JPG, JPEG, or PNG format
3. Click "Extract Product Info" for each image
4. Review the extracted data
5. Download as JSON or CSV

## Troubleshooting

**Issue: "GROQ_API_KEY not found"**
- Solution: Make sure you created a `.env` file with your API key

**Issue: "Failed to parse JSON response"**
- Solution: The image might not be clear enough. Try with a better quality image

**Issue: App won't start**
- Solution: Make sure all dependencies are installed: `pip install -r requirements.txt`

## Features Demo

### Single Image Processing
Upload one product image and extract all visible attributes instantly.

### Batch Processing
Upload multiple images and process them one by one or in sequence.

### Export Options
- **JSON**: Perfect for APIs and databases
- **CSV**: Open in Excel, Google Sheets, or import into databases

## Need Help?

Open an issue on [GitHub](https://github.com/aswathmantle-create/Codespace_Gro/issues) if you encounter any problems.
