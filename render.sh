#!/bin/sh
sudo ffmpeg -r 16 -s 1920x1080 -i frames/image%04d.png -vcodec libx264 -crf 25 -pix_fmt yuv420p videos/greenhouse.mp4
