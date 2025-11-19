import datetime


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
            
            
def filter_by_level(file_path, level):
    """
    Return only the logs that are contained in that level.
    Example levels: INFO, ERROR, WARNING, DEBUG, CRITICAL
    """
    level = level.upper()
    lines = read_logs(file_path)
    
    filtered = []
    for line in lines:
        if level in line.upper():
            filtered.append(line)
        
    return filtered


def filter_by_time(file_path, start_time, end_time):
    """
    Filter the logs by a start time and an end time.
    Expected timestamp format at the start of each log line:
    YYYY-MM-DD HH:MM:SS

    Example:
    start_time = "2025-01-01 00:00:00"
    end_time   = "2025-01-01 12:00:00"
    """
    
    lines = read_logs(file_path)
    
    fmt = "%Y-%m-%d %H:%M:%S"
    
    start = datetime.datetime.strptime(start_time, fmt)
    end =datetime.datetime.strptime(end_time, fmt)
    
    results = []
    
    for line in lines:
        try:
            # Expect the timestamp to be like:
            # "2025-11-18 12:34:56 ERROR Something happened"
            # So timestamp is the first two items when split by space
            parts.line.split(" ")
            timestamp = parts[0] + " " + parts[1]
            ts = datetime.datetime.strptime(timestamp, fmt)
            
            if start <= ts <= end:
                results.append(line)
        except Exception:
            # If no valid timestamp then skip it
            continue
    
    return results