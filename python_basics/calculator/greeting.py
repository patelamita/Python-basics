def greet(name: str = None) -> None:
    if not name:
        return "Hello, welcome to python and data science class."

    return f"Hello {name}, welcome to python and data science class."