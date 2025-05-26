CREATE TABLE cars (
    id INT AUTO_INCREMENT PRIMARY KEY,
    registration_number VARCHAR(7) NOT NULL UNIQUE,
    technical_inspection_date DATE NOT NULL,
    insurance_expiry_date DATE NOT NULL,
    owner_email NOT NULL
);
