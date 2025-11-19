import sys
import log_tools

def main():
    if len(sys.argv) > 2:
        print(f"Error: python main.py <log_file_path>")
        sys.exit(1)
        
    log_file = sys.argv[1]
    lines = log_tools.read_logs(log_file)
    
    print(f"Read {len(lines)} from file {log_file}")
    
    for line in lines[:5]:
        print(line.rstrip())
        
if __name__ == "__main__":
    main()
        
    