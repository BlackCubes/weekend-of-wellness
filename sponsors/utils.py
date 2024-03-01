model_error_messages = {
    "sponsors": {
        "name": {
            "blank": "The name cannot be blank.",
            "invalid": "Invalid value for the name.",
            "max_length": "The name must be 100 characters or less.",
            "null": "The name cannot be empty.",
            "required": "The name is required.",
            "unique": "The name must be unique.",
        },
        "image": {
            "blank": "The image cannot be empty.",
            "required": "The image is required.",
        },
        "website": {
            "blank": "The website cannot be blank.",
            "max_length": "The website must be 200 characters or less.",
            "required": "The website is required.",
        },
        "sponsor_type": {
            "blank": "The sponsor type cannot be blank.",
            "choices": "The choices for sponsor type must be either primary, secondary, or additional.",
            "max_length": "The sponsor type must be 10 characters or less.",
            "required": "The sponsor type is required.",
        },
    },
}
