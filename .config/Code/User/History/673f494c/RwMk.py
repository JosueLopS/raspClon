import gpiod
import time

# Definir los pines de datos, reloj y strobe
DATA_PIN = 17
CLK_PIN = 27
STB_PIN = 22

# Tabla de segmentos para las letras A-Z y espacio
SEGMENT_TABLE = {
    'H': 0b01110110,
    'E': 0b01111011,
    'L': 0b00001111,
    'O': 0b00111111,
    ' ': 0b00000000  # Espacio
}

chip = gpiod.Chip('gpiochip4')
data_line = chip.get_line(DATA_PIN)
clk_line = chip.get_line(CLK_PIN)
stb_line = chip.get_line(STB_PIN)

data_line.request(consumer="tm1638", type=gpiod.LINE_REQ_DIR_OUT)
clk_line.request(consumer="tm1638", type=gpiod.LINE_REQ_DIR_OUT)
stb_line.request(consumer="tm1638", type=gpiod.LINE_REQ_DIR_OUT)

def send_byte(byte):
    for i in range(8):
        data_line.set_value((byte >> i) & 0x01)
        clk_line.set_value(0)
        time.sleep(0.5)
        clk_line.set_value(1)
        time.sleep(0.5)

def send_command(cmd):
    stb_line.set_value(0)
    send_byte(cmd)
    stb_line.set_value(1)

def send_data(addr, data):
    send_command(TM1638_CMD_DATA)  # dato 0x40 dir autoinc
    send_command(TM1638_CMD_ADDR | addr)  # dir inicio C0 + offset
    send_command(data)

# Funci�n para inicializar el TM1638
def tm1638_init():
    send_command(TM1638_CMD_DISPLAY | 0x08)  # Encender el display

def tm1638_shutdown():
    send_command(TM1638_CMD_DISPLAY)

def show_text(text):
    for i, char in enumerate(text):
        if char in SEGMENT_TABLE:
            send_data(i * 2, SEGMENT_TABLE[char])

# Funci�n principal
def main():
    tm1638_init()
    try:
        show_text("HELLO")
        time.sleep(2)  # Espera 2 segundos
        tm1638_shutdown()
    finally:
        data_line.release()
        clk_line.release()
        stb_line.release()

if __name__ == "__main__":
    main()
