from src.services.generate_repo import RepositoryStudents
from src.domain.student_validator import StudentValidator
from src.services.services import Services
from src.ui.ui import UI
from src.repository.repo import MemoryRepository, TextFileRepository, BinaryFileRepository


if __name__ == "__main__":

    repository_list = MemoryRepository()
    repository_list = RepositoryStudents().generate_repo(repository_list)

    repository_txt = TextFileRepository()
    repository_bin = BinaryFileRepository()

    validator = StudentValidator()
    services = Services(repository_list, validator)
    ui = UI(services)
    ui.start()

