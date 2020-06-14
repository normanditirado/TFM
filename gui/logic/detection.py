from object import ObjectDetected, Object
import math
import cv2
from activity import Activity
from image import Image
import json
from collections import namedtuple
from json import JSONEncoder
# Function to get the distance between two objects
def distanceBetweenObjects(object1, object2):
    xM1 = object1.getCenterX()
    xM2 = object2.getCenterX()
    yM1 = object1.getCenterY()
    yM2 = object2.getCenterY()
    sumX = pow((xM1 - xM2), 2)
    sumY = pow((yM1 - yM2), 2)
    distance = math.sqrt((sumX + sumY))
    return distance

def loadObjectsFromJSON():
    return 0

def imageDecoder(imageDict):
    return namedtuple('X', imageDict.keys())(*imageDict.values())


# Parses the processed information from Yolo to an Image
def parseProcessedImage(pathToImage):
    image = detectImageSize(pathToImage)
    pos = pathToImage.rfind(".")
    print('pos: ' + str(pos))
    pathToJSON = pathToImage[0:pos + 1]
    pathToJSON += "json"
    objects = detectObjectsFromJSON(pathToJSON)
    image.setObjects(objects)
    print('It works')
    return image

# Detects the size of the image (height and width)
def detectImageSize(pathToImage):
    image = cv2.imread(pathToImage)
    height, width = image.shape[0:2]
    print('Height:' + str(height))
    print('Width:' + str(width))
    objects = []
    imageDetected = Image(height, width, objects)
    return imageDetected

# Parses Json of objects detected in an image to a list of ObjectDetected
def detectObjectsFromJSON(jsonOfImageProcessed):
    inputFile = open(jsonOfImageProcessed)
    jsonArray = json.load(inputFile)
    objectsList = []
    for item in jsonArray:
        objectDetected = ObjectDetected(item['label'], item['topleft']['x'], item['topleft']['y'], item['bottomright']['x'], item['bottomright']['y'], item['confidence'])
        objectsList.append(objectDetected)
    return objectsList

def detectActivitiesFromJSON():
    return 0
    
def getMetabolicRate(activity):
    if (activity == Activity.reading_seated or activity == Activity.writing):
        return 1
    if (activity == Activity.typing):
        return 1.1
    if (activity == Activity.archive_seated):
        return 1.2
    if (activity == Activity.archive):
        return 1.4
    if (activity == Activity.walking):
        return 1.7
    if (activity == Activity.packing):
        return 2.1
    return 0 

# Returns a list when the first item is the height and the second item is the width
def getHeightAndWidthFromRectangle(upperLeftX, upperLeftY, bottomRightX, bottomRightY):
    height = abs(bottomRightY - upperLeftY)
    width = abs(bottomRightX - upperLeftX)
    result = [height, width]
    return result

# Prints an image processed by the function parseProcessedImage
def printImage(imageProcessed):
    print('Height:' + str(imageProcessed.getHeight()))
    print('Width:' + str(imageProcessed.getWidth()))
    print('Cantidad de objetos:' + str(len(imageProcessed.getObjects())))
    for currentObject in imageProcessed.getObjects():
        print('<<')
        print('Label: ' + currentObject.getLabel() + ' Confidence: ' + str(currentObject.getConfidence()) +' Topleft>> X: ' + str(currentObject.getTopLeftX()) + ' Y: ' + str(currentObject.getTopLeftY()) + ' BottomRight X: ' + str(currentObject.getBottomRightX()) + ' Y: ' + str(currentObject.getBottomRightY()) + ' CenterX: ' + str(currentObject.getCenterX()) + ' CenterY: ' + str(currentObject.getCenterY()))





# testing
# p1 = ObjectDetected('Person', 5, 2, 5, 2, 7)
# p2 = ObjectDetected('PC', 3, 1, 3, 1, 8)
# print(distanceBetweenObjects(p1, p2))
# print(getMetabolicRate(Activity.archive))
# pathToJson = 'C:\\Users\\Normandi\\Desktop\\sample_person.json'
pathToImage ='C:\\Users\\Normandi\\Desktop\\sample_person.jpg'
imageProcessed = parseProcessedImage(pathToImage)
printImage(imageProcessed)
