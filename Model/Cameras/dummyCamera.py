""" dummyCamera.py
Dummy camera class for testing GUI and other functionalities. Based on the skeleton.
"""
import numpy as np
class camera():
    MODE_CONTINUOUS = 1
    MODE_SINGLE_SHOT = 0
    def __init__(self,camera):
        self.camera = camera
        self.running = False
        self.xsize = 2048
        self.ysize = 2048
        self.maxX = 2048
        self.maxY = 2048

    def initializeCamera(self):
        """Initializes the camera.
        """
        print('Initializing camera')
        return True

    def triggerCamera(self):
        """Triggers the camera.
        """
        return True

    def setAcquisitionMode(self, mode):
        """ Set the readout mode of the camera: Single or continuous.
        Parameters
        ==========
        mode : int
            One of self.MODE_CONTINUOUS, self.MODE_SINGLE_SHOT
        """
        print('Setting acquisition mode')
        return self.getAcquisitionMode()

    def getAcquisitionMode(self):
        """Returns the acquisition mode, either continuous or single shot.
        """
        return self.MODE_CONTINUOUS

    def acquisitionReady(self):
        """Checks if the acquisition in the camera is over.
        """
        return True

    def setExposure(self,exposure):
        """Sets the exposure of the camera.
        """
        self.exposure = exposure
        return exposure

    def getExposure(self):
        """Gets the exposure time of the camera.
        """
        return self.exposure

    def readCamera(self):
        """Reads the camera
        """
        X,Y = self.getSize()
        sample = np.random.normal(size=(X,Y))
        img = np.reshape(sample,(X,Y))
        return img

    def setROI(self,X,Y):
        """Sets up the ROI. Not all cameras are 0-indexed, so this is an important
        place to define the proper ROI.
        X -- array type with the coordinates for the ROI X[0], X[1]
        Y -- array type with the coordinates for the ROI Y[0], Y[1]
        """
        self.xsize = abs(X[1]-X[0])
        self.ysize = abs(Y[1]-Y[0])

        return self.getSize()

    def getSize(self):
        """Returns the size in pixels of the image being acquired. This is useful for checking the ROI settings.
        """

        return self.xsize,self.ysize

    def getSerialNumber(self):
        """Returns the serial number of the camera.
        """
        return "Serial Number"

    def GetCCDWidth(self):
        """
        Returns
        -------
        The CCD width in pixels

        """
        return self.maxX


    def GetCCDHeight(self):
        """
        Returns
        -------
        The CCD height in pixels

        """
        return self.maxY


    def stopCamera(self):
        """Stops the acquisition and closes the connection with the camera.
        """
        try:
            #Closing the camera
            return True
        except:
            #Camera failed to close
            return False