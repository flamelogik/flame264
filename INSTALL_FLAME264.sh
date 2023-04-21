#!/bin/bash

# Clone the repository
git clone https://github.com/flamelogik/flame264.git

# Copy the Python file to /opt/Autodesk/shared/python
cp flame264/*.py /opt/Autodesk/shared/python

# Copy the XML files to /opt/Autodesk/shared/export/presets/movie_file/
cp flame264/*.xml /opt/Autodesk/shared/export/presets/movie_file/

# Copy the cdxprof files to /opt/Autodesk/mediaconverter/2023.2/profiles/QuickTime/video/H264/
cp flame264/*.cdxprof /opt/Autodesk/mediaconverter/2023.2/profiles/QuickTime/video/H264/
