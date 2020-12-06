Histogram_Operations



This project aims to Implement histogram equalization and histogram specification on a given image and compare the outputs (mean of input image, minimum and maximum input gray levels, mean of Histogram Equalized image, mean of image enhanced by Histogram Specification). Display the input image along with the two enhanced images for visual comparison


INSTALLATION INSTRUCTIONS
The application folder contains a bunch of files from which the Histogram_Operations.exe file is to be run. This will open the Application WIndow as well as the Command Prompt Window.
Note: Do not separate the files at different locations.


OPERATING INSTRUCTIONS

The file once executed allows you to choose an image by opening a window.
User should do following:
Window number 1:
Click on choose file button - user will be prompted to choose a photo/image from any location by navigating to particular image
Click on Exit - Terminates the programme and closes the window.

Once the user has chose the image, window 1 will collapse and the programme executes, this will take a while 

Window number 2:
Once the file has been completely executed, window 2 opens which is the main window of the programme here user can do following things:

Window consists an image display to show the chosen image in the grayscale view

Histogram equalization button - Clicking on this button gives the output image after histogram equalization is executed.

Histogram Specification button - Clicking on this button gives the output image after histogram specification is carried out
Note: This should be run only after choosing the image for reference.

Choose Reference Image - Clicking on this, a new window will be opened, user will be prompted to choose a photo/image from any location by navigating to particular image.This button allows user to choose a image required as reference for the histogram specification. First user need to choose source image again and then the reference image. Once chosen the process will execute which will take a while


Histogram (input image) - Clicking on this button gives a new window which shows a plot of intensity versus frequency of the Input image chosen, the plot can be zoomed in and zoomed out, graph can be saved, also the settings of view can be changed in this window.  

Histogram(Reference image) - Clicking on this button gives a new window which shows a plot of intensity versus frequency of the Reference image chosen, the plot can be zoomed in and zoomed out, graph can be saved, also the settings of view can be changed in this window. 

Histogram (Equalised image) - Clicking on this button gives a new window which shows a plot of intensity versus frequency of the Equalised Output image, the plot can be zoomed in and zoomed out, graph can be saved, also the settings of view can be changed in this window.

Histogram (Specified image) - Clicking on this button gives a new window which shows a plot of intensity versus frequency of the Specified Output image chosen, the plot can be zoomed in and zoomed out, graph can be saved, also the settings of view can be changed in this window.

Parameters - Clicking on this button gives a new window which shows the Maximum Intensity(DN) value, Minimum Intensity(DN) value, Mean Intensity(DN) value of Input Image, Reference Image,  Equalised Output image and Specified Output Image


Save File - The current output which may be of Histogram Equalization or Specification can be saved at any desired location.

Exit - This will close the window and exit the programme


FILE MANIFEST (list of files included)

The Script file uses Python language 
Note: The programme code is completely based on preliminary mathematical operations and basic python programming functions, Following packages are used only for File handling and output purposes.
Packages Included:
Tkinter - For creating the Graphical user interface.
Opencv - To handle image files
Matplotlib.pyplot - To plot the histogram of the output values
Os - To interact with the operating system
NumPy - To handle arrays


COPYRIGHT AND LICENSING INFORMATION

The operator of this Programme/Application (“we” or “us”) offers access to the Programme or any file related to programme conditioned on your acceptance without modification of the terms, conditions and notices contained in “Terms of Laws”  and the Privacy Policy. In addition, particular features and activities offered as part of the application may also be subject to additional terms specified in connection with such features, applications and activities, all of which are incorporated herein by reference.

CONTACT INFORMATION FOR THE DISTRIBUTOR OR PROGRAMMER

Swapnil Joshi : MTech Geoinformatics and Natural Resources, CSRE, IIT Bombay.
Email: 203310005@iitb.ac.in
Vishvesh Kodihal : MTech Geoinformatics and Natural Resources, CSRE, IIT Bombay. 
Email: vkodihal@ gmail.com
	203310013@iitb.ac.in
	
CREDITS AND ACKNOWLEDGMENTS

We would like to express our special thanks of gratitude to our  Professor Dr. B. Krishna Mohan,CSRE, IIT Bombay,INDIA who gave me the golden opportunity to do this wonderful project on the topic Programme on Histogram Equalization and specification, which also helped me in doing a lot of Research and i came to know about so many new things I am really thankful.
Project Assignment submission under:
Principles of Satellite Image Processing (GNR607)

