Analyze the Apache access log located at /app/access.log and produce a JSON report at /app/report.json.

Your report must satisfy all of the following:

1. The output file must be valid JSON and written to /app/report.json.
2. Include a field named total_requests equal to the total number of log entries.
3. Include a field named unique_ips equal to the number of distinct client IP addresses.
4. Include a field named top_path equal to the most frequently requested request path.
