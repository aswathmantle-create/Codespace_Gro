"""
Freshfood CMS Template Generator
A Streamlit web app that extracts product catalog attributes from product images 
using AI vision models (Groq LLaVA).
"""

import streamlit as st
import base64
import json
import csv
import io
import os
from PIL import Image
from groq import Groq
from dotenv import load_dotenv
import pandas as pd

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Freshfood CMS Template Generator",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Groq client
def get_groq_client():
    """Initialize and return Groq client"""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        st.error("⚠️ GROQ_API_KEY not found. Please set it in your .env file.")
        st.info("Get your API key from: https://console.groq.com/")
        return None
    return Groq(api_key=api_key)

def encode_image_to_base64(image):
    """Convert PIL Image to base64 string"""
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str

def extract_product_info(client, image_base64):
    """Extract product information using Groq vision model"""
    
    prompt = """Analyze this grocery/FMCG product image and extract the following information in JSON format:

{
    "product_name": "exact product name",
    "brand": "brand name",
    "category": "product category (e.g., Beverages, Snacks, Dairy, etc.)",
    "subcategory": "subcategory if applicable",
    "price": "price with currency if visible",
    "weight_volume": "net weight or volume",
    "ingredients": "list of ingredients if visible",
    "nutritional_info": "key nutritional facts if visible",
    "barcode": "barcode number if visible",
    "manufacturing_date": "manufacturing date if visible",
    "expiry_date": "expiry date if visible",
    "description": "brief product description",
    "keywords": "relevant keywords for search",
    "packaging_type": "type of packaging (bottle, box, pouch, etc.)"
}

Extract as much information as possible from the image. If any field is not visible or cannot be determined, use "N/A" or null. Be accurate and extract text exactly as shown on the product."""

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{image_base64}",
                            },
                        },
                    ],
                }
            ],
            model="llama-3.2-90b-vision-preview",
            temperature=0.1,
            max_tokens=1024,
        )
        
        response_text = chat_completion.choices[0].message.content
        
        # Try to extract JSON from the response
        # Sometimes the model wraps JSON in markdown code blocks
        if "```json" in response_text:
            json_start = response_text.find("```json") + 7
            json_end = response_text.find("```", json_start)
            response_text = response_text[json_start:json_end].strip()
        elif "```" in response_text:
            json_start = response_text.find("```") + 3
            json_end = response_text.find("```", json_start)
            response_text = response_text[json_start:json_end].strip()
        
        product_data = json.loads(response_text)
        return product_data, None
        
    except json.JSONDecodeError as e:
        return None, f"Failed to parse JSON response: {str(e)}\n\nRaw response: {response_text}"
    except Exception as e:
        return None, f"Error during extraction: {str(e)}"

def convert_to_csv(products_data):
    """Convert list of product dictionaries to CSV string"""
    if not products_data:
        return None
    
    output = io.StringIO()
    
    # Get all unique keys from all products
    all_keys = set()
    for product in products_data:
        all_keys.update(product.keys())
    
    fieldnames = sorted(list(all_keys))
    
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(products_data)
    
    return output.getvalue()

def main():
    # Header
    st.title("🛒 Freshfood CMS Template Generator")
    st.markdown("""
    Extract product catalog attributes from grocery/FMCG product images using AI vision models.
    Upload product images and get structured JSON/CSV data instantly.
    """)
    
    # Sidebar
    with st.sidebar:
        st.header("📋 About")
        st.markdown("""
        This app uses **Groq's LLaVA vision model** to:
        - Perform OCR on product images
        - Extract product attributes
        - Generate structured catalog data
        
        **Supported attributes:**
        - Product name & brand
        - Category & subcategory
        - Price & weight/volume
        - Ingredients & nutrition
        - Dates & barcodes
        - And more...
        """)
        
        st.header("⚙️ Settings")
        show_raw_response = st.checkbox("Show raw AI response", value=False)
        
    # Initialize session state
    if "extracted_products" not in st.session_state:
        st.session_state.extracted_products = []
    
    # Initialize Groq client
    client = get_groq_client()
    
    if client is None:
        st.stop()
    
    # File uploader
    st.header("📤 Upload Product Images")
    uploaded_files = st.file_uploader(
        "Choose product image(s)",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True,
        help="Upload one or more product images (JPG, JPEG, or PNG format)"
    )
    
    if uploaded_files:
        st.subheader(f"Processing {len(uploaded_files)} image(s)...")
        
        for idx, uploaded_file in enumerate(uploaded_files):
            with st.expander(f"📦 Image {idx + 1}: {uploaded_file.name}", expanded=True):
                col1, col2 = st.columns([1, 2])
                
                with col1:
                    # Display image
                    image = Image.open(uploaded_file)
                    st.image(image, caption=uploaded_file.name, use_container_width=True)
                
                with col2:
                    # Extract button
                    if st.button(f"Extract Product Info", key=f"extract_{idx}"):
                        with st.spinner("Analyzing image with AI..."):
                            # Convert image to base64
                            image_base64 = encode_image_to_base64(image)
                            
                            # Extract product information
                            product_data, error = extract_product_info(client, image_base64)
                            
                            if error:
                                st.error(f"Error: {error}")
                            else:
                                st.success("✅ Product information extracted successfully!")
                                
                                # Add image filename to product data
                                product_data["image_filename"] = uploaded_file.name
                                
                                # Store in session state
                                st.session_state.extracted_products.append(product_data)
                                
                                # Display extracted data
                                st.json(product_data)
                                
                                if show_raw_response:
                                    st.markdown("**Raw Response:**")
                                    st.code(json.dumps(product_data, indent=2))
    
    # Display all extracted products
    if st.session_state.extracted_products:
        st.header("📊 Extracted Product Data")
        
        # Display as dataframe
        df = pd.DataFrame(st.session_state.extracted_products)
        st.dataframe(df, use_container_width=True)
        
        # Export options
        st.header("💾 Export Data")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            # JSON export
            json_str = json.dumps(st.session_state.extracted_products, indent=2)
            st.download_button(
                label="📥 Download JSON",
                data=json_str,
                file_name="product_catalog.json",
                mime="application/json",
                use_container_width=True
            )
        
        with col2:
            # CSV export
            csv_str = convert_to_csv(st.session_state.extracted_products)
            st.download_button(
                label="📥 Download CSV",
                data=csv_str,
                file_name="product_catalog.csv",
                mime="text/csv",
                use_container_width=True
            )
        
        with col3:
            # Clear data button
            if st.button("🗑️ Clear All Data", use_container_width=True):
                st.session_state.extracted_products = []
                st.rerun()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center'>
        <p>Powered by Groq LLaVA Vision Model | Built with Streamlit</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
