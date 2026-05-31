Atividade: Desenvolvimento com Testes Unitários

Cenário Escolhido:
Sistema de Autenticação de Usuários

Ciclo de Desenvolvimento (TDD):

1. Foi criado o teste para cadastro de usuário válido.
2. Implementou-se o método cadastrar_usuario().
3. Foi criado o teste para usuário duplicado.
4. Ajustou-se a validação para impedir cadastros repetidos.
5. Foram criados os testes de login válido, senha incorreta e usuário inexistente.
6. Implementou-se o método login().
7. Foi criado o teste para redefinição de senha.
8. Implementou-se o método redefinir_senha().
9. Todos os testes foram executados e aprovados.

Execução:

Instalar pytest:

pip install pytest

Executar os testes:

pytest -v