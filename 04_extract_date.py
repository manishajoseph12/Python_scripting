bulk_logs = """
[2026-05-28 14:32:10] USER_LOGIN_SUCCESS: admin
[2026-05-28 14:35:22] DATABASE_CONNECTED
[2026-05-28 14:40:01] FILE_UPLOADED: report.pdf
[2026-05-28 14:45:15] USER_LOGOUT: admin
"""

# A list to store all our extracted timestamps
all_timestamps = []

# Loop through each line in the bulk text
for line in bulk_logs.splitlines():
    # Skip empty lines
    if not line.strip():
        continue
        
    # Find brackets and slice the string
    start = line.find("[") + 1
    end = line.find("]")
    timestamp = line[start:end]
    
    # Save it to our list
    all_timestamps.append(timestamp)

# Print the final result
print("Extracted Timestamps:")
print(all_timestamps)