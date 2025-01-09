import os
import sys
import subprocess

def execute_commands(base_name):
    asm_path = f"{base_name}.asm"
    mca_path = f"{base_name}.mca"
    mc_path = f"{base_name}.mc"

    if not os.path.isfile(asm_path):
        print(f"Error: The file '{asm_path}' does not exist.")
        return

    # Execute the first command (asm2mca.py) and show its output
    print(f"{mca_path}:")
    command1 = [sys.executable, 'asm2mca.py', asm_path]
    result1 = subprocess.run(command1, capture_output=True, text=True)
    print(result1.stdout)
    with open(mca_path, 'w') as mca_file:
        subprocess.run(command1, stdout=mca_file)
    # print(f"py asm2mca.py {asm_path} > {mca_path}\n")

    # Execute the second command (mca2mc.py) and show its output
    print(f"{mc_path}:")
    command2 = [sys.executable, 'mca2mc.py', mca_path]
    result2 = subprocess.run(command2, capture_output=True, text=True)
    print(result2.stdout)
    with open(mc_path, 'w') as mc_file:
        subprocess.run(command2, stdout=mc_file)
    # print(f"py mca2mc.py {mca_path} > {mc_path}\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: py to.py <base_name>")
        sys.exit(1)

    base_name = sys.argv[1]
    if base_name.endswith(".asm"):
        base_name = base_name[:-4]
    execute_commands(base_name)