import sys
import log_tools

def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python main.py level <log_file> <LEVEL>")
        print("  python main.py time  <log_file> <START> <END>")
        sys.exit(1)
    
    mode = sys.argv[1]
    
    if mode == "level":
        if len(sys.argv) != 4:
            print("Usage: python main.py level <log_file> <LEVEL>")
            sys.exit(1)
            
        log_file = sys.argv[2]
        level = sys.argv[3]
        
        filtered = log_tools.filter_by_level(log_file, level)
        # filtered = log_tools.read_logs(log_file)
        
        print(f"Read {len(filtered)} from file {log_file} with log level {level}")
        
        for line in filtered[:5]:
            print(line.rstrip())
    elif mode == "time":
        if len(sys.argv) != 5:
            print("  python main.py time  <log_file> <START> <END>")
            sys.exit(1)
        
        log_file = sys.argv[2]
        start = sys.argv[3]
        end = sys.argv[4]
        
        filtered = log_tools.filter_by_time(log_file, start, end)
        for line in filtered[:5]:
            print(line.rstrip())
    else:
        print(f"Unknown mode: {mode}")
        sys.exit(1)
            
        
if __name__ == "__main__":
    main()
        
    