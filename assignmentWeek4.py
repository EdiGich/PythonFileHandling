import os

def file_read_write_modify(input_file_path, output_file_path):
    """
    Reads a file, modifies its content by reversing lines and adding line numbers,
    and writes the modified content to a new file.

    Args:
        input_file_path (str): The path to the input file.
        output_file_path (str): The path to the output file.

    Returns:
        bool: True if successful, False otherwise.
    """
    # Check if input file exists
    if not os.path.exists(input_file_path):
        print(f"Error: Input file '{input_file_path}' does not exist.")
        return False

    try:
        # Read the file
        with open(input_file_path, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()

        # Modify the content: reverse lines and add line numbers
        modified_lines = [f"Line {i+1}: {line.rstrip()[::-1]}\n" for i, line in enumerate(reversed(lines))]

        # Ensure output directory exists
        output_dir = os.path.dirname(output_file_path) or '.'
        os.makedirs(output_dir, exist_ok=True)

        # Write to the new file
        with open(output_file_path, 'w', encoding='utf-8') as outfile:
            outfile.writelines(modified_lines)

        print(f"Successfully modified '{input_file_path}' and wrote to '{output_file_path}'")
        print(f"Changes made: Lines reversed and numbered")
        return True

    except FileNotFoundError:
        print(f"Error: Unable to access '{input_file_path}'.")
        return False
    except PermissionError:
        print(f"Error: Permission denied while accessing '{input_file_path}' or '{output_file_path}'.")
        return False
    except IOError as e:
        print(f"IO Error: Unable to read/write file: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

def error_handling_lab():
    """
    Asks the user for a filename, handles errors if it doesn't exist or can't be read,
    and displays the file content with additional statistics if successful.
    """
    while True:
        filename = input("Enter the name of the file to read (or 'exit' to quit): ").strip()
        
        if filename.lower() == 'exit':
            print("Exiting the program.")
            break

        # Basic input validation
        if not filename:
            print("Error: Filename cannot be empty.")
            continue
        if any(char in filename for char in '<>:"/\\|?*'):
            print("Error: Filename contains invalid characters.")
            continue

        try:
            # Attempt to open and read the file
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
                # Calculate statistics
                line_count = content.count('\n') + 1
                word_count = len(content.split())
                
                print(f"\nFile '{filename}' content:")
                print("-" * 50)
                print(content)
                print("-" * 50)
                print(f"Statistics:")
                print(f"  Lines: {line_count}")
                print(f"  Words: {word_count}")
                print(f"  Characters (including spaces): {len(content)}")

        except FileNotFoundError:
            print(f"Error: File '{filename}' not found. Please check the filename and try again.")
        except PermissionError:
            print(f"Error: Permission denied while accessing '{filename}'.")
        except UnicodeDecodeError:
            print(f"Error: File '{filename}' is not a valid text file or has encoding issues.")
        except IOError as e:
            print(f"IO Error: Unable to read file '{filename}': {e}")
        except Exception as e:
            print(f"An unexpected error occurred while reading '{filename}': {e}")

if __name__ == "__main__":
    # --- File Read & Write Challenge ---
    # Create a dummy input file for testing
    input_file = "my_input.txt"
    try:
        with open(input_file, 'w', encoding='utf-8') as f:
            f.write("This is a test file.\nIt contains some text.\nHello Python!\n")
        print(f"Created test input file: {input_file}")
    except Exception as e:
        print(f"Error creating dummy file: {e}")
        exit(1)

    output_file = "my_output.txt"
    file_read_write_modify(input_file, output_file)

    # --- Error Handling Lab ---
    print("\nStarting Error Handling Lab...")
    error_handling_lab()
