class Controlador:
    def __init__(self):
        # Inicializar los componentes necesarios para el programa
        self.componente_a = ComponenteA()
        self.componente_b = ComponenteB()
        self.resultado = None

    def iniciar_programa(self):
        print("Iniciando programa...")
        try:
            # Paso 1: Ejecutar componente A
            self.ejecutar_componente_a()

            # Paso 2: Ejecutar componente B si A fue exitoso
            self.ejecutar_componente_b()

            # Paso 3: Procesar el resultado final
            self.procesar_resultado()

        except Exception as e:
            print(f"Ocurrió un error durante la ejecución: {e}")
        finally:
            print("Programa finalizado.")

    def ejecutar_componente_a(self):
        print("Ejecutando Componente A...")
        self.resultado = self.componente_a.ejecutar()

    def ejecutar_componente_b(self):
        print("Ejecutando Componente B...")
        self.resultado = self.componente_b.ejecutar(self.resultado)

    def procesar_resultado(self):
        print("Procesando resultado final...")
        # Aquí puedes aplicar la lógica de procesamiento final con self.resultado
        print(f"Resultado final: {self.resultado}")

class ComponenteA:
    def ejecutar(self):
        # Simular una operación que realiza el Componente A
        print("Componente A en ejecución")
        return "Resultado de A"

class ComponenteB:
    def ejecutar(self, input_data):
        # Simular una operación que realiza el Componente B con input_data
        print("Componente B en ejecución")
        return f"{input_data} modificado por B"

# Ejemplo de ejecución
if __name__ == "__main__":
    controlador = Controlador()
    controlador.iniciar_programa()

