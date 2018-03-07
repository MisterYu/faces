## Features:

face detection - yup

face recognition - sorta. Currently only trained to recognize Beyonce.

face greening - incomplete. Lazy implementation only paints entire square green. Needs something to do background subtraction to isolate face.

eye detection and morse code from blinks - eyes are detected and found but morse code inconsistent

## Installation:

tested on Ubuntu 16.04

checkout: `git clone git@github.com:MisterYu:faces.git`

go into checkout directory: `cd faces`

create virtual environment: `python3 -m venv env_face`

activate environment: `. env_face/bin/activate`

install requisite modules: `pip install -r requirements.txt`

install faces: `python3 setup.py`

## Usage:

activate environment: `. env_face/bin/activate`

`python3 faces.py` to bring up the gui in `faces` directory, i.e. `cd faces`. Paths hard coded relative (sorry).

everything is off by default

click "start" to have camera start collecting data

click "stop" to have camera stop collecting data

click "Face Detect" to start face detection. "Eyes?", "Hulk out", and "Beyonce Recognition" won't work without "Face Detect"

click "Eyes?" to start eye detection and Morse code deciphering from blinks

click "Hulk out" to turn box with face in green; would be better if only face greened

click "Beyonce Recognition" to kick up Queen B recognition. Adjust "confidence" levels

## Notes:

test code - NOPE. need more time to write all the test code. TDD fail.

C++ inclusion - NOPE. all time burned on feature implementation. Ideally use C++11 to thread face recognition on more than Queen B.

In order for modifications to show up, the modified ui file requires the following processing: `pyuic5 faces_gui.ui -o faces_gui.py`
