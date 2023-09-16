#!/usr/bin/env python3
"""Log stats from collection"""

import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["logs"]
collection = db["nginx"]

# Count the total number of logs
total_logs = collection.count_documents({})

# Count the number of logs for each HTTP method
http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {method: collection.count_documents({"method": method}) for method in http_methods}

# Count the number of logs with method=GET and path=/status
status_log_count = collection.count_documents({"method": "GET", "path": "/status"})

# Print the statistics
print(f"{total_logs} logs where {total_logs} is the number of documents in this collection")
print("Methods:")
for method in http_methods:
    print(f"\t{method}: {method_counts[method]}")
print(f"{status_log_count} logs with method=GET and path=/status")
