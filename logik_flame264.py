def pre_export_asset(info, userData, *args, **kwargs):
	# Save the resolved (tokens expanded) name of the file that was exported
	# so we can use it later in post_export_sequence which doesn't otherwise
	# get this information
	userData['export_file'] = info['resolvedPath']

def pre_export(info, userData, *args, **kwargs):
	import os
	# Save the export preset name used so we can look at it later
	# in post_export_sequence which doesn't otherwise get this information
	userData['export_preset'] = os.path.basename( info['presetPath'] )

def post_export_sequence(info, userData, *args, **kwargs):
	# Configure a list of preset names to intercept, can use simple * wildcards
	# (and ? for single characters)
	remux_presets = ['logik_flame*']

	import fnmatch, os, subprocess, time

	#print( "post_export_sequence: userData is" )
	#print( userData )

	for cur_preset in remux_presets:
		if( fnmatch.fnmatch( userData['export_preset'], cur_preset ) == True ):
			remux_source = os.path.join( info['destinationPath'], userData['export_file'] )
			remux_dest   = os.path.join( info['destinationPath'], os.path.splitext( userData['export_file'] )[0] + ".mp4" )
			print( "TO REMUX filename is " + remux_source )
			print( "TO REMUX destination is " + remux_dest )

			ffmpeg_cmd = ['/bin/ffmpeg', '-y', '-i', remux_source, '-codec:v', 'copy', '-codec:a', 'aac', '-ab', '320k', '-mov_gamma', '2.4', '-movflags', 'write_colr', '-color_trc', 'unspecified', '-color_primaries', 'bt709', '-colorspace', 'bt709', remux_dest]
			#ffmpeg_cmd = ['/home/bobm/bin/ffmpeg', '-y', '-i', remux_source, '-codec:v', 'copy', '-codec:a', 'copy', remux_dest]
			subprocess.run(ffmpeg_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)

			# Remove the source file if the destination file got created and isn't empty
			if( os.path.isfile(remux_dest) ):
				if( os.path.getsize(remux_dest) > 0 ):
					os.remove( remux_source )
