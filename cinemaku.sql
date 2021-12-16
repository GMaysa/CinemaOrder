-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 16, 2021 at 08:08 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cinemaku`
--

-- --------------------------------------------------------

--
-- Table structure for table `cinema_film`
--

CREATE TABLE `cinema_film` (
  `id_film` int(12) NOT NULL,
  `nama_film` varchar(100) NOT NULL,
  `desc_film` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `cinema_show`
--

CREATE TABLE `cinema_show` (
  `id_show` int(12) NOT NULL,
  `price_show` int(8) NOT NULL,
  `filmId` int(12) NOT NULL,
  `theatreId` int(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `cinema_theatre`
--

CREATE TABLE `cinema_theatre` (
  `id` int(12) NOT NULL,
  `seat` int(12) NOT NULL,
  `id_film` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `cinema_ticket`
--

CREATE TABLE `cinema_ticket` (
  `id_ticket` int(12) NOT NULL,
  `user_name` varchar(100) NOT NULL,
  `payment` varchar(50) NOT NULL,
  `showId` int(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cinema_film`
--
ALTER TABLE `cinema_film`
  ADD PRIMARY KEY (`id_film`);

--
-- Indexes for table `cinema_show`
--
ALTER TABLE `cinema_show`
  ADD PRIMARY KEY (`id_show`),
  ADD KEY `filmId` (`filmId`),
  ADD KEY `theatreId` (`theatreId`);

--
-- Indexes for table `cinema_theatre`
--
ALTER TABLE `cinema_theatre`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_film` (`id_film`);

--
-- Indexes for table `cinema_ticket`
--
ALTER TABLE `cinema_ticket`
  ADD PRIMARY KEY (`id_ticket`),
  ADD KEY `showId` (`showId`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cinema_theatre`
--
ALTER TABLE `cinema_theatre`
  MODIFY `id` int(12) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `cinema_ticket`
--
ALTER TABLE `cinema_ticket`
  MODIFY `id_ticket` int(12) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `cinema_show`
--
ALTER TABLE `cinema_show`
  ADD CONSTRAINT `cinema_show_ibfk_1` FOREIGN KEY (`theatreId`) REFERENCES `cinema_theatre` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `cinema_theatre`
--
ALTER TABLE `cinema_theatre`
  ADD CONSTRAINT `cinema_theatre_ibfk_1` FOREIGN KEY (`id_film`) REFERENCES `cinema_film` (`id_film`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `cinema_ticket`
--
ALTER TABLE `cinema_ticket`
  ADD CONSTRAINT `cinema_ticket_ibfk_1` FOREIGN KEY (`showId`) REFERENCES `cinema_show` (`id_show`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
