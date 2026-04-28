-- создаём группы, если их ещё нет
INSERT INTO groups (name) VALUES
('Friends'), ('Work'), ('Family'), ('Other')
ON CONFLICT (name) DO NOTHING;

-- добавляем контакты
INSERT INTO contacts (name, email, birthday, group_id) VALUES
('Alice Smith', 'alice@gmail.com', '1990-05-03', (SELECT id FROM groups WHERE name='Friends')),
('Bob Brown', 'bob@work.com', '1985-02-10', (SELECT id FROM groups WHERE name='Work')),
('Charlie Doe', NULL, '1999-12-01', (SELECT id FROM groups WHERE name='Family')),
('Dana White', 'dana@personal.me', '1992-07-24', (SELECT id FROM groups WHERE name='Friends')),
('Ethan Hunt', 'ethan@imf.com', '1983-09-12', (SELECT id FROM groups WHERE name='Work')),
('Fiona Clark', 'fiona@mail.com', NULL, (SELECT id FROM groups WHERE name='Friends')),
('George Hill', 'ghill@yahoo.com', '1975-11-02', (SELECT id FROM groups WHERE name='Family')),
('Hannah Lee', 'hannah@studio.io', '1998-06-15', (SELECT id FROM groups WHERE name='Work')),
('Ian Wright', NULL, '1993-03-09', (SELECT id FROM groups WHERE name='Other')),
('Julia Green', 'julia.green@gmail.com', NULL, (SELECT id FROM groups WHERE name='Friends'));

-- телефоны для каждого контакта
INSERT INTO phones (contact_id, phone, type) VALUES
((SELECT id FROM contacts WHERE name='Alice Smith'),   '555-1001', 'mobile'),
((SELECT id FROM contacts WHERE name='Alice Smith'),   '555-2221', 'home'),
((SELECT id FROM contacts WHERE name='Bob Brown'),     '555-4321', 'work'),
((SELECT id FROM contacts WHERE name='Charlie Doe'),   '555-9876', 'home'),
((SELECT id FROM contacts WHERE name='Dana White'),    '555-6543', 'mobile'),
((SELECT id FROM contacts WHERE name='Ethan Hunt'),    '555-1123', 'work'),
((SELECT id FROM contacts WHERE name='Fiona Clark'),   '555-7788', 'mobile'),
((SELECT id FROM contacts WHERE name='George Hill'),   '555-9944', 'home'),
((SELECT id FROM contacts WHERE name='Hannah Lee'),    '555-6611', 'work'),
((SELECT id FROM contacts WHERE name='Julia Green'),   '555-1357', 'mobile');
