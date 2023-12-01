-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 12, 2021 at 03:00 PM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `db_agrobazar`
--

-- --------------------------------------------------------

--
-- Table structure for table `payments`
--

CREATE TABLE IF NOT EXISTS `payments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cartid` int(11) NOT NULL,
  `customerid` int(11) NOT NULL,
  `productid` int(11) NOT NULL,
  `cardnumber` bigint(40) NOT NULL,
  `cvv` int(5) NOT NULL,
  `nameoncard` varchar(30) NOT NULL,
  `expiration` varchar(12) NOT NULL,
  `price` int(12) NOT NULL,
  `status` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=23 ;

--
-- Dumping data for table `payments`
--

INSERT INTO `payments` (`id`, `cartid`, `customerid`, `productid`, `cardnumber`, `cvv`, `nameoncard`, `expiration`, `price`, `status`) VALUES
(22, 46, 12, 19, 9999, 999, 'customer', '2021-12', 1500, 'paid');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_addproduct`
--

CREATE TABLE IF NOT EXISTS `tbl_addproduct` (
  `farmerid` int(11) NOT NULL,
  `productid` int(11) NOT NULL AUTO_INCREMENT,
  `productname` varchar(50) NOT NULL,
  `category` varchar(50) NOT NULL,
  `description` varchar(100) NOT NULL,
  `price` int(100) NOT NULL,
  `image` varchar(200) NOT NULL,
  `status` int(40) NOT NULL,
  PRIMARY KEY (`productid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=24 ;

--
-- Dumping data for table `tbl_addproduct`
--

INSERT INTO `tbl_addproduct` (`farmerid`, `productid`, `productname`, `category`, `description`, `price`, `image`, `status`) VALUES
(11, 18, 'chilly', 'grains', 'kashmeri chilly', 300, '/media/chilly_XncW6pZ.jpg', 1),
(11, 19, 'spiceskit', 'grains', 'A collection of masala spices', 500, '/media/spices_6BrB51H.jpg', 1),
(11, 22, 'Pumpkin', 'vegitables', 'quality product', 200, '/media/pumpkin_Krh6j7a.jpg', 1),
(11, 23, 'Apple', 'fruits', 'kashmeri apple', 400, '/media/green%20apple_aqO5eeq.jfif', 1);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_allocation`
--

CREATE TABLE IF NOT EXISTS `tbl_allocation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `deliveryboyid` int(11) NOT NULL,
  `customerid` int(15) NOT NULL,
  `cartid` int(10) NOT NULL,
  `status` varchar(50) NOT NULL,
  `deliverytime` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=33 ;

--
-- Dumping data for table `tbl_allocation`
--

INSERT INTO `tbl_allocation` (`id`, `deliveryboyid`, `customerid`, `cartid`, `status`, `deliverytime`) VALUES
(31, 8, 12, 46, 'delivered', '2021-05-12 20:24:19'),
(32, 8, 12, 45, 'Allocated', '0000-00-00 00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_cart`
--

CREATE TABLE IF NOT EXISTS `tbl_cart` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customerid` int(11) NOT NULL,
  `farmerid` int(11) NOT NULL,
  `productid` int(11) NOT NULL,
  `quantity` varchar(30) NOT NULL,
  `price` int(11) NOT NULL,
  `totalprice` int(50) NOT NULL,
  `bdate` date NOT NULL,
  `rdate` date NOT NULL,
  `status` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=47 ;

--
-- Dumping data for table `tbl_cart`
--

INSERT INTO `tbl_cart` (`id`, `customerid`, `farmerid`, `productid`, `quantity`, `price`, `totalprice`, `bdate`, `rdate`, `status`) VALUES
(45, 12, 11, 23, '2', 400, 800, '2021-05-12', '2021-05-28', 'Approved'),
(46, 12, 11, 19, '3', 500, 1500, '2021-05-12', '2021-05-28', 'delivered');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_customerreg`
--

CREATE TABLE IF NOT EXISTS `tbl_customerreg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `district` varchar(50) NOT NULL,
  `gender` varchar(40) NOT NULL,
  `dob` varchar(50) NOT NULL,
  `phone` bigint(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(20) NOT NULL,
  `status` int(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=23 ;

--
-- Dumping data for table `tbl_customerreg`
--

INSERT INTO `tbl_customerreg` (`id`, `name`, `address`, `city`, `district`, `gender`, `dob`, `phone`, `email`, `password`, `status`) VALUES
(12, 'customer', 'cuscus', 'Koratty', 'thrissur', 'male', '2021-03-04', 2147483647, 'customer@gmail.com', 'customer@123', 1),
(13, 'carolin', 'caspras', 'potta', 'thrissur', 'female', '2021-03-04', 8086813432, 'carolin@gmail.com', 'carolin@123', 1),
(14, 'akhil', 'vadakkeveetil', 'pooppathy', 'thrissur', 'male', '2000-07-11', 8156895161, 'akh@gmail.com', 'akh@1212', 3),
(15, 'delna', 'aynikkal', 'thrissur', 'kasargod', 'female', '2021-04-30', 8080808080, 'del@gmail.com', 'Delna@12345', 3),
(16, 'delna', 'aynikkal', 'thrissur', 'kasargod', 'female', '2021-05-16', 8080808080, 'delna@gmail.com', 'delna@1234567', 3),
(17, 'delna', 'aynikkal', 'thrissur', 'kasargod', 'male', '2021-05-07', 8080808080, 'delpp@gmail.com', 'delpp@12345', 0),
(18, 'sona', 'jbcjkdj', 'cbjd', 'kannur', 'male', '2021-04-27', 8080808080, 'gasoo@gmail.como', 'gasoo@12345', 3),
(19, 'hanu', 'ghfhj', 'tct', 'kozhikode', 'male', '2021-05-06', 8008908989, 'hanu@gmail.com', 'hanu@123', 0),
(20, 'dfgh', 'aynikkal', 'thrissur', 'kasargod', 'female', '2021-05-29', 8080808080, 'delghhbj@gmail.com', 'hfhjghjgh@12453545', 3),
(21, 'cera', 'aynikkal', 'thrissur', 'kasargod', 'female', '2021-04-30', 8080808080, 'cera@gmail.com', 'ghjghg@45343', 0),
(22, 'delna', 'aynikkal', 'thrissur', 'kasargod', 'male', '2021-04-26', 8080808080, 'dejjl@gmail.com', 'bjj#t656', 0);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_deliveryboyreg`
--

CREATE TABLE IF NOT EXISTS `tbl_deliveryboyreg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `district` varchar(50) NOT NULL,
  `gender` varchar(40) NOT NULL,
  `dob` int(11) NOT NULL,
  `phone` bigint(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(40) NOT NULL,
  `status` int(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `tbl_deliveryboyreg`
--

INSERT INTO `tbl_deliveryboyreg` (`id`, `name`, `address`, `city`, `district`, `gender`, `dob`, `phone`, `email`, `password`, `status`) VALUES
(8, 'derin', 'demoshome', 'Tvm', 'thiruvanathapuram', 'male', 2021, 8086813432, 'derin@gmail.com', 'derin@123', 1);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_farmerreg`
--

CREATE TABLE IF NOT EXISTS `tbl_farmerreg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `address` varchar(60) NOT NULL,
  `city` varchar(50) NOT NULL,
  `district` varchar(40) NOT NULL,
  `gender` varchar(40) NOT NULL,
  `dob` date NOT NULL,
  `phone` bigint(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `status` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=14 ;

--
-- Dumping data for table `tbl_farmerreg`
--

INSERT INTO `tbl_farmerreg` (`id`, `name`, `address`, `city`, `district`, `gender`, `dob`, `phone`, `email`, `password`, `status`) VALUES
(11, 'farmer', 'fabulas', 'dessam', 'ernakulam', 'female', '2021-03-03', 2147483647, 'farmer@gmail.com', 'farmer@123', '1'),
(12, 'febin', 'fabulose', 'Koratty', 'ernakulam', 'male', '2021-03-04', 8086813432, 'febin@gmail.com', 'febin@123', '3'),
(13, 'fathu', 'cxhjs', 'gscxvhbjnm', 'cvbnm', 'male', '2021-03-30', 7356777874, 'fathu@gmail.com', 'fathu@123', '1');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_feedback`
--

CREATE TABLE IF NOT EXISTS `tbl_feedback` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customerid` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `description` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `status` int(10) NOT NULL,
  `cartid` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `tbl_feedback`
--

INSERT INTO `tbl_feedback` (`id`, `customerid`, `title`, `description`, `date`, `status`, `cartid`) VALUES
(7, 12, 'quality', 'quality is good', '2021-05-12', 0, 46);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_login`
--

CREATE TABLE IF NOT EXISTS `tbl_login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `usertype` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=46 ;

--
-- Dumping data for table `tbl_login`
--

INSERT INTO `tbl_login` (`id`, `username`, `password`, `usertype`) VALUES
(30, 'customer@gmail.com', 'customer@123', 'customer'),
(31, 'farmer@gmail.com', 'farmer@123', 'farmer'),
(32, 'admin@gmail.com', 'admin', 'admin'),
(33, 'carolin@gmail.com', 'carolin@123', 'customer'),
(34, 'febin@gmail.com', 'febin@123', 'farmer'),
(35, 'derin@gmail.com', 'derin@123', 'deliveryboy'),
(36, 'fathu@gmail.com', 'fathu@123', 'farmer'),
(37, 'akh@gmail.com', 'akh@1212', 'customer'),
(38, 'del@gmail.com', 'Delna@12345', 'customer'),
(39, 'delna@gmail.com', 'delna@1234567', 'customer'),
(40, 'delpp@gmail.com', 'delpp@12345', 'customer'),
(41, 'gasoo@gmail.como', 'gasoo@12345', 'customer'),
(42, 'hanu@gmail.com', 'hanu@123', 'customer'),
(43, 'delghhbj@gmail.com', 'hfhjghjgh@12453545', 'customer'),
(44, 'cera@gmail.com', 'ghjghg@45343', 'customer'),
(45, 'dejjl@gmail.com', 'bjj#t656', 'customer');
