filename = input("Enter a filename: ")

if filename.startswith("report") and filename.endswith(".pdf"):
    print("This is a valid report PDF file.")
else:
    print("This file is not a valid report PDF.")
