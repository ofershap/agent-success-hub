"""Patch an existing recipe MCP bundle after new canonical assets are verified live.
Usage: python migrate_mcp_upstream.py INPUT_BUNDLE OUTPUT_BUNDLE
Deployment credentials, service paths and machine identifiers are intentionally excluded.
"""
from pathlib import Path
import sys
s=Path(sys.argv[1]).read_text();old='https://ofershap.github.io/agent-success-hub/';new='https://itzik-community-benefits.pages.dev/library/'
assert s.count(old)==1, 'Unexpected bundle, inspect before changing'
s=s.replace(old,new)
s=s.replace('url:Bo+"recipes/"+Ut(p)+".html"','url:Bo+"recipes/"+Ut(p)+"/"').replace('url:Bo+"recipes/"+n+(i==="en"?"-en":"")+".html"','url:Bo+"recipes/"+n+(i==="en"?"-en":"")+"/"')
s=s.replace('r&&r!=="https://ofershap.github.io"','r&&r!=="https://itzik-community-benefits.pages.dev"&&r!=="https://ofershap.github.io"')
assert old not in s
Path(sys.argv[2]).write_text(s)
