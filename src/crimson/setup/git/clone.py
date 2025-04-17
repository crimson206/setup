import os
from utils.script_writer import write_script_file

default_paths = {
    "clone_repo": "./tmp/clone_repo.sh",
}

def generate_clone_repo_content(repo_name:str) -> str:
    script_content = f'git clone https://github.com/{repo_name}'
    return script_content

def write_clone_repo_script(repo_name:str, path: str = default_paths["clone_repo"]) -> None:
    content = generate_clone_repo_content(repo_name)
    write_script_file(path, content)

def clone_repo(repo_name:str, path: str = default_paths["clone_repo"]) -> None:
    write_clone_repo_script(repo_name)
    os.execv("/bin/bash", ["/bin/bash", path])
