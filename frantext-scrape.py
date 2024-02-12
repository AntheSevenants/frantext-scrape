import urllib.request, json 
import argparse
from tqdm.auto import tqdm
from pathlib import Path
import os

parser = argparse.ArgumentParser(
    description='frantext-scrape - A scraper for the frantext corpus for Julie Nijs')
parser.add_argument('--output_dir', type=str, default="out",
                    help='Name of the output directory')
args = parser.parse_args()

# The metadata endpoint gives a list of all files and their metadata (nice)
metadata_endpoint = "https://www.frantext.fr/allegro/repositories/frantext/queries/metadata"
# I saved the POST query separately
with open("metadata.json", "rt") as reader:
    metadata = json.loads(reader.read())

# Send request and get response
req = urllib.request.Request(metadata_endpoint)
req.add_header('Content-Type', 'application/json; charset=utf-8')
json_data = json.dumps(metadata)
json_bytes = json_data.encode('utf-8')
req.add_header('Content-Length', len(json_bytes))
response = urllib.request.urlopen(req, json_bytes)

response_json = json.loads(response.read().decode("UTF-8"))

# Create output dirs
metadata_dir = f"{args.output_dir}/metadata/"
text_dir = f"{args.output_dir}/text/"

os.makedirs(args.output_dir, exist_ok=True)
os.makedirs(metadata_dir, exist_ok=True)
os.makedirs(text_dir, exist_ok=True)

# Download each file and write metadata
for document in tqdm(response_json["results"], desc="XML files"):
    xml_filename = document["document"]
    xml_path = Path(xml_filename)

    # Write metadata
    metadata = document["metadata"]
    with open(f"{metadata_dir}/{xml_path.stem}.json", "wt") as writer:
        writer.write(json.dumps(metadata, indent=4))

    # Download content
    try:
        with urllib.request.urlopen(f"https://www.frantext.fr/allegro/repositories/frantext/documents/{xml_filename}/content") as reader:
            data = reader.read()
    except:
        print(f"Cannot download {xml_filename}: this file is probably under copyright")
    else:
        with open(f"{text_dir}/{xml_filename}", "wt") as writer:
            writer.write(data.decode("UTF-8"))

print("Done")