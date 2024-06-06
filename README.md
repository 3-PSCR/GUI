# Soft Robot Interface

This repo contains a GUI created to control a [pneumatic soft continuum robot](3-pscr.github.io). It interfaces with an Arduino over Serial. The serial port used must be set on line 6 of `serialcom.py`, and the program is run from main.py.

The UI is created in Tkinter, and threading is used to ensure that reading data from the Arduino's Serial buffer does not interfere with the responsivity of the UI.

### Data Transfer
Data transfer is by serial. Python expects the Arduino to return a JSON-like serial output:

```
{
    "numSeg": (number of segments),
    "numCham": (number of chambers),
    "boardTime": (board time in milliseconds),
    "DoF": (0, 1, 2, 3 or 4 to control movement of robot base)
    "setP": (set pressure array),
    "chamPress": (chamber pressure array),
    "status": (array of status for each chamber),
    "PWM": (PWM value of each pump),
    "valveState": (status of valves of each pump)
}
```

Python returns an array to the arduino:

```
[(setP array), N]
```

where setP array is the new set pressures, and N is an integer to control the extra DoF (0 = no movement, 1 = up, 2 = down).