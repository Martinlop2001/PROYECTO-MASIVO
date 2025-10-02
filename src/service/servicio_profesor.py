

from repositorio.repositorio_profesor import RepositorioProfesor

class ServicioProfesor:
    def listar_profesores(self):
        repositorio = RepositorioProfesor()
        listado_profesores = repositorio.listar_profesores()
        return listado_profesores
    
