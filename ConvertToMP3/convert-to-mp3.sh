#!/bin/bash
mkdir ../Music/FromVideo

# todo: make paths entirely configurable up here
# todo: make threadcount configurable up here
# fixme: will throw error if there happens to be no videos of a given format
for i in *.{mp4,mkv,webm} ; do 
    #echo $i
	# remove the .extension (so we can append .mp3 later) 
	name=`echo $i | sed 's/\.[^.]*$//'` 
	echo $name
	# only convert if the file does not exist yet
	if [ ! -f ../Music/FromVideo/"$name".mp3 ]; then
		ffmpeg -i "$i" -acodec libmp3lame -threads 2 ../Music/FromVideo/"$name".mp3
	fi
done
