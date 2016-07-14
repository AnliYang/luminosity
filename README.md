# Luminosity (aka Brightly aka Funset)
[![Build Status](https://travis-ci.org/AnliYang/luminosity.svg?branch=master)](https://travis-ci.org/AnliYang/luminosity)

## Install dependencies
Install Pillow, the friendly PIL (Python Imaging Library) fork.

`pip install -r requirements.txt`

Note that Pillow depends other external libraries as well. For more information on installing Pillow, check out their docs [here](http://pillow.readthedocs.io/en/3.2.x/installation.html).

## See which of your pictures is the brightest
To run on the example fixture png files:
`python luminosity.py ./fixtures/*.png`

"Brightness" is based on relative luminance, as described [here](https://en.wikipedia.org/wiki/Relative_luminance).
