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
healthDistance = 0.01
heartSize = 0.1 - (healthDistance * 2)
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
furtherReadingScreenText = "Further Reading \n \n Source 1: https://dermnetnz.org/topics/skin-immune-system/ By Dr " \
                           "Yuliya Velykoredko,\n " \
                           "Dermatology Resident, and Dr Michal Bohdanowicz, Dermatology Resident, Source 2: " \
                           "https://kidshealth.org/en/teens/immune.html \n \n Definitions; T cell: plays a key role in " \
                           "detecting a virus Antigen: a foreign substance B cells: B cells produce antibodies. " \
                           "Complement: Plasma proteins that fight viruses. \n \n The immune system or Skin associated " \
                           "lymphoid tissue or SALT has an external physical barrier preventing infection and toxins " \
                           "from entering externally. A T cell detects a virus or antigen immediately. B cells " \
                           "produce antibodies which bind itself to a virus, by doing this it prevents infections. " \
                           "Antibodies also stay in the body after fighting a virus, It almost keeps a database of " \
                           "what to do when the virus attacks again, this why your unlikely to get the same virus " \
                           "twice. We can see this in the covid19 herd immunity ( adaptive immunity). plan. This is " \
                           "also why the antibody test works the way it does. Antibodies can also activate " \
                           "complement, which can help kill the viruses. One of the most important things we have in " \
                           "our time, is vaccines. Vaccines introduce us to a weaker version of a virus. Once the " \
                           "immune system acts, antibodies remember what to do if the body is introduced to that " \
                           "virus again." \
                           "  \n \n \n Double tap to return to menu screen. "
howToPlayScreenText = "How To Play? \n \n The down arrow = For sliding the racket into the cell \n \n The Mouse = " \
                      "Sliding the racket \n \n \n The aim of the game is to make a path through the cells using the " \
                      "virus which you bounce with your racket. There will also be blue antibodies flying around and " \
                      "if they touch the racket then you loose a life, but don't worry both the virus and some " \
                      "special balls will destroy anti bodies on impact. These special balls explode from cells that " \
                      "you destroy. To destroy a cell you simply have to hit it with the virus and then slide the " \
                      "racket into the zoomed in part of the cell that will appear at the bottom of your screen. " \
                      "  \n \n \n Double tap to return to menu screen. "

howIsItRelatedToTheSkinImmuneSystemScreenText = "How It Is Related To The Immune System? \n \n Even though this is a " \
                                                "2d arcade game, we have tried to keep it as close to life as we can. " \
                                                "For example, the aim of the game is to infiltrate the skin, " \
                                                "without alerting the immune system. Your main foe are the " \
                                                "antibodies, which in the human body, can fight the viruses by " \
                                                "attaching them self's and harming them, or by blocking the virus " \
                                                "from infecting cells. Another thing the antibodies can do, " \
                                                "is alert the complement, a group of plasma proteins, that will fight " \
                                                "the virus. As you know, your goal is to destroy all cells, " \
                                                "and enter the body, however, when you hit a cell, you need to hit " \
                                                "the right point to correctly destroy the cell, and move on to the " \
                                                "next. This was added to add a layer of complexity to the game, " \
                                                "however, this is similar to a viruses way of entering a cell, " \
                                                "by which they surf along the surface. " \
                                                "  \n \n \n Double tap to return to menu screen. "
TextFontName = "Resources/comicSans.ttf"
textPadding = 0.01
buttonColorChange = 0.7, 0.7, 0.7
