# Soft Robot Interface

Run `main.py`.
The serial port over which to communicate with the Arduino must be specified in `serialcom.py`.

### Data Transfer
Data transfer is by serial. Python expects the Arduino to return a JSON-like serial output:

```
{
    "numSeg": (number of segments),
    "numCham": (number of chambers),
    "boardTime": (board time in milliseconds),
    "DoF": (0, 1 or 2 to control movement of robot base)
    "setP": (set pressure array),
    "chamPress": (chamber pressure array),
    "status": (array of status for each chamber),
    "PWM": (PWM value of each pump),
    "valveState": (status of valves of each pump)
}
```

Python returns an array to the arduino:

```
(setP array), N
```

where setP array is the new set pressures, and N is an integer to control the extra DoF (0 = no movement, 1 = up, 2 = down).