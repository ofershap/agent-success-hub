"""Bounded diagnostic messages only; never log submitted text or secrets."""
import re

def safe_error(error):
    name=type(error).__name__
    message=str(error)
    # Allowlist only dependency/model loading errors, which contain no submission data.
    if name not in {'OSError','ImportError','ModuleNotFoundError'}:
        return name+': details withheld; inspect dependency/model load separately'
    message=re.sub(r'https?://\S+', '[url omitted]', message)
    message=re.sub(r'(?i)(token|password|secret|authorization|api[_ -]?key)[^\n]*','[secret-bearing detail omitted]',message)
    message=re.sub(r'(github_pat_|gh[pousr]_|hf_|sk-)[A-Za-z0-9_-]+','[credential omitted]',message)
    return name+': '+message[:600]
