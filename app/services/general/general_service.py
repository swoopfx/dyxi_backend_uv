from services.service import Service


class GeneralService(Service):
    
    """
    Docstring for GeneralService
    A general service class that implements the Service interface.
    """
    
    def run(self):
        """ Default running 
        """
        pass
    
    def setup(self, data: dict={}):
        """Initiate and setup Class with required data

        Args:
            data (dict, optional): _description_. Defaults to {}.
        """
        pass