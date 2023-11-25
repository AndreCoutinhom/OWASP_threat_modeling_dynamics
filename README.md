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








