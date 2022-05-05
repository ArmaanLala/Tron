# Tron Controller 

## Retrofuturistic Hardware Project VIP Project

This project uses an RP2040 chip to take the Tron Arcade Cabinet Controller information and turn the signals to the appropriate game controller inputs.

## Known Issues
- After large rotations of the knob, it might register a single press in the opposite direction. During my testing, I realized that this does not cause any noticeable issues and is an inherent problem as I am sampling the values after they have been interpreted and not directly from the source.
- Pushing the joystick to the right causes some issues. On my particular controller, the metal tabs associated with the right button are bent less than the others, which occasionally leads to issues with the tabs making contact and registering the right press

### Setup
1) First, you must flash the pi pico using the included CircuitPython.uf2 file.
2) Next, you must copy the contents from the `Pico Root` folder onto the microcontroller.
3) Using the diagrams below, wire the pico and controller together
4) Any wires that are listed as ground can be placed onto any ground pin on the pico
5) Everything should be all set up!

### Fritzing Diagram
Below is a diagram of the Pico. This diagram is for actually connecting the Molex wires to the pico.

![Pico_schem.png](Pico_schem.png)


### Wiring Diagrams
These diagrams are from previous semesters and were drawn by other students. These are used to label the wires coming out of the Molex connectors.

![Tron1.png](Tron1.png)
![Tron2.png](Tron2.png)


<!-- Mad Planets -->


I had a lot of fun working on this project and if you notice any issues please let me know!