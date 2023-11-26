class Person:
    def __init__(
        self, person_id: int, fio: str, card_number: int, hash_pass: int, login: str
    ):
        self.id = person_id
        self.FIO = fio
        self.cardNumber = card_number
        self.hashPass = hash_pass
        self.login = login

    def get_id(self):
        return self.id

    def get_FIO(self):
        return self.FIO

    def get_login(self):
        return self.login

    def set_login(self, new_login):
        self.login = new_login

    def get_hash_pass(self):
        return self.hashPass

    def set_hash_pass(self, new_hash_pass):
        self.hashPass = new_hash_pass
