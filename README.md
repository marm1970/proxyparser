# Proxy Parser

A multithreaded Python script to fetch, validate, and save HTTP proxies with a user-friendly console interface powered by **rich**.

## Features
- Fetch proxies from [ProxyScrape](https://proxyscrape.com/).
- Validate proxies against a target URL (default: Google).
- Save valid proxies to a text file for future use.
- Leverages multithreading for efficient proxy validation.

## Installation

Follow these steps to set up the project:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/marm1970/proxyparser.git
   cd proxyparser
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate    # On Linux/MacOS
   venv\Scripts\Activate.ps1   # On Windows
   ```

3. **Install Dependencies**
   ```bash
   python -m pip install requests rich
   ```
## Usage

1. Run the script:
   ```bash
   python main.py
   ```

2. Enter the name of the output file when prompted (e.g., `valid_proxies.txt`).

3. The script will:
   - Fetch proxies from the API.
   - Validate each proxy using a multithreaded approach.
   - Save the valid proxies to the specified file.

## Contribution

Contributions are welcome! Here’s how you can contribute:

1. Fork the repository.
2. Create a new branch for your feature/bugfix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push the branch to your forked repository:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request with a clear description of your changes.

## License

This project is open-source and available under the [MIT License](LICENSE).
