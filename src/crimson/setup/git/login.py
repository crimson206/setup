import os
from utils.script_writer import write_script_file

default_paths = {
    "login_gh_using_web": "./tmp/login_gh_using_web.sh",
}

def generate_login_gh_using_web_content() -> str:
    script_content = 'gh auth login --web'
    return script_content

def write_login_gh_using_web_script(path: str = default_paths["login_gh_using_web"]) -> None:
    content = generate_login_gh_using_web_content()
    write_script_file(path, content)

def login_gh_using_web(path: str = default_paths["login_gh_using_web"]) -> None:
    write_login_gh_using_web_script(path)
    os.execv("/bin/bash", ["/bin/bash", path])
