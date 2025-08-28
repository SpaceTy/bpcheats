import sys
import os

# Add the current directory to the Python path so we can import util
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from util import read_docx_file

def main():
    try:
        # Test the function
        content = read_docx_file()
        print("Contents of the .docx file:")
        print("=" * 40)
        print(content)
        print("=" * 40)
        print("Function executed successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
