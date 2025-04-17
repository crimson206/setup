from pathlib import Path

def write_script_file(path: str, content: str) -> None:
    script_path = Path(path)
    script_path.parent.mkdir(parents=True, exist_ok=True)
    script_path.write_text(content)
    script_path.chmod(0o755)
