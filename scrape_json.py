import json


def extract_fields(json_filename):
    # Open and load the contents of the JSON file
    with open(json_filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 'results' is where the list of items is stored
    results = data["results"]

    # Loop through each item in results and extract 'comment' and 'srcContext'
    for item in results:
        comment = item.get("comment", None)
        src_context = item.get("srcContext", None)

        print(src_context)
        print(comment)
        print()


if __name__ == "__main__":
    # Call the function with the filename
    extract_fields("output.json")
