class NoSuchUser(Exception):
    def __str__(self):
        return "The user with this ID is missing from the database"
