# PLAN MAESTRO DE CONTENIDO — TGA04
## Fundamentos de Computación para los Negocios
### IUB · Prof. Diego Domínguez Tapia · 2026

---

## 1. MARCO PEDAGÓGICO

### Framework GAME (RolGamificador.txt)
| Componente | Descripción |
|---|---|
| **G**uiar | Ruta de aprendizaje clara por semana, NeuroBiz como brújula |
| **A**rticular | Conectar conceptos de algoritmos con decisiones reales de negocio |
| **M**otivar | XP, badges, progresión de rango, narrativa corporativa inmersiva |
| **E**valuar | Quizzes autocalificables + prueba de escritorio + laboratorio Python |

### Taxonomía de Bloom por fase
- **Semanas 1-2 (RA1):** Recordar → Comprender → Aplicar básico
- **Semanas 3-9 (RA2):** Aplicar → Analizar → Crear (algoritmo propio)
- **Semana 11 (RA3):** Analizar → Evaluar
- **Semanas 12-15 (RA4-RA5):** Aplicar → Crear → Evaluar

### Analogías pedagógicas por RA
| RA | Analogía Vida Real | Analogía Gestión Empresarial |
|---|---|---|
| RA1 | La receta de cocina como algoritmo | El SOP (Procedimiento Operativo Estándar) de incorporación de empleados |
| RA2 selectivas | El semáforo (rojo/verde = si/no) | Política de crédito: "Si mora > 90 días → bloquear pedido" |
| RA2 repetitivas | La lavadora: repite ciclo MIENTRAS haya ropa | Procesar facturas pendientes MIENTRAS queden en bandeja |
| RA3 | Leer un libro paso a paso verificando que comprendes | Auditoría interna: revisar transacción por transacción |
| RA4-5 | Aprender a cocinar con un asistente de cocina (Colab) | Automatizar reportes con Python como lo hace un analista en McKinsey |

---

## 2. FUENTES Y MARCO DE REFERENCIA

### Bibliografía Curricular (IUB)
| Autor | Título | Relevancia 2026 |
|---|---|---|
| Cairó Battistutti & Guardati | Metodología de la programación (Alfaomega, 3ª ed.) | 🟢 VIGENTE para algoritmos y pseudocódigo |
| Deitel & Deitel | Cómo programar en Java (Pearson, 5ª ed.) | 🔴 HISTÓRICO — Java reemplazado por Python en educación de negocios; útil conceptualmente |
| Joyanes Aguilar | Fundamentos de programación (McGraw-Hill, 3ª ed.) | 🟡 EVOLUCIONADO — buena base teórica, actualizar ejemplos a Python |

### Fuentes Ampliadas (mejores escuelas del mundo)
| Fuente | Relevancia |
|---|---|
| **Harvard CS50 Business Professionals** (cs50.harvard.edu/business) | Referencia directa: "Abstract first, code later" / Visual tools y pseudocódigo como puente |
| **MIT 18.S191** — Computational Thinking (computationalthinking.mit.edu) | Resolver problemas reales antes de sintaxis; enfoque business+data |
| **WEF Future of Jobs Report 2025** | "Analytical thinking" = top skill; algorithmic thinking para no-programadores |
| **McKinsey Digital** — "We Are All Techies Now" (2023) | Python en finanzas, auditoría, ops; legibilidad de scripts como habilidad clave |
| **Deloitte Academies** (2024) | Upskilling administrativo: Python básico + automatización de reportes |
| **Wing, J.M. (2006)** — "Computational Thinking" (ACM CACM) | Artículo fundacional: CT como habilidad universal, no solo para ingenieros |
| **Google Colab** | Cloud IDE sin instalación; estándar en formación ágil |

### Marco de Relevancia de Contenidos
```
🟢 VIGENTE     — Fundamental en industria 2026. No necesita justificación adicional.
🟡 EVOLUCIONADO — Concepto válido, notación/herramienta cambió en industria. Señalar equivalente moderno.
🔴 HISTÓRICO   — Concepto presente en bibliografía pero rara vez usado en práctica actual.
                   Señalar EN QUÉ CONTEXTOS es útil aún (sistemas legados, Java empresarial, etc.)
```

---

## 3. HERRAMIENTAS DEL CURSO

### Stack Tecnológico
| Herramienta | Uso | Semanas | Por qué |
|---|---|---|---|
| **Google Colab** | IDE Python principal | 12-15 | Sin instalación, cloud, colaborativo, gratis |
| **Replit** | IDE alternativo | 12-15 | Si Colab no disponible; permite compartir código |
| **PSeInt (web)** | Editor pseudocódigo | 1-11 | Notación algorítmica estándar Colombia, genera diagrama |
| **Papel + lápiz** | Prueba de escritorio | 11 | La prueba manual entrena el debugger mental |
| **NotebookLM / Gemini** | Andamiaje IA | Todas | Asistente para resolver dudas de pseudocódigo y Python |

### Notación Colombiana → Equivalentes
| Notación TGA04 | Concepto | Python | JavaScript | Power Automate |
|---|---|---|---|---|
| SI-FSI | if simple | `if cond:` | `if (cond) {}` | Condition (True) |
| SI-SINO-FSI | if-else | `if / else:` | `if / else {}` | Condition (True/False) |
| DD-FDD | switch/match | `if/elif/else` o `match` (3.10+) | `switch/case` | Switch |
| MQ-FMQ | while | `while cond:` | `while (cond) {}` | Do Until |
| HH-FHH | do-while | `while True: ... if: break` | `do {} while(cond)` | Do (once) |
| PARA-FPARA | for (contador) | `for i in range(n):` | `for (let i=0...)` | Apply to each |

---

## 4. NARRATIVA GAMIFICADA — NEUROBIZ S.A.S.

### Contexto Corporativo
NeuroBiz S.A.S. es una startup de terapia cognitiva asistida por IA para personas neurodivergentes.
El estudiante es un **Consultor Junior de Datos** recién contratado.
Su misión: diseñar los algoritmos que van a automatizar los reportes de indicadores de gestión.

### Indicadores del Caso (variables del negocio)
```
sesiones_asistidas       → Integer  (cuántas sesiones se realizaron)
sesiones_fallidas        → Integer  (cuántas no se realizaron)
tasa_retencion           → Float    (% de pacientes que continúan)
indice_progreso          → Float    (puntaje de avance del paciente)
nombre_paciente          → String   (alfanumérica)
tipo_terapia             → String   ("cognitiva", "ocupacional", "fonoaudiología")
es_activo                → Boolean  (¿el paciente está activo?)
```

### Arco Narrativo por Semanas
| Semana | Misión NeuroBiz | Entregable Algoritmo |
|---|---|---|
| 1 | "NeuroBiz te da la bienvenida. Tu primera tarea: entender CÓMO funciona el proceso de admisión" | Diagrama de flujo del proceso de admisión (sin código) |
| 2 | "Define las variables del sistema. ¿Qué datos necesita NeuroBiz para medir su éxito?" | Declaración de variables + cálculo de tasa_retencion |
| 3 | "Un paciente llegó sin cita. ¿Debe ser atendido? Diseña el algoritmo de decisión simple" | SI-FSI: validar si paciente tiene cita activa |
| 4 | "Hay 3 tipos de terapia. El sistema debe clasificar automáticamente" | DD-FDD: clasificar tipo_terapia + asignar terapeuta |
| 6 | "Procesa la lista de sesiones del mes hasta que no queden por procesar" | MQ-FMQ: acumular sesiones_asistidas |
| 7 | "El sistema de captura de datos siempre debe pedir MÍNIMO una sesión de ingreso" | HH-FHH: validar entrada de datos con al menos 1 iteración |
| 8 | "Calcula el índice promedio de 10 pacientes del mes" | PARA-FPARA: sumar indice_progreso / 10 |
| 9 | "Genera el reporte completo del mes: filtra, suma, clasifica" | Algoritmo completo: selectivas + repetitivas anidadas |
| 11 | "Alguien entregó el algoritmo del mes. Hay un bug. ¡Encuéntralo!" | Prueba de escritorio sobre algoritmo con error |
| 12 | "Es hora de codificar. Abre Colab: tu primer algoritmo en Python" | Traducir pseudocódigo de sem 2 → Python |
| 13 | "Codifica la decisión triple de tipos de terapia + el ciclo del mes" | Python: if/elif + for loop |
| 14 | "Entrega el sistema completo de NeuroBiz en Python" | Proyecto integrador: programa Python funcional |
| 15 | "El sistema tiene 3 bugs en producción. ¡Corrígelos antes del lanzamiento!" | Debugging en Colab: identificar y corregir 3 errores |

### Rangos y Badges
| Rango | XP Requerido | Badge | Analogía Corporativa |
|---|---|---|---|
| 🔵 Aprendiz de Datos | 0-99 XP | `aprendiz.png` | Pasante recién llegado |
| 🟢 Analista Junior | 100-249 XP | `analista.png` | Analista de operaciones |
| 🟡 Consultor de Procesos | 250-449 XP | `consultor.png` | Consultor de datos NeuroBiz |
| 🟠 Arquitecto de Algoritmos | 450-649 XP | `arquitecto.png` | Líder técnico de área |
| 🔴 CTO de NeuroBiz | 650+ XP | `cto.png` | Director de Tecnología |

### XP por Actividad
| Tipo | XP | Descripción |
|---|---|---|
| Asistencia | 10 XP | Registro de CC al iniciar la sesión |
| Quiz conceptual (correcto) | 5-8 XP | 5 preguntas por semana |
| Ejercicio pseudocódigo | 15-20 XP | Resolver algoritmo en PSeInt o papel |
| Laboratorio Python | 25-30 XP | Colab notebook completado |
| Misión NeuroBiz | 20-25 XP | Entregable del caso de estudio |
| Bono por racha | +5 XP | 3 semanas consecutivas con quiz > 80% |

---

## 5. MAPA SEMANA A SEMANA

### SEMANA 1 — Algoritmos y Pensamiento Computacional
**RA1 | CE1-CE2 | Bloom: Recordar → Comprender**

**Título:** "¿Qué es un algoritmo? Pensando como una computadora"

**Relevancia:** 🟢 VIGENTE
*"Algorithmic thinking is one of the top 5 competencies for 2025" — WEF Future of Jobs 2025*
*"We start with computational thinking before any code" — Harvard CS50 Business*

**Contenidos (4h presenciales):**
- Conceptos: dato, información, software, sistemas de información (45 min)
- Algoritmo: definición, propiedades (finito, preciso, efectivo) (45 min)
- Representación: diagrama de flujo (símbolos básicos: proceso, decisión, inicio/fin) (60 min)
- Introducción a pseudocódigo: notación de Cairó (30 min)

**Analogías:**
- 🏠 VIDA REAL: La receta de ceviche. Ingredientes = datos. Instrucciones = algoritmo. Plato servido = información procesada.
- 💼 NEGOCIO: El SOP de incorporación de empleado nuevo: "SI es primer día → entregar credencial. Llevar a RR.HH. Asignar computador. Inducción..."

**Nota de relevancia para el docente:**
> El concepto de "dato vs información" es más relevante que nunca en la era del Big Data y la IA. En las empresas con Business Intelligence (Power BI, Tableau), los empleados NECESITAN distinguir entre datos crudos y KPIs procesados. Citar: "McKinsey estima que 72% de decisiones gerenciales aún se hacen con datos mal estructurados" (McKinsey Global Survey 2023).

**Actividad NeuroBiz:**
> NeuroBiz tiene estos registros: `[{"fecha": "2026-01-15", "paciente": "Ana García", "sesion": "asistida"}]`. ¿Es esto un dato o información? ¿Qué pregunta de negocio responde?

**Quiz Semana 1 (5 preguntas, 5 XP c/u):**
1. ¿Qué propiedad de un algoritmo garantiza que siempre termina? → Finitud
2. ¿Cuál es la diferencia entre dato e información? → Dato=crudo, información=procesada
3. ¿Qué símbolo en un diagrama de flujo representa una decisión? → Rombo ◇
4. NeuroBiz tiene 450 registros de sesiones. ¿Esto es dato o información? → Dato
5. ¿Cuál es el primer paso para resolver un problema algorítmicamente? → Entender el problema / análisis

**XP Semana 1:** 10 (asistencia) + 25 (quiz) + 20 (misión NeuroBiz) = **55 XP**

---

### SEMANA 2 — Variables, Tipos y Operadores
**RA1 | CE1-CE2 | Bloom: Comprender → Aplicar**

**Título:** "Las variables: los contenedores del algoritmo"

**Relevancia:** 🟢 VIGENTE
*"Variables are the foundation of every spreadsheet formula, database field, and Python script" — MIT 18.S191*

**Contenidos (4h presenciales):**
- Tipos de variables: numéricas enteras, numéricas reales, alfanuméricas, lógicas (60 min)
- Operadores matemáticos (+, -, *, /, MOD, DIV) (45 min)
- Operadores relacionales (>, <, >=, <=, =, ≠) (30 min)
- Operadores lógicos (AND, OR, NOT) (30 min)
- Operadores estadísticos básicos (SUMA, PROMEDIO, CONTEO) (15 min)

**Analogías:**
- 🏠 VIDA REAL: Las variables son cajones etiquetados en tu escritorio. Cada cajón tiene un nombre y guarda un tipo de cosa (documentos, dinero, llaves). No puedes guardar llaves en el cajón de documentos.
- 💼 NEGOCIO: Los KPIs de un tablero gerencial. `tasa_retencion` = cajón que guarda %, no texto. El sistema ERP de NeuroBiz necesita saber qué tipo de dato guarda cada campo.

**Nota de relevancia para el docente:**
> Las variables de tipo Boolean (lógico: Verdadero/Falso) son la base de TODOS los filtros en Excel, Power BI, y SQL. Cuando un gerente filtra "pacientes activos = SÍ", está usando una variable booleana. Este concepto mapea directamente a Power Automate y cualquier herramienta de automatización empresarial.
> Sobre operadores estadísticos: aunque el currículo los menciona brevemente, son la base de las fórmulas PROMEDIO, SUMA, CONTARA en Excel. Fortalecer este puente.

**Actividad NeuroBiz:**
> Define en pseudocódigo las variables para el sistema NeuroBiz:
> ```
> ENTERO sesiones_asistidas
> ENTERO sesiones_fallidas  
> REAL tasa_retencion
> REAL indice_progreso
> CADENA nombre_paciente
> LÓGICO es_activo
> ```
> Luego calcula: `tasa_retencion ← (sesiones_asistidas / (sesiones_asistidas + sesiones_fallidas)) × 100`

**Nota sobre pseudocódigo (Cairó vs estándar):**
> El símbolo de asignación en Cairó es `←`. En Python es `=`. En muchos editores se usa `:=`. El concepto es el mismo: "poner un valor en la variable".

**Quiz Semana 2 (5 preguntas):**
1. ¿Qué tipo de variable usarías para guardar el % de retención de pacientes? → Real/Flotante
2. ¿Qué operador verifica si dos valores son iguales en la condición de un algoritmo? → =
3. `NOT (Verdadero AND Falso)` = ? → Verdadero
4. Si `sesiones_asistidas = 45` y `sesiones_fallidas = 5`, ¿cuánto es `tasa_retencion`? → 90%
5. ¿Cuál es la diferencia entre DIV y MOD? → DIV=cociente entero, MOD=residuo

**XP Semana 2:** 10 + 25 + 20 = **55 XP** (acum: 110)

---

### SEMANA 3 — Primitivas Selectivas: SI-FSI
**RA2 | CE1-CE2 | Bloom: Aplicar → Analizar**

**Título:** "El primer if: enseñar al algoritmo a tomar decisiones simples"

**Relevancia:** 🟢 VIGENTE
*"Conditional logic is the backbone of every business rule engine, Excel formula, and Power Automate flow" — Microsoft Power Platform docs*

**Contenidos (4h presenciales):**
- Estructura de control: concepto de decisión en algoritmos (30 min)
- Primitiva SI-FSI: sintaxis, diagrama de flujo, pseudocódigo (60 min)
- Diseño de condiciones booleanas bien formadas (45 min)
- Ejercicios con situaciones de negocio (45 min)

**Sintaxis SI-FSI (Cairó):**
```
SI (condición) ENTONCES
   instrucciones
FSI
```
**Equivalente Python:** `if condicion:`
**Equivalente Excel:** `=SI(condicion, verdadero, "")` *(solo parte verdadera)*

**🔴 NOTA HISTÓRICA — Diagramas de flujo:**
> Los diagramas de flujo tradicionales (con las figuras de Cairó) no se usan en documentación empresarial moderna. La industria usa **BPMN 2.0** (Business Process Model and Notation) y **UML Activity Diagrams** para modelar procesos. Sin embargo, los diagramas de flujo son excelentes para APRENDER la lógica antes de codificar. Harvard CS50 usa "pseudocódigo + scratch" exactamente para este puente.
> **Escenario útil:** Sistemas legados (bancos, gobierno colombiano, ERPs de manufactura) aún tienen documentación en diagramas de flujo tradicionales.

**Analogías:**
- 🏠 VIDA REAL: El detector de humo. SI hay humo → activar alarma. (No hace nada si no hay humo)
- 💼 NEGOCIO: Política de descuento: "SI el cliente tiene más de 2 años de antigüedad → aplicar descuento del 10%"

**Actividad NeuroBiz:**
> ```
> ALGORITMO ValidarCita
> VARIABLES: tiene_cita: LÓGICO, nombre: CADENA
> INICIO
>   LEER nombre
>   LEER tiene_cita
>   SI (tiene_cita = VERDADERO) ENTONCES
>     ESCRIBIR nombre + " puede ser atendido hoy"
>   FSI
> FIN
> ```
> Misión: Extender el algoritmo para también verificar si `es_activo = VERDADERO`

**Quiz Semana 3 (5 preguntas):**
1. ¿Cuándo se ejecuta el bloque dentro de SI-FSI? → Solo cuando la condición es VERDADERA
2. ¿Qué símbolo representa SI-FSI en un diagrama de flujo? → Rombo con una salida a la instrucción
3. Si `sesiones_asistidas >= 30`, ¿qué condición verifica que un terapeuta cumplió su cuota mensual? → SI (sesiones_asistidas >= 30) ENTONCES ...
4. ¿Cómo se escribe SI-FSI en Python? → `if condicion:`
5. ¿Cuál es el error en: `SI (tasa_retencion > 90)` si tasa_retencion = "noventa"? → Tipo incorrecto: alfanumérico vs numérico

**XP Semana 3:** 10 + 25 + 20 = **55 XP** (acum: 165)

---

### SEMANA 4 — Primitivas Selectivas: SI-SINO-FSI y DD-FDD
**RA2 | CE1-CE2 | Bloom: Aplicar → Analizar**

**Título:** "Decisiones con múltiples caminos: el menú del negocio"

**Relevancia:** 🟡 EVOLUCIONADO (SI-SINO: 🟢 VIGENTE | DD-FDD: 🟡 EVOLUCIONADO)

**Contenidos (4h presenciales):**
- SI-SINO-FSI: sintaxis, pseudocódigo, diagrama (60 min)
- DD-FDD (Decisión múltiple): sintaxis, usos (60 min)
- Comparación: cuándo usar SI-SINO vs DD-FDD (30 min)
- Laboratorio: caso NeuroBiz (30 min)

**Sintaxis SI-SINO-FSI:**
```
SI (condición) ENTONCES
   instrucciones_verdadero
SINO
   instrucciones_falso
FSI
```

**Sintaxis DD-FDD:**
```
DD (variable)
  CASO "valor1": instrucciones_1
  CASO "valor2": instrucciones_2
  DEFECTO: instrucciones_por_defecto
FDD
```

**🟡 NOTA EVOLUCIONADA — DD-FDD / Switch-Case:**
> **En la bibliografía:** DD-FDD (Decisión Doble/Final DD) es la notación de Cairó para `switch/case`.
> **En la industria 2026:**
> - Java/C/JavaScript: `switch(variable) { case "valor": ... break; }`
> - Python 3.10+: `match variable: case "valor": ...`
> - Python < 3.10 (lo más común en Colombia): se simula con `if/elif/else`
> - Power Automate: "Switch" en condiciones
> **¿Es obsoleto el concepto?** NO. Es fundamental para menús, clasificaciones, routing de flujos.
> **¿Es obsoleta la notación DD-FDD?** Sí en industria, pero útil como puente conceptual.

**Analogías:**
- 🏠 VIDA REAL: El menú de un restaurante. No solo "SI pide pollo → servir pollo", sino múltiples opciones.
- 💼 NEGOCIO: Sistema de bonificaciones por rango de ventas. Caso ventas < 50M → bono básico. Caso 50M-100M → bono intermedio. Caso > 100M → bono ejecutivo.

**Actividad NeuroBiz:**
> ```
> ALGORITMO ClasificarTerapia
> VARIABLES: tipo_terapia: CADENA, terapeuta: CADENA
> INICIO
>   LEER tipo_terapia
>   DD (tipo_terapia)
>     CASO "cognitiva":    terapeuta ← "Dra. Mendoza"
>     CASO "ocupacional":  terapeuta ← "Dr. García"
>     CASO "fonoaudiología": terapeuta ← "Dra. Rivas"
>     DEFECTO: terapeuta ← "Sin asignar"
>   FDD
>   ESCRIBIR "Terapeuta asignado: " + terapeuta
> FIN
> ```

**Quiz Semana 4 (5 preguntas):**
1. ¿Cuál es la diferencia principal entre SI-FSI y SI-SINO-FSI? → SINO ejecuta cuando la condición es FALSA
2. ¿Cuándo es mejor usar DD-FDD que SI-SINO-FSI anidado? → Cuando hay múltiples opciones de un mismo valor
3. ¿En Python, cómo se escribe DD-FDD? → `if/elif/else` o `match/case` (Python 3.10+)
4. Si `tipo_terapia = "COGNITIVA"` y el caso es `"cognitiva"`, ¿qué ocurre? → No coincide (mayúsculas/minúsculas)
5. El DEFECTO en DD-FDD equivale a ¿qué en Python? → `else:` en una cadena if/elif

**XP Semana 4:** 10 + 25 + 20 = **55 XP** (acum: 220)

---

### SEMANA 5 — 🎯 PARCIAL CORTE 1
**Evaluación acumulativa RA1 + RA2 (Selectivas)**
*No se genera material HTML de semana — solo notas del profesor*

**Contenido evaluado:**
- Conceptos: dato, información, algoritmo, variables (RA1)
- Operadores: matemáticos, relacionales, lógicos (RA1)
- SI-FSI, SI-SINO-FSI, DD-FDD (RA2 parcial)

---

### SEMANA 6 — Primitivas Repetitivas: MQ-FMQ (while)
**RA2 | CE1-CE2 | Bloom: Aplicar → Analizar**

**Título:** "El primer ciclo: repitiendo tareas como una máquina"

**Relevancia:** 🟢 VIGENTE
*"The while loop is fundamental in batch processing, data ingestion pipelines, and business automation" — Python for Data Analysis, Wes McKinney*

**Contenidos (4h presenciales):**
- ¿Por qué necesitamos ciclos? Problema de repetición manual (30 min)
- Estructura MQ-FMQ: condición de entrada, cuerpo, actualización (60 min)
- Riesgo: ciclos infinitos y cómo evitarlos (30 min)
- Variables acumuladoras y contadoras (60 min)

**Sintaxis MQ-FMQ:**
```
MQ (condición) HQ
   instrucciones
   actualizar_condición
FMQ
```

**Equivalente Python:** `while condicion:`

**Analogías:**
- 🏠 VIDA REAL: La lavadora. MIENTRAS haya ropa sucia → lavar ciclo. (Si no hay ropa desde el inicio, ni siquiera arranca)
- 💼 NEGOCIO: Procesar correos en bandeja. MIENTRAS haya correos sin leer → abrir y marcar como leído. Si ya están todos leídos, el proceso no inicia.

**🟢 NOTA VIGENTE:**
> MQ-FMQ es quizás el ciclo más relevante para perfiles administrativos porque mapea directamente a:
> - Bucles de procesamiento de archivos (CSV row by row)
> - Polling en APIs (seguir consultando MIENTRAS no llegue la respuesta)
> - Automatizaciones con Power Automate: "Do Until" condition
> Citar: McKinsey reporta que automatizar flujos de aprobación con ciclos condicionales reduce tiempos de proceso en 40%.

**Actividad NeuroBiz:**
> ```
> ALGORITMO ContarSesionesMes
> VARIABLES: total_sesiones: ENTERO, sesion_actual: ENTERO, contador: ENTERO
> INICIO
>   total_sesiones ← 0
>   contador ← 1
>   MQ (contador <= 30) HQ
>     LEER sesion_actual
>     total_sesiones ← total_sesiones + sesion_actual
>     contador ← contador + 1
>   FMQ
>   ESCRIBIR "Total sesiones del mes: " + total_sesiones
> FIN
> ```
> Misión: ¿Qué pasa si en vez de 30 días, el mes tiene días variables? Adaptarlo.

**Quiz Semana 6 (5 preguntas):**
1. ¿Cuándo se evalúa la condición de MQ-FMQ? → ANTES de cada iteración
2. ¿Qué ocurre si la condición es FALSA desde el inicio? → El cuerpo no se ejecuta ni una vez
3. ¿Cuál es el error clásico en MQ-FMQ? → Olvidar actualizar la variable de condición (ciclo infinito)
4. Una variable acumuladora se inicializa en __ → 0
5. `contador ← contador + 1` es una operación de __ → Conteo / incremento

**XP Semana 6:** 10 + 25 + 20 = **55 XP** (acum: 275)

---

### SEMANA 7 — Primitivas Repetitivas: HH-FHH (do-while)
**RA2 | CE1-CE2 | Bloom: Aplicar → Analizar**

**Título:** "El ciclo que siempre arranca: Haga al menos una vez"

**Relevancia:** 🟡 EVOLUCIONADO

**Contenidos (4h presenciales):**
- Diferencia fundamental con MQ-FMQ: post-condición vs pre-condición (45 min)
- Sintaxis HH-FHH (60 min)
- Casos de uso: validación de entrada, menús de aplicación (60 min)
- Simulación en Python: `while True: ... if cond: break` (15 min)

**Sintaxis HH-FHH:**
```
HH
   instrucciones
   LEER variable_condicion
FHH (condición_de_parada)
```

**🟡 NOTA EVOLUCIONADA — HH-FHH (do-while):**
> **En bibliografía:** HH-FHH (Haga-Hasta) ejecuta el cuerpo ANTES de verificar la condición.
> **En industria 2026:**
> - Java / JavaScript / C#: `do { } while (condicion)` — existe nativamente
> - Python: **NO existe** do-while. Se simula con `while True: ... if condicion: break`
> - Por qué importa igual: garantiza AL MENOS UNA ejecución. Útil en:
>   - Menús de aplicaciones (el menú siempre se muestra una vez)
>   - Validación de formularios (siempre pides los datos, luego verificas)
>   - Sistemas de reintentos de pago (intenta al menos una vez)
> **Escenarios de uso actual:** Aplicaciones Java empresariales (bancos, ERP SAP aún usan Java), Android nativo.

**Analogías:**
- 🏠 VIDA REAL: Probar si la comida necesita sal. HACES la prueba (al menos una), HASTA que esté bien sazonada.
- 💼 NEGOCIO: El sistema de captura de datos del paciente. SIEMPRE se muestra el formulario de ingreso. El paciente llena HASTA que todos los campos estén completos.

**Actividad NeuroBiz:**
> ```
> ALGORITMO CapturarDatosPaciente
> VARIABLES: nombre: CADENA, sesiones: ENTERO
> INICIO
>   HH
>     ESCRIBIR "Ingrese nombre del paciente:"
>     LEER nombre
>     ESCRIBIR "Ingrese número de sesiones:"
>     LEER sesiones
>   FHH (nombre ≠ "" Y sesiones > 0)
>   ESCRIBIR "Datos guardados para: " + nombre
> FIN
> ```

**Quiz Semana 7 (5 preguntas):**
1. ¿Cuántas veces mínimo ejecuta su cuerpo HH-FHH? → Al menos 1 vez
2. ¿En qué se diferencia de MQ-FMQ? → La condición se evalúa DESPUÉS del cuerpo
3. ¿Cómo se simula do-while en Python? → `while True: ... if condicion: break`
4. ¿Para qué sirve un menú con HH-FHH? → Mostrar opciones al menos una vez, repetir hasta que elija "salir"
5. ¿Existe `do-while` en Python nativamente? → No

**XP Semana 7:** 10 + 25 + 20 = **55 XP** (acum: 330)

---

### SEMANA 8 — Primitivas Repetitivas: PARA-FPARA (for)
**RA2 | CE1-CE2 | Bloom: Aplicar → Analizar**

**Título:** "El ciclo del contador: procesando listas como un analista"

**Relevancia:** 🟢 VIGENTE
*"The for loop with enumeration over data collections is the most common construct in data analysis pipelines" — Python for Data Analysis, O'Reilly*

**Contenidos (4h presenciales):**
- PARA-FPARA: cuándo usarlo vs MQ-FMQ (30 min)
- Sintaxis: variable contador, inicio, fin, paso (60 min)
- Iteración sobre listas/colecciones (45 min)
- Laboratorio: calcular KPIs de un lote de pacientes (45 min)

**Sintaxis PARA-FPARA:**
```
PARA contador DESDE inicio HASTA fin PASO incremento HQ
   instrucciones
FPARA
```

**Equivalente Python:** `for i in range(inicio, fin+1, paso):`
**Excel equivalente conceptual:** "Rellenar hacia abajo" en una columna con fórmula

**🟢 NOTA VIGENTE:**
> PARA-FPARA (for loop) es el constructo más usado en análisis de datos:
> - `for fila in dataframe:` en pandas
> - `for celda in rango:` en Excel VBA
> - `for cada elemento in lista:` en Power Query M
> - `Apply to each` en Power Automate
> Citar: "Python for loops over DataFrames are the entry point for every data analyst in 2026" — Google Data Analytics Certificate

**Analogías:**
- 🏠 VIDA REAL: Contar los asistentes a una reunión. PARA cada persona en la sala, DE 1 HASTA N → incrementar conteo.
- 💼 NEGOCIO: Calcular nómina. PARA cada empleado, DE 1 HASTA total_empleados → salario += horas_trabajadas × tarifa_hora.

**Actividad NeuroBiz:**
> ```
> ALGORITMO PromedioPacientesMes
> VARIABLES: i: ENTERO, progreso_actual: REAL
>            suma_progreso: REAL, promedio: REAL
> INICIO
>   suma_progreso ← 0
>   PARA i DESDE 1 HASTA 10 PASO 1 HQ
>     LEER progreso_actual
>     suma_progreso ← suma_progreso + progreso_actual
>   FPARA
>   promedio ← suma_progreso / 10
>   ESCRIBIR "Índice promedio del mes: " + promedio
> FIN
> ```

**Quiz Semana 8 (5 preguntas):**
1. ¿Cuándo prefieres PARA-FPARA sobre MQ-FMQ? → Cuando sabes exactamente cuántas veces repetir
2. `PARA i DESDE 1 HASTA 5 PASO 1`: ¿cuántas iteraciones? → 5
3. ¿Cómo se escribe en Python? → `for i in range(1, 6):`
4. ¿Qué es el PASO en PARA-FPARA? → El incremento del contador por iteración
5. ¿Qué hace `PARA i DESDE 10 HASTA 1 PASO -1`? → Cuenta regresiva de 10 a 1

**XP Semana 8:** 10 + 25 + 20 = **55 XP** (acum: 385)

---

### SEMANA 9 — Algoritmos Complejos: Combinando Estructuras
**RA2 | CE1-CE2 | Bloom: Analizar → Crear**

**Título:** "El algoritmo del mes: el reporte completo de NeuroBiz"

**Relevancia:** 🟢 VIGENTE

**Contenidos (4h presenciales):**
- Selectivas dentro de repetitivas (SI dentro de PARA/MQ) (45 min)
- Repetitivas anidadas (PARA dentro de PARA) (45 min)
- Diseño top-down: descomponer el problema antes de codificar (30 min)
- Laboratorio integrador: reporte de KPIs NeuroBiz (60 min)

**Nota pedagógica:**
> Esta semana consolida RA2 completo. El objetivo es que el estudiante DISEÑE un algoritmo propio, no solo complete uno dado. Bloom nivel: Crear.
> Sugerencia: trabajo en parejas. Un estudiante dicta el algoritmo en lenguaje natural, el otro lo traduce a pseudocódigo. Luego invierten roles.

**Actividad NeuroBiz (misión mayor):**
> ```
> ALGORITMO ReporteMensualNeuroBiz
> VARIABLES: i: ENTERO, sesiones_asistidas: ENTERO
>            sesiones_fallidas: ENTERO, tasa: REAL
>            total_efectivas: ENTERO, alertas: ENTERO
> INICIO
>   total_efectivas ← 0
>   alertas ← 0
>   PARA i DESDE 1 HASTA 20 HQ
>     LEER sesiones_asistidas
>     LEER sesiones_fallidas
>     tasa ← sesiones_asistidas / (sesiones_asistidas + sesiones_fallidas) * 100
>     SI (tasa >= 80) ENTONCES
>       total_efectivas ← total_efectivas + 1
>     SINO
>       alertas ← alertas + 1
>     FSI
>   FPARA
>   ESCRIBIR "Terapeutas con buen rendimiento: " + total_efectivas
>   ESCRIBIR "Terapeutas que requieren apoyo: " + alertas
> FIN
> ```

**Quiz Semana 9 (5 preguntas):**
1. ¿Qué significa "anidar" estructuras de control? → Poner una estructura dentro de otra
2. ¿Cuántas iteraciones totales tiene PARA i DESDE 1 HASTA 3 con PARA j DESDE 1 HASTA 3 anidado? → 9
3. ¿Qué estrategia se recomienda para diseñar algoritmos complejos? → Top-down: dividir en subproblemas
4. ¿Puedes poner un SI-SINO-FSI dentro de un MQ-FMQ? → Sí, siempre que la indentación sea correcta
5. En el algoritmo de NeuroBiz, ¿qué variable acumula los terapeutas con problemas? → alertas

**XP Semana 9:** 10 + 25 + 25 (misión mayor) = **60 XP** (acum: 445)

---

### SEMANA 10 — 🎯 PARCIAL CORTE 2
**Evaluación acumulativa RA2 completo (Selectivas + Repetitivas)**
*No se genera material HTML de semana*

---

### SEMANA 11 — Pruebas de Escritorio (RA3)
**RA3 | CE1-CE2 | Bloom: Analizar → Evaluar**

**Título:** "La auditoría del algoritmo: encontrar el bug antes de codificar"

**Relevancia:** 🟡 EVOLUCIONADO

**Contenidos (4h presenciales):**
- ¿Qué es una prueba de escritorio? (30 min)
- Tabla de seguimiento: columnas = variables, filas = pasos (60 min)
- Ejecutar paso a paso con datos de prueba (60 min)
- Identificar errores lógicos vs errores de sintaxis (30 min)

**🟡 NOTA EVOLUCIONADA — Prueba de escritorio:**
> **En bibliografía:** La prueba de escritorio es trazar manualmente el estado de las variables paso a paso sin computador.
> **En industria 2026:**
> - Los IDEs modernos tienen **debuggers** que hacen esto automáticamente: VS Code, PyCharm, IDLE
> - Las pruebas unitarias (pytest, JUnit) automatizan la verificación de resultados esperados
> - En Google Colab: `print(variable)` en cada paso o usar el debugging step-by-step
> **¿Por qué enseñarla igual?** La prueba de escritorio ENTRENA el pensamiento algorítmico. Es el equivalente a aprender a conducir primero en un estacionamiento vacío antes de la autopista.
> Citar: "Manual tracing teaches you to think like a debugger before you have a debugger" — Harvard CS50 Week 2 lecture notes

**Analogías:**
- 🏠 VIDA REAL: Resolver el cubo de Rubik paso a paso, anotando la posición de cada pieza antes y después de cada movimiento.
- 💼 NEGOCIO: La auditoría interna. El auditor revisa cada transacción del libro contable, una por una, para encontrar la inconsistencia. La prueba de escritorio ES la auditoría del código.

**Actividad NeuroBiz:**
> Se entrega un algoritmo con 2 bugs lógicos. El estudiante debe:
> 1. Construir la tabla de prueba de escritorio
> 2. Identificar en qué paso el valor de una variable es incorrecto
> 3. Señalar la línea del error y proponer la corrección

**Quiz Semana 11 (5 preguntas):**
1. ¿Qué columnas tiene una tabla de prueba de escritorio? → Una columna por variable + columna de paso/instrucción
2. ¿Qué tipo de error detecta mejor la prueba de escritorio? → Errores lógicos (no de sintaxis)
3. ¿Cuál es el equivalente moderno de la prueba de escritorio? → Debugger del IDE / unit tests
4. Si en paso 3 `suma = 15` pero el resultado esperado era 10, ¿qué buscarías? → El paso donde se hizo la suma incorrecta
5. ¿Qué es un "caso de prueba"? → Un conjunto específico de valores de entrada con el resultado esperado

**XP Semana 11:** 10 + 25 + 20 = **55 XP** (acum: 500)

---

### SEMANA 12 — Google Colab + Python: Traduciendo Pseudocódigo
**RA4 | CE1-CE2 | Bloom: Aplicar**

**Título:** "De pseudocódigo a Python: bienvenido al IDE"

**Relevancia:** 🟢 VIGENTE
*"Python is the most in-demand programming language for business analysts in 2025" — LinkedIn Jobs Report 2025*
*"Google Colab removes all barriers to entry for non-technical learners" — Google AI Education*

**Contenidos (4h presenciales):**
- Google Colab: interfaz, notebook, ejecutar celda (45 min)
- Python: variables y tipos (`int`, `float`, `str`, `bool`) (30 min)
- Python: operadores = pseudocódigo (comparar lado a lado) (30 min)
- Traducción: algoritmo de NeuroBiz semana 2 → Python (75 min)

**Tabla comparativa pseudocódigo → Python:**
```
Pseudocódigo            →  Python
ENTERO n ← 0           →  n = 0
REAL tasa ← 0.0        →  tasa = 0.0
CADENA nombre ← ""     →  nombre = ""
LÓGICO activo ← FALSO  →  activo = False
LEER valor             →  valor = input("Ingrese valor: ")
ESCRIBIR resultado     →  print(resultado)
←                      →  =  (asignación)
MOD                    →  %
DIV                    →  //
```

**🔴 NOTA HISTÓRICA — Java (bibliografía Deitel):**
> La bibliografía incluye "Cómo programar en Java" (Deitel). Java fue el lenguaje de referencia en Colombia para programación universitaria hasta ~2015.
> **¿Por qué Python en cambio?**
> - Python tiene sintaxis 3-5x más limpia que Java para principiantes (no requiere tipos declarados, no requiere `public static void main`)
> - Harvard CS50, MIT 18.S191, Wharton Business Analytics → todos migraron a Python
> - Google, NASA, McKinsey Analytics → Python es el estándar para análisis de datos
> - Java sigue siendo relevante para Android, sistemas empresariales (SAP, Oracle), banca
> **Uso actual de Java en Colombia:** Proyectos legados en bancos (Bancolombia, Davivienda TI), aplicaciones Android nativas, algunos sistemas gubernamentales DIAN/RNEC.

**Actividad NeuroBiz (Colab):**
```python
# NeuroBiz — Algoritmo Semana 2 en Python
sesiones_asistidas = int(input("Sesiones asistidas: "))
sesiones_fallidas = int(input("Sesiones fallidas: "))

total = sesiones_asistidas + sesiones_fallidas
tasa_retencion = (sesiones_asistidas / total) * 100

print(f"Tasa de retención: {tasa_retencion:.1f}%")
```

**Quiz Semana 12 (5 preguntas):**
1. ¿Cómo se ejecuta una celda en Google Colab? → Shift+Enter o click en ▶
2. `int("45")` convierte el texto "45" en ¿qué? → Número entero 45
3. ¿Cuál es el equivalente de `ESCRIBIR` en Python? → `print()`
4. ¿Cuál es el equivalente de `LEER` en Python? → `input()`
5. ¿Por qué Python en vez de Java para este curso? → Más simple, estándar actual en data analytics y business intelligence

**XP Semana 12:** 10 + 25 + 30 (primer lab Colab) = **65 XP** (acum: 565)

---

### SEMANA 13 — Python: Condicionales y Ciclos
**RA4 | CE1-CE2 | Bloom: Aplicar → Analizar**

**Título:** "Python empresarial: decisiones y repeticiones como un analista"

**Relevancia:** 🟢 VIGENTE

**Contenidos (4h presenciales):**
- `if / elif / else` en Python (comparar con SI/SINO/DD-FDD) (60 min)
- `while` en Python (comparar con MQ-FMQ) (45 min)
- `for i in range()` en Python (comparar con PARA-FPARA) (45 min)
- Laboratorio integrador: KPIs de NeuroBiz con Python (30 min)

**Código NeuroBiz Semana 13:**
```python
# Clasificar tipo de terapia (DD-FDD → if/elif/else)
tipo_terapia = input("Tipo de terapia: ").lower()

if tipo_terapia == "cognitiva":
    terapeuta = "Dra. Mendoza"
elif tipo_terapia == "ocupacional":
    terapeuta = "Dr. García"
elif tipo_terapia == "fonoaudiología":
    terapeuta = "Dra. Rivas"
else:
    terapeuta = "Sin asignar"

print(f"Terapeuta: {terapeuta}")

# Calcular promedio de sesiones (PARA-FPARA → for)
suma = 0
for i in range(10):
    s = int(input(f"Sesiones paciente {i+1}: "))
    suma += s

promedio = suma / 10
print(f"Promedio de sesiones: {promedio:.1f}")
```

**Quiz Semana 13 (5 preguntas):**
1. ¿Cómo se escribe `SI-SINO-FSI` en Python? → `if ... else:`
2. ¿Qué produce `range(1, 6)`? → Los números 1, 2, 3, 4, 5
3. ¿Cuál es el equivalente Python de `MQ (contador < 10) HQ`? → `while contador < 10:`
4. `suma += valor` es equivalente a → `suma = suma + valor`
5. ¿Por qué usar `.lower()` al comparar strings? → Para ignorar diferencias de mayúsculas/minúsculas

**XP Semana 13:** 10 + 25 + 30 = **65 XP** (acum: 630)

---

### SEMANA 14 — Laboratorio Integrador Python (RA4)
**RA4 | CE1-CE2 | Bloom: Crear → Analizar**

**Título:** "El sistema NeuroBiz en producción: código completo"

**Relevancia:** 🟢 VIGENTE

**Contenidos (4h presenciales):**
- Diseño de programa completo (módulos, funciones simples) (60 min)
- f-strings para reportes formateados (30 min)
- Laboratorio: programa Python completo NeuroBiz (90 min)

**Código NeuroBiz Completo (Semana 14):**
```python
# NeuroBiz S.A.S. — Sistema de Reportes Mensual
# RA4 · TGA04 · IUB 2026

print("="*50)
print("  NEUROBIZ S.A.S. — REPORTE MENSUAL")
print("="*50)

total_pacientes = int(input("Total pacientes este mes: "))
suma_progreso = 0
alertas = []

for i in range(total_pacientes):
    print(f"\n--- Paciente {i+1} ---")
    nombre = input("Nombre: ")
    asistidas = int(input("Sesiones asistidas: "))
    fallidas = int(input("Sesiones fallidas: "))
    progreso = float(input("Índice de progreso (0-100): "))
    
    total_sesiones = asistidas + fallidas
    tasa = (asistidas / total_sesiones) * 100 if total_sesiones > 0 else 0
    suma_progreso += progreso
    
    if tasa < 70:
        alertas.append(nombre)
        estado = "⚠️ REQUIERE ATENCIÓN"
    elif tasa < 85:
        estado = "✅ PROGRESO NORMAL"
    else:
        estado = "🌟 EXCELENTE"
    
    print(f"Tasa retención: {tasa:.1f}% | Estado: {estado}")

promedio_progreso = suma_progreso / total_pacientes
print("\n" + "="*50)
print(f"Índice promedio del mes: {promedio_progreso:.2f}")
print(f"Pacientes en alerta: {len(alertas)}")
if alertas:
    print("Requieren seguimiento:", ", ".join(alertas))
```

**XP Semana 14:** 10 + 35 (lab mayor integrador) = **45 XP** (acum: 675) → 🔴 CTO de NeuroBiz!

---

### SEMANA 15 — Debugging y Verificación (RA5)
**RA5 | CE1-CE2 | Bloom: Evaluar → Crear**

**Título:** "Bug hunter: depuración en Colab antes del lanzamiento"

**Relevancia:** 🟢 VIGENTE
*"Debugging is twice as hard as writing the code in the first place" — Brian Kernighan (Bell Labs)*
*"The ability to read and fix code is now a key skill for business analysts" — McKinsey Digital 2024*

**Contenidos (4h presenciales):**
- Tipos de errores: sintaxis vs lógico vs runtime (45 min)
- Herramientas de debug en Colab: `print()`, mensajes de error, traceback (60 min)
- Laboratorio: 3 programas NeuroBiz con bugs — identificar y corregir (75 min)

**Tipos de Errores:**
| Tipo | Descripción | Ejemplo | Detectado por |
|---|---|---|---|
| **SyntaxError** | Error de escritura del código | `if x = 5:` (debería ser `==`) | Python antes de correr |
| **RuntimeError** | Error durante la ejecución | División por cero | Python mientras corre |
| **LogicError** | Resultado incorrecto | `tasa = asistidas / total * 10` (debería ser `* 100`) | Solo el programador / prueba |

**Misión Final NeuroBiz (3 bugs):**
```python
# PROGRAMA CON BUGS — Encuéntralos y corrígelos
sesiones = int(input("Sesiones: "))
pacientes = int(input("Pacientes: "))

promedio = sesiones / pacientes  # BUG 1: ¿Qué pasa si pacientes = 0?

for i in range(1, pacientes):  # BUG 2: ¿Cuántos pacientes procesa?
    progreso = float(input(f"Progreso paciente {i}: "))
    if progreso > 100:  # BUG 3: ¿Está bien esta condición para una alerta de bajo progreso?
        print("Paciente en alerta")
```

**Quiz Semana 15 (5 preguntas):**
1. ¿Qué tipo de error produce `print("hola"` sin cerrar paréntesis? → SyntaxError
2. ¿Cómo evitas un error de división por cero? → Verificar con `if denominador != 0:` antes de dividir
3. `range(1, 5)` produce cuántos valores? → 4 (1, 2, 3, 4)
4. ¿Qué muestra Python cuando hay un error en tiempo de ejecución? → Traceback con la línea del error
5. ¿Qué tipo de error es el más difícil de encontrar automáticamente? → Error lógico

**XP Semana 15:** 10 + 25 + 30 (lab debugging) = **65 XP** (acum: 740 total posible)

---

## 6. RESUMEN DE XP POR SEMANA

| Semana | XP Disponible | XP Acum. (max) | Rango Posible |
|---|---|---|---|
| 1 | 55 | 55 | 🔵 Aprendiz |
| 2 | 55 | 110 | 🟢 Analista Junior |
| 3 | 55 | 165 | 🟢 Analista Junior |
| 4 | 55 | 220 | 🟢 Analista Junior |
| **5** | **—** | **220** | **PARCIAL** |
| 6 | 55 | 275 | 🟡 Consultor |
| 7 | 55 | 330 | 🟡 Consultor |
| 8 | 55 | 385 | 🟡 Consultor |
| 9 | 60 | 445 | 🟠 Arquitecto |
| **10** | **—** | **445** | **PARCIAL** |
| 11 | 55 | 500 | 🟠 Arquitecto |
| 12 | 65 | 565 | 🟠 Arquitecto |
| 13 | 65 | 630 | 🟠 Arquitecto |
| 14 | 45 | 675 | 🔴 CTO |
| 15 | 65 | 740 | 🔴 CTO |

---

## 7. NOTAS DEL PROFESOR — GUÍA GENERAL

### Qué hacer la primera semana de clase
1. Registrar a todos los estudiantes con su CC en el sistema (modal de registro)
2. Explicar el sistema de XP y rangos — mostrar el tablero de líderes
3. Presentar NeuroBiz como el "cliente" del cuatrimestre
4. Diagnóstico rápido: ¿quién usa Excel? ¿quién ha visto fórmulas IF()?

### Cómo manejar la brecha tecnológica
- Algunos estudiantes no tendrán computador. Alternativas: celular con Colab app, sala de sistemas IUB
- PSeInt se puede usar en papel — los ejercicios de pseudocódigo no requieren software hasta semana 12
- Google Colab funciona en celular (modo escritorio del navegador)

### Sobre la bibliografía Java (Deitel)
- Usa Deitel solo para conceptos estructurales (capítulos de algoritmos, no de Java)
- Para Python: usar recursos de Harvard CS50 (gratuitos, en español disponible)
- Complementar con Google Colab notebooks precargados

### Señales de alerta
- Si un estudiante no sube de Analista Junior después de semana 4 → refuerzo personalizado
- Si hay muchos errores de tipo (mezclar CADENA con ENTERO) → repetir analogía de los cajones
- Semana 9 es el "muro de complejidad" — planear actividad colaborativa en pares

---

## 8. ESTRUCTURA DE ARCHIVOS A GENERAR

```
FundamentosComputacion/
├── semana1/
│   ├── index.html          ← Material de estudio estudiante
│   └── notas_profesor.html ← Guía docente
├── semana2/
│   ├── index.html
│   └── notas_profesor.html
├── semana3/ ... semana4/ ... (sem 5 solo notas_profesor)
├── semana6/ ... semana9/ ... (sem 10 solo notas_profesor)
├── semana11/ ... semana15/
├── js/
│   └── supabase-config.js   ← Existente
├── KNOWLEDGE_BASE.html      ← Existente (actualizar)
└── PLAN_CONTENIDO_TGA04.md  ← Este archivo
```

---

*Generado con base en: TGA04_Fundamentos.md, RolGamificador.txt, Caso_Estudio_NeuroBiz_Consolidado.md, Harvard CS50, MIT 18.S191, WEF FoJ 2025, McKinsey Digital 2024, Deloitte Academies 2024*
