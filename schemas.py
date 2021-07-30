user_success = {
    "definitions": {},
    "type": "object",
    "title": "The Root Schema",
    "required": [
        "username",
        "firstName",
        "lastName",
        "email",
        "password"
    ],
    "properties": {
        "username": {
            "$id": "#/properties/username",
            "type": "string",
            "title": "The Username Schema",
            "default": "",
            "examples": ["jamesbetty"],
        },
        "firstName": {
            "$id": "#/properties/firstName",
            "type": "string",
            "title": "The Firstname Schema",
            "default": "",
            "examples": ["Meagan"],
        },
        "lastName": {
            "$id": "#/properties/lastName",
            "type": "string",
            "title": "The Lastname Schema",
            "default": "",
            "examples": ["Jones"],
        },
        "email": {
            "$id": "#/properties/email",
            "type": "string",
            "title": "The Email Schema",
            "default": "",
            "examples": ["jcastillo@example.org"],
        },
        "password": {
            "$id": "#/properties/password",
            "type": "string",
            "title": "The Password Schema",
            "default": "",
            "examples": ["123456"],
        }
    }
}
