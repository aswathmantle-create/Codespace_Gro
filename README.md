# 🛒 Freshfood CMS Template Generator

A powerful Streamlit web application that extracts product catalog attributes from product images using AI vision models. Perfect for grocery stores, FMCG companies, and e-commerce platforms looking to automate product catalog creation.

## 🌟 Features

- **AI-Powered OCR**: Uses Groq's LLaVA vision model for accurate text extraction
- **Comprehensive Extraction**: Extracts multiple product attributes including:
  - Product name and brand
  - Category and subcategory
  - Price and weight/volume
  - Ingredients and nutritional information
  - Barcode, manufacturing and expiry dates
  - Product description and keywords
  - Packaging type
- **Batch Processing**: Upload and process multiple product images at once
- **Multiple Export Formats**: Download extracted data as JSON or CSV
- **User-Friendly Interface**: Clean and intuitive Streamlit UI
- **Real-time Processing**: Get instant results with visual feedback

## 📋 Requirements

- Python 3.8 or higher
- Groq API key (free tier available)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/aswathmantle-create/Codespace_Gro.git
   cd Codespace_Gro
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   - Copy `.env.example` to `.env`
     ```bash
     cp .env.example .env
     ```
   - Get your Groq API key from [https://console.groq.com/](https://console.groq.com/)
   - Add your API key to the `.env` file:
     ```
     GROQ_API_KEY=your_groq_api_key_here
     ```

## 💻 Usage

1. **Start the Streamlit app**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser**
   - The app will automatically open in your default browser
   - Or navigate to `http://localhost:8501`

3. **Upload product images**
   - Click on "Browse files" or drag and drop product images
   - Supported formats: JPG, JPEG, PNG
   - You can upload multiple images at once

4. **Extract product information**
   - Click "Extract Product Info" for each image
   - Wait for the AI to analyze the image
   - Review the extracted data

5. **Export the data**
   - Download as JSON for API integration
   - Download as CSV for spreadsheet applications
   - Clear data to start fresh

## 📁 Project Structure

```
Codespace_Gro/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## 🔧 Configuration

### Groq API Settings

The app uses Groq's `llama-3.2-90b-vision-preview` model by default. You can modify the model settings in `app.py`:

```python
model="llama-3.2-90b-vision-preview",
temperature=0.1,
max_tokens=1024,
```

### Extracted Attributes

The application extracts the following product attributes:
- `product_name`: Exact product name
- `brand`: Brand name
- `category`: Product category (Beverages, Snacks, Dairy, etc.)
- `subcategory`: Subcategory if applicable
- `price`: Price with currency
- `weight_volume`: Net weight or volume
- `ingredients`: List of ingredients
- `nutritional_info`: Key nutritional facts
- `barcode`: Barcode number
- `manufacturing_date`: Manufacturing date
- `expiry_date`: Expiry date
- `description`: Brief product description
- `keywords`: Relevant keywords for search
- `packaging_type`: Type of packaging

## 🎯 Use Cases

1. **E-commerce Catalog Creation**: Quickly build product catalogs from images
2. **Inventory Management**: Extract and organize product information
3. **Price Comparison**: Extract pricing data from competitor products
4. **Nutritional Analysis**: Gather nutritional information for health apps
5. **Compliance Checking**: Verify product labeling and information

## 🛠️ Technology Stack

- **Streamlit**: Web application framework
- **Groq**: AI vision model API (LLaVA)
- **Pillow**: Image processing
- **Pandas**: Data manipulation and export
- **Python-dotenv**: Environment variable management

## 📝 Example Output

### JSON Format
```json
{
  "product_name": "Organic Whole Milk",
  "brand": "Happy Farms",
  "category": "Dairy",
  "price": "$4.99",
  "weight_volume": "1 Gallon",
  "ingredients": "Organic Grade A Milk, Vitamin D3",
  "packaging_type": "Plastic Bottle"
}
```

### CSV Format
```csv
product_name,brand,category,price,weight_volume,ingredients,packaging_type
Organic Whole Milk,Happy Farms,Dairy,$4.99,1 Gallon,"Organic Grade A Milk, Vitamin D3",Plastic Bottle
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Powered by [Groq](https://groq.com/) for fast AI inference
- Built with [Streamlit](https://streamlit.io/) for rapid app development
- Uses LLaVA vision model for image understanding

## 📞 Support

For issues, questions, or suggestions, please open an issue on GitHub.
