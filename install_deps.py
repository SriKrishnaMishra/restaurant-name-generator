import subprocess
import sys

def install_requirements():
    packages = [
        "numpy==1.26.4",
        "transformers==4.40.1",
        "torch",
        "langchain==0.1.20",
        "langchain-community==0.0.30",
        "sentence-transformers",
        "streamlit"
    ]
    for package in packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install_requirements()
