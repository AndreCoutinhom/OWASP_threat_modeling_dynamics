-- A regra é simples: não concatenar inputs do usuário em comandos no seu servidor. Independente de ser uma instrução SQL ou um comando que será executado na máquina.
-- Usando os parâmetros abaixo, os valores não são inseridos de forma a serem concatenados como inputs, e sim como textos literais.

sql = "INSERT INTO avaliacoes (avaliacao, descricao, url_arquivo, id_usuario, id_produto)" + "VALUES (?,?,?,?,?)"
params = (avaliacao, descricao, url_arquivo, id_usuario, id_produto)

DatabaseHelper.execute(sql, params)
