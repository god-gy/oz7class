CREATE DATABASE pet_hotel;
USE pet_hotel;
CREATE TABLE PetOwners(
	ownerId int PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20) not null,
	contact VARCHAR(50)
);
CREATE TABLE Pets(
	petId INT PRIMARY KEY AUTO_INCREMENT,
    ownerId INT,
    name VARCHAR(20) not null,
    species VARCHAR(50),
    breed VARCHAR(50),
    FOREIGN KEY (ownerID) REFERENCES PetOwners(ownerID)
);
CREATE TABLE Rooms(
	roomId INT PRIMARY KEY AUTO_INCREMENT,
    roomNumber INT not null,
    roomType VARCHAR(20) not null,
    pricePerNight INT not null
);

CREATE TABLE Reservations(
	reservationId INT PRIMARY KEY AUTO_INCREMENT,
    petId INT,
    roomId INT,
    startDate date not null,
    endDate date not null,
    FOREIGN KEY (petId) REFERENCES Pets(petId),
    FOREIGN KEY (roomId) REFERENCES Rooms(roomId)
);

CREATE TABLE Services(
	serviceId INT PRIMARY KEY AUTO_INCREMENT,
    reservationId INT,
    serviceName VARCHAR(20) not null,
    servicePrice INT not null,
    FOREIGN KEY (reservationId) REFERENCES Reservations(reservationId)
);

