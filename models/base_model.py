
import uuid
from datetime import datetime
import models


class BaseModel:

    def __init__(self, *args, **kwargs):
        if kwargs:
            if "__class__" in kwargs:
                del kwargs["__class__"]

            if "created_at" in kwargs:
                kwargs["created_at"] = datetime.strptime(
                    kwargs["created_at"], '%Y-%m-%dT%H:%M:%S.%f')

            if "update_at" in kwargs:
                kwargs["update_at"] = datetime.strptime(
                    kwargs["update_at"], '%Y-%m-%dT%H:%M:%S.%f')

            for key, value in kwargs.items():
                setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        models.storage.new(self)

    def __str__(self):

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):

        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.created_at.isoformat()
        return obj_dict
