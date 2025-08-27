import os
from docx import Document

def read_docx_file(filename="exprement number 3.docx", data_dir="data"):
    """
    Read and return the contents of a .docx file from the data directory.

    Args:
        filename (str): Name of the .docx file to read. Defaults to "exprement number 3.docx"
        data_dir (str): Name of the data directory. Defaults to "data"

    Returns:
        str: Contents of the .docx file as a string

    Raises:
        FileNotFoundError: If the file doesn't exist
        Exception: If there's an error reading the file
    """
    # Construct the full path to the file in the data directory
    file_path = os.path.join(data_dir, filename)

    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    try:
        # Open and read the .docx file
        doc = Document(file_path)

        # Extract text from all paragraphs
        full_text = []
        for paragraph in doc.paragraphs:
            full_text.append(paragraph.text)

        # Join all paragraphs with newlines
        return '\n'.join(full_text)

    except Exception as e:
        raise Exception(f"Error reading the .docx file: {str(e)}")

# Example usage:
# content = read_docx_file()
# print(content)
