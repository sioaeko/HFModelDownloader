import os
import requests
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import argparse

CHUNK_SIZE = 1024 * 1024  # 1MB chunks

def download_chunk(url, start, end, filename):
    headers = {'Range': f'bytes={start}-{end}'}
    response = requests.get(url, headers=headers, stream=True)
    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

def download_file(url, output_dir, num_parts):
    response = requests.head(url)
    file_size = int(response.headers.get('content-length', 0))
    
    if file_size == 0:
        print(f"Unable to determine file size for {url}")
        return

    part_size = file_size // num_parts
    filename = os.path.basename(urlparse(url).path)
    
    with ThreadPoolExecutor(max_workers=num_parts) as executor:
        futures = []
        for i in range(num_parts):
            start = i * part_size
            end = start + part_size - 1 if i < num_parts - 1 else file_size - 1
            part_filename = f"{filename}.part{i+1}"
            futures.append(
                executor.submit(download_chunk, url, start, end, os.path.join(output_dir, part_filename))
            )
        
        for future in tqdm(as_completed(futures), total=num_parts, desc=f"Downloading {filename}"):
            future.result()

    print(f"All parts of {filename} have been downloaded.")

def combine_parts(filename, output_dir, num_parts):
    with open(os.path.join(output_dir, filename), 'wb') as outfile:
        for i in range(num_parts):
            part_filename = f"{filename}.part{i+1}"
            with open(os.path.join(output_dir, part_filename), 'rb') as infile:
                outfile.write(infile.read())
            os.remove(os.path.join(output_dir, part_filename))
    print(f"All parts have been combined into {filename}")

def main(model_url, output_dir, num_parts):
    os.makedirs(output_dir, exist_ok=True)
    
    # Parse the model page
    response = requests.get(model_url)
    if response.status_code != 200:
        print(f"Failed to access the model page. Status code: {response.status_code}")
        return

    # Extract download links (this is a simplified version and may need adjustment)
    download_links = [link for link in response.text.split('"') if link.startswith("https://") and "blob" in link]

    for link in download_links:
        download_file(link, output_dir, num_parts)
    
    # Combine parts
    for link in download_links:
        filename = os.path.basename(urlparse(link).path)
        combine_parts(filename, output_dir, num_parts)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download Hugging Face model files in parts")
    parser.add_argument("model_url", help="URL of the Hugging Face model page")
    parser.add_argument("output_dir", help="Directory to save the downloaded files")
    parser.add_argument("--parts", type=int, default=5, help="Number of parts to split each file into")
    
    args = parser.parse_args()
    
    main(args.model_url, args.output_dir, args.parts)
