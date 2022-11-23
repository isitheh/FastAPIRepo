#Import BaseSettings from pydantic
from pydantic import BaseSettings

#Define the CommonSettings class (Inherits from BaseSettings)
class CommonSettings(BaseSettings):
    APP_NAME: str = "API"
    DEBUG_MODE: bool = True

#Define the ServerSettings class (Inherits from BaseSettings)
class ServerSettings(BaseSettings):
    HOST: str = "localhost"
    PORT: int = 8080

#Main Settings class that includes all the settings classes
class Settings(CommonSettings, ServerSettings):
    pass

#We create a settings variable that will be used in the other files
settings = Settings()