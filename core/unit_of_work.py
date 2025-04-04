# core/unit_of_work.py

from abc import ABC, abstractmethod


class AbstractUnitOfWork(ABC):
    """
    Interfaz para usar Unit of Work.
    Coordina múltiples repositorios y maneja transacciones.
    """

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError
