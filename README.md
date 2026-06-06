# 3-Key Macropad

A compact, 3-key programmable macropad designed using the Seeed Studio XIAO RP2040 microcontroller and Cherry MX compatible switches.

## Features
- **Microcontroller:** Seeed Studio XIAO RP2040 (dual-core ARM Cortex M0+).
- **Keys:** 3 Cherry MX compatible mechanical switches.
- **Design:** Custom PCB designed in KiCad and enclosure designed in Fusion 360.

## Project Structure
- `macropad/`: Contains the KiCad project files (schematic and PCB layout).
- `macropad.f3d`: Fusion 360 design file for the macropad case or plate.
- `SCR-*.png`: Screenshots of the project (PCB layout and 3D design).

## Hardware
### Components
- 1x Seeed Studio XIAO RP2040
- 3x Cherry MX (or compatible) Mechanical Switches
- Custom PCB

### Schematic & PCB
The hardware design is located in the `macropad/` directory. 
- `macropad.kicad_sch`: Schematic design.
- `macropad.kicad_pcb`: PCB layout design.

## Case / Mechanicals
The mechanical design was created in Fusion 360. The `macropad.f3d` file can be opened in Fusion 360 to modify the case or export STL files for 3D printing.

## Firmware
This macropad can be used with various firmware options:
- [KMK Firmware](https://github.com/KMKfw/kmk_firmware) (CircuitPython)
- [QMK Firmware](https://qmk.fm/)
- Custom Arduino code using the RP2040 core.

## Media
![PCB Layout](SCR-20260606-octj.png)
*Typical PCB or 3D view of the project.*

---
Designed with ❤️ by [Your Name/GitHub Handle]
