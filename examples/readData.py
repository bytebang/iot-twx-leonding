from sense_hat import SenseHat
import time

def main():
    # Initialisieren Sie das Sense HAT-Objekt
    sense = SenseHat()

    try:
        while True:
            # IMU-Daten lesen
            acceleration = sense.get_accelerometer_raw()

            # Hygrometerdaten lesen
            humidity = sense.get_humidity()

            # Ausgabe auf der Kommandozeile
            print("Beschleunigung (m/s^2):")
            print(" X:", round(acceleration['x'],2))
            print(" Y:", round(acceleration['y'],2))
            print(" Z:", round(acceleration['z'],2))
            print("Luftfeuchtigkeit (%):", round(humidity,2))
            print("\n")

            # Warten Sie eine Weile, bevor Sie die nächsten Daten lesen
            time.sleep(0.1)

    except KeyboardInterrupt:
        # Programm beenden, wenn Strg+C gedrückt wird
        pass

if __name__ == "__main__":
    main()

