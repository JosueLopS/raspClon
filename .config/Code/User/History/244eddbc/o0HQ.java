import java.io.FileWriter;
import java.io.IOException;

public class BlinkLED {

    public static void main(String[] args) throws InterruptedException {
        // Especifica el n�mero del pin GPIO que quieres utilizar (17)
        final int pinNumber = 17;

        // Exporta el pin para que est� disponible para su uso
        exportPin(pinNumber);

        // Configura el pin como salida
        setDirection(pinNumber, "out");

        try {
            // Hace parpadear el LED 10 veces
            for (int i = 0; i < 100; i++) {
                // Enciende el LED
                setValue(pinNumber, 1);
                System.out.println("LED encendido");
                Thread.sleep(1000); // Espera 1 segundo

                // Apaga el LED
                setValue(pinNumber, 0);
                System.out.println("LED apagado");
                Thread.sleep(1000); // Espera 1 segundo
            }
        } finally {
            // Desexporta el pin cuando hayamos terminado
            unexportPin(pinNumber);
        }
    }

    private static void exportPin(int pinNumber) {
        try (FileWriter writer = new FileWriter("/sys/class/gpio/export")) {
            writer.write(String.valueOf(pinNumber));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void unexportPin(int pinNumber) {
        try (FileWriter writer = new FileWriter("/sys/class/gpio/unexport")) {
            writer.write(String.valueOf(pinNumber));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void setDirection(int pinNumber, String direction) {
        try (FileWriter writer = new FileWriter("/sys/class/gpio/gpio" + pinNumber + "/direction")) {
            writer.write(direction);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void setValue(int pinNumber, int value) {
        try (FileWriter writer = new FileWriter("/sys/class/gpio/gpio" + pinNumber + "/value")) {
            writer.write(String.valueOf(value));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
