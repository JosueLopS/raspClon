import gpiod
import time

# Definir los pines de datos, reloj y strobe
DATA_PIN = 17
CLK_PIN = 27
STB_PIN = 22

# Definir los comandos del TM1638
TM1638_CMD_DATA = 0x40
TM1638_CMD_ADDR = 0xC0
TM1638_CMD_DISPLAY = 0x80

# Inicializar la conexi�n con libgpiod
chip = gpiod.Chip('gpiochip4')
data_line = chip.get_line(DATA_PIN)
clk_line = chip.get_line(CLK_PIN)
stb_line = chip.get_line(STB_PIN)

# Configurar los pines como salida
data_line.request(consumer="tm1638", type=gpiod.LINE_REQ_DIR_OUT)
clk_line.request(consumer="tm1638", type=gpiod.LINE_REQ_DIR_OUT)
stb_line.request(consumer="tm1638", type=gpiod.LINE_REQ_DIR_OUT)

# Funci�n para enviar un byte al TM1638
def send_byte(byte):
    for i in range(8):
        data_line.set_value((byte >> i) & 0x01)
        clk_line.set_value(0)
        time.sleep(0.5)
        clk_line.set_value(1)
        time.sleep(0.5)

# Funci�n para enviar un comando al TM1638
def send_command(cmd):
    stb_line.set_value(0)
    send_byte(cmd)
    stb_line.set_value(1)

# Funci�n para enviar datos al TM1638
def send_data(addr, data):
    send_command(TM1638_CMD_DATA) #dato 0x40 dir autoinc
    send_command(TM1638_CMD_ADDR | addr) #dir inicio C0 + offset
    #send_command(TM1638_CMD_DATA | data)
    send_command(data)
    
# Funci�n para inicializar el TM1638
def tm1638_init():
    send_command(TM1638_CMD_DISPLAY | 0x08)  # Encender el display

# Funci�n para apagar el TM1638
def tm1638_shutdown():
    send_command(TM1638_CMD_DISPLAY)

# Funci�n para mostrar un n�mero en el TM1638
def tm1638_show_number(number): #escribe a los 8 digitos]
    #for i in range(1):   #8
        #send_data(i * 2, number & 0xFF) #dir y valor
        #send_data(i * 2, 0x3F) #dir y valor
        send_data(0, 0x3F) #dir y valor
        #tm1638_segments()
        number >>= 8

# Funci�n principal
def main():
    tm1638_init()
    try:
        
        # Mostrar n�meros del 0 al 99
        
        #tm1638_show_number(0)
        #time.sleep(0.5)
        while True:
            send_command(TM1638_CMD_DATA) #dato 0x40 dir autoinc
            stb_line.set_value(0)
            send_byte(TM1638_CMD_ADDR)  # dir 0XC0
            for i in range(8):
                send_byte(0x3F)
                send_byte(0)
            stb_line.set_value(1)
            time.sleep(0.5)
    except KeyboardInterrupt:
        tm1638_shutdown()
        print("\nPrograma terminado.")

if __name__ == "__main__":
    main()
