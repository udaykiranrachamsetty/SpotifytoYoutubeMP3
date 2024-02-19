import subprocess
import sys

requires = [
    'flask',
    'spotipy',
    'html5lib',
    'requests',
    'beautifulsoup4',
    'pytube',
    'google-api-python-client',
    'pandas',
    'pyarrow'
]

def install_package(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except subprocess.CalledProcessError as e:
        print(f"Error installing {package}: {e}")

if __name__ == "__main__":
    for package in requires:
        install_package(package)
        print(f"Successfully installed {package}")
