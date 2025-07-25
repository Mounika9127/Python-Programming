import re

# Read from input file
input_file = "sample.txt"
output_file = "extracted_emails.txt"

try:
    with open(input_file, "r") as file:
        content = file.read()

    # Regular expression to find email addresses
    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", content)

    # Remove duplicates and sort
    unique_emails = sorted(set(emails))

    # Write to output file
    with open(output_file, "w") as file:
        for email in unique_emails:
            file.write(email + "\n")

    print(f"✅ Extracted {len(unique_emails)} email(s) and saved to '{output_file}'.")

except FileNotFoundError:
    print(f"❌ File '{input_file}' not found. Please check the file name and path.")

