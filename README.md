# 📱 FreeMobileSMS

[![CI](https://github.com/nakmuaycoder/freeMobileSMS/actions/workflows/ci.yml/badge.svg)](https://github.com/nakmuaycoder/freeMobileSMS/actions/workflows/ci.yml)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)

A robust and modern Python wrapper for the **Free Mobile SMS API**. Send text notifications to your mobile phone instantly via CLI or Python script.

---

## 🚀 Features

- **Modern & Robust**: Built with `requests`, including proper error handling and configurable timeouts.
- **Developer Friendly**: Fully managed with `uv` for lightning-fast dependency management.
- **Dual Usage**: Use it as a command-line tool (CLI) or as a Python library.
- **Production Ready**: Includes unit tests, linting (Ruff), and GitHub Actions CI.

---

## 🛠️ Installation

The easiest way to install and set up the project is using the provided `Makefile`.

```shell
git clone https://github.com/nakmuaycoder/freeMobileSMS.git
cd freeMobileSMS
make install
```

*This will create a virtual environment, install all dependencies, and set up pre-commit hooks.*

---

## 📖 Usage

### 💻 Command Line (CLI)

After installation, you can use the `sms` command directly:

```shell
sms --user YOUR_ID --password YOUR_PASS --message "Hello from the CLI!"
```

Or run it via `python`:

```shell
python -m freeMobileSMS --user YOUR_ID --password YOUR_PASS --message "Hello!" --timeout 30
```

### 🐍 Python Library

Integrate SMS notifications into your own Python applications:

```python
from freeMobileSMS import FreeMobileTxtMe

# Initialize the texter
free = FreeMobileTxtMe(
    free_mobile_user="your_user_id",
    free_mobile_pass="your_api_key",
    timeout=15  # Optional: defaults to 10s
)

# Send the message
success = free.send_message("Server alert: CPU usage is high! 🚨")

if success:
    print("SMS sent successfully!")
else:
    print("Failed to send SMS.")
```

---

## 🧪 Development

We use `uv` and `make` to streamline development.

- **Run Tests**: `make test`
- **Lint Code**: `make lint`
- **Format Code**: `make format`
- **Clean Project**: `make clean`

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
