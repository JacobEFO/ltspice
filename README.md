# ltspice

Disclaimer: Linear Technology is not in any way affiliated with this repository or the implemented functions.

The functions presented are intended to read an LTspice exported version of an AC analysis. The formatting from LTspice makes it challenging just reading with a regular function. By use of this script you will be able to easily compare calculations and simulations in the same window.

To use this import ltspice and use the function "ltspiceReadAC(filename)" which will return three variables: frequency, magnitude and phase (in degree).


## Example of the ltspice repository used

The following example shows a calculated and simulated transfer function from a simple first order low-pass RC filter.

<p align="center">
  <img src="figures/magnitude.png" alt="Magnitude"/>
</p>

<p align="center">
  <img src="figures/phase.png" alt="Magnitude"/>
</p>