import os

def generate_tree(startpath, ignore_dirs=None, ignore_files=None):
    """
    Generate project directory tree
    
    Parameters:
        startpath: Project root directory path
        ignore_dirs: List of directories to ignore
        ignore_files: List of files to ignore
    """
    if ignore_dirs is None:
        ignore_dirs = ['.git', '__pycache__', 'venv']
    if ignore_files is None:
        ignore_files = ['.gitignore', '.DS_Store']
    
    output = []
    
    for root, dirs, files in os.walk(startpath):
        # Filter out directories to be ignored
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        
        # Calculate current hierarchy level
        level = root.replace(startpath, '').count(os.sep)
        indent = '│   ' * level
        
        # Add directory name
        dir_name = os.path.basename(root)
        if level > 0:
            output.append(f'{indent[:-4]}├── {dir_name}/')
        else:
            output.append(f'{dir_name}/')
        
        # Add files
        sub_indent = '│   ' * (level + 1)
        for file in sorted(files):
            if file not in ignore_files:
                output.append(f'{sub_indent[:-4]}├── {file}')
    
    # Write to file
    with open('projectStructure.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(output))
    
    return '\n'.join(output)

if __name__ == '__main__':
    # Get current directory as starting path
    current_path = os.path.dirname(os.path.abspath(__file__))
    
    # Generate directory tree and print
    tree = generate_tree(current_path)
    print(tree)