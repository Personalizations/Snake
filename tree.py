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

    # Used to track the processing status of each directory
    dir_status = {}

    # First pass: collect all directory information
    for root, dirs, files in os.walk(startpath):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        filtered_files = [f for f in files if f not in ignore_files]
        dir_status[root] = {
            'dirs': dirs.copy(),
            'files': filtered_files
        }

    # Second pass: generate the directory tree
    for root, dirs, files in os.walk(startpath):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        filtered_files = [f for f in files if f not in ignore_files]

        # Calculate current hierarchy level
        relative_path = os.path.relpath(root, startpath)
        if relative_path == '.':
            level = 0
        else:
            level = len(relative_path.split(os.sep))

        # Process directories (excluding root directory)
        if level > 0:
            dir_name = os.path.basename(root)
            parent_dir = os.path.dirname(root)

            # Check if it's the last subdirectory of the parent directory
            is_last_dir = False
            if parent_dir in dir_status:
                siblings = dir_status[parent_dir]['dirs']
                is_last_dir = (dir_name == siblings[-1])

            # Build indentation
            indent_parts = []
            for i in range(level - 1):
                # For upper-level directories, display connecting lines if not the last subdirectory
                ancestor_path = os.path.abspath(startpath)
                for j in range(i + 1):
                    ancestor_path = os.path.join(ancestor_path, os.listdir(ancestor_path)[0])

                ancestor_parent = os.path.dirname(ancestor_path)
                if ancestor_parent in dir_status:
                    ancestor_name = os.path.basename(ancestor_path)
                    ancestor_siblings = dir_status[ancestor_parent]['dirs']
                    if ancestor_name != ancestor_siblings[-1]:
                        indent_parts.append("│   ")
                    else:
                        indent_parts.append("    ")

            indent = ''.join(indent_parts)
            connector = "└── " if is_last_dir else "├── "
            output.append(f"{indent}{connector}{dir_name}/")

        # Process files
        file_indent_parts = []
        for i in range(level):
            ancestor_path = os.path.abspath(startpath)
            for j in range(i + 1):
                if os.path.isdir(ancestor_path) and os.listdir(ancestor_path):
                    ancestor_path = os.path.join(ancestor_path, os.listdir(ancestor_path)[0])

            ancestor_parent = os.path.dirname(ancestor_path)
            if ancestor_parent in dir_status:
                ancestor_name = os.path.basename(ancestor_path)
                ancestor_siblings = dir_status[ancestor_parent]['dirs']
                if ancestor_name != ancestor_siblings[-1]:
                    file_indent_parts.append("│   ")
                else:
                    file_indent_parts.append("    ")

        file_indent = ''.join(file_indent_parts)

        for i, file in enumerate(sorted(filtered_files)):
            is_last_file = (i == len(filtered_files) - 1) and (len(dirs) == 0)
            connector = "└── " if is_last_file else "├── "
            output.append(f"{file_indent}{connector}{file}")

    # Write to file
    with open("projectStructure.md", "w", encoding="utf-8") as f:
        f.write("\n".join(output))

    return "\n".join(output)


if __name__ == "__main__":
    # Get current directory as starting path
    current_path = os.path.dirname(os.path.abspath(__file__))

    # Generate directory tree and print it
    tree = generate_tree(current_path)
    print(tree)
