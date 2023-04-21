# Flame264

Flame264 is a tool that allows artists to export native H.264 files from Autodesk Flame. This project is forked for Logik and is designed as a learning experience.  Be nice.  I know its rough.

# Installation

To install Flame264, clone the repository and run the INSTALL_FLAME264 script:

git clone https://github.com/flamelogik/flame264.git
cd flame264
chmod +x INSTALL_FLAME264
sudo ./INSTALL_FLAME264

Please note that the current version of the INSTALL_FLAME264 script has an absolute link and only installs for Flame 2023.2. You will need to modify the script to work with different versions of Flame, or help me evolve the the .sh script to include all directories within this directory.

/opt/Autodesk/mediaconverter/<INSERT VERSIONS OF FLAME HERE>/profiles/Quicktime/video/H264/

# Credits

This project was inspired by the Logik Forum thread "MP4 Export" (https://forum.logik.tv/t/mp4-export/6969/3) and was developed with guidance and support from Bob Mable and Jeff Kyle.

# Known Limitations

The INSTALL_FLAME264 script has an absolute link and will only work on Flame 2023.2 due to an absolute link of the cdxproj files.

This project is designed as a learning experience and may not be suitable for production use.

The video codec portion passes through; however, the bug we could not solve is that we must re-encode the audio. When we didn’t re-encode the audio with ffmpeg, we found the audio would go out of sync. This is the part of the workflow that if someone else can figure out why and how to avoid this, I would love to not have to re-encode the audio. But for now, this is a necessary evil that I have come to terms with, and I don’t think it’s all that bad.

The way this works is by exporting an .mov H264 from Flame from a carefully configured “Profile” file that makes a nicely compressed .mov H264 via a .cdxprof file. I say nicely because the default profiles that come shipped with Flame I found do not create H264s that are both “main” and “cbr” which is where I would lean if I were making these files using other means (Media Encoder for example). I made 3 for 3 different commonly used bitrates. They are provided as cdxprof files.

The INSTALL_FLAME264.sh script will copy them to this location:

/opt/Autodesk/mediaconverter/2023.2/profiles/Quicktime/video/H264/

Then, the .sh will copy the Export Preset .xml files to this location:

/opt/Autodesk/shared/export/presets/movie_file/

These .xml presets were created in Flame and use the above profiles to create a .mov h264. You can create your own, you just have to ensure you adjust the python script we’ll be getting to in a moment.

Now you load the flameh264.py to the python location:

/opt/Autodesk/shared/python

From Jeff Kyle:
This is the brilliant work of Bob Maple who did all of the heavy lifting on python to make this a reality. This hook looks to see if you have used the above mentioned .xml Export Presets, and if so, it uses ffmpeg to re-encode the .mov h264 into an .mp4 h264 and then deletes the .mov to clean things up. I toyed with the idea of circumventing ffmpeg and simply renaming the .mov to .mp4, but you run several metadata related risks if your delivery requires .mp4’s. The video codec portion passes through; however, the bug we could not solve is that we must re-encode the audio. When we didn’t re-encode the audio with ffmpeg, we found the audio would go out of sync. This is the part of the workflow that if someone else can figure out why and how to avoid this, I would love to not have to re-encode the audio. But for now, this is a necessary evil that I have come to terms with, and I don’t think it’s all that bad.

If you have any questions or feedback, please feel free to contact me. Thanks for checking out Flame264!

te
