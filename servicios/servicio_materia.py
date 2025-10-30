
from repositorios.repositorio_materia import RepositorioMateria

class ServicioMateria:
    def listar_materias(self):
        repositorio = RepositorioMateria()
        return repositorio.listar_materias()

    def agregar_materia(self, nombre, carrera, anio):
        repositorio = RepositorioMateria()
        repositorio.agregar_materia(nombre, carrera, anio)

    def eliminar_materia(self, id_materia):
        repositorio = RepositorioMateria()
        repositorio.eliminar_materia(id_materia)

    def modificar_materia(self, nombre_original, nuevo_nombre, nueva_carrera, nuevo_anio):
        from repositorios.repositorio_materia import RepositorioMateria
        repo = RepositorioMateria()
        repo.modificar_materia(nombre_original, nuevo_nombre, nueva_carrera, nuevo_anio)
