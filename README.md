# FiveM Cache Cleaner

A simple and efficient tool to clean FiveM cache and browser data. This tool helps resolve common issues related to FiveM cache, such as loading problems, connection issues, or game performance.

## 🌟 Features

- Automatic cache directory detection
- Browser data cleaning
- User-friendly interface
- Detailed error reporting
- Administrator privileges check
- Safe operation with confirmation prompt

## 📋 Requirements

- Windows Operating System
- Python 3.6 or higher
- FiveM installed
- Administrator privileges (for full access to cache directories)

## 🚀 Installation

1. Clone this repository or download the script:
```bash
git clone https://github.com/yourusername/fivem-cache-cleaner.git
```

2. Navigate to the directory:
```bash
cd fivem-cache-cleaner
```

3. Make sure Python is installed on your system.

## 💻 Usage

### Method 1: Direct Execution
Simply double-click the `cache_cleaner.py` file to run it. However, this might not provide administrator privileges.

### Method 2: Command Line (Recommended)
1. Open Command Prompt as Administrator
2. Navigate to the script directory
3. Run the script:
```bash
python cache_cleaner.py
```

## ⚙️ What It Cleans

The script cleans the following directories:
- `%LocalAppData%\FiveM\FiveM.app\cache`
- `%LocalAppData%\FiveM\FiveM.app\browser`

## ⚠️ Warning

- Always close FiveM completely before running the cleaner
- Make sure you have administrator privileges
- Backup any important cache data if necessary
- The cleaning process cannot be undone

## 🔍 Troubleshooting

### Common Issues:

1. **"Permission denied" error**
   - Solution: Run the script as administrator

2. **"Directory not found" error**
   - Solution: Verify FiveM installation path
   - Check if FiveM is installed correctly

3. **Script doesn't run**
   - Solution: Verify Python installation
   - Check if you have Python 3.6 or higher installed
