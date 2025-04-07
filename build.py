## 🐍 `build.py` (Cross-Platform Build Script)

import argparse
import os
import subprocess
import sys

def run_command(cmd):
    print(f">>> {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"❌ Command failed with code {result.returncode}")
        sys.exit(result.returncode)

def main():
    parser = argparse.ArgumentParser(description="Cross-platform build helper for Embedded C projects.")
    parser.add_argument('--toolchain', type=str, help='Path to CMake toolchain file (optional)')
    args = parser.parse_args()

    build_dir = "build"
    os.makedirs(build_dir, exist_ok=True)

    cmake_cmd = f'cmake -S . -B {build_dir}'
    if args.toolchain:
        cmake_cmd += f' -DCMAKE_TOOLCHAIN_FILE={args.toolchain}'

    run_command(cmake_cmd)
    run_command(f'cmake --build {build_dir}')

if __name__ == "__main__":
    main()
