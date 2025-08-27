import os


def generate_tree(startpath, ignore_dirs=None, ignore_files=None):
    """
    Generate project directory tree with enhanced deep structure visualization
    """
    if ignore_dirs is None:
        ignore_dirs = [".git", "__pycache__", "venv"]
    if ignore_files is None:
        ignore_files = [".gitignore", ".DS_Store"]

    output = []
    # Add opening Markdown code block tag
    output.append("```")

    startpath = os.path.abspath(startpath)
    root_name = os.path.basename(startpath)
    output.append(f"{root_name}/")

    # Collect all directory information for subsequent judgments
    dir_hierarchy = {}
    for root, dirs, files in os.walk(startpath):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        files = [f for f in files if f not in ignore_files]
        dir_hierarchy[root] = {
            'dirs': dirs.copy(),
            'files': files.copy(),
            'parent': os.path.dirname(root)
        }

    # Generate directory tree
    for root, dirs, files in os.walk(startpath):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        files = [f for f in files if f not in ignore_files]

        # Calculate current hierarchy level
        relative_path = os.path.relpath(root, startpath)
        level = len(relative_path.split(os.sep)) if relative_path != '.' else 0

        # Process subdirectories (excluding root directory)
        if level > 0:
            dir_name = os.path.basename(root)
            parent_dir = dir_hierarchy[root]['parent']

            # Determine if it's the last subdirectory of the parent directory
            is_last_dir = dir_name == dir_hierarchy[parent_dir]['dirs'][-1] if dir_hierarchy[parent_dir][
                'dirs'] else False

            # Build indentation - accurately calculate connecting lines for each level
            indent_segments = []
            current_path = parent_dir
            current_level = level - 1

            while current_level > 0:
                grandparent = dir_hierarchy[current_path]['parent']
                current_dir_name = os.path.basename(current_path)

                # Display vertical line if not the last subdirectory of ancestor directory
                if grandparent in dir_hierarchy and dir_hierarchy[grandparent]['dirs'] and current_dir_name != \
                        dir_hierarchy[grandparent]['dirs'][-1]:
                    indent_segments.insert(0, "│   ")
                else:
                    indent_segments.insert(0, "    ")

                current_path = grandparent
                current_level -= 1

            indent = ''.join(indent_segments)
            connector = "└── " if is_last_dir else "├── "
            output.append(f"{indent}{connector}{dir_name}/")

        # Process files
        if files:
            # Build file indentation
            file_indent_segments = []
            current_path = root
            current_level = level

            while current_level > 0:
                parent = dir_hierarchy[current_path]['parent']
                current_dir_name = os.path.basename(current_path)

                if parent in dir_hierarchy and dir_hierarchy[parent]['dirs'] and current_dir_name != \
                        dir_hierarchy[parent]['dirs'][-1]:
                    file_indent_segments.insert(0, "│   ")
                else:
                    file_indent_segments.insert(0, "    ")

                current_path = parent
                current_level -= 1

            file_indent = ''.join(file_indent_segments)

            # Process each file, determine if it's the last item
            for i, file in enumerate(sorted(files)):
                # Check if it's the last file and there are no more subdirectories
                is_last_item = (i == len(files) - 1) and (len(dirs) == 0)
                connector = "└── " if is_last_item else "├── "
                output.append(f"{file_indent}{connector}{file}")

    # Add closing Markdown code block tag
    output.append("```")

    # Write to file
    with open("projectStructure.md", "w", encoding="utf-8") as f:
        f.write("\n".join(output))

    return "\n".join(output)


if __name__ == "__main__":
    current_path = os.path.dirname(os.path.abspath(__file__))
    tree = generate_tree(current_path)
    print(tree)