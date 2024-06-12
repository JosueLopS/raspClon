var http = require('http').createServer(handler); //require http server, and create server with function handler()
var fs = require('fs'); //require filesystem module
var io = require('socket.io')(http) //require socket.io module and pass the http object (server)
const gpio = require("@iiot2k/gpio");

//const INPUT_PIN = 15;
//const OUTPUT_PIN = 25;
//const DEBOUNCE_US = 1000; // us
//const GPIO_MODE_INPUT_PULLDOWN = 
const BLINK_TIME_MS = 1500; // ms
const GPIO_EDGE_BOTH = 2;
//gpio.init_gpio(OUTPUT_PIN, gpio.GPIO_MODE_OUTPUT, 0);
const LED_RED = 4;
const LED_GREEN = 17;
const LED_BLUE = 27;

//const DEBOUNCE_US = 1000; // us
//const SCAN_TIME_MS = 50; // ms
const PWM_FREQ = 200; // Hz
const PWM_DUTYC_1 = 75; // %
const PWM_DUTYC_2 = 25; // %

gpio.init_gpio(LED_RED, gpio.GPIO_MODE_PWM, 0);
gpio.init_gpio(LED_GREEN, gpio.GPIO_MODE_PWM, 0);
gpio.init_gpio(LED_BLUE, gpio.GPIO_MODE_PWM, 0);

/*var Gpio = require('pigpio').Gpio, //include pigpio to interact with the GPIO
ledRed = new Gpio(4, {mode: Gpio.OUTPUT}), //use GPIO pin 4 as output for RED
ledGreen = new Gpio(17, {mode: Gpio.OUTPUT}), //use GPIO pin 17 as output for GREEN
ledBlue = new Gpio(27, {mode: Gpio.OUTPUT}), //use GPIO pin 27 as output for BLUE

redRGB = 0, //set starting value of RED variable to off (0 for common cathode)
greenRGB = 0, //set starting value of GREEN variable to off (0 for common cathode)
blueRGB = 0; //set starting value of BLUE variable to off (0 for common cathode)
*/

//RESET RGB LED
/*ledRed.digitalWrite(0); // Turn RED LED off
ledGreen.digitalWrite(0); // Turn GREEN LED off
ledBlue.digitalWrite(0); // Turn BLUE LED off
*/
http.listen(8080); //listen to port 8080

function handler (req, res) { //what to do on requests to port 8080
  fs.readFile(__dirname + '/public/rgb.html', function(err, data) { //read file rgb.html in public folder
    if (err) {
      res.writeHead(404, {'Content-Type': 'text/html'}); //display 404 on error
      return res.end("404 Not Found");
    }
    res.writeHead(200, {'Content-Type': 'text/html'}); //write HTML
    res.write(data); //write data from rgb.html
    return res.end();
  });
}

io.sockets.on('connection', function (socket) {// Web Socket Connection
  socket.on('rgbLed', function(data) { //get light switch status from client
    console.log(data); //output data from WebSocket connection to console

    //for common cathode RGB LED 0 is fully off, and 255 is fully on
    redRGB=parseInt(data.red);
    greenRGB=parseInt(data.green);
    blueRGB=parseInt(data.blue);

    gpio.set_pwm(LED_RED, PWM_FREQ, redRGB);
    gpio.set_pwm(LED_GREEN, PWM_FREQ, greenRGB);
    gpio.set_pwm(LED_BLUE, PWM_FREQ, blueRGB);


/*    ledRed.pwmWrite(redRGB); //set RED LED to specified value
    ledGreen.pwmWrite(greenRGB); //set GREEN LED to specified value
    ledBlue.pwmWrite(blueRGB); //set BLUE LED to specified value  */
  });
});

process.on('SIGINT', function () { //on ctrl+c
  gpio.deinit_gpio(LED_RED);
  gpio.deinit_gpio(LED_GREEN);
  gpio.deinit_gpio(LED_BLUE);
  process.exit(); //exit completely
});
