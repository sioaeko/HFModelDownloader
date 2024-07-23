# 🤗 Hugging Face Model Downloader

<img src="https://github.com/user-attachments/assets/1f096ce3-b0b8-490f-a56a-8728e1050497" width="90%" alt="Hugging Face Model Downloader">

A Python script for efficiently downloading and reconstructing large Hugging Face model files by splitting them into manageable chunks.

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## ✨ Features

- 🚀 Downloads large model files from Hugging Face in multiple parts simultaneously
- 🔗 Automatically extracts download links from the model page
- 🔧 Allows customization of the number of parts for splitting files
- 🧩 Combines downloaded parts back into the original file
- 📊 Displays download progress for each file

## 🛠 Requirements

- Python 3.6+
- `requests` library
- `tqdm` library

## 📥 Installation

1. Clone this repository:
```
git clone https://github.com/sioaeko/huggingface-split-downloader.git
cd huggingface-split-downloader
```
2. Install the required dependencies:
```
pip install requests tqdm
```
## 🚀 Usage

Run the script with the following command:
```
python huggingface_split_downloader.py <model_url> <output_dir> --parts <number_of_parts>
```
### Arguments:
- `<model_url>`: The URL of the Hugging Face model page
- `<output_dir>`: The directory where you want to save the downloaded files
- `--parts`: (Optional) The number of parts to split each file into (default is 5)

### Example:
```
python huggingface_split_downloader.py https://huggingface.co/gpt2 ./downloaded_model --parts 10
```
This command will download the GPT-2 model files, splitting each file into 10 parts, and save them in the `./downloaded_model` directory.

## 🔧 How it works

1. 🔍 Access the provided Hugging Face model page and extract download links
2. For each file:
   - 📏 Determine the file size
   - ✂️ Split the download into the specified number of parts
   - 📥 Download each part concurrently
   - 📊 Show a progress bar for the download
3. 🧩 Combine parts back into the original file
4. 🗑️ Delete partial files after successful combination

## 📝 Notes

- 💾 Ensure you have sufficient storage space for the model files
- 🌐 Download speed may vary depending on your internet connection
- 🔄 The script may need adjustments if the structure of the Hugging Face website changes

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is for educational and research purposes. Always ensure you have the right to download and use the models as per Hugging Face's terms of service.
