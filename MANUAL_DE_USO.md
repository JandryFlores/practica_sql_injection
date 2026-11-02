MANUAL DE USO
Sistema de Simulación, Detección y Mitigación de SQL Injection
Descripción general del proyecto
La aplicación cuenta con una interfaz web desde la cual se puede acceder a los diferentes módulos del proyecto. Cada módulo cumple una función específica dentro del proceso de demostración y análisis.
Funcionamiento de los módulos
Módulo de inicio
Es la pantalla principal de la aplicación. Su función es presentar el propósito del sistema y facilitar el acceso a las demás secciones.
Módulo de inicio de sesión vulnerable
Este módulo representa una aplicación web que realiza consultas SQL mediante la concatenación directa de los datos introducidos en los campos de usuario y contraseña. Su funcionamiento permite demostrar cómo una consulta construida de manera insegura puede alterar el comportamiento esperado de una autenticación.
Procedimiento de funcionamiento:
1.	Seleccionar la pestaña Login vulnerable.
2.	Visualizar el formulario de inicio de sesión.
3.	Introducir los datos de prueba preparados para el laboratorio. Usuario: admin contraseña:  ' OR 1=1 --
4.	Presionar el botón de inicio de sesión.
5.	Observar la respuesta que proporciona la aplicación.
Resultado esperado:
El módulo permite comprobar el comportamiento de una autenticación vulnerable ante entradas manipuladas. En el escenario de demostración, puede evidenciarse que una consulta SQL insegura permite alterar la condición de validación.
3.3. Módulo de inicio de sesión seguro
Este módulo representa una autenticación que incorpora mecanismos para prevenir la inyección SQL.
A diferencia del módulo vulnerable, utiliza consultas parametrizadas para separar las instrucciones SQL de los datos proporcionados por el usuario.
También utiliza funciones de hash para proteger las contraseñas almacenadas.
Procedimiento de funcionamiento:
1.	Seleccionar la pestaña Login seguro.
2.	Visualizar el formulario de autenticación.
3.	Introducir un usuario y una contraseña de prueba. Usuario: admin contraseña:  ' OR 1=1 --
4.	Presionar el botón de inicio de sesión.
5.	Observar el resultado de la validación.
Resultado esperado:
•	Cuando las credenciales son correctas, el sistema permite el acceso.
•	Cuando las credenciales son incorrectas, el acceso es rechazado.
•	Cuando se introducen datos manipulados, estos se procesan como valores y no como instrucciones SQL.
Este módulo permite demostrar la importancia de utilizar consultas parametrizadas y mecanismos adecuados de protección de contraseñas.
Módulo de seguridad
Este apartado presenta información relacionada con los riesgos de SQL Injection y las medidas que permiten prevenir esta vulnerabilidad.
Su finalidad es complementar la parte práctica del proyecto con información sobre prevención y mitigación.
Módulo de escaneo de red
Este módulo permite comprobar el estado de determinados puertos TCP del equipo local.
Su funcionamiento se encuentra implementado en el archivo escaneo_red.py, que utiliza conexiones de prueba para determinar si los puertos configurados aceptan conexiones.
El análisis está limitado a la dirección local 127.0.0.1.
Procedimiento de funcionamiento:
1.	Seleccionar la pestaña Escaneo de red.
2.	Visualizar el panel de configuración.
3.	Comprobar que el equipo analizado sea 127.0.0.1.
4.	Presionar el botón Iniciar escaneo.
5.	Esperar a que termine el análisis.
6.	Consultar las estadísticas y la tabla de resultados.
