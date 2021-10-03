input.onButtonPressed(Button.A, function on_button_pressed_a() {
    music.setBuiltInSpeakerEnabled(false)
})
while (true) {
    if (input.acceleration(Dimension.Strength) >= 5) {
        music.playMelody("B A G A G F A C5 ", 120)
        music.setVolume(100)
        basic.pause(100)
    } else if (input.acceleration(Dimension.Strength) > 2 && input.acceleration(Dimension.Strength) < 5) {
        music.playMelody("C5 B A G F E D C ", 120)
        music.setVolume(100)
        basic.pause(100)
    }
    
}
basic.forever(function on_forever() {
    
})
