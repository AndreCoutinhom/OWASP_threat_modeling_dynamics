function escapeHTML(text) {
    // Cria um objeto que mapeia caracteres especiais para suas respectivas entidades HTML
    var map = {
        '&': '&amp;',  // Ampersand
        '<': '&lt;',   // Menor que
        '>': '&gt;',   // Maior que
        '"': '&quot;', // Aspas duplas
        "'": '&#x27'   // Aspas simples
    };

    // A função replace usa uma expressão regular para encontrar todos os caracteres especiais no texto
    // A função passada como segundo argumento é chamada para cada caractere especial encontrado
    // Essa função retorna a entidade HTML correspondente ao caractere especial
    return text.replace(/[&<>"']/g, function(m) { return map[m]; });
