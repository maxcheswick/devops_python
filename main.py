import argparse
import log_tools

def main():
    parser = argparse.ArgumentParser(description="DevOps Python Log Utility")
    
    sub = parser.add_subparsers(dest="command")
    
    #logs command
    logs = sub.add_parser("logs", help="Filter logs by level or time range")
    logs.add_argument("--file", required=True, help="Path to the log file")
    logs.add_argument("--level", help="Log level to filter by(ERROR, DEBUG, etc)")
    logs.add_argument("--start", help="Start time (YYYY-MM-DD HH:MM:SS)")
    logs.add_argument("--end", help="End time (YYYY-MM-DD HH:MM:SS)")
    
    count = sub.add_parser("count", help="Count log levels in a file")
    count.add_argument("--file", required=True, help="Path to log file")
    
    args = parser.parse_args()
    
    if args.command == "logs":
        if args.level:
            out = log_tools.filter_by_level(args.file, args.level)
            print(f"Found {len(out)} lines filtered by {args.level}")
            for line in out:
                print(line.rstrip())
        elif args.start and args.end:
            out = log_tools.filter_by_time(args.file, args.start, args.end)
            print(f"Found {len(out)} lines filtered by start: {args.start} end: {args.end}")
            for line in out:
                print(line.rstrip())
        else:
            print(f"You must supply either --level or both --start and --end")
    elif args.command == "count":
        print(f"Need to add count function")
        
        
if __name__ == "__main__":
    main()
        
    