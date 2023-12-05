// Esse código em Go cria um algoritmo de criptografia irreversível para armazenamento de senhas em bancos de dados

// Para isso o algoritmo usa uma biblioteca oficial da Golang para criptografia de senhas.

// O sistema utiliza a técnica de hashing. As funções hash são projetadas para serem funções de mão única. 

// Isso significa que, dado um valor hash, é computacionalmente inviável recuperar os dados de entrada originais. 

// Isso é devido à natureza das operações matemáticas usadas, que resultam em perda de informação durante o processo de hashing. 

// Em outras palavras, várias entradas diferentes podem resultar no mesmo valor hash, mas não há como determinar qual entrada específica produziu um valor hash sem ter a entrada original.

package main

import (
        "golang.org/x/crypto/bcrypt" // Importando o pacote bcrypt para criptografia de senhas
        "fmt" // Importando o pacote fmt para impressão formatada e leitura de E/S
)

func main() {
            password := []byte("MyP@ssword123") // Definindo a senha como uma sequência de bytes

            // Fazendo hashing a senha com o custo padrão de 10
            hashedPassword, err := bcrypt.GenerateFromPassword(password, bcrypt.DefaultCost)
            if err != nil {
                    panic(err) // Se houver um erro durante a geração do hash, o programa irá parar
            }
            fmt.Println(string(hashedPassword)) // Imprimindo a senha criptografada

            // Comparando a senha com o hash
            err = bcrypt.CompareHashAndPassword(hashedPassword, password)

            if err == nil {
                    fmt.Println ("Password match!") // Se a senha e o hash correspondem, imprime "Password match!"
            } else {
                fmt.Println("Password does not match!") // Se a senha e o hash não correspondem, imprime "Password does not match!"
                fmt.Println(err) // Imprime o erro
            }
}
