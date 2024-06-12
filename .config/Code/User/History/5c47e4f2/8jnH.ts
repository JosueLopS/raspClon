const SerialPort = require('@serialport/stream');

const port = new SerialPort('/dev/ttyUSB0', { baudRate: 9600 });

port.on('open', () => {
  console.log('Serial port opened');
});

port.on('error', (err) => {
  console.error('Error: ', err.message);
});

port.on('close', () => {
  console.log('Serial port closed');
});
