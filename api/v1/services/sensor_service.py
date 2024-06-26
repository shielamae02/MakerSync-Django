from api.v1.schemas import SensorRequestSchema, SensorResponseSchema
from api.v1.repositories import SensorRepository
from api.v1.exceptions import BadRequestException, ServerErrorException, NotFoundException


class SensorService:
    
    @staticmethod
    def list():
        return SensorRepository.get_sensors()
    
    
    @staticmethod
    def create(sensor_id : str):
        
        if not SensorRepository.is_sensor_exists(sensor_id):
            raise BadRequestException(
                detail="Sensors already exists."
            )
        
        if not SensorRepository.create_sensor(sensor_id):
            raise ServerErrorException()
        
        return SensorResponseSchema()
    
    
    @staticmethod
    def retrieve(sensor_id : str):
        
        if SensorRepository.is_sensor_exists(sensor_id):
            raise NotFoundException(
                detail="Sensor not found."
            )
        
        sensor=SensorRepository.get_sensor(sensor_id)
        if not sensor:
            raise BadRequestException(
                detail="Invalid Sensor ID"
            )
    
        return SensorResponseSchema(**sensor)
    
    
    @staticmethod
    def update(sensor_id : str, sensor_request : SensorRequestSchema): 
        
        if SensorRepository.is_sensor_exists(sensor_id):
            raise NotFoundException(
                detail="Sensor not found."
            )
            
        sensor=SensorRepository.update_sensor(sensor_id, sensor_request)
        if not sensor: 
            raise BadRequestException(
                detail="Invalid Sensor ID"
            )
       
        return SensorResponseSchema(**sensor_request.dict())
            
    
    @staticmethod
    def destroy(sensor_id : str):
        
        if SensorRepository.is_sensor_exists(sensor_id):
            raise NotFoundException(
                detail="Sensor not found."
            )
        
        if not SensorRepository.delete_sensor(sensor_id):
            raise ServerErrorException()
        
        return True
    