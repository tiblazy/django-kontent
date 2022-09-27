class ValidationError(Exception):
    pass


class ContentSerializer:

    content_types = {
        "title": str,
        "module": str,
        "description": str,
        "students": int,
        "is_active": bool,
    }

    def __init__(self, **kwargs) -> None:
        self.data = kwargs
        self.errors = {}

    def is_valid(self) -> bool:
        self.clean_data()

        try:
            self.validate_required_keys()
            self.validate_data_types()

            return True

        except ValidationError:
            return False

    def clean_data(self) -> None:
        data_keys = tuple(self.data.keys())

        for key in data_keys:
            if key not in self.content_types.keys():
                self.data.pop(key)

    def validate_required_keys(self) -> None:
        for valid_key in self.content_types.keys():
            if valid_key not in self.data.keys():
                self.errors[valid_key] = "missing key"

        if self.errors:
            raise ValidationError

    def validate_data_types(self) -> None:
        for valid_key, valid_type in self.content_types.items():
            if type(self.data[valid_key]) is not valid_type:
                self.errors.update({valid_key: f"must be a {valid_type.__name__}"})

        if self.errors:
            raise ValidationError
