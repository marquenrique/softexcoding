class ContaBancaria{
    constructor(saldo){
        this.saldo = saldo;
    }

    depositar(){
        return this.saldo++
    }

}

const cb1 = new ContaBancaria(10)
cb1.depositar()
console.log(cb1.saldo)

const cb2 = new ContaBancaria(98)
cb2.depositar()
cb2.depositar()
console.log(cb2.saldo)

const cb3 = new ContaBancaria(50)
console.log(cb3.saldo)
