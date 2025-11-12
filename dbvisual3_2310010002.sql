-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 12, 2025 at 12:53 AM
-- Server version: 8.0.30
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbvisual3_2310010002`
--

-- --------------------------------------------------------

--
-- Table structure for table `konsumen`
--

CREATE TABLE `konsumen` (
  `id_konsumen` varchar(10) NOT NULL,
  `nama_perusahaan` varchar(100) DEFAULT NULL,
  `alamat` text,
  `kontak` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `konsumen`
--

INSERT INTO `konsumen` (`id_konsumen`, `nama_perusahaan`, `alamat`, `kontak`) VALUES
('K001', 'PT Tambang Unlam', 'Jl. Kenari 1 ', '029232'),
('K002', 'PT Permain Suri', 'Jl.Kenari 1', '091821'),
('K003', 'PT Usaha Dunia', 'Jl Ahmad Yani', '091091021'),
('K004', 'PT Perusahaan Belakangan', 'Banjarmasin', '023923902');

-- --------------------------------------------------------

--
-- Table structure for table `pemesanan`
--

CREATE TABLE `pemesanan` (
  `id_pemesanan` varchar(10) NOT NULL,
  `id_konsumen` varchar(10) DEFAULT NULL,
  `produk_dipesan` varchar(100) DEFAULT NULL,
  `tanggal_pemesanan` date DEFAULT NULL,
  `total_harga` decimal(12,2) DEFAULT NULL,
  `status` enum('proses','selesai') DEFAULT 'proses'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `pemesanan`
--

INSERT INTO `pemesanan` (`id_pemesanan`, `id_konsumen`, `produk_dipesan`, `tanggal_pemesanan`, `total_harga`, `status`) VALUES
('PS001', 'K004', 'Batu Biasa Kijang', '2025-11-11', '121333.00', 'proses'),
('PS002', 'K001', 'BATU BARA', '2015-01-02', '100000.00', 'proses');

-- --------------------------------------------------------

--
-- Table structure for table `pengiriman`
--

CREATE TABLE `pengiriman` (
  `id_pengiriman` varchar(10) NOT NULL,
  `id_pemesanan` varchar(10) DEFAULT NULL,
  `tanggal_kirim` date DEFAULT NULL,
  `jumlah_kirim` int DEFAULT NULL,
  `kendaraan` varchar(50) DEFAULT NULL,
  `sopir` varchar(100) DEFAULT NULL,
  `status` enum('dikirim','selesai') DEFAULT 'dikirim'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `pengiriman`
--

INSERT INTO `pengiriman` (`id_pengiriman`, `id_pemesanan`, `tanggal_kirim`, `jumlah_kirim`, `kendaraan`, `sopir`, `status`) VALUES
('P001', 'PS001', '2015-01-01', 12, 'Tronton', 'Muhammad Ansari', 'selesai'),
('P002', 'PS001', '2015-01-01', 100, 'Tronton', 'Muhammad Bimo', 'dikirim'),
('P003', 'PS002', '2015-01-01', 15, 'Truck', 'Muhammad Bimo', 'dikirim');

-- --------------------------------------------------------

--
-- Table structure for table `produksi`
--

CREATE TABLE `produksi` (
  `id_produksi` varchar(10) NOT NULL,
  `id_pemesanan` varchar(10) DEFAULT NULL,
  `tanggal_produksi` date DEFAULT NULL,
  `jumlah_produksi` int DEFAULT NULL,
  `keterangan` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `produksi`
--

INSERT INTO `produksi` (`id_produksi`, `id_pemesanan`, `tanggal_produksi`, `jumlah_produksi`, `keterangan`) VALUES
('PR001', 'PS001', '2025-10-01', 10001, 'Sebuah Batu bara dengan api yang sangat besar'),
('PR002', 'PS002', '2025-01-01', 100, 'Sebuah Batu bara dengan api yang sangat besar'),
('PR003', 'PS002', '2025-01-01', 100, 'Sebuah Batu bara dengan api yang sangat besar'),
('PR004', 'PS001', '2025-01-01', 100, 'Sebuah Batu bara dengan api yang sangat besar');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `konsumen`
--
ALTER TABLE `konsumen`
  ADD PRIMARY KEY (`id_konsumen`);

--
-- Indexes for table `pemesanan`
--
ALTER TABLE `pemesanan`
  ADD PRIMARY KEY (`id_pemesanan`),
  ADD KEY `pemesanan_ibfk_1` (`id_konsumen`);

--
-- Indexes for table `pengiriman`
--
ALTER TABLE `pengiriman`
  ADD PRIMARY KEY (`id_pengiriman`),
  ADD KEY `fk_pengiriman_pemesanan` (`id_pemesanan`);

--
-- Indexes for table `produksi`
--
ALTER TABLE `produksi`
  ADD PRIMARY KEY (`id_produksi`),
  ADD KEY `fk_produksi_pemesanan` (`id_pemesanan`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `pemesanan`
--
ALTER TABLE `pemesanan`
  ADD CONSTRAINT `pemesanan_ibfk_1` FOREIGN KEY (`id_konsumen`) REFERENCES `konsumen` (`id_konsumen`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `pengiriman`
--
ALTER TABLE `pengiriman`
  ADD CONSTRAINT `fk_pengiriman_pemesanan` FOREIGN KEY (`id_pemesanan`) REFERENCES `pemesanan` (`id_pemesanan`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `produksi`
--
ALTER TABLE `produksi`
  ADD CONSTRAINT `fk_produksi_pemesanan` FOREIGN KEY (`id_pemesanan`) REFERENCES `pemesanan` (`id_pemesanan`) ON DELETE SET NULL ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
