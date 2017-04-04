"""_skeleton.py
Camera class with the skeleton functions. Important to keep track of the methods that are
exposed to the View. Ideally copy/paste and start developing from here.
"""

class cameraBase():
    MODE_CONTINUOUS = 1
    MODE_SINGLE_SHOT = 0
    def __init__(self, camera):
        self.camera = camera
        self.running = False
        self.maxWidth = 0
        self.maxHeight = 0

    def initializeCamera(self):
        """Initializes the camera.
        """
        self.maxWidth = self.GetCCDWidth()
        self.maxHeight = self.GetCCDHeight()
        return True

    def triggerCamera(self):
        """Triggers the camera.
        """
        raise NotImplementedError

    def setAcquisitionMode(self, mode):
        """ Set the readout mode of the camera: Single or continuous.
        Parameters
        ==========
        mode : int
            One of self.MODE_CONTINUOUS, self.MODE_SINGLE_SHOT
        """
        self.mode = mode

    def getAcquisitionMode(self):
        """Returns the acquisition mode, either continuous or single shot.
        """
        return self.mode

    def acquisitionReady(self):
        """Checks if the acquisition in the camera is over.
        """
        raise NotImplementedError

    def setExposure(self,exposure):
        """Sets the exposure of the camera.
        """
        raise NotImplementedError

    def getExposure(self):
        """Gets the exposure time of the camera.
        """
        raise NotImplementedError

    def readCamera(self):
        """Reads the camera
        """
        raise NotImplementedError

    def setROI(self,X,Y):
        """Sets up the ROI. Not all cameras are 0-indexed, so this is an important
        place to define the proper ROI.
        X -- array type with the coordinates for the ROI X[0], X[1]
        Y -- array type with the coordinates for the ROI Y[0], Y[1]
        """
        raise NotImplementedError

    def clearROI(self):
        """Clears the ROI from the camera."""
        self.setROI(self.maxWidth, self.maxHeight)

    def getSize(self):
        """Returns the size in pixels of the image being acquired. This is useful for checking the ROI settings.
        """
        raise NotImplementedError

    def getSerialNumber(self):
        """Returns the serial number of the camera.
        """
        raise NotImplementedError

    def GetCCDWidth(self):
        """
        Returns
        -------
        The CCD width in pixels
        """
        raise NotImplementedError

    def GetCCDHeight(self):
        """
        Returns
        -------
        The CCD height in pixels
        """
        raise NotImplementedError

    def stopAcq(self):
        """Stops the acquisition without closing the connection to the camera."""
        raise NotImplementedError

    def setBinning(self,xbin,ybin):
        """
        Sets the binning of the camera if supported. Has to check if binning in X/Y can be different or not, etc.
        
        :param xbin: 
        :param ybin: 
        :return: 
        """
        raise NotImplementedError

    def stopCamera(self):
        """Stops the acquisition and closes the connection with the camera.
        """
        try:
            #Closing the camera
            raise NotImplementedError
        except:
            #Camera failed to close
            raise NotImplementedError