import os
import subprocess
import hashlib
from PIL import Image, ImageDraw, ImageFont
import textwrap

def run_command_and_capture_output(command, field_dir="field", output_dir="output"):
    """
    Run a command in the field directory and generate a PNG of the output.

    Args:
        command (str): The command to execute
        field_dir (str): Directory to run the command in. Defaults to "field"
        output_dir (str): Directory to save the output PNG. Defaults to "output"
        width (int): Width of the output image. Defaults to 800
        height (int): Height of the output image. Defaults to 600

    Returns:
        str: Path to the generated PNG file
    """
    # Ensure directories exist
    if not os.path.exists(field_dir):
        raise FileNotFoundError(f"Field directory '{field_dir}' does not exist")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Run the command
    try:
        result = subprocess.run(
            command,
            shell=True,
            cwd=field_dir,
            capture_output=True,
            text=True,
            timeout=30  # Timeout after 30 seconds
        )

        # Combine stdout and stderr
        output = f"$ {command}\n"
        if result.stdout:
            output += result.stdout
        if result.stderr:
            output += result.stderr
        if result.returncode != 0:
            output += f"\n[Exit code: {result.returncode}]"

    except subprocess.TimeoutExpired:
        output = f"$ {command}\n[Command timed out after 30 seconds]"
    except Exception as e:
        output = f"$ {command}\n[Error running command: {str(e)}]"

    # Generate a unique filename based on the command
    command_hash = hashlib.md5(command.encode()).hexdigest()[:8]
    output_filename = f"command_{command_hash}.png"
    output_path = os.path.join(output_dir, output_filename)

    # Create image with the output
    create_output_image(output, output_path)

    return output_path

def create_output_image(text, output_path):
    """
    Create a PNG image with the given text.

    Args:
        text (str): Text to render in the image
        output_path (str): Path to save the image
    """
    # Try to use a monospace font, fallback to default if not available
    try:
        font = ImageFont.truetype("DejaVuSansMono.ttf", 14)
    except:
        try:
            font = ImageFont.truetype("cour.ttf", 14)
        except:
            font = ImageFont.load_default()

    # Calculate text size
    lines = text.split('\n')

    # Calculate dimensions based on text content
    max_line_width = 0
    for line in lines:
        # Wrap long lines
        wrapped_lines = textwrap.wrap(line, width=100)  # Max 100 chars per line
        for wrapped_line in wrapped_lines:
            bbox = font.getbbox(wrapped_line)
            line_width = bbox[2] - bbox[0]
            max_line_width = max(max_line_width, line_width)

    # Calculate image dimensions
    # Width: max line width + padding (20 pixels on each side)
    width = max_line_width + 40
    # Height: number of lines * line height + padding (10 pixels top/bottom)
    line_height = 18  # Approximate line height
    total_lines = sum(len(textwrap.wrap(line, width=100)) for line in lines)
    height = total_lines * line_height + 20

    # Ensure minimum dimensions
    width = max(width, 200)  # Minimum width of 200 pixels
    height = max(height, 50)  # Minimum height of 50 pixels

    # Create image
    image = Image.new('RGB', (width, height), color=(0, 0, 0))
    draw = ImageDraw.Draw(image)

    # Draw text
    y_offset = 10
    for line in lines:
        # Wrap long lines
        wrapped_lines = textwrap.wrap(line, width=100)
        for wrapped_line in wrapped_lines:
            draw.text((10, y_offset), wrapped_line, fill=(255, 255, 255), font=font)
            y_offset += line_height

    # Save image
    image.save(output_path)

# Example usage:
# output_path = run_command_and_capture_output("ls -la")
# print(f"Output saved to: {output_path}")
