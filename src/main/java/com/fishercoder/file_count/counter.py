import os

def count_lines_in_file(file_path):
    """Counts the number of lines in a given file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return sum(1 for _ in file)

def read_file_content(file_path):
    """Reads and returns the content of a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def scan_java_files(directory):
    """Scans Java files in a directory and filters those with over 100 lines."""
    java_files_over_100_lines = []
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".java"):
                file_path = os.path.join(root, file)
                line_count = count_lines_in_file(file_path)
                if line_count > 100:
                    content = read_file_content(file_path)
                    java_files_over_100_lines.append((file, line_count, content))
    
    return java_files_over_100_lines

if __name__ == "__main__":
    directory = "../solutions/fourththousand"
    file_name = directory.split("/")[-1]
    result = scan_java_files(directory)
    
    if result:
        print("Java files with more than 100 lines:")
        for file, lines, _ in result:
            print(f"{file}: {lines} lines")
        with open(f"./{file_name}.txt", "w", encoding='utf-8') as f:
            f.write(f"Total files count: {len(result)}\n")
            for file, lines, content in result:
                f.write(f"{'='*50}\n")
                f.write(f"File: {file}\n")
                f.write(f"Line count: {lines}\n")
                f.write(f"{'='*50}\n")
                f.write("Content:\n")
                f.write(content)
                f.write("\n\n")
    else:
        print("No Java files with more than 100 lines found.")
