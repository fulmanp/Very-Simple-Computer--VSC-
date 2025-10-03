import os
import sys
import subprocess

def execute_commands(base_name):
    asm_path = f"{base_name}.asm"
    mca_path = f"{sys.argv[2]}.mca" if len(sys.argv) == 3 else f"{base_name}.mca"
    mc_path = f"{sys.argv[2]}.mc" if len(sys.argv) == 3 else f"{base_name}.mc"

    if not os.path.isfile(asm_path):
        print(f"Error: The file '{asm_path}' does not exist.")
        return

    # | tail -n +15
    def process_output(output, file_path):
        lines = output.splitlines()
        processed_output = "\n".join(lines[14:])
        print(processed_output)
        with open(file_path, 'w') as file:
            file.write(processed_output)

    # Execute the first command (asm2mca.py) and process its output
    print(f"{mca_path}:")
    command1 = [sys.executable, 'asm2mca.py', asm_path]
    result1 = subprocess.run(command1, capture_output=True, text=True)
    process_output(result1.stdout, mca_path)

    print()
    
    # Execute the second command (mca2mc.py) and process its output
    print(f"{mc_path}:")
    command2 = [sys.executable, 'mca2mc.py', mca_path]
    result2 = subprocess.run(command2, capture_output=True, text=True)
    process_output(result2.stdout, mc_path)

if __name__ == "__main__":
    if len(sys.argv) not in {2, 3}:
        print("Usage: py asm2mc.py <base_name> [output_file]")
        sys.exit(1)

    base_name = sys.argv[1].removesuffix(".asm")
    execute_commands(base_name)
