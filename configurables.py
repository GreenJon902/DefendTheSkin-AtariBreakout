prePlayToPlayDelay = 0.5
fadeLength = 0.5
bgBloodColor = 0.7, 0, 0
bgSkinColor1 = 1, 0.70196078431, 0
bgSkinColor2 = 0.94509803921, 0.66274509803, 0
bgSkinBottom = 0.7
bgSkinTop = 0.9
bgFontName = "Resources/minecraft.ttf"
bgExplainerTextY = 0.7
bgExplainerTextWidth = 0.9
atariGridShape = 6, 5
atariColorGrid = [
    [0.7, 0.0, 0.0],
    [1.0, 0.5, 0.0],
    [1.0, 1.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0]
]
atariHitColorChange = 0.3
atariHitRegenTime = 5
atariIdToPosGrid = {}
n = 0
for x in range(atariGridShape[0]):
    for y in range(atariGridShape[1]):
        atariIdToPosGrid[n] = [x, y]

        n += 1
del n
atariIdToPosGridInverted = {}
n = 0
for y in range(atariGridShape[1]):
    for x in range(atariGridShape[0]):
        atariIdToPosGridInverted[n] = [x, y]

        n += 1
del n
posToAtariIdGrid = {}
n = 0
for x in range(atariGridShape[0]):
    posToAtariIdGrid[x] = {}
    for y in range(atariGridShape[1]):
        posToAtariIdGrid[x][y] = n

        n += 1
del n
playButtonPos = {"x": 0, "y": bgSkinBottom}
playButtonSize = 1, bgSkinTop - bgSkinBottom
atariGridPos = playButtonPos
atariGridSize = playButtonSize
brickOpeningDelay = 0
brickFallTime = 0.1
brickFallTransition = "in_out_cubic"
ballColor = 1, 1, 1
ballY = 0.3
ballSize = 0.05
ballSpeedUp = 1.05
ballStartSpeed = 2
racketY = 0.1
racketColor = 1, 1, 1
racketSize = 0.2, 0.05
racketMoveAmount = 0.01
racketClickAccuracyTop = 0.05
racketClickAccuracyBottom = 0.02
racketMoveTime = 0.1
racketWaitTime = 0.1
racketMoveTransition = "in_out_quad"
bigBrickWidth = 0.9
bigBrickHeight = 0.06
bigBrickHoleColorChange = 0.5
bigBrickRacketFitAccuracy = 0.05
bigBrickMoveTime = 0.5
bigBrickFlashTime = 3
bigBrickFlashTransition = "out_expo"
heartSize = 0.1
healthDistance = 0.01
healthGrowSize = 1.5
healthLeaveTime = 0.5
bodyRadius = 0.02
bodyColors = {"anti": (0.19999999962, 1, 1), "antianti": (0.78039215538, 0.91764705708, 0.2745098034)}
bodyMoveSpeed = 5
antiBodyDirectionChangeMax = 50
antiBodyDirectionChangeMax2 = 100
antiBodyCreationAmount = 3
antiBodyCreationTime = 10
antiantiBodyAmount = 10
furtherReadingScreenText = ""
howToPlayScreenText = "How To Play? \n \n The aim of the game is to make a path through the cells using the virus " \
                      "which you bounce with your racket. There will also be blue antibodies flying around and if " \
                      "they touch the racket then you loose a life, but don't worry both the virus and some special " \
                      "balls will destroy anti bodies on impact. These special balls explode from cells that you " \
                      "destroy. To destroy a cell you simply have to hit it with the virus and then slide the racket " \
                      "into the zoomed in part of the cell that will appear at the bottom of your screen."

howIsItRelatedToTheSkinImmuneSystemScreenText = ""
textPadding = 0.01
buttonColorChange = 0.7, 0.7, 0.7, 0
