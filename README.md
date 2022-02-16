# project_eureciclo
Desafio de programação

O diretório existente trata-se de uma aplicação para upload de arquivos em formato .txt que será persistido em base de dados.

# Aplicação

O framework utilizando para o desenvolvimento é o Django e a base de dados é o Postgres, ambos são buildados e executados via Docker e docker-compose.

# Requisitos
- É necessário que o Docker e docker-compose estejam instalados na máquina em que a aplicação será executada.
- É necessário que as portas 5432 e 8000 estejam disponíveis.

# Execução

- /project_eureciclo$ sudo docker build -t eureciclo .
- /project_eureciclo$ sudo docker-compose up
  - Os comandos de migrate e test são executados nesse processo.
- Abra em seu navegador http://127.0.0.1:8000/api/upload

# Navegação
- Upload interface: interface de upload do arquivo.
- File preview interface: interface direcionada para visualização dos campos armazenados a partir do arquivo encaminhado.
- All files preview interface: interface de visualização de todos os campos de todos arquivos armazenados.

# Regras Aplicadas
- Campo Title: Campo obrigatório de caráter unico.
- Campo File: Campo obrigatório com validação para extenções de formato .txt.
