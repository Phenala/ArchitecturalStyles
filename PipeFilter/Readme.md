Pipe and Filter Architecture
------------------------------------------------------------

Image Postprocessing

Test file is main.py

The project is an application that uses filter modules to tweak color of a given image in
sequence. There are a few filter classes available, and creating a filter only requires
extending the ImageFilter class and overriding the filterPixel method.

	pipe = Pipe Object

	pipe.addFilter(Filter object) - add filters to the pipe

	pipe.run(image Object) - run the image through the pipe to apply the effects

In the demo provided, the image (ktna.png) is filtered through an object pipe that the GrayScale, 
BlueTint, Vivify, Contrast and Brighten filters and displayed.


		GrayScale ────► BlueTint ────► Vivify ────► Contrast ────► Brighten

