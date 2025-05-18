from .core import run_all
import json

def main():
    result = run_all()
    print(json.dumps(result, indent=2))
