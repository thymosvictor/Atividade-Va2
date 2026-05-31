import pytest
from usuario import SistemaAutenticacao


def test_cadastro_usuario_valido():
    sistema = SistemaAutenticacao()

    resultado = sistema.cadastrar_usuario("joao", "123456")

    assert resultado is True


def test_usuario_duplicado():
    sistema = SistemaAutenticacao()

    sistema.cadastrar_usuario("joao", "123456")

    with pytest.raises(ValueError):
        sistema.cadastrar_usuario("joao", "654321")


def test_senha_muito_curta():
    sistema = SistemaAutenticacao()

    with pytest.raises(ValueError):
        sistema.cadastrar_usuario("joao", "123")


def test_login_valido():
    sistema = SistemaAutenticacao()

    sistema.cadastrar_usuario("joao", "123456")

    assert sistema.login("joao", "123456") is True


def test_senha_incorreta():
    sistema = SistemaAutenticacao()

    sistema.cadastrar_usuario("joao", "123456")

    with pytest.raises(ValueError):
        sistema.login("joao", "000000")


def test_usuario_inexistente():
    sistema = SistemaAutenticacao()

    with pytest.raises(ValueError):
        sistema.login("maria", "123456")


def test_redefinir_senha():
    sistema = SistemaAutenticacao()

    sistema.cadastrar_usuario("joao", "123456")
    sistema.redefinir_senha("joao", "nova123")

    assert sistema.login("joao", "nova123") is True