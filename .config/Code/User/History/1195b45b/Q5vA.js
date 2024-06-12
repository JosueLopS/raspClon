const SerialPort = require('serialport');

// Replace '/dev/ttyUSB0' with the correct port name
const port = new SerialPort('/dev/ttyUSB0', {
  baudRate: 9600,
});

port.on('open', () => {
  console.log('Serial port opened');
});

port.on('error', (err) => {
  console.error('Error: ', err.message);
});

port.on('close', () => {
  console.log('Serial port closed');
});

// Ensure you close the port when you're done
process.on('SIGINT', () => {
  port.close(() => {
    console.log('Process terminated, serial port closed');
    process.exit();
  });
});
