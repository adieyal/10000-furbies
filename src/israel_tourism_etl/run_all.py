import argparse
from . import discover_sources, download_sources, build_long_dataset, validate_dataset, export_outputs

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--start',default='2015-01'); ap.add_argument('--end',default='2026-05')
    a=ap.parse_args(); discover_sources.main(['--start',a.start,'--end',a.end]); download_sources.main(); build_long_dataset.main(); validate_dataset.main(a.start,a.end); export_outputs.main()
if __name__=='__main__': main()
