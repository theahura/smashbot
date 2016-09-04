Smash Bot: Neural Network Solution to Super Smash Bros Melee AI

NOTE: BEFORE ALL DOLPHIN SCREENSHOTS RUN
    
    wmctrl -r "Dolphin 5.0-Git | JIT64 DC" -e 0,0,0,640,480

TO ENSURE IMAGE IS IN THE RIGHT SPOT AND SIZE


Pipeline: 
    [Screen cap software] => 
    [neural net input] =>
    [neural net output] => 
    [keyboard input software] =>
    [Dolphin]

<screenshot> : size of the screenshot, likely 600x600.

Screen cap:
    Use Ubuntu GTK to grab screenshot every 4 frames, i.e. 60ms. Current tests
    show grab rate at 8ms. The im is converted into an RGB 1D numpy array. Size
    will be modified to <screenshot>.

Neural Net:
    Neural net designed to take in 1D numpy array of <screenshot> size. The net
    has two components: an action calculator, and a damage calculator. The first
    determines what button presses to do. The second determines whether the AI
    has taken or given damage. 

    Action calculator: completely untrained to start. Learns from playing games
    against AI, and later itself. Input is whole screenshot, output is to a set
    of neurons each indicating a different button press. All keys above a
    threshold will be pressed, with the highest value pressed first in
    descending order. Keys within a certain range will be pressed at the same 
    time. May also use values of joystick keys to indicate force.

    Damage calculator: trained using preset images to start (supervised).
    Learns to identify damage of a character with preset images (entire screen).
    Note that only learns damages for a single character at a time; two of these
    will run simultaneously to learn damage of own char vs opponent.

    Inside the neural net, the damage calculator and action calculator are run
    in parallel. The output of the damage calculator is compared to previous
    outputs of the damage calculator, with the loss changing the weights of the
    action calculator.

Key output:
    An interface will map the neuron outputs to a keyboard mapping software. 
    Dolphin will have a preset configuration to allow for the right keys to do 
    the right things.

Goals:
    Screen cap software: find a way to grab screenshots every frame from a 
    specific window, or see if dolphin has a way to do this in app

        Done, 8-30-16. GTK on Ubuntu grabs full screenshots quickly.
    
    Keyboard input software: programmatically input keys into a system and have
    it run on dolphin using preset keyboard mappings on dolphin layout.

        50%, evdev for key presses, dolphin still profile

    Get damage classifier running:
        Create data list (pngs) with csv to map filenames to values.
		Docs in place, labels started
        Train TF model on csv data.        
		Add in stock tracking
		
		Switch from 0-999 to 3 [1-10] arrays (or find way for every
		datapt to be repped)	
	
        Wire up screen cap software to damage classifier.

DEPS:
    numpy
    gtk
    evdev
    matplotlib

=================================================================================================

