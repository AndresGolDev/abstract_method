from radioportatil import RadioPortatil
from televisorsmart import TelevisorSmart


def main():
    print("==== Radio Portatil ======\n")
    r1 = RadioPortatil("Samsung")
    r1.mostrar_info()
    r1.reproducir()
    r1.detener()

    print("\n==== Televisor Smart ======")

    t1 = TelevisorSmart("LG")
    t1.mostrar_info()
    t1.reproducir()
    t1.detener()

if __name__ == "__main__":
    main()


