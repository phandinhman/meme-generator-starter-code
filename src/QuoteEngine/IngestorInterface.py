from abc import ABC, abstractmethod


class IngestorInterface(ABC):

    @abstractmethod
    def can_ingest(cls, path: str):
        #return bool
        return True

    @abstractmethod
    def parse(cls, path: str):
        #return list(QouteModel)
        pass
