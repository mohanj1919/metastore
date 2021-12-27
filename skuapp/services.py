import logging
from typing import Any, List
from models import (
    Location,
    Department,
    Category,
    ProductSku
)

class ModelService():
    logger = logging.getLogger(__name__)
    def __init__(self, model) -> None:
        self.model = model

    def get_by_id(self, id: int) -> Any:
        try:
            return self.model.get(id=id)
        except self.model.DoesNotExist as e:
            self.logger.error(
                f"Error getting {type(self.model)} with id: {id} Error: {str(e)}.", exc_info=True)
            raise e

    def get(self) -> List:
        """
        return List of self.model instances
        """
        return self.objects.all()

    def post(self, data) -> None:
        """
        """
        instance = self.model(**data)
        instance.save()

class LocationService():
    pass

