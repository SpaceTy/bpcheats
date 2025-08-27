from terminal_emulator import run_command_and_capture_output

# Test the terminal emulator function
try:
    # Test with a simple ls command
    output_path = run_command_and_capture_output("ls -la")
    print(f"Command output saved to: {output_path}")

    # Test with a command that creates a file
    output_path = run_command_and_capture_output("touch test_file.txt && echo 'Hello, World!' > test_file.txt")
    print(f"File creation output saved to: {output_path}")

    # Test with a command that reads the file
    output_path = run_command_and_capture_output("cat test_file.txt")
    print(f"File content output saved to: {output_path}")

    # Test with a command that lists the files
    output_path = run_command_and_capture_output("ls -la")
    print(f"Directory listing output saved to: {output_path}")

    print("All tests completed successfully!")

except Exception as e:
    print(f"Error: {e}")
