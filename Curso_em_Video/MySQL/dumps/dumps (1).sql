CREATE DATABASE  IF NOT EXISTS `cadastro` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `cadastro`;
-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: cadastro
-- ------------------------------------------------------
-- Server version	9.1.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cursos`
--

DROP TABLE IF EXISTS `cursos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cursos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  `descricao` varchar(255) NOT NULL,
  `carga` int NOT NULL,
  `t_aulas` int DEFAULT NULL,
  `ano` year NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cursos`
--

LOCK TABLES `cursos` WRITE;
/*!40000 ALTER TABLE `cursos` DISABLE KEYS */;
INSERT INTO `cursos` VALUES (1,'Python','Linguagem versátil e fácil de aprender.',40,20,2013),(2,'Java','Popular para aplicações corporativas.',50,25,2014),(3,'C++','Ideal para programação de sistemas e jogos.',60,30,2015),(4,'JavaScript','Linguagem essencial para o desenvolvimento web.',45,22,2016),(5,'Ruby','Linguagem focada em simplicidade e produtividade.',35,18,2013),(6,'C#','Ótima para desenvolvimento na plataforma .NET.',55,27,2017),(7,'PHP','Muito usada em desenvolvimento web dinâmico.',50,25,2018),(8,'Swift','Desenvolvida pela Apple para iOS e macOS.',40,20,2019),(9,'Kotlin','Linguagem moderna para Android e muito mais.',45,22,2020),(10,'R','Popular para ciência de dados e estatísticas.',50,25,2021),(11,'Go','Linguagem eficiente desenvolvida pelo Google.',60,30,2016),(12,'Rust','Confiável para sistemas de alto desempenho.',55,27,2020),(13,'Scala','Combina orientação a objetos e funcional.',50,25,2014),(14,'Perl','Conhecida por sua força em manipulação de texto.',40,20,2015),(15,'Lua','Linguagem leve para jogos e sistemas embarcados.',35,18,2017),(16,'TypeScript','Superset do JavaScript com tipagem estática.',45,22,2018),(17,'Dart','Focada no desenvolvimento de aplicações Flutter.',50,25,2019),(18,'Haskell','Poderosa linguagem funcional.',60,30,2014),(19,'Elixir','Linguagem funcional para aplicações escaláveis.',55,27,2015),(20,'Shell Script','Automatiza tarefas no sistema operacional.',40,20,2016),(21,'Objective-C','Linguagem predecessora do Swift.',50,25,2013),(22,'F#','Linguagem funcional para .NET.',45,22,2017),(23,'VB.NET','Voltada para aplicativos Windows.',50,25,2018),(24,'MATLAB','Utilizada em engenharia e ciências.',60,30,2019),(25,'COBOL','Muito usada em sistemas financeiros.',55,27,2014),(26,'Fortran','Popular em computação científica.',50,25,2015),(27,'Pascal','Clássica para introdução à programação.',40,20,2013),(28,'Delphi','Focada em aplicações desktop.',45,22,2016),(29,'SQL','Linguagem para gerenciamento de bancos de dados.',50,25,2017),(30,'PL/SQL','Extensão do SQL para Oracle.',60,30,2018),(31,'Prolog','Focada em inteligência artificial.',55,27,2014),(32,'Lisp','Clássica em IA e processamento simbólico.',50,25,2013),(33,'Àssembly','Linguagem de baixo nível para sistemas.',40,20,2015),(34,'Scratch','Desenvolvida para ensino de lógica.',35,18,2016),(35,'Ada','Linguagem robusta para sistemas críticos.',45,22,2018),(36,'Clojure','Linguagem funcional moderna.',50,25,2019),(37,'Erlang','Linguagem para sistemas distribuídos.',60,30,2020),(38,'Smalltalk','Clássica em orientação a objetos.',55,27,2013),(39,'Julia','Focada em computação de alto desempenho.',50,25,2019),(40,'ABAP','Usada em sistemas SAP.',40,20,2018),(41,'Groovy','Flexível para a plataforma Java.',45,22,2017),(42,'VHDL','Focada em hardware.',50,25,2016),(43,'Verilog','Outra linguagem para design de hardware.',60,30,2021),(44,'RPG','Usada em sistemas de mainframe.',55,27,2015),(45,'APL','Focada em cálculos matemáticos.',50,25,2013),(46,'Tcl','Ideal para scripts e prototipagem.',40,20,2016),(47,'Awk','Processamento de textos e dados.',35,18,2018),(48,'Simula','Predecessora de linguagens orientadas a objetos.',45,22,2020);
/*!40000 ALTER TABLE `cursos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gafanhotos`
--

DROP TABLE IF EXISTS `gafanhotos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gafanhotos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `profissao` varchar(50) NOT NULL,
  `nascimento` date NOT NULL,
  `sexo` enum('M','F') NOT NULL,
  `peso` decimal(5,2) NOT NULL,
  `altura` decimal(4,2) NOT NULL,
  `nacionalidade` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gafanhotos`
--

LOCK TABLES `gafanhotos` WRITE;
/*!40000 ALTER TABLE `gafanhotos` DISABLE KEYS */;
INSERT INTO `gafanhotos` VALUES (1,'João Silva','Professor','1990-05-15','M',75.50,1.75,'Brasileiro'),(2,'Maria Oliveira','Médica','1985-10-30','F',60.00,1.65,'Brasileira'),(3,'Carlos Souza','Engenheiro','1992-07-21','M',80.30,1.80,'Português'),(4,'Ana Paula','Advogada','1988-12-05','F',68.50,1.70,'USA'),(5,'Luiz Santos','Desenvolvedor','1995-03-12','M',70.20,1.78,'Argentino'),(6,'Camila Rocha','Designer','1993-08-25','F',58.00,1.62,'Brasileira'),(7,'Pedro Almeida','Empresário','1980-11-11','M',85.00,1.85,'Chileno'),(8,'Juliana Ribeiro','Psicóloga','1996-04-18','F',65.00,1.68,'Brasileira'),(9,'Rafael Costa','Chef de Cozinha','1987-09-30','M',78.50,1.72,'Mexicano'),(10,'Fernanda Lima','Arquiteta','1991-06-14','F',62.50,1.66,'Brasileira'),(11,'Ana Silva','Engenheira','1992-04-15','F',68.50,1.65,'Brasil'),(12,'Carlos Souza','Professor','1987-09-10','M',80.30,1.75,'Brasil'),(13,'Mariana Costa','Designer','1995-06-21','F',54.00,1.60,'Brasil'),(14,'John Smith','Developer','1990-03-22','M',85.00,1.80,'Estados Unidos'),(15,'Emily Davis','Médica','1993-11-08','F',62.00,1.68,'Estados Unidos'),(16,'Robert Brown','Advogado','1985-01-12','M',78.00,1.74,'Estados Unidos'),(17,'Rajesh Kumar','Engenheiro','1991-05-13','M',72.00,1.70,'Índia'),(18,'Priya Sharma','Professora','1996-02-25','F',58.50,1.65,'Índia'),(19,'Amit Patel','Empresário','1988-08-14','M',75.00,1.75,'Índia'),(20,'Hiroshi Tanaka','Desenvolvedor','1994-07-17','M',67.00,1.68,'Japão'),(21,'Sakura Yamamoto','Artista','1990-12-03','F',50.00,1.55,'Japão'),(22,'Kenji Nakamura','Professor','1989-03-19','M',60.00,1.65,'Japão'),(23,'Liam Wilson','Engenheiro','1992-10-30','M',81.00,1.78,'Canadá'),(24,'Sophia Johnson','Enfermeira','1995-01-25','F',57.00,1.65,'Reino Unido'),(25,'Lucas Martins','Advogado','1988-09-09','M',90.00,1.80,'Brasil'),(26,'Isabela Oliveira','Nutricionista','1993-03-15','F',60.50,1.70,'Brasil'),(27,'Ethan Clark','Arquiteto','1989-07-01','M',82.00,1.76,'Austrália'),(28,'Olivia Taylor','Cientista','1994-05-19','F',65.00,1.62,'Canadá'),(29,'Noah Baker','Jornalista','1990-12-10','M',78.00,1.74,'Estados Unidos'),(30,'Emma Harris','Médica','1997-06-20','F',55.00,1.60,'Reino Unido'),(31,'Aiden Martinez','Veterinário','1987-04-18','M',73.00,1.72,'Espanha'),(32,'Sophia Gonzalez','Designer','1993-12-05','F',59.50,1.67,'México'),(33,'Mateo Lopez','Arquiteto','1986-07-08','M',77.00,1.79,'Argentina'),(34,'Mia Torres','Bióloga','1992-02-14','F',62.00,1.68,'Colômbia'),(35,'Luna Perez','Artista','1994-09-21','F',53.00,1.57,'Chile'),(36,'Benjamin Evans','Psicólogo','1990-11-11','M',80.00,1.81,'Austrália'),(37,'Isabella Carter','Cientista','1995-03-30','F',65.50,1.70,'Canadá'),(38,'Ethan Lewis','Jornalista','1988-05-25','M',78.20,1.75,'Irlanda'),(39,'Olivia Walker','Médica','1993-08-04','F',58.00,1.66,'Reino Unido'),(40,'Logan Hall','Engenheiro','1992-01-15','M',85.00,1.85,'EUA'),(41,'Emma Allen','Advogada','1996-10-10','F',60.00,1.68,'França'),(42,'Jack Wright','Professor','1987-06-14','M',74.00,1.78,'Alemanha'),(43,'Sophia King','Veterinária','1991-07-22','F',59.50,1.69,'Austrália'),(44,'Lucas Scott','Artista','1988-04-09','M',76.00,1.73,'Brasil'),(45,'Liam Young','Músico','1985-09-19','M',80.00,1.77,'Canadá'),(46,'Charlotte Adams','Nutricionista','1994-12-31','F',54.00,1.60,'Espanha'),(47,'Henry Green','Desenvolvedor','1989-08-18','M',72.00,1.70,'Japão'),(48,'Mila Moore','Designer','1992-06-27','F',56.00,1.64,'Itália'),(49,'Eleanor James','Cientista','1993-10-12','F',67.00,1.73,'Irlanda'),(50,'James Anderson','Engenheiro','1991-01-20','M',90.00,1.88,'EUA');
/*!40000 ALTER TABLE `gafanhotos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-18 20:01:05
