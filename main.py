def on_button_pressed_a():
    music.set_built_in_speaker_enabled(False)
input.on_button_pressed(Button.A, on_button_pressed_a)

while True:
    if input.acceleration(Dimension.STRENGTH) >= 5:
        music.play_melody("B A G A G F A C5 ", 120)
        music.set_volume(100)
        basic.pause(100)
    elif input.acceleration(Dimension.STRENGTH) > 2 and input.acceleration(Dimension.STRENGTH) < 5:
        music.play_melody("C5 B A G F E D C ", 120)
        music.set_volume(100)
        basic.pause(100)

def on_forever():
    pass
basic.forever(on_forever)
