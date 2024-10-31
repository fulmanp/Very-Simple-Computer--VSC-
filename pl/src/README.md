# VSC emulator

[![Selct language](../../icon20x24px-exported-transparent.png)](../../README.md)
[English](../../en/src/README.md)


- VSC 1.0 [source code](../../src/1_0/vsc.py)
- Opis zestawu instrukcji [Markdown](instruction_set.md), [PDF](instruction_set.pdf)
- Przykłady:

  - Przykładowa [bardzo prosta sesja VSC](examples/session_simple_test.md) przeprowadzona na pliku [`simple_test.mc`](examples/simple_test.mc).
  - Przykładowa [sesja z VSC](examples/session_tutorial_05_01.md) przeprowadzona na pliku [`tutorial_05_01.mc`](examples/tutorial_05_01.mc).
  - Przykładowa [sesja z VSC](examples/session_scalar_product.md) przeprowadzona na pliku [`scalar_product.asm`](examples/scalar_product.asm).

## Konwertery

Plik `*.asm` zawiera czytelny dla człowieka kod maszynowy z mnemonikami i etykietami, bez jawnych adresów.

Plik `*.mca` zawiera kod pośredni, który jest mieszanką asemblera i kodu maszynowego: zawiera mnemoniki, ale zamiast etykiet są dokładne adresy.

Plik `*.mc` to czysty kod maszynowy z dokładnymi adresami i instrukcjami zakodowanymi jako liczby.

- [Konwerter z assemblera (`*.mca`) na kod maszynowy z mnemonikami (`*.mca`)](../../src/1_0/asm2mca.py)
- [Konwerter z kodu maszynowego z mnemonikami (`*.mca`) na kod maszynowy (`*.mc`)](../../src/1_0/mca2mc.py)

## Przykładowe rozwiązania zadań

- [`tutorial_02_01_solution_1_2.mc`](examples/tutorial_02_01_solution_1_2.mc)
- [`tutorial_04_02_solution_2_2.mc`](examples/tutorial_04_02_solution_2_2.mc)
- [`tutorial_05_01.mc`](examples/tutorial_05_01.mc)
- [`tutorial_05_03_solution_3_1.mc`](examples/tutorial_05_03_solution_3_1.mc)
- [`tutorial_06_05_solution_1.mc`](examples/tutorial_06_05_solution_1.mc)
- [`tutorial_06_05_solution_2.mc`](examples/tutorial_06_05_solution_2.mc)
