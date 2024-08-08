# Calculadora de IMC

## Descripción
Esta aplicación de calculadora de Índice de Masa Corporal (IMC) permite a los usuarios ingresar su nombre, peso, altura, edad y sexo para calcular su IMC. La aplicación también permite guardar los datos en un archivo CSV con el nombre del usuario.

## Requisitos
- Python 3.x
- Tkinter
- PIL (Pillow)
- csv
- os

## Instalación
1. Asegúrese de tener Python 3.x instalado en su sistema.
2. Instale las bibliotecas necesarias utilizando pip:
    ```
    pip install tkinter
    pip install pillow
    ```

## Uso
1. Ejecutar el script de Python `calculadora_imc.py`.
2. Ingrese los detalles requeridos en los campos correspondientes:
    - Nombre
    - Peso (kg)
    - Altura (m)
    - Edad
    - Sexo (Hombre/Mujer)
3. Haga clic en el botón "Calcular IMC" para calcular su Índice de Masa Corporal.
4. El IMC calculado se mostrará en la aplicación.
5. Para guardar los datos, haga clic en el botón "Guardar Datos". Los datos se guardarán en un archivo CSV con el nombre del usuario.

## Estructura del Código
- `calcular_imc()`: Función para calcular el IMC utilizando los valores ingresados y mostrar el resultado.
- `guardar_datos()`: Función para guardar los datos del usuario en un archivo CSV.
- `configurar_cursor_hand2(event)`: Función para cambiar el cursor a `hand2` cuando el ratón entra en un botón.
- Interfaz de usuario creada con Tkinter y elementos organizados en un canvas con una imagen de fondo.

## Archivos
- `calculadora_imc.py`: Script principal de la aplicación.
- `IMSS-logo.png`: Imagen de fondo para el canvas.
- `imss_bot.jpeg`: Imagen para el botón de "Calcular IMC".

## Notas
- Asegúrese de que los archivos de imagen (`IMSS-logo.png` y `imss_bot.jpeg`) estén en el mismo directorio que el script `calculadora_imc.py` para que se carguen correctamente.
- El IMC se calcula utilizando una fórmula ajustada por sexo y edad:
    - `ks = 1.0` para hombres, `ks = 1.1` para mujeres.
    - `ka = 1 + 0.01 * (edad - 25)`.

¡Disfrute de su aplicación de calculadora de IMC!
