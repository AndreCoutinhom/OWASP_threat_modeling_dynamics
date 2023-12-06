# Modelagem de ameaças: identifique riscos na concepção do software

![image](https://github.com/AndreCoutinhom/OWASP_threat_modeling_dynamics/assets/91290799/8b68549d-2b26-4f69-b1d4-ea7104a2894e)


> OTT, Ben-Hur Santos. Modelagem de ameaças: identifique riscos na concepção do software. Alura, 2023.

Este repositório serve para armazenar materiais didáticos do curso de *threat modeling* da Alura.

---

### Faça esse curso de Segurança e:
* Aprenda os principais riscos de segurança em aplicações web
* Conheça como mitigar problemas antes mesmo da equipe começar a desenvolver
* Conheça as metodologias mais utilizadas para classificação de vulnerabilidades
* Identifique possíveis vulnerabilidades com poucas informações sobre o sistema
* Revise códigos e desenhos de software em busca de brechas de segurança

---

# Apresentação

## Termos recorrentes

* CVE (Common Vulnerabilities and Exposures)
* Risco / Vulnerabilidade
* Exploit (Conjunto de técnicas e scripts que executam comandos que permitem a manipulação do banco de dados)
* Ameaça

![image](https://github.com/AndreCoutinhom/OWASP_threat_modeling_dynamics/assets/91290799/897d49da-5ed6-4e0f-bb14-4eeed5113522)

![image](https://github.com/AndreCoutinhom/OWASP_threat_modeling_dynamics/assets/91290799/5f49271c-6f67-42d8-b954-558db4903d72)

![image](https://github.com/AndreCoutinhom/OWASP_threat_modeling_dynamics/assets/91290799/9aeaa914-cb99-4c5c-82d6-1a363dea9f33)

![image](https://github.com/AndreCoutinhom/OWASP_threat_modeling_dynamics/assets/91290799/9c61cb57-8489-47bc-8a2f-afdeb3571659)

---

# Decompondo a aplicação

## Caderno de modelagem de ameaças

| INFORMAÇÕES | 
|-------------|
| Nome da Aplicação | 
| Versão da Aplicação | 
| Descrição | 
| Autor (nome e contato) | 
| Participantes (nome e contato) | 
| Revisor (nome e contato) | 

## Caminho ideal de requisição para API

![image](https://github.com/AndreCoutinhom/OWASP_threat_modeling_dynamics/assets/91290799/034cf6b0-be7c-459d-9900-6801fd3f80ff)

---

Acesse [aqui](Scripts%20úteis%20de%20exemplo/byte_limit.py) um exemplo de script para reduzir os efeitos de DOS.

## Tabela de dependências externas

| ID | DESCRIÇÃO | 
|-------------|-------------|
| 1 | Por onde a plataforma é acessada? 
| 2 | Para onde vão as informações enviadas pelo usuário? |
| 3 | Onde são salvos os dados enviados pelo usuário? |
| 4 | Há outros tipos de dados salvos em outro servidor? Se sim quais? |

---

## Tabela de controle do ponto de entrada

| ID | NOME | DESCRIÇÃO | NÍVEL DE CONFIANÇA
|-------------|-------------|-------------|-------------|
| 1 | Nome do ponto de entrada | Como interagimos com o ponto de entrada | Autorização necessária para acesso |

> **Se algo está público na Internet, seja um site, um app ou uma interação com API, então é algo que pode ser acessado pelo atacante (OTT, 2023).**

### Notas:

* Pontos de entrada são meios pelos quais usuários podem acessar um recurso de uma plataforma.
* Fronteiras são a divisão entre o que fica disponível para o usuário e o que fica nos servidores (Front-end X Back-end). As fronteiras definem onde os níveis de interação mudam, podem ser divisões de rede, onde níveis de permissão de acesso mudam, onde entendemos que existem grupos de dependências externas.
* Tudo que está na internet é um ponto de entrada para qualquer usuário, incluindo um possível atacante.
* Se algo no lado da fronteira back-end sirva como ponto de entrada, então existem dados no servidor que podem ser acessados pela internet.

---

* Todo ponto de entrada tem uma saída.
* Pontos de saída são coisas que acontecem quando o usuário é bem ou mal-sucedido na tentativa de acessar um ponto de entrada.
* É sempre bom para um modelador de ameaças que destaque os pontos onde existem variáveis, ou seja, dados que podem ser diferentes para cada usuário.

## Exemplos de documentação de descrição de entrada e saída

### Modelador com conhecimento técnico total
![image](https://github.com/AndreCoutinhom/OWASP_threat_modeling_dynamics/assets/91290799/d42e088b-cfb5-41cd-8e4c-aae3855976f7)

### Modelador com conhecimento técnico parcial
![image](https://github.com/AndreCoutinhom/OWASP_threat_modeling_dynamics/assets/91290799/6ff35a79-7e40-4946-8a34-19a921c2e9aa)

### Modelador sem nenhum conhecimento técnico
![image](https://github.com/AndreCoutinhom/OWASP_threat_modeling_dynamics/assets/91290799/6eeb20f2-f70e-483e-a576-8ffcc8448d72)

--- 

> Toda informação valiosa que o atacante pode usar contra a empresa, chamamos de Ativo. Pode ser um dado palpável ou abstrato. Porém, o que é algo "palpável"? Pode ser uma base de dados, um acesso ao servidor ou aos documentos das pessoas. Isto é, são ativos físicos em que o valor está diretamente relacionado ao ativo.

> Os ativos abstratos são os que estão relacionados à reputação da empresa - por alguma informação que pode impactar o negócio. Por exemplo, uma empresa que fabrica eletrônicos de ponta, se vazar algum documento de um produto que ainda será lançado, isso gera um impacto direto nas vendas e ações da empresa.

## Tabela de controle de riscos de Ativos

| ID | NOME | DESCRIÇÃO | NÍVEL DE CONFIANÇA
|-------------|-------------|-------------|-------------|
| O identificador único do ativo | O nome que nós vamos dar ao ativo | Um texto breve sobre o por aquele ativo ser relevante para o nosso negócio sistema | Para saber quem tem acesso direto às informações deste ativo |

---

* É importante mapear todos os níveis de confiança para entender todos os tipos de interação que podem ser feitos na aplicação.

---

# Determinar e categorizar as ameaças
---
> Nenhum sistema é totalmente livre de ameaças. Um sistema pode apenas estar seguro em determinados momentos.
---
## Threat Modeling Frameworks

### STRIDE

Criado por Koren Kohnfelder e Praerit Garg para classificar os tipos de ameaças à segurança.

|  | AMEAÇA | CONTROLE | 
|-------------|-------------|-------------|
| S | Spoofing | Authentication | 
| T | Tampering | Integrity |
| R | Repudiation | Non-Repudiation |
| I | Information Disclosure | Confidentiality |
| D | Denial of Service | Availability |
| E | Elevation of Privilage | Authorization |

---

### DREAD

Para calcular os níveis das possíveis ameaças.

|  | CRITÉRIO | 
|-------------|-------------|
| D | Damage | Authentication | 
| R | Reproducibility |
| E | Exploitability |
| A | Affected users |
| D | Discoverability |

---

### Níveis para cada critério
---
![image](https://github.com/AndreCoutinhom/OWASP_threat_modeling_dynamics/assets/91290799/e3b6a489-f6af-4076-bb84-9c51219224d5)

---

![image](https://github.com/AndreCoutinhom/OWASP_threat_modeling_dynamics/assets/91290799/116229d7-02e3-474f-9a7d-676cfc390fcc)

---

![image](https://github.com/AndreCoutinhom/OWASP_threat_modeling_dynamics/assets/91290799/f3f3c575-75fd-4b66-99a6-295932fc5f35)

---

![image](https://github.com/AndreCoutinhom/OWASP_threat_modeling_dynamics/assets/91290799/3c082653-e15a-4457-8d05-a92ca6d1cfa9)

---

![image](https://github.com/AndreCoutinhom/OWASP_threat_modeling_dynamics/assets/91290799/c1835d82-285c-485f-b8fe-1dd38cec4b93)

---

## CVSS

![image](https://github.com/AndreCoutinhom/OWASP_threat_modeling_dynamics/assets/91290799/717b6e42-ab8b-45b8-8a86-e3ab43289163)

---

### [Mais sobre DREAD](https://www.eccouncil.org/cybersecurity-exchange/threat-intelligence/dread-threat-modeling-intro/)

---

## Modelo de risco qualitativo 

> Nesse método se fazem perguntas importantes sobre as portas de entrada e os níveis de ameaça de forma que se tenha uma ideia relfexiva e personalizada em relação às possíveis ações do atacante.

> Isso é muito útil se nem todas as métricas pelo framework DREAD puderem ser solucionadas.

---

### Dicas em geral

* Vazaram dados dos usuários ou sigilosos? Corrija agora.
* O atacante consegue acesso aos sistemas? Corrija agora.
* O atacante consegue tirar os sistemas do ar? Corrija agora.

---

# Mitigando riscos #1

### Autenticação

> "Autenticação é o processo que verifica se o indivíduo, entidade ou aplicação informa que é quem pretende ser." *OWASP*

---

## Estudo de caso - Autenticação via Token de sessão

### Dicas em geral

* O token de sessão deve ser transitado somente pelos Headers da requisição e em protocolos seguros.
  * A utilização de https é obrigatória.
  * Utilize apenas o header Authorization ou cookies para trafegar o token de sessão. Nunca na URL.
* Ao receber o token de sessão na api, valide:
  * Se o token de sessão não está expirado.
  * Se o token de sessão é válido, ou seja, pertence de fato a um usuário logado no momento.

---

## [ASVS (Application Security Verification Standard)](https://github.com/OWASP/ASVS/tree/v4.0.3)
Acesse o artigo completo [aqui](/ASVS_document.pdf)

---

## [OWASP Cheat Sheet](https://github.com/OWASP/CheatSheetSeries)

### [Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)

---

> Se há apenas um processo de autenticação, o atacante tem poucos passos a percorrer para ter acesso aos dados do servidor que revelem uma porta de entrada de alto risco para a empresa.
> 
> É sempre bom ficar de olho nas requisições e os passos que levam o usuário a cada uma delas.

---

> Quando a requisição tiver IDs, garantir que o usuário logado possa realizar a operação que deseja nos ids que ele informa (ex: se ele quer atualizar um endereço, se ele informar qualquer id que não seja um endereço dele, deve retornar erro).
>
> Sempre devemos validar os ids da requisição.

---

> Quando o usuário tentar acessar uma funcionalidade, devemos verificar se ele possui permissão para acessar.
>
> Devemos inclusive descrever o processo de como a aplicação garante isto.

---

### [Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)

---

### [Security best practices for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html)
Acesse o guia de usuário para serviço de armazenamento da Amazon [aqui](/amazon_simple_storage_service.pdf)

---

### [Security Misconfiguration](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/)

---

> O melhor a se fazer em bucket lists é conceder acesso apenas para caminhos de URL específicas e exclusivas, nunca torná-las públicas de forma alguma.
>
> Esse é um dos erros de segurança mais cometidos por empresas.

---

> Os atacantes não olham somente o sistema em produção; se eles encontrarem o sistema de desenvolvimento, este pode ter dados de backup de produção. Então se um ambiente está público para a internet, ele deve ter os mesmos cuidados de segurança de um ambiente de produção.
>
> Qualquer ambiente que está exposto para a internet pode estar vulnerável.

---

* Nunca armazene senhas em banco de dados em forma de texto aberto ou algoritmo de criptografia reversível (recomendável utilizar [algoritmos de hash](Scripts%20úteis%20de%20exemplo/unreversible_encrypted_password.go)).

---

### [PCI DSS](https://www.pcisecuritystandards.org/document_library/)

---

* Atenção aos problemas na gestão de conhecimento da chave:
  * Pessoas com acesso à senhas do banco de dados não podem mais ter acesso à senha utilizada. Alterar todo o sistema de senhas se possível
  * Danos ou comprometimentos em um computador específico devem ser motivo para a reestruturação completa do computador.

---

* Separe e restrinja os tipos de acesso.
  * Cada membro deve ter uma credencial para poder acessar dados do sistema.
  * Sempre forneça o mínimo de acesso possível a diversos bancos para novos funcionários.
  * Utilize dados falsos para testes.
  * Criptografar o armazenamento de dados.
---

> Qualquer dado sensível e/ou pessoal deve ser removido ou completamente anonimizado, ou seja, não deve ser possível identificar dados de pessoas reais.
>
> Quando levamos dados de produção para outros ambientes, ele não deve conter dados de pessoas.

---

### [Protect Data Everywhere](https://owasp.org/www-project-proactive-controls/v3/en/c8-protect-data-everywhere)

---

### [User Privacy Protection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/User_Privacy_Protection_Cheat_Sheet.html)

---

### [DATA PROTECTION](https://owaspsamm.org/model/operations/operational-management/stream-a/)

---

### XSS (Cross-Site Scripting)

Quando capturamos as informações que o usuário envia e renderizamos para outro usuário sem restrição.

---

### [How to prevent XSS](https://portswigger.net/web-security/cross-site-scripting/preventing)

---

### [Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

---

[Este script](Scripts%20úteis%20de%20exemplo/text_substitution.js) faz com que os valores não serão renderizados como um script. Uma tag script vai virar outro tipo de tag ou escrita. E vão bloquear a maioria dos ataques, isso porque o browser vai escrever na tela, mas não vai renderizar como um script.

---

### SQL Injection

Vulnerabilidade em que o atacante envia dentro de um campo da requisição um comando SQL, incluindo-o no comando SQL fonte.

> Concatenar inputs do usuário direto em instruções sql nos leva à vulnerabilidade de SQL Injection.

Para evitar, utilizar [SQL Parameters](Scripts%20úteis%20de%20exemplo/params_model.sql).

---

### Null Byte

Um ataque que consiste em colocar no final do nome do arquivo um comando que pode alterar o tipo de arquivo recebido dependedendo da tecnologia utilizada pela empresa.

Para evitar, fazer uma validação de tipos de arquivo pelo conteúdo. Usse [este código](Scripts%20úteis%20de%20exemplo/file_validation.py) como modelo.

---

Para saber quais sãos os parâmetros de conteúdo para cada tipo de arquivo acesse o link abaixo:

### [File Magic Bytes](https://en.wikipedia.org/wiki/List_of_file_signatures)

---

### SSRF (Server Side Request Forgery)

Forma do atacante enviar uma URL com o protocolo `file://`, o que o concederá acesso a parte dos arquivos internos da empresa. 

Para evitar é bom evitar a possibilidade do uso de URLs para envio de conteúdo. Caso a primeira opção não seja possível, restringir o envio de URLs para o protocolo HTTP ou HTTPS.

---

### [Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)

---

### [Validate All Inputs](https://owasp.org/www-project-proactive-controls/v3/en/c5-validate-inputs)

---

### [Improper Data Validation](https://owasp.org/www-community/vulnerabilities/Improper_Data_Validation)

---

### [Improper Input Validation](https://cwe.mitre.org/data/definitions/20.html)

---

### Dica de conduta
> Apenas informações para os usuários comuns devem ser entregues, não de sistema. Devemos gerenciar estas mensagens internamente.

---

### [HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

---

### [Improper Error Handling](https://owasp.org/www-community/Improper_Error_Handling)

---

### [Error Handling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html)

---

### [Handle all Errors and Exceptions](https://owasp.org/www-project-proactive-controls/v3/en/c10-errors-exceptions)

---

* Devemos ter total controle sobre a sessão e o usuário do lado da API.

---

* Não devemos punir os usuários originais por ataques realizados por criminosos.

---

### [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)

---

### [Improper Session Handling](https://owasp.org/www-project-mobile-top-10/2014-risks/m9-improper-session-handling)

---

### Logs
Método pelo qual podemos registrar toda a atividade dos usuários.

---

### Nunca logar:

* Dados de contato, como e-mail e telefone.
* Dados sigilosos, como senhas e tokens de sessão.
* Informações pessoais e sensíveis, como dados cadastrais.

---

### [Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)

---

### [Security Logging and Monitoring Failures](https://owasp.org/Top10/A09_2021-Security_Logging_and_Monitoring_Failures/)

---

### [Insufficient Logging & Monitoring](https://owasp.org/www-project-top-ten/2017/A10_2017-Insufficient_Logging%2526Monitoring)

---

### [Implement Security Logging and Monitoring](https://owasp.org/www-project-proactive-controls/v3/en/c9-security-logging)

---

## JSON Web Tokens 

Uma ferramenta que hackers podem utilizar para recolher informações a partir de documentos log.

Dependendo de como for a padronização de segurança e o gerenciamento de logs, é possível que qualquer pessoa com acesso aos logs possa ter acesso à informações sigilosas.

JSON Web Tokens é uma ferramenta com grande potencial de perigo se usada por hackers criminosos. No entanto, é também uma excelente ferramenta como parte da conduta de hackers éticos e equipes de QA.

---

# Conclusão

Parabéns pela conclusão do curso de Modelagem de ameaças: identifique riscos na concepção do software!

Neste curso, aprendemos a identificar possíveis problemas de segurança na concepção de software, antes dele ser construído.

O que aprendemos?

* Desenhamos o nosso sistema para termos visibilidade do que existe.
* Entendemos as conexões e como os componentes de software se comunicam.
* Vimos quais são os dados que temos e o que pode ser interessante para um atacante.
* Analisar criticamente as configurações dos nossos serviços.

Se você aplicar estes principais conceitos que aprendemos no seu cotidiano de desenvolvimento, com certeza construirá sistemas mais seguros.

Áreas que você também pode conhecer:

* Segurança Ofensiva (Red Team)
* Operações de Segurança (Blue Team e SOC)

Espero que você tenha conseguido realizar todas as atividades para colocar em prática o que aprendeu. Caso fique com dúvidas, pode postar no fórum que a comunidade vai te ajudar!
