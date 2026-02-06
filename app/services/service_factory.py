from services.general.general_service import GeneralService
from services.auth.authentication_service import AuthenticatonService
from services.service import Service
from config.factory_config import factory_config

class ServiceFactory:
    
    @staticmethod
    def create_service(service_type: str) -> Service:
        if service_type == factory_config["services_name"]["GeneralService"]:
            return GeneralService()
         
        elif service_type == factory_config["services_name"]["AuthenticatonService"]:
            return AuthenticatonService()
        # Add more service types as needed
        raise ValueError(f"Unknown service type: {service_type}")