# Importing Ursina game engine
from ursina import *
from pynput_robocorp.keyboard import Key, Controller
#from pynput.keyboard import  Key , Controller
app = Ursina()  # Create an app
window.title = 'MUSIC BOARD'
window.borderless = False
# window.fps_counter.enabled = False
camera.orthographic = True  # This makes the objects look of standard size.
window.set_size(720, 800)  # Size of the window
camera.fov = 15  # Zoom in or zoom out the window
camera.ui_size = 40  # Change size
camera.position = (3, 4)  # This becomes the point(0,0) for below refernece .
Text.default_resolution *= 2  # The size of the text

# Player is the music player which runs through each row in a loop
player = Entity(model='quad', name='Entity', collider='box', color=color.clear, position=(0, 0), scale=(13, .9),
                origin=(-.5, .5))
player1 = Entity(model='quad', name='Entity1', color=color.black33, position=(-.45, 0), scale=(6.9, .9),
                 origin=(-.5, .5))

# Reload button reloads the code
reload_button = Button(parent=scene,
                       color=color.white,
                       position=(-2.9, 9.5),scale=(1.2,1.2),
                       texture=load_texture('reload_image.png'))  # Colour defines colour of button on click
instrument = 1
limit = 5  # Default instrumet = 1#limit should be 1+ of original limit
change_file = Button(parent=scene, position=(-2.9, 8.2), scale=(1, 1),
                     text=f'{instrument}')  #Button to change instrument.

count=0 ;counter = 10 ; count_limit=4; show_count=1
change_speed = Button(parent=scene, position=(-2.9, 6.2), scale=(1, 1),
                     text=f'{1}')#Button to change speed of music player

#Changes the speed
def on_click_change_speed():#Slows down the loop player as number increases
    global counter
    global show_count
    if show_count + 1 < count_limit:
        print(counter)
        show_count +=1
        counter += 5
        change_speed.text = f'>{show_count}'




    #print(instrument)


change_speed.on_click = on_click_change_speed
def on_click_change():
    global instrument
    if instrument + 1 < limit:
        instrument += 1
        change_file.text = f'{instrument}'
        keyboard = Controller()
        keyboard.press('s')
        keyboard.release('s')
    else:

        instrument = 1
        change_file.text = f'{instrument}'
        keyboard = Controller()
        keyboard.press('d')
        keyboard.release('d')
    #print(instrument)


change_file.on_click = on_click_change


# reload button redirects to keypress a. This key has been given a function in the class and is this invoked to reload
def reload_on_click():
    keyboard = Controller()
    keyboard.press('a')
    keyboard.release('a')


reload_button.on_click = reload_on_click

# This describes the background
bg = Entity(parent=scene, model='quad',position=(3, 4), scale=(14.4, 16), z=10, texture=load_texture('background/bg_1.jpg'), collider='box')
background = 1
limit_bg = 6  # Default background = 1#limit should be 1+ of original limit

def on_click_bg_change():

    global background
    if background + 1 < limit_bg:
        background += 1
        bg.texture = load_texture(f'bg_{background}.jpg')
    else:
        background = 1
        bg.texture = load_texture(f'bg_{background}.jpg')
    #print(background)


bg.on_click = on_click_bg_change

mouse.visible = True


# Making  Button
class Button_Entity(Button):
    def __init__(self, position, file_number):
        super().__init__()
        # self.model='quad'
        self.parent = scene
        self.color = color.black66
        self.scale = (.9, .9)
        self.origin = (0, .5)
        self.position = position
        self.row = position[0] + 1
        self.initial_file_number=file_number

        self.file_number = file_number
        self.collider = 'box'
        self.audio = f"audio_{file_number}/row {self.row}.wav"

        self.count_x = 0

    def update(self):  # This function is automatically called within the game loop
        hits_player = self.intersects()  # Checks which object the entity has colided with
        if hits_player.entity != None:  # If the colided entity is not Nothing , then it is the music player that is colliding . Hence play the music.
            if self.color ==  color.rgb(0,255,230):
                self.count_x += 1  # Count is used for changing time
                # print('done')
                global counter
                if self.count_x == counter*2:
                    # The value of self.count_x determined the amout of time that the player entity stays on the button , before moving ahead .
                    # this value should be set in accodance to the value of count in the update() function outside this class{That is , the count concerning with the music player)
                    # The value of self.count_x should be double of the value at line nuber 155 . It is currently set to 10 , hence self.count_x is set to 20 .
                    a = Audio(self.audio, loop=False, autoplay=True,
                              volume=100)  # To change the music , specify the path of the music here
                    self.count_x = 0

    def input(self, key):  # When 'a' is pressed , reload all the buttons to default.
        if key == 'a':
            self.color = color.black66
        if key == 's':
            self.file_number += 1
            self.audio = f"audio_{self.file_number}/row {self.row}.wav"
        if key == 'd':
            self.file_number = self.initial_file_number
            self.audio = f"audio_{self.file_number}/row {self.row}.wav"


# creating button entities in a grid and assigning their behaviour on click
for i in range(0, 7):
    for j in range(10):
        button = Button_Entity(position=(i, j), file_number=instrument)


        def action(button=button):
            if button.color !=  color.rgb(0,255,230):
                button.color =  color.rgb(0,255,230)
            elif button.color ==  color.rgb(0,255,230):
                button.color = color.black66


        button.on_click = action


def change_y_coordinate(entity):  # function to change coordinates of the music player.
    entity.y -= 1


 # This variable is used to count time  (It works better than time.sleep() because it does not interfere with the game loop)


def update():
    global count
    global counter
    count = count + 1
    if count == counter:  # Increase it to slow down the loop , change the self.count_x at line number 110 to double the value set here .
        if player.y == 0:  # If the player is at the bottom of the grid , take it back to the top.
            player.y = 9
            player1.y = 9
            count = 0
        elif player.y > 0:  # If the player is somewhere , move it further by 1 unit
            player.y -= 1
            player1.y -= 1
            count = 0


app.run()