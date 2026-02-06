from abc import ABC, abstractmethod


class Service(ABC):
    
    @abstractmethod
    def run(self): 
        """ Default running 
        """
        
    @abstractmethod
    def setup(self, data: dict={}):
        """Initiate and setup Class with required data

        Args:
            data (dict, optional): _description_. Defaults to {}.
        """