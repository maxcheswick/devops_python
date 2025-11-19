def read_logs(file_path):
    """
    Read all log files and return them as a list of strings
    """
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
        return lines
    except FileNotFoundError:
        print(f"Error: file not found {file_path}")
        return []
    except Exception as e:
        print(f"Error: Unexpected error while reading {file_path}: {e}")
        return []
            