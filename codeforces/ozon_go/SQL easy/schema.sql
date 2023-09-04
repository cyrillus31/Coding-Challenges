create table packages
(
    id   bigint primary key,
    name text not null
);

create table fulfilments
(
    id   bigint primary key,
    name text not null
);

create table transportations
(
    id             bigint primary key,
    package_id     bigint    not null,
    source_id      bigint    not null,
    destination_id bigint    not null,
    departure_time timestamp not null,
    arrival_time   timestamp not null,
    constraint fk_transportations_package_id foreign key (package_id) references packages (id),
    constraint fk_transportations_source_id foreign key (source_id) references fulfilments (id),
    constraint fk_transportations_destination_id foreign key (destination_id) references fulfilments (id)
);

insert into packages
values (1, 'Package slow'),
       (2, 'Package fast'),
       (3, 'Package strange');

insert into fulfilments
values (1, 'Moscow'),
       (2, 'Spb'),
       (3, 'Almaty'),
       (4, 'Novosibirsk'),
       (5, 'Vladivostok');

insert into transportations
values (1, 1, 1, 3, '2023-01-01 12:00:00', '2023-01-13 12:00:00'),
       (2, 1, 3, 5, '2023-01-15 12:00:00', '2023-01-31 12:00:00'),
       (3, 1, 5, 2, '2023-02-27 12:00:00', '2023-03-14 12:00:00'),
       (4, 1, 2, 4, '2023-03-15 12:00:00', '2023-03-28 12:00:00'),
       (5, 2, 1, 2, '2023-02-15 12:00:00', '2023-02-15 18:00:00'),
       (6, 3, 2, 3, '2023-04-02 12:00:00', '2023-04-05 12:00:00'),
       (7, 3, 3, 5, '2023-04-07 12:00:00', '2023-04-28 12:00:00');
