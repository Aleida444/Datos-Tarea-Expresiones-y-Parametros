create database Ropa ;

Use Ropa;

drop table Empleados;

create table tallas ( talla_id int primary key, talla_name varchar(10))
ENGINE = innodb;

create table color ( color_id int primary key, color_name varchar(50))
ENGINE = innodb;

create table Departamento ( dep_id int primary key, dep_name varchar(50))
ENGINE = innodb;

create table Sexo ( sexo_id int primary key, sexo_name varchar(50))
ENGINE = innodb;

create table temporada ( temp_id int primary key, temp_name varchar(50))
ENGINE = innodb;

create table Pais ( pais_id int primary key, pais_name varchar(100))
ENGINE = innodb;

create table Sucursal ( Suc_id int primary key, Suc_name varchar(100))
ENGINE = innodb;

create table reciclado ( rec_id int primary key, rec_name varchar(10))
ENGINE = innodb;

create table comision ( Com_id int primary key, Com_name varchar(100))
ENGINE = innodb;

create table material ( Mat_id int primary key, Mat_name varchar(100))
ENGINE = innodb;

create table descuento ( desc_id int primary key, desc_name varchar(50))
ENGINE = innodb;

create table Meses ( MSI_id int primary key, MSI_name varchar(10))
ENGINE = innodb;

create table Turno ( turno_id int primary key, turno_name varchar(10))
ENGINE = innodb;

create table  Acepta_DEV( Acepta_DEV_id int primary key, acepta_DEV_value varchar(10))
ENGINE = innodb;

create table Empleos ( Job_id int primary key, job_name varchar(100))
ENGINE = innodb;

create table Inventario (
    
	Product_id  int primary key, 
    talla_id int not null,
    FOREIGN KEY (talla_id) REFERENCES tallas(talla_id),
    color_id int not null,
    FOREIGN KEY (color_id) REFERENCES color(color_id),
    sexo_id int not null,
    FOREIGN KEY (sexo_id) REFERENCES Sexo(sexo_id),
    temp_id int not null,
    FOREIGN KEY (temp_id) REFERENCES temporada(temp_id),
    pais_id int not null,
    FOREIGN KEY (pais_id) REFERENCES Pais(pais_id),
    Suc_id int not null,
    FOREIGN KEY (Suc_id) REFERENCES Sucursal(Suc_id),
    rec_id int not null,
    FOREIGN KEY (rec_id) REFERENCES reciclado(rec_id),
    dep_id int not null,
    FOREIGN KEY (dep_id) REFERENCES Departamento(dep_id),
    Com_id int not null,
    FOREIGN KEY (Com_id) REFERENCES comision(Com_id),
    Mat_id int not null,
    FOREIGN KEY (Mat_id) REFERENCES material(Mat_id),
    desc_id int not null,
    FOREIGN KEY (desc_id) REFERENCES descuento(desc_id),
	MSI_id int not null,
    FOREIGN KEY (MSI_id) REFERENCES Meses(MSI_id),
    precio decimal (10,2),
    llegada date not null,
    Acepta_DEV_id int not null,
    FOREIGN KEY (Acepta_DEV_id) REFERENCES Acepta_DEV(Acepta_DEV_id)
)
ENGINE = innodb;

CREATE TABLE nivel_salario (
    grade INT primary key,
    min_sal INT,
    max_sal INT
)
ENGINE = innodb;

INSERT INTO nivel_salario (grade, min_sal, max_sal)
VALUES
    (1, 800, 1300),
    (2, 1301, 1500),
    (3, 1501, 2100),
    (4, 2101, 3100),
    (5, 3101, 9999);

create table Empleados (
	emp_id int primary key,
    emp_name varchar(15) not null,
    Suc_id int not null,
    FOREIGN KEY (Suc_id) REFERENCES Sucursal(Suc_id),
    Job_id int not null,
    FOREIGN KEY (Job_id) REFERENCES Empleos(Job_id),
    dep_id int not null,
    FOREIGN KEY (dep_id) REFERENCES Departamento(dep_id),
    Com_id decimal(10,2) ,
    grade int not null,
    FOREIGN KEY(grade) REFERENCES nivel_salario(grade),
    manager_id int default 0,
    hire_date date not null,
    turno_id int not null,
    FOREIGN KEY (turno_id) REFERENCES Turno(turno_id)
)
ENGINE = innodb;

create table venta (
    Sell_id int not null primary key, 
    Product_id int not null,
    FOREIGN KEY (Product_id) REFERENCES Inventario(Product_id),
    Fecha_sell date not null,
	emp_id int not null,
    FOREIGN KEY (emp_id) REFERENCES Empleados(emp_id)
)
ENGINE = innodb;

create table devolución (
    Dev_id int not null primary key, 
    Product_id int not null,
    FOREIGN KEY (Product_id) REFERENCES Inventario(Product_id),
    Sell_id int not null, 
    FOREIGN KEY (Sell_id) REFERENCES venta(Sell_id),
    Fecha_dev date not null,
	emp_id int not null,
    FOREIGN KEY (emp_id) REFERENCES Empleados(emp_id)
)
ENGINE = innodb;
