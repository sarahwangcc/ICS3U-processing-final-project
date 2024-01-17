import random
add_library('minim')

def setup():
    global welcome, instructions, i, heartx, hearty, enemyx, enemyy, enemy_speed,  hit_enemy, hwx, hwy, num1, num2, dictionary, xlist, ylist, sound, num_attacks, enemy_hw, coffee
    global playerx, playery, song, powerupx, powerupy, speed, status, hearts, num_powerup, x, y, cor, direction, congrats, num_enemy, num_run, sound1, hit, spikes, heartimg, person
    y = 50
    size(1000, 700)
    background('#F1E3B0')
    welcome = loadImage('Game start screen.png')
    instructions = loadImage('Game Instructions Screen.png')
    congrats = loadImage('End screen  (1).png')
    enemy_hw = loadImage('homework.png')
    enemy_hw.resize(50, 50)
    heartimg = loadImage('heart-png-15.png')
    heartimg.resize(50, 50)
    coffee = loadImage('coffee.png')
    coffee.resize(50, 50)
    person = loadImage('happy-removebg-preview.png')
    person.resize(50, 50)
    
    #player variables
    playerx = 50
    playery = 50
   
    #speed variable
    speed = 8
    
    #song variable
    minim = Minim(this)
    song = minim.loadFile('2021-08-16_-_8_Bit_Adventure_-_www.FesliyanStudios.com.mp3')
    sound = minim.loadSample('mixkit-video-game-retro-click-237.wav')
    sound1 = minim.loadSample('cartoon-jump-6462.mp3')
   
    #powerup varaible
    powerupx = random.randrange(50, 435)
    powerupy = random.randrange(50, 650)
    
    #extra hearts variable
    heartx = random.randrange(575, 900)
    hearty = random.randrange(50, 650)
   
    #state variable
    status = 0
   
    #hearts variable
    hearts = 3
   
    #number of powerups gained
    num_powerup = 0
    
    #number of times player runs away
    num_run = 0
   
    #barrier variables
    x = 50
    y = 50
   
    #counting variable
    i = 0
    j= 0
   
   #list for coordinates
    cor = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    spikes = [0, 0, 0, 0]
    
    #variables for enemies
    enemyx = 620
    enemyy = 175
    enemy_speed = 1
    direction = 1
    hit_enemy = False
    num_enemy = 0
    
    #variables for minigame #1
    hwx = random.randrange(25, 950)
    hwy = random.randrange(180, 600)
    
    #variables for minigame #2
    num1 = random.randrange(0, 100)
    num2 = random.randrange(0, 100)    
    sum = num1 + num2
    dictionary = {'sum1' : sum, 'sum2' : sum + 33, 'sum3' : sum - 12, 'sum4' : 2*sum}
    xlist = [230, 730, 205, 730]
    ylist = [285, 285, 550, 550]
    
    #attack variable
    num_attacks = 0

def draw():
    global playerx, playery, person
    background('#F1E3B0')
    if status == 0:
        start_screen()
    if status == 1:
        instruction_screen()
    fill('#2DA12B')
    
    #calling the levels
    if status == 2:
        level1()
    if status == 3:
        level2()
    if status == 4:
        whackhw()
    if status == 5:
        level3()
    if status == 6:
        level4()
    if status == 7:
        trivia()
    if status == 8:
        level5()
    if status == 9:
        congrats_screen()
    if status == 10:
        end_screen()
    if hearts <= 0:
        dead()
        
    if num_attacks == 5:
        fight()
   
    #the player square/ icon
    if status >= 2 and status < 10:
        image(person, playerx, playery)
        
######################################################################
# Function Name: keyPressed
# Function Purpose: to detect key presses
# Variables:playerx, playery, song, speed, status, sound, hit_enemy, sound1, num_attacks, powerupx, powerupy, heartx, hearty, enemyx, enemyy, hit_enemy, direction
# Return: whenever a specific key is pressed, something will happen
######################################################################

def keyPressed():
    global playerx, playery, song, speed, status, sound, hit_enemy, sound1, num_attacks, powerupx, powerupy, heartx, hearty, enemyx, enemyy, hit_enemy, direction
    #player movement
    if key == 'w':
        playerx += 0
        playery += -speed
        sound.trigger()
    elif key == 's':
        playerx += 0
        playery += speed
        sound.trigger()
    elif key == 'a':
        playerx += -speed
        playery += 0
        sound.trigger()
    elif key == 'd':
        playerx += speed
        playery += 0
        sound.trigger()
    elif key == ' ':
        playerx += 50
        sound1.trigger()
       
    #keys for the music
    if key == "g":
        song.play()
    if key == "p":
        song.pause()
    if key == "r":
        song.rewind()
       
    #keys for the screens
    if key == ENTER:
        status = 1
    if key == 'x':
        status = 2
    if key == 'c':
        status = 10
        
    #keys for running away or figting
    if key == 'n':
        run()
    if key == 'y':
        fight()
        
    #quit screen
    if key == 'q':
        status = 10
        
    if key =='1':
        #powerup variable
        powerupx = random.randrange(50, 435)
        powerupy = random.randrange(50, 650)
    
        #extra hearts variable
        heartx = random.randrange(575, 900)
        hearty = random.randrange(50, 650)
        
        num_attacks = 0
        enemyx = 620
        enemyy = 175
        hit_enemy = False
        
######################################################################
# Function Name: mouse Pressed
# Function Purpose: to detect mouse presses
# Variables: global playerx, playery, num_attacks, hit, num_attacks
######################################################################

def mousePressed():
    global playerx, playery, num_attacks, hit, num_attacks
    print(mouseX, mouseY)
    print(playerx, playery)
    fill('#FFC214')
    rect(playerx + 60, playery + 20, 50, 10)
    if playerx + 70 > enemyx - 20  and playery < enemyy and playery > enemyy - 20: 
        num_attacks += 1
        print(num_attacks)
######################################################################
# Function Name: start screen
# Function Purpose: to display the welcome screen
# Variables: welcome
######################################################################

def start_screen():
    global welcome
    image(welcome, 0, 0)
    
######################################################################
# Function Name: instruction screen
# Function Purpose: to display the instruction screen
# Variables: instructions
######################################################################

def instruction_screen():
    global instructions
    image(instructions, 0, 0)

######################################################################
# Function Name: congrats screen 
# Function Purpose: to display the congrats screen
# Variables: congrats
######################################################################

def congrats_screen():
    global congrats
    image(congrats, 0, 0)
    fill(0)
    textSize(25)
    text('Press c to continue', 300, 500)

######################################################################
# Function Name:stats screen 
# Function Purpose: shows all the stats when the player ends the game
# Variables: num_powerup, num_enemy, num_run
######################################################################

def stats_screen():
    global num_powerup, num_enemy, num_run
    fill(255)
    rect(100, 100, 800, 500)
    fill(0)
    textSize(25)
    text('Your stats are:', 200, 200)
    text('Number of powerups picked up:', 200, 250)
    text(num_powerup, 600, 250)
    text('Number of Enemies defeated:', 200, 300)
    text(num_enemy, 600, 300)
    text('Number of times that you ran away:', 200, 350)
    text(num_run, 700, 350)
    text('Number of lives you ended with:', 200, 400)
    text(hearts, 700, 400)
    
def end_screen():
    global num_powerup, num_enemy, num_run
    fill(255)
    rect(100, 100, 800, 500)
    fill(0)
    textSize(25)
    text('Your stats are:', 200, 200)
    text('Number of powerups picked up:', 200, 250)
    text(num_powerup, 600, 250)
    text('Number of Enemies defeated:', 200, 300)
    text('5', 600, 300)
    text('Number of times that you ran away:', 200, 350)
    text(num_run, 700, 350)
    text('Number of lives you ended with:', 200, 400)
    text(hearts, 700, 400)
    
######################################################################
# Function Name: wall barriers
# Function Purpose: to make sure the player cannot leave the screen
# Variables: playerx, playery
######################################################################

def wall_barriers():
    global playerx, playery
    if playerx + 50 > width:
        playerx = width - 50
    if playery  + 50 > height:
        playery = height - 50
    elif playerx < 0:
        playerx = 0
    elif playery < 0:
        playery = 0

######################################################################
# Function Name: platform barriers
# Function Purpose: to prevent the player from walking into walls
# Variables: playerx, playery, speed, cor, x, y, i
######################################################################

def platform_barriers():
    global playerx, playery, speed, cor, x, y, i
    i = 0
    if (cor[i][0] - 50 <= playerx <= cor[i][2]) and (cor[i][3] >= playery >= cor[i][1] - 50):
        playery = y
        playerx = x
    i += 1
    if (cor[i][0] - 50 <= playerx <= cor[i][2]) and (cor[i][3] >= playery >= cor[i][1] - 50):
        playery = y
        playerx = x
    i += 1
    if (cor[i][0] - 50 <= playerx <= cor[i][2]) and (cor[i][3] >= playery >= cor[i][1] - 50):
        playery = y
        playerx = x
    i += 1
    if (cor[i][0] - 50 <= playerx <= cor[i][2]) and (cor[i][3] >= playery >= cor[i][1] - 50):
        playery = y
        playerx = x
    i += 1
    if (cor[i][0] - 50 <= playerx <= cor[i][2]) and (cor[i][3] >= playery >= cor[i][1] - 50):
        playery = y
        playerx = x
    else:
        y = playery
        x = playerx
        
######################################################################
# Function Name: spikes
# Function Purpose: to create the spikes
# Variables: playerx, playery, spikes, hearts
######################################################################

def easy_spikes():
    global playerx, playery, spikes, hearts
    if (spikes[0] - 50 <= playerx <= spikes[2]) and (spikes[3] >= playery >= (spikes[1] - 50)):
        playery = 50
        playerx = 50
        hearts -= 1
        
######################################################################
# Function Name: speed powerup
# Function Purpose: to create the speed powerups
# Variables: powerupx, powerupy, speed, num_powerup, hearts
######################################################################
    
def speed_powerup():
    global powerupx, powerupy, speed, num_powerup, hearts, heartimg, coffee
    #spawns the powerup in a random place
    fill('#00FF00')
    image(coffee, powerupx, powerupy)
    #detects the powerup
    if (playerx + 50) > (powerupx - 25) and playerx - 50 < (powerupx + 25) and (playery + 50) >= (powerupy - 25) and playery - 50 <= (powerupy + 25):
        fill(0)
        text('you got a powerup!', 755, 100)
        speed += 1
        powerupx = 2000
        powerupy = 2000
        num_powerup += 1    
        
######################################################################
# Function Name: heart powerup
# Function Purpose: to create the heart powerups
# Variables: global speed, num_powerup, heartx, hearty, hearts
######################################################################
       
def heart_powerup():
    global speed, num_powerup, heartx, hearty, hearts
    #spawns the powerup in a random place
    fill('#FF00000')
    image(heartimg, heartx, hearty)
    #detects the powerup
    if (playerx + 50) > (heartx - 25) and playerx - 50 < (heartx + 25) and (playery + 50) >= (hearty - 25) and playery - 50 <= (hearty + 25):
        fill(0)
        text('you got a powerup!', 755, 100)
        heartx = 2000
        hearty = 2000
        num_powerup += 1
        hearts += 1
        
######################################################################
# Function Name: stats
# Function Purpose: to show the message box 
# Variables: hearts, num_powerup, num_enemy, num_run
######################################################################

def stats():
    global hearts, num_powerup, num_enemy, num_run
    #message box
    fill('#FFFFFF')
    textSize(15)
    rect(750, 0, 300, 125)
    fill(0)
    text('number of hearts is:', 755, 20)
    text(hearts, 910, 20)
    text('number of powerups is:', 755, 40)
    text(num_powerup, 935, 40)
    text('number of times you ran away:', 755, 60)
    text(num_run, 985, 60)
    text('number of enemies defeated:', 755, 80)
    text(num_enemy, 980, 80)
 
######################################################################
# Function Name: door
# Function Purpose: to make the exit box
# Variables: status, playerx, playery
######################################################################
 
def door():
    global status, playerx, playery
    #door
    fill('#FF0000')
    rect(970, 550, 200, 200)
    if (playerx + 25) > 970 and playery > (500):
        status += 1
        playerx = 50
        playery = 50
        
######################################################################
# Function Name: dead
# Function Purpose: what happens after the player dies
# Variables: hearts
######################################################################
        
def dead():
    global hearts
    fill(255)
    rect(100, 100, 800, 500)
    fill(0)
    textSize(50)
    text('You have died :(', 200, 200)
    textSize(15)
    fill(0)
    textSize(25)
    text('Number of powerups picked up:', 200, 250)
    text(num_powerup, 600, 250)
    text('Number of Enemies defeated:', 200, 300)
    text(num_enemy, 600, 300)
    text('Number of times that you ran away:', 200, 350)
    text(num_run, 700, 350)
    text('Number of lives you ended with:', 200, 400)
    text(hearts, 700, 400)
    
######################################################################
# Function Name: enemy
# Function Purpose: code controlling the enemies
# Variables: enemyx, enemyy, hearts, enemy_speed, direction, playerx, playery, hit_enemy, num_run, num_attacks
######################################################################

def enemy():
    global enemyx, enemyy, hearts, enemy_speed, direction, playerx, playery, hit_enemy, num_run, num_attacks, enemy_hw
    fill(255)
    image(enemy_hw, enemyx, enemyy)
    
    #enemy movement
    enemyy = enemyy + (enemy_speed * direction)
    if enemyy <= 170 or enemyy >= 550:
        direction *= -1
                
    # detects if the player hits the enemy
    if playerx >= (enemyx - 50) and playerx <= (enemyx + 50) and playery >= (enemyy - 50) and playery <= (enemyy + 50):
        fill(0)
        enemy_speed = 0
        hit_enemy = True
        if hit_enemy == True:
            rect(100, 100, 800, 500)
            fill(255)
            rect(150, 150, 700, 400)
            fill(0)
            textSize(25)
            text('Fight the evil homework?', 300, 180)
            textSize(15)
            text('Press the y key for Yes (fight), or n for No (Run away)', 300, 200)
            textSize(25)
            text('YES', 270, 420)
            text('NO', 690, 420)
            
######################################################################
# Function Name: fight
# Function Purpose: what happens when the player chooses yes
# Variables: enemyx, enemy, hit_enemy, playerx, playery, enemyx, enemyy, num_attacks, num_enemy
######################################################################
        
def fight():
    global enemyx, enemy, hit_enemy, playerx, playery, enemyx, enemyy, num_attacks, num_enemy
    enemyx = 700 
    enemyy = 300
    if num_attacks == 5:
        enemyx = 2000
        enemyy = 2000
        num_enemy = status - 1
        print('You won!')

######################################################################
# Function Name: run
# Function Purpose: what happens when the player chooses no
# Variables: hit_enemy, playerx, playery, num_run, enemy_speed
######################################################################

def run():
    global hit_enemy, playerx, playery, num_run, enemy_speed
    hit_enemy = 0
    playerx = 50
    playery = 50
    num_run += 1
    enemy_speed = 1

######################################################################
# Function Name: level 1
# Function Purpose: draws level 1
# Variables: playerx, playery, powerupx, powerupy, cor, i, num_attacks, spikes 
######################################################################

def level1():
    #variables and calling functions
    global playerx, playery, powerupx, powerupy, cor, i, num_attacks, spikes
    heart_powerup()
    stats()
    platform_barriers()
    wall_barriers()
    speed_powerup()
    door()
    easy_spikes()
   
    #list for coordinates
    cor = [[150, 0, 160, 300], [0, 400, 300, 400], [300, 110, 310, 400], [450, 0, 460, 550], [125, 550, 460, 560]]
    spikes = [0, 360, 80, 400]
    
    #maze
    stroke(0)
    fill('#AD901C')
    rect(150, 0, 10, 300)
    rect(0, 400, 300, 10)
    rect(300, 110, 10, 300)
    rect (450, 0, 10, 550)
    rect(125, 550, 335, 10)
    
    #spikes
    fill(0)
    triangle(0, 400, 40, 360, 80, 400)
    enemy()

######################################################################
# Function Name: level 2
# Function Purpose: draws level 2
# Variables: playerx, playery, powerupx, powerupy, cor, i, num_attacks, spikes 
######################################################################

def level2():
    #variables and calling functions
    global playerx, playery, powerupx, powerupy, cor, i, num_attacks, spikes, heartx, hearty, spikes, hearts
    heart_powerup()
    stats()
    platform_barriers()
    wall_barriers()
    speed_powerup()
    door()
    easy_spikes()
   
    #coordinate list
    cor = [[0, 100, 300, 110], [120, 195, 420, 205], [0, 310, 300, 320], [420, 0, 430, 300], [420, 415, 430, 700]]
    spikes = [120, 170, 210, 195]
   
    #maze lines
    fill('#AD901C')
    rect(0, 100, 300, 10)
    rect(420, 0, 10, 300)
    rect(120, 195, 300, 10)
    rect(0, 310, 300, 10)
    rect(420, 415, 10, 300)
    #spikes
    fill(0)
    triangle(120, 195, 165, 170, 210, 195)
    enemy()
    
######################################################################
# Function Name: level 3
# Function Purpose: draws level 3
# Variables: playerx, playery, powerupx, powerupy, cor, i, num_attacks, spikes 
######################################################################
   
def level3():
    #variables and calling functions
    global playerx, playery, powerupx, powerupy, cor, i, spikes, enemyx, enemyy, spikes, hearts
    
    heart_powerup()
    stats()
    platform_barriers()
    wall_barriers()
    speed_powerup()
    door()
    easy_spikes()
   
    #coordinate list
    cor = [[485, 190, 495, 700], [150, 0, 160, 550], [300, 200, 310, 500], [150, 100, 350, 110], [0,0,0,0]]
    spikes = [260, 470, 300, 370]
    
    #maze lines
    fill('#AD901C')
    rect(485, 190, 10, 550)
    rect(150, 0, 10, 550)
    rect(300, 200, 10, 300)
    rect(150, 100, 200, 10)
    fill(0)
    triangle(300, 475, 260, 430, 300, 370)
    
    enemy()

######################################################################
# Function Name: level 4
# Function Purpose: draws level 4
# Variables: playerx, playery, powerupx, powerupy, cor, i, num_attacks, spikes 
######################################################################

def level4():
    #variables and calling functions
    global playerx, playery, powerupx, powerupy, cor, i, spikes, hearts
    heart_powerup()
    stats()
    platform_barriers()
    wall_barriers()
    speed_powerup()
    door()
    easy_spikes()
    
    enemyx = 620
    enemyy = 175
   
    #coordinate list
    cor = [[0, 120, 340, 130], [440, 0, 450, 490], [110, 490, 450, 500], [340, 120, 350, 320], [110, 300, 120, 490]]
    spikes = [120, 450, 210, 490]
              
    #maze lines
    fill('#AD901C')
    rect(0, 120, 350, 10)
    rect(440, 0, 10, 500)
    rect(110, 490, 340, 10)
    rect(340, 120, 10, 200)
    rect(110, 300, 10, 190)
    fill(0)
    triangle(120, 490, 175, 450, 210, 490)
    
    enemy()

######################################################################
# Function Name: level 5
# Function Purpose: draws level 5
# Variables: playerx, playery, powerupx, powerupy, cor, i, num_attacks, spikes 
######################################################################

def level5():
    #variables and calling functions
    global playerx, playery, powerupx, powerupy, cor, i, spikes, hearts
    heart_powerup()
    stats()
    platform_barriers()
    wall_barriers()
    speed_powerup()
    door()
    
    enemyx = 620
    enemyy = 175
   
    #coordinate list
    cor = [[210, 100, 410, 200], [210, 300, 410, 400], [210, 500, 410, 600], [645, 130, 745, 330], [645, 390, 745, 590]]
   
    #maze lines
    fill('#AD901C')
    rect(210, 100, 200, 100)
    rect(210, 300, 200, 100)
    rect(210, 500, 200, 100)
    rect(645, 130, 100, 200)
    rect(645, 390, 100, 200)
    
    enemy()
    
######################################################################
# Function Name: hw game
# Function Purpose: for the first minigame
# Variables: hwx, hwy, status
######################################################################

def whackhw():
    global hwx, hwy, status
    fill('#00FF00')
    rect(200, 345, 45, 55)
    fill('#3EA3D2')
    circle(456, 198, 100)
    fill('#BC3ED2')
    rect(500, 400, 200, 100)
    fill(0)
    circle(300, 200, 50)
    fill('#3ED2A3')
    circle(300, 300, 120)
    fill('#FFD800')
    rect(700, 500, 120, 300)
    fill('#00ECFF')
    circle(434, 563, 60)
    fill('#FF00FF')
    rect(876, 200, 120, 300)
    fill('#FF8700')
    rect(97, 567, 100, 234)
    fill('#6AAE31')
    rect(708, 260, 324, 134)
    fill('#FFBD00')
    circle(106, 243, 100)
    fill('#FF0000')
    rect(hwx, hwy, 50, 50)
    
    textSize(30)
    fill(255)
    rect(0, 0, 1000, 170)
    fill(0)
    text('Oh no! An assignment has gone missing.', 100, 80)
    text('Look for the red square.', 100, 130)

    if mousePressed == True:
        if mouseX > hwx and mouseX < (hwx + 70) and mouseY > hwy and mouseY < (hwy + 100):
            text('You found the lost assigment!', 300, 300)
            status += 1
        else:
            text('That is not it!', mouseX, mouseY)

######################################################################
# Function Name: trivia
# Function Purpose: for the second minigame, trivia
# Variables: num1, num2, dictionary, xlist, ylist, status
######################################################################
def trivia():
    global num1, num2, dictionary, xlist, ylist, status
    #trivia boxes
    fill(255)
    rect(0, 0, 1000, 150)
    textSize(35)
    fill(0)
    text("What is the sum of: ", 100, 75)
    text(num1, 500, 75)
    text('+', 550, 75)
    text(num2, 600, 75)
    line(500, 150, 500, 800)
    line(0, 425, 1000, 425)
    text(dictionary['sum1'], xlist[0], ylist[0])
    text(dictionary['sum2'], xlist[1], ylist[1])
    text(dictionary['sum3'], xlist[2], ylist[2])
    text(dictionary['sum4'], xlist[3], ylist[3])
    if mousePressed == True:
        if mouseX > 0 and mouseX < 500 and mouseY > 150 and mouseY < 425:
            text("Correct!", 720, 65)
            status += 1
        else:
            text('Incorrect :(', 720, 65)
    
