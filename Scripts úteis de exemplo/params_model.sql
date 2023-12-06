sql = "INSERT INTO avaliacoes (avaliacao, descricao, url_arquivo, id_usuario, id_produto)" + "VALUES (?,?,?,?,?)"
params = (avaliacao, descricao, url_arquivo, id_usuario, id_produto)

DatabaseHelper.execute(sql, params)
