import os
from utils.script_writer import write_script_file

default_paths = {
    "setup_gituser": "./tmp/setup_gituser.sh",
}

def generate_git_config_script_content(name: str, email: str, use_global: bool = True) -> str:
    scope = "--global" if use_global else ""
    lines = [
        f'git config {scope} user.name "{name}"',
        f'git config {scope} user.email "{email}"'
    ]
    return "\n".join(lines)

def write_git_config_script(name: str, email: str, path: str = default_paths["setup_gituser"], use_global: bool = True) -> None:
    content = generate_git_config_script_content(name, email, use_global)
    write_script_file(path, content)

def setup_gituser(name: str, email: str, path: str = default_paths["setup_gituser"], use_global: bool = True) -> None:
    write_git_config_script(name, email, path, use_global)
    os.execv("/bin/bash", ["/bin/bash", path])
