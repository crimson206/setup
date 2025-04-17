import os
from utils.script_writer import write_script_file

default_paths = {
    "install_gh_packages": "./tmp/install_gh_packages.sh",
}

def generate_install_gh_packages_in_linux_content() -> str:
    script_content = """
sudo apt update
sudo apt install -y git gh
sudo apt install -y wslu
"""
    return script_content

def write_install_gh_packages_script(path: str = default_paths["install_gh_packages"]) -> None:
    content = generate_install_gh_packages_in_linux_content()
    write_script_file(path, content)

def install_gh_packages(path: str = default_paths["install_gh_packages"]) -> None:
    write_install_gh_packages_script(path)
    os.execv("/bin/bash", ["/bin/bash", path])
