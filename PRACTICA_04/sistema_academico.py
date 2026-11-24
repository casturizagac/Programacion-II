from datetime import date

class Persona:
    def __init__(self, nombre, ci):
        self._nombre = nombre
        self._ci = ci

    def get_nombre(self):
        return self._nombre

    def get_ci(self):
        return self._ci

    def __str__(self):
        return f"Persona: {self._nombre}"

_TOKEN_HORARIO = object()

class Horario:
    def __init__(self, fecha, aula, token=None):
        if token is not _TOKEN_HORARIO:
            raise ValueError("El Horario debe crearse desde una Materia.")

        self._fecha = fecha
        self._aula = aula

    def get_fecha(self):
        return self._fecha

    def get_aula(self):
        return self._aula

    def __str__(self):
        return f"{self._fecha} - {self._aula}"

class Calificable:
    def calcular_nota(self):
        raise NotImplementedError("Este método debe ser implementado.")

class Estudiante(Persona):
    def __init__(self, nombre, ci, codigo):
        super().__init__(nombre, ci)
        self._codigo = codigo
        self._inscripciones = []

    def get_codigo(self):
        return self._codigo

    def get_inscripciones(self):
        return list(self._inscripciones)

    def inscribirse(self, materia):
        for inscripcion in self._inscripciones:
            if inscripcion.get_materia() is materia:
                raise ValueError(
                    f"{self._nombre} ya está inscrito en {materia.get_codigo()}."
                )

        inscripcion = Inscripcion(self, materia, date.today())
        self._inscripciones.append(inscripcion)
        materia.registrar_inscripcion(inscripcion)
        return inscripcion

    def __str__(self):
        return f"Estudiante {self._nombre} (código {self._codigo})"

class Docente(Persona):
    def __init__(self, nombre, ci, especialidad):
        super().__init__(nombre, ci)
        self._especialidad = especialidad
        self._materias = []
        self._ayudantes = []

    def dictar(self, materia):
        if materia.get_docente() is not None:
            raise ValueError(
                f"La materia {materia.get_codigo()} ya tiene un docente asignado."
            )

        materia.set_docente(self)
        self._materias.append(materia)

    def generar_acta(self, materia):
        return Acta(materia)

    def agregar_ayudante(self, ayudante):
        if ayudante not in self._ayudantes:
            self._ayudantes.append(ayudante)

    def get_materias(self):
        return list(self._materias)

    def get_ayudantes(self):
        return list(self._ayudantes)

    def __str__(self):
        return f"Docente {self._nombre} ({self._especialidad})"

class Ayudante(Estudiante):
    def __init__(self, nombre, ci, codigo, docente):
        super().__init__(nombre, ci, codigo)

        if not isinstance(docente, Docente):
            raise TypeError("El ayudante debe estar asociado a un Docente.")

        self._docente = docente
        docente.agregar_ayudante(self)

    def colaborar(self):
        return (
            f"{self._nombre} colabora con el docente "
            f"{self._docente.get_nombre()}."
        )

    def get_docente(self):
        return self._docente

class Universidad:
    def __init__(self, nombre):
        self._nombre = nombre
        self._carreras = []

    def crear_carrera(self, nombre_carrera):
        carrera = Carrera(nombre_carrera)
        self._carreras.append(carrera)
        return carrera

    def get_nombre(self):
        return self._nombre

    def get_carreras(self):
        return list(self._carreras)

class Carrera:
    def __init__(self, nombre):
        self._nombre = nombre
        self._docentes = []

    def agregar_docente(self, docente):
        if not isinstance(docente, Docente):
            raise TypeError("Solo se pueden agregar docentes.")

        if hasattr(docente, "_carrera") and docente._carrera is not self:
            raise ValueError(
                f"El docente {docente.get_nombre()} ya pertenece a otra carrera."
            )

        if docente not in self._docentes:
            self._docentes.append(docente)
            docente._carrera = self

    def get_nombre(self):
        return self._nombre

    def get_docentes(self):
        return list(self._docentes)

class Materia:
    def __init__(self, codigo, creditos):
        self._codigo = codigo
        self._creditos = creditos
        self._docente = None
        self._horarios = []
        self._inscripciones = []

    def agregar_horario(self, fecha, aula):
        horario = Horario(fecha, aula, _TOKEN_HORARIO)
        self._horarios.append(horario)
        return horario

    def registrar_inscripcion(self, inscripcion):
        if inscripcion not in self._inscripciones:
            self._inscripciones.append(inscripcion)

    def set_docente(self, docente):
        if self._docente is not None:
            raise ValueError("Esta materia ya tiene un docente.")
        self._docente = docente

    def get_codigo(self):
        return self._codigo

    def get_creditos(self):
        return self._creditos

    def get_docente(self):
        return self._docente

    def get_horarios(self):
        return list(self._horarios)

    def get_inscripciones(self):
        return list(self._inscripciones)

class Inscripcion(Calificable):
    def __init__(self, estudiante, materia, fecha):
        self._estudiante = estudiante
        self._materia = materia
        self._fecha = fecha
        self._nota = None

    def registrar_nota(self, nota):
        if nota < 0 or nota > 100:
            raise ValueError("La nota debe estar entre 0 y 100.")

        self._nota = float(nota)

    def calcular_nota(self):
        if self._nota is None:
            raise ValueError("La nota todavía no fue registrada.")

        return self._nota

    def get_estudiante(self):
        return self._estudiante

    def get_materia(self):
        return self._materia

    def get_fecha(self):
        return self._fecha

class Acta:
    def __init__(self, materia):
        self._fecha = date.today()
        contenido = []
        contenido.append(f"ACTA {materia.get_codigo()} - {self._fecha}")

        for inscripcion in materia.get_inscripciones():
            nombre = inscripcion.get_estudiante().get_nombre()
            nota = inscripcion.calcular_nota()
            contenido.append(f"{nombre}: {nota}")

        self._contenido = "\n".join(contenido)

    def __str__(self):
        return self._contenido

def main():
    print("========== SISTEMA ACADEMICO ==========\n")

    umsa = Universidad("UMSA")
    informatica = umsa.crear_carrera("Informática")

    docente = Docente(
        "Ana Alba",
        "1234567",
        "Ingeniería de Software"
    )
    informatica.agregar_docente(docente)

    poo = Materia("INF-121", 6)
    docente.dictar(poo)

    poo.agregar_horario(date(2026, 7, 2), "Aula 101")
    poo.agregar_horario(date(2026, 7, 9), "Aula 101")

    e1 = Estudiante("Carlos Flores", "7654321", "E-001")
    e2 = Estudiante("Maria Salas", "7654322", "E-002")

    i1 = e1.inscribirse(poo)
    i2 = e2.inscribirse(poo)

    i1.registrar_nota(85)
    i2.registrar_nota(92)

    personas = [docente, e1, e2]

    print("PERSONAS:")
    for persona in personas:
        print(persona)

    calificable = i1
    print(
        "\nNota de",
        e1.get_nombre(),
        ":",
        calificable.calcular_nota()
    )

    acta = docente.generar_acta(poo)
    print("\n", acta)

    ayudante = Ayudante(
        "Luis Perez",
        "7654323",
        "E-003",
        docente
    )
    print("\n", ayudante.colaborar())

    print("\n========== PRUEBAS DE CORRECCIONES ==========")

    try:
        e1.inscribirse(poo)
    except ValueError as error:
        print("\nDoble inscripción:", error)

    try:
        docente2 = Docente("Pedro Ruiz", "2222222", "Programación")
        docente2.dictar(poo)
    except ValueError as error:
        print("\nDos docentes en una materia:", error)

    try:
        e3 = Estudiante("Sofia Rojas", "3333333", "E-004")
        inscripcion_sin_nota = e3.inscribirse(poo)
        inscripcion_sin_nota.calcular_nota()
    except ValueError as error:
        print("\nNota sin registrar:", error)

    try:
        otra_carrera = umsa.crear_carrera("Electrónica")
        otra_carrera.agregar_docente(docente)
    except ValueError as error:
        print("\nDocente en dos carreras:", error)

    try:
        horario = Horario(date.today(), "Aula 202")
    except ValueError as error:
        print("\nComposición no estricta:", error)

if __name__ == "__main__":
    main()
