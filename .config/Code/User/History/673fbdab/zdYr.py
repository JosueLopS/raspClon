import gpiod
import time

# Define los pines GPIO que est�s utilizando
CHIP = gpiod.Chip('gpiochip0')

# Define los pines para el STB, CLK y DIO
stb = CHIP.get_line(22)
clk = CHIP.get_line(27)
dio = CHIP.get_line(17)

# Configura los pines como salida
stb.request(consumer="my_app", type=gpiod.LINE_REQ_DIR_OUT)
clk.request(consumer="my_app", type=gpiod.LINE_REQ_DIR_OUT)
dio.request(consumer="my_app", type=gpiod.LINE_REQ_DIR_OUT)

# Funci�n para enviar un byte al TM1638
def send_byte(data):
    for i in range(8):
        clk.set_value(0)
        dio.set_value(data & 1)
        clk.set_value(1)
        data >>= 1

# Funci�n para enviar un comando al TM1638
def send_command(cmd):
    stb.set_value(0)
    send_byte(cmd)
    stb.set_value(1)

# Funci�n para enviar datos al TM1638
def send_data(addr, data):
    send_command(0x44)
    stb.set_value(0)
    send_byte(0xC0 | addr << 1)
    send_byte(data)
    stb.set_value(1)

# Inicializa el TM1638
send_command(0x8F)

# Muestra un mensaje (por ejemplo, "Hola")
send_data(0, 0x76)  # H
send_data(1, 0x5C)  # o
send_data(2, 0x7C)  # l
send_data(3, 0x6E)  # a

# Espera 5 segundos
time.sleep(5)

# Limpia el display
for i in range(8):
    send_data(i, 0)
