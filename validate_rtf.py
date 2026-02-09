from pathlib import Path
from rtfparse.parser import Rtf_Parser
import sys

def validate_rtf(filepath):
    p = Path(filepath)
    if not p.exists():
        print(f"❌ {filepath}: File not found")
        return False
    try:
        parser = Rtf_Parser(rtf_path=p)
        parsed = parser.parse_file()
        print(f"✅ {filepath}: Valid RTF")
        return True
    except Exception as e:
        print(f"❌ {filepath}: Invalid RTF — {type(e).__name__}: {e}")
        return False

if len(sys.argv) < 2:
    print("Usage: python validate_rtf.py <file1.rtf> [file2.rtf ...]")
    sys.exit(1)

results = [validate_rtf(f) for f in sys.argv[1:]]
sys.exit(0 if all(results) else 1)
