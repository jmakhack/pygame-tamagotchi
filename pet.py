#class for all pets
class Pet():
    def __init__(self, image):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.step = 1
        self.image = image

    #set x and y position for character
    def setPosition(self, x, y):
        self.x = x
        self.y = y

    #get x position of character
    def getX(self):
        return self.x

    #get y position of character
    def getY(self):
        return self.y

    #get x and y position of character
    def getPosition(self):
        return self.x, self.y

    #set width of image
    def setWidth(self, width):
        self.width = width

    #set height of image
    def setHeight(self, height):
        self.height = height

    #get width of image
    def getWidth(self):
        return self.width

    #get height of image
    def getHeight(self):
        return self.height

    #set how many pixels character moves with each call to a move method
    def setStep(self, step):
        self.step = step

    #set image of pet on screen
    def setImage(self, image):
        self.image = image

    #set animation to be played when idle and walking left
    def setIdleLAnim(self, frames, *images):
        self.idleLFrames = frames
        self.idleLCurrFrame = 0
        self.idleL = list(images)

    #play animation to be played when idle and walking left
    def moveIdleL(self):
        self.idleLCurrFrame += 1
        if self.idleLCurrFrame > self.idleLFrames:
            self.idleL.append(self.idleL.pop(0))
            self.idleLCurrFrame = 0
        self.image = self.idleL[0]
        self.setPosition(self.x - self.step, self.y)

    #set animation to be played when idle and walking left
    def setIdleRAnim(self, frames, *images):
        self.idleRFrames = frames
        self.idleRCurrFrame = 0
        self.idleR = list(images)

    #play animation to be played when idle and walking left
    def moveIdleR(self):
        self.idleRCurrFrame += 1
        if self.idleRCurrFrame > self.idleRFrames:
            self.idleR.append(self.idleR.pop(0))
            self.idleRCurrFrame = 0
        self.image = self.idleR[0]
        self.setPosition(self.x + self.step, self.y)

    #get image to display on screen
    def getImage(self):
        return self.image