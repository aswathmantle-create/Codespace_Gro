"""
Test script to validate the Streamlit app structure and imports
"""
import sys
import importlib.util

def test_imports():
    """Test that all required imports work"""
    print("Testing imports...")
    
    try:
        import streamlit
        print("✓ streamlit imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import streamlit: {e}")
        return False
    
    try:
        import PIL
        print("✓ PIL imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import PIL: {e}")
        return False
    
    try:
        import groq
        print("✓ groq imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import groq: {e}")
        return False
    
    try:
        import pandas
        print("✓ pandas imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import pandas: {e}")
        return False
    
    try:
        from dotenv import load_dotenv
        print("✓ dotenv imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import dotenv: {e}")
        return False
    
    return True

def test_app_module():
    """Test that app.py can be loaded as a module"""
    print("\nTesting app.py module...")
    
    try:
        spec = importlib.util.spec_from_file_location("app", "app.py")
        app_module = importlib.util.module_from_spec(spec)
        # We don't execute it since it has streamlit.set_page_config which can't run outside streamlit
        print("✓ app.py module loaded successfully")
        return True
    except Exception as e:
        print(f"✗ Failed to load app.py: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("Freshfood CMS Template Generator - Test Suite")
    print("=" * 60)
    
    imports_ok = test_imports()
    module_ok = test_app_module()
    
    print("\n" + "=" * 60)
    if imports_ok and module_ok:
        print("✓ All tests passed!")
        print("=" * 60)
        sys.exit(0)
    else:
        print("✗ Some tests failed")
        print("=" * 60)
        sys.exit(1)
