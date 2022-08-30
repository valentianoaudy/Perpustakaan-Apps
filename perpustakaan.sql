-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 23, 2022 at 11:34 AM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 7.3.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `perpustakaan`
--

-- --------------------------------------------------------

--
-- Table structure for table `perpustakaan`
--

CREATE TABLE `perpustakaan` (
  `kode` int(11) NOT NULL,
  `judul` varchar(200) NOT NULL,
  `tahun` varchar(4) NOT NULL,
  `isbn` varchar(13) NOT NULL,
  `pengarang` varchar(200) NOT NULL,
  `penerbit` varchar(200) NOT NULL,
  `rak` varchar(200) NOT NULL,
  `stok` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `perpustakaan`
--

INSERT INTO `perpustakaan` (`kode`, `judul`, `tahun`, `isbn`, `pengarang`, `penerbit`, `rak`, `stok`) VALUES
(1, 'IPAS SD KELAS IV', '2019', '9786022443735', 'Amalia Fitri Dkk', 'Pusat Kurikulum dan Perbukuan', '1', '25'),
(2, 'Prakarya dan Kewirausahaan Kelas XII', '2019', '9786024271589', 'Hendriana Werdhaningsih, Wawat Naswati, Desta Wirnas, Rinrin Jamriati', 'Pusat Kurikulum dan Perbukuan, Balitbang, Kemendikbud', '2', '25'),
(3, 'Sejarah Indonesia Kelas XII', '2019', '9786024271251', 'Abdurakhman, Arif Pradono, Linda Sunarti, Susanto Zuhdi', 'Pusat Kurikulum dan Perbukuan, Balitbang, Kemendikbud', '2', '25'),
(4, 'Seni Budaya Kelas XII', '2019', '9786024271473', 'Agus Budiman, Dewi Suryati Budiwati, Sukanta, dan Zakaria S. Soetedja', 'Pusat Kurikulum dan Perbukuan, Balitbang, Kemendikbud', '2', '25'),
(5, 'Pendidikan Agama Hindu dan Budi Pekerti Kelas VII', '2017', '9786022829379', 'Ida Made Sugita', 'Pusat Kurikulum dan Perbukuan, Balitbang, Kemendikbud', '3', '25'),
(6, 'Pendidikan Agama Kristen dan Budi Pekerti Kelas IX', '2018', '9786022822769', 'Pdt. Stephen Suleeman dan Pdt. Dien Sumiyatiningsih', 'Pusat Kurikulum dan Perbukuan, Balitbang, Kemendikbud', '4', '25'),
(7, 'Pendidikan Jasmani, Olahraga, dan Kesehatan Kelas VII', '2017', '978-602-427-0', 'Muhajir', 'Pusat Kurikulum dan Perbukuan, Balitbang, Kemendikbud', '5', '25'),
(8, 'Pendidikan Pancasila dan Kewarganegaraan Kelas XI', '2017', '9786024270926', 'Yusnawan Lubis Mohamad Sodeli', 'Pusat Kurikulum dan Perbukuan, Balitbang, Kemendikbud', '2', '50'),
(9, 'Bahasa Inggris Kelas XI', '2017', '9786024271084', 'Mahrukh Bashir', 'Pusat Kurikulum dan Perbukuan, Balitbang, Kemendikbud', '7', '50');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `perpustakaan`
--
ALTER TABLE `perpustakaan`
  ADD PRIMARY KEY (`kode`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `perpustakaan`
--
ALTER TABLE `perpustakaan`
  MODIFY `kode` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
