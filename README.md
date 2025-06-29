Calculadora de Rentabilidad Mensual
Este programa de consola, escrito en Python y orientado a objetos, permite a pequeños negocios y autónomos analizar la rentabilidad de los servicios que ofrecen. El usuario puede registrar servicios, sus materiales asociados y precios, y calcular de forma estimada si cubren costes fijos y alcanzan un sueldo deseado.

Características principales
Registro de servicios con nombre, materiales usados y precio de venta.

    Materiales con coste total y cálculo automático del coste por servicio según número de usos.

    Visualización detallada de cada servicio: materiales, costes, beneficio y recomendaciones.

    Modificación de servicios existentes para corregir datos.

    Cálculo del beneficio mensual total sumando todos los servicios registrados.

    Validaciones básicas para entradas numéricas.

    Código estructurado en clases para facilitar mantenimiento y ampliaciones futuras.

    Limpieza de pantalla automática: cada vez que accedes a una opción del menú o función, la pantalla se limpia para mantener la interfaz clara y evitar acumulación de texto.

Público objetivo
Autónomos, freelancers y emprendedores que ofrecen servicios (peluquería, tatuadores, formación, etc.).

    Cualquier persona que quiera analizar la rentabilidad de su oferta y optimizar precios.

Estructura actual del proyecto

    rentabilidad/
    ├── main.py           # Punto de entrada y menú principal
    ├── modelos.py        # Definición de la clase Servicio y sus métodos
    ├── registro.py       # Gestión de servicios (añadir, listar, modificar)
    ├── utils.py          # Funciones auxiliares, como limpieza de pantalla
    └── README.md         # Documentación del proyecto
    Nota: Los archivos calculo.py y datos.py han sido integrados dentro de la lógica orientada a objetos para simplificar el proyecto.

    Limpieza de pantalla
    Para mejorar la experiencia de usuario en consola, se implementó la función limpiar_pantalla() en el archivo utils.py. Esta función detecta el sistema operativo y ejecuta el comando correcto para limpiar la consola (cls en Windows, clear en Linux/macOS).

    Cada vez que se entra en un menú o submenú, o antes de pedir datos al usuario, se llama a esta función para evitar acumulación de texto y mantener la interfaz clara.

Ejemplo de uso:

    from utils import limpiar_pantalla

    def añadir_servicio():
        limpiar_pantalla()
        print("=== Añadir nuevo servicio ===")
        # resto de la función...

Cómo ejecutar
Asegúrate de tener Python 3.8 o superior instalado.

    Clona o descarga este repositorio.

    En la terminal, navega a la carpeta del proyecto y ejecuta:

    python main.py
    Sigue las instrucciones del menú para añadir, ver, modificar servicios y calcular beneficios.

Mejoras futuras
Persistencia de datos en archivos para conservar la información entre sesiones.

    Generación de informes en .txt o formatos más amigables.

    Implementación de interfaz gráfica para mayor usabilidad.

    Incorporar análisis más avanzados, como gastos fijos y recomendaciones automáticas de subida de precios.

Licencia
Este proyecto está bajo licencia MIT. Puedes usarlo, modificarlo y compartirlo libremente, siempre dando el crédito correspondiente.

Contribuciones
¿Tienes sugerencias o quieres colaborar? Abre un issue o haz un fork y envía un pull request. ¡Toda contribución es bienvenida!

Autor
RubenVC-dev
GitHub: https://github.com/RubenVC-dev
