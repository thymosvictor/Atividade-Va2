class SistemaAutenticacao:
    def __init__(self):
        self.usuarios = {}

    def cadastrar_usuario(self, usuario, senha):
        if usuario in self.usuarios:
            raise ValueError("Usuário já cadastrado.")

        if len(senha) < 6:
            raise ValueError("A senha deve ter pelo menos 6 caracteres.")

        self.usuarios[usuario] = senha
        return True

    def login(self, usuario, senha):
        if usuario not in self.usuarios:
            raise ValueError("Usuário inexistente.")

        if self.usuarios[usuario] != senha:
            raise ValueError("Senha incorreta.")

        return True

    def redefinir_senha(self, usuario, nova_senha):
        if usuario not in self.usuarios:
            raise ValueError("Usuário inexistente.")

        if len(nova_senha) < 6:
            raise ValueError("A senha deve ter pelo menos 6 caracteres.")

        self.usuarios[usuario] = nova_senha
        return True