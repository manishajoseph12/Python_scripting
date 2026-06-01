# Question 1: The Log File Parser (Data Filtering)

# The Scenario: You are given a massive block of server log data. Every line starts with a timestamp, followed by a status code (INFO, WARNING, or ERROR), and a message.Your Task: Write a script to calculate the total number of logs, and extract only the messages that contain an ERROR.

# Sample Input:

# Plaintext

# 2026-05-26 10:00:01 INFO User admin logged in successfully.
# 2026-05-26 10:02:15 WARNING Disk usage reached 85%.
# 2026-05-26 10:05:40 ERROR Database connection timeout occurred on port 5432.
# 2026-05-26 10:06:12 INFO Generated monthly sales report.
# 2026-05-26 10:12:00 ERROR Failed to write to file system permissions error. 

# Expected output:

# Total Logs Processed: 5

# Extracted Error Messages:
# - Database connection timeout occurred on port 5432.
# - Failed to write to file system permissions error.

import sys

def parse_logs():
    total_logs = 0
    error_messages = []
    
    # sys.stdin reads data line-by-line as it is input
    for line in sys.stdin:
        # Strip newline characters and skip empty lines
        cleaned_line = line.strip()
        if not cleaned_line:
            continue
            
        total_logs += 1
        
        # Check for ERROR in the log line
        if "ERROR" in cleaned_line:
            parts = cleaned_line.split("ERROR ", 1)
            if len(parts) > 1:
                error_messages.append(parts[1])

    # Print results exactly as requested
    print(f"Total Logs Processed: {total_logs}")
    print("\nExtracted Error Messages:")
    for msg in error_messages:
        print(f"- {msg}")

if __name__ == "__main__":
    parse_logs()