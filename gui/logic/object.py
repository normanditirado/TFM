import enum
class ObjectDetected:

    def __init__(self, label, topLeftX, topLeftY, bottomRightX, bottomRightY, confidence):
        self.label = label
        self.topLeftX = topLeftX
        self.topLeftY = topLeftY
        self.bottomRightX = bottomRightX
        self.bottomRightY = bottomRightY
        self.confidence = confidence

    def getLabel(self):
        return self.label

    def getTopLeftX(self):
        return self.topLeftX
    
    def getTopLeftY(self):
        return self.topLeftY

    def getBottomRightX(self):
        return self.bottomRightX
    
    def getBottomRightY(self):
        return self.bottomRightY
    
    def setLabel(self, label):
        self.label = label
    
    def setTopLeftX(self, topLeftX):
        self.topLeftX = topLeftX
    
    def setTopLeftY(self, topLeftY):
        self.topLeftY = topLeftY
    
    def setBottomRightX(self, bottomRightX):
        self.bottomRightX = bottomRightX
    
    def setBottomRightY(self, bottomRightY):
        self.bottomRightY = bottomRightY
    
    def getCenterX(self):
        centerX = (self.getTopLeftX() + self.getBottomRightX())/2
        return centerX
    
    def getCenterY(self):
        centerY = (self.getTopLeftY() + self.getBottomRightY())/2
        return centerY
    
    def getConfidence(self):
        return self.confidence
    
    def setConfidence(self, confidence):
        self.confidence = confidence


class Object(enum.Enum):
    person = 1
    chair = 2
    sofa = 3
    book = 4
    laptop = 5
    tvmonitor = 6
    keyboard = 7
    
