import os


def generate_tree(startpath, ignore_dirs=None, ignore_files=None):
    """
    Generate project directory tree with proper formatting
    """
    if ignore_dirs is None:
        ignore_dirs = [".git", "__pycache__", "venv"]
    if ignore_files is None:
        ignore_files = [".gitignore", ".DS_Store"]

    output = []
    startpath = os.path.abspath(startpath)
    root_name = os.path.basename(startpath)
    output.append(f"{root_name}/")

    # First pass: collect all directory information
    dir_info = {}
    for root, dirs, files in os.walk(startpath):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        files = [f for f in files if f not in ignore_files]
        dir_info[root] = {
            'dirs': dirs.copy(),
            'files': files.copy()
        }

    # Second pass: generate directory tree
    for root, dirs, files in os.walk(startpath):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        files = [f for f in files if f not in ignore_files]

        # Calculate current level
        relative_path = os.path.relpath(root, startpath)
        if relative_path == '.':
            level = 0
        else:
            level = len(relative_path.split(os.sep))

        # Process subdirectories (excluding root directory)
        if level > 0:
            dir_name = os.path.basename(root)
            parent_dir = os.path.dirname(root)

            # Determine if it's the last subdirectory of the parent directory
            is_last = dir_name == dir_info[parent_dir]['dirs'][-1]

            # Build indentation
            indent = ""
            if level > 1:
                # Traverse up through directories to determine indentation style
                current_path = parent_dir
                for i in range(level - 2, 0, -1):
                    grandparent = os.path.dirname(current_path)
                    current_dir_name = os.path.basename(current_path)
                    if current_dir_name != dir_info[grandparent]['dirs'][-1]:
                        indent = "│   " + indent
                    else:
                        indent = "    " + indent
                    current_path = grandparent

            # Determine connector
            connector = "└── " if is_last else "├── "
            output.append(f"{indent}{connector}{dir_name}/")

        # Process files
        if files:
            # Build file indentation
            file_indent = ""
            if level > 0:
                current_path = root
                for i in range(level - 1, 0, -1):
                    parent = os.path.dirname(current_path)
                    current_dir_name = os.path.basename(current_path)
                    if current_dir_name != dir_info[parent]['dirs'][-1]:
                        file_indent = "│   " + file_indent
                    else:
                        file_indent = "    " + file_indent
                    current_path = parent

            # Process each file
            for i, file in enumerate(sorted(files)):
                is_last_file = (i == len(files) - 1) and (len(dirs) == 0)
                connector = "└── " if is_last_file else "├── "
                output.append(f"{file_indent}{connector}{file}")

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
