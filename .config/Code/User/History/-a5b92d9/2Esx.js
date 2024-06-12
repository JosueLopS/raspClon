"use strict";
const gpio = require("@iiot2k/gpio");
const OUTPUT_PIN = 17;
gpio.init_gpio(OUTPUT_PIN, gpio.GPIO_MODE_OUTPUT, 1);
var blinkInterval = setInterval(blinkLED, 250); //run the blinkLED function every 250ms

function blinkLED() { //function to start blinking
    gpio.toggle_gpio(OUTPUT_PIN);
}

function endBlink() { //function to stop blinking
  clearInterval(blinkInterval); // Stop blink intervals
  gpio.set_gpio(25, 0);
  gpio.deinit_gpio(25);
}

setTimeout(endBlink, 5000); //stop blinking after 5 seconds