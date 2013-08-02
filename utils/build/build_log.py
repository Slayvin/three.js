import subprocess
import argparse
import re
import sys

def main(argv=None):
	parser = argparse.ArgumentParser()
	parser.add_argument('--default', action='store_true', default=False)
	parser.add_argument('--min', action='store_true', default=False)
	parser.add_argument('--extras', action='store_true', default=False)
	args = parser.parse_args()

	if args.default is True:
		print ' * Building three.js',
		output, error = subprocess.Popen("build.py --include common --include extras --output ../../build/three.js", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()
		printError(output, error)

	if args.min is True:
		print ' * Building three.min.js',
		output, error = subprocess.Popen("build.py --include common --include extras --minify --output ../../build/three.min.js", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()
		printError(output, error)

	if args.extras is True:
		print ' * Building three-canvas.min.js',
		output, error = subprocess.Popen("build.py --include canvas --minify --output ../../build/three-canvas.min.js", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()
		printError(output, error)
		
		print ' * Building three-css3d.min.js',
		output, error = subprocess.Popen("build.py --include css3d --minify --output ../../build/three-css3d.min.js", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()
		printError(output, error)
		
		print ' * Building three-webgl.min.js',
		output, error = subprocess.Popen("build.py --include webgl --minify --output ../../build/three-webgl.min.js", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()
		printError(output, error)
		
		print ' * Building three-extras.min.js',
		output, error = subprocess.Popen("build.py --include extras --externs externs/extras.js --minify --output ../../build/three-extras.min.js", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()
		printError(output, error)
		
		print ' * Building three-math.js',
		output, error = subprocess.Popen("build.py --include math --output ../../build/three-math.js", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()
		printError(output, error)
		
		print ' * Building three-math.min.js',
		output, error = subprocess.Popen("build.py --include math --output ../../build/three-math.min.js", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()
		printError(output, error)

def printError(outputMsg, errorMsg):
	sys.stderr.write(outputMsg)
	errors = re.search( '^ *(.+ error.*).$', errorMsg, re.M)
	if errors:
		print ': ', errors.group()
		sys.stderr.write(errorMsg)
	else:
		print ': OK'


if __name__ == "__main__":
	main()