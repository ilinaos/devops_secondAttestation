create table test_table (
id serial primary key,
name varchar(10),
surname varchar(50),
city varchar(70),
age integer
);

insert into test_table(name, surname, city, age)
values
('Rick', 'Kennedy', 'Paris', 37),
('Summer', 'Kennedy', 'Washington', 28),
('Maximus', 'Pines', 'Oslo', 40),
('Beth', 'Kennedy', 'Helsinki', 40),
('Jerry', 'Oswald', 'Washington', 24),
('Morty', 'Kennedy', 'Paris', 26),
('Rick', 'Smith', 'Washington', 25),
('Beth', 'Kennedy', 'Helsinki', 24),
('Jerry', 'Kennedy', 'Helsinki', 19),
('Stanley', 'Oswald', 'Moscow', 49),
('Annabel', 'Kennedy', 'Washington', 26),
('Annabel', 'Smith', 'Moscow', 37),
('Jerry', 'Smith', 'Paris', 20),
('Rick', 'Kennedy', 'Moscow', 30),
('Rick', 'Pines', 'Moscow', 36),
('Rick', 'Oswald', 'Paris', 20),
('Stanley', 'Oswald', 'Washington', 20),
('Rick', 'Smith', 'Washington', 49),
('Morty', 'Kennedy', 'Helsinki', 42),
('Morty', 'Kennedy', 'Moscow', 31);