


DROP DATABASE IF EXISTS FuelDummy;
CREATE DATABASE FuelDummy;

use FuelDummy;


CREATE TABLE Login_Info (
  Username_ID int(11) PRIMARY KEY NOT NULL auto_increment,
  Username varchar(45) NOT NULL,
  Passwd varchar(45) NOT NULL,
  Type_of_user varchar(45) NOT NULL,
  Register_Date DATE NOT NULL COMMENT 'When they first register'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (1, 'username_01', 'password_01', 'manager');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (2, 'username_02', 'password_02', 'agent');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (3, 'username_03', 'password_03', 'agent');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (4, 'username_04', 'password_04', 'agent');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (5, 'username_05', 'password_05', 'agent');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (6, 'username_06', 'password_06', 'client');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (7, 'username_07', 'password_07', 'client');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (8, 'username_08', 'password_08', 'client');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (9, 'username_09', 'password_09', 'client');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (10, 'username_10', 'password_10', 'client');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (11, 'username_11', 'password_11', 'client');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (12, 'username_12', 'password_12', 'client');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (13, 'username_13', 'password_13', 'client');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (14, 'username_14', 'password_14', 'client');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (15, 'username_15', 'password_15', 'client');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (16, 'username_16', 'password_16', 'client');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (17, 'username_17', 'password_17', 'client');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (18, 'username_18', 'password_18', 'client');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (19, 'username_19', 'password_19', 'client');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (20, 'username_20', 'password_20', 'client');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (21, 'username_21', 'password_21', 'client');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (22, 'username_22', 'password_22', 'client');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (23, 'username_23', 'password_23', 'client');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (24, 'username_24', 'password_24', 'client');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (25, 'username_25', 'password_25', 'client');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (26, 'username_26', 'password_26', 'client');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (27, 'username_27', 'password_27', 'client');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (28, 'username_28', 'password_28', 'client');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (29, 'username_29', 'password_29', 'client');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (30, 'username_30', 'password_30', 'client');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (31, 'username_31', 'password_31', 'client');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (32, 'username_32', 'password_32', 'client');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (33, 'username_33', 'password_33', 'client');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (34, 'username_34', 'password_34', 'client');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (35, 'username_35', 'password_35', 'client');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (36, 'username_36', 'password_36', 'client');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (37, 'username_37', 'password_37', 'client');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (38, 'username_38', 'password_38', 'client');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (39, 'username_39', 'password_39', 'client');
INSERT INTO Login_Info(Username_ID, Username, Passwd, Type_of_user)
VALUES (40, 'username_40', 'password_40', 'client');



 CREATE TABLE Quote (
  Quote_ID int(11) NOT NULL auto_increment,
  Number_of_Gallons int(11) NOT NULL,
  Price decimal(8,2) NOT NULL,
  Request_Date DATE NOT NULL COMMENT 'When they placed the order',
  Request_Delivery_Date DATE NOT NULL COMMENT 'When they expect the order',
  Username_ID int(11) NOT NULL,
  PRIMARY KEY (Quote_ID),
  FOREIGN KEY (Username_ID)
  REFERENCES Login_Info (Username_ID)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



CREATE TABLE Invoice (
  Invoice_ID int(11) NOT NULL auto_increment,
  Delivery_Date datetime NULL COMMENT 'When they deliver the obj',
  Username_ID int(11) NOT NULL,
  Paid INT NOT NULL,
  Quote_ID int(11) NOT NULL,
  PRIMARY KEY (Invoice_ID),
  FOREIGN KEY (Quote_ID)
  REFERENCES Quote (Quote_ID)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;






CREATE TABLE Profile_for_Users (
  Company_Name varchar(45) NOT NULL,
  Username_ID int(11) NOT NULL,
  Profile_ID int(11) NOT NULL auto_increment,
  First_Name varchar(45) NULL,
  Last_Name varchar(45) NULL,
  Address varchar(45) NULL,
  Address2 varchar(45) NULL,
  City varchar(45) NULL,
  State varchar(2) NULL,
  Zipcode int(5) NULL,
  PRIMARY KEY (Profile_ID),
  FOREIGN KEY (Username_ID)
  REFERENCES Login_Info (Username_ID)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



INSERT INTO Profile_for_Users (Company_Name, UserName_ID, Profile_ID, First_Name, Last_Name, Address, City, State, Zipcode)
VALUES ('Alfa', 1, 1, 'Luis', 'M', 'address_01', 'city_01', 'TX' , 11111);
INSERT INTO Profile_for_Users (Company_Name, UserName_ID, Profile_ID, First_Name, Last_Name, Address, City, State, Zipcode)
VALUES ('Bravo', 2, 2, 'Kazem', 'G', 'address_02', 'city_02', 'NY' , 11112);
INSERT INTO Profile_for_Users (Company_Name, UserName_ID, Profile_ID, First_Name, Last_Name, Address, City, State, Zipcode)
VALUES ('Charlie', 3, 3, 'Suyog', 'R', 'address_03', 'city_03', 'CH' , 11113);
INSERT INTO Profile_for_Users (Company_Name, UserName_ID, Profile_ID, First_Name, Last_Name, Address, City, State, Zipcode)
VALUES ('Delta', 4, 4, 'Summit', 'K', 'address_04', 'city_04', 'KN' , 11114);
INSERT INTO Profile_for_Users (Company_Name, UserName_ID, Profile_ID, First_Name, Last_Name, Address, City, State, Zipcode)
VALUES ('Echo', 5, 5, 'Shorty', 'L', 'address_05', 'city_05', 'KA' , 11115);
INSERT INTO Profile_for_Users (Company_Name, UserName_ID, Profile_ID, First_Name, Last_Name, Address, City, State, Zipcode)
VALUES ('Foxtrot', 6, 6, 'Waffle', 'P', 'address_06', 'city_06', 'OK' , 11116);
INSERT INTO Profile_for_Users (Company_Name, UserName_ID, Profile_ID, First_Name, Last_Name, Address, City, State, Zipcode)
VALUES ('Golf', 7, 7, 'Lirik', 'O', 'address_07', 'city_07', 'RI' , 11117);
INSERT INTO Profile_for_Users (Company_Name, UserName_ID, Profile_ID, First_Name, Last_Name, Address, City, State, Zipcode)
VALUES ('Hotel', 8, 8, 'Poke', 'B', 'address_08', 'city_08', 'GH' , 11118);
INSERT INTO Profile_for_Users (Company_Name, UserName_ID, Profile_ID, First_Name, Last_Name, Address, City, State, Zipcode)
VALUES ('India', 9, 9, 'Lily', 'V', 'address_09', 'city_09', 'JK' , 11119);
INSERT INTO Profile_for_Users (Company_Name, UserName_ID, Profile_ID, First_Name, Last_Name, Address, City, State, Zipcode)
VALUES ('Julliet', 10, 10, 'Patrick', 'C', 'address_10', 'city_10', 'DF' , 11120);
INSERT INTO Profile_for_Users (Company_Name, UserName_ID, Profile_ID, First_Name, Last_Name, Address, City, State, Zipcode)
VALUES ('Kilo', 11, 11, 'Spongebob', 'Y', 'address_11', 'city_11', 'TH' , 11121);
INSERT INTO Profile_for_Users (Company_Name, UserName_ID, Profile_ID, First_Name, Last_Name, Address, City, State, Zipcode)
VALUES ('Lima', 12, 12, 'Sandy', 'O', 'address_12', 'city_12', 'RI' , 11122);
INSERT INTO Profile_for_Users (Company_Name, UserName_ID, Profile_ID, First_Name, Last_Name, Address, City, State, Zipcode)
VALUES ('Mike', 13, 13, 'Crabs', 'M', 'address_13', 'city_13', 'RI' , 11123);
INSERT INTO Profile_for_Users (Company_Name, UserName_ID, Profile_ID, First_Name, Last_Name, Address, City, State, Zipcode)
VALUES ('November', 14, 14, 'Squidward', 'A', 'address_14', 'city_14', 'PL' , 11124);
INSERT INTO Profile_for_Users (Company_Name, UserName_ID, Profile_ID, First_Name, Last_Name, Address, City, State, Zipcode)
VALUES ('Oscar', 15, 15, 'Larry', 'S', 'address_15', 'city_15', 'RE' , 11125);
INSERT INTO Profile_for_Users (Company_Name, UserName_ID, Profile_ID, First_Name, Last_Name, Address, City, State, Zipcode)
VALUES ('Papa', 16, 16, 'Homer', 'H', 'address_16', 'city_16', 'GR' , 11126);
INSERT INTO Profile_for_Users (Company_Name, UserName_ID, Profile_ID, First_Name, Last_Name, Address, City, State, Zipcode)
VALUES ('Quebec', 17, 17, 'Lisa', 'D', 'address_17', 'city_17', 'FL' , 11127);
INSERT INTO Profile_for_Users (Company_Name, UserName_ID, Profile_ID, First_Name, Last_Name, Address, City, State, Zipcode)
VALUES ('Romeo', 18, 18, 'Bart', 'X', 'address_18', 'city_18', 'OL' , 11128);
INSERT INTO Profile_for_Users (Company_Name, UserName_ID, Profile_ID, First_Name, Last_Name, Address, City, State, Zipcode)
VALUES ('Sierra', 19, 19, 'Marge', 'W', 'address_19', 'city_19', 'FL' , 11129);
INSERT INTO Profile_for_Users (Company_Name, UserName_ID, Profile_ID, First_Name, Last_Name, Address, City, State, Zipcode)
VALUES ('Tango', 20, 20, 'Skinner', 'I', 'address_20', 'city_20', 'NM' , 11130);
INSERT INTO Profile_for_Users (Company_Name, UserName_ID, Profile_ID, First_Name, Last_Name, Address, City, State, Zipcode)
VALUES ('Uniform', 21, 21, 'Seymour', 'U', 'address_21', 'city_21', 'CO' , 11131);
INSERT INTO Profile_for_Users (Company_Name, UserName_ID, Profile_ID, First_Name, Last_Name, Address, City, State, Zipcode)
VALUES ('Victor', 22, 22, 'Ned', 'J', 'address_22', 'city_22', 'WA' , 11132);
INSERT INTO Profile_for_Users (Company_Name, UserName_ID, Profile_ID, First_Name, Last_Name, Address, City, State, Zipcode)
VALUES ('Whiskey', 23, 23, 'Ramon', 'Z', 'address_23', 'city_23', 'IO' , 11133);
INSERT INTO Profile_for_Users (Company_Name, UserName_ID, Profile_ID, First_Name, Last_Name, Address, City, State, Zipcode)
VALUES ('Xray', 24, 24, 'Pepe', 'J', 'address_24', 'city_24', 'KS' , 11134);
INSERT INTO Profile_for_Users (Company_Name, UserName_ID, Profile_ID, First_Name, Last_Name, Address, City, State, Zipcode)
VALUES ('Yankee', 25, 25, 'Bike', 'T', 'address_25', 'city_25', 'QW' , 11135);
INSERT INTO Profile_for_Users (Company_Name, UserName_ID, Profile_ID, First_Name, Last_Name, Address, City, State, Zipcode)
VALUES ('Zulu', 26, 26, 'Lukaku', 'L', 'address_26', 'city_26', 'VB' , 11136);


CREATE TABLE Competitors (
  Competitor_ID int(11) NULL auto_increment,
  Competitor_name varchar(45) NOT NULL,
  January decimal(4,0) NULL,
  February decimal(4,0) NULL,
  March decimal(4,0) NULL,
  April decimal(4,0) NULL,
  May decimal(4,0) NULL,
  June decimal(4,0) NULL,
  July decimal(4,0) NULL,
  August decimal(4,0) NULL,
  September decimal(4,0) NULL,
  October decimal(4,0) NULL,
  November decimal(4,0) NULL,
  December decimal(4,0) NULL,
  Competitor_year int(11) NOT NULL,
  PRIMARY KEY (Competitor_ID)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



