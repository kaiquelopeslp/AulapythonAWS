CREATE TABLE loyalty
(
    cliente_id INTEGER NOT NULL PRIMARY KEY,
    sobrenome varchar (20) NULL,
    nomw varchar(25) NOT NULL,
    numero_fidelidade INTEGER NOT NULL,
    telefone varchar(20) NULL,
    email varchar (80) NOT NULL,
    saldo_pontos INTEGER NOT NULL
)

INSERT INTO loyalty
(1, "Alves", "Severino", 10, "83999999999", "teste@gmail.com", 50)
(2, "Pereira", "Jose", 15, "8396666666", "teste2@gmail.com", 70)