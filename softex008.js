class Diretor{
    #nome
    #email
    #senha
    constructor(nome, email, senha, role = 'diretor', ativo=true){
        this.#nome = nome
        this.#email = email
        this.#senha = senha 
        this.role = role 
        this.ativo = ativo
    }

    get nome(){
        return this.#nome
    }

    get senha(){
        return this.#senha
    }

    set senha(novaSenha){
        this.#senha = novaSenha
    }

}

const srDiretor = new Diretor('Fatima', 'f@f.com', '0506')
console.log(srDiretor)
console.log(srDiretor.nome)
srDiretor.senha = '1478'
console.log(srDiretor.senha)