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





