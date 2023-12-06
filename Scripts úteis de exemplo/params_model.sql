-- A regra é simples: não concatenar inputs do usuário em comandos no seu servidor. Independente de ser uma instrução SQL ou um comando que será executado na máquina.

sql = "INSERT INTO avaliacoes (avaliacao, descricao, url_arquivo, id_usuario, id_produto)" + "VALUES (?,?,?,?,?)"
params = (avaliacao, descricao, url_arquivo, id_usuario, id_produto)

DatabaseHelper.execute(sql, params)
