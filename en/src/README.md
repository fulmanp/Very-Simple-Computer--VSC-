# VSC emulator

[![Selct language](../../icon20x24px-exported-transparent.png)](../../README.md)
[polski](../../pl/src/README.md)

- VSC 1.0 [source code](../../src/1_0/vsc.py)
- Complete instruction set reference [Markdown](instruction_set.md), [PDF](instruction_set.pdf)
- Examples:

  - Example, very basic, [VSC session](examples/session_simple_test.md) on [`simple_test.mc`](examples/simple_test.mc) file.
  - Example [VSC session](examples/session_tutorial_05_01.md) on [`tutorial_05_01.mc`](examples/tutorial_05_01.mc) file.
  - Example [VSC session](examples/session_scalar_product.md) on [`scalar_product.asm`](examples/scalar_product.asm) file.

## Converters

`*.asm` file contains human readable machine code with mnemonics and labels, without explicite addresses.
  
`*.mca` file contains intermediate code which is a mixture of assembler and machine code: it contains mnemonics but instead of labels there are exact addresses.
  
`*.mc` file is a pure machine code with exact addresses and instructions encoded as numbers.
  
- [Converter from the assembler (`*.asm`) to the machine code with mnemonics (`*.mca`)](../../src/1_0/asm2mca.py)
- [Converter from the machine code with mnemonics (`*.mca`) to the machine code (`*.mc`)](../../src/1_0/mca2mc.py)

## Examples of task solutions

- [`tutorial_02_01_solution_1_2.mc`](examples/tutorial_02_01_solution_1_2.mc)
- [`tutorial_04_02_solution_2_2.mc`](examples/tutorial_04_02_solution_2_2.mc)
- [`tutorial_05_01.mc`](examples/tutorial_05_01.mc)
- [`tutorial_05_03_solution_3_1.mc`](examples/tutorial_05_03_solution_3_1.mc)
- [`tutorial_06_05_solution_1.mc`](examples/tutorial_06_05_solution_1.mc)
- [`tutorial_06_05_solution_2.mc`](examples/tutorial_06_05_solution_2.mc)
