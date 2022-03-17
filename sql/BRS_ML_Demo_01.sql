--------------------------
-- Load Demo Input Data
--------------------------

DROP TABLE IF EXISTS BRS_2021_input;

CREATE TABLE BRS_2021_input (Key int, 
                             Game_Date date, 
                             Game_Result int,
                             At_Bats int,
                             Runs_Scored int,
                             Hits int,
                             Runs_Batted_In int,
                             Walks int,
                             Strikeouts int,
                             Batting_Average float,
                             On_Base_Percentage float,
                             Slugging_Percentage float,
                             OnBase_Plus_Slugging float);

INSERT INTO BRS_2021_input VALUES(1, '04-02-2021', '0', '29', '0', '2', '0', '2', '8', '.069', '.129', '.103', '.232');
INSERT INTO BRS_2021_input VALUES(2, '04-03-2021', '0', '33', '2', '7', '2', '2', '8', '.212', '.270', '.242', '.513');
INSERT INTO BRS_2021_input VALUES(3, '04-04-2021', '0', '32', '3', '6', '3', '2', '8', '.188', '.229', '.344', '.572');
INSERT INTO BRS_2021_input VALUES(4, '04-05-2021', '1', '36', '11', '16', '10', '3', '8', '.444', '.463', '.639', '1.102');
INSERT INTO BRS_2021_input VALUES(5, '04-06-2021', '1', '44', '6', '10', '5', '3', '15', '.227', '.292', '.432', '.723');
INSERT INTO BRS_2021_input VALUES(6, '04-07-2021', '1', '35', '9', '13', '7', '1', '4', '.371', '.405', '.514', '.920');
INSERT INTO BRS_2021_input VALUES(7, '04-08-2021', '1', '38', '7', '12', '7', '3', '10', '.316', '.381', '.605', '.986');
INSERT INTO BRS_2021_input VALUES(8, '04-10-2021', '1', '38', '6', '10', '4', '4', '6', '.263', '.333', '.395', '.728');
INSERT INTO BRS_2021_input VALUES(9, '04-11-2021', '1', '44', '14', '17', '13', '3', '11', '.386', '.460', '.841', '1.301');
INSERT INTO BRS_2021_input VALUES(10, '04-13-2021', '1', '32', '4', '7', '4', '2', '5', '.219', '.265', '.500', '.765');
INSERT INTO BRS_2021_input VALUES(11, '04-14-2021', '1', '32', '3', '11', '2', '3', '7', '.344', '.400', '.438', '.838');
INSERT INTO BRS_2021_input VALUES(12, '04-14-2021', '1', '27', '7', '8', '6', '5', '11', '.296', '.406', '.444', '.851');
INSERT INTO BRS_2021_input VALUES(13, '04-15-2021', '0', '30', '3', '4', '3', '4', '10', '.133', '.257', '.200', '.457');
INSERT INTO BRS_2021_input VALUES(14, '04-17-2021', '1', '34', '7', '13', '7', '6', '11', '.382', '.452', '.559', '1.011');
INSERT INTO BRS_2021_input VALUES(15, '04-18-2021', '0', '26', '2', '8', '2', '0', '3', '.308', '.308', '.462', '.769');
INSERT INTO BRS_2021_input VALUES(16, '04-18-2021', '0', '25', '1', '4', '1', '1', '8', '.160', '.192', '.200', '.392');
INSERT INTO BRS_2021_input VALUES(17, '04-19-2021', '1', '38', '11', '16', '9', '6', '8', '.421', '.500', '.684', '1.184');
INSERT INTO BRS_2021_input VALUES(18, '04-20-2021', '1', '33', '4', '9', '4', '0', '5', '.273', '.273', '.515', '.788');
INSERT INTO BRS_2021_input VALUES(19, '04-21-2021', '0', '36', '3', '10', '3', '3', '10', '.278', '.333', '.500', '.833');
INSERT INTO BRS_2021_input VALUES(20, '04-22-2021', '0', '38', '3', '8', '2', '2', '11', '.211', '.268', '.395', '.663');
INSERT INTO BRS_2021_input VALUES(21, '04-23-2021', '1', '35', '6', '11', '4', '3', '7', '.314', '.368', '.486', '.854');
INSERT INTO BRS_2021_input VALUES(22, '04-24-2021', '0', '31', '2', '6', '2', '1', '9', '.194', '.242', '.290', '.533');
INSERT INTO BRS_2021_input VALUES(23, '04-25-2021', '1', '26', '5', '5', '5', '7', '6', '.192', '.382', '.308', '.690');
INSERT INTO BRS_2021_input VALUES(24, '04-27-2021', '1', '29', '2', '5', '2', '2', '8', '.172', '.226', '.345', '.571');
INSERT INTO BRS_2021_input VALUES(25, '04-28-2021', '1', '30', '1', '4', '1', '1', '15', '.133', '.161', '.233', '.395');
INSERT INTO BRS_2021_input VALUES(26, '04-29-2021', '0', '30', '1', '3', '1', '3', '6', '.100', '.182', '.167', '.348');
INSERT INTO BRS_2021_input VALUES(27, '04-30-2021', '1', '34', '6', '6', '6', '3', '6', '.176', '.263', '.529', '.793');
INSERT INTO BRS_2021_input VALUES(28, '05-01-2021', '0', '38', '6', '12', '6', '4', '12', '.316', '.372', '.447', '.819');
INSERT INTO BRS_2021_input VALUES(29, '05-02-2021', '0', '32', '3', '9', '3', '1', '7', '.281', '.324', '.438', '.761');
INSERT INTO BRS_2021_input VALUES(30, '05-04-2021', '1', '38', '11', '14', '10', '3', '6', '.368', '.415', '.737', '1.151');
INSERT INTO BRS_2021_input VALUES(31, '05-05-2021', '0', '39', '5', '9', '5', '6', '8', '.231', '.348', '.333', '.681');
INSERT INTO BRS_2021_input VALUES(32, '05-06-2021', '1', '43', '12', '16', '11', '3', '8', '.372', '.438', '.465', '.903');
INSERT INTO BRS_2021_input VALUES(33, '05-07-2021', '1', '35', '6', '7', '6', '3', '6', '.200', '.282', '.371', '.653');
INSERT INTO BRS_2021_input VALUES(34, '05-08-2021', '1', '42', '11', '14', '10', '5', '11', '.333', '.404', '.500', '.904');
INSERT INTO BRS_2021_input VALUES(35, '05-09-2021', '1', '35', '4', '8', '4', '3', '7', '.229', '.289', '.457', '.747');
INSERT INTO BRS_2021_input VALUES(36, '05-10-2021', '0', '30', '1', '4', '1', '0', '11', '.133', '.156', '.200', '.356');
INSERT INTO BRS_2021_input VALUES(37, '05-11-2021', '0', '30', '2', '4', '2', '2', '11', '.133', '.182', '.233', '.415');
INSERT INTO BRS_2021_input VALUES(38, '05-12-2021', '0', '32', '1', '5', '1', '4', '10', '.156', '.250', '.281', '.531');
INSERT INTO BRS_2021_input VALUES(39, '05-13-2021', '1', '35', '8', '13', '6', '3', '6', '.371', '.421', '.629', '1.050');
INSERT INTO BRS_2021_input VALUES(40, '05-14-2021', '1', '31', '4', '9', '4', '2', '9', '.290', '.333', '.484', '.817');
INSERT INTO BRS_2021_input VALUES(41, '05-15-2021', '1', '35', '9', '12', '9', '2', '4', '.343', '.378', '.743', '1.121');
INSERT INTO BRS_2021_input VALUES(42, '05-16-2021', '0', '35', '5', '9', '5', '2', '14', '.257', '.297', '.486', '.783');
INSERT INTO BRS_2021_input VALUES(43, '05-18-2021', '0', '33', '0', '5', '0', '2', '11', '.152', '.200', '.182', '.382');
INSERT INTO BRS_2021_input VALUES(44, '05-19-2021', '1', '39', '7', '13', '7', '0', '11', '.333', '.333', '.744', '1.077');
INSERT INTO BRS_2021_input VALUES(45, '05-20-2021', '1', '39', '8', '14', '8', '3', '8', '.359', '.405', '.538', '.943');
INSERT INTO BRS_2021_input VALUES(46, '05-21-2021', '1', '41', '11', '13', '10', '2', '17', '.317', '.349', '.561', '.910');
INSERT INTO BRS_2021_input VALUES(47, '05-22-2021', '1', '33', '4', '7', '4', '5', '11', '.212', '.325', '.424', '.749');
INSERT INTO BRS_2021_input VALUES(48, '05-23-2021', '0', '31', '2', '4', '2', '2', '12', '.129', '.206', '.323', '.528');
INSERT INTO BRS_2021_input VALUES(49, '05-25-2021', '0', '29', '1', '4', '1', '3', '12', '.138', '.242', '.207', '.449');
INSERT INTO BRS_2021_input VALUES(50, '05-26-2021', '1', '32', '9', '7', '9', '3', '7', '.219', '.278', '.469', '.747');
INSERT INTO BRS_2021_input VALUES(51, '05-28-2021', '1', '21', '5', '5', '5', '2', '6', '.238', '.304', '.524', '.828');
INSERT INTO BRS_2021_input VALUES(52, '05-29-2021', '1', '35', '3', '12', '3', '0', '6', '.343', '.343', '.486', '.829');
INSERT INTO BRS_2021_input VALUES(53, '05-31-2021', '0', '32', '2', '5', '2', '1', '12', '.156', '.182', '.375', '.557');
INSERT INTO BRS_2021_input VALUES(54, '06-01-2021', '0', '32', '1', '5', '1', '1', '9', '.156', '.182', '.188', '.369');
INSERT INTO BRS_2021_input VALUES(55, '06-02-2021', '0', '34', '1', '7', '1', '2', '11', '.206', '.250', '.206', '.456');
INSERT INTO BRS_2021_input VALUES(56, '06-03-2021', '1', '34', '5', '8', '5', '7', '12', '.235', '.366', '.441', '.807');
INSERT INTO BRS_2021_input VALUES(57, '06-04-2021', '1', '36', '5', '9', '5', '0', '10', '.250', '.250', '.417', '.667');
INSERT INTO BRS_2021_input VALUES(58, '06-05-2021', '1', '38', '7', '13', '7', '2', '7', '.342', '.375', '.553', '.928');
INSERT INTO BRS_2021_input VALUES(59, '06-06-2021', '1', '34', '6', '6', '6', '4', '6', '.176', '.256', '.382', '.639');
INSERT INTO BRS_2021_input VALUES(60, '06-07-2021', '1', '33', '5', '10', '3', '3', '6', '.303', '.361', '.364', '.725');
INSERT INTO BRS_2021_input VALUES(61, '06-08-2021', '0', '33', '1', '6', '1', '1', '12', '.182', '.250', '.212', '.462');
INSERT INTO BRS_2021_input VALUES(62, '06-09-2021', '0', '30', '3', '4', '3', '1', '9', '.133', '.156', '.267', '.423');
INSERT INTO BRS_2021_input VALUES(63, '06-10-2021', '1', '38', '12', '14', '12', '4', '3', '.368', '.444', '.632', '1.076');
INSERT INTO BRS_2021_input VALUES(64, '06-11-2021', '1', '33', '6', '8', '5', '3', '9', '.242', '.342', '.455', '.797');
INSERT INTO BRS_2021_input VALUES(65, '06-12-2021', '0', '31', '2', '5', '2', '3', '13', '.161', '.278', '.290', '.568');
INSERT INTO BRS_2021_input VALUES(66, '06-13-2021', '0', '32', '4', '6', '4', '4', '12', '.188', '.278', '.406', '.684');
INSERT INTO BRS_2021_input VALUES(67, '06-14-2021', '1', '31', '2', '7', '2', '1', '7', '.226', '.250', '.258', '.508');
INSERT INTO BRS_2021_input VALUES(68, '06-15-2021', '1', '39', '10', '14', '10', '2', '11', '.359', '.390', '.744', '1.134');
INSERT INTO BRS_2021_input VALUES(69, '06-16-2021', '1', '41', '10', '14', '10', '3', '10', '.341', '.386', '.610', '.996');
INSERT INTO BRS_2021_input VALUES(70, '06-18-2021', '0', '36', '3', '11', '3', '2', '11', '.306', '.342', '.417', '.759');
INSERT INTO BRS_2021_input VALUES(71, '06-19-2021', '1', '34', '7', '8', '7', '3', '5', '.235', '.316', '.500', '.816');
INSERT INTO BRS_2021_input VALUES(72, '06-20-2021', '0', '37', '3', '11', '3', '3', '8', '.297', '.350', '.541', '.891');
INSERT INTO BRS_2021_input VALUES(73, '06-22-2021', '1', '39', '9', '10', '7', '3', '11', '.256', '.311', '.410', '.721');
INSERT INTO BRS_2021_input VALUES(74, '06-23-2021', '0', '32', '2', '6', '2', '6', '12', '.188', '.333', '.250', '.583');
INSERT INTO BRS_2021_input VALUES(75, '06-24-2021', '0', '29', '0', '4', '0', '5', '10', '.138', '.265', '.172', '.437');
INSERT INTO BRS_2021_input VALUES(76, '06-25-2021', '1', '32', '5', '7', '5', '4', '10', '.219', '.297', '.281', '.579');
INSERT INTO BRS_2021_input VALUES(77, '06-26-2021', '1', '30', '4', '10', '4', '2', '6', '.333', '.343', '.400', '.743');
INSERT INTO BRS_2021_input VALUES(78, '06-27-2021', '1', '35', '9', '13', '9', '2', '7', '.371', '.410', '.800', '1.210');
INSERT INTO BRS_2021_input VALUES(79, '06-28-2021', '1', '30', '6', '9', '6', '4', '6', '.300', '.382', '.733', '1.116');
INSERT INTO BRS_2021_input VALUES(80, '06-29-2021', '1', '30', '7', '12', '7', '7', '4', '.400', '.500', '.433', '.933');
INSERT INTO BRS_2021_input VALUES(81, '06-30-2021', '1', '32', '6', '8', '6', '2', '3', '.250', '.314', '.500', '.814');

SELECT * FROM BRS_2021_input;

 Key | Game_Date  | Game_Result | At_Bats | Runs_Scored | Hits | Runs_Batted_In | Walks | Strikeouts | Batting_Average | On_Base_Percentage | Slugging_Percentage | OnBase_Plus_Slugging
-----+------------+-------------+---------+-------------+------+----------------+-------+------------+-----------------+--------------------+---------------------+----------------------
   1 | 2021-04-02 |           0 |      29 |           0 |    2 |              0 |     2 |          8 |           0.069 |              0.129 |               0.103 |                0.232
   2 | 2021-04-03 |           0 |      33 |           2 |    7 |              2 |     2 |          8 |           0.212 |               0.27 |               0.242 |                0.513
   3 | 2021-04-04 |           0 |      32 |           3 |    6 |              3 |     2 |          8 |           0.188 |              0.229 |               0.344 |                0.572
   4 | 2021-04-05 |           1 |      36 |          11 |   16 |             10 |     3 |          8 |           0.444 |              0.463 |               0.639 |                1.102
   5 | 2021-04-06 |           1 |      44 |           6 |   10 |              5 |     3 |         15 |           0.227 |              0.292 |               0.432 |                0.723
   6 | 2021-04-07 |           1 |      35 |           9 |   13 |              7 |     1 |          4 |           0.371 |              0.405 |               0.514 |                 0.92
   7 | 2021-04-08 |           1 |      38 |           7 |   12 |              7 |     3 |         10 |           0.316 |              0.381 |               0.605 |                0.986
   8 | 2021-04-10 |           1 |      38 |           6 |   10 |              4 |     4 |          6 |           0.263 |              0.333 |               0.395 |                0.728
   9 | 2021-04-11 |           1 |      44 |          14 |   17 |             13 |     3 |         11 |           0.386 |               0.46 |               0.841 |                1.301
  10 | 2021-04-13 |           1 |      32 |           4 |    7 |              4 |     2 |          5 |           0.219 |              0.265 |                 0.5 |                0.765
  11 | 2021-04-14 |           1 |      32 |           3 |   11 |              2 |     3 |          7 |           0.344 |                0.4 |               0.438 |                0.838
  12 | 2021-04-14 |           1 |      27 |           7 |    8 |              6 |     5 |         11 |           0.296 |              0.406 |               0.444 |                0.851
  13 | 2021-04-15 |           0 |      30 |           3 |    4 |              3 |     4 |         10 |           0.133 |              0.257 |                 0.2 |                0.457
  14 | 2021-04-17 |           1 |      34 |           7 |   13 |              7 |     6 |         11 |           0.382 |              0.452 |               0.559 |                1.011
  15 | 2021-04-18 |           0 |      26 |           2 |    8 |              2 |     0 |          3 |           0.308 |              0.308 |               0.462 |                0.769
  16 | 2021-04-18 |           0 |      25 |           1 |    4 |              1 |     1 |          8 |            0.16 |              0.192 |                 0.2 |                0.392
  17 | 2021-04-19 |           1 |      38 |          11 |   16 |              9 |     6 |          8 |           0.421 |                0.5 |               0.684 |                1.184
  18 | 2021-04-20 |           1 |      33 |           4 |    9 |              4 |     0 |          5 |           0.273 |              0.273 |               0.515 |                0.788
  19 | 2021-04-21 |           0 |      36 |           3 |   10 |              3 |     3 |         10 |           0.278 |              0.333 |                 0.5 |                0.833
  20 | 2021-04-22 |           0 |      38 |           3 |    8 |              2 |     2 |         11 |           0.211 |              0.268 |               0.395 |                0.663
  21 | 2021-04-23 |           1 |      35 |           6 |   11 |              4 |     3 |          7 |           0.314 |              0.368 |               0.486 |                0.854
  22 | 2021-04-24 |           0 |      31 |           2 |    6 |              2 |     1 |          9 |           0.194 |              0.242 |                0.29 |                0.533
  23 | 2021-04-25 |           1 |      26 |           5 |    5 |              5 |     7 |          6 |           0.192 |              0.382 |               0.308 |                 0.69
  24 | 2021-04-27 |           1 |      29 |           2 |    5 |              2 |     2 |          8 |           0.172 |              0.226 |               0.345 |                0.571
  25 | 2021-04-28 |           1 |      30 |           1 |    4 |              1 |     1 |         15 |           0.133 |              0.161 |               0.233 |                0.395
  26 | 2021-04-29 |           0 |      30 |           1 |    3 |              1 |     3 |          6 |             0.1 |              0.182 |               0.167 |                0.348
  27 | 2021-04-30 |           1 |      34 |           6 |    6 |              6 |     3 |          6 |           0.176 |              0.263 |               0.529 |                0.793
  28 | 2021-05-01 |           0 |      38 |           6 |   12 |              6 |     4 |         12 |           0.316 |              0.372 |               0.447 |                0.819
  29 | 2021-05-02 |           0 |      32 |           3 |    9 |              3 |     1 |          7 |           0.281 |              0.324 |               0.438 |                0.761
  30 | 2021-05-04 |           1 |      38 |          11 |   14 |             10 |     3 |          6 |           0.368 |              0.415 |               0.737 |                1.151
  31 | 2021-05-05 |           0 |      39 |           5 |    9 |              5 |     6 |          8 |           0.231 |              0.348 |               0.333 |                0.681
  32 | 2021-05-06 |           1 |      43 |          12 |   16 |             11 |     3 |          8 |           0.372 |              0.438 |               0.465 |                0.903
  33 | 2021-05-07 |           1 |      35 |           6 |    7 |              6 |     3 |          6 |             0.2 |              0.282 |               0.371 |                0.653
  34 | 2021-05-08 |           1 |      42 |          11 |   14 |             10 |     5 |         11 |           0.333 |              0.404 |                 0.5 |                0.904
  35 | 2021-05-09 |           1 |      35 |           4 |    8 |              4 |     3 |          7 |           0.229 |              0.289 |               0.457 |                0.747
  36 | 2021-05-10 |           0 |      30 |           1 |    4 |              1 |     0 |         11 |           0.133 |              0.156 |                 0.2 |                0.356
  37 | 2021-05-11 |           0 |      30 |           2 |    4 |              2 |     2 |         11 |           0.133 |              0.182 |               0.233 |                0.415
  38 | 2021-05-12 |           0 |      32 |           1 |    5 |              1 |     4 |         10 |           0.156 |               0.25 |               0.281 |                0.531
  39 | 2021-05-13 |           1 |      35 |           8 |   13 |              6 |     3 |          6 |           0.371 |              0.421 |               0.629 |                 1.05
  40 | 2021-05-14 |           1 |      31 |           4 |    9 |              4 |     2 |          9 |            0.29 |              0.333 |               0.484 |                0.817
  41 | 2021-05-15 |           1 |      35 |           9 |   12 |              9 |     2 |          4 |           0.343 |              0.378 |               0.743 |                1.121
  42 | 2021-05-16 |           0 |      35 |           5 |    9 |              5 |     2 |         14 |           0.257 |              0.297 |               0.486 |                0.783
  43 | 2021-05-18 |           0 |      33 |           0 |    5 |              0 |     2 |         11 |           0.152 |                0.2 |               0.182 |                0.382
  44 | 2021-05-19 |           1 |      39 |           7 |   13 |              7 |     0 |         11 |           0.333 |              0.333 |               0.744 |                1.077
  45 | 2021-05-20 |           1 |      39 |           8 |   14 |              8 |     3 |          8 |           0.359 |              0.405 |               0.538 |                0.943
  46 | 2021-05-21 |           1 |      41 |          11 |   13 |             10 |     2 |         17 |           0.317 |              0.349 |               0.561 |                 0.91
  47 | 2021-05-22 |           1 |      33 |           4 |    7 |              4 |     5 |         11 |           0.212 |              0.325 |               0.424 |                0.749
  48 | 2021-05-23 |           0 |      31 |           2 |    4 |              2 |     2 |         12 |           0.129 |              0.206 |               0.323 |                0.528
  49 | 2021-05-25 |           0 |      29 |           1 |    4 |              1 |     3 |         12 |           0.138 |              0.242 |               0.207 |                0.449
  50 | 2021-05-26 |           1 |      32 |           9 |    7 |              9 |     3 |          7 |           0.219 |              0.278 |               0.469 |                0.747
  51 | 2021-05-28 |           1 |      21 |           5 |    5 |              5 |     2 |          6 |           0.238 |              0.304 |               0.524 |                0.828
  52 | 2021-05-29 |           1 |      35 |           3 |   12 |              3 |     0 |          6 |           0.343 |              0.343 |               0.486 |                0.829
  53 | 2021-05-31 |           0 |      32 |           2 |    5 |              2 |     1 |         12 |           0.156 |              0.182 |               0.375 |                0.557
  54 | 2021-06-01 |           0 |      32 |           1 |    5 |              1 |     1 |          9 |           0.156 |              0.182 |               0.188 |                0.369
  55 | 2021-06-02 |           0 |      34 |           1 |    7 |              1 |     2 |         11 |           0.206 |               0.25 |               0.206 |                0.456
  56 | 2021-06-03 |           1 |      34 |           5 |    8 |              5 |     7 |         12 |           0.235 |              0.366 |               0.441 |                0.807
  57 | 2021-06-04 |           1 |      36 |           5 |    9 |              5 |     0 |         10 |            0.25 |               0.25 |               0.417 |                0.667
  58 | 2021-06-05 |           1 |      38 |           7 |   13 |              7 |     2 |          7 |           0.342 |              0.375 |               0.553 |                0.928
  59 | 2021-06-06 |           1 |      34 |           6 |    6 |              6 |     4 |          6 |           0.176 |              0.256 |               0.382 |                0.639
  60 | 2021-06-07 |           1 |      33 |           5 |   10 |              3 |     3 |          6 |           0.303 |              0.361 |               0.364 |                0.725
  61 | 2021-06-08 |           0 |      33 |           1 |    6 |              1 |     1 |         12 |           0.182 |               0.25 |               0.212 |                0.462
  62 | 2021-06-09 |           0 |      30 |           3 |    4 |              3 |     1 |          9 |           0.133 |              0.156 |               0.267 |                0.423
  63 | 2021-06-10 |           1 |      38 |          12 |   14 |             12 |     4 |          3 |           0.368 |              0.444 |               0.632 |                1.076
  64 | 2021-06-11 |           1 |      33 |           6 |    8 |              5 |     3 |          9 |           0.242 |              0.342 |               0.455 |                0.797
  65 | 2021-06-12 |           0 |      31 |           2 |    5 |              2 |     3 |         13 |           0.161 |              0.278 |                0.29 |                0.568
  66 | 2021-06-13 |           0 |      32 |           4 |    6 |              4 |     4 |         12 |           0.188 |              0.278 |               0.406 |                0.684
  67 | 2021-06-14 |           1 |      31 |           2 |    7 |              2 |     1 |          7 |           0.226 |               0.25 |               0.258 |                0.508
  68 | 2021-06-15 |           1 |      39 |          10 |   14 |             10 |     2 |         11 |           0.359 |               0.39 |               0.744 |                1.134
  69 | 2021-06-16 |           1 |      41 |          10 |   14 |             10 |     3 |         10 |           0.341 |              0.386 |                0.61 |                0.996
  70 | 2021-06-18 |           0 |      36 |           3 |   11 |              3 |     2 |         11 |           0.306 |              0.342 |               0.417 |                0.759
  71 | 2021-06-19 |           1 |      34 |           7 |    8 |              7 |     3 |          5 |           0.235 |              0.316 |                 0.5 |                0.816
  72 | 2021-06-20 |           0 |      37 |           3 |   11 |              3 |     3 |          8 |           0.297 |               0.35 |               0.541 |                0.891
  73 | 2021-06-22 |           1 |      39 |           9 |   10 |              7 |     3 |         11 |           0.256 |              0.311 |                0.41 |                0.721
  74 | 2021-06-23 |           0 |      32 |           2 |    6 |              2 |     6 |         12 |           0.188 |              0.333 |                0.25 |                0.583
  75 | 2021-06-24 |           0 |      29 |           0 |    4 |              0 |     5 |         10 |           0.138 |              0.265 |               0.172 |                0.437
  76 | 2021-06-25 |           1 |      32 |           5 |    7 |              5 |     4 |         10 |           0.219 |              0.297 |               0.281 |                0.579
  77 | 2021-06-26 |           1 |      30 |           4 |   10 |              4 |     2 |          6 |           0.333 |              0.343 |                 0.4 |                0.743
  78 | 2021-06-27 |           1 |      35 |           9 |   13 |              9 |     2 |          7 |           0.371 |               0.41 |                 0.8 |                 1.21
  79 | 2021-06-28 |           1 |      30 |           6 |    9 |              6 |     4 |          6 |             0.3 |              0.382 |               0.733 |                1.116
  80 | 2021-06-29 |           1 |      30 |           7 |   12 |              7 |     7 |          4 |             0.4 |                0.5 |               0.433 |                0.933
  81 | 2021-06-30 |           1 |      32 |           6 |    8 |              6 |     2 |          3 |            0.25 |              0.314 |                 0.5 |                0.814

(81 rows)


---------------------------------------------------
-- Classification using Logistic Regression (LR)
---------------------------------------------------

DROP MODEL BRS_2021_LogisticRegressionModel;

SELECT LOGISTIC_REG('BRS_2021_LogisticRegressionModel', 
                    'BRS_2021_input',
                    'Game_Result',
                    'At_Bats, Runs_Scored, Hits, Runs_Batted_In, Walks, Strikeouts, Batting_Average, On_Base_Percentage, Slugging_Percentage, OnBase_Plus_Slugging');

SELECT GET_MODEL_SUMMARY(USING PARAMETERS model_name='BRS_2021_LogisticRegressionModel');

=======
details
=======
     predictor      |coefficient| std_err  |z_value |p_value
--------------------+-----------+----------+--------+--------
     Intercept      | 10.12266  | 18.36691 | 0.55114| 0.58154
      at_bats       | -0.41974  |  0.58498 |-0.71752| 0.47305
    runs_scored     |  5.36862  |  2.49437 | 2.15229| 0.03137
        hits        |  0.23942  |  2.23938 | 0.10691| 0.91486
   runs_batted_in   | -4.06376  |  2.36324 |-1.71957| 0.08551
       walks        |  0.33120  |  0.88358 | 0.37484| 0.70778
     strikeouts     | -0.21593  |  0.21884 |-0.98671| 0.32379
  batting_average   | 12.22556  | 83.09821 | 0.14712| 0.88304
 on_base_percentage |-2468.59229|1127.31500|-2.18980| 0.02854
slugging_percentage |-2435.11002|1115.26131|-2.18344| 0.02900
onbase_plus_slugging|2442.25950 |1117.29009| 2.18588| 0.02882


==============
regularization
==============
type| lambda
----+--------
none| 1.00000


===========
call_string
===========
logistic_reg('public.BRS_2021_LogisticRegressionModel', 'BRS_2021_input', '"game_result"', 'At_Bats, Runs_Scored, Hits, Runs_Batted_In, Walks, Strikeouts, Batting_Average, On_Base_Percentage, Slugging_Percentage, OnBase_Plus_Slugging'
USING PARAMETERS optimizer='newton', epsilon=1e-06, max_iterations=100, regularization='none', lambda=1, alpha=0.5)

===============
Additional Info
===============
       Name       |Value
------------------+-----
 iteration_count  |  8
rejected_row_count|  0
accepted_row_count| 81

(1 row)

SELECT CONFUSION_MATRIX(obs::int, pred::int USING PARAMETERS num_classes=2) OVER()
       FROM (SELECT Game_Result AS obs, PREDICT_LOGISTIC_REG (At_Bats, Runs_Scored, Hits, Runs_Batted_In, Walks, Strikeouts, Batting_Average, On_Base_Percentage, Slugging_Percentage, OnBase_Plus_Slugging
             USING PARAMETERS model_name='BRS_2021_LogisticRegressionModel') AS PRED FROM BRS_2021_input) AS prediction_output;

 actual_class | predicted_0 | predicted_1 |                   comment
--------------+-------------+-------------+---------------------------------------------
            0 |          26 |           5 |
            1 |           6 |          44 | Of 81 rows, 81 were used and 0 were ignored

(2 rows)

DROP TABLE IF EXISTS BRS_2021_prediction_LR;

CREATE TABLE BRS_2021_prediction_LR AS (SELECT Key, Game_Date, Game_Result, 
                                        PREDICT_LOGISTIC_REG (At_Bats, Runs_Scored, Hits, Runs_Batted_In, Walks, Strikeouts, Batting_Average, On_Base_Percentage, Slugging_Percentage, OnBase_Plus_Slugging 
                                        USING PARAMETERS model_name='BRS_2021_LogisticRegressionModel') AS ML_Prediction, At_Bats, Runs_Scored, Hits, Runs_Batted_In, Walks, Strikeouts, Batting_Average, On_Base_Percentage, Slugging_Percentage, OnBase_Plus_Slugging
                                        FROM BRS_2021_input); 

SELECT COUNT(*) AS LR_Prediction_Errors FROM BRS_2021_prediction_LR WHERE Game_Result != ML_Prediction;

 LR_Prediction_Errors
----------------------
                   11
(1 row)


-------------------------------------------------------
-- Classification using Support Vector Machine (SVM) 
-------------------------------------------------------

DROP MODEL BRS_2021_SupportVectorMachineModel;

SELECT SVM_CLASSIFIER('BRS_2021_SupportVectorMachineModel', 
                      'BRS_2021_input', 
                      'Game_Result', 
                      'At_Bats, Runs_Scored, Hits, Runs_Batted_In, Walks, Strikeouts, Batting_Average, On_Base_Percentage, Slugging_Percentage, OnBase_Plus_Slugging');

SELECT GET_MODEL_SUMMARY(USING PARAMETERS model_name='BRS_2021_SupportVectorMachineModel');

=======
details
=======
     predictor      |coefficient
--------------------+-----------
     Intercept      |  0.58329
      at_bats       | -0.04953
    runs_scored     |  0.76314
        hits        | -0.01600
   runs_batted_in   | -0.38194
       walks        | -0.06003
     strikeouts     | -0.04901
  batting_average   |  0.15048
 on_base_percentage |  0.09705
slugging_percentage |  0.19929
onbase_plus_slugging|  0.30510


===========
call_string
===========
SELECT svm_classifier('public.BRS_2021_SupportVectorMachineModel', 'BRS_2021_input', '"game_result"', 'At_Bats, Runs_Scored, Hits, Runs_Batted_In, Walks, Strikeouts, Batting_Average, On_Base_Percentage, Slugging_Percentage, OnBase_Plus_Slugging'
USING PARAMETERS class_weights='none', C=1, max_iterations=100, intercept_mode='regularized', intercept_scaling=1, epsilon=0.001);

===============
Additional Info
===============
       Name       |Value
------------------+-----
accepted_row_count| 81
rejected_row_count|  0
 iteration_count  | 10

(1 row)

SELECT CONFUSION_MATRIX(obs::int, pred::int USING PARAMETERS num_classes=2) OVER() 
       FROM (SELECT Game_Result AS obs, PREDICT_SVM_CLASSIFIER (At_Bats, Runs_Scored, Hits, Runs_Batted_In, Walks, Strikeouts, Batting_Average, On_Base_Percentage, Slugging_Percentage, OnBase_Plus_Slugging 
             USING PARAMETERS model_name='BRS_2021_SupportVectorMachineModel') AS PRED FROM BRS_2021_input) AS prediction_output;

 actual_class | predicted_0 | predicted_1 |                   comment
--------------+-------------+-------------+---------------------------------------------
            0 |          27 |           4 |
            1 |           5 |          45 | Of 81 rows, 81 were used and 0 were ignored
(2 rows)

DROP TABLE IF EXISTS BRS_2021_prediction_SVM;

CREATE TABLE BRS_2021_prediction_SVM AS (SELECT Key, Game_Date, Game_Result,
                                         PREDICT_SVM_CLASSIFIER (At_Bats, Runs_Scored, Hits, Runs_Batted_In, Walks, Strikeouts, Batting_Average, On_Base_Percentage, Slugging_Percentage, OnBase_Plus_Slugging 
                                         USING PARAMETERS model_name='BRS_2021_SupportVectorMachineModel') AS ML_Prediction, At_Bats, Runs_Scored, Hits, Runs_Batted_In, Walks, Strikeouts, Batting_Average, On_Base_Percentage, Slugging_Percentage, OnBase_Plus_Slugging 
                                         FROM BRS_2021_input);

SELECT COUNT(*) AS SVM_Prediction_Errors FROM BRS_2021_prediction_SVM WHERE Game_Result != ML_Prediction;

 SVM_Prediction_Errors
-----------------------
                     9
(1 row)


---------------------------------------------
-- Classification using Random Forest (RF) 
---------------------------------------------

DROP MODEL BRS_2021_RandomForestModel;

SELECT RF_CLASSIFIER('BRS_2021_RandomForestModel', 
                     'BRS_2021_input', 
                     'Game_Result', 
                     'At_Bats, Runs_Scored, Hits, Runs_Batted_In, Walks, Strikeouts, Batting_Average, On_Base_Percentage, Slugging_Percentage, OnBase_Plus_Slugging');

SELECT GET_MODEL_SUMMARY(USING PARAMETERS model_name='BRS_2021_RandomForestModel');

===========
call_string
===========
SELECT rf_classifier('public.BRS_2021_RandomForestModel', 'BRS_2021_input', 'game_result', 'At_Bats, Runs_Scored, Hits, Runs_Batted_In, Walks, Strikeouts, Batting_Average, On_Base_Percentage, Slugging_Percentage, OnBase_Plus_Slugging' USING PARAMETERS exclude_columns='', ntree=20, mtry=3, sampling_size=0.632, max_depth=5, max_breadth=32, min_leaf_size=1, min_info_gain=0, nbins=32);

=======
details
=======
     predictor      |      type
--------------------+----------------
      at_bats       |      int
    runs_scored     |      int
        hits        |      int
   runs_batted_in   |      int
       walks        |      int
     strikeouts     |      int
  batting_average   |float or numeric
 on_base_percentage |float or numeric
slugging_percentage |float or numeric
onbase_plus_slugging|float or numeric


===============
Additional Info
===============
       Name       |Value
------------------+-----
    tree_count    | 20
rejected_row_count|  0
accepted_row_count| 81

(1 row)

SELECT CONFUSION_MATRIX(obs::int, pred::int USING PARAMETERS num_classes=2) OVER() 
       FROM (SELECT Game_Result AS obs, PREDICT_RF_CLASSIFIER (At_Bats, Runs_Scored, Hits, Runs_Batted_In, Walks, Strikeouts, Batting_Average, On_Base_Percentage, Slugging_Percentage, OnBase_Plus_Slugging 
             USING PARAMETERS model_name='BRS_2021_RandomForestModel') AS PRED FROM BRS_2021_input) AS prediction_output;

 actual_class | predicted_0 | predicted_1 |                   comment
--------------+-------------+-------------+---------------------------------------------
            0 |          31 |           0 |
            1 |           2 |          48 | Of 81 rows, 81 were used and 0 were ignored
(2 rows)

DROP TABLE IF EXISTS BRS_2021_prediction_RF;

CREATE TABLE BRS_2021_prediction_RF AS (SELECT Key, Game_Date, Game_Result,
                                        PREDICT_RF_CLASSIFIER (At_Bats, Runs_Scored, Hits, Runs_Batted_In, Walks, Strikeouts, Batting_Average, On_Base_Percentage, Slugging_Percentage, OnBase_Plus_Slugging 
                                        USING PARAMETERS model_name='BRS_2021_RandomForestModel') AS ML_Prediction, At_Bats, Runs_Scored, Hits, Runs_Batted_In, Walks, Strikeouts, Batting_Average, On_Base_Percentage, Slugging_Percentage, OnBase_Plus_Slugging 
                                        FROM BRS_2021_input);

SELECT COUNT(*) AS RF_Prediction_Errors FROM BRS_2021_prediction_RF WHERE Game_Result != ML_Prediction;

 RF_Prediction_Errors
----------------------
                    2
(1 row)


------------------------------
-- Compare ML Model Results 
------------------------------

SELECT * FROM BRS_2021_prediction_RF WHERE Game_Result != ML_Prediction;
 Key | Game_Date  | Game_Result | ML_Prediction | At_Bats | Runs_Scored | Hits | Runs_Batted_In | Walks | Strikeouts | Batting_Average | On_Base_Percentage | Slugging_Percentage | OnBase_Plus_Slugging
-----+------------+-------------+---------------+---------+-------------+------+----------------+-------+------------+-----------------+--------------------+---------------------+----------------------
  25 | 2021-04-28 |           1 | 0             |      30 |           1 |    4 |              1 |     1 |         15 |           0.133 |              0.161 |               0.233 |                0.395
  67 | 2021-06-14 |           1 | 0             |      31 |           2 |    7 |              2 |     1 |          7 |           0.226 |               0.25 |               0.258 |                0.508

(2 rows)

SELECT * FROM BRS_2021_prediction_SVM WHERE Game_Result != ML_Prediction;
 Key | Game_Date  | Game_Result | ML_Prediction | At_Bats | Runs_Scored | Hits | Runs_Batted_In | Walks | Strikeouts | Batting_Average | On_Base_Percentage | Slugging_Percentage | OnBase_Plus_Slugging
-----+------------+-------------+---------------+---------+-------------+------+----------------+-------+------------+-----------------+--------------------+---------------------+----------------------
  15 | 2021-04-18 |           0 |             1 |      26 |           2 |    8 |              2 |     0 |          3 |           0.308 |              0.308 |               0.462 |                0.769
  24 | 2021-04-27 |           1 |             0 |      29 |           2 |    5 |              2 |     2 |          8 |           0.172 |              0.226 |               0.345 |                0.571
  25 | 2021-04-28 |           1 |             0 |      30 |           1 |    4 |              1 |     1 |         15 |           0.133 |              0.161 |               0.233 |                0.395
  28 | 2021-05-01 |           0 |             1 |      38 |           6 |   12 |              6 |     4 |         12 |           0.316 |              0.372 |               0.447 |                0.819
  31 | 2021-05-05 |           0 |             1 |      39 |           5 |    9 |              5 |     6 |          8 |           0.231 |              0.348 |               0.333 |                0.681
  42 | 2021-05-16 |           0 |             1 |      35 |           5 |    9 |              5 |     2 |         14 |           0.257 |              0.297 |               0.486 |                0.783
  47 | 2021-05-22 |           1 |             0 |      33 |           4 |    7 |              4 |     5 |         11 |           0.212 |              0.325 |               0.424 |                0.749
  52 | 2021-05-29 |           1 |             0 |      35 |           3 |   12 |              3 |     0 |          6 |           0.343 |              0.343 |               0.486 |                0.829
  67 | 2021-06-14 |           1 |             0 |      31 |           2 |    7 |              2 |     1 |          7 |           0.226 |               0.25 |               0.258 |                0.508

(9 rows)

SELECT * FROM BRS_2021_prediction_LR WHERE Game_Result != ML_Prediction;

 Key | Game_Date  | Game_Result | ML_Prediction | At_Bats | Runs_Scored | Hits | Runs_Batted_In | Walks | Strikeouts | Batting_Average | On_Base_Percentage | Slugging_Percentage | OnBase_Plus_Slugging
-----+------------+-------------+---------------+---------+-------------+------+----------------+-------+------------+-----------------+--------------------+---------------------+----------------------
   5 | 2021-04-06 |           1 |             0 |      44 |           6 |   10 |              5 |     3 |         15 |           0.227 |              0.292 |               0.432 |                0.723
  20 | 2021-04-22 |           0 |             1 |      38 |           3 |    8 |              2 |     2 |         11 |           0.211 |              0.268 |               0.395 |                0.663
  22 | 2021-04-24 |           0 |             1 |      31 |           2 |    6 |              2 |     1 |          9 |           0.194 |              0.242 |                0.29 |                0.533
  24 | 2021-04-27 |           1 |             0 |      29 |           2 |    5 |              2 |     2 |          8 |           0.172 |              0.226 |               0.345 |                0.571
  25 | 2021-04-28 |           1 |             0 |      30 |           1 |    4 |              1 |     1 |         15 |           0.133 |              0.161 |               0.233 |                0.395
  28 | 2021-05-01 |           0 |             1 |      38 |           6 |   12 |              6 |     4 |         12 |           0.316 |              0.372 |               0.447 |                0.819
  42 | 2021-05-16 |           0 |             1 |      35 |           5 |    9 |              5 |     2 |         14 |           0.257 |              0.297 |               0.486 |                0.783
  47 | 2021-05-22 |           1 |             0 |      33 |           4 |    7 |              4 |     5 |         11 |           0.212 |              0.325 |               0.424 |                0.749
  52 | 2021-05-29 |           1 |             0 |      35 |           3 |   12 |              3 |     0 |          6 |           0.343 |              0.343 |               0.486 |                0.829
  62 | 2021-06-09 |           0 |             1 |      30 |           3 |    4 |              3 |     1 |          9 |           0.133 |              0.156 |               0.267 |                0.423
  67 | 2021-06-14 |           1 |             0 |      31 |           2 |    7 |              2 |     1 |          7 |           0.226 |               0.25 |               0.258 |                0.508

(11 rows)
