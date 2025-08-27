import os


def generate_tree(startpath, ignore_dirs=None, ignore_files=None):
    """
    Generate project directory tree with proper formatting

    Parameters:
        startpath: Project root directory path
        ignore_dirs: List of directories to ignore
        ignore_files: List of files to ignore
    """
    if ignore_dirs is None:
        ignore_dirs = [".git", "__pycache__", "venv"]
    if ignore_files is None:
        ignore_files = [".gitignore", ".DS_Store"]

    output = []
    startpath = os.path.abspath(startpath)
    root_name = os.path.basename(startpath)
    output.append(f"{root_name}/")

    for root, dirs, files in os.walk(startpath):
        # Filter out directories to be ignored
        dirs[:] = [d for d in dirs if d not in ignore_dirs]

        # Calculate current hierarchy level
        relative_path = os.path.relpath(root, startpath)
        if relative_path == '.':
            level = 0
        else:
            level = len(relative_path.split(os.sep))

        # Process directories (excluding root)
        if level > 0:
            dir_name = os.path.basename(root)
            # Determine indentation based on level
            indent = "│   " * (level - 1)
            output.append(f"{indent}├── {dir_name}/")

        # Process files
        file_indent = "│   " * level
        for i, file in enumerate(sorted(files)):
            if file not in ignore_files:
                # Check if it's the last file in the directory
                if i == len(files) - 1 and not any(d not in ignore_dirs for d in dirs):
                    output.append(f"{file_indent}└── {file}")
                else:
                    output.append(f"{file_indent}├── {file}")

    # Write to file
    with open("projectStructure.md", "w", encoding="utf-8") as f:
        f.write("\n".join(output))

    return "\n".join(output)


if __name__ == "__main__":
    # Get current directory as starting path
    current_path = os.path.dirname(os.path.abspath(__file__))

    # Generate directory tree and print
    tree = generate_tree(current_path)
    print(tree)
