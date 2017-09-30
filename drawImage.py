from PIL import Image, ImageDraw, ImageFont
from os import listdir
from os.path import isfile, join
import math

def arrangeImagesInCircle(masterImage, imagesToArrange):
    imgWidth, imgHeight = masterImage.size

    #we want the circle to be as large as possible.
    #but the circle shouldn't extend all the way to the edge of the image.
    #If we do that, then when we paste images onto the circle, those images will partially fall over the edge.
    #so we reduce the diameter of the circle by the width/height of the widest/tallest image.
    diameter = min(
        imgWidth  - max(img.size[0] for img in imagesToArrange),
        imgHeight - max(img.size[1] for img in imagesToArrange)
    )
    radius = diameter / 2

    circleCenterX = imgWidth  / 2
    circleCenterY = imgHeight / 2
    theta = 2*math.pi / len(imagesToArrange)
    for i, curImg in enumerate(imagesToArrange):
        angle = i * theta - (math.pi/2)
        dx = int(radius * math.cos(angle))
        dy = int(radius * math.sin(angle))

        #dx and dy give the coordinates of where the center of our images would go.
        #so we must subtract half the height/width of the image to find where their top-left corners should be.
        pos = (
            circleCenterX + dx - curImg.size[0]/2,
            circleCenterY + dy - curImg.size[1]/2
        )
        masterImage.paste(curImg, pos)

# teams = [u'Arsenal', u'Aston Villa', u'Birmingham City', u'Blackburn Rovers', u'Bolton Wanderers', u'Charlton Athletic', u'Chelsea', u'Everton', u'Fulham', u'Liverpool', u'Manchester City', u'Manchester United', u'Middlesbrough', u'Newcastle United', u'Portsmouth', u'Sunderland', u'Tottenham Hotspur', u'West Bromwich Albion', u'West Ham United', u'Wigan Athletic']
def genericLogo(txt):
    image = Image.new("RGBA", (150,150), (255,255,255))
    x, y =  image.size
    eX, eY = 80, 120

    bbox =  (x/2 - eX/2, y/2 - eY/2, x/2 + eX/2, y/2 + eY/2)
    draw = ImageDraw.Draw(image)
    draw.ellipse(bbox, fill=(0,0,0))
    font = ImageFont.truetype("Ubuntu-B.ttf", 15)
    draw.text((60, 60),txt,(255,255,255),font=font)
    del draw
    return image

def scoreImg(score):
    # img = Image.open('./Logos/Arsenal.png')
    image = Image.new("RGBA", (30, 30), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("Ubuntu-B.ttf", 20)
    draw.text((2, 2), score, (0, 0, 0), font=font)
    del draw
    return image

def clubLogo(loc):
    image = Image.open(loc)
    width, height = image.size
    ratio = 100.0 / width

    w, h = int(ratio * width), int(ratio * height)

    image = image.resize((w, h), Image.ANTIALIAS)
    return image



# for file in onlyfiles:
#     print file.lower()
def getImage(teams,cop,scores):
    images = []
    onlyfiles = [f for f in listdir('./ClubLogos') if isfile(join('./ClubLogos', f))]
    count = 0
    for i in range(len(cop)):
        team = teams[cop[i]]
        score = scores[cop[i]][cop[(i+1)%len(cop)]]
        parts = team.split(' ')
        flag = False
        for file in onlyfiles:
            found = True
            for part in parts:
                if part.lower() not in file.lower():
                    found = False
            if found:
                images.append(clubLogo('./ClubLogos/' + file))
                flag = True
                break
        if not flag:
            if len(parts) > 1:
                c_name = list(parts[0])[0] + (parts[1])[0]
                images.append(genericLogo(c_name))
            else:
                c_name = list(parts[0])[0] + list(parts[0])[1] + list(parts[0])[2]
                images.append(genericLogo(c_name))
        if count > 4 and count <= 14:
            g1, g2 = score.split('-')
            score = g2 + '-' + g1
            images.append(scoreImg(score))
        else:
            images.append(scoreImg(score))
        count += 1

    img = Image.new("RGB", (1500,1500), (255,255,255))
    arrangeImagesInCircle(img, images)
    img.save("output.png")
