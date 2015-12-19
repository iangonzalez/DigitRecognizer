import sys
import numpy as np
from DigitReader import ImageReader
img_reader = ImageReader()
features_file = sys.argv[1]
img_reader.readImgFromFile(features_file)
features = img_reader.getPxDataArray()
pixels_low = []
pixels_high = []
if features[17][14] <= 0.5:
	pixels_low.append((17, 14))
	if features[14][15] <= 0.5:
		pixels_low.append((14, 15))
		if features[7][16] <= 5.5:
			pixels_low.append((7, 16))
			if features[15][11] <= 8.0:
				pixels_low.append((15, 11))
				if features[13][17] <= 1.0:
					pixels_low.append((13, 17))
					if features[15][6] <= 1.5:
						pixels_low.append((15, 6))
						if features[10][20] <= 16.0:
							pixels_low.append((10, 20))
							if features[8][22] <= 27.0:
								pixels_low.append((8, 22))
								if features[13][5] <= 64.5:
									pixels_low.append((13, 5))
									if features[14][13] <= 127.0:
										pixels_low.append((14, 13))
										if features[7][5] <= 89.5:
											pixels_low.append((7, 5))
											ans = 7											 # approximately 84 were 7 out of 84 samples at leaf node
										else:
											pixels_high.append((7, 5))
											ans = 4											 # approximately 1 were 4 out of 1 samples at leaf node
									else:
										pixels_high.append((14, 13))
										ans = 9										 # approximately 1 were 9 out of 1 samples at leaf node
								else:
									pixels_high.append((13, 5))
									if features[11][16] <= 94.0:
										pixels_low.append((11, 16))
										ans = 4										 # approximately 1 were 4 out of 1 samples at leaf node
									else:
										pixels_high.append((11, 16))
										ans = 6										 # approximately 3 were 6 out of 3 samples at leaf node
							else:
								pixels_high.append((8, 22))
								if features[13][22] <= 154.5:
									pixels_low.append((13, 22))
									ans = 0									 # approximately 3 were 0 out of 3 samples at leaf node
								else:
									pixels_high.append((13, 22))
									if features[8][20] <= 88.0:
										pixels_low.append((8, 20))
										ans = 2										 # approximately 2 were 2 out of 2 samples at leaf node
									else:
										pixels_high.append((8, 20))
										if features[8][10] <= 8.5:
											pixels_low.append((8, 10))
											ans = 8											 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											pixels_high.append((8, 10))
											ans = 5											 # approximately 2 were 5 out of 2 samples at leaf node
						else:
							pixels_high.append((10, 20))
							if features[12][14] <= 8.5:
								pixels_low.append((12, 14))
								if features[18][19] <= 3.5:
									pixels_low.append((18, 19))
									if features[20][17] <= 7.5:
										pixels_low.append((20, 17))
										if features[15][9] <= 89.5:
											pixels_low.append((15, 9))
											if features[20][12] <= 127.0:
												pixels_low.append((20, 12))
												ans = 6												 # approximately 1 were 6 out of 1 samples at leaf node
											else:
												pixels_high.append((20, 12))
												ans = 2												 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											pixels_high.append((15, 9))
											ans = 5											 # approximately 2 were 5 out of 2 samples at leaf node
									else:
										pixels_high.append((20, 17))
										ans = 0										 # approximately 2 were 0 out of 2 samples at leaf node
								else:
									pixels_high.append((18, 19))
									ans = 0									 # approximately 28 were 0 out of 28 samples at leaf node
							else:
								pixels_high.append((12, 14))
								if features[11][15] <= 5.5:
									pixels_low.append((11, 15))
									ans = 5									 # approximately 4 were 5 out of 4 samples at leaf node
								else:
									pixels_high.append((11, 15))
									if features[10][4] <= 126.5:
										pixels_low.append((10, 4))
										if features[11][13] <= 186.5:
											pixels_low.append((11, 13))
											ans = 6											 # approximately 3 were 6 out of 3 samples at leaf node
										else:
											pixels_high.append((11, 13))
											if features[16][19] <= 47.0:
												pixels_low.append((16, 19))
												ans = 8												 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												pixels_high.append((16, 19))
												if features[7][19] <= 66.5:
													pixels_low.append((7, 19))
													ans = 7													 # approximately 1 were 7 out of 1 samples at leaf node
												else:
													pixels_high.append((7, 19))
													ans = 3													 # approximately 1 were 3 out of 1 samples at leaf node
									else:
										pixels_high.append((10, 4))
										ans = 2										 # approximately 3 were 2 out of 3 samples at leaf node
					else:
						pixels_high.append((15, 6))
						if features[11][22] <= 16.5:
							pixels_low.append((11, 22))
							if features[16][4] <= 17.0:
								pixels_low.append((16, 4))
								if features[20][9] <= 115.0:
									pixels_low.append((20, 9))
									if features[9][18] <= 143.5:
										pixels_low.append((9, 18))
										if features[12][6] <= 236.0:
											pixels_low.append((12, 6))
											if features[16][18] <= 236.0:
												pixels_low.append((16, 18))
												ans = 5												 # approximately 7 were 5 out of 7 samples at leaf node
											else:
												pixels_high.append((16, 18))
												ans = 6												 # approximately 1 were 6 out of 1 samples at leaf node
										else:
											pixels_high.append((12, 6))
											if features[16][19] <= 154.0:
												pixels_low.append((16, 19))
												ans = 0												 # approximately 2 were 0 out of 2 samples at leaf node
											else:
												pixels_high.append((16, 19))
												if features[9][14] <= 90.5:
													pixels_low.append((9, 14))
													if features[18][14] <= 109.5:
														pixels_low.append((18, 14))
														ans = 2														 # approximately 1 were 2 out of 1 samples at leaf node
													else:
														pixels_high.append((18, 14))
														ans = 7														 # approximately 1 were 7 out of 1 samples at leaf node
												else:
													pixels_high.append((9, 14))
													ans = 9													 # approximately 1 were 9 out of 1 samples at leaf node
									else:
										pixels_high.append((9, 18))
										ans = 2										 # approximately 6 were 2 out of 6 samples at leaf node
								else:
									pixels_high.append((20, 9))
									if features[20][23] <= 126.0:
										pixels_low.append((20, 23))
										ans = 0										 # approximately 16 were 0 out of 16 samples at leaf node
									else:
										pixels_high.append((20, 23))
										ans = 9										 # approximately 2 were 9 out of 2 samples at leaf node
							else:
								pixels_high.append((16, 4))
								if features[20][11] <= 10.5:
									pixels_low.append((20, 11))
									if features[21][12] <= 138.5:
										pixels_low.append((21, 12))
										ans = 6										 # approximately 20 were 6 out of 20 samples at leaf node
									else:
										pixels_high.append((21, 12))
										ans = 0										 # approximately 1 were 0 out of 1 samples at leaf node
								else:
									pixels_high.append((20, 11))
									if features[9][7] <= 120.0:
										pixels_low.append((9, 7))
										if features[16][6] <= 139.5:
											pixels_low.append((16, 6))
											ans = 4											 # approximately 1 were 4 out of 1 samples at leaf node
										else:
											pixels_high.append((16, 6))
											ans = 1											 # approximately 1 were 1 out of 1 samples at leaf node
									else:
										pixels_high.append((9, 7))
										ans = 0										 # approximately 1 were 0 out of 1 samples at leaf node
						else:
							pixels_high.append((11, 22))
							if features[16][13] <= 22.5:
								pixels_low.append((16, 13))
								if features[14][19] <= 181.5:
									pixels_low.append((14, 19))
									if features[15][10] <= 184.5:
										pixels_low.append((15, 10))
										if features[24][17] <= 164.5:
											pixels_low.append((24, 17))
											if features[20][3] <= 190.0:
												pixels_low.append((20, 3))
												if features[8][6] <= 253.5:
													pixels_low.append((8, 6))
													if features[14][10] <= 209.5:
														pixels_low.append((14, 10))
														ans = 0														 # approximately 321 were 0 out of 321 samples at leaf node
													else:
														pixels_high.append((14, 10))
														if features[17][10] <= 105.0:
															pixels_low.append((17, 10))
															ans = 0															 # approximately 9 were 0 out of 9 samples at leaf node
														else:
															pixels_high.append((17, 10))
															if features[19][10] <= 181.5:
																pixels_low.append((19, 10))
																ans = 5																 # approximately 1 were 5 out of 1 samples at leaf node
															else:
																pixels_high.append((19, 10))
																ans = 9																 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													pixels_high.append((8, 6))
													if features[21][13] <= 97.5:
														pixels_low.append((21, 13))
														ans = 5														 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														pixels_high.append((21, 13))
														ans = 0														 # approximately 1 were 0 out of 1 samples at leaf node
											else:
												pixels_high.append((20, 3))
												ans = 6												 # approximately 1 were 6 out of 1 samples at leaf node
										else:
											pixels_high.append((24, 17))
											ans = 2											 # approximately 2 were 2 out of 2 samples at leaf node
									else:
										pixels_high.append((15, 10))
										if features[8][17] <= 32.0:
											pixels_low.append((8, 17))
											if features[15][6] <= 232.0:
												pixels_low.append((15, 6))
												ans = 5												 # approximately 4 were 5 out of 4 samples at leaf node
											else:
												pixels_high.append((15, 6))
												if features[19][8] <= 45.5:
													pixels_low.append((19, 8))
													ans = 3													 # approximately 2 were 3 out of 2 samples at leaf node
												else:
													pixels_high.append((19, 8))
													ans = 0													 # approximately 1 were 0 out of 1 samples at leaf node
										else:
											pixels_high.append((8, 17))
											ans = 0											 # approximately 4 were 0 out of 4 samples at leaf node
								else:
									pixels_high.append((14, 19))
									if features[11][10] <= 21.0:
										pixels_low.append((11, 10))
										if features[20][9] <= 195.0:
											pixels_low.append((20, 9))
											if features[16][19] <= 90.0:
												pixels_low.append((16, 19))
												ans = 3												 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												pixels_high.append((16, 19))
												ans = 2												 # approximately 9 were 2 out of 9 samples at leaf node
										else:
											pixels_high.append((20, 9))
											ans = 7											 # approximately 2 were 7 out of 2 samples at leaf node
									else:
										pixels_high.append((11, 10))
										if features[15][5] <= 34.5:
											pixels_low.append((15, 5))
											if features[11][22] <= 146.0:
												pixels_low.append((11, 22))
												ans = 2												 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												pixels_high.append((11, 22))
												ans = 6												 # approximately 1 were 6 out of 1 samples at leaf node
										else:
											pixels_high.append((15, 5))
											if features[8][13] <= 223.0:
												pixels_low.append((8, 13))
												ans = 0												 # approximately 15 were 0 out of 15 samples at leaf node
											else:
												pixels_high.append((8, 13))
												ans = 7												 # approximately 1 were 7 out of 1 samples at leaf node
							else:
								pixels_high.append((16, 13))
								if features[18][6] <= 126.5:
									pixels_low.append((18, 6))
									if features[13][5] <= 128.0:
										pixels_low.append((13, 5))
										ans = 6										 # approximately 2 were 6 out of 2 samples at leaf node
									else:
										pixels_high.append((13, 5))
										ans = 3										 # approximately 1 were 3 out of 1 samples at leaf node
								else:
									pixels_high.append((18, 6))
									ans = 5									 # approximately 5 were 5 out of 5 samples at leaf node
				else:
					pixels_high.append((13, 17))
					if features[11][19] <= 86.0:
						pixels_low.append((11, 19))
						if features[19][15] <= 11.5:
							pixels_low.append((19, 15))
							if features[18][4] <= 26.0:
								pixels_low.append((18, 4))
								if features[14][3] <= 5.0:
									pixels_low.append((14, 3))
									if features[14][13] <= 36.0:
										pixels_low.append((14, 13))
										if features[21][18] <= 169.5:
											pixels_low.append((21, 18))
											if features[17][2] <= 107.5:
												pixels_low.append((17, 2))
												ans = 5												 # approximately 98 were 5 out of 98 samples at leaf node
											else:
												pixels_high.append((17, 2))
												ans = 6												 # approximately 1 were 6 out of 1 samples at leaf node
										else:
											pixels_high.append((21, 18))
											if features[24][18] <= 29.0:
												pixels_low.append((24, 18))
												ans = 0												 # approximately 1 were 0 out of 1 samples at leaf node
											else:
												pixels_high.append((24, 18))
												ans = 2												 # approximately 2 were 2 out of 2 samples at leaf node
									else:
										pixels_high.append((14, 13))
										if features[8][23] <= 43.0:
											pixels_low.append((8, 23))
											if features[9][17] <= 124.0:
												pixels_low.append((9, 17))
												ans = 1												 # approximately 1 were 1 out of 1 samples at leaf node
											else:
												pixels_high.append((9, 17))
												ans = 8												 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											pixels_high.append((8, 23))
											ans = 3											 # approximately 2 were 3 out of 2 samples at leaf node
								else:
									pixels_high.append((14, 3))
									ans = 6									 # approximately 4 were 6 out of 4 samples at leaf node
							else:
								pixels_high.append((18, 4))
								ans = 6								 # approximately 6 were 6 out of 6 samples at leaf node
						else:
							pixels_high.append((19, 15))
							if features[11][15] <= 103.5:
								pixels_low.append((11, 15))
								if features[16][8] <= 235.0:
									pixels_low.append((16, 8))
									ans = 2									 # approximately 14 were 2 out of 14 samples at leaf node
								else:
									pixels_high.append((16, 8))
									ans = 7									 # approximately 3 were 7 out of 3 samples at leaf node
							else:
								pixels_high.append((11, 15))
								if features[16][19] <= 204.0:
									pixels_low.append((16, 19))
									if features[10][11] <= 253.5:
										pixels_low.append((10, 11))
										ans = 9										 # approximately 2 were 9 out of 2 samples at leaf node
									else:
										pixels_high.append((10, 11))
										if features[15][7] <= 127.0:
											pixels_low.append((15, 7))
											ans = 4											 # approximately 1 were 4 out of 1 samples at leaf node
										else:
											pixels_high.append((15, 7))
											ans = 8											 # approximately 1 were 8 out of 1 samples at leaf node
								else:
									pixels_high.append((16, 19))
									ans = 6									 # approximately 6 were 6 out of 6 samples at leaf node
					else:
						pixels_high.append((11, 19))
						if features[9][7] <= 1.5:
							pixels_low.append((9, 7))
							if features[11][15] <= 12.0:
								pixels_low.append((11, 15))
								if features[14][17] <= 145.0:
									pixels_low.append((14, 17))
									if features[26][9] <= 8.0:
										pixels_low.append((26, 9))
										if features[20][21] <= 65.5:
											pixels_low.append((20, 21))
											if features[15][18] <= 151.0:
												pixels_low.append((15, 18))
												ans = 6												 # approximately 1 were 6 out of 1 samples at leaf node
											else:
												pixels_high.append((15, 18))
												ans = 0												 # approximately 1 were 0 out of 1 samples at leaf node
										else:
											pixels_high.append((20, 21))
											ans = 9											 # approximately 2 were 9 out of 2 samples at leaf node
									else:
										pixels_high.append((26, 9))
										ans = 5										 # approximately 2 were 5 out of 2 samples at leaf node
								else:
									pixels_high.append((14, 17))
									if features[8][7] <= 22.0:
										pixels_low.append((8, 7))
										ans = 2										 # approximately 6 were 2 out of 6 samples at leaf node
									else:
										pixels_high.append((8, 7))
										ans = 4										 # approximately 1 were 4 out of 1 samples at leaf node
							else:
								pixels_high.append((11, 15))
								if features[16][5] <= 2.5:
									pixels_low.append((16, 5))
									if features[15][4] <= 7.5:
										pixels_low.append((15, 4))
										if features[21][18] <= 6.5:
											pixels_low.append((21, 18))
											if features[11][12] <= 41.5:
												pixels_low.append((11, 12))
												if features[16][18] <= 211.0:
													pixels_low.append((16, 18))
													ans = 6													 # approximately 1 were 6 out of 1 samples at leaf node
												else:
													pixels_high.append((16, 18))
													ans = 4													 # approximately 1 were 4 out of 1 samples at leaf node
											else:
												pixels_high.append((11, 12))
												if features[12][20] <= 253.5:
													pixels_low.append((12, 20))
													ans = 5													 # approximately 4 were 5 out of 4 samples at leaf node
												else:
													pixels_high.append((12, 20))
													ans = 1													 # approximately 1 were 1 out of 1 samples at leaf node
										else:
											pixels_high.append((21, 18))
											ans = 2											 # approximately 3 were 2 out of 3 samples at leaf node
									else:
										pixels_high.append((15, 4))
										ans = 6										 # approximately 5 were 6 out of 5 samples at leaf node
								else:
									pixels_high.append((16, 5))
									if features[12][4] <= 183.0:
										pixels_low.append((12, 4))
										ans = 6										 # approximately 61 were 6 out of 61 samples at leaf node
									else:
										pixels_high.append((12, 4))
										ans = 2										 # approximately 1 were 2 out of 1 samples at leaf node
						else:
							pixels_high.append((9, 7))
							if features[15][19] <= 64.0:
								pixels_low.append((15, 19))
								if features[12][16] <= 46.0:
									pixels_low.append((12, 16))
									if features[20][15] <= 84.5:
										pixels_low.append((20, 15))
										ans = 4										 # approximately 2 were 4 out of 2 samples at leaf node
									else:
										pixels_high.append((20, 15))
										ans = 6										 # approximately 1 were 6 out of 1 samples at leaf node
								else:
									pixels_high.append((12, 16))
									ans = 0									 # approximately 5 were 0 out of 5 samples at leaf node
							else:
								pixels_high.append((15, 19))
								if features[4][5] <= 149.0:
									pixels_low.append((4, 5))
									ans = 2									 # approximately 32 were 2 out of 32 samples at leaf node
								else:
									pixels_high.append((4, 5))
									ans = 7									 # approximately 1 were 7 out of 1 samples at leaf node
			else:
				pixels_high.append((15, 11))
				if features[4][10] <= 1.5:
					pixels_low.append((4, 10))
					if features[10][17] <= 112.5:
						pixels_low.append((10, 17))
						if features[9][10] <= 5.5:
							pixels_low.append((9, 10))
							if features[12][5] <= 12.5:
								pixels_low.append((12, 5))
								if features[11][7] <= 60.0:
									pixels_low.append((11, 7))
									if features[9][16] <= 227.0:
										pixels_low.append((9, 16))
										if features[4][19] <= 220.0:
											pixels_low.append((4, 19))
											if features[12][11] <= 7.5:
												pixels_low.append((12, 11))
												if features[14][20] <= 116.0:
													pixels_low.append((14, 20))
													if features[20][16] <= 13.5:
														pixels_low.append((20, 16))
														if features[15][18] <= 29.5:
															pixels_low.append((15, 18))
															if features[16][6] <= 2.0:
																pixels_low.append((16, 6))
																ans = 5																 # approximately 2 were 5 out of 2 samples at leaf node
															else:
																pixels_high.append((16, 6))
																if features[17][4] <= 127.0:
																	pixels_low.append((17, 4))
																	ans = 1																	 # approximately 1 were 1 out of 1 samples at leaf node
																else:
																	pixels_high.append((17, 4))
																	ans = 8																	 # approximately 1 were 8 out of 1 samples at leaf node
														else:
															pixels_high.append((15, 18))
															ans = 2															 # approximately 2 were 2 out of 2 samples at leaf node
													else:
														pixels_high.append((20, 16))
														ans = 4														 # approximately 2 were 4 out of 2 samples at leaf node
												else:
													pixels_high.append((14, 20))
													if features[16][18] <= 232.0:
														pixels_low.append((16, 18))
														ans = 3														 # approximately 5 were 3 out of 5 samples at leaf node
													else:
														pixels_high.append((16, 18))
														ans = 6														 # approximately 1 were 6 out of 1 samples at leaf node
											else:
												pixels_high.append((12, 11))
												if features[8][12] <= 249.0:
													pixels_low.append((8, 12))
													if features[15][23] <= 207.0:
														pixels_low.append((15, 23))
														if features[23][13] <= 39.0:
															pixels_low.append((23, 13))
															if features[18][15] <= 187.5:
																pixels_low.append((18, 15))
																if features[17][17] <= 252.5:
																	pixels_low.append((17, 17))
																	ans = 5																	 # approximately 63 were 5 out of 63 samples at leaf node
																else:
																	pixels_high.append((17, 17))
																	ans = 6																	 # approximately 1 were 6 out of 1 samples at leaf node
															else:
																pixels_high.append((18, 15))
																ans = 3																 # approximately 1 were 3 out of 1 samples at leaf node
														else:
															pixels_high.append((23, 13))
															ans = 0															 # approximately 1 were 0 out of 1 samples at leaf node
													else:
														pixels_high.append((15, 23))
														if features[12][13] <= 215.5:
															pixels_low.append((12, 13))
															if features[14][11] <= 122.0:
																pixels_low.append((14, 11))
																if features[20][19] <= 55.0:
																	pixels_low.append((20, 19))
																	ans = 4																	 # approximately 1 were 4 out of 1 samples at leaf node
																else:
																	pixels_high.append((20, 19))
																	ans = 3																	 # approximately 1 were 3 out of 1 samples at leaf node
															else:
																pixels_high.append((14, 11))
																ans = 5																 # approximately 3 were 5 out of 3 samples at leaf node
														else:
															pixels_high.append((12, 13))
															ans = 1															 # approximately 3 were 1 out of 3 samples at leaf node
												else:
													pixels_high.append((8, 12))
													ans = 7													 # approximately 3 were 7 out of 3 samples at leaf node
										else:
											pixels_high.append((4, 19))
											ans = 3											 # approximately 6 were 3 out of 6 samples at leaf node
									else:
										pixels_high.append((9, 16))
										if features[15][11] <= 185.5:
											pixels_low.append((15, 11))
											ans = 0											 # approximately 5 were 0 out of 5 samples at leaf node
										else:
											pixels_high.append((15, 11))
											if features[21][15] <= 196.5:
												pixels_low.append((21, 15))
												ans = 8												 # approximately 4 were 8 out of 4 samples at leaf node
											else:
												pixels_high.append((21, 15))
												ans = 6												 # approximately 2 were 6 out of 2 samples at leaf node
								else:
									pixels_high.append((11, 7))
									if features[14][6] <= 254.5:
										pixels_low.append((14, 6))
										if features[14][12] <= 12.0:
											pixels_low.append((14, 12))
											if features[13][21] <= 126.0:
												pixels_low.append((13, 21))
												ans = 7												 # approximately 2 were 7 out of 2 samples at leaf node
											else:
												pixels_high.append((13, 21))
												if features[4][15] <= 125.0:
													pixels_low.append((4, 15))
													ans = 2													 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													pixels_high.append((4, 15))
													ans = 0													 # approximately 1 were 0 out of 1 samples at leaf node
										else:
											pixels_high.append((14, 12))
											if features[10][10] <= 60.5:
												pixels_low.append((10, 10))
												ans = 3												 # approximately 27 were 3 out of 27 samples at leaf node
											else:
												pixels_high.append((10, 10))
												if features[14][23] <= 121.5:
													pixels_low.append((14, 23))
													ans = 4													 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													pixels_high.append((14, 23))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
									else:
										pixels_high.append((14, 6))
										ans = 5										 # approximately 3 were 5 out of 3 samples at leaf node
							else:
								pixels_high.append((12, 5))
								if features[11][9] <= 140.5:
									pixels_low.append((11, 9))
									if features[6][11] <= 109.5:
										pixels_low.append((6, 11))
										if features[11][18] <= 188.0:
											pixels_low.append((11, 18))
											if features[14][16] <= 218.5:
												pixels_low.append((14, 16))
												if features[20][22] <= 244.0:
													pixels_low.append((20, 22))
													if features[23][10] <= 79.5:
														pixels_low.append((23, 10))
														if features[12][9] <= 250.0:
															pixels_low.append((12, 9))
															ans = 3															 # approximately 169 were 3 out of 169 samples at leaf node
														else:
															pixels_high.append((12, 9))
															if features[14][22] <= 138.5:
																pixels_low.append((14, 22))
																ans = 3																 # approximately 2 were 3 out of 2 samples at leaf node
															else:
																pixels_high.append((14, 22))
																ans = 5																 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														pixels_high.append((23, 10))
														ans = 5														 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													pixels_high.append((20, 22))
													if features[6][11] <= 15.0:
														pixels_low.append((6, 11))
														ans = 8														 # approximately 1 were 8 out of 1 samples at leaf node
													else:
														pixels_high.append((6, 11))
														ans = 5														 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												pixels_high.append((14, 16))
												ans = 1												 # approximately 2 were 1 out of 2 samples at leaf node
										else:
											pixels_high.append((11, 18))
											if features[13][16] <= 3.5:
												pixels_low.append((13, 16))
												if features[19][13] <= 87.5:
													pixels_low.append((19, 13))
													ans = 8													 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													pixels_high.append((19, 13))
													ans = 3													 # approximately 2 were 3 out of 2 samples at leaf node
											else:
												pixels_high.append((13, 16))
												ans = 2												 # approximately 4 were 2 out of 4 samples at leaf node
									else:
										pixels_high.append((6, 11))
										if features[16][19] <= 126.0:
											pixels_low.append((16, 19))
											ans = 5											 # approximately 6 were 5 out of 6 samples at leaf node
										else:
											pixels_high.append((16, 19))
											ans = 9											 # approximately 1 were 9 out of 1 samples at leaf node
								else:
									pixels_high.append((11, 9))
									if features[16][8] <= 40.5:
										pixels_low.append((16, 8))
										if features[14][12] <= 253.0:
											pixels_low.append((14, 12))
											ans = 5											 # approximately 12 were 5 out of 12 samples at leaf node
										else:
											pixels_high.append((14, 12))
											ans = 6											 # approximately 1 were 6 out of 1 samples at leaf node
									else:
										pixels_high.append((16, 8))
										if features[14][22] <= 21.5:
											pixels_low.append((14, 22))
											if features[20][5] <= 127.5:
												pixels_low.append((20, 5))
												ans = 8												 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												pixels_high.append((20, 5))
												ans = 5												 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											pixels_high.append((14, 22))
											ans = 3											 # approximately 4 were 3 out of 4 samples at leaf node
						else:
							pixels_high.append((9, 10))
							if features[14][6] <= 6.5:
								pixels_low.append((14, 6))
								if features[18][17] <= 84.5:
									pixels_low.append((18, 17))
									if features[5][15] <= 95.5:
										pixels_low.append((5, 15))
										if features[14][13] <= 27.5:
											pixels_low.append((14, 13))
											if features[20][12] <= 153.0:
												pixels_low.append((20, 12))
												if features[16][16] <= 126.5:
													pixels_low.append((16, 16))
													ans = 5													 # approximately 18 were 5 out of 18 samples at leaf node
												else:
													pixels_high.append((16, 16))
													ans = 7													 # approximately 1 were 7 out of 1 samples at leaf node
											else:
												pixels_high.append((20, 12))
												if features[19][7] <= 6.5:
													pixels_low.append((19, 7))
													ans = 7													 # approximately 2 were 7 out of 2 samples at leaf node
												else:
													pixels_high.append((19, 7))
													if features[22][19] <= 38.0:
														pixels_low.append((22, 19))
														ans = 0														 # approximately 1 were 0 out of 1 samples at leaf node
													else:
														pixels_high.append((22, 19))
														ans = 3														 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											pixels_high.append((14, 13))
											if features[12][8] <= 39.5:
												pixels_low.append((12, 8))
												if features[20][19] <= 85.5:
													pixels_low.append((20, 19))
													ans = 4													 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													pixels_high.append((20, 19))
													ans = 8													 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												pixels_high.append((12, 8))
												ans = 9												 # approximately 4 were 9 out of 4 samples at leaf node
									else:
										pixels_high.append((5, 15))
										ans = 0										 # approximately 6 were 0 out of 6 samples at leaf node
								else:
									pixels_high.append((18, 17))
									if features[19][7] <= 81.5:
										pixels_low.append((19, 7))
										ans = 7										 # approximately 28 were 7 out of 28 samples at leaf node
									else:
										pixels_high.append((19, 7))
										if features[18][7] <= 239.5:
											pixels_low.append((18, 7))
											if features[16][16] <= 8.5:
												pixels_low.append((16, 16))
												ans = 5												 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												pixels_high.append((16, 16))
												ans = 3												 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											pixels_high.append((18, 7))
											ans = 0											 # approximately 2 were 0 out of 2 samples at leaf node
							else:
								pixels_high.append((14, 6))
								if features[16][9] <= 112.0:
									pixels_low.append((16, 9))
									if features[14][9] <= 209.0:
										pixels_low.append((14, 9))
										if features[9][12] <= 42.0:
											pixels_low.append((9, 12))
											if features[14][7] <= 198.0:
												pixels_low.append((14, 7))
												ans = 5												 # approximately 6 were 5 out of 6 samples at leaf node
											else:
												pixels_high.append((14, 7))
												if features[22][14] <= 13.5:
													pixels_low.append((22, 14))
													ans = 3													 # approximately 5 were 3 out of 5 samples at leaf node
												else:
													pixels_high.append((22, 14))
													if features[17][20] <= 54.0:
														pixels_low.append((17, 20))
														ans = 8														 # approximately 1 were 8 out of 1 samples at leaf node
													else:
														pixels_high.append((17, 20))
														ans = 0														 # approximately 1 were 0 out of 1 samples at leaf node
										else:
											pixels_high.append((9, 12))
											if features[8][16] <= 198.5:
												pixels_low.append((8, 16))
												if features[16][11] <= 4.5:
													pixels_low.append((16, 11))
													ans = 3													 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													pixels_high.append((16, 11))
													if features[17][16] <= 86.0:
														pixels_low.append((17, 16))
														ans = 5														 # approximately 110 were 5 out of 110 samples at leaf node
													else:
														pixels_high.append((17, 16))
														ans = 9														 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												pixels_high.append((8, 16))
												ans = 8												 # approximately 1 were 8 out of 1 samples at leaf node
									else:
										pixels_high.append((14, 9))
										if features[10][5] <= 107.5:
											pixels_low.append((10, 5))
											if features[12][20] <= 34.0:
												pixels_low.append((12, 20))
												ans = 7												 # approximately 1 were 7 out of 1 samples at leaf node
											else:
												pixels_high.append((12, 20))
												ans = 5												 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											pixels_high.append((10, 5))
											ans = 3											 # approximately 5 were 3 out of 5 samples at leaf node
								else:
									pixels_high.append((16, 9))
									if features[20][9] <= 225.0:
										pixels_low.append((20, 9))
										if features[9][10] <= 204.5:
											pixels_low.append((9, 10))
											if features[12][9] <= 244.0:
												pixels_low.append((12, 9))
												if features[8][10] <= 172.0:
													pixels_low.append((8, 10))
													ans = 3													 # approximately 20 were 3 out of 20 samples at leaf node
												else:
													pixels_high.append((8, 10))
													if features[10][11] <= 114.5:
														pixels_low.append((10, 11))
														ans = 2														 # approximately 1 were 2 out of 1 samples at leaf node
													else:
														pixels_high.append((10, 11))
														ans = 8														 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												pixels_high.append((12, 9))
												ans = 5												 # approximately 3 were 5 out of 3 samples at leaf node
										else:
											pixels_high.append((9, 10))
											if features[10][11] <= 252.5:
												pixels_low.append((10, 11))
												if features[12][22] <= 92.0:
													pixels_low.append((12, 22))
													ans = 9													 # approximately 2 were 9 out of 2 samples at leaf node
												else:
													pixels_high.append((12, 22))
													if features[8][19] <= 210.0:
														pixels_low.append((8, 19))
														ans = 2														 # approximately 1 were 2 out of 1 samples at leaf node
													else:
														pixels_high.append((8, 19))
														if features[16][19] <= 27.5:
															pixels_low.append((16, 19))
															ans = 8															 # approximately 1 were 8 out of 1 samples at leaf node
														else:
															pixels_high.append((16, 19))
															ans = 3															 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												pixels_high.append((10, 11))
												ans = 5												 # approximately 9 were 5 out of 9 samples at leaf node
									else:
										pixels_high.append((20, 9))
										if features[17][9] <= 252.5:
											pixels_low.append((17, 9))
											ans = 0											 # approximately 7 were 0 out of 7 samples at leaf node
										else:
											pixels_high.append((17, 9))
											ans = 9											 # approximately 1 were 9 out of 1 samples at leaf node
					else:
						pixels_high.append((10, 17))
						if features[10][12] <= 14.0:
							pixels_low.append((10, 12))
							if features[22][20] <= 0.5:
								pixels_low.append((22, 20))
								if features[20][3] <= 1.5:
									pixels_low.append((20, 3))
									if features[17][11] <= 108.0:
										pixels_low.append((17, 11))
										if features[12][10] <= 82.5:
											pixels_low.append((12, 10))
											if features[16][20] <= 252.5:
												pixels_low.append((16, 20))
												ans = 2												 # approximately 22 were 2 out of 22 samples at leaf node
											else:
												pixels_high.append((16, 20))
												if features[20][20] <= 89.5:
													pixels_low.append((20, 20))
													ans = 6													 # approximately 3 were 6 out of 3 samples at leaf node
												else:
													pixels_high.append((20, 20))
													ans = 2													 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											pixels_high.append((12, 10))
											if features[13][21] <= 126.5:
												pixels_low.append((13, 21))
												ans = 1												 # approximately 2 were 1 out of 2 samples at leaf node
											else:
												pixels_high.append((13, 21))
												ans = 0												 # approximately 1 were 0 out of 1 samples at leaf node
									else:
										pixels_high.append((17, 11))
										if features[15][13] <= 235.0:
											pixels_low.append((15, 13))
											if features[11][5] <= 176.5:
												pixels_low.append((11, 5))
												if features[18][13] <= 25.5:
													pixels_low.append((18, 13))
													if features[14][14] <= 18.0:
														pixels_low.append((14, 14))
														if features[22][6] <= 32.0:
															pixels_low.append((22, 6))
															ans = 5															 # approximately 6 were 5 out of 6 samples at leaf node
														else:
															pixels_high.append((22, 6))
															ans = 0															 # approximately 1 were 0 out of 1 samples at leaf node
													else:
														pixels_high.append((14, 14))
														if features[12][16] <= 92.5:
															pixels_low.append((12, 16))
															ans = 2															 # approximately 3 were 2 out of 3 samples at leaf node
														else:
															pixels_high.append((12, 16))
															if features[14][10] <= 109.5:
																pixels_low.append((14, 10))
																if features[22][6] <= 122.5:
																	pixels_low.append((22, 6))
																	ans = 3																	 # approximately 1 were 3 out of 1 samples at leaf node
																else:
																	pixels_high.append((22, 6))
																	ans = 1																	 # approximately 1 were 1 out of 1 samples at leaf node
															else:
																pixels_high.append((14, 10))
																if features[9][7] <= 72.5:
																	pixels_low.append((9, 7))
																	ans = 6																	 # approximately 1 were 6 out of 1 samples at leaf node
																else:
																	pixels_high.append((9, 7))
																	ans = 8																	 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													pixels_high.append((18, 13))
													ans = 6													 # approximately 6 were 6 out of 6 samples at leaf node
											else:
												pixels_high.append((11, 5))
												if features[17][22] <= 239.0:
													pixels_low.append((17, 22))
													ans = 3													 # approximately 5 were 3 out of 5 samples at leaf node
												else:
													pixels_high.append((17, 22))
													ans = 2													 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											pixels_high.append((15, 13))
											ans = 8											 # approximately 5 were 8 out of 5 samples at leaf node
								else:
									pixels_high.append((20, 3))
									ans = 6									 # approximately 12 were 6 out of 12 samples at leaf node
							else:
								pixels_high.append((22, 20))
								if features[20][14] <= 124.0:
									pixels_low.append((20, 14))
									if features[24][14] <= 126.5:
										pixels_low.append((24, 14))
										ans = 2										 # approximately 46 were 2 out of 46 samples at leaf node
									else:
										pixels_high.append((24, 14))
										ans = 8										 # approximately 1 were 8 out of 1 samples at leaf node
								else:
									pixels_high.append((20, 14))
									ans = 3									 # approximately 2 were 3 out of 2 samples at leaf node
						else:
							pixels_high.append((10, 12))
							if features[18][19] <= 39.0:
								pixels_low.append((18, 19))
								if features[13][14] <= 127.5:
									pixels_low.append((13, 14))
									if features[19][5] <= 174.5:
										pixels_low.append((19, 5))
										if features[11][4] <= 4.0:
											pixels_low.append((11, 4))
											if features[17][16] <= 72.0:
												pixels_low.append((17, 16))
												if features[22][12] <= 210.5:
													pixels_low.append((22, 12))
													ans = 5													 # approximately 38 were 5 out of 38 samples at leaf node
												else:
													pixels_high.append((22, 12))
													ans = 6													 # approximately 1 were 6 out of 1 samples at leaf node
											else:
												pixels_high.append((17, 16))
												if features[10][7] <= 127.0:
													pixels_low.append((10, 7))
													if features[13][24] <= 118.0:
														pixels_low.append((13, 24))
														ans = 8														 # approximately 1 were 8 out of 1 samples at leaf node
													else:
														pixels_high.append((13, 24))
														ans = 7														 # approximately 1 were 7 out of 1 samples at leaf node
												else:
													pixels_high.append((10, 7))
													ans = 4													 # approximately 1 were 4 out of 1 samples at leaf node
										else:
											pixels_high.append((11, 4))
											ans = 2											 # approximately 2 were 2 out of 2 samples at leaf node
									else:
										pixels_high.append((19, 5))
										if features[20][12] <= 126.5:
											pixels_low.append((20, 12))
											ans = 6											 # approximately 3 were 6 out of 3 samples at leaf node
										else:
											pixels_high.append((20, 12))
											ans = 0											 # approximately 1 were 0 out of 1 samples at leaf node
								else:
									pixels_high.append((13, 14))
									if features[11][19] <= 173.5:
										pixels_low.append((11, 19))
										ans = 8										 # approximately 7 were 8 out of 7 samples at leaf node
									else:
										pixels_high.append((11, 19))
										if features[20][9] <= 127.0:
											pixels_low.append((20, 9))
											ans = 6											 # approximately 2 were 6 out of 2 samples at leaf node
										else:
											pixels_high.append((20, 9))
											ans = 0											 # approximately 1 were 0 out of 1 samples at leaf node
							else:
								pixels_high.append((18, 19))
								if features[12][23] <= 6.0:
									pixels_low.append((12, 23))
									if features[6][19] <= 13.0:
										pixels_low.append((6, 19))
										if features[26][15] <= 106.0:
											pixels_low.append((26, 15))
											if features[27][7] <= 77.0:
												pixels_low.append((27, 7))
												ans = 6												 # approximately 35 were 6 out of 35 samples at leaf node
											else:
												pixels_high.append((27, 7))
												ans = 0												 # approximately 1 were 0 out of 1 samples at leaf node
										else:
											pixels_high.append((26, 15))
											ans = 2											 # approximately 1 were 2 out of 1 samples at leaf node
									else:
										pixels_high.append((6, 19))
										if features[6][22] <= 20.0:
											pixels_low.append((6, 22))
											ans = 2											 # approximately 2 were 2 out of 2 samples at leaf node
										else:
											pixels_high.append((6, 22))
											ans = 3											 # approximately 1 were 3 out of 1 samples at leaf node
								else:
									pixels_high.append((12, 23))
									if features[15][9] <= 29.5:
										pixels_low.append((15, 9))
										if features[20][18] <= 105.0:
											pixels_low.append((20, 18))
											if features[10][9] <= 230.0:
												pixels_low.append((10, 9))
												ans = 8												 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												pixels_high.append((10, 9))
												ans = 6												 # approximately 1 were 6 out of 1 samples at leaf node
										else:
											pixels_high.append((20, 18))
											ans = 5											 # approximately 5 were 5 out of 5 samples at leaf node
									else:
										pixels_high.append((15, 9))
										if features[19][16] <= 11.0:
											pixels_low.append((19, 16))
											if features[13][18] <= 83.5:
												pixels_low.append((13, 18))
												if features[11][15] <= 221.0:
													pixels_low.append((11, 15))
													ans = 8													 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													pixels_high.append((11, 15))
													ans = 2													 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												pixels_high.append((13, 18))
												ans = 5												 # approximately 2 were 5 out of 2 samples at leaf node
										else:
											pixels_high.append((19, 16))
											if features[20][4] <= 254.5:
												pixels_low.append((20, 4))
												if features[13][21] <= 7.5:
													pixels_low.append((13, 21))
													if features[12][7] <= 2.5:
														pixels_low.append((12, 7))
														ans = 0														 # approximately 1 were 0 out of 1 samples at leaf node
													else:
														pixels_high.append((12, 7))
														ans = 6														 # approximately 1 were 6 out of 1 samples at leaf node
												else:
													pixels_high.append((13, 21))
													ans = 0													 # approximately 21 were 0 out of 21 samples at leaf node
											else:
												pixels_high.append((20, 4))
												ans = 6												 # approximately 1 were 6 out of 1 samples at leaf node
				else:
					pixels_high.append((4, 10))
					if features[10][20] <= 7.5:
						pixels_low.append((10, 20))
						if features[16][6] <= 79.0:
							pixels_low.append((16, 6))
							ans = 7							 # approximately 78 were 7 out of 78 samples at leaf node
						else:
							pixels_high.append((16, 6))
							if features[16][23] <= 244.5:
								pixels_low.append((16, 23))
								ans = 3								 # approximately 2 were 3 out of 2 samples at leaf node
							else:
								pixels_high.append((16, 23))
								ans = 5								 # approximately 2 were 5 out of 2 samples at leaf node
					else:
						pixels_high.append((10, 20))
						if features[9][7] <= 253.0:
							pixels_low.append((9, 7))
							ans = 3							 # approximately 7 were 3 out of 7 samples at leaf node
						else:
							pixels_high.append((9, 7))
							ans = 8							 # approximately 1 were 8 out of 1 samples at leaf node
		else:
			pixels_high.append((7, 16))
			if features[13][17] <= 127.0:
				pixels_low.append((13, 17))
				if features[11][22] <= 0.5:
					pixels_low.append((11, 22))
					if features[7][19] <= 34.0:
						pixels_low.append((7, 19))
						if features[11][19] <= 5.0:
							pixels_low.append((11, 19))
							if features[11][14] <= 65.5:
								pixels_low.append((11, 14))
								if features[15][6] <= 93.0:
									pixels_low.append((15, 6))
									if features[13][17] <= 62.0:
										pixels_low.append((13, 17))
										ans = 7										 # approximately 54 were 7 out of 54 samples at leaf node
									else:
										pixels_high.append((13, 17))
										ans = 5										 # approximately 3 were 5 out of 3 samples at leaf node
								else:
									pixels_high.append((15, 6))
									if features[17][6] <= 126.0:
										pixels_low.append((17, 6))
										ans = 4										 # approximately 1 were 4 out of 1 samples at leaf node
									else:
										pixels_high.append((17, 6))
										ans = 0										 # approximately 3 were 0 out of 3 samples at leaf node
							else:
								pixels_high.append((11, 14))
								if features[20][15] <= 116.5:
									pixels_low.append((20, 15))
									ans = 5									 # approximately 6 were 5 out of 6 samples at leaf node
								else:
									pixels_high.append((20, 15))
									if features[13][7] <= 64.5:
										pixels_low.append((13, 7))
										if features[22][9] <= 15.5:
											pixels_low.append((22, 9))
											ans = 4											 # approximately 1 were 4 out of 1 samples at leaf node
										else:
											pixels_high.append((22, 9))
											ans = 7											 # approximately 3 were 7 out of 3 samples at leaf node
									else:
										pixels_high.append((13, 7))
										ans = 9										 # approximately 5 were 9 out of 5 samples at leaf node
						else:
							pixels_high.append((11, 19))
							if features[17][8] <= 28.5:
								pixels_low.append((17, 8))
								if features[16][20] <= 73.0:
									pixels_low.append((16, 20))
									if features[12][18] <= 235.5:
										pixels_low.append((12, 18))
										if features[14][8] <= 128.5:
											pixels_low.append((14, 8))
											if features[20][9] <= 122.5:
												pixels_low.append((20, 9))
												if features[7][17] <= 101.0:
													pixels_low.append((7, 17))
													ans = 9													 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													pixels_high.append((7, 17))
													ans = 6													 # approximately 2 were 6 out of 2 samples at leaf node
											else:
												pixels_high.append((20, 9))
												ans = 0												 # approximately 2 were 0 out of 2 samples at leaf node
										else:
											pixels_high.append((14, 8))
											ans = 2											 # approximately 2 were 2 out of 2 samples at leaf node
									else:
										pixels_high.append((12, 18))
										ans = 4										 # approximately 4 were 4 out of 4 samples at leaf node
								else:
									pixels_high.append((16, 20))
									if features[5][10] <= 195.0:
										pixels_low.append((5, 10))
										if features[26][17] <= 128.0:
											pixels_low.append((26, 17))
											ans = 6											 # approximately 24 were 6 out of 24 samples at leaf node
										else:
											pixels_high.append((26, 17))
											ans = 2											 # approximately 1 were 2 out of 1 samples at leaf node
									else:
										pixels_high.append((5, 10))
										ans = 0										 # approximately 2 were 0 out of 2 samples at leaf node
							else:
								pixels_high.append((17, 8))
								if features[19][14] <= 84.0:
									pixels_low.append((19, 14))
									if features[8][3] <= 99.0:
										pixels_low.append((8, 3))
										if features[17][24] <= 156.0:
											pixels_low.append((17, 24))
											ans = 0											 # approximately 24 were 0 out of 24 samples at leaf node
										else:
											pixels_high.append((17, 24))
											ans = 5											 # approximately 1 were 5 out of 1 samples at leaf node
									else:
										pixels_high.append((8, 3))
										ans = 6										 # approximately 1 were 6 out of 1 samples at leaf node
								else:
									pixels_high.append((19, 14))
									if features[10][20] <= 112.5:
										pixels_low.append((10, 20))
										ans = 9										 # approximately 8 were 9 out of 8 samples at leaf node
									else:
										pixels_high.append((10, 20))
										if features[20][11] <= 8.0:
											pixels_low.append((20, 11))
											if features[7][18] <= 31.5:
												pixels_low.append((7, 18))
												ans = 5												 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												pixels_high.append((7, 18))
												ans = 3												 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											pixels_high.append((20, 11))
											ans = 0											 # approximately 5 were 0 out of 5 samples at leaf node
					else:
						pixels_high.append((7, 19))
						if features[22][12] <= 1.5:
							pixels_low.append((22, 12))
							if features[8][23] <= 1.0:
								pixels_low.append((8, 23))
								if features[20][16] <= 62.5:
									pixels_low.append((20, 16))
									if features[23][9] <= 109.5:
										pixels_low.append((23, 9))
										if features[5][16] <= 132.5:
											pixels_low.append((5, 16))
											if features[24][21] <= 169.5:
												pixels_low.append((24, 21))
												ans = 2												 # approximately 10 were 2 out of 10 samples at leaf node
											else:
												pixels_high.append((24, 21))
												ans = 1												 # approximately 1 were 1 out of 1 samples at leaf node
										else:
											pixels_high.append((5, 16))
											ans = 6											 # approximately 1 were 6 out of 1 samples at leaf node
									else:
										pixels_high.append((23, 9))
										ans = 5										 # approximately 2 were 5 out of 2 samples at leaf node
								else:
									pixels_high.append((20, 16))
									if features[13][19] <= 105.5:
										pixels_low.append((13, 19))
										if features[8][8] <= 18.5:
											pixels_low.append((8, 8))
											ans = 5											 # approximately 3 were 5 out of 3 samples at leaf node
										else:
											pixels_high.append((8, 8))
											ans = 7											 # approximately 4 were 7 out of 4 samples at leaf node
									else:
										pixels_high.append((13, 19))
										if features[9][14] <= 10.5:
											pixels_low.append((9, 14))
											if features[15][6] <= 22.0:
												pixels_low.append((15, 6))
												ans = 0												 # approximately 3 were 0 out of 3 samples at leaf node
											else:
												pixels_high.append((15, 6))
												if features[16][7] <= 137.0:
													pixels_low.append((16, 7))
													ans = 3													 # approximately 2 were 3 out of 2 samples at leaf node
												else:
													pixels_high.append((16, 7))
													ans = 9													 # approximately 2 were 9 out of 2 samples at leaf node
										else:
											pixels_high.append((9, 14))
											if features[18][8] <= 168.0:
												pixels_low.append((18, 8))
												if features[24][16] <= 87.5:
													pixels_low.append((24, 16))
													ans = 6													 # approximately 8 were 6 out of 8 samples at leaf node
												else:
													pixels_high.append((24, 16))
													ans = 2													 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												pixels_high.append((18, 8))
												ans = 4												 # approximately 1 were 4 out of 1 samples at leaf node
							else:
								pixels_high.append((8, 23))
								ans = 0								 # approximately 9 were 0 out of 9 samples at leaf node
						else:
							pixels_high.append((22, 12))
							if features[11][4] <= 129.5:
								pixels_low.append((11, 4))
								if features[13][15] <= 74.5:
									pixels_low.append((13, 15))
									if features[16][24] <= 213.0:
										pixels_low.append((16, 24))
										if features[22][25] <= 45.0:
											pixels_low.append((22, 25))
											if features[4][14] <= 254.5:
												pixels_low.append((4, 14))
												if features[5][17] <= 254.5:
													pixels_low.append((5, 17))
													ans = 0													 # approximately 150 were 0 out of 150 samples at leaf node
												else:
													pixels_high.append((5, 17))
													if features[19][8] <= 52.5:
														pixels_low.append((19, 8))
														ans = 6														 # approximately 1 were 6 out of 1 samples at leaf node
													else:
														pixels_high.append((19, 8))
														ans = 0														 # approximately 4 were 0 out of 4 samples at leaf node
											else:
												pixels_high.append((4, 14))
												ans = 4												 # approximately 1 were 4 out of 1 samples at leaf node
										else:
											pixels_high.append((22, 25))
											ans = 9											 # approximately 1 were 9 out of 1 samples at leaf node
									else:
										pixels_high.append((16, 24))
										if features[15][6] <= 84.5:
											pixels_low.append((15, 6))
											ans = 7											 # approximately 2 were 7 out of 2 samples at leaf node
										else:
											pixels_high.append((15, 6))
											if features[19][16] <= 226.5:
												pixels_low.append((19, 16))
												ans = 0												 # approximately 2 were 0 out of 2 samples at leaf node
											else:
												pixels_high.append((19, 16))
												ans = 9												 # approximately 1 were 9 out of 1 samples at leaf node
								else:
									pixels_high.append((13, 15))
									if features[9][20] <= 127.0:
										pixels_low.append((9, 20))
										ans = 5										 # approximately 1 were 5 out of 1 samples at leaf node
									else:
										pixels_high.append((9, 20))
										ans = 6										 # approximately 1 were 6 out of 1 samples at leaf node
							else:
								pixels_high.append((11, 4))
								if features[20][19] <= 36.5:
									pixels_low.append((20, 19))
									ans = 9									 # approximately 1 were 9 out of 1 samples at leaf node
								else:
									pixels_high.append((20, 19))
									ans = 6									 # approximately 4 were 6 out of 4 samples at leaf node
				else:
					pixels_high.append((11, 22))
					if features[16][12] <= 119.5:
						pixels_low.append((16, 12))
						if features[16][11] <= 201.5:
							pixels_low.append((16, 11))
							if features[11][25] <= 12.5:
								pixels_low.append((11, 25))
								if features[19][3] <= 3.5:
									pixels_low.append((19, 3))
									if features[3][19] <= 189.5:
										pixels_low.append((3, 19))
										if features[6][25] <= 57.5:
											pixels_low.append((6, 25))
											if features[14][13] <= 253.5:
												pixels_low.append((14, 13))
												if features[12][3] <= 254.5:
													pixels_low.append((12, 3))
													if features[12][17] <= 246.5:
														pixels_low.append((12, 17))
														if features[12][18] <= 251.5:
															pixels_low.append((12, 18))
															if features[16][10] <= 253.5:
																pixels_low.append((16, 10))
																if features[12][3] <= 251.5:
																	pixels_low.append((12, 3))
																	if features[14][17] <= 113.5:
																		pixels_low.append((14, 17))
																		if features[19][13] <= 253.5:
																			pixels_low.append((19, 13))
																			if features[21][4] <= 214.5:
																				pixels_low.append((21, 4))
																				ans = 0																				 # approximately 2386 were 0 out of 2386 samples at leaf node
																			else:
																				pixels_high.append((21, 4))
																				if features[21][17] <= 253.5:
																					pixels_low.append((21, 17))
																					ans = 0																					 # approximately 53 were 0 out of 53 samples at leaf node
																				else:
																					pixels_high.append((21, 17))
																					ans = 6																					 # approximately 1 were 6 out of 1 samples at leaf node
																		else:
																			pixels_high.append((19, 13))
																			if features[16][24] <= 216.0:
																				pixels_low.append((16, 24))
																				if features[15][24] <= 198.5:
																					pixels_low.append((15, 24))
																					ans = 0																					 # approximately 45 were 0 out of 45 samples at leaf node
																				else:
																					pixels_high.append((15, 24))
																					ans = 5																					 # approximately 1 were 5 out of 1 samples at leaf node
																			else:
																				pixels_high.append((16, 24))
																				ans = 9																				 # approximately 1 were 9 out of 1 samples at leaf node
																	else:
																		pixels_high.append((14, 17))
																		if features[14][17] <= 117.0:
																			pixels_low.append((14, 17))
																			ans = 6																			 # approximately 1 were 6 out of 1 samples at leaf node
																		else:
																			pixels_high.append((14, 17))
																			ans = 0																			 # approximately 12 were 0 out of 12 samples at leaf node
																else:
																	pixels_high.append((12, 3))
																	if features[21][13] <= 254.5:
																		pixels_low.append((21, 13))
																		ans = 0																		 # approximately 7 were 0 out of 7 samples at leaf node
																	else:
																		pixels_high.append((21, 13))
																		ans = 6																		 # approximately 1 were 6 out of 1 samples at leaf node
															else:
																pixels_high.append((16, 10))
																if features[16][8] <= 59.0:
																	pixels_low.append((16, 8))
																	if features[19][17] <= 109.0:
																		pixels_low.append((19, 17))
																		ans = 5																		 # approximately 1 were 5 out of 1 samples at leaf node
																	else:
																		pixels_high.append((19, 17))
																		ans = 3																		 # approximately 1 were 3 out of 1 samples at leaf node
																else:
																	pixels_high.append((16, 8))
																	ans = 0																	 # approximately 20 were 0 out of 20 samples at leaf node
														else:
															pixels_high.append((12, 18))
															if features[11][20] <= 31.5:
																pixels_low.append((11, 20))
																ans = 2																 # approximately 2 were 2 out of 2 samples at leaf node
															else:
																pixels_high.append((11, 20))
																ans = 0																 # approximately 13 were 0 out of 13 samples at leaf node
													else:
														pixels_high.append((12, 17))
														if features[17][21] <= 126.0:
															pixels_low.append((17, 21))
															ans = 0															 # approximately 1 were 0 out of 1 samples at leaf node
														else:
															pixels_high.append((17, 21))
															ans = 6															 # approximately 1 were 6 out of 1 samples at leaf node
												else:
													pixels_high.append((12, 3))
													if features[22][17] <= 106.0:
														pixels_low.append((22, 17))
														ans = 3														 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														pixels_high.append((22, 17))
														ans = 0														 # approximately 1 were 0 out of 1 samples at leaf node
											else:
												pixels_high.append((14, 13))
												ans = 2												 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											pixels_high.append((6, 25))
											ans = 7											 # approximately 1 were 7 out of 1 samples at leaf node
									else:
										pixels_high.append((3, 19))
										if features[14][18] <= 81.5:
											pixels_low.append((14, 18))
											ans = 5											 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											pixels_high.append((14, 18))
											ans = 2											 # approximately 1 were 2 out of 1 samples at leaf node
								else:
									pixels_high.append((19, 3))
									if features[21][9] <= 1.5:
										pixels_low.append((21, 9))
										if features[17][17] <= 245.5:
											pixels_low.append((17, 17))
											if features[20][6] <= 111.0:
												pixels_low.append((20, 6))
												ans = 0												 # approximately 6 were 0 out of 6 samples at leaf node
											else:
												pixels_high.append((20, 6))
												if features[16][8] <= 254.5:
													pixels_low.append((16, 8))
													ans = 2													 # approximately 2 were 2 out of 2 samples at leaf node
												else:
													pixels_high.append((16, 8))
													ans = 6													 # approximately 1 were 6 out of 1 samples at leaf node
										else:
											pixels_high.append((17, 17))
											ans = 6											 # approximately 9 were 6 out of 9 samples at leaf node
									else:
										pixels_high.append((21, 9))
										if features[3][18] <= 71.5:
											pixels_low.append((3, 18))
											ans = 0											 # approximately 41 were 0 out of 41 samples at leaf node
										else:
											pixels_high.append((3, 18))
											ans = 3											 # approximately 1 were 3 out of 1 samples at leaf node
							else:
								pixels_high.append((11, 25))
								if features[17][10] <= 42.0:
									pixels_low.append((17, 10))
									ans = 7									 # approximately 2 were 7 out of 2 samples at leaf node
								else:
									pixels_high.append((17, 10))
									if features[17][16] <= 93.5:
										pixels_low.append((17, 16))
										if features[9][9] <= 126.5:
											pixels_low.append((9, 9))
											ans = 5											 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											pixels_high.append((9, 9))
											ans = 0											 # approximately 1 were 0 out of 1 samples at leaf node
									else:
										pixels_high.append((17, 16))
										ans = 9										 # approximately 1 were 9 out of 1 samples at leaf node
						else:
							pixels_high.append((16, 11))
							if features[21][10] <= 55.0:
								pixels_low.append((21, 10))
								if features[14][8] <= 205.0:
									pixels_low.append((14, 8))
									if features[16][9] <= 12.0:
										pixels_low.append((16, 9))
										ans = 5										 # approximately 8 were 5 out of 8 samples at leaf node
									else:
										pixels_high.append((16, 9))
										if features[18][19] <= 43.5:
											pixels_low.append((18, 19))
											if features[11][14] <= 88.0:
												pixels_low.append((11, 14))
												ans = 5												 # approximately 3 were 5 out of 3 samples at leaf node
											else:
												pixels_high.append((11, 14))
												if features[6][22] <= 126.5:
													pixels_low.append((6, 22))
													ans = 8													 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													pixels_high.append((6, 22))
													ans = 0													 # approximately 1 were 0 out of 1 samples at leaf node
										else:
											pixels_high.append((18, 19))
											if features[10][9] <= 61.0:
												pixels_low.append((10, 9))
												ans = 3												 # approximately 7 were 3 out of 7 samples at leaf node
											else:
												pixels_high.append((10, 9))
												ans = 6												 # approximately 1 were 6 out of 1 samples at leaf node
								else:
									pixels_high.append((14, 8))
									if features[8][12] <= 85.0:
										pixels_low.append((8, 12))
										if features[21][12] <= 125.5:
											pixels_low.append((21, 12))
											if features[9][7] <= 0.5:
												pixels_low.append((9, 7))
												if features[7][11] <= 80.0:
													pixels_low.append((7, 11))
													ans = 8													 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													pixels_high.append((7, 11))
													ans = 3													 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												pixels_high.append((9, 7))
												ans = 2												 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											pixels_high.append((21, 12))
											ans = 6											 # approximately 2 were 6 out of 2 samples at leaf node
									else:
										pixels_high.append((8, 12))
										ans = 0										 # approximately 8 were 0 out of 8 samples at leaf node
							else:
								pixels_high.append((21, 10))
								if features[13][18] <= 252.0:
									pixels_low.append((13, 18))
									ans = 0									 # approximately 51 were 0 out of 51 samples at leaf node
								else:
									pixels_high.append((13, 18))
									ans = 5									 # approximately 1 were 5 out of 1 samples at leaf node
					else:
						pixels_high.append((16, 12))
						if features[15][9] <= 217.5:
							pixels_low.append((15, 9))
							if features[8][18] <= 241.0:
								pixels_low.append((8, 18))
								if features[19][9] <= 6.0:
									pixels_low.append((19, 9))
									if features[20][13] <= 18.0:
										pixels_low.append((20, 13))
										if features[9][12] <= 92.5:
											pixels_low.append((9, 12))
											ans = 8											 # approximately 2 were 8 out of 2 samples at leaf node
										else:
											pixels_high.append((9, 12))
											ans = 6											 # approximately 1 were 6 out of 1 samples at leaf node
									else:
										pixels_high.append((20, 13))
										if features[18][13] <= 20.5:
											pixels_low.append((18, 13))
											if features[7][11] <= 126.5:
												pixels_low.append((7, 11))
												ans = 3												 # approximately 3 were 3 out of 3 samples at leaf node
											else:
												pixels_high.append((7, 11))
												if features[22][21] <= 114.0:
													pixels_low.append((22, 21))
													ans = 0													 # approximately 1 were 0 out of 1 samples at leaf node
												else:
													pixels_high.append((22, 21))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											pixels_high.append((18, 13))
											if features[12][10] <= 252.5:
												pixels_low.append((12, 10))
												ans = 5												 # approximately 20 were 5 out of 20 samples at leaf node
											else:
												pixels_high.append((12, 10))
												ans = 3												 # approximately 1 were 3 out of 1 samples at leaf node
								else:
									pixels_high.append((19, 9))
									if features[13][9] <= 5.5:
										pixels_low.append((13, 9))
										if features[15][19] <= 2.0:
											pixels_low.append((15, 19))
											if features[9][11] <= 22.5:
												pixels_low.append((9, 11))
												ans = 2												 # approximately 2 were 2 out of 2 samples at leaf node
											else:
												pixels_high.append((9, 11))
												ans = 8												 # approximately 5 were 8 out of 5 samples at leaf node
										else:
											pixels_high.append((15, 19))
											ans = 3											 # approximately 7 were 3 out of 7 samples at leaf node
									else:
										pixels_high.append((13, 9))
										ans = 0										 # approximately 7 were 0 out of 7 samples at leaf node
							else:
								pixels_high.append((8, 18))
								if features[18][8] <= 71.0:
									pixels_low.append((18, 8))
									if features[8][15] <= 108.5:
										pixels_low.append((8, 15))
										if features[6][16] <= 42.5:
											pixels_low.append((6, 16))
											ans = 8											 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											pixels_high.append((6, 16))
											ans = 5											 # approximately 1 were 5 out of 1 samples at leaf node
									else:
										pixels_high.append((8, 15))
										ans = 6										 # approximately 16 were 6 out of 16 samples at leaf node
								else:
									pixels_high.append((18, 8))
									if features[18][8] <= 252.5:
										pixels_low.append((18, 8))
										if features[9][8] <= 242.0:
											pixels_low.append((9, 8))
											ans = 0											 # approximately 2 were 0 out of 2 samples at leaf node
										else:
											pixels_high.append((9, 8))
											ans = 8											 # approximately 1 were 8 out of 1 samples at leaf node
									else:
										pixels_high.append((18, 8))
										ans = 2										 # approximately 3 were 2 out of 3 samples at leaf node
						else:
							pixels_high.append((15, 9))
							if features[8][13] <= 88.5:
								pixels_low.append((8, 13))
								if features[21][13] <= 197.0:
									pixels_low.append((21, 13))
									if features[6][16] <= 81.5:
										pixels_low.append((6, 16))
										ans = 3										 # approximately 2 were 3 out of 2 samples at leaf node
									else:
										pixels_high.append((6, 16))
										if features[5][15] <= 98.5:
											pixels_low.append((5, 15))
											ans = 2											 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											pixels_high.append((5, 15))
											ans = 5											 # approximately 2 were 5 out of 2 samples at leaf node
								else:
									pixels_high.append((21, 13))
									ans = 0									 # approximately 4 were 0 out of 4 samples at leaf node
							else:
								pixels_high.append((8, 13))
								ans = 0								 # approximately 38 were 0 out of 38 samples at leaf node
			else:
				pixels_high.append((13, 17))
				if features[8][12] <= 2.0:
					pixels_low.append((8, 12))
					if features[16][18] <= 169.0:
						pixels_low.append((16, 18))
						if features[25][7] <= 30.5:
							pixels_low.append((25, 7))
							if features[5][12] <= 14.5:
								pixels_low.append((5, 12))
								if features[8][13] <= 2.5:
									pixels_low.append((8, 13))
									if features[20][16] <= 44.5:
										pixels_low.append((20, 16))
										if features[12][19] <= 52.0:
											pixels_low.append((12, 19))
											ans = 3											 # approximately 2 were 3 out of 2 samples at leaf node
										else:
											pixels_high.append((12, 19))
											if features[18][19] <= 34.0:
												pixels_low.append((18, 19))
												if features[6][21] <= 97.5:
													pixels_low.append((6, 21))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													pixels_high.append((6, 21))
													ans = 8													 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												pixels_high.append((18, 19))
												ans = 6												 # approximately 2 were 6 out of 2 samples at leaf node
									else:
										pixels_high.append((20, 16))
										ans = 2										 # approximately 3 were 2 out of 3 samples at leaf node
								else:
									pixels_high.append((8, 13))
									ans = 0									 # approximately 4 were 0 out of 4 samples at leaf node
							else:
								pixels_high.append((5, 12))
								if features[14][8] <= 10.5:
									pixels_low.append((14, 8))
									if features[22][12] <= 253.5:
										pixels_low.append((22, 12))
										ans = 4										 # approximately 3 were 4 out of 3 samples at leaf node
									else:
										pixels_high.append((22, 12))
										ans = 0										 # approximately 1 were 0 out of 1 samples at leaf node
								else:
									pixels_high.append((14, 8))
									ans = 9									 # approximately 8 were 9 out of 8 samples at leaf node
						else:
							pixels_high.append((25, 7))
							ans = 5							 # approximately 6 were 5 out of 6 samples at leaf node
					else:
						pixels_high.append((16, 18))
						if features[7][12] <= 12.5:
							pixels_low.append((7, 12))
							if features[23][5] <= 147.5:
								pixels_low.append((23, 5))
								if features[11][24] <= 190.0:
									pixels_low.append((11, 24))
									if features[16][11] <= 253.5:
										pixels_low.append((16, 11))
										ans = 2										 # approximately 56 were 2 out of 56 samples at leaf node
									else:
										pixels_high.append((16, 11))
										ans = 3										 # approximately 1 were 3 out of 1 samples at leaf node
								else:
									pixels_high.append((11, 24))
									ans = 3									 # approximately 1 were 3 out of 1 samples at leaf node
							else:
								pixels_high.append((23, 5))
								ans = 6								 # approximately 2 were 6 out of 2 samples at leaf node
						else:
							pixels_high.append((7, 12))
							if features[21][15] <= 251.5:
								pixels_low.append((21, 15))
								ans = 9								 # approximately 2 were 9 out of 2 samples at leaf node
							else:
								pixels_high.append((21, 15))
								ans = 4								 # approximately 2 were 4 out of 2 samples at leaf node
				else:
					pixels_high.append((8, 12))
					if features[23][13] <= 60.0:
						pixels_low.append((23, 13))
						if features[19][14] <= 44.5:
							pixels_low.append((19, 14))
							if features[17][5] <= 127.5:
								pixels_low.append((17, 5))
								if features[22][15] <= 20.0:
									pixels_low.append((22, 15))
									if features[6][17] <= 23.5:
										pixels_low.append((6, 17))
										ans = 5										 # approximately 23 were 5 out of 23 samples at leaf node
									else:
										pixels_high.append((6, 17))
										if features[16][22] <= 64.0:
											pixels_low.append((16, 22))
											ans = 9											 # approximately 2 were 9 out of 2 samples at leaf node
										else:
											pixels_high.append((16, 22))
											ans = 5											 # approximately 1 were 5 out of 1 samples at leaf node
								else:
									pixels_high.append((22, 15))
									if features[21][16] <= 89.5:
										pixels_low.append((21, 16))
										ans = 9										 # approximately 1 were 9 out of 1 samples at leaf node
									else:
										pixels_high.append((21, 16))
										ans = 6										 # approximately 4 were 6 out of 4 samples at leaf node
							else:
								pixels_high.append((17, 5))
								if features[13][15] <= 47.5:
									pixels_low.append((13, 15))
									ans = 6									 # approximately 7 were 6 out of 7 samples at leaf node
								else:
									pixels_high.append((13, 15))
									if features[8][16] <= 103.0:
										pixels_low.append((8, 16))
										ans = 2										 # approximately 1 were 2 out of 1 samples at leaf node
									else:
										pixels_high.append((8, 16))
										ans = 8										 # approximately 3 were 8 out of 3 samples at leaf node
						else:
							pixels_high.append((19, 14))
							if features[13][7] <= 193.0:
								pixels_low.append((13, 7))
								if features[5][12] <= 221.5:
									pixels_low.append((5, 12))
									ans = 4									 # approximately 23 were 4 out of 23 samples at leaf node
								else:
									pixels_high.append((5, 12))
									ans = 9									 # approximately 1 were 9 out of 1 samples at leaf node
							else:
								pixels_high.append((13, 7))
								if features[12][10] <= 24.5:
									pixels_low.append((12, 10))
									ans = 9									 # approximately 8 were 9 out of 8 samples at leaf node
								else:
									pixels_high.append((12, 10))
									if features[16][6] <= 129.5:
										pixels_low.append((16, 6))
										if features[13][11] <= 53.5:
											pixels_low.append((13, 11))
											ans = 4											 # approximately 1 were 4 out of 1 samples at leaf node
										else:
											pixels_high.append((13, 11))
											ans = 0											 # approximately 2 were 0 out of 2 samples at leaf node
									else:
										pixels_high.append((16, 6))
										ans = 2										 # approximately 2 were 2 out of 2 samples at leaf node
					else:
						pixels_high.append((23, 13))
						if features[14][12] <= 168.0:
							pixels_low.append((14, 12))
							if features[13][3] <= 14.5:
								pixels_low.append((13, 3))
								if features[15][24] <= 217.0:
									pixels_low.append((15, 24))
									ans = 0									 # approximately 26 were 0 out of 26 samples at leaf node
								else:
									pixels_high.append((15, 24))
									ans = 9									 # approximately 1 were 9 out of 1 samples at leaf node
							else:
								pixels_high.append((13, 3))
								if features[11][18] <= 205.5:
									pixels_low.append((11, 18))
									ans = 2									 # approximately 1 were 2 out of 1 samples at leaf node
								else:
									pixels_high.append((11, 18))
									if features[24][18] <= 34.5:
										pixels_low.append((24, 18))
										ans = 4										 # approximately 1 were 4 out of 1 samples at leaf node
									else:
										pixels_high.append((24, 18))
										ans = 6										 # approximately 1 were 6 out of 1 samples at leaf node
						else:
							pixels_high.append((14, 12))
							ans = 6							 # approximately 9 were 6 out of 9 samples at leaf node
	else:
		pixels_high.append((14, 15))
		if features[11][13] <= 0.5:
			pixels_low.append((11, 13))
			if features[18][19] <= 0.5:
				pixels_low.append((18, 19))
				if features[10][7] <= 0.5:
					pixels_low.append((10, 7))
					if features[9][16] <= 7.5:
						pixels_low.append((9, 16))
						if features[11][10] <= 41.5:
							pixels_low.append((11, 10))
							if features[19][21] <= 52.5:
								pixels_low.append((19, 21))
								if features[6][18] <= 1.0:
									pixels_low.append((6, 18))
									if features[20][10] <= 130.0:
										pixels_low.append((20, 10))
										if features[17][17] <= 2.0:
											pixels_low.append((17, 17))
											if features[10][5] <= 89.0:
												pixels_low.append((10, 5))
												if features[10][25] <= 105.5:
													pixels_low.append((10, 25))
													if features[22][8] <= 123.5:
														pixels_low.append((22, 8))
														if features[14][13] <= 141.5:
															pixels_low.append((14, 13))
															if features[19][10] <= 55.0:
																pixels_low.append((19, 10))
																if features[12][15] <= 125.5:
																	pixels_low.append((12, 15))
																	if features[7][21] <= 18.5:
																		pixels_low.append((7, 21))
																		if features[10][10] <= 12.5:
																			pixels_low.append((10, 10))
																			if features[12][5] <= 208.5:
																				pixels_low.append((12, 5))
																				ans = 1																				 # approximately 55 were 1 out of 55 samples at leaf node
																			else:
																				pixels_high.append((12, 5))
																				ans = 7																				 # approximately 1 were 7 out of 1 samples at leaf node
																		else:
																			pixels_high.append((10, 10))
																			if features[11][18] <= 1.5:
																				pixels_low.append((11, 18))
																				ans = 7																				 # approximately 1 were 7 out of 1 samples at leaf node
																			else:
																				pixels_high.append((11, 18))
																				ans = 4																				 # approximately 1 were 4 out of 1 samples at leaf node
																	else:
																		pixels_high.append((7, 21))
																		ans = 5																		 # approximately 2 were 5 out of 2 samples at leaf node
																else:
																	pixels_high.append((12, 15))
																	if features[11][19] <= 131.5:
																		pixels_low.append((11, 19))
																		if features[17][10] <= 85.0:
																			pixels_low.append((17, 10))
																			if features[12][5] <= 74.0:
																				pixels_low.append((12, 5))
																				if features[14][18] <= 141.0:
																					pixels_low.append((14, 18))
																					ans = 8																					 # approximately 1 were 8 out of 1 samples at leaf node
																				else:
																					pixels_high.append((14, 18))
																					ans = 5																					 # approximately 1 were 5 out of 1 samples at leaf node
																			else:
																				pixels_high.append((12, 5))
																				ans = 3																				 # approximately 1 were 3 out of 1 samples at leaf node
																		else:
																			pixels_high.append((17, 10))
																			ans = 4																			 # approximately 1 were 4 out of 1 samples at leaf node
																	else:
																		pixels_high.append((11, 19))
																		ans = 6																		 # approximately 2 were 6 out of 2 samples at leaf node
															else:
																pixels_high.append((19, 10))
																if features[14][16] <= 142.5:
																	pixels_low.append((14, 16))
																	if features[13][6] <= 15.5:
																		pixels_low.append((13, 6))
																		if features[15][13] <= 235.5:
																			pixels_low.append((15, 13))
																			ans = 8																			 # approximately 1 were 8 out of 1 samples at leaf node
																		else:
																			pixels_high.append((15, 13))
																			ans = 1																			 # approximately 1 were 1 out of 1 samples at leaf node
																	else:
																		pixels_high.append((13, 6))
																		ans = 2																		 # approximately 2 were 2 out of 2 samples at leaf node
																else:
																	pixels_high.append((14, 16))
																	ans = 7																	 # approximately 4 were 7 out of 4 samples at leaf node
														else:
															pixels_high.append((14, 13))
															if features[20][9] <= 63.5:
																pixels_low.append((20, 9))
																if features[18][12] <= 220.5:
																	pixels_low.append((18, 12))
																	if features[8][18] <= 40.0:
																		pixels_low.append((8, 18))
																		if features[10][6] <= 151.0:
																			pixels_low.append((10, 6))
																			if features[5][20] <= 103.0:
																				pixels_low.append((5, 20))
																				if features[17][18] <= 43.5:
																					pixels_low.append((17, 18))
																					if features[18][13] <= 5.0:
																						pixels_low.append((18, 13))
																						if features[20][3] <= 231.0:
																							pixels_low.append((20, 3))
																							if features[15][3] <= 202.0:
																								pixels_low.append((15, 3))
																								if features[17][15] <= 3.0:
																									pixels_low.append((17, 15))
																									if features[12][11] <= 254.0:
																										pixels_low.append((12, 11))
																										if features[12][12] <= 225.5:
																											pixels_low.append((12, 12))
																											if features[9][24] <= 254.5:
																												pixels_low.append((9, 24))
																												if features[11][4] <= 218.5:
																													pixels_low.append((11, 4))
																													if features[19][8] <= 253.5:
																														pixels_low.append((19, 8))
																														if features[16][17] <= 140.5:
																															pixels_low.append((16, 17))
																															if features[17][9] <= 254.5:
																																pixels_low.append((17, 9))
																																ans = 1																																 # approximately 3236 were 1 out of 3236 samples at leaf node
																															else:
																																pixels_high.append((17, 9))
																																if features[13][8] <= 90.5:
																																	pixels_low.append((13, 8))
																																	ans = 1																																	 # approximately 70 were 1 out of 70 samples at leaf node
																																else:
																																	pixels_high.append((13, 8))
																																	ans = 8																																	 # approximately 1 were 8 out of 1 samples at leaf node
																														else:
																															pixels_high.append((16, 17))
																															if features[11][17] <= 44.5:
																																pixels_low.append((11, 17))
																																ans = 1																																 # approximately 118 were 1 out of 118 samples at leaf node
																															else:
																																pixels_high.append((11, 17))
																																if features[13][11] <= 228.0:
																																	pixels_low.append((13, 11))
																																	ans = 1																																	 # approximately 1 were 1 out of 1 samples at leaf node
																																else:
																																	pixels_high.append((13, 11))
																																	ans = 8																																	 # approximately 2 were 8 out of 2 samples at leaf node
																													else:
																														pixels_high.append((19, 8))
																														if features[16][19] <= 25.5:
																															pixels_low.append((16, 19))
																															ans = 1																															 # approximately 26 were 1 out of 26 samples at leaf node
																														else:
																															pixels_high.append((16, 19))
																															ans = 8																															 # approximately 2 were 8 out of 2 samples at leaf node
																												else:
																													pixels_high.append((11, 4))
																													if features[14][19] <= 58.0:
																														pixels_low.append((14, 19))
																														ans = 2																														 # approximately 1 were 2 out of 1 samples at leaf node
																													else:
																														pixels_high.append((14, 19))
																														ans = 1																														 # approximately 6 were 1 out of 6 samples at leaf node
																											else:
																												pixels_high.append((9, 24))
																												if features[11][17] <= 64.0:
																													pixels_low.append((11, 17))
																													ans = 3																													 # approximately 1 were 3 out of 1 samples at leaf node
																												else:
																													pixels_high.append((11, 17))
																													ans = 1																													 # approximately 5 were 1 out of 5 samples at leaf node
																										else:
																											pixels_high.append((12, 12))
																											if features[17][4] <= 73.5:
																												pixels_low.append((17, 4))
																												ans = 1																												 # approximately 18 were 1 out of 18 samples at leaf node
																											else:
																												pixels_high.append((17, 4))
																												ans = 8																												 # approximately 2 were 8 out of 2 samples at leaf node
																									else:
																										pixels_high.append((12, 11))
																										if features[13][24] <= 223.0:
																											pixels_low.append((13, 24))
																											ans = 1																											 # approximately 3 were 1 out of 3 samples at leaf node
																										else:
																											pixels_high.append((13, 24))
																											ans = 8																											 # approximately 1 were 8 out of 1 samples at leaf node
																								else:
																									pixels_high.append((17, 15))
																									if features[10][22] <= 252.5:
																										pixels_low.append((10, 22))
																										ans = 1																										 # approximately 3 were 1 out of 3 samples at leaf node
																									else:
																										pixels_high.append((10, 22))
																										ans = 3																										 # approximately 1 were 3 out of 1 samples at leaf node
																							else:
																								pixels_high.append((15, 3))
																								if features[15][11] <= 176.0:
																									pixels_low.append((15, 11))
																									ans = 6																									 # approximately 1 were 6 out of 1 samples at leaf node
																								else:
																									pixels_high.append((15, 11))
																									ans = 1																									 # approximately 3 were 1 out of 3 samples at leaf node
																						else:
																							pixels_high.append((20, 3))
																							if features[12][15] <= 200.0:
																								pixels_low.append((12, 15))
																								ans = 1																								 # approximately 1 were 1 out of 1 samples at leaf node
																							else:
																								pixels_high.append((12, 15))
																								ans = 6																								 # approximately 1 were 6 out of 1 samples at leaf node
																					else:
																						pixels_high.append((18, 13))
																						if features[17][7] <= 3.0:
																							pixels_low.append((17, 7))
																							ans = 8																							 # approximately 2 were 8 out of 2 samples at leaf node
																						else:
																							pixels_high.append((17, 7))
																							ans = 1																							 # approximately 5 were 1 out of 5 samples at leaf node
																				else:
																					pixels_high.append((17, 18))
																					if features[17][5] <= 88.5:
																						pixels_low.append((17, 5))
																						ans = 1																						 # approximately 4 were 1 out of 4 samples at leaf node
																					else:
																						pixels_high.append((17, 5))
																						ans = 8																						 # approximately 2 were 8 out of 2 samples at leaf node
																			else:
																				pixels_high.append((5, 20))
																				ans = 5																				 # approximately 1 were 5 out of 1 samples at leaf node
																		else:
																			pixels_high.append((10, 6))
																			ans = 7																			 # approximately 1 were 7 out of 1 samples at leaf node
																	else:
																		pixels_high.append((8, 18))
																		if features[15][17] <= 55.5:
																			pixels_low.append((15, 17))
																			ans = 1																			 # approximately 12 were 1 out of 12 samples at leaf node
																		else:
																			pixels_high.append((15, 17))
																			if features[15][14] <= 177.5:
																				pixels_low.append((15, 14))
																				ans = 5																				 # approximately 2 were 5 out of 2 samples at leaf node
																			else:
																				pixels_high.append((15, 14))
																				ans = 8																				 # approximately 3 were 8 out of 3 samples at leaf node
																else:
																	pixels_high.append((18, 12))
																	if features[12][24] <= 183.0:
																		pixels_low.append((12, 24))
																		ans = 8																		 # approximately 2 were 8 out of 2 samples at leaf node
																	else:
																		pixels_high.append((12, 24))
																		ans = 1																		 # approximately 1 were 1 out of 1 samples at leaf node
															else:
																pixels_high.append((20, 9))
																if features[14][7] <= 11.0:
																	pixels_low.append((14, 7))
																	ans = 1																	 # approximately 49 were 1 out of 49 samples at leaf node
																else:
																	pixels_high.append((14, 7))
																	if features[7][24] <= 70.5:
																		pixels_low.append((7, 24))
																		ans = 8																		 # approximately 9 were 8 out of 9 samples at leaf node
																	else:
																		pixels_high.append((7, 24))
																		if features[15][22] <= 127.0:
																			pixels_low.append((15, 22))
																			ans = 9																			 # approximately 1 were 9 out of 1 samples at leaf node
																		else:
																			pixels_high.append((15, 22))
																			ans = 3																			 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														pixels_high.append((22, 8))
														if features[19][11] <= 26.5:
															pixels_low.append((19, 11))
															ans = 5															 # approximately 4 were 5 out of 4 samples at leaf node
														else:
															pixels_high.append((19, 11))
															if features[10][22] <= 89.5:
																pixels_low.append((10, 22))
																ans = 1																 # approximately 1 were 1 out of 1 samples at leaf node
															else:
																pixels_high.append((10, 22))
																ans = 8																 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													pixels_high.append((10, 25))
													if features[14][16] <= 234.0:
														pixels_low.append((14, 16))
														ans = 9														 # approximately 2 were 9 out of 2 samples at leaf node
													else:
														pixels_high.append((14, 16))
														ans = 7														 # approximately 4 were 7 out of 4 samples at leaf node
											else:
												pixels_high.append((10, 5))
												if features[13][12] <= 161.5:
													pixels_low.append((13, 12))
													if features[17][22] <= 1.0:
														pixels_low.append((17, 22))
														if features[15][14] <= 243.5:
															pixels_low.append((15, 14))
															ans = 3															 # approximately 3 were 3 out of 3 samples at leaf node
														else:
															pixels_high.append((15, 14))
															ans = 7															 # approximately 3 were 7 out of 3 samples at leaf node
													else:
														pixels_high.append((17, 22))
														ans = 2														 # approximately 4 were 2 out of 4 samples at leaf node
												else:
													pixels_high.append((13, 12))
													ans = 1													 # approximately 3 were 1 out of 3 samples at leaf node
										else:
											pixels_high.append((17, 17))
											if features[14][17] <= 144.5:
												pixels_low.append((14, 17))
												if features[12][16] <= 43.5:
													pixels_low.append((12, 16))
													if features[16][11] <= 27.0:
														pixels_low.append((16, 11))
														if features[16][19] <= 235.5:
															pixels_low.append((16, 19))
															ans = 5															 # approximately 1 were 5 out of 1 samples at leaf node
														else:
															pixels_high.append((16, 19))
															ans = 1															 # approximately 2 were 1 out of 2 samples at leaf node
													else:
														pixels_high.append((16, 11))
														ans = 3														 # approximately 14 were 3 out of 14 samples at leaf node
												else:
													pixels_high.append((12, 16))
													if features[14][19] <= 72.0:
														pixels_low.append((14, 19))
														ans = 8														 # approximately 7 were 8 out of 7 samples at leaf node
													else:
														pixels_high.append((14, 19))
														if features[12][21] <= 178.0:
															pixels_low.append((12, 21))
															if features[9][20] <= 217.5:
																pixels_low.append((9, 20))
																ans = 2																 # approximately 2 were 2 out of 2 samples at leaf node
															else:
																pixels_high.append((9, 20))
																ans = 5																 # approximately 1 were 5 out of 1 samples at leaf node
														else:
															pixels_high.append((12, 21))
															ans = 6															 # approximately 3 were 6 out of 3 samples at leaf node
											else:
												pixels_high.append((14, 17))
												if features[14][13] <= 201.0:
													pixels_low.append((14, 13))
													if features[9][17] <= 45.0:
														pixels_low.append((9, 17))
														if features[12][24] <= 65.0:
															pixels_low.append((12, 24))
															if features[13][18] <= 98.0:
																pixels_low.append((13, 18))
																ans = 4																 # approximately 1 were 4 out of 1 samples at leaf node
															else:
																pixels_high.append((13, 18))
																if features[11][18] <= 15.0:
																	pixels_low.append((11, 18))
																	if features[12][20] <= 169.0:
																		pixels_low.append((12, 20))
																		ans = 1																		 # approximately 1 were 1 out of 1 samples at leaf node
																	else:
																		pixels_high.append((12, 20))
																		ans = 5																		 # approximately 1 were 5 out of 1 samples at leaf node
																else:
																	pixels_high.append((11, 18))
																	if features[12][17] <= 28.5:
																		pixels_low.append((12, 17))
																		ans = 8																		 # approximately 1 were 8 out of 1 samples at leaf node
																	else:
																		pixels_high.append((12, 17))
																		ans = 6																		 # approximately 1 were 6 out of 1 samples at leaf node
														else:
															pixels_high.append((12, 24))
															ans = 7															 # approximately 2 were 7 out of 2 samples at leaf node
													else:
														pixels_high.append((9, 17))
														ans = 2														 # approximately 2 were 2 out of 2 samples at leaf node
												else:
													pixels_high.append((14, 13))
													if features[11][17] <= 246.0:
														pixels_low.append((11, 17))
														ans = 1														 # approximately 47 were 1 out of 47 samples at leaf node
													else:
														pixels_high.append((11, 17))
														ans = 6														 # approximately 1 were 6 out of 1 samples at leaf node
									else:
										pixels_high.append((20, 10))
										if features[10][23] <= 17.5:
											pixels_low.append((10, 23))
											if features[15][19] <= 126.5:
												pixels_low.append((15, 19))
												if features[18][5] <= 253.5:
													pixels_low.append((18, 5))
													ans = 1													 # approximately 1 were 1 out of 1 samples at leaf node
												else:
													pixels_high.append((18, 5))
													ans = 2													 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												pixels_high.append((15, 19))
												ans = 5												 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											pixels_high.append((10, 23))
											ans = 8											 # approximately 14 were 8 out of 14 samples at leaf node
								else:
									pixels_high.append((6, 18))
									if features[8][22] <= 232.0:
										pixels_low.append((8, 22))
										if features[11][15] <= 169.5:
											pixels_low.append((11, 15))
											if features[7][19] <= 1.5:
												pixels_low.append((7, 19))
												ans = 1												 # approximately 1 were 1 out of 1 samples at leaf node
											else:
												pixels_high.append((7, 19))
												ans = 5												 # approximately 21 were 5 out of 21 samples at leaf node
										else:
											pixels_high.append((11, 15))
											ans = 2											 # approximately 2 were 2 out of 2 samples at leaf node
									else:
										pixels_high.append((8, 22))
										if features[13][16] <= 252.5:
											pixels_low.append((13, 16))
											ans = 3											 # approximately 3 were 3 out of 3 samples at leaf node
										else:
											pixels_high.append((13, 16))
											if features[12][9] <= 59.0:
												pixels_low.append((12, 9))
												ans = 2												 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												pixels_high.append((12, 9))
												ans = 7												 # approximately 1 were 7 out of 1 samples at leaf node
							else:
								pixels_high.append((19, 21))
								if features[13][8] <= 101.0:
									pixels_low.append((13, 8))
									if features[16][15] <= 197.5:
										pixels_low.append((16, 15))
										ans = 2										 # approximately 42 were 2 out of 42 samples at leaf node
									else:
										pixels_high.append((16, 15))
										ans = 3										 # approximately 1 were 3 out of 1 samples at leaf node
								else:
									pixels_high.append((13, 8))
									if features[18][9] <= 127.0:
										pixels_low.append((18, 9))
										ans = 1										 # approximately 8 were 1 out of 8 samples at leaf node
									else:
										pixels_high.append((18, 9))
										ans = 9										 # approximately 1 were 9 out of 1 samples at leaf node
						else:
							pixels_high.append((11, 10))
							if features[8][10] <= 24.5:
								pixels_low.append((8, 10))
								if features[18][7] <= 11.0:
									pixels_low.append((18, 7))
									if features[14][17] <= 170.0:
										pixels_low.append((14, 17))
										if features[15][14] <= 134.5:
											pixels_low.append((15, 14))
											ans = 5											 # approximately 5 were 5 out of 5 samples at leaf node
										else:
											pixels_high.append((15, 14))
											if features[10][22] <= 45.5:
												pixels_low.append((10, 22))
												ans = 9												 # approximately 3 were 9 out of 3 samples at leaf node
											else:
												pixels_high.append((10, 22))
												if features[18][10] <= 131.0:
													pixels_low.append((18, 10))
													ans = 8													 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													pixels_high.append((18, 10))
													ans = 4													 # approximately 2 were 4 out of 2 samples at leaf node
									else:
										pixels_high.append((14, 17))
										if features[17][8] <= 157.5:
											pixels_low.append((17, 8))
											if features[7][19] <= 99.0:
												pixels_low.append((7, 19))
												ans = 1												 # approximately 40 were 1 out of 40 samples at leaf node
											else:
												pixels_high.append((7, 19))
												if features[12][7] <= 7.0:
													pixels_low.append((12, 7))
													ans = 6													 # approximately 1 were 6 out of 1 samples at leaf node
												else:
													pixels_high.append((12, 7))
													ans = 2													 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											pixels_high.append((17, 8))
											if features[17][8] <= 213.0:
												pixels_low.append((17, 8))
												ans = 7												 # approximately 3 were 7 out of 3 samples at leaf node
											else:
												pixels_high.append((17, 8))
												if features[9][19] <= 30.0:
													pixels_low.append((9, 19))
													ans = 9													 # approximately 2 were 9 out of 2 samples at leaf node
												else:
													pixels_high.append((9, 19))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
								else:
									pixels_high.append((18, 7))
									if features[14][6] <= 13.5:
										pixels_low.append((14, 6))
										if features[10][25] <= 10.0:
											pixels_low.append((10, 25))
											if features[12][17] <= 249.5:
												pixels_low.append((12, 17))
												if features[11][24] <= 94.0:
													pixels_low.append((11, 24))
													if features[13][9] <= 238.5:
														pixels_low.append((13, 9))
														if features[20][3] <= 16.0:
															pixels_low.append((20, 3))
															ans = 9															 # approximately 3 were 9 out of 3 samples at leaf node
														else:
															pixels_high.append((20, 3))
															ans = 4															 # approximately 1 were 4 out of 1 samples at leaf node
													else:
														pixels_high.append((13, 9))
														ans = 5														 # approximately 3 were 5 out of 3 samples at leaf node
												else:
													pixels_high.append((11, 24))
													ans = 8													 # approximately 3 were 8 out of 3 samples at leaf node
											else:
												pixels_high.append((12, 17))
												ans = 1												 # approximately 4 were 1 out of 4 samples at leaf node
										else:
											pixels_high.append((10, 25))
											if features[14][17] <= 147.0:
												pixels_low.append((14, 17))
												ans = 3												 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												pixels_high.append((14, 17))
												ans = 7												 # approximately 7 were 7 out of 7 samples at leaf node
									else:
										pixels_high.append((14, 6))
										if features[6][19] <= 3.0:
											pixels_low.append((6, 19))
											if features[18][22] <= 126.0:
												pixels_low.append((18, 22))
												if features[9][10] <= 41.0:
													pixels_low.append((9, 10))
													ans = 8													 # approximately 28 were 8 out of 28 samples at leaf node
												else:
													pixels_high.append((9, 10))
													ans = 3													 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												pixels_high.append((18, 22))
												ans = 2												 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											pixels_high.append((6, 19))
											if features[14][14] <= 126.0:
												pixels_low.append((14, 14))
												ans = 2												 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												pixels_high.append((14, 14))
												ans = 5												 # approximately 2 were 5 out of 2 samples at leaf node
							else:
								pixels_high.append((8, 10))
								if features[6][11] <= 136.0:
									pixels_low.append((6, 11))
									if features[16][9] <= 31.5:
										pixels_low.append((16, 9))
										ans = 3										 # approximately 2 were 3 out of 2 samples at leaf node
									else:
										pixels_high.append((16, 9))
										ans = 7										 # approximately 23 were 7 out of 23 samples at leaf node
								else:
									pixels_high.append((6, 11))
									if features[16][22] <= 127.0:
										pixels_low.append((16, 22))
										ans = 2										 # approximately 3 were 2 out of 3 samples at leaf node
									else:
										pixels_high.append((16, 22))
										ans = 5										 # approximately 1 were 5 out of 1 samples at leaf node
					else:
						pixels_high.append((9, 16))
						if features[8][13] <= 4.0:
							pixels_low.append((8, 13))
							if features[13][11] <= 27.0:
								pixels_low.append((13, 11))
								if features[8][23] <= 9.0:
									pixels_low.append((8, 23))
									if features[9][21] <= 25.5:
										pixels_low.append((9, 21))
										if features[7][17] <= 74.5:
											pixels_low.append((7, 17))
											if features[13][14] <= 85.0:
												pixels_low.append((13, 14))
												ans = 7												 # approximately 6 were 7 out of 6 samples at leaf node
											else:
												pixels_high.append((13, 14))
												if features[16][15] <= 61.5:
													pixels_low.append((16, 15))
													ans = 1													 # approximately 3 were 1 out of 3 samples at leaf node
												else:
													pixels_high.append((16, 15))
													if features[14][9] <= 182.5:
														pixels_low.append((14, 9))
														ans = 5														 # approximately 2 were 5 out of 2 samples at leaf node
													else:
														pixels_high.append((14, 9))
														ans = 3														 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											pixels_high.append((7, 17))
											if features[6][14] <= 7.5:
												pixels_low.append((6, 14))
												if features[12][16] <= 57.5:
													pixels_low.append((12, 16))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													pixels_high.append((12, 16))
													ans = 2													 # approximately 9 were 2 out of 9 samples at leaf node
											else:
												pixels_high.append((6, 14))
												if features[12][19] <= 88.5:
													pixels_low.append((12, 19))
													ans = 4													 # approximately 2 were 4 out of 2 samples at leaf node
												else:
													pixels_high.append((12, 19))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
									else:
										pixels_high.append((9, 21))
										if features[18][12] <= 209.0:
											pixels_low.append((18, 12))
											ans = 2											 # approximately 28 were 2 out of 28 samples at leaf node
										else:
											pixels_high.append((18, 12))
											ans = 8											 # approximately 1 were 8 out of 1 samples at leaf node
								else:
									pixels_high.append((8, 23))
									if features[9][21] <= 151.0:
										pixels_low.append((9, 21))
										if features[16][14] <= 109.5:
											pixels_low.append((16, 14))
											if features[6][24] <= 203.5:
												pixels_low.append((6, 24))
												if features[15][21] <= 66.0:
													pixels_low.append((15, 21))
													ans = 7													 # approximately 2 were 7 out of 2 samples at leaf node
												else:
													pixels_high.append((15, 21))
													ans = 2													 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												pixels_high.append((6, 24))
												ans = 3												 # approximately 2 were 3 out of 2 samples at leaf node
										else:
											pixels_high.append((16, 14))
											ans = 8											 # approximately 3 were 8 out of 3 samples at leaf node
									else:
										pixels_high.append((9, 21))
										ans = 1										 # approximately 17 were 1 out of 17 samples at leaf node
							else:
								pixels_high.append((13, 11))
								if features[15][10] <= 215.5:
									pixels_low.append((15, 10))
									if features[10][9] <= 157.5:
										pixels_low.append((10, 9))
										ans = 8										 # approximately 33 were 8 out of 33 samples at leaf node
									else:
										pixels_high.append((10, 9))
										ans = 2										 # approximately 1 were 2 out of 1 samples at leaf node
								else:
									pixels_high.append((15, 10))
									if features[12][21] <= 90.0:
										pixels_low.append((12, 21))
										if features[12][11] <= 123.5:
											pixels_low.append((12, 11))
											ans = 1											 # approximately 7 were 1 out of 7 samples at leaf node
										else:
											pixels_high.append((12, 11))
											if features[13][24] <= 100.0:
												pixels_low.append((13, 24))
												ans = 4												 # approximately 1 were 4 out of 1 samples at leaf node
											else:
												pixels_high.append((13, 24))
												ans = 8												 # approximately 1 were 8 out of 1 samples at leaf node
									else:
										pixels_high.append((12, 21))
										if features[15][5] <= 134.5:
											pixels_low.append((15, 5))
											if features[14][22] <= 47.5:
												pixels_low.append((14, 22))
												ans = 5												 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												pixels_high.append((14, 22))
												if features[21][8] <= 23.0:
													pixels_low.append((21, 8))
													ans = 6													 # approximately 1 were 6 out of 1 samples at leaf node
												else:
													pixels_high.append((21, 8))
													ans = 8													 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											pixels_high.append((15, 5))
											ans = 2											 # approximately 2 were 2 out of 2 samples at leaf node
						else:
							pixels_high.append((8, 13))
							if features[19][16] <= 2.0:
								pixels_low.append((19, 16))
								if features[17][12] <= 30.0:
									pixels_low.append((17, 12))
									ans = 5									 # approximately 15 were 5 out of 15 samples at leaf node
								else:
									pixels_high.append((17, 12))
									if features[14][16] <= 214.5:
										pixels_low.append((14, 16))
										if features[16][20] <= 90.5:
											pixels_low.append((16, 20))
											ans = 9											 # approximately 2 were 9 out of 2 samples at leaf node
										else:
											pixels_high.append((16, 20))
											if features[7][15] <= 46.0:
												pixels_low.append((7, 15))
												ans = 8												 # approximately 2 were 8 out of 2 samples at leaf node
											else:
												pixels_high.append((7, 15))
												if features[5][22] <= 104.5:
													pixels_low.append((5, 22))
													ans = 6													 # approximately 1 were 6 out of 1 samples at leaf node
												else:
													pixels_high.append((5, 22))
													ans = 3													 # approximately 1 were 3 out of 1 samples at leaf node
									else:
										pixels_high.append((14, 16))
										ans = 4										 # approximately 4 were 4 out of 4 samples at leaf node
							else:
								pixels_high.append((19, 16))
								if features[20][8] <= 230.5:
									pixels_low.append((20, 8))
									if features[15][16] <= 45.5:
										pixels_low.append((15, 16))
										if features[9][12] <= 121.0:
											pixels_low.append((9, 12))
											ans = 2											 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											pixels_high.append((9, 12))
											ans = 6											 # approximately 1 were 6 out of 1 samples at leaf node
									else:
										pixels_high.append((15, 16))
										ans = 4										 # approximately 23 were 4 out of 23 samples at leaf node
								else:
									pixels_high.append((20, 8))
									ans = 9									 # approximately 2 were 9 out of 2 samples at leaf node
				else:
					pixels_high.append((10, 7))
					if features[10][19] <= 3.0:
						pixels_low.append((10, 19))
						if features[12][10] <= 111.5:
							pixels_low.append((12, 10))
							if features[13][13] <= 20.5:
								pixels_low.append((13, 13))
								if features[18][22] <= 3.5:
									pixels_low.append((18, 22))
									if features[8][15] <= 71.5:
										pixels_low.append((8, 15))
										if features[8][22] <= 7.5:
											pixels_low.append((8, 22))
											if features[10][14] <= 49.5:
												pixels_low.append((10, 14))
												if features[16][12] <= 87.0:
													pixels_low.append((16, 12))
													if features[13][18] <= 211.5:
														pixels_low.append((13, 18))
														ans = 1														 # approximately 2 were 1 out of 2 samples at leaf node
													else:
														pixels_high.append((13, 18))
														ans = 7														 # approximately 1 were 7 out of 1 samples at leaf node
												else:
													pixels_high.append((16, 12))
													if features[16][18] <= 248.0:
														pixels_low.append((16, 18))
														ans = 7														 # approximately 70 were 7 out of 70 samples at leaf node
													else:
														pixels_high.append((16, 18))
														ans = 3														 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												pixels_high.append((10, 14))
												ans = 9												 # approximately 2 were 9 out of 2 samples at leaf node
										else:
											pixels_high.append((8, 22))
											if features[15][15] <= 10.5:
												pixels_low.append((15, 15))
												ans = 3												 # approximately 2 were 3 out of 2 samples at leaf node
											else:
												pixels_high.append((15, 15))
												if features[9][8] <= 116.0:
													pixels_low.append((9, 8))
													ans = 2													 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													pixels_high.append((9, 8))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
									else:
										pixels_high.append((8, 15))
										if features[6][13] <= 31.0:
											pixels_low.append((6, 13))
											if features[10][10] <= 76.0:
												pixels_low.append((10, 10))
												ans = 2												 # approximately 4 were 2 out of 4 samples at leaf node
											else:
												pixels_high.append((10, 10))
												if features[23][9] <= 10.5:
													pixels_low.append((23, 9))
													if features[18][8] <= 62.0:
														pixels_low.append((18, 8))
														ans = 9														 # approximately 1 were 9 out of 1 samples at leaf node
													else:
														pixels_high.append((18, 8))
														ans = 4														 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													pixels_high.append((23, 9))
													ans = 5													 # approximately 2 were 5 out of 2 samples at leaf node
										else:
											pixels_high.append((6, 13))
											ans = 4											 # approximately 3 were 4 out of 3 samples at leaf node
								else:
									pixels_high.append((18, 22))
									if features[13][18] <= 89.0:
										pixels_low.append((13, 18))
										if features[15][23] <= 111.5:
											pixels_low.append((15, 23))
											if features[11][21] <= 33.0:
												pixels_low.append((11, 21))
												if features[9][8] <= 48.5:
													pixels_low.append((9, 8))
													if features[19][24] <= 156.5:
														pixels_low.append((19, 24))
														ans = 8														 # approximately 1 were 8 out of 1 samples at leaf node
													else:
														pixels_high.append((19, 24))
														ans = 4														 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													pixels_high.append((9, 8))
													ans = 9													 # approximately 2 were 9 out of 2 samples at leaf node
											else:
												pixels_high.append((11, 21))
												ans = 1												 # approximately 2 were 1 out of 2 samples at leaf node
										else:
											pixels_high.append((15, 23))
											ans = 5											 # approximately 5 were 5 out of 5 samples at leaf node
									else:
										pixels_high.append((13, 18))
										ans = 2										 # approximately 10 were 2 out of 10 samples at leaf node
							else:
								pixels_high.append((13, 13))
								if features[12][20] <= 144.0:
									pixels_low.append((12, 20))
									if features[14][10] <= 242.0:
										pixels_low.append((14, 10))
										if features[8][15] <= 12.0:
											pixels_low.append((8, 15))
											if features[11][16] <= 253.5:
												pixels_low.append((11, 16))
												ans = 3												 # approximately 33 were 3 out of 33 samples at leaf node
											else:
												pixels_high.append((11, 16))
												if features[15][16] <= 132.0:
													pixels_low.append((15, 16))
													ans = 3													 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													pixels_high.append((15, 16))
													ans = 7													 # approximately 2 were 7 out of 2 samples at leaf node
										else:
											pixels_high.append((8, 15))
											if features[8][11] <= 25.0:
												pixels_low.append((8, 11))
												ans = 2												 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												pixels_high.append((8, 11))
												ans = 9												 # approximately 2 were 9 out of 2 samples at leaf node
									else:
										pixels_high.append((14, 10))
										if features[12][23] <= 35.5:
											pixels_low.append((12, 23))
											if features[15][18] <= 246.5:
												pixels_low.append((15, 18))
												if features[12][13] <= 29.0:
													pixels_low.append((12, 13))
													ans = 0													 # approximately 1 were 0 out of 1 samples at leaf node
												else:
													pixels_high.append((12, 13))
													ans = 4													 # approximately 1 were 4 out of 1 samples at leaf node
											else:
												pixels_high.append((15, 18))
												ans = 7												 # approximately 2 were 7 out of 2 samples at leaf node
										else:
											pixels_high.append((12, 23))
											ans = 1											 # approximately 2 were 1 out of 2 samples at leaf node
								else:
									pixels_high.append((12, 20))
									if features[11][11] <= 32.0:
										pixels_low.append((11, 11))
										if features[11][19] <= 62.0:
											pixels_low.append((11, 19))
											if features[16][11] <= 182.0:
												pixels_low.append((16, 11))
												ans = 1												 # approximately 2 were 1 out of 2 samples at leaf node
											else:
												pixels_high.append((16, 11))
												ans = 7												 # approximately 3 were 7 out of 3 samples at leaf node
										else:
											pixels_high.append((11, 19))
											if features[13][11] <= 72.0:
												pixels_low.append((13, 11))
												ans = 2												 # approximately 9 were 2 out of 9 samples at leaf node
											else:
												pixels_high.append((13, 11))
												ans = 7												 # approximately 1 were 7 out of 1 samples at leaf node
									else:
										pixels_high.append((11, 11))
										ans = 8										 # approximately 4 were 8 out of 4 samples at leaf node
						else:
							pixels_high.append((12, 10))
							if features[17][9] <= 17.0:
								pixels_low.append((17, 9))
								ans = 1								 # approximately 42 were 1 out of 42 samples at leaf node
							else:
								pixels_high.append((17, 9))
								if features[12][19] <= 178.0:
									pixels_low.append((12, 19))
									if features[15][11] <= 134.0:
										pixels_low.append((15, 11))
										if features[11][8] <= 206.5:
											pixels_low.append((11, 8))
											ans = 7											 # approximately 1 were 7 out of 1 samples at leaf node
										else:
											pixels_high.append((11, 8))
											if features[17][18] <= 73.0:
												pixels_low.append((17, 18))
												ans = 1												 # approximately 1 were 1 out of 1 samples at leaf node
											else:
												pixels_high.append((17, 18))
												ans = 5												 # approximately 1 were 5 out of 1 samples at leaf node
									else:
										pixels_high.append((15, 11))
										ans = 9										 # approximately 2 were 9 out of 2 samples at leaf node
								else:
									pixels_high.append((12, 19))
									ans = 8									 # approximately 3 were 8 out of 3 samples at leaf node
					else:
						pixels_high.append((10, 19))
						if features[12][11] <= 30.5:
							pixels_low.append((12, 11))
							if features[8][13] <= 22.0:
								pixels_low.append((8, 13))
								if features[12][5] <= 3.5:
									pixels_low.append((12, 5))
									if features[15][16] <= 87.5:
										pixels_low.append((15, 16))
										ans = 2										 # approximately 14 were 2 out of 14 samples at leaf node
									else:
										pixels_high.append((15, 16))
										if features[9][20] <= 141.5:
											pixels_low.append((9, 20))
											ans = 7											 # approximately 12 were 7 out of 12 samples at leaf node
										else:
											pixels_high.append((9, 20))
											if features[25][13] <= 32.0:
												pixels_low.append((25, 13))
												ans = 2												 # approximately 4 were 2 out of 4 samples at leaf node
											else:
												pixels_high.append((25, 13))
												ans = 7												 # approximately 1 were 7 out of 1 samples at leaf node
								else:
									pixels_high.append((12, 5))
									if features[13][8] <= 250.5:
										pixels_low.append((13, 8))
										if features[12][24] <= 252.5:
											pixels_low.append((12, 24))
											ans = 2											 # approximately 80 were 2 out of 80 samples at leaf node
										else:
											pixels_high.append((12, 24))
											if features[19][7] <= 223.0:
												pixels_low.append((19, 7))
												ans = 7												 # approximately 1 were 7 out of 1 samples at leaf node
											else:
												pixels_high.append((19, 7))
												ans = 2												 # approximately 1 were 2 out of 1 samples at leaf node
									else:
										pixels_high.append((13, 8))
										ans = 1										 # approximately 1 were 1 out of 1 samples at leaf node
							else:
								pixels_high.append((8, 13))
								if features[16][8] <= 2.5:
									pixels_low.append((16, 8))
									ans = 6									 # approximately 10 were 6 out of 10 samples at leaf node
								else:
									pixels_high.append((16, 8))
									if features[18][10] <= 175.0:
										pixels_low.append((18, 10))
										if features[18][6] <= 64.0:
											pixels_low.append((18, 6))
											ans = 2											 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											pixels_high.append((18, 6))
											if features[10][11] <= 9.5:
												pixels_low.append((10, 11))
												ans = 9												 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												pixels_high.append((10, 11))
												ans = 0												 # approximately 1 were 0 out of 1 samples at leaf node
									else:
										pixels_high.append((18, 10))
										ans = 8										 # approximately 2 were 8 out of 2 samples at leaf node
						else:
							pixels_high.append((12, 11))
							if features[11][23] <= 19.0:
								pixels_low.append((11, 23))
								if features[22][19] <= 49.0:
									pixels_low.append((22, 19))
									ans = 2									 # approximately 6 were 2 out of 6 samples at leaf node
								else:
									pixels_high.append((22, 19))
									if features[12][8] <= 137.5:
										pixels_low.append((12, 8))
										ans = 1										 # approximately 1 were 1 out of 1 samples at leaf node
									else:
										pixels_high.append((12, 8))
										ans = 9										 # approximately 1 were 9 out of 1 samples at leaf node
							else:
								pixels_high.append((11, 23))
								if features[10][24] <= 252.5:
									pixels_low.append((10, 24))
									ans = 8									 # approximately 29 were 8 out of 29 samples at leaf node
								else:
									pixels_high.append((10, 24))
									ans = 7									 # approximately 1 were 7 out of 1 samples at leaf node
			else:
				pixels_high.append((18, 19))
				if features[8][13] <= 2.0:
					pixels_low.append((8, 13))
					if features[15][23] <= 1.5:
						pixels_low.append((15, 23))
						if features[12][16] <= 1.0:
							pixels_low.append((12, 16))
							if features[18][10] <= 29.0:
								pixels_low.append((18, 10))
								if features[15][18] <= 38.5:
									pixels_low.append((15, 18))
									if features[12][8] <= 111.0:
										pixels_low.append((12, 8))
										if features[17][15] <= 38.5:
											pixels_low.append((17, 15))
											ans = 2											 # approximately 2 were 2 out of 2 samples at leaf node
										else:
											pixels_high.append((17, 15))
											ans = 3											 # approximately 2 were 3 out of 2 samples at leaf node
									else:
										pixels_high.append((12, 8))
										ans = 5										 # approximately 3 were 5 out of 3 samples at leaf node
								else:
									pixels_high.append((15, 18))
									if features[9][4] <= 116.5:
										pixels_low.append((9, 4))
										if features[14][22] <= 205.5:
											pixels_low.append((14, 22))
											if features[22][13] <= 101.5:
												pixels_low.append((22, 13))
												ans = 1												 # approximately 31 were 1 out of 31 samples at leaf node
											else:
												pixels_high.append((22, 13))
												ans = 6												 # approximately 1 were 6 out of 1 samples at leaf node
										else:
											pixels_high.append((14, 22))
											if features[16][21] <= 91.0:
												pixels_low.append((16, 21))
												ans = 2												 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												pixels_high.append((16, 21))
												ans = 5												 # approximately 1 were 5 out of 1 samples at leaf node
									else:
										pixels_high.append((9, 4))
										ans = 2										 # approximately 4 were 2 out of 4 samples at leaf node
							else:
								pixels_high.append((18, 10))
								if features[19][6] <= 21.5:
									pixels_low.append((19, 6))
									if features[19][19] <= 96.5:
										pixels_low.append((19, 19))
										ans = 2										 # approximately 2 were 2 out of 2 samples at leaf node
									else:
										pixels_high.append((19, 19))
										ans = 6										 # approximately 6 were 6 out of 6 samples at leaf node
								else:
									pixels_high.append((19, 6))
									ans = 3									 # approximately 6 were 3 out of 6 samples at leaf node
						else:
							pixels_high.append((12, 16))
							if features[6][13] <= 123.5:
								pixels_low.append((6, 13))
								if features[9][20] <= 5.5:
									pixels_low.append((9, 20))
									if features[20][19] <= 13.5:
										pixels_low.append((20, 19))
										if features[17][10] <= 94.5:
											pixels_low.append((17, 10))
											if features[17][19] <= 10.5:
												pixels_low.append((17, 19))
												ans = 1												 # approximately 4 were 1 out of 4 samples at leaf node
											else:
												pixels_high.append((17, 19))
												if features[14][5] <= 154.0:
													pixels_low.append((14, 5))
													if features[13][20] <= 52.0:
														pixels_low.append((13, 20))
														if features[18][19] <= 226.5:
															pixels_low.append((18, 19))
															ans = 2															 # approximately 1 were 2 out of 1 samples at leaf node
														else:
															pixels_high.append((18, 19))
															if features[20][23] <= 45.5:
																pixels_low.append((20, 23))
																ans = 4																 # approximately 1 were 4 out of 1 samples at leaf node
															else:
																pixels_high.append((20, 23))
																ans = 3																 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														pixels_high.append((13, 20))
														ans = 6														 # approximately 6 were 6 out of 6 samples at leaf node
												else:
													pixels_high.append((14, 5))
													if features[15][15] <= 202.5:
														pixels_low.append((15, 15))
														ans = 2														 # approximately 7 were 2 out of 7 samples at leaf node
													else:
														pixels_high.append((15, 15))
														ans = 5														 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											pixels_high.append((17, 10))
											if features[12][14] <= 2.0:
												pixels_low.append((12, 14))
												ans = 7												 # approximately 2 were 7 out of 2 samples at leaf node
											else:
												pixels_high.append((12, 14))
												ans = 3												 # approximately 8 were 3 out of 8 samples at leaf node
									else:
										pixels_high.append((20, 19))
										if features[18][25] <= 18.0:
											pixels_low.append((18, 25))
											if features[11][24] <= 40.0:
												pixels_low.append((11, 24))
												ans = 2												 # approximately 44 were 2 out of 44 samples at leaf node
											else:
												pixels_high.append((11, 24))
												ans = 7												 # approximately 1 were 7 out of 1 samples at leaf node
										else:
											pixels_high.append((18, 25))
											if features[16][13] <= 28.5:
												pixels_low.append((16, 13))
												ans = 7												 # approximately 1 were 7 out of 1 samples at leaf node
											else:
												pixels_high.append((16, 13))
												ans = 3												 # approximately 2 were 3 out of 2 samples at leaf node
								else:
									pixels_high.append((9, 20))
									if features[12][12] <= 107.0:
										pixels_low.append((12, 12))
										if features[11][10] <= 254.5:
											pixels_low.append((11, 10))
											if features[6][24] <= 173.5:
												pixels_low.append((6, 24))
												if features[12][23] <= 252.5:
													pixels_low.append((12, 23))
													if features[18][22] <= 253.5:
														pixels_low.append((18, 22))
														ans = 2														 # approximately 345 were 2 out of 345 samples at leaf node
													else:
														pixels_high.append((18, 22))
														if features[20][20] <= 84.0:
															pixels_low.append((20, 20))
															ans = 1															 # approximately 1 were 1 out of 1 samples at leaf node
														else:
															pixels_high.append((20, 20))
															ans = 2															 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													pixels_high.append((12, 23))
													if features[8][8] <= 73.0:
														pixels_low.append((8, 8))
														ans = 2														 # approximately 1 were 2 out of 1 samples at leaf node
													else:
														pixels_high.append((8, 8))
														ans = 1														 # approximately 1 were 1 out of 1 samples at leaf node
											else:
												pixels_high.append((6, 24))
												ans = 7												 # approximately 1 were 7 out of 1 samples at leaf node
										else:
											pixels_high.append((11, 10))
											ans = 6											 # approximately 1 were 6 out of 1 samples at leaf node
									else:
										pixels_high.append((12, 12))
										if features[16][17] <= 60.0:
											pixels_low.append((16, 17))
											ans = 1											 # approximately 2 were 1 out of 2 samples at leaf node
										else:
											pixels_high.append((16, 17))
											if features[20][19] <= 74.5:
												pixels_low.append((20, 19))
												ans = 8												 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												pixels_high.append((20, 19))
												ans = 2												 # approximately 1 were 2 out of 1 samples at leaf node
							else:
								pixels_high.append((6, 13))
								if features[18][23] <= 39.0:
									pixels_low.append((18, 23))
									ans = 6									 # approximately 12 were 6 out of 12 samples at leaf node
								else:
									pixels_high.append((18, 23))
									if features[17][20] <= 64.0:
										pixels_low.append((17, 20))
										ans = 4										 # approximately 3 were 4 out of 3 samples at leaf node
									else:
										pixels_high.append((17, 20))
										ans = 9										 # approximately 1 were 9 out of 1 samples at leaf node
					else:
						pixels_high.append((15, 23))
						if features[12][11] <= 41.0:
							pixels_low.append((12, 11))
							if features[17][17] <= 13.0:
								pixels_low.append((17, 17))
								if features[11][21] <= 24.0:
									pixels_low.append((11, 21))
									if features[14][19] <= 118.5:
										pixels_low.append((14, 19))
										if features[25][8] <= 52.5:
											pixels_low.append((25, 8))
											ans = 3											 # approximately 2 were 3 out of 2 samples at leaf node
										else:
											pixels_high.append((25, 8))
											ans = 5											 # approximately 1 were 5 out of 1 samples at leaf node
									else:
										pixels_high.append((14, 19))
										ans = 1										 # approximately 5 were 1 out of 5 samples at leaf node
								else:
									pixels_high.append((11, 21))
									if features[22][12] <= 126.5:
										pixels_low.append((22, 12))
										if features[18][19] <= 6.0:
											pixels_low.append((18, 19))
											ans = 1											 # approximately 1 were 1 out of 1 samples at leaf node
										else:
											pixels_high.append((18, 19))
											ans = 2											 # approximately 39 were 2 out of 39 samples at leaf node
									else:
										pixels_high.append((22, 12))
										ans = 9										 # approximately 1 were 9 out of 1 samples at leaf node
							else:
								pixels_high.append((17, 17))
								if features[13][14] <= 7.5:
									pixels_low.append((13, 14))
									if features[19][20] <= 21.0:
										pixels_low.append((19, 20))
										if features[17][22] <= 14.0:
											pixels_low.append((17, 22))
											ans = 7											 # approximately 8 were 7 out of 8 samples at leaf node
										else:
											pixels_high.append((17, 22))
											if features[10][16] <= 127.0:
												pixels_low.append((10, 16))
												if features[17][8] <= 126.0:
													pixels_low.append((17, 8))
													ans = 1													 # approximately 1 were 1 out of 1 samples at leaf node
												else:
													pixels_high.append((17, 8))
													ans = 3													 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												pixels_high.append((10, 16))
												ans = 4												 # approximately 1 were 4 out of 1 samples at leaf node
									else:
										pixels_high.append((19, 20))
										ans = 2										 # approximately 5 were 2 out of 5 samples at leaf node
								else:
									pixels_high.append((13, 14))
									if features[20][14] <= 31.0:
										pixels_low.append((20, 14))
										if features[13][10] <= 214.0:
											pixels_low.append((13, 10))
											if features[8][18] <= 250.5:
												pixels_low.append((8, 18))
												if features[17][25] <= 232.5:
													pixels_low.append((17, 25))
													ans = 3													 # approximately 74 were 3 out of 74 samples at leaf node
												else:
													pixels_high.append((17, 25))
													ans = 7													 # approximately 1 were 7 out of 1 samples at leaf node
											else:
												pixels_high.append((8, 18))
												ans = 8												 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											pixels_high.append((13, 10))
											if features[14][5] <= 126.5:
												pixels_low.append((14, 5))
												ans = 1												 # approximately 1 were 1 out of 1 samples at leaf node
											else:
												pixels_high.append((14, 5))
												ans = 8												 # approximately 1 were 8 out of 1 samples at leaf node
									else:
										pixels_high.append((20, 14))
										if features[15][12] <= 125.0:
											pixels_low.append((15, 12))
											ans = 2											 # approximately 2 were 2 out of 2 samples at leaf node
										else:
											pixels_high.append((15, 12))
											ans = 9											 # approximately 1 were 9 out of 1 samples at leaf node
						else:
							pixels_high.append((12, 11))
							if features[15][19] <= 231.5:
								pixels_low.append((15, 19))
								if features[14][10] <= 96.0:
									pixels_low.append((14, 10))
									if features[7][22] <= 93.5:
										pixels_low.append((7, 22))
										if features[14][14] <= 167.0:
											pixels_low.append((14, 14))
											if features[13][10] <= 219.0:
												pixels_low.append((13, 10))
												ans = 3												 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												pixels_high.append((13, 10))
												ans = 5												 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											pixels_high.append((14, 14))
											if features[20][14] <= 48.0:
												pixels_low.append((20, 14))
												ans = 8												 # approximately 43 were 8 out of 43 samples at leaf node
											else:
												pixels_high.append((20, 14))
												ans = 9												 # approximately 1 were 9 out of 1 samples at leaf node
									else:
										pixels_high.append((7, 22))
										if features[14][7] <= 140.0:
											pixels_low.append((14, 7))
											ans = 2											 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											pixels_high.append((14, 7))
											ans = 5											 # approximately 3 were 5 out of 3 samples at leaf node
								else:
									pixels_high.append((14, 10))
									if features[15][17] <= 235.5:
										pixels_low.append((15, 17))
										ans = 3										 # approximately 6 were 3 out of 6 samples at leaf node
									else:
										pixels_high.append((15, 17))
										if features[12][5] <= 44.5:
											pixels_low.append((12, 5))
											ans = 5											 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											pixels_high.append((12, 5))
											ans = 8											 # approximately 1 were 8 out of 1 samples at leaf node
							else:
								pixels_high.append((15, 19))
								if features[11][21] <= 20.0:
									pixels_low.append((11, 21))
									ans = 1									 # approximately 24 were 1 out of 24 samples at leaf node
								else:
									pixels_high.append((11, 21))
									if features[12][16] <= 6.5:
										pixels_low.append((12, 16))
										ans = 3										 # approximately 1 were 3 out of 1 samples at leaf node
									else:
										pixels_high.append((12, 16))
										ans = 7										 # approximately 1 were 7 out of 1 samples at leaf node
				else:
					pixels_high.append((8, 13))
					if features[12][20] <= 53.5:
						pixels_low.append((12, 20))
						if features[19][14] <= 2.5:
							pixels_low.append((19, 14))
							if features[15][13] <= 19.0:
								pixels_low.append((15, 13))
								if features[10][19] <= 22.5:
									pixels_low.append((10, 19))
									ans = 5									 # approximately 47 were 5 out of 47 samples at leaf node
								else:
									pixels_high.append((10, 19))
									ans = 6									 # approximately 2 were 6 out of 2 samples at leaf node
							else:
								pixels_high.append((15, 13))
								if features[21][11] <= 48.0:
									pixels_low.append((21, 11))
									if features[10][15] <= 106.5:
										pixels_low.append((10, 15))
										if features[16][16] <= 53.0:
											pixels_low.append((16, 16))
											if features[19][18] <= 174.5:
												pixels_low.append((19, 18))
												if features[16][17] <= 14.0:
													pixels_low.append((16, 17))
													ans = 7													 # approximately 1 were 7 out of 1 samples at leaf node
												else:
													pixels_high.append((16, 17))
													ans = 2													 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												pixels_high.append((19, 18))
												ans = 0												 # approximately 2 were 0 out of 2 samples at leaf node
										else:
											pixels_high.append((16, 16))
											ans = 3											 # approximately 3 were 3 out of 3 samples at leaf node
									else:
										pixels_high.append((10, 15))
										if features[13][7] <= 35.5:
											pixels_low.append((13, 7))
											if features[14][26] <= 18.5:
												pixels_low.append((14, 26))
												ans = 2												 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												pixels_high.append((14, 26))
												ans = 5												 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											pixels_high.append((13, 7))
											ans = 8											 # approximately 6 were 8 out of 6 samples at leaf node
								else:
									pixels_high.append((21, 11))
									ans = 6									 # approximately 6 were 6 out of 6 samples at leaf node
						else:
							pixels_high.append((19, 14))
							if features[15][7] <= 8.0:
								pixels_low.append((15, 7))
								if features[16][6] <= 161.5:
									pixels_low.append((16, 6))
									ans = 4									 # approximately 35 were 4 out of 35 samples at leaf node
								else:
									pixels_high.append((16, 6))
									if features[15][5] <= 92.0:
										pixels_low.append((15, 5))
										ans = 9										 # approximately 1 were 9 out of 1 samples at leaf node
									else:
										pixels_high.append((15, 5))
										ans = 0										 # approximately 1 were 0 out of 1 samples at leaf node
							else:
								pixels_high.append((15, 7))
								if features[9][12] <= 234.5:
									pixels_low.append((9, 12))
									ans = 9									 # approximately 11 were 9 out of 11 samples at leaf node
								else:
									pixels_high.append((9, 12))
									if features[9][18] <= 126.5:
										pixels_low.append((9, 18))
										ans = 4										 # approximately 1 were 4 out of 1 samples at leaf node
									else:
										pixels_high.append((9, 18))
										ans = 0										 # approximately 1 were 0 out of 1 samples at leaf node
					else:
						pixels_high.append((12, 20))
						if features[15][8] <= 40.5:
							pixels_low.append((15, 8))
							if features[8][21] <= 252.5:
								pixels_low.append((8, 21))
								if features[20][7] <= 241.5:
									pixels_low.append((20, 7))
									ans = 6									 # approximately 96 were 6 out of 96 samples at leaf node
								else:
									pixels_high.append((20, 7))
									if features[17][11] <= 127.0:
										pixels_low.append((17, 11))
										ans = 2										 # approximately 1 were 2 out of 1 samples at leaf node
									else:
										pixels_high.append((17, 11))
										ans = 8										 # approximately 1 were 8 out of 1 samples at leaf node
							else:
								pixels_high.append((8, 21))
								ans = 5								 # approximately 2 were 5 out of 2 samples at leaf node
						else:
							pixels_high.append((15, 8))
							if features[23][15] <= 19.0:
								pixels_low.append((23, 15))
								if features[18][18] <= 174.0:
									pixels_low.append((18, 18))
									if features[15][17] <= 28.5:
										pixels_low.append((15, 17))
										ans = 2										 # approximately 1 were 2 out of 1 samples at leaf node
									else:
										pixels_high.append((15, 17))
										ans = 8										 # approximately 7 were 8 out of 7 samples at leaf node
								else:
									pixels_high.append((18, 18))
									if features[8][17] <= 15.5:
										pixels_low.append((8, 17))
										if features[8][16] <= 13.5:
											pixels_low.append((8, 16))
											ans = 2											 # approximately 2 were 2 out of 2 samples at leaf node
										else:
											pixels_high.append((8, 16))
											ans = 5											 # approximately 3 were 5 out of 3 samples at leaf node
									else:
										pixels_high.append((8, 17))
										ans = 6										 # approximately 4 were 6 out of 4 samples at leaf node
							else:
								pixels_high.append((23, 15))
								ans = 0								 # approximately 4 were 0 out of 4 samples at leaf node
		else:
			pixels_high.append((11, 13))
			if features[15][12] <= 23.5:
				pixels_low.append((15, 12))
				if features[11][18] <= 52.5:
					pixels_low.append((11, 18))
					if features[20][15] <= 3.0:
						pixels_low.append((20, 15))
						if features[10][5] <= 77.5:
							pixels_low.append((10, 5))
							if features[9][18] <= 213.5:
								pixels_low.append((9, 18))
								if features[21][7] <= 2.5:
									pixels_low.append((21, 7))
									if features[14][12] <= 139.0:
										pixels_low.append((14, 12))
										if features[7][8] <= 48.5:
											pixels_low.append((7, 8))
											if features[16][13] <= 35.0:
												pixels_low.append((16, 13))
												if features[11][4] <= 103.0:
													pixels_low.append((11, 4))
													if features[11][6] <= 138.0:
														pixels_low.append((11, 6))
														if features[19][13] <= 26.0:
															pixels_low.append((19, 13))
															if features[20][16] <= 37.5:
																pixels_low.append((20, 16))
																if features[13][4] <= 160.5:
																	pixels_low.append((13, 4))
																	if features[17][22] <= 254.5:
																		pixels_low.append((17, 22))
																		if features[7][23] <= 253.5:
																			pixels_low.append((7, 23))
																			if features[13][25] <= 252.5:
																				pixels_low.append((13, 25))
																				if features[13][25] <= 152.0:
																					pixels_low.append((13, 25))
																					if features[12][18] <= 188.5:
																						pixels_low.append((12, 18))
																						ans = 5																						 # approximately 188 were 5 out of 188 samples at leaf node
																					else:
																						pixels_high.append((12, 18))
																						if features[11][21] <= 68.0:
																							pixels_low.append((11, 21))
																							ans = 5																							 # approximately 3 were 5 out of 3 samples at leaf node
																						else:
																							pixels_high.append((11, 21))
																							ans = 8																							 # approximately 1 were 8 out of 1 samples at leaf node
																				else:
																					pixels_high.append((13, 25))
																					if features[13][23] <= 19.0:
																						pixels_low.append((13, 23))
																						ans = 3																						 # approximately 1 were 3 out of 1 samples at leaf node
																					else:
																						pixels_high.append((13, 23))
																						ans = 5																						 # approximately 3 were 5 out of 3 samples at leaf node
																			else:
																				pixels_high.append((13, 25))
																				ans = 3																				 # approximately 1 were 3 out of 1 samples at leaf node
																		else:
																			pixels_high.append((7, 23))
																			ans = 3																			 # approximately 1 were 3 out of 1 samples at leaf node
																	else:
																		pixels_high.append((17, 22))
																		ans = 6																		 # approximately 1 were 6 out of 1 samples at leaf node
																else:
																	pixels_high.append((13, 4))
																	if features[15][11] <= 1.5:
																		pixels_low.append((15, 11))
																		ans = 5																		 # approximately 1 were 5 out of 1 samples at leaf node
																	else:
																		pixels_high.append((15, 11))
																		ans = 3																		 # approximately 2 were 3 out of 2 samples at leaf node
															else:
																pixels_high.append((20, 16))
																if features[13][22] <= 67.5:
																	pixels_low.append((13, 22))
																	ans = 2																	 # approximately 1 were 2 out of 1 samples at leaf node
																else:
																	pixels_high.append((13, 22))
																	ans = 6																	 # approximately 2 were 6 out of 2 samples at leaf node
														else:
															pixels_high.append((19, 13))
															if features[17][20] <= 57.0:
																pixels_low.append((17, 20))
																ans = 9																 # approximately 2 were 9 out of 2 samples at leaf node
															else:
																pixels_high.append((17, 20))
																if features[10][22] <= 127.5:
																	pixels_low.append((10, 22))
																	ans = 4																	 # approximately 1 were 4 out of 1 samples at leaf node
																else:
																	pixels_high.append((10, 22))
																	ans = 2																	 # approximately 1 were 2 out of 1 samples at leaf node
													else:
														pixels_high.append((11, 6))
														if features[13][11] <= 101.0:
															pixels_low.append((13, 11))
															if features[20][23] <= 11.0:
																pixels_low.append((20, 23))
																ans = 5																 # approximately 18 were 5 out of 18 samples at leaf node
															else:
																pixels_high.append((20, 23))
																if features[22][13] <= 126.5:
																	pixels_low.append((22, 13))
																	ans = 1																	 # approximately 1 were 1 out of 1 samples at leaf node
																else:
																	pixels_high.append((22, 13))
																	ans = 0																	 # approximately 1 were 0 out of 1 samples at leaf node
														else:
															pixels_high.append((13, 11))
															if features[13][18] <= 2.0:
																pixels_low.append((13, 18))
																ans = 3																 # approximately 9 were 3 out of 9 samples at leaf node
															else:
																pixels_high.append((13, 18))
																ans = 1																 # approximately 2 were 1 out of 2 samples at leaf node
												else:
													pixels_high.append((11, 4))
													ans = 3													 # approximately 5 were 3 out of 5 samples at leaf node
											else:
												pixels_high.append((16, 13))
												if features[12][7] <= 70.5:
													pixels_low.append((12, 7))
													if features[16][7] <= 126.5:
														pixels_low.append((16, 7))
														ans = 4														 # approximately 3 were 4 out of 3 samples at leaf node
													else:
														pixels_high.append((16, 7))
														if features[15][17] <= 234.0:
															pixels_low.append((15, 17))
															ans = 2															 # approximately 1 were 2 out of 1 samples at leaf node
														else:
															pixels_high.append((15, 17))
															ans = 9															 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													pixels_high.append((12, 7))
													ans = 8													 # approximately 4 were 8 out of 4 samples at leaf node
										else:
											pixels_high.append((7, 8))
											if features[8][16] <= 18.5:
												pixels_low.append((8, 16))
												if features[11][7] <= 254.5:
													pixels_low.append((11, 7))
													ans = 3													 # approximately 10 were 3 out of 10 samples at leaf node
												else:
													pixels_high.append((11, 7))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												pixels_high.append((8, 16))
												if features[19][22] <= 4.0:
													pixels_low.append((19, 22))
													ans = 2													 # approximately 2 were 2 out of 2 samples at leaf node
												else:
													pixels_high.append((19, 22))
													if features[20][9] <= 38.5:
														pixels_low.append((20, 9))
														ans = 5														 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														pixels_high.append((20, 9))
														ans = 8														 # approximately 1 were 8 out of 1 samples at leaf node
									else:
										pixels_high.append((14, 12))
										if features[13][9] <= 229.5:
											pixels_low.append((13, 9))
											if features[12][6] <= 27.5:
												pixels_low.append((12, 6))
												if features[14][21] <= 30.5:
													pixels_low.append((14, 21))
													ans = 2													 # approximately 2 were 2 out of 2 samples at leaf node
												else:
													pixels_high.append((14, 21))
													ans = 5													 # approximately 3 were 5 out of 3 samples at leaf node
											else:
												pixels_high.append((12, 6))
												ans = 3												 # approximately 5 were 3 out of 5 samples at leaf node
										else:
											pixels_high.append((13, 9))
											ans = 1											 # approximately 13 were 1 out of 13 samples at leaf node
								else:
									pixels_high.append((21, 7))
									if features[16][13] <= 141.0:
										pixels_low.append((16, 13))
										ans = 5										 # approximately 560 were 5 out of 560 samples at leaf node
									else:
										pixels_high.append((16, 13))
										if features[20][10] <= 190.0:
											pixels_low.append((20, 10))
											if features[9][13] <= 230.5:
												pixels_low.append((9, 13))
												ans = 4												 # approximately 1 were 4 out of 1 samples at leaf node
											else:
												pixels_high.append((9, 13))
												ans = 9												 # approximately 1 were 9 out of 1 samples at leaf node
										else:
											pixels_high.append((20, 10))
											ans = 8											 # approximately 2 were 8 out of 2 samples at leaf node
							else:
								pixels_high.append((9, 18))
								if features[20][4] <= 8.0:
									pixels_low.append((20, 4))
									if features[16][23] <= 7.5:
										pixels_low.append((16, 23))
										if features[11][9] <= 252.5:
											pixels_low.append((11, 9))
											ans = 5											 # approximately 7 were 5 out of 7 samples at leaf node
										else:
											pixels_high.append((11, 9))
											ans = 8											 # approximately 1 were 8 out of 1 samples at leaf node
									else:
										pixels_high.append((16, 23))
										if features[9][22] <= 3.5:
											pixels_low.append((9, 22))
											if features[14][8] <= 162.0:
												pixels_low.append((14, 8))
												ans = 0												 # approximately 1 were 0 out of 1 samples at leaf node
											else:
												pixels_high.append((14, 8))
												ans = 6												 # approximately 1 were 6 out of 1 samples at leaf node
										else:
											pixels_high.append((9, 22))
											ans = 8											 # approximately 7 were 8 out of 7 samples at leaf node
								else:
									pixels_high.append((20, 4))
									if features[19][5] <= 253.5:
										pixels_low.append((19, 5))
										ans = 6										 # approximately 16 were 6 out of 16 samples at leaf node
									else:
										pixels_high.append((19, 5))
										ans = 8										 # approximately 1 were 8 out of 1 samples at leaf node
						else:
							pixels_high.append((10, 5))
							if features[10][9] <= 31.0:
								pixels_low.append((10, 9))
								if features[16][16] <= 80.5:
									pixels_low.append((16, 16))
									if features[19][23] <= 101.0:
										pixels_low.append((19, 23))
										if features[14][19] <= 126.5:
											pixels_low.append((14, 19))
											ans = 2											 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											pixels_high.append((14, 19))
											ans = 1											 # approximately 1 were 1 out of 1 samples at leaf node
									else:
										pixels_high.append((19, 23))
										ans = 8										 # approximately 3 were 8 out of 3 samples at leaf node
								else:
									pixels_high.append((16, 16))
									ans = 3									 # approximately 42 were 3 out of 42 samples at leaf node
							else:
								pixels_high.append((10, 9))
								if features[12][12] <= 248.5:
									pixels_low.append((12, 12))
									ans = 5									 # approximately 17 were 5 out of 17 samples at leaf node
								else:
									pixels_high.append((12, 12))
									if features[13][6] <= 119.5:
										pixels_low.append((13, 6))
										ans = 1										 # approximately 2 were 1 out of 2 samples at leaf node
									else:
										pixels_high.append((13, 6))
										if features[15][13] <= 35.5:
											pixels_low.append((15, 13))
											ans = 0											 # approximately 2 were 0 out of 2 samples at leaf node
										else:
											pixels_high.append((15, 13))
											ans = 3											 # approximately 1 were 3 out of 1 samples at leaf node
					else:
						pixels_high.append((20, 15))
						if features[16][16] <= 32.5:
							pixels_low.append((16, 16))
							if features[10][12] <= 44.0:
								pixels_low.append((10, 12))
								if features[12][11] <= 127.0:
									pixels_low.append((12, 11))
									ans = 2									 # approximately 1 were 2 out of 1 samples at leaf node
								else:
									pixels_high.append((12, 11))
									ans = 9									 # approximately 1 were 9 out of 1 samples at leaf node
							else:
								pixels_high.append((10, 12))
								ans = 0								 # approximately 15 were 0 out of 15 samples at leaf node
						else:
							pixels_high.append((16, 16))
							if features[14][4] <= 5.0:
								pixels_low.append((14, 4))
								if features[19][13] <= 54.5:
									pixels_low.append((19, 13))
									if features[11][13] <= 252.5:
										pixels_low.append((11, 13))
										if features[8][13] <= 72.0:
											pixels_low.append((8, 13))
											if features[11][10] <= 243.0:
												pixels_low.append((11, 10))
												ans = 2												 # approximately 4 were 2 out of 4 samples at leaf node
											else:
												pixels_high.append((11, 10))
												if features[18][21] <= 81.5:
													pixels_low.append((18, 21))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													pixels_high.append((18, 21))
													ans = 6													 # approximately 1 were 6 out of 1 samples at leaf node
										else:
											pixels_high.append((8, 13))
											if features[12][22] <= 206.0:
												pixels_low.append((12, 22))
												ans = 9												 # approximately 4 were 9 out of 4 samples at leaf node
											else:
												pixels_high.append((12, 22))
												if features[12][10] <= 55.5:
													pixels_low.append((12, 10))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													pixels_high.append((12, 10))
													if features[16][21] <= 24.0:
														pixels_low.append((16, 21))
														ans = 4														 # approximately 1 were 4 out of 1 samples at leaf node
													else:
														pixels_high.append((16, 21))
														if features[6][23] <= 88.5:
															pixels_low.append((6, 23))
															ans = 6															 # approximately 1 were 6 out of 1 samples at leaf node
														else:
															pixels_high.append((6, 23))
															ans = 0															 # approximately 1 were 0 out of 1 samples at leaf node
									else:
										pixels_high.append((11, 13))
										ans = 3										 # approximately 3 were 3 out of 3 samples at leaf node
								else:
									pixels_high.append((19, 13))
									if features[17][8] <= 39.0:
										pixels_low.append((17, 8))
										ans = 4										 # approximately 10 were 4 out of 10 samples at leaf node
									else:
										pixels_high.append((17, 8))
										if features[13][18] <= 65.0:
											pixels_low.append((13, 18))
											ans = 2											 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											pixels_high.append((13, 18))
											ans = 9											 # approximately 1 were 9 out of 1 samples at leaf node
							else:
								pixels_high.append((14, 4))
								if features[9][11] <= 213.0:
									pixels_low.append((9, 11))
									ans = 2									 # approximately 20 were 2 out of 20 samples at leaf node
								else:
									pixels_high.append((9, 11))
									ans = 5									 # approximately 1 were 5 out of 1 samples at leaf node
				else:
					pixels_high.append((11, 18))
					if features[20][9] <= 11.5:
						pixels_low.append((20, 9))
						if features[13][23] <= 18.0:
							pixels_low.append((13, 23))
							if features[13][21] <= 32.0:
								pixels_low.append((13, 21))
								if features[14][17] <= 138.0:
									pixels_low.append((14, 17))
									if features[8][24] <= 121.5:
										pixels_low.append((8, 24))
										ans = 6										 # approximately 6 were 6 out of 6 samples at leaf node
									else:
										pixels_high.append((8, 24))
										ans = 5										 # approximately 1 were 5 out of 1 samples at leaf node
								else:
									pixels_high.append((14, 17))
									if features[18][7] <= 21.5:
										pixels_low.append((18, 7))
										if features[14][19] <= 214.5:
											pixels_low.append((14, 19))
											ans = 2											 # approximately 7 were 2 out of 7 samples at leaf node
										else:
											pixels_high.append((14, 19))
											ans = 6											 # approximately 1 were 6 out of 1 samples at leaf node
									else:
										pixels_high.append((18, 7))
										ans = 5										 # approximately 4 were 5 out of 4 samples at leaf node
							else:
								pixels_high.append((13, 21))
								if features[20][22] <= 175.0:
									pixels_low.append((20, 22))
									if features[23][7] <= 129.0:
										pixels_low.append((23, 7))
										ans = 6										 # approximately 124 were 6 out of 124 samples at leaf node
									else:
										pixels_high.append((23, 7))
										ans = 8										 # approximately 1 were 8 out of 1 samples at leaf node
								else:
									pixels_high.append((20, 22))
									if features[23][20] <= 125.5:
										pixels_low.append((23, 20))
										ans = 5										 # approximately 1 were 5 out of 1 samples at leaf node
									else:
										pixels_high.append((23, 20))
										ans = 2										 # approximately 1 were 2 out of 1 samples at leaf node
						else:
							pixels_high.append((13, 23))
							if features[19][4] <= 74.5:
								pixels_low.append((19, 4))
								if features[18][6] <= 212.5:
									pixels_low.append((18, 6))
									if features[11][20] <= 65.0:
										pixels_low.append((11, 20))
										if features[13][16] <= 106.0:
											pixels_low.append((13, 16))
											ans = 4											 # approximately 2 were 4 out of 2 samples at leaf node
										else:
											pixels_high.append((13, 16))
											if features[18][23] <= 2.5:
												pixels_low.append((18, 23))
												ans = 5												 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												pixels_high.append((18, 23))
												ans = 1												 # approximately 1 were 1 out of 1 samples at leaf node
									else:
										pixels_high.append((11, 20))
										ans = 8										 # approximately 11 were 8 out of 11 samples at leaf node
								else:
									pixels_high.append((18, 6))
									if features[15][20] <= 252.5:
										pixels_low.append((15, 20))
										ans = 5										 # approximately 9 were 5 out of 9 samples at leaf node
									else:
										pixels_high.append((15, 20))
										if features[11][11] <= 251.5:
											pixels_low.append((11, 11))
											ans = 8											 # approximately 2 were 8 out of 2 samples at leaf node
										else:
											pixels_high.append((11, 11))
											ans = 6											 # approximately 1 were 6 out of 1 samples at leaf node
							else:
								pixels_high.append((19, 4))
								if features[14][8] <= 72.5:
									pixels_low.append((14, 8))
									ans = 8									 # approximately 2 were 8 out of 2 samples at leaf node
								else:
									pixels_high.append((14, 8))
									ans = 6									 # approximately 11 were 6 out of 11 samples at leaf node
					else:
						pixels_high.append((20, 9))
						if features[14][22] <= 2.5:
							pixels_low.append((14, 22))
							if features[7][15] <= 180.5:
								pixels_low.append((7, 15))
								if features[19][22] <= 252.5:
									pixels_low.append((19, 22))
									ans = 5									 # approximately 32 were 5 out of 32 samples at leaf node
								else:
									pixels_high.append((19, 22))
									ans = 8									 # approximately 1 were 8 out of 1 samples at leaf node
							else:
								pixels_high.append((7, 15))
								if features[11][14] <= 240.0:
									pixels_low.append((11, 14))
									if features[6][20] <= 87.0:
										pixels_low.append((6, 20))
										ans = 4										 # approximately 2 were 4 out of 2 samples at leaf node
									else:
										pixels_high.append((6, 20))
										ans = 0										 # approximately 2 were 0 out of 2 samples at leaf node
								else:
									pixels_high.append((11, 14))
									ans = 2									 # approximately 6 were 2 out of 6 samples at leaf node
						else:
							pixels_high.append((14, 22))
							if features[9][17] <= 70.0:
								pixels_low.append((9, 17))
								if features[13][9] <= 242.5:
									pixels_low.append((13, 9))
									ans = 8									 # approximately 18 were 8 out of 18 samples at leaf node
								else:
									pixels_high.append((13, 9))
									if features[22][9] <= 1.0:
										pixels_low.append((22, 9))
										if features[14][5] <= 13.0:
											pixels_low.append((14, 5))
											if features[15][18] <= 7.5:
												pixels_low.append((15, 18))
												ans = 6												 # approximately 1 were 6 out of 1 samples at leaf node
											else:
												pixels_high.append((15, 18))
												ans = 1												 # approximately 1 were 1 out of 1 samples at leaf node
										else:
											pixels_high.append((14, 5))
											ans = 8											 # approximately 3 were 8 out of 3 samples at leaf node
									else:
										pixels_high.append((22, 9))
										ans = 5										 # approximately 4 were 5 out of 4 samples at leaf node
							else:
								pixels_high.append((9, 17))
								if features[16][17] <= 102.5:
									pixels_low.append((16, 17))
									ans = 0									 # approximately 4 were 0 out of 4 samples at leaf node
								else:
									pixels_high.append((16, 17))
									if features[14][9] <= 4.5:
										pixels_low.append((14, 9))
										ans = 2										 # approximately 3 were 2 out of 3 samples at leaf node
									else:
										pixels_high.append((14, 9))
										if features[13][14] <= 253.5:
											pixels_low.append((13, 14))
											ans = 6											 # approximately 5 were 6 out of 5 samples at leaf node
										else:
											pixels_high.append((13, 14))
											if features[20][10] <= 11.0:
												pixels_low.append((20, 10))
												ans = 8												 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												pixels_high.append((20, 10))
												ans = 5												 # approximately 1 were 5 out of 1 samples at leaf node
			else:
				pixels_high.append((15, 12))
				if features[13][23] <= 1.5:
					pixels_low.append((13, 23))
					if features[20][13] <= 8.0:
						pixels_low.append((20, 13))
						if features[23][9] <= 58.5:
							pixels_low.append((23, 9))
							if features[22][18] <= 6.0:
								pixels_low.append((22, 18))
								if features[10][13] <= 1.5:
									pixels_low.append((10, 13))
									if features[14][11] <= 245.0:
										pixels_low.append((14, 11))
										if features[11][11] <= 6.5:
											pixels_low.append((11, 11))
											if features[16][17] <= 165.5:
												pixels_low.append((16, 17))
												if features[13][20] <= 120.5:
													pixels_low.append((13, 20))
													ans = 1													 # approximately 12 were 1 out of 12 samples at leaf node
												else:
													pixels_high.append((13, 20))
													if features[21][9] <= 71.5:
														pixels_low.append((21, 9))
														if features[14][6] <= 253.5:
															pixels_low.append((14, 6))
															ans = 2															 # approximately 11 were 2 out of 11 samples at leaf node
														else:
															pixels_high.append((14, 6))
															ans = 1															 # approximately 1 were 1 out of 1 samples at leaf node
													else:
														pixels_high.append((21, 9))
														if features[21][9] <= 226.5:
															pixels_low.append((21, 9))
															ans = 6															 # approximately 3 were 6 out of 3 samples at leaf node
														else:
															pixels_high.append((21, 9))
															ans = 8															 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												pixels_high.append((16, 17))
												if features[13][4] <= 118.5:
													pixels_low.append((13, 4))
													ans = 3													 # approximately 11 were 3 out of 11 samples at leaf node
												else:
													pixels_high.append((13, 4))
													ans = 2													 # approximately 2 were 2 out of 2 samples at leaf node
										else:
											pixels_high.append((11, 11))
											if features[16][11] <= 3.5:
												pixels_low.append((16, 11))
												if features[18][8] <= 127.0:
													pixels_low.append((18, 8))
													ans = 1													 # approximately 4 were 1 out of 4 samples at leaf node
												else:
													pixels_high.append((18, 8))
													ans = 9													 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												pixels_high.append((16, 11))
												if features[20][16] <= 113.0:
													pixels_low.append((20, 16))
													ans = 8													 # approximately 16 were 8 out of 16 samples at leaf node
												else:
													pixels_high.append((20, 16))
													ans = 2													 # approximately 1 were 2 out of 1 samples at leaf node
									else:
										pixels_high.append((14, 11))
										if features[15][14] <= 33.0:
											pixels_low.append((15, 14))
											if features[11][21] <= 248.0:
												pixels_low.append((11, 21))
												if features[8][21] <= 7.5:
													pixels_low.append((8, 21))
													ans = 8													 # approximately 2 were 8 out of 2 samples at leaf node
												else:
													pixels_high.append((8, 21))
													if features[20][7] <= 89.5:
														pixels_low.append((20, 7))
														ans = 2														 # approximately 1 were 2 out of 1 samples at leaf node
													else:
														pixels_high.append((20, 7))
														ans = 1														 # approximately 1 were 1 out of 1 samples at leaf node
											else:
												pixels_high.append((11, 21))
												ans = 6												 # approximately 3 were 6 out of 3 samples at leaf node
										else:
											pixels_high.append((15, 14))
											if features[21][21] <= 126.5:
												pixels_low.append((21, 21))
												if features[8][23] <= 254.0:
													pixels_low.append((8, 23))
													ans = 1													 # approximately 60 were 1 out of 60 samples at leaf node
												else:
													pixels_high.append((8, 23))
													ans = 3													 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												pixels_high.append((21, 21))
												ans = 2												 # approximately 2 were 2 out of 2 samples at leaf node
								else:
									pixels_high.append((10, 13))
									if features[18][18] <= 41.5:
										pixels_low.append((18, 18))
										if features[18][16] <= 8.0:
											pixels_low.append((18, 16))
											if features[6][19] <= 19.5:
												pixels_low.append((6, 19))
												if features[19][10] <= 2.5:
													pixels_low.append((19, 10))
													if features[15][5] <= 4.0:
														pixels_low.append((15, 5))
														if features[13][7] <= 8.0:
															pixels_low.append((13, 7))
															if features[12][14] <= 1.0:
																pixels_low.append((12, 14))
																ans = 9																 # approximately 3 were 9 out of 3 samples at leaf node
															else:
																pixels_high.append((12, 14))
																if features[19][8] <= 127.0:
																	pixels_low.append((19, 8))
																	if features[8][18] <= 89.0:
																		pixels_low.append((8, 18))
																		ans = 4																		 # approximately 5 were 4 out of 5 samples at leaf node
																	else:
																		pixels_high.append((8, 18))
																		if features[17][8] <= 127.0:
																			pixels_low.append((17, 8))
																			ans = 5																			 # approximately 1 were 5 out of 1 samples at leaf node
																		else:
																			pixels_high.append((17, 8))
																			ans = 2																			 # approximately 1 were 2 out of 1 samples at leaf node
																else:
																	pixels_high.append((19, 8))
																	ans = 1																	 # approximately 3 were 1 out of 3 samples at leaf node
														else:
															pixels_high.append((13, 7))
															ans = 9															 # approximately 19 were 9 out of 19 samples at leaf node
													else:
														pixels_high.append((15, 5))
														if features[14][10] <= 246.5:
															pixels_low.append((14, 10))
															if features[11][18] <= 15.5:
																pixels_low.append((11, 18))
																ans = 4																 # approximately 6 were 4 out of 6 samples at leaf node
															else:
																pixels_high.append((11, 18))
																if features[12][16] <= 4.0:
																	pixels_low.append((12, 16))
																	ans = 9																	 # approximately 1 were 9 out of 1 samples at leaf node
																else:
																	pixels_high.append((12, 16))
																	ans = 2																	 # approximately 2 were 2 out of 2 samples at leaf node
														else:
															pixels_high.append((14, 10))
															if features[11][8] <= 181.0:
																pixels_low.append((11, 8))
																ans = 1																 # approximately 8 were 1 out of 8 samples at leaf node
															else:
																pixels_high.append((11, 8))
																ans = 2																 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													pixels_high.append((19, 10))
													if features[11][9] <= 51.0:
														pixels_low.append((11, 9))
														if features[8][22] <= 147.0:
															pixels_low.append((8, 22))
															if features[15][13] <= 9.0:
																pixels_low.append((15, 13))
																ans = 5																 # approximately 3 were 5 out of 3 samples at leaf node
															else:
																pixels_high.append((15, 13))
																if features[19][20] <= 100.0:
																	pixels_low.append((19, 20))
																	if features[10][22] <= 178.0:
																		pixels_low.append((10, 22))
																		if features[15][13] <= 129.5:
																			pixels_low.append((15, 13))
																			ans = 9																			 # approximately 1 were 9 out of 1 samples at leaf node
																		else:
																			pixels_high.append((15, 13))
																			if features[8][23] <= 86.5:
																				pixels_low.append((8, 23))
																				ans = 8																				 # approximately 1 were 8 out of 1 samples at leaf node
																			else:
																				pixels_high.append((8, 23))
																				ans = 4																				 # approximately 1 were 4 out of 1 samples at leaf node
																	else:
																		pixels_high.append((10, 22))
																		ans = 1																		 # approximately 2 were 1 out of 2 samples at leaf node
																else:
																	pixels_high.append((19, 20))
																	ans = 2																	 # approximately 2 were 2 out of 2 samples at leaf node
														else:
															pixels_high.append((8, 22))
															ans = 3															 # approximately 4 were 3 out of 4 samples at leaf node
													else:
														pixels_high.append((11, 9))
														if features[12][15] <= 21.0:
															pixels_low.append((12, 15))
															ans = 9															 # approximately 2 were 9 out of 2 samples at leaf node
														else:
															pixels_high.append((12, 15))
															ans = 8															 # approximately 11 were 8 out of 11 samples at leaf node
											else:
												pixels_high.append((6, 19))
												if features[18][10] <= 233.5:
													pixels_low.append((18, 10))
													ans = 5													 # approximately 12 were 5 out of 12 samples at leaf node
												else:
													pixels_high.append((18, 10))
													if features[8][22] <= 9.5:
														pixels_low.append((8, 22))
														ans = 2														 # approximately 3 were 2 out of 3 samples at leaf node
													else:
														pixels_high.append((8, 22))
														if features[5][22] <= 95.5:
															pixels_low.append((5, 22))
															ans = 3															 # approximately 2 were 3 out of 2 samples at leaf node
														else:
															pixels_high.append((5, 22))
															ans = 8															 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											pixels_high.append((18, 16))
											if features[15][16] <= 44.0:
												pixels_low.append((15, 16))
												if features[19][18] <= 97.0:
													pixels_low.append((19, 18))
													ans = 6													 # approximately 1 were 6 out of 1 samples at leaf node
												else:
													pixels_high.append((19, 18))
													if features[17][8] <= 24.0:
														pixels_low.append((17, 8))
														ans = 8														 # approximately 1 were 8 out of 1 samples at leaf node
													else:
														pixels_high.append((17, 8))
														ans = 3														 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												pixels_high.append((15, 16))
												ans = 4												 # approximately 24 were 4 out of 24 samples at leaf node
									else:
										pixels_high.append((18, 18))
										if features[16][19] <= 115.0:
											pixels_low.append((16, 19))
											if features[9][12] <= 13.5:
												pixels_low.append((9, 12))
												if features[14][19] <= 31.5:
													pixels_low.append((14, 19))
													ans = 3													 # approximately 10 were 3 out of 10 samples at leaf node
												else:
													pixels_high.append((14, 19))
													if features[13][7] <= 252.5:
														pixels_low.append((13, 7))
														ans = 2														 # approximately 1 were 2 out of 1 samples at leaf node
													else:
														pixels_high.append((13, 7))
														ans = 8														 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												pixels_high.append((9, 12))
												if features[12][10] <= 217.5:
													pixels_low.append((12, 10))
													ans = 8													 # approximately 19 were 8 out of 19 samples at leaf node
												else:
													pixels_high.append((12, 10))
													ans = 4													 # approximately 1 were 4 out of 1 samples at leaf node
										else:
											pixels_high.append((16, 19))
											if features[10][15] <= 59.5:
												pixels_low.append((10, 15))
												if features[13][9] <= 252.5:
													pixels_low.append((13, 9))
													if features[12][11] <= 117.5:
														pixels_low.append((12, 11))
														ans = 3														 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														pixels_high.append((12, 11))
														ans = 4														 # approximately 2 were 4 out of 2 samples at leaf node
												else:
													pixels_high.append((13, 9))
													ans = 1													 # approximately 2 were 1 out of 2 samples at leaf node
											else:
												pixels_high.append((10, 15))
												if features[16][11] <= 251.0:
													pixels_low.append((16, 11))
													if features[23][24] <= 8.5:
														pixels_low.append((23, 24))
														ans = 6														 # approximately 15 were 6 out of 15 samples at leaf node
													else:
														pixels_high.append((23, 24))
														ans = 8														 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													pixels_high.append((16, 11))
													if features[14][4] <= 30.0:
														pixels_low.append((14, 4))
														if features[22][13] <= 85.0:
															pixels_low.append((22, 13))
															ans = 3															 # approximately 1 were 3 out of 1 samples at leaf node
														else:
															pixels_high.append((22, 13))
															ans = 6															 # approximately 1 were 6 out of 1 samples at leaf node
													else:
														pixels_high.append((14, 4))
														ans = 2														 # approximately 3 were 2 out of 3 samples at leaf node
							else:
								pixels_high.append((22, 18))
								if features[9][13] <= 246.5:
									pixels_low.append((9, 13))
									if features[14][13] <= 184.5:
										pixels_low.append((14, 13))
										if features[12][21] <= 83.0:
											pixels_low.append((12, 21))
											ans = 2											 # approximately 4 were 2 out of 4 samples at leaf node
										else:
											pixels_high.append((12, 21))
											if features[9][12] <= 11.5:
												pixels_low.append((9, 12))
												if features[12][12] <= 87.0:
													pixels_low.append((12, 12))
													ans = 1													 # approximately 1 were 1 out of 1 samples at leaf node
												else:
													pixels_high.append((12, 12))
													ans = 3													 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												pixels_high.append((9, 12))
												if features[6][18] <= 1.0:
													pixels_low.append((6, 18))
													if features[14][21] <= 113.5:
														pixels_low.append((14, 21))
														ans = 7														 # approximately 1 were 7 out of 1 samples at leaf node
													else:
														pixels_high.append((14, 21))
														ans = 8														 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													pixels_high.append((6, 18))
													ans = 6													 # approximately 1 were 6 out of 1 samples at leaf node
									else:
										pixels_high.append((14, 13))
										if features[22][9] <= 84.0:
											pixels_low.append((22, 9))
											ans = 2											 # approximately 80 were 2 out of 80 samples at leaf node
										else:
											pixels_high.append((22, 9))
											ans = 6											 # approximately 1 were 6 out of 1 samples at leaf node
								else:
									pixels_high.append((9, 13))
									if features[10][11] <= 78.5:
										pixels_low.append((10, 11))
										ans = 3										 # approximately 2 were 3 out of 2 samples at leaf node
									else:
										pixels_high.append((10, 11))
										if features[16][7] <= 126.5:
											pixels_low.append((16, 7))
											ans = 6											 # approximately 2 were 6 out of 2 samples at leaf node
										else:
											pixels_high.append((16, 7))
											if features[8][14] <= 153.5:
												pixels_low.append((8, 14))
												ans = 8												 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												pixels_high.append((8, 14))
												ans = 4												 # approximately 2 were 4 out of 2 samples at leaf node
						else:
							pixels_high.append((23, 9))
							if features[14][11] <= 26.5:
								pixels_low.append((14, 11))
								if features[19][10] <= 114.5:
									pixels_low.append((19, 10))
									if features[12][14] <= 253.0:
										pixels_low.append((12, 14))
										ans = 0										 # approximately 1 were 0 out of 1 samples at leaf node
									else:
										pixels_high.append((12, 14))
										ans = 3										 # approximately 1 were 3 out of 1 samples at leaf node
								else:
									pixels_high.append((19, 10))
									ans = 8									 # approximately 5 were 8 out of 5 samples at leaf node
							else:
								pixels_high.append((14, 11))
								if features[20][17] <= 69.0:
									pixels_low.append((20, 17))
									if features[17][13] <= 56.5:
										pixels_low.append((17, 13))
										ans = 5										 # approximately 71 were 5 out of 71 samples at leaf node
									else:
										pixels_high.append((17, 13))
										ans = 8										 # approximately 1 were 8 out of 1 samples at leaf node
								else:
									pixels_high.append((20, 17))
									ans = 0									 # approximately 1 were 0 out of 1 samples at leaf node
					else:
						pixels_high.append((20, 13))
						if features[20][7] <= 87.5:
							pixels_low.append((20, 7))
							if features[16][9] <= 198.0:
								pixels_low.append((16, 9))
								ans = 6								 # approximately 109 were 6 out of 109 samples at leaf node
							else:
								pixels_high.append((16, 9))
								if features[11][15] <= 252.0:
									pixels_low.append((11, 15))
									if features[13][20] <= 253.5:
										pixels_low.append((13, 20))
										ans = 6										 # approximately 6 were 6 out of 6 samples at leaf node
									else:
										pixels_high.append((13, 20))
										ans = 3										 # approximately 1 were 3 out of 1 samples at leaf node
								else:
									pixels_high.append((11, 15))
									if features[11][13] <= 246.0:
										pixels_low.append((11, 13))
										ans = 2										 # approximately 2 were 2 out of 2 samples at leaf node
									else:
										pixels_high.append((11, 13))
										if features[8][12] <= 109.5:
											pixels_low.append((8, 12))
											ans = 4											 # approximately 1 were 4 out of 1 samples at leaf node
										else:
											pixels_high.append((8, 12))
											if features[10][21] <= 84.5:
												pixels_low.append((10, 21))
												ans = 0												 # approximately 1 were 0 out of 1 samples at leaf node
											else:
												pixels_high.append((10, 21))
												ans = 5												 # approximately 1 were 5 out of 1 samples at leaf node
						else:
							pixels_high.append((20, 7))
							if features[14][19] <= 179.5:
								pixels_low.append((14, 19))
								if features[17][7] <= 87.5:
									pixels_low.append((17, 7))
									if features[9][12] <= 199.0:
										pixels_low.append((9, 12))
										ans = 8										 # approximately 1 were 8 out of 1 samples at leaf node
									else:
										pixels_high.append((9, 12))
										ans = 9										 # approximately 1 were 9 out of 1 samples at leaf node
								else:
									pixels_high.append((17, 7))
									ans = 1									 # approximately 1 were 1 out of 1 samples at leaf node
							else:
								pixels_high.append((14, 19))
								ans = 0								 # approximately 4 were 0 out of 4 samples at leaf node
				else:
					pixels_high.append((13, 23))
					if features[11][18] <= 2.5:
						pixels_low.append((11, 18))
						if features[9][17] <= 68.5:
							pixels_low.append((9, 17))
							if features[13][19] <= 30.0:
								pixels_low.append((13, 19))
								if features[11][10] <= 59.0:
									pixels_low.append((11, 10))
									if features[24][8] <= 12.5:
										pixels_low.append((24, 8))
										if features[13][10] <= 254.0:
											pixels_low.append((13, 10))
											if features[8][11] <= 250.0:
												pixels_low.append((8, 11))
												if features[9][12] <= 254.0:
													pixels_low.append((9, 12))
													ans = 3													 # approximately 227 were 3 out of 227 samples at leaf node
												else:
													pixels_high.append((9, 12))
													ans = 9													 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												pixels_high.append((8, 11))
												if features[7][9] <= 166.0:
													pixels_low.append((7, 9))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													pixels_high.append((7, 9))
													ans = 0													 # approximately 1 were 0 out of 1 samples at leaf node
										else:
											pixels_high.append((13, 10))
											ans = 1											 # approximately 2 were 1 out of 2 samples at leaf node
									else:
										pixels_high.append((24, 8))
										ans = 5										 # approximately 3 were 5 out of 3 samples at leaf node
								else:
									pixels_high.append((11, 10))
									if features[9][22] <= 39.0:
										pixels_low.append((9, 22))
										if features[14][25] <= 43.5:
											pixels_low.append((14, 25))
											if features[17][9] <= 121.5:
												pixels_low.append((17, 9))
												if features[18][12] <= 4.5:
													pixels_low.append((18, 12))
													if features[14][11] <= 2.0:
														pixels_low.append((14, 11))
														ans = 1														 # approximately 1 were 1 out of 1 samples at leaf node
													else:
														pixels_high.append((14, 11))
														if features[11][11] <= 252.5:
															pixels_low.append((11, 11))
															ans = 0															 # approximately 1 were 0 out of 1 samples at leaf node
														else:
															pixels_high.append((11, 11))
															ans = 5															 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													pixels_high.append((18, 12))
													ans = 8													 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												pixels_high.append((17, 9))
												ans = 3												 # approximately 5 were 3 out of 5 samples at leaf node
										else:
											pixels_high.append((14, 25))
											if features[16][9] <= 253.5:
												pixels_low.append((16, 9))
												ans = 9												 # approximately 5 were 9 out of 5 samples at leaf node
											else:
												pixels_high.append((16, 9))
												ans = 4												 # approximately 2 were 4 out of 2 samples at leaf node
									else:
										pixels_high.append((9, 22))
										if features[14][6] <= 213.5:
											pixels_low.append((14, 6))
											ans = 5											 # approximately 16 were 5 out of 16 samples at leaf node
										else:
											pixels_high.append((14, 6))
											if features[17][21] <= 210.0:
												pixels_low.append((17, 21))
												if features[20][17] <= 177.5:
													pixels_low.append((20, 17))
													if features[17][23] <= 180.0:
														pixels_low.append((17, 23))
														if features[18][6] <= 123.0:
															pixels_low.append((18, 6))
															ans = 1															 # approximately 1 were 1 out of 1 samples at leaf node
														else:
															pixels_high.append((18, 6))
															if features[10][16] <= 48.5:
																pixels_low.append((10, 16))
																ans = 9																 # approximately 1 were 9 out of 1 samples at leaf node
															else:
																pixels_high.append((10, 16))
																ans = 8																 # approximately 1 were 8 out of 1 samples at leaf node
													else:
														pixels_high.append((17, 23))
														ans = 3														 # approximately 2 were 3 out of 2 samples at leaf node
												else:
													pixels_high.append((20, 17))
													ans = 0													 # approximately 2 were 0 out of 2 samples at leaf node
											else:
												pixels_high.append((17, 21))
												ans = 5												 # approximately 3 were 5 out of 3 samples at leaf node
							else:
								pixels_high.append((13, 19))
								if features[14][11] <= 211.5:
									pixels_low.append((14, 11))
									if features[16][23] <= 17.5:
										pixels_low.append((16, 23))
										if features[12][25] <= 4.5:
											pixels_low.append((12, 25))
											if features[19][11] <= 15.5:
												pixels_low.append((19, 11))
												if features[15][6] <= 140.5:
													pixels_low.append((15, 6))
													if features[17][11] <= 236.5:
														pixels_low.append((17, 11))
														ans = 4														 # approximately 12 were 4 out of 12 samples at leaf node
													else:
														pixels_high.append((17, 11))
														ans = 9														 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													pixels_high.append((15, 6))
													if features[16][17] <= 11.0:
														pixels_low.append((16, 17))
														ans = 9														 # approximately 3 were 9 out of 3 samples at leaf node
													else:
														pixels_high.append((16, 17))
														if features[17][8] <= 36.0:
															pixels_low.append((17, 8))
															ans = 8															 # approximately 2 were 8 out of 2 samples at leaf node
														else:
															pixels_high.append((17, 8))
															if features[11][22] <= 15.5:
																pixels_low.append((11, 22))
																ans = 4																 # approximately 1 were 4 out of 1 samples at leaf node
															else:
																pixels_high.append((11, 22))
																if features[13][24] <= 4.5:
																	pixels_low.append((13, 24))
																	ans = 1																	 # approximately 1 were 1 out of 1 samples at leaf node
																else:
																	pixels_high.append((13, 24))
																	if features[14][20] <= 222.0:
																		pixels_low.append((14, 20))
																		ans = 7																		 # approximately 1 were 7 out of 1 samples at leaf node
																	else:
																		pixels_high.append((14, 20))
																		ans = 5																		 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												pixels_high.append((19, 11))
												ans = 3												 # approximately 7 were 3 out of 7 samples at leaf node
										else:
											pixels_high.append((12, 25))
											if features[14][13] <= 138.0:
												pixels_low.append((14, 13))
												if features[14][13] <= 4.0:
													pixels_low.append((14, 13))
													ans = 9													 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													pixels_high.append((14, 13))
													ans = 7													 # approximately 3 were 7 out of 3 samples at leaf node
											else:
												pixels_high.append((14, 13))
												ans = 9												 # approximately 15 were 9 out of 15 samples at leaf node
									else:
										pixels_high.append((16, 23))
										if features[13][17] <= 56.5:
											pixels_low.append((13, 17))
											if features[13][12] <= 127.5:
												pixels_low.append((13, 12))
												ans = 5												 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												pixels_high.append((13, 12))
												if features[18][22] <= 23.5:
													pixels_low.append((18, 22))
													ans = 9													 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													pixels_high.append((18, 22))
													ans = 3													 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											pixels_high.append((13, 17))
											ans = 8											 # approximately 38 were 8 out of 38 samples at leaf node
								else:
									pixels_high.append((14, 11))
									if features[18][8] <= 21.0:
										pixels_low.append((18, 8))
										if features[13][20] <= 181.0:
											pixels_low.append((13, 20))
											if features[14][5] <= 3.5:
												pixels_low.append((14, 5))
												ans = 9												 # approximately 3 were 9 out of 3 samples at leaf node
											else:
												pixels_high.append((14, 5))
												if features[14][21] <= 252.0:
													pixels_low.append((14, 21))
													if features[15][18] <= 127.0:
														pixels_low.append((15, 18))
														ans = 3														 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														pixels_high.append((15, 18))
														ans = 4														 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													pixels_high.append((14, 21))
													ans = 1													 # approximately 3 were 1 out of 3 samples at leaf node
										else:
											pixels_high.append((13, 20))
											ans = 1											 # approximately 36 were 1 out of 36 samples at leaf node
									else:
										pixels_high.append((18, 8))
										if features[14][9] <= 149.5:
											pixels_low.append((14, 9))
											ans = 3											 # approximately 4 were 3 out of 4 samples at leaf node
										else:
											pixels_high.append((14, 9))
											if features[22][13] <= 125.5:
												pixels_low.append((22, 13))
												if features[13][14] <= 212.0:
													pixels_low.append((13, 14))
													if features[12][15] <= 252.5:
														pixels_low.append((12, 15))
														ans = 5														 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														pixels_high.append((12, 15))
														ans = 7														 # approximately 1 were 7 out of 1 samples at leaf node
												else:
													pixels_high.append((13, 14))
													ans = 8													 # approximately 2 were 8 out of 2 samples at leaf node
											else:
												pixels_high.append((22, 13))
												ans = 0												 # approximately 2 were 0 out of 2 samples at leaf node
						else:
							pixels_high.append((9, 17))
							if features[9][14] <= 222.5:
								pixels_low.append((9, 14))
								if features[5][23] <= 76.5:
									pixels_low.append((5, 23))
									if features[19][16] <= 248.0:
										pixels_low.append((19, 16))
										if features[13][4] <= 253.5:
											pixels_low.append((13, 4))
											if features[23][21] <= 66.5:
												pixels_low.append((23, 21))
												if features[23][5] <= 228.5:
													pixels_low.append((23, 5))
													if features[22][10] <= 253.5:
														pixels_low.append((22, 10))
														ans = 8														 # approximately 83 were 8 out of 83 samples at leaf node
													else:
														pixels_high.append((22, 10))
														ans = 5														 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													pixels_high.append((23, 5))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												pixels_high.append((23, 21))
												ans = 2												 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											pixels_high.append((13, 4))
											ans = 3											 # approximately 1 were 3 out of 1 samples at leaf node
									else:
										pixels_high.append((19, 16))
										if features[15][11] <= 186.5:
											pixels_low.append((15, 11))
											ans = 2											 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											pixels_high.append((15, 11))
											ans = 4											 # approximately 1 were 4 out of 1 samples at leaf node
								else:
									pixels_high.append((5, 23))
									if features[7][19] <= 111.0:
										pixels_low.append((7, 19))
										ans = 3										 # approximately 3 were 3 out of 3 samples at leaf node
									else:
										pixels_high.append((7, 19))
										ans = 8										 # approximately 1 were 8 out of 1 samples at leaf node
							else:
								pixels_high.append((9, 14))
								if features[12][6] <= 160.5:
									pixels_low.append((12, 6))
									if features[24][8] <= 11.5:
										pixels_low.append((24, 8))
										if features[8][20] <= 130.0:
											pixels_low.append((8, 20))
											if features[16][11] <= 229.0:
												pixels_low.append((16, 11))
												ans = 9												 # approximately 2 were 9 out of 2 samples at leaf node
											else:
												pixels_high.append((16, 11))
												if features[20][15] <= 64.0:
													pixels_low.append((20, 15))
													ans = 4													 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													pixels_high.append((20, 15))
													ans = 3													 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											pixels_high.append((8, 20))
											ans = 0											 # approximately 3 were 0 out of 3 samples at leaf node
									else:
										pixels_high.append((24, 8))
										ans = 5										 # approximately 4 were 5 out of 4 samples at leaf node
								else:
									pixels_high.append((12, 6))
									ans = 8									 # approximately 4 were 8 out of 4 samples at leaf node
					else:
						pixels_high.append((11, 18))
						if features[14][10] <= 250.0:
							pixels_low.append((14, 10))
							if features[20][15] <= 3.5:
								pixels_low.append((20, 15))
								if features[23][20] <= 18.0:
									pixels_low.append((23, 20))
									if features[14][15] <= 22.0:
										pixels_low.append((14, 15))
										if features[15][19] <= 78.5:
											pixels_low.append((15, 19))
											ans = 2											 # approximately 3 were 2 out of 3 samples at leaf node
										else:
											pixels_high.append((15, 19))
											if features[14][5] <= 127.0:
												pixels_low.append((14, 5))
												if features[23][6] <= 38.0:
													pixels_low.append((23, 6))
													ans = 7													 # approximately 1 were 7 out of 1 samples at leaf node
												else:
													pixels_high.append((23, 6))
													if features[18][6] <= 17.5:
														pixels_low.append((18, 6))
														ans = 8														 # approximately 1 were 8 out of 1 samples at leaf node
													else:
														pixels_high.append((18, 6))
														ans = 6														 # approximately 1 were 6 out of 1 samples at leaf node
											else:
												pixels_high.append((14, 5))
												ans = 3												 # approximately 1 were 3 out of 1 samples at leaf node
									else:
										pixels_high.append((14, 15))
										if features[6][6] <= 17.5:
											pixels_low.append((6, 6))
											if features[4][22] <= 122.0:
												pixels_low.append((4, 22))
												if features[13][14] <= 6.5:
													pixels_low.append((13, 14))
													if features[14][5] <= 47.0:
														pixels_low.append((14, 5))
														if features[19][7] <= 34.5:
															pixels_low.append((19, 7))
															if features[17][24] <= 10.5:
																pixels_low.append((17, 24))
																ans = 7																 # approximately 1 were 7 out of 1 samples at leaf node
															else:
																pixels_high.append((17, 24))
																ans = 9																 # approximately 1 were 9 out of 1 samples at leaf node
														else:
															pixels_high.append((19, 7))
															ans = 4															 # approximately 2 were 4 out of 2 samples at leaf node
													else:
														pixels_high.append((14, 5))
														ans = 8														 # approximately 2 were 8 out of 2 samples at leaf node
												else:
													pixels_high.append((13, 14))
													if features[6][18] <= 156.5:
														pixels_low.append((6, 18))
														if features[10][4] <= 236.0:
															pixels_low.append((10, 4))
															if features[6][25] <= 29.0:
																pixels_low.append((6, 25))
																if features[11][4] <= 254.5:
																	pixels_low.append((11, 4))
																	if features[14][23] <= 0.5:
																		pixels_low.append((14, 23))
																		if features[16][10] <= 245.5:
																			pixels_low.append((16, 10))
																			if features[15][11] <= 244.0:
																				pixels_low.append((15, 11))
																				ans = 8																				 # approximately 25 were 8 out of 25 samples at leaf node
																			else:
																				pixels_high.append((15, 11))
																				ans = 3																				 # approximately 1 were 3 out of 1 samples at leaf node
																		else:
																			pixels_high.append((16, 10))
																			if features[16][7] <= 3.0:
																				pixels_low.append((16, 7))
																				ans = 2																				 # approximately 1 were 2 out of 1 samples at leaf node
																			else:
																				pixels_high.append((16, 7))
																				ans = 1																				 # approximately 3 were 1 out of 3 samples at leaf node
																	else:
																		pixels_high.append((14, 23))
																		ans = 8																		 # approximately 498 were 8 out of 498 samples at leaf node
																else:
																	pixels_high.append((11, 4))
																	ans = 3																	 # approximately 1 were 3 out of 1 samples at leaf node
															else:
																pixels_high.append((6, 25))
																ans = 3																 # approximately 1 were 3 out of 1 samples at leaf node
														else:
															pixels_high.append((10, 4))
															ans = 2															 # approximately 1 were 2 out of 1 samples at leaf node
													else:
														pixels_high.append((6, 18))
														ans = 5														 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												pixels_high.append((4, 22))
												ans = 3												 # approximately 2 were 3 out of 2 samples at leaf node
										else:
											pixels_high.append((6, 6))
											if features[9][14] <= 86.5:
												pixels_low.append((9, 14))
												ans = 2												 # approximately 2 were 2 out of 2 samples at leaf node
											else:
												pixels_high.append((9, 14))
												ans = 3												 # approximately 2 were 3 out of 2 samples at leaf node
								else:
									pixels_high.append((23, 20))
									ans = 2									 # approximately 6 were 2 out of 6 samples at leaf node
							else:
								pixels_high.append((20, 15))
								if features[13][14] <= 183.0:
									pixels_low.append((13, 14))
									ans = 4									 # approximately 4 were 4 out of 4 samples at leaf node
								else:
									pixels_high.append((13, 14))
									if features[18][6] <= 113.5:
										pixels_low.append((18, 6))
										ans = 6										 # approximately 4 were 6 out of 4 samples at leaf node
									else:
										pixels_high.append((18, 6))
										if features[9][15] <= 44.5:
											pixels_low.append((9, 15))
											ans = 8											 # approximately 3 were 8 out of 3 samples at leaf node
										else:
											pixels_high.append((9, 15))
											if features[10][12] <= 213.0:
												pixels_low.append((10, 12))
												if features[14][14] <= 252.5:
													pixels_low.append((14, 14))
													ans = 3													 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													pixels_high.append((14, 14))
													if features[13][10] <= 5.5:
														pixels_low.append((13, 10))
														ans = 9														 # approximately 1 were 9 out of 1 samples at leaf node
													else:
														pixels_high.append((13, 10))
														if features[17][20] <= 124.5:
															pixels_low.append((17, 20))
															ans = 2															 # approximately 1 were 2 out of 1 samples at leaf node
														else:
															pixels_high.append((17, 20))
															ans = 5															 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												pixels_high.append((10, 12))
												ans = 0												 # approximately 2 were 0 out of 2 samples at leaf node
						else:
							pixels_high.append((14, 10))
							if features[13][19] <= 233.5:
								pixels_low.append((13, 19))
								if features[17][7] <= 153.5:
									pixels_low.append((17, 7))
									if features[11][16] <= 57.0:
										pixels_low.append((11, 16))
										ans = 3										 # approximately 4 were 3 out of 4 samples at leaf node
									else:
										pixels_high.append((11, 16))
										if features[9][15] <= 36.0:
											pixels_low.append((9, 15))
											ans = 8											 # approximately 2 were 8 out of 2 samples at leaf node
										else:
											pixels_high.append((9, 15))
											if features[13][8] <= 234.0:
												pixels_low.append((13, 8))
												if features[13][15] <= 190.5:
													pixels_low.append((13, 15))
													ans = 4													 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													pixels_high.append((13, 15))
													ans = 2													 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												pixels_high.append((13, 8))
												ans = 5												 # approximately 2 were 5 out of 2 samples at leaf node
								else:
									pixels_high.append((17, 7))
									if features[17][4] <= 16.5:
										pixels_low.append((17, 4))
										ans = 8										 # approximately 19 were 8 out of 19 samples at leaf node
									else:
										pixels_high.append((17, 4))
										if features[14][9] <= 235.0:
											pixels_low.append((14, 9))
											ans = 2											 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											pixels_high.append((14, 9))
											if features[15][20] <= 126.5:
												pixels_low.append((15, 20))
												ans = 1												 # approximately 1 were 1 out of 1 samples at leaf node
											else:
												pixels_high.append((15, 20))
												ans = 0												 # approximately 1 were 0 out of 1 samples at leaf node
							else:
								pixels_high.append((13, 19))
								if features[20][7] <= 45.0:
									pixels_low.append((20, 7))
									if features[10][6] <= 126.0:
										pixels_low.append((10, 6))
										if features[8][12] <= 83.0:
											pixels_low.append((8, 12))
											ans = 1											 # approximately 63 were 1 out of 63 samples at leaf node
										else:
											pixels_high.append((8, 12))
											ans = 7											 # approximately 1 were 7 out of 1 samples at leaf node
									else:
										pixels_high.append((10, 6))
										ans = 2										 # approximately 2 were 2 out of 2 samples at leaf node
								else:
									pixels_high.append((20, 7))
									if features[9][15] <= 46.5:
										pixels_low.append((9, 15))
										if features[11][12] <= 66.5:
											pixels_low.append((11, 12))
											ans = 1											 # approximately 1 were 1 out of 1 samples at leaf node
										else:
											pixels_high.append((11, 12))
											ans = 8											 # approximately 5 were 8 out of 5 samples at leaf node
									else:
										pixels_high.append((9, 15))
										if features[17][18] <= 126.0:
											pixels_low.append((17, 18))
											ans = 6											 # approximately 2 were 6 out of 2 samples at leaf node
										else:
											pixels_high.append((17, 18))
											ans = 0											 # approximately 2 were 0 out of 2 samples at leaf node
else:
	pixels_high.append((17, 14))
	if features[15][5] <= 0.5:
		pixels_low.append((15, 5))
		if features[15][8] <= 0.5:
			pixels_low.append((15, 8))
			if features[12][3] <= 0.5:
				pixels_low.append((12, 3))
				if features[9][15] <= 36.5:
					pixels_low.append((9, 15))
					if features[14][10] <= 72.5:
						pixels_low.append((14, 10))
						if features[9][21] <= 53.5:
							pixels_low.append((9, 21))
							if features[15][7] <= 19.0:
								pixels_low.append((15, 7))
								if features[23][12] <= 27.5:
									pixels_low.append((23, 12))
									if features[13][3] <= 4.5:
										pixels_low.append((13, 3))
										if features[14][11] <= 109.5:
											pixels_low.append((14, 11))
											if features[16][16] <= 7.5:
												pixels_low.append((16, 16))
												if features[12][7] <= 252.5:
													pixels_low.append((12, 7))
													if features[14][20] <= 43.0:
														pixels_low.append((14, 20))
														if features[22][22] <= 252.5:
															pixels_low.append((22, 22))
															if features[17][14] <= 18.5:
																pixels_low.append((17, 14))
																if features[19][14] <= 116.0:
																	pixels_low.append((19, 14))
																	ans = 1																	 # approximately 3 were 1 out of 3 samples at leaf node
																else:
																	pixels_high.append((19, 14))
																	if features[12][13] <= 127.0:
																		pixels_low.append((12, 13))
																		ans = 4																		 # approximately 1 were 4 out of 1 samples at leaf node
																	else:
																		pixels_high.append((12, 13))
																		ans = 7																		 # approximately 1 were 7 out of 1 samples at leaf node
															else:
																pixels_high.append((17, 14))
																if features[11][9] <= 239.5:
																	pixels_low.append((11, 9))
																	if features[23][10] <= 22.5:
																		pixels_low.append((23, 10))
																		ans = 4																		 # approximately 17 were 4 out of 17 samples at leaf node
																	else:
																		pixels_high.append((23, 10))
																		if features[17][11] <= 70.5:
																			pixels_low.append((17, 11))
																			ans = 6																			 # approximately 1 were 6 out of 1 samples at leaf node
																		else:
																			pixels_high.append((17, 11))
																			ans = 1																			 # approximately 1 were 1 out of 1 samples at leaf node
																else:
																	pixels_high.append((11, 9))
																	if features[17][17] <= 101.0:
																		pixels_low.append((17, 17))
																		ans = 3																		 # approximately 1 were 3 out of 1 samples at leaf node
																	else:
																		pixels_high.append((17, 17))
																		ans = 9																		 # approximately 1 were 9 out of 1 samples at leaf node
														else:
															pixels_high.append((22, 22))
															if features[16][23] <= 126.5:
																pixels_low.append((16, 23))
																ans = 9																 # approximately 2 were 9 out of 2 samples at leaf node
															else:
																pixels_high.append((16, 23))
																ans = 5																 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														pixels_high.append((14, 20))
														if features[10][15] <= 12.0:
															pixels_low.append((10, 15))
															ans = 5															 # approximately 3 were 5 out of 3 samples at leaf node
														else:
															pixels_high.append((10, 15))
															if features[20][14] <= 111.0:
																pixels_low.append((20, 14))
																if features[9][21] <= 15.5:
																	pixels_low.append((9, 21))
																	ans = 8																	 # approximately 1 were 8 out of 1 samples at leaf node
																else:
																	pixels_high.append((9, 21))
																	ans = 2																	 # approximately 1 were 2 out of 1 samples at leaf node
															else:
																pixels_high.append((20, 14))
																ans = 6																 # approximately 2 were 6 out of 2 samples at leaf node
												else:
													pixels_high.append((12, 7))
													ans = 3													 # approximately 8 were 3 out of 8 samples at leaf node
											else:
												pixels_high.append((16, 16))
												if features[9][20] <= 25.0:
													pixels_low.append((9, 20))
													if features[4][12] <= 86.5:
														pixels_low.append((4, 12))
														if features[22][18] <= 195.0:
															pixels_low.append((22, 18))
															if features[8][22] <= 2.0:
																pixels_low.append((8, 22))
																if features[12][5] <= 254.5:
																	pixels_low.append((12, 5))
																	if features[8][3] <= 11.5:
																		pixels_low.append((8, 3))
																		if features[14][6] <= 72.5:
																			pixels_low.append((14, 6))
																			if features[15][10] <= 226.0:
																				pixels_low.append((15, 10))
																				if features[9][25] <= 229.0:
																					pixels_low.append((9, 25))
																					if features[9][5] <= 254.5:
																						pixels_low.append((9, 5))
																						if features[16][18] <= 254.5:
																							pixels_low.append((16, 18))
																							ans = 4																							 # approximately 275 were 4 out of 275 samples at leaf node
																						else:
																							pixels_high.append((16, 18))
																							if features[9][12] <= 70.5:
																								pixels_low.append((9, 12))
																								ans = 9																								 # approximately 1 were 9 out of 1 samples at leaf node
																							else:
																								pixels_high.append((9, 12))
																								ans = 4																								 # approximately 5 were 4 out of 5 samples at leaf node
																					else:
																						pixels_high.append((9, 5))
																						if features[18][15] <= 23.5:
																							pixels_low.append((18, 15))
																							ans = 4																							 # approximately 1 were 4 out of 1 samples at leaf node
																						else:
																							pixels_high.append((18, 15))
																							ans = 8																							 # approximately 1 were 8 out of 1 samples at leaf node
																				else:
																					pixels_high.append((9, 25))
																					if features[21][7] <= 114.5:
																						pixels_low.append((21, 7))
																						ans = 4																						 # approximately 1 were 4 out of 1 samples at leaf node
																					else:
																						pixels_high.append((21, 7))
																						ans = 7																						 # approximately 1 were 7 out of 1 samples at leaf node
																			else:
																				pixels_high.append((15, 10))
																				if features[15][9] <= 24.5:
																					pixels_low.append((15, 9))
																					ans = 5																					 # approximately 1 were 5 out of 1 samples at leaf node
																				else:
																					pixels_high.append((15, 9))
																					ans = 4																					 # approximately 1 were 4 out of 1 samples at leaf node
																		else:
																			pixels_high.append((14, 6))
																			if features[11][5] <= 19.0:
																				pixels_low.append((11, 5))
																				if features[16][25] <= 148.5:
																					pixels_low.append((16, 25))
																					ans = 4																					 # approximately 24 were 4 out of 24 samples at leaf node
																				else:
																					pixels_high.append((16, 25))
																					ans = 9																					 # approximately 1 were 9 out of 1 samples at leaf node
																			else:
																				pixels_high.append((11, 5))
																				if features[13][22] <= 116.0:
																					pixels_low.append((13, 22))
																					ans = 9																					 # approximately 1 were 9 out of 1 samples at leaf node
																				else:
																					pixels_high.append((13, 22))
																					ans = 8																					 # approximately 3 were 8 out of 3 samples at leaf node
																	else:
																		pixels_high.append((8, 3))
																		ans = 6																		 # approximately 1 were 6 out of 1 samples at leaf node
																else:
																	pixels_high.append((12, 5))
																	if features[13][14] <= 154.0:
																		pixels_low.append((13, 14))
																		ans = 9																		 # approximately 1 were 9 out of 1 samples at leaf node
																	else:
																		pixels_high.append((13, 14))
																		ans = 3																		 # approximately 1 were 3 out of 1 samples at leaf node
															else:
																pixels_high.append((8, 22))
																if features[11][23] <= 187.5:
																	pixels_low.append((11, 23))
																	ans = 5																	 # approximately 1 were 5 out of 1 samples at leaf node
																else:
																	pixels_high.append((11, 23))
																	ans = 7																	 # approximately 1 were 7 out of 1 samples at leaf node
														else:
															pixels_high.append((22, 18))
															if features[8][10] <= 84.5:
																pixels_low.append((8, 10))
																ans = 3																 # approximately 2 were 3 out of 2 samples at leaf node
															else:
																pixels_high.append((8, 10))
																if features[19][22] <= 126.5:
																	pixels_low.append((19, 22))
																	if features[6][8] <= 155.5:
																		pixels_low.append((6, 8))
																		ans = 6																		 # approximately 1 were 6 out of 1 samples at leaf node
																	else:
																		pixels_high.append((6, 8))
																		ans = 4																		 # approximately 1 were 4 out of 1 samples at leaf node
																else:
																	pixels_high.append((19, 22))
																	ans = 5																	 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														pixels_high.append((4, 12))
														if features[4][8] <= 23.5:
															pixels_low.append((4, 8))
															ans = 7															 # approximately 5 were 7 out of 5 samples at leaf node
														else:
															pixels_high.append((4, 8))
															if features[17][13] <= 253.5:
																pixels_low.append((17, 13))
																ans = 4																 # approximately 4 were 4 out of 4 samples at leaf node
															else:
																pixels_high.append((17, 13))
																ans = 1																 # approximately 1 were 1 out of 1 samples at leaf node
												else:
													pixels_high.append((9, 20))
													if features[13][19] <= 233.0:
														pixels_low.append((13, 19))
														if features[19][9] <= 139.0:
															pixels_low.append((19, 9))
															if features[12][13] <= 24.5:
																pixels_low.append((12, 13))
																if features[16][11] <= 125.0:
																	pixels_low.append((16, 11))
																	ans = 9																	 # approximately 1 were 9 out of 1 samples at leaf node
																else:
																	pixels_high.append((16, 11))
																	ans = 6																	 # approximately 1 were 6 out of 1 samples at leaf node
															else:
																pixels_high.append((12, 13))
																ans = 5																 # approximately 2 were 5 out of 2 samples at leaf node
														else:
															pixels_high.append((19, 9))
															ans = 2															 # approximately 4 were 2 out of 4 samples at leaf node
													else:
														pixels_high.append((13, 19))
														ans = 4														 # approximately 4 were 4 out of 4 samples at leaf node
										else:
											pixels_high.append((14, 11))
											if features[7][11] <= 7.0:
												pixels_low.append((7, 11))
												if features[12][7] <= 252.5:
													pixels_low.append((12, 7))
													if features[17][17] <= 85.5:
														pixels_low.append((17, 17))
														ans = 4														 # approximately 5 were 4 out of 5 samples at leaf node
													else:
														pixels_high.append((17, 17))
														if features[18][13] <= 19.0:
															pixels_low.append((18, 13))
															ans = 8															 # approximately 2 were 8 out of 2 samples at leaf node
														else:
															pixels_high.append((18, 13))
															if features[17][19] <= 15.0:
																pixels_low.append((17, 19))
																ans = 5																 # approximately 1 were 5 out of 1 samples at leaf node
															else:
																pixels_high.append((17, 19))
																if features[18][21] <= 0.5:
																	pixels_low.append((18, 21))
																	ans = 7																	 # approximately 1 were 7 out of 1 samples at leaf node
																else:
																	pixels_high.append((18, 21))
																	ans = 6																	 # approximately 1 were 6 out of 1 samples at leaf node
												else:
													pixels_high.append((12, 7))
													ans = 3													 # approximately 5 were 3 out of 5 samples at leaf node
											else:
												pixels_high.append((7, 11))
												if features[13][14] <= 84.5:
													pixels_low.append((13, 14))
													if features[8][5] <= 33.5:
														pixels_low.append((8, 5))
														ans = 7														 # approximately 15 were 7 out of 15 samples at leaf node
													else:
														pixels_high.append((8, 5))
														ans = 5														 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													pixels_high.append((13, 14))
													if features[12][11] <= 112.0:
														pixels_low.append((12, 11))
														ans = 2														 # approximately 2 were 2 out of 2 samples at leaf node
													else:
														pixels_high.append((12, 11))
														if features[11][15] <= 18.5:
															pixels_low.append((11, 15))
															ans = 9															 # approximately 1 were 9 out of 1 samples at leaf node
														else:
															pixels_high.append((11, 15))
															ans = 8															 # approximately 1 were 8 out of 1 samples at leaf node
									else:
										pixels_high.append((13, 3))
										ans = 6										 # approximately 19 were 6 out of 19 samples at leaf node
								else:
									pixels_high.append((23, 12))
									if features[23][15] <= 16.0:
										pixels_low.append((23, 15))
										if features[8][13] <= 60.5:
											pixels_low.append((8, 13))
											if features[15][11] <= 44.5:
												pixels_low.append((15, 11))
												ans = 6												 # approximately 3 were 6 out of 3 samples at leaf node
											else:
												pixels_high.append((15, 11))
												if features[23][12] <= 238.0:
													pixels_low.append((23, 12))
													ans = 8													 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													pixels_high.append((23, 12))
													ans = 7													 # approximately 1 were 7 out of 1 samples at leaf node
										else:
											pixels_high.append((8, 13))
											ans = 4											 # approximately 4 were 4 out of 4 samples at leaf node
									else:
										pixels_high.append((23, 15))
										ans = 6										 # approximately 26 were 6 out of 26 samples at leaf node
							else:
								pixels_high.append((15, 7))
								if features[9][7] <= 7.5:
									pixels_low.append((9, 7))
									if features[16][15] <= 44.5:
										pixels_low.append((16, 15))
										if features[17][24] <= 1.0:
											pixels_low.append((17, 24))
											if features[14][12] <= 85.0:
												pixels_low.append((14, 12))
												if features[15][15] <= 70.0:
													pixels_low.append((15, 15))
													ans = 7													 # approximately 2 were 7 out of 2 samples at leaf node
												else:
													pixels_high.append((15, 15))
													ans = 3													 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												pixels_high.append((14, 12))
												ans = 5												 # approximately 2 were 5 out of 2 samples at leaf node
										else:
											pixels_high.append((17, 24))
											ans = 8											 # approximately 3 were 8 out of 3 samples at leaf node
									else:
										pixels_high.append((16, 15))
										if features[11][20] <= 213.5:
											pixels_low.append((11, 20))
											if features[17][5] <= 15.5:
												pixels_low.append((17, 5))
												if features[22][10] <= 189.0:
													pixels_low.append((22, 10))
													if features[20][17] <= 33.0:
														pixels_low.append((20, 17))
														if features[15][7] <= 22.0:
															pixels_low.append((15, 7))
															ans = 7															 # approximately 1 were 7 out of 1 samples at leaf node
														else:
															pixels_high.append((15, 7))
															if features[12][23] <= 213.0:
																pixels_low.append((12, 23))
																ans = 9																 # approximately 72 were 9 out of 72 samples at leaf node
															else:
																pixels_high.append((12, 23))
																if features[15][13] <= 4.5:
																	pixels_low.append((15, 13))
																	if features[15][20] <= 98.0:
																		pixels_low.append((15, 20))
																		ans = 7																		 # approximately 3 were 7 out of 3 samples at leaf node
																	else:
																		pixels_high.append((15, 20))
																		ans = 9																		 # approximately 2 were 9 out of 2 samples at leaf node
																else:
																	pixels_high.append((15, 13))
																	if features[12][16] <= 161.5:
																		pixels_low.append((12, 16))
																		ans = 9																		 # approximately 16 were 9 out of 16 samples at leaf node
																	else:
																		pixels_high.append((12, 16))
																		ans = 4																		 # approximately 1 were 4 out of 1 samples at leaf node
													else:
														pixels_high.append((20, 17))
														ans = 7														 # approximately 1 were 7 out of 1 samples at leaf node
												else:
													pixels_high.append((22, 10))
													ans = 8													 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												pixels_high.append((17, 5))
												ans = 4												 # approximately 2 were 4 out of 2 samples at leaf node
										else:
											pixels_high.append((11, 20))
											if features[9][25] <= 57.5:
												pixels_low.append((9, 25))
												ans = 8												 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												pixels_high.append((9, 25))
												ans = 7												 # approximately 2 were 7 out of 2 samples at leaf node
								else:
									pixels_high.append((9, 7))
									if features[13][14] <= 5.5:
										pixels_low.append((13, 14))
										if features[17][24] <= 29.5:
											pixels_low.append((17, 24))
											ans = 7											 # approximately 20 were 7 out of 20 samples at leaf node
										else:
											pixels_high.append((17, 24))
											if features[16][11] <= 6.5:
												pixels_low.append((16, 11))
												ans = 9												 # approximately 2 were 9 out of 2 samples at leaf node
											else:
												pixels_high.append((16, 11))
												ans = 5												 # approximately 1 were 5 out of 1 samples at leaf node
									else:
										pixels_high.append((13, 14))
										if features[10][19] <= 3.0:
											pixels_low.append((10, 19))
											if features[16][19] <= 49.5:
												pixels_low.append((16, 19))
												if features[15][24] <= 194.0:
													pixels_low.append((15, 24))
													ans = 3													 # approximately 8 were 3 out of 8 samples at leaf node
												else:
													pixels_high.append((15, 24))
													ans = 5													 # approximately 2 were 5 out of 2 samples at leaf node
											else:
												pixels_high.append((16, 19))
												if features[19][6] <= 126.0:
													pixels_low.append((19, 6))
													ans = 9													 # approximately 3 were 9 out of 3 samples at leaf node
												else:
													pixels_high.append((19, 6))
													ans = 5													 # approximately 2 were 5 out of 2 samples at leaf node
										else:
											pixels_high.append((10, 19))
											if features[24][12] <= 2.0:
												pixels_low.append((24, 12))
												ans = 8												 # approximately 4 were 8 out of 4 samples at leaf node
											else:
												pixels_high.append((24, 12))
												ans = 6												 # approximately 1 were 6 out of 1 samples at leaf node
						else:
							pixels_high.append((9, 21))
							if features[16][11] <= 194.0:
								pixels_low.append((16, 11))
								if features[14][16] <= 12.0:
									pixels_low.append((14, 16))
									if features[22][18] <= 7.5:
										pixels_low.append((22, 18))
										if features[10][10] <= 12.0:
											pixels_low.append((10, 10))
											ans = 3											 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											pixels_high.append((10, 10))
											ans = 5											 # approximately 9 were 5 out of 9 samples at leaf node
									else:
										pixels_high.append((22, 18))
										if features[17][13] <= 217.0:
											pixels_low.append((17, 13))
											ans = 3											 # approximately 2 were 3 out of 2 samples at leaf node
										else:
											pixels_high.append((17, 13))
											ans = 2											 # approximately 1 were 2 out of 1 samples at leaf node
								else:
									pixels_high.append((14, 16))
									if features[15][22] <= 28.5:
										pixels_low.append((15, 22))
										if features[10][11] <= 139.5:
											pixels_low.append((10, 11))
											if features[7][24] <= 2.0:
												pixels_low.append((7, 24))
												if features[14][20] <= 252.5:
													pixels_low.append((14, 20))
													if features[16][12] <= 222.5:
														pixels_low.append((16, 12))
														if features[14][17] <= 36.5:
															pixels_low.append((14, 17))
															if features[14][19] <= 56.0:
																pixels_low.append((14, 19))
																ans = 8																 # approximately 1 were 8 out of 1 samples at leaf node
															else:
																pixels_high.append((14, 19))
																ans = 6																 # approximately 1 were 6 out of 1 samples at leaf node
														else:
															pixels_high.append((14, 17))
															ans = 2															 # approximately 8 were 2 out of 8 samples at leaf node
													else:
														pixels_high.append((16, 12))
														ans = 1														 # approximately 4 were 1 out of 4 samples at leaf node
												else:
													pixels_high.append((14, 20))
													ans = 6													 # approximately 6 were 6 out of 6 samples at leaf node
											else:
												pixels_high.append((7, 24))
												ans = 7												 # approximately 6 were 7 out of 6 samples at leaf node
										else:
											pixels_high.append((10, 11))
											if features[17][6] <= 16.5:
												pixels_low.append((17, 6))
												ans = 4												 # approximately 7 were 4 out of 7 samples at leaf node
											else:
												pixels_high.append((17, 6))
												if features[12][16] <= 127.0:
													pixels_low.append((12, 16))
													ans = 9													 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													pixels_high.append((12, 16))
													ans = 8													 # approximately 1 were 8 out of 1 samples at leaf node
									else:
										pixels_high.append((15, 22))
										if features[13][14] <= 1.5:
											pixels_low.append((13, 14))
											ans = 2											 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											pixels_high.append((13, 14))
											ans = 8											 # approximately 10 were 8 out of 10 samples at leaf node
							else:
								pixels_high.append((16, 11))
								if features[11][13] <= 78.5:
									pixels_low.append((11, 13))
									if features[11][18] <= 23.5:
										pixels_low.append((11, 18))
										if features[10][18] <= 16.0:
											pixels_low.append((10, 18))
											ans = 6											 # approximately 3 were 6 out of 3 samples at leaf node
										else:
											pixels_high.append((10, 18))
											if features[8][20] <= 254.0:
												pixels_low.append((8, 20))
												ans = 5												 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												pixels_high.append((8, 20))
												ans = 2												 # approximately 1 were 2 out of 1 samples at leaf node
									else:
										pixels_high.append((11, 18))
										if features[18][15] <= 43.0:
											pixels_low.append((18, 15))
											ans = 1											 # approximately 168 were 1 out of 168 samples at leaf node
										else:
											pixels_high.append((18, 15))
											ans = 2											 # approximately 2 were 2 out of 2 samples at leaf node
								else:
									pixels_high.append((11, 13))
									if features[12][14] <= 252.5:
										pixels_low.append((12, 14))
										if features[7][22] <= 16.0:
											pixels_low.append((7, 22))
											if features[15][10] <= 2.5:
												pixels_low.append((15, 10))
												ans = 9												 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												pixels_high.append((15, 10))
												if features[10][16] <= 14.0:
													pixels_low.append((10, 16))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													pixels_high.append((10, 16))
													ans = 8													 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											pixels_high.append((7, 22))
											ans = 3											 # approximately 2 were 3 out of 2 samples at leaf node
									else:
										pixels_high.append((12, 14))
										ans = 4										 # approximately 4 were 4 out of 4 samples at leaf node
					else:
						pixels_high.append((14, 10))
						if features[13][14] <= 0.5:
							pixels_low.append((13, 14))
							if features[9][18] <= 3.5:
								pixels_low.append((9, 18))
								if features[13][5] <= 29.0:
									pixels_low.append((13, 5))
									if features[17][7] <= 147.0:
										pixels_low.append((17, 7))
										if features[22][19] <= 117.5:
											pixels_low.append((22, 19))
											if features[5][20] <= 1.5:
												pixels_low.append((5, 20))
												if features[7][6] <= 237.0:
													pixels_low.append((7, 6))
													if features[12][7] <= 247.0:
														pixels_low.append((12, 7))
														ans = 7														 # approximately 209 were 7 out of 209 samples at leaf node
													else:
														pixels_high.append((12, 7))
														if features[16][18] <= 237.0:
															pixels_low.append((16, 18))
															ans = 7															 # approximately 7 were 7 out of 7 samples at leaf node
														else:
															pixels_high.append((16, 18))
															ans = 9															 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													pixels_high.append((7, 6))
													if features[18][23] <= 111.0:
														pixels_low.append((18, 23))
														ans = 5														 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														pixels_high.append((18, 23))
														ans = 3														 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												pixels_high.append((5, 20))
												if features[21][8] <= 88.0:
													pixels_low.append((21, 8))
													ans = 3													 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													pixels_high.append((21, 8))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											pixels_high.append((22, 19))
											if features[20][14] <= 22.0:
												pixels_low.append((20, 14))
												ans = 2												 # approximately 2 were 2 out of 2 samples at leaf node
											else:
												pixels_high.append((20, 14))
												if features[13][10] <= 233.5:
													pixels_low.append((13, 10))
													ans = 7													 # approximately 1 were 7 out of 1 samples at leaf node
												else:
													pixels_high.append((13, 10))
													ans = 9													 # approximately 1 were 9 out of 1 samples at leaf node
									else:
										pixels_high.append((17, 7))
										ans = 5										 # approximately 2 were 5 out of 2 samples at leaf node
								else:
									pixels_high.append((13, 5))
									if features[8][10] <= 58.5:
										pixels_low.append((8, 10))
										ans = 3										 # approximately 6 were 3 out of 6 samples at leaf node
									else:
										pixels_high.append((8, 10))
										if features[13][4] <= 8.5:
											pixels_low.append((13, 4))
											ans = 9											 # approximately 1 were 9 out of 1 samples at leaf node
										else:
											pixels_high.append((13, 4))
											ans = 5											 # approximately 1 were 5 out of 1 samples at leaf node
							else:
								pixels_high.append((9, 18))
								if features[14][12] <= 121.5:
									pixels_low.append((14, 12))
									if features[15][16] <= 187.5:
										pixels_low.append((15, 16))
										if features[13][15] <= 65.5:
											pixels_low.append((13, 15))
											if features[8][14] <= 50.0:
												pixels_low.append((8, 14))
												if features[6][17] <= 24.0:
													pixels_low.append((6, 17))
													ans = 7													 # approximately 1 were 7 out of 1 samples at leaf node
												else:
													pixels_high.append((6, 17))
													if features[14][9] <= 121.0:
														pixels_low.append((14, 9))
														ans = 5														 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														pixels_high.append((14, 9))
														ans = 9														 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												pixels_high.append((8, 14))
												ans = 0												 # approximately 2 were 0 out of 2 samples at leaf node
										else:
											pixels_high.append((13, 15))
											ans = 8											 # approximately 2 were 8 out of 2 samples at leaf node
									else:
										pixels_high.append((15, 16))
										if features[2][9] <= 5.5:
											pixels_low.append((2, 9))
											ans = 2											 # approximately 5 were 2 out of 5 samples at leaf node
										else:
											pixels_high.append((2, 9))
											ans = 7											 # approximately 1 were 7 out of 1 samples at leaf node
								else:
									pixels_high.append((14, 12))
									ans = 5									 # approximately 7 were 5 out of 7 samples at leaf node
						else:
							pixels_high.append((13, 14))
							if features[6][19] <= 23.5:
								pixels_low.append((6, 19))
								if features[11][19] <= 13.5:
									pixels_low.append((11, 19))
									if features[19][15] <= 196.5:
										pixels_low.append((19, 15))
										if features[18][22] <= 73.5:
											pixels_low.append((18, 22))
											if features[11][12] <= 223.5:
												pixels_low.append((11, 12))
												if features[18][11] <= 10.5:
													pixels_low.append((18, 11))
													if features[8][13] <= 127.0:
														pixels_low.append((8, 13))
														if features[12][11] <= 62.5:
															pixels_low.append((12, 11))
															ans = 7															 # approximately 1 were 7 out of 1 samples at leaf node
														else:
															pixels_high.append((12, 11))
															if features[13][24] <= 17.0:
																pixels_low.append((13, 24))
																if features[18][12] <= 5.0:
																	pixels_low.append((18, 12))
																	ans = 2																	 # approximately 1 were 2 out of 1 samples at leaf node
																else:
																	pixels_high.append((18, 12))
																	ans = 4																	 # approximately 1 were 4 out of 1 samples at leaf node
															else:
																pixels_high.append((13, 24))
																ans = 3																 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														pixels_high.append((8, 13))
														ans = 5														 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													pixels_high.append((18, 11))
													ans = 9													 # approximately 4 were 9 out of 4 samples at leaf node
											else:
												pixels_high.append((11, 12))
												if features[13][26] <= 127.5:
													pixels_low.append((13, 26))
													ans = 4													 # approximately 6 were 4 out of 6 samples at leaf node
												else:
													pixels_high.append((13, 26))
													ans = 7													 # approximately 1 were 7 out of 1 samples at leaf node
										else:
											pixels_high.append((18, 22))
											if features[10][11] <= 251.5:
												pixels_low.append((10, 11))
												ans = 1												 # approximately 6 were 1 out of 6 samples at leaf node
											else:
												pixels_high.append((10, 11))
												ans = 3												 # approximately 1 were 3 out of 1 samples at leaf node
									else:
										pixels_high.append((19, 15))
										if features[15][10] <= 62.5:
											pixels_low.append((15, 10))
											if features[21][14] <= 209.0:
												pixels_low.append((21, 14))
												ans = 3												 # approximately 4 were 3 out of 4 samples at leaf node
											else:
												pixels_high.append((21, 14))
												ans = 7												 # approximately 1 were 7 out of 1 samples at leaf node
										else:
											pixels_high.append((15, 10))
											ans = 7											 # approximately 9 were 7 out of 9 samples at leaf node
								else:
									pixels_high.append((11, 19))
									if features[20][6] <= 248.5:
										pixels_low.append((20, 6))
										if features[23][17] <= 6.5:
											pixels_low.append((23, 17))
											if features[10][11] <= 82.5:
												pixels_low.append((10, 11))
												if features[7][18] <= 80.5:
													pixels_low.append((7, 18))
													if features[18][11] <= 34.5:
														pixels_low.append((18, 11))
														ans = 2														 # approximately 3 were 2 out of 3 samples at leaf node
													else:
														pixels_high.append((18, 11))
														if features[18][20] <= 54.0:
															pixels_low.append((18, 20))
															if features[13][14] <= 133.5:
																pixels_low.append((13, 14))
																ans = 8																 # approximately 1 were 8 out of 1 samples at leaf node
															else:
																pixels_high.append((13, 14))
																ans = 4																 # approximately 1 were 4 out of 1 samples at leaf node
														else:
															pixels_high.append((18, 20))
															ans = 3															 # approximately 2 were 3 out of 2 samples at leaf node
												else:
													pixels_high.append((7, 18))
													ans = 5													 # approximately 3 were 5 out of 3 samples at leaf node
											else:
												pixels_high.append((10, 11))
												if features[10][26] <= 7.0:
													pixels_low.append((10, 26))
													ans = 8													 # approximately 11 were 8 out of 11 samples at leaf node
												else:
													pixels_high.append((10, 26))
													ans = 7													 # approximately 1 were 7 out of 1 samples at leaf node
										else:
											pixels_high.append((23, 17))
											ans = 2											 # approximately 6 were 2 out of 6 samples at leaf node
									else:
										pixels_high.append((20, 6))
										if features[14][11] <= 253.5:
											pixels_low.append((14, 11))
											ans = 1											 # approximately 7 were 1 out of 7 samples at leaf node
										else:
											pixels_high.append((14, 11))
											ans = 6											 # approximately 1 were 6 out of 1 samples at leaf node
							else:
								pixels_high.append((6, 19))
								if features[9][17] <= 58.5:
									pixels_low.append((9, 17))
									ans = 5									 # approximately 17 were 5 out of 17 samples at leaf node
								else:
									pixels_high.append((9, 17))
									if features[19][14] <= 147.0:
										pixels_low.append((19, 14))
										ans = 8										 # approximately 3 were 8 out of 3 samples at leaf node
									else:
										pixels_high.append((19, 14))
										ans = 2										 # approximately 2 were 2 out of 2 samples at leaf node
				else:
					pixels_high.append((9, 15))
					if features[15][6] <= 86.5:
						pixels_low.append((15, 6))
						if features[9][3] <= 2.0:
							pixels_low.append((9, 3))
							if features[15][3] <= 3.0:
								pixels_low.append((15, 3))
								if features[15][10] <= 145.5:
									pixels_low.append((15, 10))
									if features[14][11] <= 126.5:
										pixels_low.append((14, 11))
										if features[7][3] <= 81.0:
											pixels_low.append((7, 3))
											if features[10][3] <= 10.5:
												pixels_low.append((10, 3))
												if features[5][20] <= 217.0:
													pixels_low.append((5, 20))
													if features[21][25] <= 219.5:
														pixels_low.append((21, 25))
														if features[16][2] <= 9.5:
															pixels_low.append((16, 2))
															if features[15][26] <= 32.0:
																pixels_low.append((15, 26))
																if features[17][26] <= 68.5:
																	pixels_low.append((17, 26))
																	if features[3][17] <= 204.5:
																		pixels_low.append((3, 17))
																		if features[23][18] <= 245.5:
																			pixels_low.append((23, 18))
																			if features[8][20] <= 242.0:
																				pixels_low.append((8, 20))
																				if features[26][13] <= 42.0:
																					pixels_low.append((26, 13))
																					if features[26][16] <= 66.0:
																						pixels_low.append((26, 16))
																						if features[6][22] <= 231.0:
																							pixels_low.append((6, 22))
																							if features[3][11] <= 253.5:
																								pixels_low.append((3, 11))
																								if features[23][13] <= 254.5:
																									pixels_low.append((23, 13))
																									if features[13][3] <= 109.0:
																										pixels_low.append((13, 3))
																										if features[23][2] <= 76.0:
																											pixels_low.append((23, 2))
																											if features[24][20] <= 225.0:
																												pixels_low.append((24, 20))
																												if features[15][7] <= 169.5:
																													pixels_low.append((15, 7))
																													if features[17][3] <= 23.5:
																														pixels_low.append((17, 3))
																														if features[7][21] <= 246.5:
																															pixels_low.append((7, 21))
																															if features[11][6] <= 253.5:
																																pixels_low.append((11, 6))
																																if features[15][6] <= 50.5:
																																	pixels_low.append((15, 6))
																																	if features[14][5] <= 93.0:
																																		pixels_low.append((14, 5))
																																		if features[13][4] <= 192.0:
																																			pixels_low.append((13, 4))
																																			if features[20][25] <= 192.0:
																																				pixels_low.append((20, 25))
																																				if features[16][25] <= 252.5:
																																					pixels_low.append((16, 25))
																																					if features[13][7] <= 254.5:
																																						pixels_low.append((13, 7))
																																						ans = 4																																						 # approximately 2199 were 4 out of 2199 samples at leaf node
																																					else:
																																						pixels_high.append((13, 7))
																																						if features[12][9] <= 185.5:
																																							pixels_low.append((12, 9))
																																							ans = 9																																							 # approximately 1 were 9 out of 1 samples at leaf node
																																						else:
																																							pixels_high.append((12, 9))
																																							ans = 4																																							 # approximately 16 were 4 out of 16 samples at leaf node
																																				else:
																																					pixels_high.append((16, 25))
																																					if features[12][12] <= 95.5:
																																						pixels_low.append((12, 12))
																																						ans = 4																																						 # approximately 13 were 4 out of 13 samples at leaf node
																																					else:
																																						pixels_high.append((12, 12))
																																						ans = 9																																						 # approximately 1 were 9 out of 1 samples at leaf node
																																			else:
																																				pixels_high.append((20, 25))
																																				if features[20][14] <= 180.0:
																																					pixels_low.append((20, 14))
																																					ans = 4																																					 # approximately 8 were 4 out of 8 samples at leaf node
																																				else:
																																					pixels_high.append((20, 14))
																																					ans = 9																																					 # approximately 1 were 9 out of 1 samples at leaf node
																																		else:
																																			pixels_high.append((13, 4))
																																			if features[9][22] <= 55.0:
																																				pixels_low.append((9, 22))
																																				ans = 4																																				 # approximately 2 were 4 out of 2 samples at leaf node
																																			else:
																																				pixels_high.append((9, 22))
																																				ans = 0																																				 # approximately 1 were 0 out of 1 samples at leaf node
																																	else:
																																		pixels_high.append((14, 5))
																																		if features[7][9] <= 84.5:
																																			pixels_low.append((7, 9))
																																			if features[17][6] <= 88.5:
																																				pixels_low.append((17, 6))
																																				if features[10][9] <= 253.5:
																																					pixels_low.append((10, 9))
																																					ans = 4																																					 # approximately 40 were 4 out of 40 samples at leaf node
																																				else:
																																					pixels_high.append((10, 9))
																																					ans = 6																																					 # approximately 1 were 6 out of 1 samples at leaf node
																																			else:
																																				pixels_high.append((17, 6))
																																				ans = 9																																				 # approximately 1 were 9 out of 1 samples at leaf node
																																		else:
																																			pixels_high.append((7, 9))
																																			ans = 9																																			 # approximately 2 were 9 out of 2 samples at leaf node
																																else:
																																	pixels_high.append((15, 6))
																																	if features[16][18] <= 13.5:
																																		pixels_low.append((16, 18))
																																		ans = 9																																		 # approximately 2 were 9 out of 2 samples at leaf node
																																	else:
																																		pixels_high.append((16, 18))
																																		ans = 4																																		 # approximately 12 were 4 out of 12 samples at leaf node
																															else:
																																pixels_high.append((11, 6))
																																if features[8][7] <= 163.5:
																																	pixels_low.append((8, 7))
																																	if features[21][13] <= 128.5:
																																		pixels_low.append((21, 13))
																																		if features[15][12] <= 232.0:
																																			pixels_low.append((15, 12))
																																			ans = 4																																			 # approximately 56 were 4 out of 56 samples at leaf node
																																		else:
																																			pixels_high.append((15, 12))
																																			ans = 9																																			 # approximately 1 were 9 out of 1 samples at leaf node
																																	else:
																																		pixels_high.append((21, 13))
																																		if features[21][20] <= 31.5:
																																			pixels_low.append((21, 20))
																																			if features[23][17] <= 108.0:
																																				pixels_low.append((23, 17))
																																				ans = 9																																				 # approximately 2 were 9 out of 2 samples at leaf node
																																			else:
																																				pixels_high.append((23, 17))
																																				ans = 6																																				 # approximately 1 were 6 out of 1 samples at leaf node
																																		else:
																																			pixels_high.append((21, 20))
																																			ans = 4																																			 # approximately 3 were 4 out of 3 samples at leaf node
																																else:
																																	pixels_high.append((8, 7))
																																	if features[22][10] <= 126.5:
																																		pixels_low.append((22, 10))
																																		if features[14][15] <= 149.5:
																																			pixels_low.append((14, 15))
																																			ans = 3																																			 # approximately 1 were 3 out of 1 samples at leaf node
																																		else:
																																			pixels_high.append((14, 15))
																																			ans = 5																																			 # approximately 1 were 5 out of 1 samples at leaf node
																																	else:
																																		pixels_high.append((22, 10))
																																		ans = 8																																		 # approximately 1 were 8 out of 1 samples at leaf node
																														else:
																															pixels_high.append((7, 21))
																															if features[7][21] <= 252.5:
																																pixels_low.append((7, 21))
																																ans = 0																																 # approximately 1 were 0 out of 1 samples at leaf node
																															else:
																																pixels_high.append((7, 21))
																																ans = 4																																 # approximately 1 were 4 out of 1 samples at leaf node
																													else:
																														pixels_high.append((17, 3))
																														if features[18][7] <= 140.0:
																															pixels_low.append((18, 7))
																															ans = 4																															 # approximately 2 were 4 out of 2 samples at leaf node
																														else:
																															pixels_high.append((18, 7))
																															if features[15][20] <= 78.5:
																																pixels_low.append((15, 20))
																																ans = 8																																 # approximately 1 were 8 out of 1 samples at leaf node
																															else:
																																pixels_high.append((15, 20))
																																ans = 0																																 # approximately 1 were 0 out of 1 samples at leaf node
																												else:
																													pixels_high.append((15, 7))
																													ans = 9																													 # approximately 1 were 9 out of 1 samples at leaf node
																											else:
																												pixels_high.append((24, 20))
																												ans = 9																												 # approximately 1 were 9 out of 1 samples at leaf node
																										else:
																											pixels_high.append((23, 2))
																											ans = 6																											 # approximately 1 were 6 out of 1 samples at leaf node
																									else:
																										pixels_high.append((13, 3))
																										ans = 6																										 # approximately 1 were 6 out of 1 samples at leaf node
																								else:
																									pixels_high.append((23, 13))
																									ans = 6																									 # approximately 1 were 6 out of 1 samples at leaf node
																							else:
																								pixels_high.append((3, 11))
																								ans = 8																								 # approximately 1 were 8 out of 1 samples at leaf node
																						else:
																							pixels_high.append((6, 22))
																							ans = 8																							 # approximately 1 were 8 out of 1 samples at leaf node
																					else:
																						pixels_high.append((26, 16))
																						ans = 2																						 # approximately 1 were 2 out of 1 samples at leaf node
																				else:
																					pixels_high.append((26, 13))
																					if features[12][16] <= 253.5:
																						pixels_low.append((12, 16))
																						ans = 4																						 # approximately 1 were 4 out of 1 samples at leaf node
																					else:
																						pixels_high.append((12, 16))
																						ans = 2																						 # approximately 2 were 2 out of 2 samples at leaf node
																			else:
																				pixels_high.append((8, 20))
																				if features[17][17] <= 47.0:
																					pixels_low.append((17, 17))
																					if features[21][7] <= 121.5:
																						pixels_low.append((21, 7))
																						if features[15][22] <= 124.0:
																							pixels_low.append((15, 22))
																							ans = 2																							 # approximately 1 were 2 out of 1 samples at leaf node
																						else:
																							pixels_high.append((15, 22))
																							ans = 6																							 # approximately 1 were 6 out of 1 samples at leaf node
																					else:
																						pixels_high.append((21, 7))
																						ans = 8																						 # approximately 3 were 8 out of 3 samples at leaf node
																				else:
																					pixels_high.append((17, 17))
																					if features[18][13] <= 11.5:
																						pixels_low.append((18, 13))
																						if features[5][17] <= 42.5:
																							pixels_low.append((5, 17))
																							ans = 5																							 # approximately 1 were 5 out of 1 samples at leaf node
																						else:
																							pixels_high.append((5, 17))
																							ans = 0																							 # approximately 1 were 0 out of 1 samples at leaf node
																					else:
																						pixels_high.append((18, 13))
																						ans = 4																						 # approximately 12 were 4 out of 12 samples at leaf node
																		else:
																			pixels_high.append((23, 18))
																			if features[9][11] <= 250.5:
																				pixels_low.append((9, 11))
																				if features[12][5] <= 80.5:
																					pixels_low.append((12, 5))
																					if features[14][15] <= 126.5:
																						pixels_low.append((14, 15))
																						ans = 0																						 # approximately 1 were 0 out of 1 samples at leaf node
																					else:
																						pixels_high.append((14, 15))
																						if features[17][15] <= 174.5:
																							pixels_low.append((17, 15))
																							ans = 5																							 # approximately 1 were 5 out of 1 samples at leaf node
																						else:
																							pixels_high.append((17, 15))
																							ans = 3																							 # approximately 1 were 3 out of 1 samples at leaf node
																				else:
																					pixels_high.append((12, 5))
																					ans = 6																					 # approximately 1 were 6 out of 1 samples at leaf node
																			else:
																				pixels_high.append((9, 11))
																				ans = 4																				 # approximately 2 were 4 out of 2 samples at leaf node
																	else:
																		pixels_high.append((3, 17))
																		ans = 2																		 # approximately 2 were 2 out of 2 samples at leaf node
																else:
																	pixels_high.append((17, 26))
																	if features[16][15] <= 147.5:
																		pixels_low.append((16, 15))
																		ans = 9																		 # approximately 3 were 9 out of 3 samples at leaf node
																	else:
																		pixels_high.append((16, 15))
																		ans = 4																		 # approximately 1 were 4 out of 1 samples at leaf node
															else:
																pixels_high.append((15, 26))
																if features[20][10] <= 75.5:
																	pixels_low.append((20, 10))
																	ans = 9																	 # approximately 3 were 9 out of 3 samples at leaf node
																else:
																	pixels_high.append((20, 10))
																	if features[18][18] <= 26.5:
																		pixels_low.append((18, 18))
																		ans = 4																		 # approximately 1 were 4 out of 1 samples at leaf node
																	else:
																		pixels_high.append((18, 18))
																		ans = 7																		 # approximately 1 were 7 out of 1 samples at leaf node
														else:
															pixels_high.append((16, 2))
															ans = 2															 # approximately 3 were 2 out of 3 samples at leaf node
													else:
														pixels_high.append((21, 25))
														if features[18][11] <= 205.5:
															pixels_low.append((18, 11))
															ans = 4															 # approximately 1 were 4 out of 1 samples at leaf node
														else:
															pixels_high.append((18, 11))
															ans = 9															 # approximately 4 were 9 out of 4 samples at leaf node
												else:
													pixels_high.append((5, 20))
													if features[18][18] <= 24.0:
														pixels_low.append((18, 18))
														if features[10][9] <= 80.5:
															pixels_low.append((10, 9))
															ans = 1															 # approximately 1 were 1 out of 1 samples at leaf node
														else:
															pixels_high.append((10, 9))
															if features[17][13] <= 138.5:
																pixels_low.append((17, 13))
																ans = 0																 # approximately 1 were 0 out of 1 samples at leaf node
															else:
																pixels_high.append((17, 13))
																ans = 4																 # approximately 1 were 4 out of 1 samples at leaf node
													else:
														pixels_high.append((18, 18))
														ans = 2														 # approximately 4 were 2 out of 4 samples at leaf node
											else:
												pixels_high.append((10, 3))
												if features[7][18] <= 127.0:
													pixels_low.append((7, 18))
													ans = 6													 # approximately 6 were 6 out of 6 samples at leaf node
												else:
													pixels_high.append((7, 18))
													ans = 4													 # approximately 1 were 4 out of 1 samples at leaf node
										else:
											pixels_high.append((7, 3))
											ans = 6											 # approximately 7 were 6 out of 7 samples at leaf node
									else:
										pixels_high.append((14, 11))
										if features[11][13] <= 237.0:
											pixels_low.append((11, 13))
											if features[11][11] <= 235.5:
												pixels_low.append((11, 11))
												if features[11][22] <= 126.0:
													pixels_low.append((11, 22))
													if features[13][15] <= 210.0:
														pixels_low.append((13, 15))
														if features[18][9] <= 252.5:
															pixels_low.append((18, 9))
															ans = 9															 # approximately 3 were 9 out of 3 samples at leaf node
														else:
															pixels_high.append((18, 9))
															ans = 4															 # approximately 1 were 4 out of 1 samples at leaf node
													else:
														pixels_high.append((13, 15))
														ans = 2														 # approximately 3 were 2 out of 3 samples at leaf node
												else:
													pixels_high.append((11, 22))
													ans = 8													 # approximately 4 were 8 out of 4 samples at leaf node
											else:
												pixels_high.append((11, 11))
												if features[17][11] <= 254.5:
													pixels_low.append((17, 11))
													ans = 7													 # approximately 7 were 7 out of 7 samples at leaf node
												else:
													pixels_high.append((17, 11))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											pixels_high.append((11, 13))
											if features[19][10] <= 23.5:
												pixels_low.append((19, 10))
												if features[20][16] <= 34.0:
													pixels_low.append((20, 16))
													ans = 5													 # approximately 2 were 5 out of 2 samples at leaf node
												else:
													pixels_high.append((20, 16))
													if features[19][24] <= 31.0:
														pixels_low.append((19, 24))
														if features[14][5] <= 73.5:
															pixels_low.append((14, 5))
															ans = 4															 # approximately 1 were 4 out of 1 samples at leaf node
														else:
															pixels_high.append((14, 5))
															ans = 6															 # approximately 1 were 6 out of 1 samples at leaf node
													else:
														pixels_high.append((19, 24))
														ans = 3														 # approximately 2 were 3 out of 2 samples at leaf node
											else:
												pixels_high.append((19, 10))
												if features[17][18] <= 253.5:
													pixels_low.append((17, 18))
													ans = 4													 # approximately 19 were 4 out of 19 samples at leaf node
												else:
													pixels_high.append((17, 18))
													ans = 7													 # approximately 1 were 7 out of 1 samples at leaf node
								else:
									pixels_high.append((15, 10))
									if features[13][14] <= 1.5:
										pixels_low.append((13, 14))
										if features[11][16] <= 143.0:
											pixels_low.append((11, 16))
											if features[21][12] <= 252.5:
												pixels_low.append((21, 12))
												ans = 7												 # approximately 30 were 7 out of 30 samples at leaf node
											else:
												pixels_high.append((21, 12))
												ans = 0												 # approximately 1 were 0 out of 1 samples at leaf node
										else:
											pixels_high.append((11, 16))
											if features[15][11] <= 213.5:
												pixels_low.append((15, 11))
												ans = 4												 # approximately 5 were 4 out of 5 samples at leaf node
											else:
												pixels_high.append((15, 11))
												if features[15][16] <= 253.5:
													pixels_low.append((15, 16))
													if features[18][11] <= 92.0:
														pixels_low.append((18, 11))
														ans = 2														 # approximately 1 were 2 out of 1 samples at leaf node
													else:
														pixels_high.append((18, 11))
														if features[16][17] <= 23.0:
															pixels_low.append((16, 17))
															ans = 5															 # approximately 1 were 5 out of 1 samples at leaf node
														else:
															pixels_high.append((16, 17))
															ans = 3															 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													pixels_high.append((15, 16))
													ans = 7													 # approximately 2 were 7 out of 2 samples at leaf node
									else:
										pixels_high.append((13, 14))
										if features[23][8] <= 3.5:
											pixels_low.append((23, 8))
											if features[14][10] <= 135.0:
												pixels_low.append((14, 10))
												if features[9][13] <= 3.5:
													pixels_low.append((9, 13))
													if features[9][21] <= 126.0:
														pixels_low.append((9, 21))
														ans = 2														 # approximately 1 were 2 out of 1 samples at leaf node
													else:
														pixels_high.append((9, 21))
														ans = 1														 # approximately 1 were 1 out of 1 samples at leaf node
												else:
													pixels_high.append((9, 13))
													ans = 4													 # approximately 14 were 4 out of 14 samples at leaf node
											else:
												pixels_high.append((14, 10))
												if features[14][21] <= 151.5:
													pixels_low.append((14, 21))
													if features[8][18] <= 9.5:
														pixels_low.append((8, 18))
														if features[16][16] <= 127.5:
															pixels_low.append((16, 16))
															if features[13][15] <= 252.5:
																pixels_low.append((13, 15))
																if features[22][12] <= 56.5:
																	pixels_low.append((22, 12))
																	if features[6][14] <= 86.0:
																		pixels_low.append((6, 14))
																		ans = 1																		 # approximately 1 were 1 out of 1 samples at leaf node
																	else:
																		pixels_high.append((6, 14))
																		if features[17][13] <= 253.0:
																			pixels_low.append((17, 13))
																			ans = 4																			 # approximately 1 were 4 out of 1 samples at leaf node
																		else:
																			pixels_high.append((17, 13))
																			ans = 9																			 # approximately 1 were 9 out of 1 samples at leaf node
																else:
																	pixels_high.append((22, 12))
																	ans = 5																	 # approximately 1 were 5 out of 1 samples at leaf node
															else:
																pixels_high.append((13, 15))
																ans = 3																 # approximately 2 were 3 out of 2 samples at leaf node
														else:
															pixels_high.append((16, 16))
															if features[6][6] <= 78.0:
																pixels_low.append((6, 6))
																ans = 9																 # approximately 11 were 9 out of 11 samples at leaf node
															else:
																pixels_high.append((6, 6))
																ans = 7																 # approximately 1 were 7 out of 1 samples at leaf node
													else:
														pixels_high.append((8, 18))
														if features[12][12] <= 13.5:
															pixels_low.append((12, 12))
															ans = 2															 # approximately 4 were 2 out of 4 samples at leaf node
														else:
															pixels_high.append((12, 12))
															if features[17][10] <= 216.0:
																pixels_low.append((17, 10))
																ans = 6																 # approximately 3 were 6 out of 3 samples at leaf node
															else:
																pixels_high.append((17, 10))
																if features[17][18] <= 95.5:
																	pixels_low.append((17, 18))
																	if features[22][24] <= 125.5:
																		pixels_low.append((22, 24))
																		ans = 8																		 # approximately 1 were 8 out of 1 samples at leaf node
																	else:
																		pixels_high.append((22, 24))
																		ans = 9																		 # approximately 1 were 9 out of 1 samples at leaf node
																else:
																	pixels_high.append((17, 18))
																	ans = 0																	 # approximately 2 were 0 out of 2 samples at leaf node
												else:
													pixels_high.append((14, 21))
													ans = 7													 # approximately 4 were 7 out of 4 samples at leaf node
										else:
											pixels_high.append((23, 8))
											if features[18][11] <= 111.5:
												pixels_low.append((18, 11))
												ans = 5												 # approximately 14 were 5 out of 14 samples at leaf node
											else:
												pixels_high.append((18, 11))
												if features[9][13] <= 13.0:
													pixels_low.append((9, 13))
													ans = 0													 # approximately 1 were 0 out of 1 samples at leaf node
												else:
													pixels_high.append((9, 13))
													if features[16][14] <= 210.5:
														pixels_low.append((16, 14))
														ans = 1														 # approximately 1 were 1 out of 1 samples at leaf node
													else:
														pixels_high.append((16, 14))
														if features[11][25] <= 78.5:
															pixels_low.append((11, 25))
															ans = 4															 # approximately 1 were 4 out of 1 samples at leaf node
														else:
															pixels_high.append((11, 25))
															ans = 8															 # approximately 1 were 8 out of 1 samples at leaf node
							else:
								pixels_high.append((15, 3))
								if features[18][5] <= 8.0:
									pixels_low.append((18, 5))
									ans = 6									 # approximately 42 were 6 out of 42 samples at leaf node
								else:
									pixels_high.append((18, 5))
									ans = 2									 # approximately 14 were 2 out of 14 samples at leaf node
						else:
							pixels_high.append((9, 3))
							if features[14][20] <= 30.0:
								pixels_low.append((14, 20))
								if features[10][22] <= 5.5:
									pixels_low.append((10, 22))
									ans = 4									 # approximately 5 were 4 out of 5 samples at leaf node
								else:
									pixels_high.append((10, 22))
									ans = 6									 # approximately 1 were 6 out of 1 samples at leaf node
							else:
								pixels_high.append((14, 20))
								ans = 6								 # approximately 76 were 6 out of 76 samples at leaf node
					else:
						pixels_high.append((15, 6))
						if features[22][7] <= 1.0:
							pixels_low.append((22, 7))
							if features[16][17] <= 12.5:
								pixels_low.append((16, 17))
								if features[17][6] <= 189.0:
									pixels_low.append((17, 6))
									if features[10][20] <= 2.5:
										pixels_low.append((10, 20))
										ans = 9										 # approximately 12 were 9 out of 12 samples at leaf node
									else:
										pixels_high.append((10, 20))
										if features[11][10] <= 86.5:
											pixels_low.append((11, 10))
											if features[23][17] <= 60.5:
												pixels_low.append((23, 17))
												if features[20][20] <= 87.0:
													pixels_low.append((20, 20))
													ans = 7													 # approximately 1 were 7 out of 1 samples at leaf node
												else:
													pixels_high.append((20, 20))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												pixels_high.append((23, 17))
												ans = 2												 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											pixels_high.append((11, 10))
											if features[19][16] <= 114.5:
												pixels_low.append((19, 16))
												ans = 4												 # approximately 1 were 4 out of 1 samples at leaf node
											else:
												pixels_high.append((19, 16))
												ans = 6												 # approximately 1 were 6 out of 1 samples at leaf node
								else:
									pixels_high.append((17, 6))
									if features[19][14] <= 155.0:
										pixels_low.append((19, 14))
										if features[17][22] <= 52.0:
											pixels_low.append((17, 22))
											if features[6][18] <= 126.5:
												pixels_low.append((6, 18))
												ans = 7												 # approximately 2 were 7 out of 2 samples at leaf node
											else:
												pixels_high.append((6, 18))
												ans = 2												 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											pixels_high.append((17, 22))
											ans = 5											 # approximately 2 were 5 out of 2 samples at leaf node
									else:
										pixels_high.append((19, 14))
										ans = 3										 # approximately 4 were 3 out of 4 samples at leaf node
							else:
								pixels_high.append((16, 17))
								if features[13][9] <= 197.0:
									pixels_low.append((13, 9))
									if features[11][6] <= 156.0:
										pixels_low.append((11, 6))
										if features[7][8] <= 254.5:
											pixels_low.append((7, 8))
											ans = 9											 # approximately 115 were 9 out of 115 samples at leaf node
										else:
											pixels_high.append((7, 8))
											ans = 3											 # approximately 1 were 3 out of 1 samples at leaf node
									else:
										pixels_high.append((11, 6))
										ans = 7										 # approximately 2 were 7 out of 2 samples at leaf node
								else:
									pixels_high.append((13, 9))
									ans = 4									 # approximately 2 were 4 out of 2 samples at leaf node
						else:
							pixels_high.append((22, 7))
							if features[9][12] <= 130.0:
								pixels_low.append((9, 12))
								if features[13][17] <= 29.5:
									pixels_low.append((13, 17))
									if features[22][8] <= 226.5:
										pixels_low.append((22, 8))
										ans = 3										 # approximately 1 were 3 out of 1 samples at leaf node
									else:
										pixels_high.append((22, 8))
										ans = 2										 # approximately 1 were 2 out of 1 samples at leaf node
								else:
									pixels_high.append((13, 17))
									ans = 8									 # approximately 2 were 8 out of 2 samples at leaf node
							else:
								pixels_high.append((9, 12))
								ans = 4								 # approximately 4 were 4 out of 4 samples at leaf node
			else:
				pixels_high.append((12, 3))
				if features[18][6] <= 5.0:
					pixels_low.append((18, 6))
					if features[15][20] <= 13.5:
						pixels_low.append((15, 20))
						if features[18][17] <= 237.5:
							pixels_low.append((18, 17))
							if features[9][6] <= 193.0:
								pixels_low.append((9, 6))
								if features[13][8] <= 9.0:
									pixels_low.append((13, 8))
									ans = 6									 # approximately 8 were 6 out of 8 samples at leaf node
								else:
									pixels_high.append((13, 8))
									if features[10][15] <= 50.5:
										pixels_low.append((10, 15))
										if features[12][3] <= 81.0:
											pixels_low.append((12, 3))
											ans = 0											 # approximately 1 were 0 out of 1 samples at leaf node
										else:
											pixels_high.append((12, 3))
											ans = 3											 # approximately 1 were 3 out of 1 samples at leaf node
									else:
										pixels_high.append((10, 15))
										ans = 4										 # approximately 1 were 4 out of 1 samples at leaf node
							else:
								pixels_high.append((9, 6))
								ans = 5								 # approximately 3 were 5 out of 3 samples at leaf node
						else:
							pixels_high.append((18, 17))
							ans = 4							 # approximately 5 were 4 out of 5 samples at leaf node
					else:
						pixels_high.append((15, 20))
						if features[14][9] <= 105.0:
							pixels_low.append((14, 9))
							if features[18][8] <= 93.5:
								pixels_low.append((18, 8))
								if features[12][22] <= 254.5:
									pixels_low.append((12, 22))
									if features[15][11] <= 254.5:
										pixels_low.append((15, 11))
										if features[15][4] <= 214.0:
											pixels_low.append((15, 4))
											if features[14][6] <= 241.0:
												pixels_low.append((14, 6))
												if features[15][22] <= 253.5:
													pixels_low.append((15, 22))
													ans = 6													 # approximately 555 were 6 out of 555 samples at leaf node
												else:
													pixels_high.append((15, 22))
													if features[12][22] <= 54.5:
														pixels_low.append((12, 22))
														ans = 6														 # approximately 4 were 6 out of 4 samples at leaf node
													else:
														pixels_high.append((12, 22))
														ans = 8														 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												pixels_high.append((14, 6))
												if features[7][9] <= 18.5:
													pixels_low.append((7, 9))
													ans = 6													 # approximately 1 were 6 out of 1 samples at leaf node
												else:
													pixels_high.append((7, 9))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											pixels_high.append((15, 4))
											ans = 5											 # approximately 1 were 5 out of 1 samples at leaf node
									else:
										pixels_high.append((15, 11))
										ans = 5										 # approximately 1 were 5 out of 1 samples at leaf node
								else:
									pixels_high.append((12, 22))
									ans = 4									 # approximately 1 were 4 out of 1 samples at leaf node
							else:
								pixels_high.append((18, 8))
								ans = 4								 # approximately 2 were 4 out of 2 samples at leaf node
						else:
							pixels_high.append((14, 9))
							ans = 1							 # approximately 2 were 1 out of 2 samples at leaf node
				else:
					pixels_high.append((18, 6))
					if features[13][22] <= 27.0:
						pixels_low.append((13, 22))
						ans = 2						 # approximately 22 were 2 out of 22 samples at leaf node
					else:
						pixels_high.append((13, 22))
						if features[11][9] <= 1.0:
							pixels_low.append((11, 9))
							ans = 3							 # approximately 3 were 3 out of 3 samples at leaf node
						else:
							pixels_high.append((11, 9))
							ans = 6							 # approximately 1 were 6 out of 1 samples at leaf node
		else:
			pixels_high.append((15, 8))
			if features[11][15] <= 0.5:
				pixels_low.append((11, 15))
				if features[13][13] <= 9.5:
					pixels_low.append((13, 13))
					if features[9][17] <= 4.5:
						pixels_low.append((9, 17))
						if features[12][5] <= 10.0:
							pixels_low.append((12, 5))
							if features[6][19] <= 7.5:
								pixels_low.append((6, 19))
								if features[18][5] <= 15.0:
									pixels_low.append((18, 5))
									if features[21][19] <= 25.5:
										pixels_low.append((21, 19))
										if features[10][16] <= 123.5:
											pixels_low.append((10, 16))
											if features[21][21] <= 122.0:
												pixels_low.append((21, 21))
												if features[8][18] <= 167.5:
													pixels_low.append((8, 18))
													if features[22][24] <= 42.0:
														pixels_low.append((22, 24))
														if features[22][17] <= 83.0:
															pixels_low.append((22, 17))
															if features[24][13] <= 112.5:
																pixels_low.append((24, 13))
																if features[14][12] <= 197.0:
																	pixels_low.append((14, 12))
																	if features[13][9] <= 10.5:
																		pixels_low.append((13, 9))
																		if features[13][11] <= 35.5:
																			pixels_low.append((13, 11))
																			if features[18][24] <= 70.0:
																				pixels_low.append((18, 24))
																				if features[17][22] <= 234.5:
																					pixels_low.append((17, 22))
																					if features[22][7] <= 230.0:
																						pixels_low.append((22, 7))
																						if features[22][15] <= 200.0:
																							pixels_low.append((22, 15))
																							if features[20][18] <= 160.0:
																								pixels_low.append((20, 18))
																								if features[17][14] <= 8.0:
																									pixels_low.append((17, 14))
																									if features[17][11] <= 191.0:
																										pixels_low.append((17, 11))
																										ans = 7																										 # approximately 3 were 7 out of 3 samples at leaf node
																									else:
																										pixels_high.append((17, 11))
																										ans = 2																										 # approximately 1 were 2 out of 1 samples at leaf node
																								else:
																									pixels_high.append((17, 14))
																									if features[15][10] <= 167.5:
																										pixels_low.append((15, 10))
																										ans = 7																										 # approximately 221 were 7 out of 221 samples at leaf node
																									else:
																										pixels_high.append((15, 10))
																										if features[15][19] <= 233.0:
																											pixels_low.append((15, 19))
																											ans = 3																											 # approximately 1 were 3 out of 1 samples at leaf node
																										else:
																											pixels_high.append((15, 19))
																											ans = 7																											 # approximately 3 were 7 out of 3 samples at leaf node
																							else:
																								pixels_high.append((20, 18))
																								ans = 2																								 # approximately 1 were 2 out of 1 samples at leaf node
																						else:
																							pixels_high.append((22, 15))
																							ans = 2																							 # approximately 1 were 2 out of 1 samples at leaf node
																					else:
																						pixels_high.append((22, 7))
																						ans = 3																						 # approximately 1 were 3 out of 1 samples at leaf node
																				else:
																					pixels_high.append((17, 22))
																					ans = 3																					 # approximately 2 were 3 out of 2 samples at leaf node
																			else:
																				pixels_high.append((18, 24))
																				if features[18][19] <= 2.0:
																					pixels_low.append((18, 19))
																					ans = 2																					 # approximately 6 were 2 out of 6 samples at leaf node
																				else:
																					pixels_high.append((18, 19))
																					if features[12][24] <= 23.5:
																						pixels_low.append((12, 24))
																						ans = 7																						 # approximately 4 were 7 out of 4 samples at leaf node
																					else:
																						pixels_high.append((12, 24))
																						ans = 3																						 # approximately 1 were 3 out of 1 samples at leaf node
																		else:
																			pixels_high.append((13, 11))
																			if features[16][8] <= 12.0:
																				pixels_low.append((16, 8))
																				ans = 7																				 # approximately 1 were 7 out of 1 samples at leaf node
																			else:
																				pixels_high.append((16, 8))
																				ans = 9																				 # approximately 10 were 9 out of 10 samples at leaf node
																	else:
																		pixels_high.append((13, 9))
																		if features[12][14] <= 148.5:
																			pixels_low.append((12, 14))
																			if features[11][5] <= 56.5:
																				pixels_low.append((11, 5))
																				if features[3][17] <= 19.0:
																					pixels_low.append((3, 17))
																					if features[11][14] <= 193.0:
																						pixels_low.append((11, 14))
																						if features[5][26] <= 145.0:
																							pixels_low.append((5, 26))
																							if features[13][14] <= 124.5:
																								pixels_low.append((13, 14))
																								if features[10][16] <= 41.5:
																									pixels_low.append((10, 16))
																									if features[13][12] <= 138.5:
																										pixels_low.append((13, 12))
																										if features[14][6] <= 202.5:
																											pixels_low.append((14, 6))
																											if features[7][24] <= 253.5:
																												pixels_low.append((7, 24))
																												if features[17][15] <= 23.5:
																													pixels_low.append((17, 15))
																													if features[20][15] <= 179.0:
																														pixels_low.append((20, 15))
																														if features[15][6] <= 238.0:
																															pixels_low.append((15, 6))
																															if features[8][15] <= 184.0:
																																pixels_low.append((8, 15))
																																if features[13][11] <= 90.0:
																																	pixels_low.append((13, 11))
																																	ans = 7																																	 # approximately 140 were 7 out of 140 samples at leaf node
																																else:
																																	pixels_high.append((13, 11))
																																	if features[17][9] <= 168.5:
																																		pixels_low.append((17, 9))
																																		ans = 9																																		 # approximately 2 were 9 out of 2 samples at leaf node
																																	else:
																																		pixels_high.append((17, 9))
																																		ans = 7																																		 # approximately 9 were 7 out of 9 samples at leaf node
																															else:
																																pixels_high.append((8, 15))
																																ans = 9																																 # approximately 1 were 9 out of 1 samples at leaf node
																														else:
																															pixels_high.append((15, 6))
																															ans = 9																															 # approximately 1 were 9 out of 1 samples at leaf node
																													else:
																														pixels_high.append((20, 15))
																														ans = 3																														 # approximately 1 were 3 out of 1 samples at leaf node
																												else:
																													pixels_high.append((17, 15))
																													if features[19][21] <= 253.5:
																														pixels_low.append((19, 21))
																														if features[12][15] <= 19.0:
																															pixels_low.append((12, 15))
																															ans = 7																															 # approximately 2457 were 7 out of 2457 samples at leaf node
																														else:
																															pixels_high.append((12, 15))
																															if features[12][26] <= 79.5:
																																pixels_low.append((12, 26))
																																ans = 7																																 # approximately 16 were 7 out of 16 samples at leaf node
																															else:
																																pixels_high.append((12, 26))
																																ans = 3																																 # approximately 1 were 3 out of 1 samples at leaf node
																													else:
																														pixels_high.append((19, 21))
																														if features[16][18] <= 207.0:
																															pixels_low.append((16, 18))
																															ans = 7																															 # approximately 7 were 7 out of 7 samples at leaf node
																														else:
																															pixels_high.append((16, 18))
																															ans = 2																															 # approximately 1 were 2 out of 1 samples at leaf node
																											else:
																												pixels_high.append((7, 24))
																												if features[12][9] <= 247.0:
																													pixels_low.append((12, 9))
																													ans = 2																													 # approximately 1 were 2 out of 1 samples at leaf node
																												else:
																													pixels_high.append((12, 9))
																													ans = 7																													 # approximately 5 were 7 out of 5 samples at leaf node
																										else:
																											pixels_high.append((14, 6))
																											if features[14][6] <= 209.0:
																												pixels_low.append((14, 6))
																												ans = 3																												 # approximately 2 were 3 out of 2 samples at leaf node
																											else:
																												pixels_high.append((14, 6))
																												if features[16][25] <= 251.0:
																													pixels_low.append((16, 25))
																													if features[13][15] <= 113.5:
																														pixels_low.append((13, 15))
																														ans = 7																														 # approximately 67 were 7 out of 67 samples at leaf node
																													else:
																														pixels_high.append((13, 15))
																														if features[10][22] <= 126.5:
																															pixels_low.append((10, 22))
																															ans = 3																															 # approximately 1 were 3 out of 1 samples at leaf node
																														else:
																															pixels_high.append((10, 22))
																															ans = 7																															 # approximately 4 were 7 out of 4 samples at leaf node
																												else:
																													pixels_high.append((16, 25))
																													if features[10][22] <= 133.0:
																														pixels_low.append((10, 22))
																														ans = 2																														 # approximately 1 were 2 out of 1 samples at leaf node
																													else:
																														pixels_high.append((10, 22))
																														ans = 7																														 # approximately 1 were 7 out of 1 samples at leaf node
																									else:
																										pixels_high.append((13, 12))
																										if features[12][10] <= 145.5:
																											pixels_low.append((12, 10))
																											ans = 9																											 # approximately 2 were 9 out of 2 samples at leaf node
																										else:
																											pixels_high.append((12, 10))
																											if features[12][6] <= 126.5:
																												pixels_low.append((12, 6))
																												ans = 7																												 # approximately 28 were 7 out of 28 samples at leaf node
																											else:
																												pixels_high.append((12, 6))
																												ans = 5																												 # approximately 1 were 5 out of 1 samples at leaf node
																								else:
																									pixels_high.append((10, 16))
																									if features[12][9] <= 159.0:
																										pixels_low.append((12, 9))
																										ans = 9																										 # approximately 1 were 9 out of 1 samples at leaf node
																									else:
																										pixels_high.append((12, 9))
																										ans = 7																										 # approximately 3 were 7 out of 3 samples at leaf node
																							else:
																								pixels_high.append((13, 14))
																								if features[9][12] <= 149.0:
																									pixels_low.append((9, 12))
																									ans = 7																									 # approximately 2 were 7 out of 2 samples at leaf node
																								else:
																									pixels_high.append((9, 12))
																									ans = 3																									 # approximately 1 were 3 out of 1 samples at leaf node
																						else:
																							pixels_high.append((5, 26))
																							if features[18][16] <= 49.0:
																								pixels_low.append((18, 16))
																								ans = 7																								 # approximately 6 were 7 out of 6 samples at leaf node
																							else:
																								pixels_high.append((18, 16))
																								if features[23][10] <= 1.5:
																									pixels_low.append((23, 10))
																									ans = 9																									 # approximately 1 were 9 out of 1 samples at leaf node
																								else:
																									pixels_high.append((23, 10))
																									ans = 4																									 # approximately 1 were 4 out of 1 samples at leaf node
																					else:
																						pixels_high.append((11, 14))
																						ans = 9																						 # approximately 1 were 9 out of 1 samples at leaf node
																				else:
																					pixels_high.append((3, 17))
																					ans = 3																					 # approximately 1 were 3 out of 1 samples at leaf node
																			else:
																				pixels_high.append((11, 5))
																				ans = 4																				 # approximately 1 were 4 out of 1 samples at leaf node
																		else:
																			pixels_high.append((12, 14))
																			ans = 8																			 # approximately 1 were 8 out of 1 samples at leaf node
																else:
																	pixels_high.append((14, 12))
																	if features[17][6] <= 51.5:
																		pixels_low.append((17, 6))
																		if features[9][6] <= 126.5:
																			pixels_low.append((9, 6))
																			ans = 7																			 # approximately 17 were 7 out of 17 samples at leaf node
																		else:
																			pixels_high.append((9, 6))
																			ans = 3																			 # approximately 1 were 3 out of 1 samples at leaf node
																	else:
																		pixels_high.append((17, 6))
																		if features[19][9] <= 104.5:
																			pixels_low.append((19, 9))
																			if features[7][11] <= 14.5:
																				pixels_low.append((7, 11))
																				ans = 3																				 # approximately 2 were 3 out of 2 samples at leaf node
																			else:
																				pixels_high.append((7, 11))
																				if features[15][23] <= 240.5:
																					pixels_low.append((15, 23))
																					ans = 8																					 # approximately 1 were 8 out of 1 samples at leaf node
																				else:
																					pixels_high.append((15, 23))
																					ans = 5																					 # approximately 1 were 5 out of 1 samples at leaf node
																		else:
																			pixels_high.append((19, 9))
																			ans = 9																			 # approximately 4 were 9 out of 4 samples at leaf node
															else:
																pixels_high.append((24, 13))
																ans = 2																 # approximately 2 were 2 out of 2 samples at leaf node
														else:
															pixels_high.append((22, 17))
															if features[18][11] <= 215.5:
																pixels_low.append((18, 11))
																ans = 2																 # approximately 5 were 2 out of 5 samples at leaf node
															else:
																pixels_high.append((18, 11))
																ans = 7																 # approximately 6 were 7 out of 6 samples at leaf node
													else:
														pixels_high.append((22, 24))
														if features[9][10] <= 126.5:
															pixels_low.append((9, 10))
															ans = 2															 # approximately 3 were 2 out of 3 samples at leaf node
														else:
															pixels_high.append((9, 10))
															ans = 7															 # approximately 1 were 7 out of 1 samples at leaf node
												else:
													pixels_high.append((8, 18))
													if features[12][12] <= 32.0:
														pixels_low.append((12, 12))
														if features[10][21] <= 34.5:
															pixels_low.append((10, 21))
															ans = 9															 # approximately 1 were 9 out of 1 samples at leaf node
														else:
															pixels_high.append((10, 21))
															ans = 0															 # approximately 1 were 0 out of 1 samples at leaf node
													else:
														pixels_high.append((12, 12))
														ans = 5														 # approximately 2 were 5 out of 2 samples at leaf node
											else:
												pixels_high.append((21, 21))
												ans = 2												 # approximately 3 were 2 out of 3 samples at leaf node
										else:
											pixels_high.append((10, 16))
											ans = 9											 # approximately 5 were 9 out of 5 samples at leaf node
									else:
										pixels_high.append((21, 19))
										if features[13][16] <= 62.0:
											pixels_low.append((13, 16))
											if features[8][22] <= 5.5:
												pixels_low.append((8, 22))
												if features[16][8] <= 9.5:
													pixels_low.append((16, 8))
													ans = 2													 # approximately 2 were 2 out of 2 samples at leaf node
												else:
													pixels_high.append((16, 8))
													if features[21][21] <= 193.0:
														pixels_low.append((21, 21))
														ans = 7														 # approximately 19 were 7 out of 19 samples at leaf node
													else:
														pixels_high.append((21, 21))
														if features[11][6] <= 53.5:
															pixels_low.append((11, 6))
															ans = 2															 # approximately 1 were 2 out of 1 samples at leaf node
														else:
															pixels_high.append((11, 6))
															ans = 9															 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												pixels_high.append((8, 22))
												if features[15][22] <= 160.0:
													pixels_low.append((15, 22))
													if features[15][8] <= 117.5:
														pixels_low.append((15, 8))
														ans = 5														 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														pixels_high.append((15, 8))
														ans = 2														 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													pixels_high.append((15, 22))
													ans = 3													 # approximately 3 were 3 out of 3 samples at leaf node
										else:
											pixels_high.append((13, 16))
											if features[20][16] <= 45.0:
												pixels_low.append((20, 16))
												ans = 2												 # approximately 16 were 2 out of 16 samples at leaf node
											else:
												pixels_high.append((20, 16))
												if features[3][15] <= 127.5:
													pixels_low.append((3, 15))
													ans = 3													 # approximately 4 were 3 out of 4 samples at leaf node
												else:
													pixels_high.append((3, 15))
													ans = 9													 # approximately 1 were 9 out of 1 samples at leaf node
								else:
									pixels_high.append((18, 5))
									if features[17][10] <= 87.5:
										pixels_low.append((17, 10))
										if features[12][20] <= 0.5:
											pixels_low.append((12, 20))
											ans = 5											 # approximately 5 were 5 out of 5 samples at leaf node
										else:
											pixels_high.append((12, 20))
											if features[17][19] <= 7.0:
												pixels_low.append((17, 19))
												ans = 8												 # approximately 3 were 8 out of 3 samples at leaf node
											else:
												pixels_high.append((17, 19))
												if features[22][19] <= 36.0:
													pixels_low.append((22, 19))
													if features[22][4] <= 2.5:
														pixels_low.append((22, 4))
														if features[8][15] <= 93.5:
															pixels_low.append((8, 15))
															ans = 3															 # approximately 1 were 3 out of 1 samples at leaf node
														else:
															pixels_high.append((8, 15))
															if features[13][17] <= 36.0:
																pixels_low.append((13, 17))
																ans = 9																 # approximately 1 were 9 out of 1 samples at leaf node
															else:
																pixels_high.append((13, 17))
																ans = 6																 # approximately 1 were 6 out of 1 samples at leaf node
													else:
														pixels_high.append((22, 4))
														ans = 0														 # approximately 1 were 0 out of 1 samples at leaf node
												else:
													pixels_high.append((22, 19))
													ans = 4													 # approximately 1 were 4 out of 1 samples at leaf node
									else:
										pixels_high.append((17, 10))
										if features[13][9] <= 254.0:
											pixels_low.append((13, 9))
											ans = 1											 # approximately 11 were 1 out of 11 samples at leaf node
										else:
											pixels_high.append((13, 9))
											ans = 2											 # approximately 1 were 2 out of 1 samples at leaf node
							else:
								pixels_high.append((6, 19))
								if features[20][12] <= 75.5:
									pixels_low.append((20, 12))
									if features[14][11] <= 158.5:
										pixels_low.append((14, 11))
										if features[12][7] <= 0.5:
											pixels_low.append((12, 7))
											ans = 6											 # approximately 6 were 6 out of 6 samples at leaf node
										else:
											pixels_high.append((12, 7))
											if features[16][8] <= 230.5:
												pixels_low.append((16, 8))
												if features[22][7] <= 126.5:
													pixels_low.append((22, 7))
													ans = 2													 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													pixels_high.append((22, 7))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												pixels_high.append((16, 8))
												ans = 7												 # approximately 3 were 7 out of 3 samples at leaf node
									else:
										pixels_high.append((14, 11))
										if features[23][14] <= 58.0:
											pixels_low.append((23, 14))
											ans = 5											 # approximately 17 were 5 out of 17 samples at leaf node
										else:
											pixels_high.append((23, 14))
											ans = 0											 # approximately 1 were 0 out of 1 samples at leaf node
								else:
									pixels_high.append((20, 12))
									if features[21][7] <= 115.0:
										pixels_low.append((21, 7))
										ans = 9										 # approximately 8 were 9 out of 8 samples at leaf node
									else:
										pixels_high.append((21, 7))
										if features[7][14] <= 28.0:
											pixels_low.append((7, 14))
											ans = 2											 # approximately 2 were 2 out of 2 samples at leaf node
										else:
											pixels_high.append((7, 14))
											ans = 0											 # approximately 20 were 0 out of 20 samples at leaf node
						else:
							pixels_high.append((12, 5))
							if features[14][11] <= 162.5:
								pixels_low.append((14, 11))
								if features[10][24] <= 0.5:
									pixels_low.append((10, 24))
									if features[22][10] <= 29.0:
										pixels_low.append((22, 10))
										if features[5][23] <= 115.0:
											pixels_low.append((5, 23))
											if features[11][22] <= 2.5:
												pixels_low.append((11, 22))
												if features[16][22] <= 30.5:
													pixels_low.append((16, 22))
													if features[14][14] <= 37.5:
														pixels_low.append((14, 14))
														if features[5][7] <= 122.5:
															pixels_low.append((5, 7))
															ans = 2															 # approximately 1 were 2 out of 1 samples at leaf node
														else:
															pixels_high.append((5, 7))
															ans = 3															 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														pixels_high.append((14, 14))
														ans = 7														 # approximately 4 were 7 out of 4 samples at leaf node
												else:
													pixels_high.append((16, 22))
													if features[21][19] <= 172.0:
														pixels_low.append((21, 19))
														ans = 2														 # approximately 14 were 2 out of 14 samples at leaf node
													else:
														pixels_high.append((21, 19))
														ans = 7														 # approximately 1 were 7 out of 1 samples at leaf node
											else:
												pixels_high.append((11, 22))
												ans = 2												 # approximately 33 were 2 out of 33 samples at leaf node
										else:
											pixels_high.append((5, 23))
											ans = 3											 # approximately 1 were 3 out of 1 samples at leaf node
									else:
										pixels_high.append((22, 10))
										ans = 7										 # approximately 2 were 7 out of 2 samples at leaf node
								else:
									pixels_high.append((10, 24))
									if features[8][7] <= 161.5:
										pixels_low.append((8, 7))
										ans = 7										 # approximately 8 were 7 out of 8 samples at leaf node
									else:
										pixels_high.append((8, 7))
										if features[15][10] <= 157.0:
											pixels_low.append((15, 10))
											ans = 2											 # approximately 3 were 2 out of 3 samples at leaf node
										else:
											pixels_high.append((15, 10))
											ans = 3											 # approximately 1 were 3 out of 1 samples at leaf node
							else:
								pixels_high.append((14, 11))
								if features[14][15] <= 92.5:
									pixels_low.append((14, 15))
									if features[14][9] <= 22.0:
										pixels_low.append((14, 9))
										ans = 5										 # approximately 4 were 5 out of 4 samples at leaf node
									else:
										pixels_high.append((14, 9))
										if features[8][8] <= 245.0:
											pixels_low.append((8, 8))
											ans = 3											 # approximately 6 were 3 out of 6 samples at leaf node
										else:
											pixels_high.append((8, 8))
											if features[16][9] <= 126.5:
												pixels_low.append((16, 9))
												ans = 2												 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												pixels_high.append((16, 9))
												if features[19][15] <= 217.5:
													pixels_low.append((19, 15))
													ans = 0													 # approximately 1 were 0 out of 1 samples at leaf node
												else:
													pixels_high.append((19, 15))
													ans = 7													 # approximately 1 were 7 out of 1 samples at leaf node
								else:
									pixels_high.append((14, 15))
									ans = 1									 # approximately 4 were 1 out of 4 samples at leaf node
					else:
						pixels_high.append((9, 17))
						if features[8][15] <= 1.0:
							pixels_low.append((8, 15))
							if features[5][15] <= 18.5:
								pixels_low.append((5, 15))
								if features[9][20] <= 1.0:
									pixels_low.append((9, 20))
									if features[14][8] <= 58.5:
										pixels_low.append((14, 8))
										ans = 9										 # approximately 4 were 9 out of 4 samples at leaf node
									else:
										pixels_high.append((14, 8))
										if features[8][18] <= 251.5:
											pixels_low.append((8, 18))
											if features[16][15] <= 146.0:
												pixels_low.append((16, 15))
												if features[18][16] <= 49.5:
													pixels_low.append((18, 16))
													if features[14][10] <= 4.5:
														pixels_low.append((14, 10))
														ans = 3														 # approximately 3 were 3 out of 3 samples at leaf node
													else:
														pixels_high.append((14, 10))
														if features[17][10] <= 5.0:
															pixels_low.append((17, 10))
															ans = 8															 # approximately 1 were 8 out of 1 samples at leaf node
														else:
															pixels_high.append((17, 10))
															ans = 9															 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													pixels_high.append((18, 16))
													ans = 7													 # approximately 4 were 7 out of 4 samples at leaf node
											else:
												pixels_high.append((16, 15))
												if features[9][14] <= 93.0:
													pixels_low.append((9, 14))
													ans = 7													 # approximately 53 were 7 out of 53 samples at leaf node
												else:
													pixels_high.append((9, 14))
													ans = 9													 # approximately 1 were 9 out of 1 samples at leaf node
										else:
											pixels_high.append((8, 18))
											if features[10][9] <= 46.0:
												pixels_low.append((10, 9))
												ans = 2												 # approximately 4 were 2 out of 4 samples at leaf node
											else:
												pixels_high.append((10, 9))
												if features[17][10] <= 30.5:
													pixels_low.append((17, 10))
													ans = 3													 # approximately 2 were 3 out of 2 samples at leaf node
												else:
													pixels_high.append((17, 10))
													if features[8][12] <= 66.0:
														pixels_low.append((8, 12))
														ans = 7														 # approximately 2 were 7 out of 2 samples at leaf node
													else:
														pixels_high.append((8, 12))
														ans = 9														 # approximately 1 were 9 out of 1 samples at leaf node
								else:
									pixels_high.append((9, 20))
									if features[9][24] <= 52.0:
										pixels_low.append((9, 24))
										if features[6][24] <= 5.5:
											pixels_low.append((6, 24))
											if features[14][24] <= 13.5:
												pixels_low.append((14, 24))
												if features[12][17] <= 46.0:
													pixels_low.append((12, 17))
													if features[3][9] <= 127.5:
														pixels_low.append((3, 9))
														if features[16][7] <= 194.0:
															pixels_low.append((16, 7))
															ans = 0															 # approximately 1 were 0 out of 1 samples at leaf node
														else:
															pixels_high.append((16, 7))
															if features[19][14] <= 161.5:
																pixels_low.append((19, 14))
																ans = 3																 # approximately 1 were 3 out of 1 samples at leaf node
															else:
																pixels_high.append((19, 14))
																ans = 2																 # approximately 1 were 2 out of 1 samples at leaf node
													else:
														pixels_high.append((3, 9))
														ans = 7														 # approximately 1 were 7 out of 1 samples at leaf node
												else:
													pixels_high.append((12, 17))
													if features[11][23] <= 207.0:
														pixels_low.append((11, 23))
														ans = 2														 # approximately 51 were 2 out of 51 samples at leaf node
													else:
														pixels_high.append((11, 23))
														ans = 7														 # approximately 1 were 7 out of 1 samples at leaf node
											else:
												pixels_high.append((14, 24))
												if features[17][10] <= 108.5:
													pixels_low.append((17, 10))
													ans = 2													 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													pixels_high.append((17, 10))
													ans = 7													 # approximately 3 were 7 out of 3 samples at leaf node
										else:
											pixels_high.append((6, 24))
											ans = 7											 # approximately 4 were 7 out of 4 samples at leaf node
									else:
										pixels_high.append((9, 24))
										if features[8][20] <= 247.5:
											pixels_low.append((8, 20))
											ans = 7											 # approximately 9 were 7 out of 9 samples at leaf node
										else:
											pixels_high.append((8, 20))
											ans = 8											 # approximately 2 were 8 out of 2 samples at leaf node
							else:
								pixels_high.append((5, 15))
								if features[10][11] <= 251.0:
									pixels_low.append((10, 11))
									if features[6][8] <= 234.5:
										pixels_low.append((6, 8))
										ans = 9										 # approximately 38 were 9 out of 38 samples at leaf node
									else:
										pixels_high.append((6, 8))
										ans = 7										 # approximately 1 were 7 out of 1 samples at leaf node
								else:
									pixels_high.append((10, 11))
									if features[20][7] <= 126.0:
										pixels_low.append((20, 7))
										ans = 4										 # approximately 2 were 4 out of 2 samples at leaf node
									else:
										pixels_high.append((20, 7))
										ans = 9										 # approximately 1 were 9 out of 1 samples at leaf node
						else:
							pixels_high.append((8, 15))
							if features[13][7] <= 5.5:
								pixels_low.append((13, 7))
								if features[13][9] <= 179.5:
									pixels_low.append((13, 9))
									if features[16][7] <= 119.0:
										pixels_low.append((16, 7))
										if features[18][9] <= 179.0:
											pixels_low.append((18, 9))
											ans = 9											 # approximately 3 were 9 out of 3 samples at leaf node
										else:
											pixels_high.append((18, 9))
											if features[15][20] <= 52.0:
												pixels_low.append((15, 20))
												ans = 8												 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												pixels_high.append((15, 20))
												ans = 5												 # approximately 1 were 5 out of 1 samples at leaf node
									else:
										pixels_high.append((16, 7))
										ans = 4										 # approximately 20 were 4 out of 20 samples at leaf node
								else:
									pixels_high.append((13, 9))
									if features[11][13] <= 159.5:
										pixels_low.append((11, 13))
										if features[11][17] <= 35.0:
											pixels_low.append((11, 17))
											if features[14][7] <= 6.0:
												pixels_low.append((14, 7))
												ans = 7												 # approximately 10 were 7 out of 10 samples at leaf node
											else:
												pixels_high.append((14, 7))
												ans = 9												 # approximately 1 were 9 out of 1 samples at leaf node
										else:
											pixels_high.append((11, 17))
											if features[20][17] <= 25.5:
												pixels_low.append((20, 17))
												if features[24][7] <= 195.5:
													pixels_low.append((24, 7))
													if features[7][22] <= 81.0:
														pixels_low.append((7, 22))
														ans = 9														 # approximately 19 were 9 out of 19 samples at leaf node
													else:
														pixels_high.append((7, 22))
														ans = 8														 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													pixels_high.append((24, 7))
													if features[17][14] <= 189.0:
														pixels_low.append((17, 14))
														ans = 5														 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														pixels_high.append((17, 14))
														ans = 4														 # approximately 1 were 4 out of 1 samples at leaf node
											else:
												pixels_high.append((20, 17))
												ans = 4												 # approximately 4 were 4 out of 4 samples at leaf node
									else:
										pixels_high.append((11, 13))
										if features[19][17] <= 27.5:
											pixels_low.append((19, 17))
											if features[15][17] <= 113.0:
												pixels_low.append((15, 17))
												ans = 9												 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												pixels_high.append((15, 17))
												ans = 0												 # approximately 2 were 0 out of 2 samples at leaf node
										else:
											pixels_high.append((19, 17))
											ans = 6											 # approximately 13 were 6 out of 13 samples at leaf node
							else:
								pixels_high.append((13, 7))
								if features[12][17] <= 1.5:
									pixels_low.append((12, 17))
									if features[10][15] <= 37.5:
										pixels_low.append((10, 15))
										if features[14][21] <= 131.5:
											pixels_low.append((14, 21))
											if features[5][15] <= 174.5:
												pixels_low.append((5, 15))
												ans = 9												 # approximately 19 were 9 out of 19 samples at leaf node
											else:
												pixels_high.append((5, 15))
												ans = 3												 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											pixels_high.append((14, 21))
											if features[21][14] <= 60.0:
												pixels_low.append((21, 14))
												if features[18][9] <= 123.0:
													pixels_low.append((18, 9))
													ans = 3													 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													pixels_high.append((18, 9))
													ans = 7													 # approximately 2 were 7 out of 2 samples at leaf node
											else:
												pixels_high.append((21, 14))
												ans = 0												 # approximately 2 were 0 out of 2 samples at leaf node
									else:
										pixels_high.append((10, 15))
										if features[12][21] <= 26.5:
											pixels_low.append((12, 21))
											ans = 7											 # approximately 14 were 7 out of 14 samples at leaf node
										else:
											pixels_high.append((12, 21))
											ans = 0											 # approximately 7 were 0 out of 7 samples at leaf node
								else:
									pixels_high.append((12, 17))
									if features[22][16] <= 148.0:
										pixels_low.append((22, 16))
										if features[5][19] <= 97.0:
											pixels_low.append((5, 19))
											if features[22][5] <= 95.5:
												pixels_low.append((22, 5))
												if features[12][11] <= 253.5:
													pixels_low.append((12, 11))
													if features[18][5] <= 244.5:
														pixels_low.append((18, 5))
														if features[12][4] <= 101.5:
															pixels_low.append((12, 4))
															if features[21][19] <= 254.5:
																pixels_low.append((21, 19))
																if features[25][10] <= 127.0:
																	pixels_low.append((25, 10))
																	if features[20][7] <= 254.5:
																		pixels_low.append((20, 7))
																		if features[15][23] <= 254.5:
																			pixels_low.append((15, 23))
																			if features[19][7] <= 253.5:
																				pixels_low.append((19, 7))
																				ans = 9																				 # approximately 288 were 9 out of 288 samples at leaf node
																			else:
																				pixels_high.append((19, 7))
																				if features[12][6] <= 119.0:
																					pixels_low.append((12, 6))
																					ans = 9																					 # approximately 4 were 9 out of 4 samples at leaf node
																				else:
																					pixels_high.append((12, 6))
																					ans = 7																					 # approximately 1 were 7 out of 1 samples at leaf node
																		else:
																			pixels_high.append((15, 23))
																			if features[10][14] <= 6.0:
																				pixels_low.append((10, 14))
																				ans = 9																				 # approximately 3 were 9 out of 3 samples at leaf node
																			else:
																				pixels_high.append((10, 14))
																				ans = 4																				 # approximately 1 were 4 out of 1 samples at leaf node
																	else:
																		pixels_high.append((20, 7))
																		ans = 4																		 # approximately 1 were 4 out of 1 samples at leaf node
																else:
																	pixels_high.append((25, 10))
																	ans = 8																	 # approximately 1 were 8 out of 1 samples at leaf node
															else:
																pixels_high.append((21, 19))
																ans = 2																 # approximately 1 were 2 out of 1 samples at leaf node
														else:
															pixels_high.append((12, 4))
															ans = 0															 # approximately 1 were 0 out of 1 samples at leaf node
													else:
														pixels_high.append((18, 5))
														if features[19][24] <= 97.5:
															pixels_low.append((19, 24))
															ans = 6															 # approximately 1 were 6 out of 1 samples at leaf node
														else:
															pixels_high.append((19, 24))
															ans = 4															 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													pixels_high.append((12, 11))
													ans = 4													 # approximately 3 were 4 out of 3 samples at leaf node
											else:
												pixels_high.append((22, 5))
												if features[17][22] <= 40.0:
													pixels_low.append((17, 22))
													ans = 4													 # approximately 3 were 4 out of 3 samples at leaf node
												else:
													pixels_high.append((17, 22))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											pixels_high.append((5, 19))
											if features[23][10] <= 198.0:
												pixels_low.append((23, 10))
												ans = 2												 # approximately 3 were 2 out of 3 samples at leaf node
											else:
												pixels_high.append((23, 10))
												ans = 0												 # approximately 1 were 0 out of 1 samples at leaf node
									else:
										pixels_high.append((22, 16))
										if features[12][7] <= 37.5:
											pixels_low.append((12, 7))
											ans = 4											 # approximately 3 were 4 out of 3 samples at leaf node
										else:
											pixels_high.append((12, 7))
											if features[11][11] <= 18.0:
												pixels_low.append((11, 11))
												if features[14][7] <= 150.0:
													pixels_low.append((14, 7))
													ans = 2													 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													pixels_high.append((14, 7))
													ans = 7													 # approximately 1 were 7 out of 1 samples at leaf node
											else:
												pixels_high.append((11, 11))
												ans = 6												 # approximately 2 were 6 out of 2 samples at leaf node
				else:
					pixels_high.append((13, 13))
					if features[22][7] <= 3.5:
						pixels_low.append((22, 7))
						if features[15][17] <= 10.5:
							pixels_low.append((15, 17))
							if features[9][6] <= 1.5:
								pixels_low.append((9, 6))
								if features[17][10] <= 6.0:
									pixels_low.append((17, 10))
									if features[17][7] <= 3.5:
										pixels_low.append((17, 7))
										if features[14][5] <= 1.5:
											pixels_low.append((14, 5))
											if features[16][9] <= 129.0:
												pixels_low.append((16, 9))
												ans = 9												 # approximately 5 were 9 out of 5 samples at leaf node
											else:
												pixels_high.append((16, 9))
												ans = 5												 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											pixels_high.append((14, 5))
											ans = 3											 # approximately 6 were 3 out of 6 samples at leaf node
									else:
										pixels_high.append((17, 7))
										if features[13][16] <= 5.0:
											pixels_low.append((13, 16))
											if features[6][8] <= 134.5:
												pixels_low.append((6, 8))
												if features[15][6] <= 251.0:
													pixels_low.append((15, 6))
													ans = 5													 # approximately 59 were 5 out of 59 samples at leaf node
												else:
													pixels_high.append((15, 6))
													if features[15][25] <= 62.0:
														pixels_low.append((15, 25))
														ans = 5														 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														pixels_high.append((15, 25))
														ans = 9														 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												pixels_high.append((6, 8))
												if features[15][20] <= 84.5:
													pixels_low.append((15, 20))
													ans = 3													 # approximately 3 were 3 out of 3 samples at leaf node
												else:
													pixels_high.append((15, 20))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											pixels_high.append((13, 16))
											if features[12][12] <= 87.0:
												pixels_low.append((12, 12))
												ans = 2												 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												pixels_high.append((12, 12))
												if features[7][15] <= 103.5:
													pixels_low.append((7, 15))
													if features[14][15] <= 253.5:
														pixels_low.append((14, 15))
														ans = 9														 # approximately 1 were 9 out of 1 samples at leaf node
													else:
														pixels_high.append((14, 15))
														if features[12][23] <= 251.5:
															pixels_low.append((12, 23))
															ans = 4															 # approximately 1 were 4 out of 1 samples at leaf node
														else:
															pixels_high.append((12, 23))
															ans = 8															 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													pixels_high.append((7, 15))
													ans = 6													 # approximately 1 were 6 out of 1 samples at leaf node
								else:
									pixels_high.append((17, 10))
									if features[8][11] <= 57.0:
										pixels_low.append((8, 11))
										if features[12][17] <= 16.0:
											pixels_low.append((12, 17))
											if features[17][20] <= 253.5:
												pixels_low.append((17, 20))
												if features[22][9] <= 140.5:
													pixels_low.append((22, 9))
													if features[10][11] <= 237.5:
														pixels_low.append((10, 11))
														ans = 3														 # approximately 19 were 3 out of 19 samples at leaf node
													else:
														pixels_high.append((10, 11))
														ans = 9														 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													pixels_high.append((22, 9))
													ans = 5													 # approximately 2 were 5 out of 2 samples at leaf node
											else:
												pixels_high.append((17, 20))
												if features[7][19] <= 17.0:
													pixels_low.append((7, 19))
													ans = 9													 # approximately 2 were 9 out of 2 samples at leaf node
												else:
													pixels_high.append((7, 19))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											pixels_high.append((12, 17))
											if features[12][13] <= 155.0:
												pixels_low.append((12, 13))
												if features[9][18] <= 10.0:
													pixels_low.append((9, 18))
													if features[12][23] <= 86.0:
														pixels_low.append((12, 23))
														ans = 7														 # approximately 1 were 7 out of 1 samples at leaf node
													else:
														pixels_high.append((12, 23))
														ans = 1														 # approximately 2 were 1 out of 2 samples at leaf node
												else:
													pixels_high.append((9, 18))
													ans = 2													 # approximately 2 were 2 out of 2 samples at leaf node
											else:
												pixels_high.append((12, 13))
												if features[15][16] <= 143.5:
													pixels_low.append((15, 16))
													ans = 8													 # approximately 5 were 8 out of 5 samples at leaf node
												else:
													pixels_high.append((15, 16))
													ans = 4													 # approximately 1 were 4 out of 1 samples at leaf node
									else:
										pixels_high.append((8, 11))
										if features[11][10] <= 243.5:
											pixels_low.append((11, 10))
											if features[21][19] <= 216.0:
												pixels_low.append((21, 19))
												if features[10][9] <= 22.5:
													pixels_low.append((10, 9))
													ans = 4													 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													pixels_high.append((10, 9))
													ans = 9													 # approximately 20 were 9 out of 20 samples at leaf node
											else:
												pixels_high.append((21, 19))
												if features[20][14] <= 63.0:
													pixels_low.append((20, 14))
													ans = 2													 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													pixels_high.append((20, 14))
													ans = 5													 # approximately 2 were 5 out of 2 samples at leaf node
										else:
											pixels_high.append((11, 10))
											if features[12][13] <= 195.0:
												pixels_low.append((12, 13))
												ans = 7												 # approximately 7 were 7 out of 7 samples at leaf node
											else:
												pixels_high.append((12, 13))
												if features[21][15] <= 42.0:
													pixels_low.append((21, 15))
													ans = 5													 # approximately 3 were 5 out of 3 samples at leaf node
												else:
													pixels_high.append((21, 15))
													if features[8][14] <= 114.5:
														pixels_low.append((8, 14))
														ans = 3														 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														pixels_high.append((8, 14))
														ans = 0														 # approximately 1 were 0 out of 1 samples at leaf node
							else:
								pixels_high.append((9, 6))
								if features[9][10] <= 41.5:
									pixels_low.append((9, 10))
									if features[6][15] <= 87.5:
										pixels_low.append((6, 15))
										if features[13][17] <= 135.0:
											pixels_low.append((13, 17))
											if features[8][12] <= 253.5:
												pixels_low.append((8, 12))
												ans = 3												 # approximately 116 were 3 out of 116 samples at leaf node
											else:
												pixels_high.append((8, 12))
												ans = 9												 # approximately 1 were 9 out of 1 samples at leaf node
										else:
											pixels_high.append((13, 17))
											ans = 7											 # approximately 1 were 7 out of 1 samples at leaf node
									else:
										pixels_high.append((6, 15))
										if features[11][12] <= 208.0:
											pixels_low.append((11, 12))
											ans = 5											 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											pixels_high.append((11, 12))
											ans = 2											 # approximately 1 were 2 out of 1 samples at leaf node
								else:
									pixels_high.append((9, 10))
									if features[17][6] <= 1.0:
										pixels_low.append((17, 6))
										if features[19][19] <= 15.5:
											pixels_low.append((19, 19))
											if features[20][20] <= 13.0:
												pixels_low.append((20, 20))
												ans = 9												 # approximately 3 were 9 out of 3 samples at leaf node
											else:
												pixels_high.append((20, 20))
												ans = 8												 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											pixels_high.append((19, 19))
											if features[13][8] <= 101.0:
												pixels_low.append((13, 8))
												if features[13][20] <= 126.0:
													pixels_low.append((13, 20))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													pixels_high.append((13, 20))
													ans = 7													 # approximately 1 were 7 out of 1 samples at leaf node
											else:
												pixels_high.append((13, 8))
												ans = 3												 # approximately 9 were 3 out of 9 samples at leaf node
									else:
										pixels_high.append((17, 6))
										if features[9][11] <= 17.0:
											pixels_low.append((9, 11))
											if features[8][8] <= 252.5:
												pixels_low.append((8, 8))
												ans = 8												 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												pixels_high.append((8, 8))
												ans = 3												 # approximately 3 were 3 out of 3 samples at leaf node
										else:
											pixels_high.append((9, 11))
											if features[19][11] <= 186.5:
												pixels_low.append((19, 11))
												if features[15][23] <= 126.5:
													pixels_low.append((15, 23))
													ans = 3													 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													pixels_high.append((15, 23))
													ans = 5													 # approximately 16 were 5 out of 16 samples at leaf node
											else:
												pixels_high.append((19, 11))
												ans = 8												 # approximately 1 were 8 out of 1 samples at leaf node
						else:
							pixels_high.append((15, 17))
							if features[13][15] <= 153.0:
								pixels_low.append((13, 15))
								if features[14][10] <= 211.5:
									pixels_low.append((14, 10))
									if features[8][20] <= 39.5:
										pixels_low.append((8, 20))
										if features[14][7] <= 2.5:
											pixels_low.append((14, 7))
											if features[10][12] <= 165.5:
												pixels_low.append((10, 12))
												if features[10][12] <= 76.5:
													pixels_low.append((10, 12))
													if features[16][7] <= 227.0:
														pixels_low.append((16, 7))
														ans = 7														 # approximately 4 were 7 out of 4 samples at leaf node
													else:
														pixels_high.append((16, 7))
														if features[17][5] <= 170.0:
															pixels_low.append((17, 5))
															ans = 4															 # approximately 1 were 4 out of 1 samples at leaf node
														else:
															pixels_high.append((17, 5))
															ans = 1															 # approximately 1 were 1 out of 1 samples at leaf node
												else:
													pixels_high.append((10, 12))
													ans = 9													 # approximately 4 were 9 out of 4 samples at leaf node
											else:
												pixels_high.append((10, 12))
												ans = 4												 # approximately 8 were 4 out of 8 samples at leaf node
										else:
											pixels_high.append((14, 7))
											if features[9][7] <= 150.0:
												pixels_low.append((9, 7))
												if features[17][13] <= 7.5:
													pixels_low.append((17, 13))
													if features[17][8] <= 251.5:
														pixels_low.append((17, 8))
														ans = 5														 # approximately 4 were 5 out of 4 samples at leaf node
													else:
														pixels_high.append((17, 8))
														ans = 9														 # approximately 2 were 9 out of 2 samples at leaf node
												else:
													pixels_high.append((17, 13))
													if features[22][7] <= 1.0:
														pixels_low.append((22, 7))
														if features[18][5] <= 87.5:
															pixels_low.append((18, 5))
															if features[24][9] <= 193.0:
																pixels_low.append((24, 9))
																if features[22][24] <= 167.5:
																	pixels_low.append((22, 24))
																	if features[13][18] <= 254.5:
																		pixels_low.append((13, 18))
																		if features[13][13] <= 16.5:
																			pixels_low.append((13, 13))
																			if features[15][20] <= 103.5:
																				pixels_low.append((15, 20))
																				ans = 7																				 # approximately 2 were 7 out of 2 samples at leaf node
																			else:
																				pixels_high.append((15, 20))
																				ans = 9																				 # approximately 4 were 9 out of 4 samples at leaf node
																		else:
																			pixels_high.append((13, 13))
																			if features[10][6] <= 57.5:
																				pixels_low.append((10, 6))
																				if features[17][16] <= 254.5:
																					pixels_low.append((17, 16))
																					if features[15][17] <= 24.5:
																						pixels_low.append((15, 17))
																						if features[15][6] <= 143.5:
																							pixels_low.append((15, 6))
																							ans = 9																							 # approximately 6 were 9 out of 6 samples at leaf node
																						else:
																							pixels_high.append((15, 6))
																							ans = 5																							 # approximately 1 were 5 out of 1 samples at leaf node
																					else:
																						pixels_high.append((15, 17))
																						if features[15][21] <= 253.5:
																							pixels_low.append((15, 21))
																							ans = 9																							 # approximately 240 were 9 out of 240 samples at leaf node
																						else:
																							pixels_high.append((15, 21))
																							if features[11][8] <= 68.5:
																								pixels_low.append((11, 8))
																								ans = 4																								 # approximately 1 were 4 out of 1 samples at leaf node
																							else:
																								pixels_high.append((11, 8))
																								ans = 9																								 # approximately 12 were 9 out of 12 samples at leaf node
																				else:
																					pixels_high.append((17, 16))
																					if features[18][12] <= 4.5:
																						pixels_low.append((18, 12))
																						ans = 8																						 # approximately 1 were 8 out of 1 samples at leaf node
																					else:
																						pixels_high.append((18, 12))
																						ans = 9																						 # approximately 3 were 9 out of 3 samples at leaf node
																			else:
																				pixels_high.append((10, 6))
																				if features[18][12] <= 15.0:
																					pixels_low.append((18, 12))
																					ans = 7																					 # approximately 1 were 7 out of 1 samples at leaf node
																				else:
																					pixels_high.append((18, 12))
																					ans = 9																					 # approximately 2 were 9 out of 2 samples at leaf node
																	else:
																		pixels_high.append((13, 18))
																		ans = 4																		 # approximately 1 were 4 out of 1 samples at leaf node
																else:
																	pixels_high.append((22, 24))
																	ans = 4																	 # approximately 1 were 4 out of 1 samples at leaf node
															else:
																pixels_high.append((24, 9))
																ans = 4																 # approximately 1 were 4 out of 1 samples at leaf node
														else:
															pixels_high.append((18, 5))
															ans = 5															 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														pixels_high.append((22, 7))
														ans = 4														 # approximately 2 were 4 out of 2 samples at leaf node
											else:
												pixels_high.append((9, 7))
												if features[15][22] <= 252.5:
													pixels_low.append((15, 22))
													if features[16][23] <= 137.0:
														pixels_low.append((16, 23))
														if features[8][11] <= 126.5:
															pixels_low.append((8, 11))
															ans = 7															 # approximately 1 were 7 out of 1 samples at leaf node
														else:
															pixels_high.append((8, 11))
															ans = 4															 # approximately 1 were 4 out of 1 samples at leaf node
													else:
														pixels_high.append((16, 23))
														if features[10][24] <= 80.5:
															pixels_low.append((10, 24))
															ans = 8															 # approximately 6 were 8 out of 6 samples at leaf node
														else:
															pixels_high.append((10, 24))
															ans = 5															 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													pixels_high.append((15, 22))
													ans = 9													 # approximately 4 were 9 out of 4 samples at leaf node
									else:
										pixels_high.append((8, 20))
										if features[20][19] <= 60.5:
											pixels_low.append((20, 19))
											if features[14][15] <= 119.5:
												pixels_low.append((14, 15))
												if features[12][10] <= 1.5:
													pixels_low.append((12, 10))
													ans = 3													 # approximately 5 were 3 out of 5 samples at leaf node
												else:
													pixels_high.append((12, 10))
													ans = 5													 # approximately 4 were 5 out of 4 samples at leaf node
											else:
												pixels_high.append((14, 15))
												ans = 8												 # approximately 4 were 8 out of 4 samples at leaf node
										else:
											pixels_high.append((20, 19))
											ans = 2											 # approximately 4 were 2 out of 4 samples at leaf node
								else:
									pixels_high.append((14, 10))
									if features[18][15] <= 54.0:
										pixels_low.append((18, 15))
										if features[16][12] <= 243.5:
											pixels_low.append((16, 12))
											if features[10][21] <= 21.5:
												pixels_low.append((10, 21))
												if features[15][17] <= 79.0:
													pixels_low.append((15, 17))
													ans = 3													 # approximately 4 were 3 out of 4 samples at leaf node
												else:
													pixels_high.append((15, 17))
													if features[15][17] <= 194.5:
														pixels_low.append((15, 17))
														ans = 4														 # approximately 4 were 4 out of 4 samples at leaf node
													else:
														pixels_high.append((15, 17))
														if features[13][11] <= 241.5:
															pixels_low.append((13, 11))
															if features[19][12] <= 35.0:
																pixels_low.append((19, 12))
																if features[15][9] <= 163.0:
																	pixels_low.append((15, 9))
																	ans = 9																	 # approximately 1 were 9 out of 1 samples at leaf node
																else:
																	pixels_high.append((15, 9))
																	ans = 7																	 # approximately 1 were 7 out of 1 samples at leaf node
															else:
																pixels_high.append((19, 12))
																ans = 8																 # approximately 2 were 8 out of 2 samples at leaf node
														else:
															pixels_high.append((13, 11))
															ans = 1															 # approximately 3 were 1 out of 3 samples at leaf node
											else:
												pixels_high.append((10, 21))
												if features[18][16] <= 94.0:
													pixels_low.append((18, 16))
													ans = 5													 # approximately 6 were 5 out of 6 samples at leaf node
												else:
													pixels_high.append((18, 16))
													ans = 6													 # approximately 1 were 6 out of 1 samples at leaf node
										else:
											pixels_high.append((16, 12))
											if features[9][14] <= 234.0:
												pixels_low.append((9, 14))
												if features[19][10] <= 240.5:
													pixels_low.append((19, 10))
													if features[12][13] <= 26.5:
														pixels_low.append((12, 13))
														ans = 7														 # approximately 1 were 7 out of 1 samples at leaf node
													else:
														pixels_high.append((12, 13))
														ans = 9														 # approximately 16 were 9 out of 16 samples at leaf node
												else:
													pixels_high.append((19, 10))
													if features[11][22] <= 220.0:
														pixels_low.append((11, 22))
														ans = 4														 # approximately 1 were 4 out of 1 samples at leaf node
													else:
														pixels_high.append((11, 22))
														ans = 7														 # approximately 1 were 7 out of 1 samples at leaf node
											else:
												pixels_high.append((9, 14))
												if features[11][18] <= 44.5:
													pixels_low.append((11, 18))
													ans = 1													 # approximately 1 were 1 out of 1 samples at leaf node
												else:
													pixels_high.append((11, 18))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
									else:
										pixels_high.append((18, 15))
										if features[16][10] <= 209.0:
											pixels_low.append((16, 10))
											if features[5][9] <= 12.0:
												pixels_low.append((5, 9))
												if features[10][25] <= 90.0:
													pixels_low.append((10, 25))
													if features[15][11] <= 241.0:
														pixels_low.append((15, 11))
														if features[14][16] <= 2.0:
															pixels_low.append((14, 16))
															ans = 5															 # approximately 2 were 5 out of 2 samples at leaf node
														else:
															pixels_high.append((14, 16))
															if features[12][14] <= 108.0:
																pixels_low.append((12, 14))
																if features[12][9] <= 143.5:
																	pixels_low.append((12, 9))
																	ans = 6																	 # approximately 1 were 6 out of 1 samples at leaf node
																else:
																	pixels_high.append((12, 9))
																	ans = 1																	 # approximately 1 were 1 out of 1 samples at leaf node
															else:
																pixels_high.append((12, 14))
																ans = 2																 # approximately 1 were 2 out of 1 samples at leaf node
													else:
														pixels_high.append((15, 11))
														if features[13][20] <= 47.0:
															pixels_low.append((13, 20))
															ans = 9															 # approximately 1 were 9 out of 1 samples at leaf node
														else:
															pixels_high.append((13, 20))
															ans = 3															 # approximately 3 were 3 out of 3 samples at leaf node
												else:
													pixels_high.append((10, 25))
													ans = 7													 # approximately 2 were 7 out of 2 samples at leaf node
											else:
												pixels_high.append((5, 9))
												ans = 8												 # approximately 3 were 8 out of 3 samples at leaf node
										else:
											pixels_high.append((16, 10))
											if features[17][6] <= 27.5:
												pixels_low.append((17, 6))
												ans = 7												 # approximately 25 were 7 out of 25 samples at leaf node
											else:
												pixels_high.append((17, 6))
												ans = 9												 # approximately 1 were 9 out of 1 samples at leaf node
							else:
								pixels_high.append((13, 15))
								if features[11][12] <= 20.0:
									pixels_low.append((11, 12))
									if features[10][8] <= 16.5:
										pixels_low.append((10, 8))
										if features[18][12] <= 187.0:
											pixels_low.append((18, 12))
											ans = 1											 # approximately 39 were 1 out of 39 samples at leaf node
										else:
											pixels_high.append((18, 12))
											if features[14][5] <= 20.0:
												pixels_low.append((14, 5))
												if features[13][22] <= 120.0:
													pixels_low.append((13, 22))
													if features[13][13] <= 119.5:
														pixels_low.append((13, 13))
														ans = 7														 # approximately 1 were 7 out of 1 samples at leaf node
													else:
														pixels_high.append((13, 13))
														ans = 9														 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													pixels_high.append((13, 22))
													ans = 8													 # approximately 2 were 8 out of 2 samples at leaf node
											else:
												pixels_high.append((14, 5))
												ans = 3												 # approximately 2 were 3 out of 2 samples at leaf node
									else:
										pixels_high.append((10, 8))
										if features[13][18] <= 98.0:
											pixels_low.append((13, 18))
											if features[13][18] <= 35.5:
												pixels_low.append((13, 18))
												ans = 3												 # approximately 6 were 3 out of 6 samples at leaf node
											else:
												pixels_high.append((13, 18))
												ans = 1												 # approximately 2 were 1 out of 2 samples at leaf node
										else:
											pixels_high.append((13, 18))
											if features[19][18] <= 245.5:
												pixels_low.append((19, 18))
												ans = 7												 # approximately 28 were 7 out of 28 samples at leaf node
											else:
												pixels_high.append((19, 18))
												ans = 2												 # approximately 1 were 2 out of 1 samples at leaf node
								else:
									pixels_high.append((11, 12))
									if features[13][17] <= 10.5:
										pixels_low.append((13, 17))
										if features[11][6] <= 250.5:
											pixels_low.append((11, 6))
											ans = 9											 # approximately 6 were 9 out of 6 samples at leaf node
										else:
											pixels_high.append((11, 6))
											ans = 8											 # approximately 1 were 8 out of 1 samples at leaf node
									else:
										pixels_high.append((13, 17))
										if features[15][13] <= 252.5:
											pixels_low.append((15, 13))
											ans = 8											 # approximately 31 were 8 out of 31 samples at leaf node
										else:
											pixels_high.append((15, 13))
											if features[12][15] <= 66.0:
												pixels_low.append((12, 15))
												if features[11][12] <= 231.0:
													pixels_low.append((11, 12))
													ans = 4													 # approximately 3 were 4 out of 3 samples at leaf node
												else:
													pixels_high.append((11, 12))
													if features[11][25] <= 64.0:
														pixels_low.append((11, 25))
														ans = 1														 # approximately 2 were 1 out of 2 samples at leaf node
													else:
														pixels_high.append((11, 25))
														if features[21][14] <= 64.0:
															pixels_low.append((21, 14))
															ans = 9															 # approximately 1 were 9 out of 1 samples at leaf node
														else:
															pixels_high.append((21, 14))
															ans = 7															 # approximately 1 were 7 out of 1 samples at leaf node
											else:
												pixels_high.append((12, 15))
												ans = 8												 # approximately 3 were 8 out of 3 samples at leaf node
					else:
						pixels_high.append((22, 7))
						if features[19][11] <= 13.5:
							pixels_low.append((19, 11))
							if features[22][12] <= 9.5:
								pixels_low.append((22, 12))
								if features[12][16] <= 91.0:
									pixels_low.append((12, 16))
									if features[19][10] <= 236.0:
										pixels_low.append((19, 10))
										if features[24][11] <= 61.0:
											pixels_low.append((24, 11))
											if features[8][25] <= 194.5:
												pixels_low.append((8, 25))
												ans = 5												 # approximately 222 were 5 out of 222 samples at leaf node
											else:
												pixels_high.append((8, 25))
												if features[11][11] <= 192.5:
													pixels_low.append((11, 11))
													ans = 5													 # approximately 2 were 5 out of 2 samples at leaf node
												else:
													pixels_high.append((11, 11))
													ans = 9													 # approximately 1 were 9 out of 1 samples at leaf node
										else:
											pixels_high.append((24, 11))
											ans = 9											 # approximately 1 were 9 out of 1 samples at leaf node
									else:
										pixels_high.append((19, 10))
										ans = 8										 # approximately 1 were 8 out of 1 samples at leaf node
								else:
									pixels_high.append((12, 16))
									ans = 6									 # approximately 1 were 6 out of 1 samples at leaf node
							else:
								pixels_high.append((22, 12))
								if features[7][9] <= 45.0:
									pixels_low.append((7, 9))
									ans = 0									 # approximately 1 were 0 out of 1 samples at leaf node
								else:
									pixels_high.append((7, 9))
									ans = 8									 # approximately 3 were 8 out of 3 samples at leaf node
						else:
							pixels_high.append((19, 11))
							if features[13][16] <= 145.0:
								pixels_low.append((13, 16))
								if features[12][10] <= 6.0:
									pixels_low.append((12, 10))
									if features[24][9] <= 82.5:
										pixels_low.append((24, 9))
										ans = 3										 # approximately 14 were 3 out of 14 samples at leaf node
									else:
										pixels_high.append((24, 9))
										ans = 5										 # approximately 1 were 5 out of 1 samples at leaf node
								else:
									pixels_high.append((12, 10))
									if features[7][17] <= 187.0:
										pixels_low.append((7, 17))
										if features[16][13] <= 70.0:
											pixels_low.append((16, 13))
											if features[23][5] <= 104.0:
												pixels_low.append((23, 5))
												ans = 7												 # approximately 6 were 7 out of 6 samples at leaf node
											else:
												pixels_high.append((23, 5))
												ans = 4												 # approximately 1 were 4 out of 1 samples at leaf node
										else:
											pixels_high.append((16, 13))
											if features[15][11] <= 253.5:
												pixels_low.append((15, 11))
												if features[13][10] <= 77.0:
													pixels_low.append((13, 10))
													ans = 9													 # approximately 4 were 9 out of 4 samples at leaf node
												else:
													pixels_high.append((13, 10))
													if features[11][8] <= 144.0:
														pixels_low.append((11, 8))
														if features[10][23] <= 131.0:
															pixels_low.append((10, 23))
															ans = 2															 # approximately 1 were 2 out of 1 samples at leaf node
														else:
															pixels_high.append((10, 23))
															ans = 4															 # approximately 3 were 4 out of 3 samples at leaf node
													else:
														pixels_high.append((11, 8))
														ans = 3														 # approximately 3 were 3 out of 3 samples at leaf node
											else:
												pixels_high.append((15, 11))
												ans = 5												 # approximately 5 were 5 out of 5 samples at leaf node
									else:
										pixels_high.append((7, 17))
										ans = 0										 # approximately 10 were 0 out of 10 samples at leaf node
							else:
								pixels_high.append((13, 16))
								if features[7][25] <= 21.5:
									pixels_low.append((7, 25))
									if features[15][11] <= 221.0:
										pixels_low.append((15, 11))
										if features[14][17] <= 15.5:
											pixels_low.append((14, 17))
											ans = 7											 # approximately 1 were 7 out of 1 samples at leaf node
										else:
											pixels_high.append((14, 17))
											ans = 8											 # approximately 31 were 8 out of 31 samples at leaf node
									else:
										pixels_high.append((15, 11))
										ans = 7										 # approximately 1 were 7 out of 1 samples at leaf node
								else:
									pixels_high.append((7, 25))
									if features[18][17] <= 14.0:
										pixels_low.append((18, 17))
										ans = 9										 # approximately 3 were 9 out of 3 samples at leaf node
									else:
										pixels_high.append((18, 17))
										ans = 7										 # approximately 1 were 7 out of 1 samples at leaf node
			else:
				pixels_high.append((11, 15))
				if features[9][20] <= 0.5:
					pixels_low.append((9, 20))
					if features[9][11] <= 0.5:
						pixels_low.append((9, 11))
						if features[13][13] <= 178.5:
							pixels_low.append((13, 13))
							if features[6][12] <= 1.5:
								pixels_low.append((6, 12))
								if features[11][12] <= 7.0:
									pixels_low.append((11, 12))
									if features[19][19] <= 1.0:
										pixels_low.append((19, 19))
										if features[16][15] <= 205.0:
											pixels_low.append((16, 15))
											if features[16][20] <= 198.5:
												pixels_low.append((16, 20))
												if features[8][11] <= 143.5:
													pixels_low.append((8, 11))
													if features[10][8] <= 162.0:
														pixels_low.append((10, 8))
														if features[12][14] <= 85.5:
															pixels_low.append((12, 14))
															ans = 2															 # approximately 5 were 2 out of 5 samples at leaf node
														else:
															pixels_high.append((12, 14))
															if features[10][21] <= 79.5:
																pixels_low.append((10, 21))
																if features[16][25] <= 6.0:
																	pixels_low.append((16, 25))
																	if features[15][9] <= 67.0:
																		pixels_low.append((15, 9))
																		ans = 3																		 # approximately 1 were 3 out of 1 samples at leaf node
																	else:
																		pixels_high.append((15, 9))
																		ans = 6																		 # approximately 1 were 6 out of 1 samples at leaf node
																else:
																	pixels_high.append((16, 25))
																	if features[20][15] <= 4.5:
																		pixels_low.append((20, 15))
																		ans = 4																		 # approximately 1 were 4 out of 1 samples at leaf node
																	else:
																		pixels_high.append((20, 15))
																		ans = 7																		 # approximately 1 were 7 out of 1 samples at leaf node
															else:
																pixels_high.append((10, 21))
																ans = 8																 # approximately 2 were 8 out of 2 samples at leaf node
													else:
														pixels_high.append((10, 8))
														ans = 7														 # approximately 4 were 7 out of 4 samples at leaf node
												else:
													pixels_high.append((8, 11))
													ans = 9													 # approximately 4 were 9 out of 4 samples at leaf node
											else:
												pixels_high.append((16, 20))
												if features[8][10] <= 156.0:
													pixels_low.append((8, 10))
													ans = 3													 # approximately 13 were 3 out of 13 samples at leaf node
												else:
													pixels_high.append((8, 10))
													ans = 9													 # approximately 1 were 9 out of 1 samples at leaf node
										else:
											pixels_high.append((16, 15))
											if features[7][17] <= 253.5:
												pixels_low.append((7, 17))
												if features[7][22] <= 73.0:
													pixels_low.append((7, 22))
													if features[7][11] <= 176.5:
														pixels_low.append((7, 11))
														if features[25][16] <= 10.0:
															pixels_low.append((25, 16))
															if features[19][24] <= 78.5:
																pixels_low.append((19, 24))
																if features[14][5] <= 140.0:
																	pixels_low.append((14, 5))
																	if features[8][19] <= 126.0:
																		pixels_low.append((8, 19))
																		if features[17][15] <= 58.5:
																			pixels_low.append((17, 15))
																			if features[17][20] <= 77.0:
																				pixels_low.append((17, 20))
																				ans = 7																				 # approximately 3 were 7 out of 3 samples at leaf node
																			else:
																				pixels_high.append((17, 20))
																				ans = 3																				 # approximately 1 were 3 out of 1 samples at leaf node
																		else:
																			pixels_high.append((17, 15))
																			ans = 7																			 # approximately 138 were 7 out of 138 samples at leaf node
																	else:
																		pixels_high.append((8, 19))
																		ans = 3																		 # approximately 1 were 3 out of 1 samples at leaf node
																else:
																	pixels_high.append((14, 5))
																	if features[14][17] <= 126.5:
																		pixels_low.append((14, 17))
																		ans = 3																		 # approximately 1 were 3 out of 1 samples at leaf node
																	else:
																		pixels_high.append((14, 17))
																		ans = 4																		 # approximately 1 were 4 out of 1 samples at leaf node
															else:
																pixels_high.append((19, 24))
																if features[17][25] <= 20.5:
																	pixels_low.append((17, 25))
																	ans = 2																	 # approximately 1 were 2 out of 1 samples at leaf node
																else:
																	pixels_high.append((17, 25))
																	ans = 3																	 # approximately 1 were 3 out of 1 samples at leaf node
														else:
															pixels_high.append((25, 16))
															ans = 2															 # approximately 2 were 2 out of 2 samples at leaf node
													else:
														pixels_high.append((7, 11))
														ans = 9														 # approximately 2 were 9 out of 2 samples at leaf node
												else:
													pixels_high.append((7, 22))
													ans = 3													 # approximately 5 were 3 out of 5 samples at leaf node
											else:
												pixels_high.append((7, 17))
												if features[11][8] <= 254.5:
													pixels_low.append((11, 8))
													ans = 2													 # approximately 6 were 2 out of 6 samples at leaf node
												else:
													pixels_high.append((11, 8))
													ans = 7													 # approximately 1 were 7 out of 1 samples at leaf node
									else:
										pixels_high.append((19, 19))
										if features[17][22] <= 11.5:
											pixels_low.append((17, 22))
											if features[16][17] <= 1.0:
												pixels_low.append((16, 17))
												if features[21][19] <= 54.0:
													pixels_low.append((21, 19))
													ans = 3													 # approximately 4 were 3 out of 4 samples at leaf node
												else:
													pixels_high.append((21, 19))
													if features[14][7] <= 250.5:
														pixels_low.append((14, 7))
														if features[14][13] <= 106.0:
															pixels_low.append((14, 13))
															ans = 9															 # approximately 1 were 9 out of 1 samples at leaf node
														else:
															pixels_high.append((14, 13))
															ans = 5															 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														pixels_high.append((14, 7))
														ans = 2														 # approximately 2 were 2 out of 2 samples at leaf node
											else:
												pixels_high.append((16, 17))
												if features[7][10] <= 169.0:
													pixels_low.append((7, 10))
													if features[7][8] <= 253.5:
														pixels_low.append((7, 8))
														ans = 2														 # approximately 22 were 2 out of 22 samples at leaf node
													else:
														pixels_high.append((7, 8))
														ans = 3														 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													pixels_high.append((7, 10))
													ans = 7													 # approximately 2 were 7 out of 2 samples at leaf node
										else:
											pixels_high.append((17, 22))
											if features[9][18] <= 107.5:
												pixels_low.append((9, 18))
												ans = 3												 # approximately 15 were 3 out of 15 samples at leaf node
											else:
												pixels_high.append((9, 18))
												ans = 7												 # approximately 1 were 7 out of 1 samples at leaf node
								else:
									pixels_high.append((11, 12))
									if features[8][16] <= 50.0:
										pixels_low.append((8, 16))
										if features[19][16] <= 11.0:
											pixels_low.append((19, 16))
											if features[14][14] <= 3.0:
												pixels_low.append((14, 14))
												if features[13][16] <= 2.0:
													pixels_low.append((13, 16))
													if features[18][11] <= 17.5:
														pixels_low.append((18, 11))
														if features[14][12] <= 116.5:
															pixels_low.append((14, 12))
															ans = 9															 # approximately 2 were 9 out of 2 samples at leaf node
														else:
															pixels_high.append((14, 12))
															ans = 5															 # approximately 2 were 5 out of 2 samples at leaf node
													else:
														pixels_high.append((18, 11))
														ans = 7														 # approximately 17 were 7 out of 17 samples at leaf node
												else:
													pixels_high.append((13, 16))
													if features[14][20] <= 79.5:
														pixels_low.append((14, 20))
														if features[10][13] <= 78.0:
															pixels_low.append((10, 13))
															ans = 5															 # approximately 1 were 5 out of 1 samples at leaf node
														else:
															pixels_high.append((10, 13))
															ans = 4															 # approximately 7 were 4 out of 7 samples at leaf node
													else:
														pixels_high.append((14, 20))
														if features[13][14] <= 3.0:
															pixels_low.append((13, 14))
															ans = 9															 # approximately 10 were 9 out of 10 samples at leaf node
														else:
															pixels_high.append((13, 14))
															if features[16][15] <= 221.0:
																pixels_low.append((16, 15))
																ans = 0																 # approximately 1 were 0 out of 1 samples at leaf node
															else:
																pixels_high.append((16, 15))
																ans = 4																 # approximately 2 were 4 out of 2 samples at leaf node
											else:
												pixels_high.append((14, 14))
												if features[6][21] <= 7.0:
													pixels_low.append((6, 21))
													if features[13][9] <= 170.5:
														pixels_low.append((13, 9))
														if features[11][15] <= 225.5:
															pixels_low.append((11, 15))
															if features[11][6] <= 43.0:
																pixels_low.append((11, 6))
																if features[20][11] <= 43.5:
																	pixels_low.append((20, 11))
																	ans = 9																	 # approximately 17 were 9 out of 17 samples at leaf node
																else:
																	pixels_high.append((20, 11))
																	ans = 4																	 # approximately 2 were 4 out of 2 samples at leaf node
															else:
																pixels_high.append((11, 6))
																if features[20][22] <= 5.5:
																	pixels_low.append((20, 22))
																	ans = 7																	 # approximately 2 were 7 out of 2 samples at leaf node
																else:
																	pixels_high.append((20, 22))
																	ans = 5																	 # approximately 1 were 5 out of 1 samples at leaf node
														else:
															pixels_high.append((11, 15))
															if features[16][14] <= 252.5:
																pixels_low.append((16, 14))
																if features[13][9] <= 122.5:
																	pixels_low.append((13, 9))
																	ans = 9																	 # approximately 5 were 9 out of 5 samples at leaf node
																else:
																	pixels_high.append((13, 9))
																	ans = 4																	 # approximately 2 were 4 out of 2 samples at leaf node
															else:
																pixels_high.append((16, 14))
																if features[8][24] <= 81.0:
																	pixels_low.append((8, 24))
																	ans = 4																	 # approximately 9 were 4 out of 9 samples at leaf node
																else:
																	pixels_high.append((8, 24))
																	ans = 9																	 # approximately 1 were 9 out of 1 samples at leaf node
													else:
														pixels_high.append((13, 9))
														if features[17][13] <= 2.0:
															pixels_low.append((17, 13))
															ans = 5															 # approximately 2 were 5 out of 2 samples at leaf node
														else:
															pixels_high.append((17, 13))
															if features[16][5] <= 44.5:
																pixels_low.append((16, 5))
																if features[8][15] <= 197.0:
																	pixels_low.append((8, 15))
																	if features[14][26] <= 89.0:
																		pixels_low.append((14, 26))
																		ans = 9																		 # approximately 105 were 9 out of 105 samples at leaf node
																	else:
																		pixels_high.append((14, 26))
																		if features[13][9] <= 220.0:
																			pixels_low.append((13, 9))
																			ans = 9																			 # approximately 2 were 9 out of 2 samples at leaf node
																		else:
																			pixels_high.append((13, 9))
																			ans = 4																			 # approximately 1 were 4 out of 1 samples at leaf node
																else:
																	pixels_high.append((8, 15))
																	ans = 4																	 # approximately 1 were 4 out of 1 samples at leaf node
															else:
																pixels_high.append((16, 5))
																ans = 8																 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													pixels_high.append((6, 21))
													if features[9][17] <= 13.0:
														pixels_low.append((9, 17))
														if features[21][11] <= 1.0:
															pixels_low.append((21, 11))
															ans = 5															 # approximately 3 were 5 out of 3 samples at leaf node
														else:
															pixels_high.append((21, 11))
															ans = 3															 # approximately 2 were 3 out of 2 samples at leaf node
													else:
														pixels_high.append((9, 17))
														ans = 8														 # approximately 6 were 8 out of 6 samples at leaf node
										else:
											pixels_high.append((19, 16))
											if features[10][18] <= 241.5:
												pixels_low.append((10, 18))
												if features[13][16] <= 180.0:
													pixels_low.append((13, 16))
													if features[18][7] <= 175.0:
														pixels_low.append((18, 7))
														if features[12][22] <= 118.0:
															pixels_low.append((12, 22))
															ans = 3															 # approximately 10 were 3 out of 10 samples at leaf node
														else:
															pixels_high.append((12, 22))
															if features[18][13] <= 121.5:
																pixels_low.append((18, 13))
																ans = 8																 # approximately 1 were 8 out of 1 samples at leaf node
															else:
																pixels_high.append((18, 13))
																ans = 0																 # approximately 1 were 0 out of 1 samples at leaf node
													else:
														pixels_high.append((18, 7))
														ans = 5														 # approximately 4 were 5 out of 4 samples at leaf node
												else:
													pixels_high.append((13, 16))
													ans = 4													 # approximately 5 were 4 out of 5 samples at leaf node
											else:
												pixels_high.append((10, 18))
												ans = 6												 # approximately 7 were 6 out of 7 samples at leaf node
									else:
										pixels_high.append((8, 16))
										if features[15][16] <= 95.5:
											pixels_low.append((15, 16))
											if features[11][14] <= 85.5:
												pixels_low.append((11, 14))
												ans = 9												 # approximately 5 were 9 out of 5 samples at leaf node
											else:
												pixels_high.append((11, 14))
												if features[19][5] <= 85.5:
													pixels_low.append((19, 5))
													if features[16][21] <= 42.5:
														pixels_low.append((16, 21))
														if features[17][15] <= 30.0:
															pixels_low.append((17, 15))
															ans = 8															 # approximately 3 were 8 out of 3 samples at leaf node
														else:
															pixels_high.append((17, 15))
															if features[6][10] <= 53.5:
																pixels_low.append((6, 10))
																if features[18][6] <= 14.5:
																	pixels_low.append((18, 6))
																	if features[14][8] <= 108.5:
																		pixels_low.append((14, 8))
																		ans = 7																		 # approximately 1 were 7 out of 1 samples at leaf node
																	else:
																		pixels_high.append((14, 8))
																		ans = 4																		 # approximately 1 were 4 out of 1 samples at leaf node
																else:
																	pixels_high.append((18, 6))
																	ans = 6																	 # approximately 1 were 6 out of 1 samples at leaf node
															else:
																pixels_high.append((6, 10))
																ans = 3																 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														pixels_high.append((16, 21))
														ans = 5														 # approximately 4 were 5 out of 4 samples at leaf node
												else:
													pixels_high.append((19, 5))
													ans = 0													 # approximately 5 were 0 out of 5 samples at leaf node
										else:
											pixels_high.append((15, 16))
											if features[11][25] <= 55.5:
												pixels_low.append((11, 25))
												if features[11][11] <= 253.5:
													pixels_low.append((11, 11))
													if features[8][22] <= 67.0:
														pixels_low.append((8, 22))
														if features[11][20] <= 254.5:
															pixels_low.append((11, 20))
															ans = 4															 # approximately 70 were 4 out of 70 samples at leaf node
														else:
															pixels_high.append((11, 20))
															ans = 6															 # approximately 1 were 6 out of 1 samples at leaf node
													else:
														pixels_high.append((8, 22))
														if features[16][10] <= 125.0:
															pixels_low.append((16, 10))
															ans = 7															 # approximately 1 were 7 out of 1 samples at leaf node
														else:
															pixels_high.append((16, 10))
															ans = 0															 # approximately 1 were 0 out of 1 samples at leaf node
												else:
													pixels_high.append((11, 11))
													if features[11][18] <= 3.5:
														pixels_low.append((11, 18))
														if features[19][6] <= 127.0:
															pixels_low.append((19, 6))
															ans = 4															 # approximately 3 were 4 out of 3 samples at leaf node
														else:
															pixels_high.append((19, 6))
															ans = 5															 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														pixels_high.append((11, 18))
														ans = 9														 # approximately 3 were 9 out of 3 samples at leaf node
											else:
												pixels_high.append((11, 25))
												if features[18][6] <= 197.5:
													pixels_low.append((18, 6))
													if features[12][16] <= 43.5:
														pixels_low.append((12, 16))
														ans = 7														 # approximately 2 were 7 out of 2 samples at leaf node
													else:
														pixels_high.append((12, 16))
														ans = 4														 # approximately 4 were 4 out of 4 samples at leaf node
												else:
													pixels_high.append((18, 6))
													if features[17][21] <= 61.5:
														pixels_low.append((17, 21))
														ans = 9														 # approximately 4 were 9 out of 4 samples at leaf node
													else:
														pixels_high.append((17, 21))
														ans = 3														 # approximately 1 were 3 out of 1 samples at leaf node
							else:
								pixels_high.append((6, 12))
								if features[12][7] <= 1.5:
									pixels_low.append((12, 7))
									if features[19][20] <= 25.5:
										pixels_low.append((19, 20))
										if features[9][13] <= 15.5:
											pixels_low.append((9, 13))
											ans = 7											 # approximately 1 were 7 out of 1 samples at leaf node
										else:
											pixels_high.append((9, 13))
											if features[13][16] <= 127.0:
												pixels_low.append((13, 16))
												ans = 8												 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												pixels_high.append((13, 16))
												if features[5][19] <= 126.5:
													pixels_low.append((5, 19))
													ans = 9													 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													pixels_high.append((5, 19))
													ans = 2													 # approximately 1 were 2 out of 1 samples at leaf node
									else:
										pixels_high.append((19, 20))
										ans = 4										 # approximately 9 were 4 out of 9 samples at leaf node
								else:
									pixels_high.append((12, 7))
									if features[13][19] <= 252.5:
										pixels_low.append((13, 19))
										if features[13][12] <= 14.5:
											pixels_low.append((13, 12))
											if features[9][15] <= 8.0:
												pixels_low.append((9, 15))
												if features[15][23] <= 7.0:
													pixels_low.append((15, 23))
													ans = 9													 # approximately 2 were 9 out of 2 samples at leaf node
												else:
													pixels_high.append((15, 23))
													if features[22][15] <= 3.5:
														pixels_low.append((22, 15))
														if features[11][13] <= 78.5:
															pixels_low.append((11, 13))
															ans = 3															 # approximately 1 were 3 out of 1 samples at leaf node
														else:
															pixels_high.append((11, 13))
															ans = 8															 # approximately 1 were 8 out of 1 samples at leaf node
													else:
														pixels_high.append((22, 15))
														ans = 7														 # approximately 2 were 7 out of 2 samples at leaf node
											else:
												pixels_high.append((9, 15))
												if features[23][6] <= 8.0:
													pixels_low.append((23, 6))
													ans = 9													 # approximately 118 were 9 out of 118 samples at leaf node
												else:
													pixels_high.append((23, 6))
													if features[23][18] <= 70.0:
														pixels_low.append((23, 18))
														ans = 4														 # approximately 1 were 4 out of 1 samples at leaf node
													else:
														pixels_high.append((23, 18))
														ans = 5														 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											pixels_high.append((13, 12))
											ans = 3											 # approximately 3 were 3 out of 3 samples at leaf node
									else:
										pixels_high.append((13, 19))
										if features[15][24] <= 106.0:
											pixels_low.append((15, 24))
											ans = 9											 # approximately 1 were 9 out of 1 samples at leaf node
										else:
											pixels_high.append((15, 24))
											ans = 8											 # approximately 5 were 8 out of 5 samples at leaf node
						else:
							pixels_high.append((13, 13))
							if features[11][6] <= 3.0:
								pixels_low.append((11, 6))
								if features[8][18] <= 219.5:
									pixels_low.append((8, 18))
									if features[17][11] <= 35.5:
										pixels_low.append((17, 11))
										if features[11][19] <= 216.5:
											pixels_low.append((11, 19))
											if features[19][8] <= 1.5:
												pixels_low.append((19, 8))
												if features[10][16] <= 36.0:
													pixels_low.append((10, 16))
													if features[16][11] <= 216.5:
														pixels_low.append((16, 11))
														ans = 3														 # approximately 7 were 3 out of 7 samples at leaf node
													else:
														pixels_high.append((16, 11))
														ans = 7														 # approximately 1 were 7 out of 1 samples at leaf node
												else:
													pixels_high.append((10, 16))
													if features[9][15] <= 102.5:
														pixels_low.append((9, 15))
														ans = 5														 # approximately 2 were 5 out of 2 samples at leaf node
													else:
														pixels_high.append((9, 15))
														if features[23][7] <= 30.0:
															pixels_low.append((23, 7))
															ans = 2															 # approximately 1 were 2 out of 1 samples at leaf node
														else:
															pixels_high.append((23, 7))
															ans = 4															 # approximately 1 were 4 out of 1 samples at leaf node
											else:
												pixels_high.append((19, 8))
												if features[21][11] <= 79.0:
													pixels_low.append((21, 11))
													if features[11][15] <= 4.5:
														pixels_low.append((11, 15))
														ans = 9														 # approximately 1 were 9 out of 1 samples at leaf node
													else:
														pixels_high.append((11, 15))
														ans = 5														 # approximately 25 were 5 out of 25 samples at leaf node
												else:
													pixels_high.append((21, 11))
													if features[19][14] <= 218.5:
														pixels_low.append((19, 14))
														ans = 3														 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														pixels_high.append((19, 14))
														ans = 8														 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											pixels_high.append((11, 19))
											ans = 6											 # approximately 11 were 6 out of 11 samples at leaf node
									else:
										pixels_high.append((17, 11))
										if features[11][11] <= 220.5:
											pixels_low.append((11, 11))
											if features[8][23] <= 35.5:
												pixels_low.append((8, 23))
												if features[11][8] <= 91.5:
													pixels_low.append((11, 8))
													if features[17][15] <= 153.0:
														pixels_low.append((17, 15))
														if features[16][10] <= 235.0:
															pixels_low.append((16, 10))
															ans = 9															 # approximately 6 were 9 out of 6 samples at leaf node
														else:
															pixels_high.append((16, 10))
															if features[19][15] <= 20.5:
																pixels_low.append((19, 15))
																ans = 1																 # approximately 7 were 1 out of 7 samples at leaf node
															else:
																pixels_high.append((19, 15))
																if features[17][5] <= 14.5:
																	pixels_low.append((17, 5))
																	ans = 7																	 # approximately 1 were 7 out of 1 samples at leaf node
																else:
																	pixels_high.append((17, 5))
																	ans = 4																	 # approximately 2 were 4 out of 2 samples at leaf node
													else:
														pixels_high.append((17, 15))
														ans = 4														 # approximately 14 were 4 out of 14 samples at leaf node
												else:
													pixels_high.append((11, 8))
													if features[7][11] <= 16.5:
														pixels_low.append((7, 11))
														if features[18][19] <= 2.0:
															pixels_low.append((18, 19))
															if features[10][16] <= 8.5:
																pixels_low.append((10, 16))
																ans = 7																 # approximately 4 were 7 out of 4 samples at leaf node
															else:
																pixels_high.append((10, 16))
																if features[11][14] <= 246.5:
																	pixels_low.append((11, 14))
																	ans = 2																	 # approximately 3 were 2 out of 3 samples at leaf node
																else:
																	pixels_high.append((11, 14))
																	ans = 3																	 # approximately 1 were 3 out of 1 samples at leaf node
														else:
															pixels_high.append((18, 19))
															ans = 3															 # approximately 7 were 3 out of 7 samples at leaf node
													else:
														pixels_high.append((7, 11))
														ans = 9														 # approximately 12 were 9 out of 12 samples at leaf node
											else:
												pixels_high.append((8, 23))
												if features[19][9] <= 121.5:
													pixels_low.append((19, 9))
													if features[20][7] <= 16.0:
														pixels_low.append((20, 7))
														ans = 1														 # approximately 1 were 1 out of 1 samples at leaf node
													else:
														pixels_high.append((20, 7))
														ans = 5														 # approximately 4 were 5 out of 4 samples at leaf node
												else:
													pixels_high.append((19, 9))
													ans = 3													 # approximately 16 were 3 out of 16 samples at leaf node
										else:
											pixels_high.append((11, 11))
											if features[15][21] <= 253.5:
												pixels_low.append((15, 21))
												if features[21][8] <= 243.0:
													pixels_low.append((21, 8))
													ans = 9													 # approximately 30 were 9 out of 30 samples at leaf node
												else:
													pixels_high.append((21, 8))
													ans = 4													 # approximately 1 were 4 out of 1 samples at leaf node
											else:
												pixels_high.append((15, 21))
												ans = 4												 # approximately 2 were 4 out of 2 samples at leaf node
								else:
									pixels_high.append((8, 18))
									if features[9][15] <= 253.5:
										pixels_low.append((9, 15))
										if features[4][16] <= 14.0:
											pixels_low.append((4, 16))
											ans = 8											 # approximately 27 were 8 out of 27 samples at leaf node
										else:
											pixels_high.append((4, 16))
											ans = 3											 # approximately 1 were 3 out of 1 samples at leaf node
									else:
										pixels_high.append((9, 15))
										if features[8][22] <= 66.5:
											pixels_low.append((8, 22))
											if features[23][7] <= 4.0:
												pixels_low.append((23, 7))
												ans = 2												 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												pixels_high.append((23, 7))
												ans = 4												 # approximately 1 were 4 out of 1 samples at leaf node
										else:
											pixels_high.append((8, 22))
											ans = 5											 # approximately 1 were 5 out of 1 samples at leaf node
							else:
								pixels_high.append((11, 6))
								if features[12][18] <= 150.5:
									pixels_low.append((12, 18))
									if features[7][12] <= 130.0:
										pixels_low.append((7, 12))
										if features[11][10] <= 187.0:
											pixels_low.append((11, 10))
											ans = 3											 # approximately 139 were 3 out of 139 samples at leaf node
										else:
											pixels_high.append((11, 10))
											if features[16][15] <= 142.0:
												pixels_low.append((16, 15))
												ans = 5												 # approximately 3 were 5 out of 3 samples at leaf node
											else:
												pixels_high.append((16, 15))
												if features[17][19] <= 206.0:
													pixels_low.append((17, 19))
													if features[14][24] <= 194.0:
														pixels_low.append((14, 24))
														ans = 1														 # approximately 2 were 1 out of 2 samples at leaf node
													else:
														pixels_high.append((14, 24))
														ans = 4														 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													pixels_high.append((17, 19))
													ans = 3													 # approximately 3 were 3 out of 3 samples at leaf node
									else:
										pixels_high.append((7, 12))
										if features[9][13] <= 240.0:
											pixels_low.append((9, 13))
											ans = 9											 # approximately 5 were 9 out of 5 samples at leaf node
										else:
											pixels_high.append((9, 13))
											ans = 5											 # approximately 1 were 5 out of 1 samples at leaf node
								else:
									pixels_high.append((12, 18))
									if features[17][23] <= 16.0:
										pixels_low.append((17, 23))
										ans = 7										 # approximately 5 were 7 out of 5 samples at leaf node
									else:
										pixels_high.append((17, 23))
										if features[11][8] <= 252.5:
											pixels_low.append((11, 8))
											if features[11][8] <= 216.5:
												pixels_low.append((11, 8))
												if features[6][7] <= 44.5:
													pixels_low.append((6, 7))
													ans = 1													 # approximately 1 were 1 out of 1 samples at leaf node
												else:
													pixels_high.append((6, 7))
													ans = 3													 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												pixels_high.append((11, 8))
												ans = 2												 # approximately 2 were 2 out of 2 samples at leaf node
										else:
											pixels_high.append((11, 8))
											ans = 8											 # approximately 3 were 8 out of 3 samples at leaf node
					else:
						pixels_high.append((9, 11))
						if features[13][8] <= 1.0:
							pixels_low.append((13, 8))
							if features[14][6] <= 76.5:
								pixels_low.append((14, 6))
								if features[13][10] <= 131.5:
									pixels_low.append((13, 10))
									if features[16][26] <= 92.5:
										pixels_low.append((16, 26))
										if features[13][5] <= 181.5:
											pixels_low.append((13, 5))
											ans = 4											 # approximately 140 were 4 out of 140 samples at leaf node
										else:
											pixels_high.append((13, 5))
											ans = 8											 # approximately 2 were 8 out of 2 samples at leaf node
									else:
										pixels_high.append((16, 26))
										ans = 9										 # approximately 2 were 9 out of 2 samples at leaf node
								else:
									pixels_high.append((13, 10))
									if features[15][10] <= 248.0:
										pixels_low.append((15, 10))
										if features[18][6] <= 35.5:
											pixels_low.append((18, 6))
											if features[12][12] <= 164.0:
												pixels_low.append((12, 12))
												if features[21][20] <= 67.0:
													pixels_low.append((21, 20))
													ans = 9													 # approximately 6 were 9 out of 6 samples at leaf node
												else:
													pixels_high.append((21, 20))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												pixels_high.append((12, 12))
												if features[22][9] <= 20.0:
													pixels_low.append((22, 9))
													if features[13][17] <= 198.5:
														pixels_low.append((13, 17))
														ans = 8														 # approximately 1 were 8 out of 1 samples at leaf node
													else:
														pixels_high.append((13, 17))
														ans = 2														 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													pixels_high.append((22, 9))
													ans = 7													 # approximately 1 were 7 out of 1 samples at leaf node
										else:
											pixels_high.append((18, 6))
											if features[10][11] <= 239.5:
												pixels_low.append((10, 11))
												ans = 4												 # approximately 5 were 4 out of 5 samples at leaf node
											else:
												pixels_high.append((10, 11))
												ans = 5												 # approximately 1 were 5 out of 1 samples at leaf node
									else:
										pixels_high.append((15, 10))
										if features[17][7] <= 253.5:
											pixels_low.append((17, 7))
											ans = 7											 # approximately 8 were 7 out of 8 samples at leaf node
										else:
											pixels_high.append((17, 7))
											ans = 9											 # approximately 1 were 9 out of 1 samples at leaf node
							else:
								pixels_high.append((14, 6))
								if features[11][5] <= 93.0:
									pixels_low.append((11, 5))
									if features[15][9] <= 248.5:
										pixels_low.append((15, 9))
										if features[17][15] <= 4.5:
											pixels_low.append((17, 15))
											ans = 8											 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											pixels_high.append((17, 15))
											if features[10][17] <= 253.5:
												pixels_low.append((10, 17))
												ans = 9												 # approximately 39 were 9 out of 39 samples at leaf node
											else:
												pixels_high.append((10, 17))
												ans = 3												 # approximately 1 were 3 out of 1 samples at leaf node
									else:
										pixels_high.append((15, 9))
										if features[14][12] <= 146.0:
											pixels_low.append((14, 12))
											ans = 4											 # approximately 3 were 4 out of 3 samples at leaf node
										else:
											pixels_high.append((14, 12))
											ans = 3											 # approximately 1 were 3 out of 1 samples at leaf node
								else:
									pixels_high.append((11, 5))
									ans = 8									 # approximately 4 were 8 out of 4 samples at leaf node
						else:
							pixels_high.append((13, 8))
							if features[23][6] <= 8.5:
								pixels_low.append((23, 6))
								if features[21][16] <= 0.5:
									pixels_low.append((21, 16))
									if features[11][19] <= 182.0:
										pixels_low.append((11, 19))
										if features[7][22] <= 16.0:
											pixels_low.append((7, 22))
											if features[17][12] <= 2.5:
												pixels_low.append((17, 12))
												if features[19][12] <= 16.5:
													pixels_low.append((19, 12))
													if features[15][17] <= 31.0:
														pixels_low.append((15, 17))
														if features[15][12] <= 42.5:
															pixels_low.append((15, 12))
															if features[18][23] <= 252.0:
																pixels_low.append((18, 23))
																if features[15][19] <= 31.5:
																	pixels_low.append((15, 19))
																	ans = 5																	 # approximately 32 were 5 out of 32 samples at leaf node
																else:
																	pixels_high.append((15, 19))
																	ans = 9																	 # approximately 1 were 9 out of 1 samples at leaf node
															else:
																pixels_high.append((18, 23))
																ans = 9																 # approximately 2 were 9 out of 2 samples at leaf node
														else:
															pixels_high.append((15, 12))
															if features[16][21] <= 117.0:
																pixels_low.append((16, 21))
																if features[11][14] <= 206.5:
																	pixels_low.append((11, 14))
																	if features[10][9] <= 46.0:
																		pixels_low.append((10, 9))
																		ans = 4																		 # approximately 1 were 4 out of 1 samples at leaf node
																	else:
																		pixels_high.append((10, 9))
																		if features[15][8] <= 193.0:
																			pixels_low.append((15, 8))
																			ans = 7																			 # approximately 1 were 7 out of 1 samples at leaf node
																		else:
																			pixels_high.append((15, 8))
																			ans = 8																			 # approximately 1 were 8 out of 1 samples at leaf node
																else:
																	pixels_high.append((11, 14))
																	ans = 9																	 # approximately 2 were 9 out of 2 samples at leaf node
															else:
																pixels_high.append((16, 21))
																ans = 3																 # approximately 3 were 3 out of 3 samples at leaf node
													else:
														pixels_high.append((15, 17))
														if features[15][9] <= 243.5:
															pixels_low.append((15, 9))
															ans = 9															 # approximately 14 were 9 out of 14 samples at leaf node
														else:
															pixels_high.append((15, 9))
															if features[13][21] <= 61.0:
																pixels_low.append((13, 21))
																ans = 4																 # approximately 4 were 4 out of 4 samples at leaf node
															else:
																pixels_high.append((13, 21))
																if features[18][8] <= 126.5:
																	pixels_low.append((18, 8))
																	ans = 9																	 # approximately 1 were 9 out of 1 samples at leaf node
																else:
																	pixels_high.append((18, 8))
																	ans = 5																	 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													pixels_high.append((19, 12))
													if features[17][7] <= 22.0:
														pixels_low.append((17, 7))
														if features[16][8] <= 145.5:
															pixels_low.append((16, 8))
															if features[11][15] <= 29.5:
																pixels_low.append((11, 15))
																ans = 8																 # approximately 1 were 8 out of 1 samples at leaf node
															else:
																pixels_high.append((11, 15))
																ans = 4																 # approximately 11 were 4 out of 11 samples at leaf node
														else:
															pixels_high.append((16, 8))
															if features[21][11] <= 71.5:
																pixels_low.append((21, 11))
																ans = 9																 # approximately 4 were 9 out of 4 samples at leaf node
															else:
																pixels_high.append((21, 11))
																if features[21][9] <= 162.0:
																	pixels_low.append((21, 9))
																	ans = 2																	 # approximately 1 were 2 out of 1 samples at leaf node
																else:
																	pixels_high.append((21, 9))
																	ans = 7																	 # approximately 2 were 7 out of 2 samples at leaf node
													else:
														pixels_high.append((17, 7))
														if features[9][15] <= 2.5:
															pixels_low.append((9, 15))
															if features[14][14] <= 173.5:
																pixels_low.append((14, 14))
																if features[16][18] <= 252.5:
																	pixels_low.append((16, 18))
																	ans = 8																	 # approximately 6 were 8 out of 6 samples at leaf node
																else:
																	pixels_high.append((16, 18))
																	if features[20][14] <= 12.0:
																		pixels_low.append((20, 14))
																		ans = 2																		 # approximately 1 were 2 out of 1 samples at leaf node
																	else:
																		pixels_high.append((20, 14))
																		if features[17][13] <= 26.0:
																			pixels_low.append((17, 13))
																			ans = 9																			 # approximately 1 were 9 out of 1 samples at leaf node
																		else:
																			pixels_high.append((17, 13))
																			ans = 7																			 # approximately 1 were 7 out of 1 samples at leaf node
															else:
																pixels_high.append((14, 14))
																ans = 9																 # approximately 6 were 9 out of 6 samples at leaf node
														else:
															pixels_high.append((9, 15))
															if features[18][5] <= 181.5:
																pixels_low.append((18, 5))
																if features[17][14] <= 15.0:
																	pixels_low.append((17, 14))
																	ans = 4																	 # approximately 1 were 4 out of 1 samples at leaf node
																else:
																	pixels_high.append((17, 14))
																	if features[11][26] <= 245.0:
																		pixels_low.append((11, 26))
																		ans = 9																		 # approximately 72 were 9 out of 72 samples at leaf node
																	else:
																		pixels_high.append((11, 26))
																		if features[18][17] <= 106.0:
																			pixels_low.append((18, 17))
																			ans = 7																			 # approximately 1 were 7 out of 1 samples at leaf node
																		else:
																			pixels_high.append((18, 17))
																			ans = 9																			 # approximately 1 were 9 out of 1 samples at leaf node
															else:
																pixels_high.append((18, 5))
																ans = 4																 # approximately 1 were 4 out of 1 samples at leaf node
											else:
												pixels_high.append((17, 12))
												if features[7][7] <= 10.0:
													pixels_low.append((7, 7))
													if features[21][15] <= 126.5:
														pixels_low.append((21, 15))
														if features[13][15] <= 0.5:
															pixels_low.append((13, 15))
															if features[14][13] <= 35.5:
																pixels_low.append((14, 13))
																if features[12][17] <= 15.5:
																	pixels_low.append((12, 17))
																	if features[10][12] <= 186.0:
																		pixels_low.append((10, 12))
																		if features[9][8] <= 32.0:
																			pixels_low.append((9, 8))
																			ans = 9																			 # approximately 3 were 9 out of 3 samples at leaf node
																		else:
																			pixels_high.append((9, 8))
																			ans = 7																			 # approximately 1 were 7 out of 1 samples at leaf node
																	else:
																		pixels_high.append((10, 12))
																		if features[16][10] <= 254.0:
																			pixels_low.append((16, 10))
																			ans = 7																			 # approximately 28 were 7 out of 28 samples at leaf node
																		else:
																			pixels_high.append((16, 10))
																			ans = 9																			 # approximately 1 were 9 out of 1 samples at leaf node
																else:
																	pixels_high.append((12, 17))
																	if features[11][8] <= 3.0:
																		pixels_low.append((11, 8))
																		ans = 4																		 # approximately 4 were 4 out of 4 samples at leaf node
																	else:
																		pixels_high.append((11, 8))
																		if features[12][20] <= 150.0:
																			pixels_low.append((12, 20))
																			if features[5][11] <= 100.5:
																				pixels_low.append((5, 11))
																				if features[9][15] <= 22.0:
																					pixels_low.append((9, 15))
																					ans = 7																					 # approximately 1 were 7 out of 1 samples at leaf node
																				else:
																					pixels_high.append((9, 15))
																					ans = 9																					 # approximately 35 were 9 out of 35 samples at leaf node
																			else:
																				pixels_high.append((5, 11))
																				ans = 4																				 # approximately 1 were 4 out of 1 samples at leaf node
																		else:
																			pixels_high.append((12, 20))
																			ans = 8																			 # approximately 2 were 8 out of 2 samples at leaf node
															else:
																pixels_high.append((14, 13))
																if features[20][14] <= 105.0:
																	pixels_low.append((20, 14))
																	if features[10][6] <= 206.5:
																		pixels_low.append((10, 6))
																		ans = 9																		 # approximately 73 were 9 out of 73 samples at leaf node
																	else:
																		pixels_high.append((10, 6))
																		ans = 5																		 # approximately 1 were 5 out of 1 samples at leaf node
																else:
																	pixels_high.append((20, 14))
																	ans = 4																	 # approximately 1 were 4 out of 1 samples at leaf node
														else:
															pixels_high.append((13, 15))
															if features[12][5] <= 13.0:
																pixels_low.append((12, 5))
																if features[12][18] <= 210.0:
																	pixels_low.append((12, 18))
																	if features[16][8] <= 3.5:
																		pixels_low.append((16, 8))
																		if features[11][11] <= 244.0:
																			pixels_low.append((11, 11))
																			if features[14][25] <= 253.5:
																				pixels_low.append((14, 25))
																				if features[14][8] <= 18.5:
																					pixels_low.append((14, 8))
																					ans = 4																					 # approximately 1 were 4 out of 1 samples at leaf node
																				else:
																					pixels_high.append((14, 8))
																					if features[6][10] <= 14.5:
																						pixels_low.append((6, 10))
																						ans = 9																						 # approximately 55 were 9 out of 55 samples at leaf node
																					else:
																						pixels_high.append((6, 10))
																						ans = 4																						 # approximately 1 were 4 out of 1 samples at leaf node
																			else:
																				pixels_high.append((14, 25))
																				if features[17][15] <= 158.5:
																					pixels_low.append((17, 15))
																					ans = 9																					 # approximately 1 were 9 out of 1 samples at leaf node
																				else:
																					pixels_high.append((17, 15))
																					ans = 4																					 # approximately 2 were 4 out of 2 samples at leaf node
																		else:
																			pixels_high.append((11, 11))
																			if features[11][18] <= 6.5:
																				pixels_low.append((11, 18))
																				if features[14][21] <= 253.5:
																					pixels_low.append((14, 21))
																					ans = 4																					 # approximately 14 were 4 out of 14 samples at leaf node
																				else:
																					pixels_high.append((14, 21))
																					ans = 9																					 # approximately 1 were 9 out of 1 samples at leaf node
																			else:
																				pixels_high.append((11, 18))
																				ans = 9																				 # approximately 5 were 9 out of 5 samples at leaf node
																	else:
																		pixels_high.append((16, 8))
																		if features[24][18] <= 112.5:
																			pixels_low.append((24, 18))
																			if features[25][7] <= 13.5:
																				pixels_low.append((25, 7))
																				if features[20][16] <= 232.0:
																					pixels_low.append((20, 16))
																					if features[21][15] <= 9.5:
																						pixels_low.append((21, 15))
																						if features[19][26] <= 253.5:
																							pixels_low.append((19, 26))
																							if features[19][5] <= 49.5:
																								pixels_low.append((19, 5))
																								if features[7][20] <= 4.0:
																									pixels_low.append((7, 20))
																									if features[7][9] <= 202.5:
																										pixels_low.append((7, 9))
																										if features[9][7] <= 254.5:
																											pixels_low.append((9, 7))
																											if features[12][8] <= 26.5:
																												pixels_low.append((12, 8))
																												if features[16][6] <= 155.0:
																													pixels_low.append((16, 6))
																													if features[5][14] <= 168.0:
																														pixels_low.append((5, 14))
																														if features[15][8] <= 60.0:
																															pixels_low.append((15, 8))
																															ans = 4																															 # approximately 1 were 4 out of 1 samples at leaf node
																														else:
																															pixels_high.append((15, 8))
																															if features[16][7] <= 254.5:
																																pixels_low.append((16, 7))
																																ans = 9																																 # approximately 85 were 9 out of 85 samples at leaf node
																															else:
																																pixels_high.append((16, 7))
																																if features[14][25] <= 127.0:
																																	pixels_low.append((14, 25))
																																	ans = 9																																	 # approximately 1 were 9 out of 1 samples at leaf node
																																else:
																																	pixels_high.append((14, 25))
																																	ans = 4																																	 # approximately 1 were 4 out of 1 samples at leaf node
																													else:
																														pixels_high.append((5, 14))
																														ans = 4																														 # approximately 2 were 4 out of 2 samples at leaf node
																												else:
																													pixels_high.append((16, 6))
																													if features[13][14] <= 176.5:
																														pixels_low.append((13, 14))
																														ans = 4																														 # approximately 4 were 4 out of 4 samples at leaf node
																													else:
																														pixels_high.append((13, 14))
																														ans = 9																														 # approximately 1 were 9 out of 1 samples at leaf node
																											else:
																												pixels_high.append((12, 8))
																												if features[24][9] <= 174.5:
																													pixels_low.append((24, 9))
																													if features[20][18] <= 116.5:
																														pixels_low.append((20, 18))
																														if features[8][7] <= 44.0:
																															pixels_low.append((8, 7))
																															if features[23][11] <= 178.0:
																																pixels_low.append((23, 11))
																																if features[21][7] <= 254.5:
																																	pixels_low.append((21, 7))
																																	if features[15][8] <= 4.5:
																																		pixels_low.append((15, 8))
																																		if features[12][12] <= 97.0:
																																			pixels_low.append((12, 12))
																																			ans = 9																																			 # approximately 2 were 9 out of 2 samples at leaf node
																																		else:
																																			pixels_high.append((12, 12))
																																			ans = 4																																			 # approximately 1 were 4 out of 1 samples at leaf node
																																	else:
																																		pixels_high.append((15, 8))
																																		if features[4][13] <= 196.0:
																																			pixels_low.append((4, 13))
																																			if features[6][9] <= 47.5:
																																				pixels_low.append((6, 9))
																																				if features[13][15] <= 4.5:
																																					pixels_low.append((13, 15))
																																					if features[7][17] <= 28.0:
																																						pixels_low.append((7, 17))
																																						ans = 9																																						 # approximately 7 were 9 out of 7 samples at leaf node
																																					else:
																																						pixels_high.append((7, 17))
																																						ans = 7																																						 # approximately 1 were 7 out of 1 samples at leaf node
																																				else:
																																					pixels_high.append((13, 15))
																																					if features[20][17] <= 72.5:
																																						pixels_low.append((20, 17))
																																						if features[12][8] <= 86.5:
																																							pixels_low.append((12, 8))
																																							if features[15][6] <= 246.5:
																																								pixels_low.append((15, 6))
																																								if features[15][26] <= 207.0:
																																									pixels_low.append((15, 26))
																																									if features[15][8] <= 63.5:
																																										pixels_low.append((15, 8))
																																										if features[15][10] <= 59.0:
																																											pixels_low.append((15, 10))
																																											ans = 4																																											 # approximately 1 were 4 out of 1 samples at leaf node
																																										else:
																																											pixels_high.append((15, 10))
																																											ans = 9																																											 # approximately 1 were 9 out of 1 samples at leaf node
																																									else:
																																										pixels_high.append((15, 8))
																																										ans = 9																																										 # approximately 93 were 9 out of 93 samples at leaf node
																																								else:
																																									pixels_high.append((15, 26))
																																									ans = 4																																									 # approximately 1 were 4 out of 1 samples at leaf node
																																							else:
																																								pixels_high.append((15, 6))
																																								ans = 4																																								 # approximately 1 were 4 out of 1 samples at leaf node
																																						else:
																																							pixels_high.append((12, 8))
																																							if features[17][13] <= 46.5:
																																								pixels_low.append((17, 13))
																																								if features[17][6] <= 8.5:
																																									pixels_low.append((17, 6))
																																									ans = 9																																									 # approximately 12 were 9 out of 12 samples at leaf node
																																								else:
																																									pixels_high.append((17, 6))
																																									ans = 3																																									 # approximately 1 were 3 out of 1 samples at leaf node
																																							else:
																																								pixels_high.append((17, 13))
																																								if features[17][14] <= 32.5:
																																									pixels_low.append((17, 14))
																																									if features[12][6] <= 68.0:
																																										pixels_low.append((12, 6))
																																										ans = 9																																										 # approximately 12 were 9 out of 12 samples at leaf node
																																									else:
																																										pixels_high.append((12, 6))
																																										ans = 8																																										 # approximately 1 were 8 out of 1 samples at leaf node
																																								else:
																																									pixels_high.append((17, 14))
																																									if features[11][15] <= 7.0:
																																										pixels_low.append((11, 15))
																																										if features[8][24] <= 28.0:
																																											pixels_low.append((8, 24))
																																											ans = 9																																											 # approximately 15 were 9 out of 15 samples at leaf node
																																										else:
																																											pixels_high.append((8, 24))
																																											ans = 3																																											 # approximately 1 were 3 out of 1 samples at leaf node
																																									else:
																																										pixels_high.append((11, 15))
																																										if features[21][9] <= 253.5:
																																											pixels_low.append((21, 9))
																																											ans = 9																																											 # approximately 1481 were 9 out of 1481 samples at leaf node
																																										else:
																																											pixels_high.append((21, 9))
																																											if features[17][8] <= 8.5:
																																												pixels_low.append((17, 8))
																																												ans = 4																																												 # approximately 1 were 4 out of 1 samples at leaf node
																																											else:
																																												pixels_high.append((17, 8))
																																												ans = 9																																												 # approximately 15 were 9 out of 15 samples at leaf node
																																					else:
																																						pixels_high.append((20, 17))
																																						if features[20][17] <= 75.5:
																																							pixels_low.append((20, 17))
																																							ans = 7																																							 # approximately 1 were 7 out of 1 samples at leaf node
																																						else:
																																							pixels_high.append((20, 17))
																																							ans = 9																																							 # approximately 11 were 9 out of 11 samples at leaf node
																																			else:
																																				pixels_high.append((6, 9))
																																				if features[12][23] <= 128.0:
																																					pixels_low.append((12, 23))
																																					ans = 9																																					 # approximately 3 were 9 out of 3 samples at leaf node
																																				else:
																																					pixels_high.append((12, 23))
																																					ans = 7																																					 # approximately 1 were 7 out of 1 samples at leaf node
																																		else:
																																			pixels_high.append((4, 13))
																																			if features[8][9] <= 159.0:
																																				pixels_low.append((8, 9))
																																				ans = 4																																				 # approximately 1 were 4 out of 1 samples at leaf node
																																			else:
																																				pixels_high.append((8, 9))
																																				ans = 9																																				 # approximately 2 were 9 out of 2 samples at leaf node
																																else:
																																	pixels_high.append((21, 7))
																																	if features[12][7] <= 95.5:
																																		pixels_low.append((12, 7))
																																		ans = 9																																		 # approximately 2 were 9 out of 2 samples at leaf node
																																	else:
																																		pixels_high.append((12, 7))
																																		ans = 3																																		 # approximately 1 were 3 out of 1 samples at leaf node
																															else:
																																pixels_high.append((23, 11))
																																if features[19][7] <= 251.0:
																																	pixels_low.append((19, 7))
																																	ans = 9																																	 # approximately 2 were 9 out of 2 samples at leaf node
																																else:
																																	pixels_high.append((19, 7))
																																	ans = 8																																	 # approximately 1 were 8 out of 1 samples at leaf node
																														else:
																															pixels_high.append((8, 7))
																															if features[8][13] <= 20.0:
																																pixels_low.append((8, 13))
																																if features[18][6] <= 13.5:
																																	pixels_low.append((18, 6))
																																	if features[11][9] <= 120.0:
																																		pixels_low.append((11, 9))
																																		ans = 3																																		 # approximately 1 were 3 out of 1 samples at leaf node
																																	else:
																																		pixels_high.append((11, 9))
																																		ans = 7																																		 # approximately 1 were 7 out of 1 samples at leaf node
																																else:
																																	pixels_high.append((18, 6))
																																	ans = 8																																	 # approximately 2 were 8 out of 2 samples at leaf node
																															else:
																																pixels_high.append((8, 13))
																																ans = 9																																 # approximately 21 were 9 out of 21 samples at leaf node
																													else:
																														pixels_high.append((20, 18))
																														if features[14][24] <= 67.5:
																															pixels_low.append((14, 24))
																															ans = 9																															 # approximately 5 were 9 out of 5 samples at leaf node
																														else:
																															pixels_high.append((14, 24))
																															if features[19][24] <= 1.5:
																																pixels_low.append((19, 24))
																																ans = 5																																 # approximately 1 were 5 out of 1 samples at leaf node
																															else:
																																pixels_high.append((19, 24))
																																ans = 8																																 # approximately 1 were 8 out of 1 samples at leaf node
																												else:
																													pixels_high.append((24, 9))
																													ans = 4																													 # approximately 1 were 4 out of 1 samples at leaf node
																										else:
																											pixels_high.append((9, 7))
																											ans = 7																											 # approximately 1 were 7 out of 1 samples at leaf node
																									else:
																										pixels_high.append((7, 9))
																										if features[7][13] <= 35.0:
																											pixels_low.append((7, 13))
																											if features[10][17] <= 10.5:
																												pixels_low.append((10, 17))
																												ans = 8																												 # approximately 3 were 8 out of 3 samples at leaf node
																											else:
																												pixels_high.append((10, 17))
																												if features[10][22] <= 82.0:
																													pixels_low.append((10, 22))
																													ans = 7																													 # approximately 1 were 7 out of 1 samples at leaf node
																												else:
																													pixels_high.append((10, 22))
																													ans = 3																													 # approximately 2 were 3 out of 2 samples at leaf node
																										else:
																											pixels_high.append((7, 13))
																											ans = 9																											 # approximately 24 were 9 out of 24 samples at leaf node
																								else:
																									pixels_high.append((7, 20))
																									ans = 4																									 # approximately 1 were 4 out of 1 samples at leaf node
																							else:
																								pixels_high.append((19, 5))
																								if features[13][17] <= 186.0:
																									pixels_low.append((13, 17))
																									if features[10][7] <= 19.0:
																										pixels_low.append((10, 7))
																										ans = 9																										 # approximately 8 were 9 out of 8 samples at leaf node
																									else:
																										pixels_high.append((10, 7))
																										ans = 8																										 # approximately 1 were 8 out of 1 samples at leaf node
																								else:
																									pixels_high.append((13, 17))
																									ans = 4																									 # approximately 3 were 4 out of 3 samples at leaf node
																						else:
																							pixels_high.append((19, 26))
																							ans = 3																							 # approximately 1 were 3 out of 1 samples at leaf node
																					else:
																						pixels_high.append((21, 15))
																						if features[18][13] <= 224.5:
																							pixels_low.append((18, 13))
																							if features[10][7] <= 156.0:
																								pixels_low.append((10, 7))
																								ans = 4																								 # approximately 4 were 4 out of 4 samples at leaf node
																							else:
																								pixels_high.append((10, 7))
																								ans = 7																								 # approximately 2 were 7 out of 2 samples at leaf node
																						else:
																							pixels_high.append((18, 13))
																							ans = 9																							 # approximately 18 were 9 out of 18 samples at leaf node
																				else:
																					pixels_high.append((20, 16))
																					if features[14][25] <= 86.5:
																						pixels_low.append((14, 25))
																						ans = 4																						 # approximately 1 were 4 out of 1 samples at leaf node
																					else:
																						pixels_high.append((14, 25))
																						ans = 3																						 # approximately 1 were 3 out of 1 samples at leaf node
																			else:
																				pixels_high.append((25, 7))
																				ans = 4																				 # approximately 2 were 4 out of 2 samples at leaf node
																		else:
																			pixels_high.append((24, 18))
																			ans = 2																			 # approximately 2 were 2 out of 2 samples at leaf node
																else:
																	pixels_high.append((12, 18))
																	if features[10][16] <= 19.5:
																		pixels_low.append((10, 16))
																		if features[12][19] <= 145.5:
																			pixels_low.append((12, 19))
																			if features[11][8] <= 253.0:
																				pixels_low.append((11, 8))
																				ans = 3																				 # approximately 1 were 3 out of 1 samples at leaf node
																			else:
																				pixels_high.append((11, 8))
																				ans = 7																				 # approximately 1 were 7 out of 1 samples at leaf node
																		else:
																			pixels_high.append((12, 19))
																			if features[12][10] <= 250.0:
																				pixels_low.append((12, 10))
																				ans = 8																				 # approximately 10 were 8 out of 10 samples at leaf node
																			else:
																				pixels_high.append((12, 10))
																				ans = 9																				 # approximately 1 were 9 out of 1 samples at leaf node
																	else:
																		pixels_high.append((10, 16))
																		if features[22][9] <= 82.5:
																			pixels_low.append((22, 9))
																			if features[17][12] <= 95.5:
																				pixels_low.append((17, 12))
																				if features[9][10] <= 126.5:
																					pixels_low.append((9, 10))
																					ans = 4																					 # approximately 1 were 4 out of 1 samples at leaf node
																				else:
																					pixels_high.append((9, 10))
																					ans = 8																					 # approximately 1 were 8 out of 1 samples at leaf node
																			else:
																				pixels_high.append((17, 12))
																				if features[10][26] <= 57.5:
																					pixels_low.append((10, 26))
																					if features[18][14] <= 41.0:
																						pixels_low.append((18, 14))
																						if features[11][13] <= 126.5:
																							pixels_low.append((11, 13))
																							ans = 3																							 # approximately 1 were 3 out of 1 samples at leaf node
																						else:
																							pixels_high.append((11, 13))
																							ans = 9																							 # approximately 1 were 9 out of 1 samples at leaf node
																					else:
																						pixels_high.append((18, 14))
																						ans = 9																						 # approximately 36 were 9 out of 36 samples at leaf node
																				else:
																					pixels_high.append((10, 26))
																					ans = 7																					 # approximately 1 were 7 out of 1 samples at leaf node
																		else:
																			pixels_high.append((22, 9))
																			if features[13][13] <= 144.0:
																				pixels_low.append((13, 13))
																				ans = 4																				 # approximately 2 were 4 out of 2 samples at leaf node
																			else:
																				pixels_high.append((13, 13))
																				if features[11][20] <= 80.5:
																					pixels_low.append((11, 20))
																					ans = 2																					 # approximately 1 were 2 out of 1 samples at leaf node
																				else:
																					pixels_high.append((11, 20))
																					ans = 8																					 # approximately 1 were 8 out of 1 samples at leaf node
															else:
																pixels_high.append((12, 5))
																if features[9][9] <= 100.0:
																	pixels_low.append((9, 9))
																	ans = 4																	 # approximately 6 were 4 out of 6 samples at leaf node
																else:
																	pixels_high.append((9, 9))
																	if features[10][14] <= 141.0:
																		pixels_low.append((10, 14))
																		if features[16][22] <= 187.5:
																			pixels_low.append((16, 22))
																			ans = 2																			 # approximately 1 were 2 out of 1 samples at leaf node
																		else:
																			pixels_high.append((16, 22))
																			ans = 8																			 # approximately 3 were 8 out of 3 samples at leaf node
																	else:
																		pixels_high.append((10, 14))
																		ans = 9																		 # approximately 3 were 9 out of 3 samples at leaf node
													else:
														pixels_high.append((21, 15))
														if features[9][12] <= 100.5:
															pixels_low.append((9, 12))
															ans = 7															 # approximately 5 were 7 out of 5 samples at leaf node
														else:
															pixels_high.append((9, 12))
															ans = 4															 # approximately 4 were 4 out of 4 samples at leaf node
												else:
													pixels_high.append((7, 7))
													if features[13][19] <= 214.5:
														pixels_low.append((13, 19))
														if features[10][12] <= 72.0:
															pixels_low.append((10, 12))
															if features[10][15] <= 39.0:
																pixels_low.append((10, 15))
																ans = 3																 # approximately 1 were 3 out of 1 samples at leaf node
															else:
																pixels_high.append((10, 15))
																ans = 9																 # approximately 13 were 9 out of 13 samples at leaf node
														else:
															pixels_high.append((10, 12))
															if features[13][14] <= 53.0:
																pixels_low.append((13, 14))
																ans = 7																 # approximately 6 were 7 out of 6 samples at leaf node
															else:
																pixels_high.append((13, 14))
																if features[16][24] <= 201.5:
																	pixels_low.append((16, 24))
																	ans = 4																	 # approximately 5 were 4 out of 5 samples at leaf node
																else:
																	pixels_high.append((16, 24))
																	if features[17][16] <= 243.5:
																		pixels_low.append((17, 16))
																		ans = 8																		 # approximately 1 were 8 out of 1 samples at leaf node
																	else:
																		pixels_high.append((17, 16))
																		ans = 9																		 # approximately 3 were 9 out of 3 samples at leaf node
													else:
														pixels_high.append((13, 19))
														if features[10][14] <= 253.5:
															pixels_low.append((10, 14))
															ans = 8															 # approximately 13 were 8 out of 13 samples at leaf node
														else:
															pixels_high.append((10, 14))
															ans = 9															 # approximately 1 were 9 out of 1 samples at leaf node
										else:
											pixels_high.append((7, 22))
											if features[7][19] <= 218.5:
												pixels_low.append((7, 19))
												if features[9][25] <= 243.0:
													pixels_low.append((9, 25))
													if features[9][13] <= 42.0:
														pixels_low.append((9, 13))
														if features[6][16] <= 3.5:
															pixels_low.append((6, 16))
															ans = 3															 # approximately 2 were 3 out of 2 samples at leaf node
														else:
															pixels_high.append((6, 16))
															ans = 2															 # approximately 1 were 2 out of 1 samples at leaf node
													else:
														pixels_high.append((9, 13))
														if features[12][20] <= 242.5:
															pixels_low.append((12, 20))
															ans = 5															 # approximately 13 were 5 out of 13 samples at leaf node
														else:
															pixels_high.append((12, 20))
															ans = 9															 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													pixels_high.append((9, 25))
													ans = 3													 # approximately 4 were 3 out of 4 samples at leaf node
											else:
												pixels_high.append((7, 19))
												ans = 8												 # approximately 7 were 8 out of 7 samples at leaf node
									else:
										pixels_high.append((11, 19))
										if features[13][23] <= 94.0:
											pixels_low.append((13, 23))
											if features[15][16] <= 246.0:
												pixels_low.append((15, 16))
												if features[7][16] <= 152.0:
													pixels_low.append((7, 16))
													if features[17][11] <= 252.5:
														pixels_low.append((17, 11))
														if features[11][23] <= 89.5:
															pixels_low.append((11, 23))
															if features[12][15] <= 74.0:
																pixels_low.append((12, 15))
																ans = 0																 # approximately 2 were 0 out of 2 samples at leaf node
															else:
																pixels_high.append((12, 15))
																if features[15][22] <= 127.0:
																	pixels_low.append((15, 22))
																	ans = 2																	 # approximately 1 were 2 out of 1 samples at leaf node
																else:
																	pixels_high.append((15, 22))
																	ans = 6																	 # approximately 1 were 6 out of 1 samples at leaf node
														else:
															pixels_high.append((11, 23))
															ans = 8															 # approximately 2 were 8 out of 2 samples at leaf node
													else:
														pixels_high.append((17, 11))
														ans = 7														 # approximately 2 were 7 out of 2 samples at leaf node
												else:
													pixels_high.append((7, 16))
													ans = 4													 # approximately 2 were 4 out of 2 samples at leaf node
											else:
												pixels_high.append((15, 16))
												if features[10][11] <= 210.0:
													pixels_low.append((10, 11))
													if features[9][18] <= 248.5:
														pixels_low.append((9, 18))
														ans = 2														 # approximately 1 were 2 out of 1 samples at leaf node
													else:
														pixels_high.append((9, 18))
														ans = 3														 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													pixels_high.append((10, 11))
													ans = 9													 # approximately 11 were 9 out of 11 samples at leaf node
										else:
											pixels_high.append((13, 23))
											if features[20][14] <= 181.0:
												pixels_low.append((20, 14))
												if features[19][4] <= 81.0:
													pixels_low.append((19, 4))
													ans = 8													 # approximately 38 were 8 out of 38 samples at leaf node
												else:
													pixels_high.append((19, 4))
													ans = 6													 # approximately 1 were 6 out of 1 samples at leaf node
											else:
												pixels_high.append((20, 14))
												if features[13][11] <= 175.0:
													pixels_low.append((13, 11))
													ans = 4													 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													pixels_high.append((13, 11))
													ans = 9													 # approximately 1 were 9 out of 1 samples at leaf node
								else:
									pixels_high.append((21, 16))
									if features[8][10] <= 21.5:
										pixels_low.append((8, 10))
										if features[8][6] <= 13.0:
											pixels_low.append((8, 6))
											if features[17][16] <= 77.5:
												pixels_low.append((17, 16))
												if features[15][7] <= 244.0:
													pixels_low.append((15, 7))
													if features[19][6] <= 2.0:
														pixels_low.append((19, 6))
														if features[20][8] <= 126.5:
															pixels_low.append((20, 8))
															ans = 4															 # approximately 1 were 4 out of 1 samples at leaf node
														else:
															pixels_high.append((20, 8))
															ans = 7															 # approximately 1 were 7 out of 1 samples at leaf node
													else:
														pixels_high.append((19, 6))
														ans = 5														 # approximately 3 were 5 out of 3 samples at leaf node
												else:
													pixels_high.append((15, 7))
													ans = 9													 # approximately 4 were 9 out of 4 samples at leaf node
											else:
												pixels_high.append((17, 16))
												if features[10][15] <= 30.5:
													pixels_low.append((10, 15))
													ans = 9													 # approximately 2 were 9 out of 2 samples at leaf node
												else:
													pixels_high.append((10, 15))
													if features[15][16] <= 63.5:
														pixels_low.append((15, 16))
														ans = 9														 # approximately 1 were 9 out of 1 samples at leaf node
													else:
														pixels_high.append((15, 16))
														if features[7][18] <= 252.5:
															pixels_low.append((7, 18))
															ans = 4															 # approximately 37 were 4 out of 37 samples at leaf node
														else:
															pixels_high.append((7, 18))
															ans = 2															 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											pixels_high.append((8, 6))
											ans = 3											 # approximately 8 were 3 out of 8 samples at leaf node
									else:
										pixels_high.append((8, 10))
										if features[20][13] <= 196.0:
											pixels_low.append((20, 13))
											if features[15][17] <= 42.5:
												pixels_low.append((15, 17))
												if features[9][14] <= 44.5:
													pixels_low.append((9, 14))
													if features[10][12] <= 145.0:
														pixels_low.append((10, 12))
														if features[15][7] <= 34.0:
															pixels_low.append((15, 7))
															if features[14][7] <= 73.0:
																pixels_low.append((14, 7))
																ans = 2																 # approximately 1 were 2 out of 1 samples at leaf node
															else:
																pixels_high.append((14, 7))
																ans = 9																 # approximately 1 were 9 out of 1 samples at leaf node
														else:
															pixels_high.append((15, 7))
															ans = 3															 # approximately 6 were 3 out of 6 samples at leaf node
													else:
														pixels_high.append((10, 12))
														ans = 8														 # approximately 4 were 8 out of 4 samples at leaf node
												else:
													pixels_high.append((9, 14))
													if features[15][9] <= 252.5:
														pixels_low.append((15, 9))
														if features[9][8] <= 80.5:
															pixels_low.append((9, 8))
															if features[13][14] <= 125.0:
																pixels_low.append((13, 14))
																ans = 4																 # approximately 1 were 4 out of 1 samples at leaf node
															else:
																pixels_high.append((13, 14))
																ans = 2																 # approximately 1 were 2 out of 1 samples at leaf node
														else:
															pixels_high.append((9, 8))
															ans = 5															 # approximately 20 were 5 out of 20 samples at leaf node
													else:
														pixels_high.append((15, 9))
														if features[16][16] <= 8.0:
															pixels_low.append((16, 16))
															if features[15][10] <= 249.0:
																pixels_low.append((15, 10))
																ans = 9																 # approximately 1 were 9 out of 1 samples at leaf node
															else:
																pixels_high.append((15, 10))
																ans = 0																 # approximately 2 were 0 out of 2 samples at leaf node
														else:
															pixels_high.append((16, 16))
															ans = 8															 # approximately 2 were 8 out of 2 samples at leaf node
											else:
												pixels_high.append((15, 17))
												if features[8][12] <= 74.5:
													pixels_low.append((8, 12))
													if features[10][6] <= 135.5:
														pixels_low.append((10, 6))
														if features[17][6] <= 246.5:
															pixels_low.append((17, 6))
															ans = 7															 # approximately 20 were 7 out of 20 samples at leaf node
														else:
															pixels_high.append((17, 6))
															ans = 3															 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														pixels_high.append((10, 6))
														ans = 2														 # approximately 2 were 2 out of 2 samples at leaf node
												else:
													pixels_high.append((8, 12))
													if features[22][15] <= 2.5:
														pixels_low.append((22, 15))
														if features[22][17] <= 21.0:
															pixels_low.append((22, 17))
															ans = 9															 # approximately 12 were 9 out of 12 samples at leaf node
														else:
															pixels_high.append((22, 17))
															if features[15][19] <= 14.0:
																pixels_low.append((15, 19))
																if features[9][6] <= 126.5:
																	pixels_low.append((9, 6))
																	ans = 9																	 # approximately 1 were 9 out of 1 samples at leaf node
																else:
																	pixels_high.append((9, 6))
																	ans = 5																	 # approximately 1 were 5 out of 1 samples at leaf node
															else:
																pixels_high.append((15, 19))
																ans = 8																 # approximately 4 were 8 out of 4 samples at leaf node
													else:
														pixels_high.append((22, 15))
														if features[7][11] <= 216.5:
															pixels_low.append((7, 11))
															if features[19][14] <= 204.5:
																pixels_low.append((19, 14))
																if features[8][17] <= 127.0:
																	pixels_low.append((8, 17))
																	ans = 9																	 # approximately 1 were 9 out of 1 samples at leaf node
																else:
																	pixels_high.append((8, 17))
																	ans = 8																	 # approximately 1 were 8 out of 1 samples at leaf node
															else:
																pixels_high.append((19, 14))
																ans = 4																 # approximately 7 were 4 out of 7 samples at leaf node
														else:
															pixels_high.append((7, 11))
															if features[12][13] <= 7.0:
																pixels_low.append((12, 13))
																ans = 7																 # approximately 6 were 7 out of 6 samples at leaf node
															else:
																pixels_high.append((12, 13))
																if features[19][9] <= 69.0:
																	pixels_low.append((19, 9))
																	ans = 2																	 # approximately 1 were 2 out of 1 samples at leaf node
																else:
																	pixels_high.append((19, 9))
																	if features[19][11] <= 140.5:
																		pixels_low.append((19, 11))
																		ans = 5																		 # approximately 1 were 5 out of 1 samples at leaf node
																	else:
																		pixels_high.append((19, 11))
																		ans = 3																		 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											pixels_high.append((20, 13))
											if features[12][21] <= 90.5:
												pixels_low.append((12, 21))
												if features[9][10] <= 254.5:
													pixels_low.append((9, 10))
													if features[4][8] <= 65.0:
														pixels_low.append((4, 8))
														ans = 9														 # approximately 41 were 9 out of 41 samples at leaf node
													else:
														pixels_high.append((4, 8))
														ans = 7														 # approximately 1 were 7 out of 1 samples at leaf node
												else:
													pixels_high.append((9, 10))
													if features[11][22] <= 92.0:
														pixels_low.append((11, 22))
														ans = 4														 # approximately 1 were 4 out of 1 samples at leaf node
													else:
														pixels_high.append((11, 22))
														if features[9][12] <= 127.5:
															pixels_low.append((9, 12))
															ans = 3															 # approximately 1 were 3 out of 1 samples at leaf node
														else:
															pixels_high.append((9, 12))
															ans = 5															 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												pixels_high.append((12, 21))
												if features[9][12] <= 158.5:
													pixels_low.append((9, 12))
													ans = 7													 # approximately 3 were 7 out of 3 samples at leaf node
												else:
													pixels_high.append((9, 12))
													if features[13][11] <= 220.5:
														pixels_low.append((13, 11))
														if features[21][11] <= 126.0:
															pixels_low.append((21, 11))
															if features[17][21] <= 125.5:
																pixels_low.append((17, 21))
																ans = 4																 # approximately 1 were 4 out of 1 samples at leaf node
															else:
																pixels_high.append((17, 21))
																ans = 0																 # approximately 1 were 0 out of 1 samples at leaf node
														else:
															pixels_high.append((21, 11))
															ans = 8															 # approximately 2 were 8 out of 2 samples at leaf node
													else:
														pixels_high.append((13, 11))
														ans = 3														 # approximately 2 were 3 out of 2 samples at leaf node
							else:
								pixels_high.append((23, 6))
								if features[19][12] <= 11.0:
									pixels_low.append((19, 12))
									if features[16][11] <= 106.0:
										pixels_low.append((16, 11))
										ans = 5										 # approximately 65 were 5 out of 65 samples at leaf node
									else:
										pixels_high.append((16, 11))
										ans = 3										 # approximately 1 were 3 out of 1 samples at leaf node
								else:
									pixels_high.append((19, 12))
									if features[19][6] <= 15.5:
										pixels_low.append((19, 6))
										if features[11][10] <= 118.0:
											pixels_low.append((11, 10))
											ans = 8											 # approximately 4 were 8 out of 4 samples at leaf node
										else:
											pixels_high.append((11, 10))
											if features[15][25] <= 156.5:
												pixels_low.append((15, 25))
												ans = 4												 # approximately 39 were 4 out of 39 samples at leaf node
											else:
												pixels_high.append((15, 25))
												if features[13][21] <= 233.0:
													pixels_low.append((13, 21))
													ans = 9													 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													pixels_high.append((13, 21))
													ans = 7													 # approximately 1 were 7 out of 1 samples at leaf node
									else:
										pixels_high.append((19, 6))
										if features[12][10] <= 80.0:
											pixels_low.append((12, 10))
											ans = 8											 # approximately 10 were 8 out of 10 samples at leaf node
										else:
											pixels_high.append((12, 10))
											if features[17][12] <= 239.0:
												pixels_low.append((17, 12))
												ans = 9												 # approximately 12 were 9 out of 12 samples at leaf node
											else:
												pixels_high.append((17, 12))
												if features[13][12] <= 85.5:
													pixels_low.append((13, 12))
													ans = 8													 # approximately 3 were 8 out of 3 samples at leaf node
												else:
													pixels_high.append((13, 12))
													if features[9][8] <= 118.5:
														pixels_low.append((9, 8))
														ans = 5														 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														pixels_high.append((9, 8))
														ans = 3														 # approximately 1 were 3 out of 1 samples at leaf node
				else:
					pixels_high.append((9, 20))
					if features[20][3] <= 2.0:
						pixels_low.append((20, 3))
						if features[12][17] <= 8.5:
							pixels_low.append((12, 17))
							if features[19][12] <= 2.5:
								pixels_low.append((19, 12))
								if features[16][11] <= 117.5:
									pixels_low.append((16, 11))
									if features[9][17] <= 171.5:
										pixels_low.append((9, 17))
										if features[10][17] <= 253.5:
											pixels_low.append((10, 17))
											if features[17][11] <= 130.5:
												pixels_low.append((17, 11))
												if features[8][5] <= 31.5:
													pixels_low.append((8, 5))
													if features[20][12] <= 28.0:
														pixels_low.append((20, 12))
														ans = 5														 # approximately 175 were 5 out of 175 samples at leaf node
													else:
														pixels_high.append((20, 12))
														ans = 2														 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													pixels_high.append((8, 5))
													if features[16][21] <= 120.0:
														pixels_low.append((16, 21))
														ans = 5														 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														pixels_high.append((16, 21))
														ans = 3														 # approximately 2 were 3 out of 2 samples at leaf node
											else:
												pixels_high.append((17, 11))
												if features[25][17] <= 40.5:
													pixels_low.append((25, 17))
													ans = 0													 # approximately 1 were 0 out of 1 samples at leaf node
												else:
													pixels_high.append((25, 17))
													ans = 2													 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											pixels_high.append((10, 17))
											ans = 8											 # approximately 2 were 8 out of 2 samples at leaf node
									else:
										pixels_high.append((9, 17))
										if features[19][4] <= 6.5:
											pixels_low.append((19, 4))
											if features[20][14] <= 39.5:
												pixels_low.append((20, 14))
												ans = 5												 # approximately 9 were 5 out of 9 samples at leaf node
											else:
												pixels_high.append((20, 14))
												if features[21][10] <= 95.0:
													pixels_low.append((21, 10))
													ans = 6													 # approximately 1 were 6 out of 1 samples at leaf node
												else:
													pixels_high.append((21, 10))
													ans = 8													 # approximately 2 were 8 out of 2 samples at leaf node
										else:
											pixels_high.append((19, 4))
											ans = 6											 # approximately 12 were 6 out of 12 samples at leaf node
								else:
									pixels_high.append((16, 11))
									if features[9][19] <= 1.5:
										pixels_low.append((9, 19))
										if features[8][12] <= 186.5:
											pixels_low.append((8, 12))
											ans = 3											 # approximately 27 were 3 out of 27 samples at leaf node
										else:
											pixels_high.append((8, 12))
											ans = 9											 # approximately 1 were 9 out of 1 samples at leaf node
									else:
										pixels_high.append((9, 19))
										if features[9][17] <= 69.5:
											pixels_low.append((9, 17))
											if features[13][11] <= 104.5:
												pixels_low.append((13, 11))
												ans = 3												 # approximately 8 were 3 out of 8 samples at leaf node
											else:
												pixels_high.append((13, 11))
												if features[17][14] <= 30.0:
													pixels_low.append((17, 14))
													ans = 0													 # approximately 1 were 0 out of 1 samples at leaf node
												else:
													pixels_high.append((17, 14))
													if features[18][23] <= 234.5:
														pixels_low.append((18, 23))
														ans = 5														 # approximately 14 were 5 out of 14 samples at leaf node
													else:
														pixels_high.append((18, 23))
														ans = 3														 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											pixels_high.append((9, 17))
											if features[15][17] <= 221.0:
												pixels_low.append((15, 17))
												ans = 8												 # approximately 8 were 8 out of 8 samples at leaf node
											else:
												pixels_high.append((15, 17))
												if features[12][12] <= 135.0:
													pixels_low.append((12, 12))
													ans = 2													 # approximately 5 were 2 out of 5 samples at leaf node
												else:
													pixels_high.append((12, 12))
													if features[12][15] <= 201.5:
														pixels_low.append((12, 15))
														ans = 5														 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														pixels_high.append((12, 15))
														ans = 6														 # approximately 1 were 6 out of 1 samples at leaf node
							else:
								pixels_high.append((19, 12))
								if features[15][14] <= 20.5:
									pixels_low.append((15, 14))
									if features[11][22] <= 31.0:
										pixels_low.append((11, 22))
										if features[12][9] <= 6.0:
											pixels_low.append((12, 9))
											ans = 2											 # approximately 3 were 2 out of 3 samples at leaf node
										else:
											pixels_high.append((12, 9))
											if features[13][21] <= 74.5:
												pixels_low.append((13, 21))
												if features[9][16] <= 118.0:
													pixels_low.append((9, 16))
													ans = 3													 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													pixels_high.append((9, 16))
													ans = 0													 # approximately 1 were 0 out of 1 samples at leaf node
											else:
												pixels_high.append((13, 21))
												ans = 5												 # approximately 3 were 5 out of 3 samples at leaf node
									else:
										pixels_high.append((11, 22))
										if features[24][5] <= 250.0:
											pixels_low.append((24, 5))
											ans = 0											 # approximately 58 were 0 out of 58 samples at leaf node
										else:
											pixels_high.append((24, 5))
											ans = 5											 # approximately 2 were 5 out of 2 samples at leaf node
								else:
									pixels_high.append((15, 14))
									if features[8][16] <= 34.0:
										pixels_low.append((8, 16))
										if features[16][20] <= 2.0:
											pixels_low.append((16, 20))
											if features[14][9] <= 14.0:
												pixels_low.append((14, 9))
												ans = 2												 # approximately 3 were 2 out of 3 samples at leaf node
											else:
												pixels_high.append((14, 9))
												if features[10][21] <= 163.0:
													pixels_low.append((10, 21))
													if features[13][8] <= 91.0:
														pixels_low.append((13, 8))
														ans = 5														 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														pixels_high.append((13, 8))
														ans = 3														 # approximately 4 were 3 out of 4 samples at leaf node
												else:
													pixels_high.append((10, 21))
													if features[11][20] <= 224.5:
														pixels_low.append((11, 20))
														ans = 5														 # approximately 2 were 5 out of 2 samples at leaf node
													else:
														pixels_high.append((11, 20))
														ans = 9														 # approximately 4 were 9 out of 4 samples at leaf node
										else:
											pixels_high.append((16, 20))
											if features[8][14] <= 231.0:
												pixels_low.append((8, 14))
												ans = 3												 # approximately 40 were 3 out of 40 samples at leaf node
											else:
												pixels_high.append((8, 14))
												if features[17][12] <= 241.5:
													pixels_low.append((17, 12))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													pixels_high.append((17, 12))
													ans = 9													 # approximately 1 were 9 out of 1 samples at leaf node
									else:
										pixels_high.append((8, 16))
										if features[10][12] <= 15.0:
											pixels_low.append((10, 12))
											if features[18][16] <= 125.5:
												pixels_low.append((18, 16))
												if features[20][15] <= 186.0:
													pixels_low.append((20, 15))
													if features[12][6] <= 45.0:
														pixels_low.append((12, 6))
														if features[11][14] <= 236.0:
															pixels_low.append((11, 14))
															ans = 3															 # approximately 1 were 3 out of 1 samples at leaf node
														else:
															pixels_high.append((11, 14))
															ans = 5															 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														pixels_high.append((12, 6))
														ans = 2														 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													pixels_high.append((20, 15))
													ans = 8													 # approximately 2 were 8 out of 2 samples at leaf node
											else:
												pixels_high.append((18, 16))
												ans = 2												 # approximately 11 were 2 out of 11 samples at leaf node
										else:
											pixels_high.append((10, 12))
											if features[22][9] <= 158.0:
												pixels_low.append((22, 9))
												if features[13][8] <= 162.0:
													pixels_low.append((13, 8))
													ans = 6													 # approximately 4 were 6 out of 4 samples at leaf node
												else:
													pixels_high.append((13, 8))
													if features[11][9] <= 237.0:
														pixels_low.append((11, 9))
														if features[21][19] <= 187.5:
															pixels_low.append((21, 19))
															if features[8][8] <= 11.0:
																pixels_low.append((8, 8))
																ans = 0																 # approximately 2 were 0 out of 2 samples at leaf node
															else:
																pixels_high.append((8, 8))
																if features[6][13] <= 58.0:
																	pixels_low.append((6, 13))
																	ans = 5																	 # approximately 2 were 5 out of 2 samples at leaf node
																else:
																	pixels_high.append((6, 13))
																	ans = 8																	 # approximately 1 were 8 out of 1 samples at leaf node
														else:
															pixels_high.append((21, 19))
															ans = 3															 # approximately 3 were 3 out of 3 samples at leaf node
													else:
														pixels_high.append((11, 9))
														ans = 9														 # approximately 3 were 9 out of 3 samples at leaf node
											else:
												pixels_high.append((22, 9))
												if features[9][20] <= 13.5:
													pixels_low.append((9, 20))
													ans = 4													 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													pixels_high.append((9, 20))
													ans = 8													 # approximately 6 were 8 out of 6 samples at leaf node
						else:
							pixels_high.append((12, 17))
							if features[13][23] <= 2.0:
								pixels_low.append((13, 23))
								if features[21][18] <= 4.0:
									pixels_low.append((21, 18))
									if features[16][11] <= 248.0:
										pixels_low.append((16, 11))
										if features[17][15] <= 48.5:
											pixels_low.append((17, 15))
											if features[19][16] <= 19.5:
												pixels_low.append((19, 16))
												if features[17][11] <= 175.0:
													pixels_low.append((17, 11))
													if features[12][16] <= 152.5:
														pixels_low.append((12, 16))
														if features[14][18] <= 181.0:
															pixels_low.append((14, 18))
															ans = 9															 # approximately 2 were 9 out of 2 samples at leaf node
														else:
															pixels_high.append((14, 18))
															ans = 5															 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														pixels_high.append((12, 16))
														ans = 8														 # approximately 39 were 8 out of 39 samples at leaf node
												else:
													pixels_high.append((17, 11))
													if features[9][18] <= 252.5:
														pixels_low.append((9, 18))
														if features[23][6] <= 54.5:
															pixels_low.append((23, 6))
															if features[16][6] <= 175.5:
																pixels_low.append((16, 6))
																if features[10][16] <= 9.5:
																	pixels_low.append((10, 16))
																	ans = 9																	 # approximately 1 were 9 out of 1 samples at leaf node
																else:
																	pixels_high.append((10, 16))
																	ans = 7																	 # approximately 2 were 7 out of 2 samples at leaf node
															else:
																pixels_high.append((16, 6))
																ans = 2																 # approximately 3 were 2 out of 3 samples at leaf node
														else:
															pixels_high.append((23, 6))
															ans = 4															 # approximately 4 were 4 out of 4 samples at leaf node
													else:
														pixels_high.append((9, 18))
														ans = 8														 # approximately 4 were 8 out of 4 samples at leaf node
											else:
												pixels_high.append((19, 16))
												if features[11][8] <= 126.5:
													pixels_low.append((11, 8))
													ans = 6													 # approximately 8 were 6 out of 8 samples at leaf node
												else:
													pixels_high.append((11, 8))
													ans = 8													 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											pixels_high.append((17, 15))
											if features[11][11] <= 5.5:
												pixels_low.append((11, 11))
												if features[7][17] <= 16.0:
													pixels_low.append((7, 17))
													if features[13][8] <= 169.5:
														pixels_low.append((13, 8))
														if features[20][11] <= 48.0:
															pixels_low.append((20, 11))
															if features[8][9] <= 127.0:
																pixels_low.append((8, 9))
																ans = 6																 # approximately 11 were 6 out of 11 samples at leaf node
															else:
																pixels_high.append((8, 9))
																ans = 4																 # approximately 1 were 4 out of 1 samples at leaf node
														else:
															pixels_high.append((20, 11))
															if features[14][17] <= 246.0:
																pixels_low.append((14, 17))
																ans = 3																 # approximately 2 were 3 out of 2 samples at leaf node
															else:
																pixels_high.append((14, 17))
																if features[10][7] <= 10.0:
																	pixels_low.append((10, 7))
																	if features[21][8] <= 70.5:
																		pixels_low.append((21, 8))
																		ans = 9																		 # approximately 1 were 9 out of 1 samples at leaf node
																	else:
																		pixels_high.append((21, 8))
																		if features[13][20] <= 116.0:
																			pixels_low.append((13, 20))
																			ans = 2																			 # approximately 1 were 2 out of 1 samples at leaf node
																		else:
																			pixels_high.append((13, 20))
																			ans = 0																			 # approximately 1 were 0 out of 1 samples at leaf node
																else:
																	pixels_high.append((10, 7))
																	ans = 8																	 # approximately 2 were 8 out of 2 samples at leaf node
													else:
														pixels_high.append((13, 8))
														if features[18][18] <= 102.5:
															pixels_low.append((18, 18))
															ans = 7															 # approximately 16 were 7 out of 16 samples at leaf node
														else:
															pixels_high.append((18, 18))
															ans = 3															 # approximately 2 were 3 out of 2 samples at leaf node
												else:
													pixels_high.append((7, 17))
													if features[13][12] <= 244.5:
														pixels_low.append((13, 12))
														if features[12][12] <= 112.0:
															pixels_low.append((12, 12))
															if features[5][13] <= 143.0:
																pixels_low.append((5, 13))
																if features[5][24] <= 72.0:
																	pixels_low.append((5, 24))
																	ans = 2																	 # approximately 34 were 2 out of 34 samples at leaf node
																else:
																	pixels_high.append((5, 24))
																	ans = 7																	 # approximately 1 were 7 out of 1 samples at leaf node
															else:
																pixels_high.append((5, 13))
																ans = 9																 # approximately 1 were 9 out of 1 samples at leaf node
														else:
															pixels_high.append((12, 12))
															if features[13][19] <= 149.0:
																pixels_low.append((13, 19))
																ans = 6																 # approximately 1 were 6 out of 1 samples at leaf node
															else:
																pixels_high.append((13, 19))
																ans = 3																 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														pixels_high.append((13, 12))
														if features[13][15] <= 167.5:
															pixels_low.append((13, 15))
															if features[15][8] <= 245.5:
																pixels_low.append((15, 8))
																ans = 5																 # approximately 1 were 5 out of 1 samples at leaf node
															else:
																pixels_high.append((15, 8))
																if features[24][8] <= 4.0:
																	pixels_low.append((24, 8))
																	ans = 4																	 # approximately 1 were 4 out of 1 samples at leaf node
																else:
																	pixels_high.append((24, 8))
																	ans = 0																	 # approximately 1 were 0 out of 1 samples at leaf node
														else:
															pixels_high.append((13, 15))
															ans = 8															 # approximately 4 were 8 out of 4 samples at leaf node
											else:
												pixels_high.append((11, 11))
												if features[17][8] <= 60.0:
													pixels_low.append((17, 8))
													if features[19][5] <= 1.0:
														pixels_low.append((19, 5))
														if features[17][6] <= 211.0:
															pixels_low.append((17, 6))
															ans = 4															 # approximately 33 were 4 out of 33 samples at leaf node
														else:
															pixels_high.append((17, 6))
															ans = 9															 # approximately 1 were 9 out of 1 samples at leaf node
													else:
														pixels_high.append((19, 5))
														if features[21][13] <= 10.5:
															pixels_low.append((21, 13))
															if features[10][14] <= 181.5:
																pixels_low.append((10, 14))
																ans = 9																 # approximately 1 were 9 out of 1 samples at leaf node
															else:
																pixels_high.append((10, 14))
																ans = 6																 # approximately 2 were 6 out of 2 samples at leaf node
														else:
															pixels_high.append((21, 13))
															ans = 8															 # approximately 3 were 8 out of 3 samples at leaf node
												else:
													pixels_high.append((17, 8))
													if features[7][25] <= 2.5:
														pixels_low.append((7, 25))
														if features[23][12] <= 26.0:
															pixels_low.append((23, 12))
															if features[20][8] <= 26.0:
																pixels_low.append((20, 8))
																if features[17][19] <= 4.0:
																	pixels_low.append((17, 19))
																	ans = 4																	 # approximately 7 were 4 out of 7 samples at leaf node
																else:
																	pixels_high.append((17, 19))
																	if features[16][14] <= 126.5:
																		pixels_low.append((16, 14))
																		if features[17][11] <= 137.5:
																			pixels_low.append((17, 11))
																			ans = 3																			 # approximately 1 were 3 out of 1 samples at leaf node
																		else:
																			pixels_high.append((17, 11))
																			ans = 4																			 # approximately 1 were 4 out of 1 samples at leaf node
																	else:
																		pixels_high.append((16, 14))
																		ans = 6																		 # approximately 5 were 6 out of 5 samples at leaf node
															else:
																pixels_high.append((20, 8))
																if features[19][12] <= 24.0:
																	pixels_low.append((19, 12))
																	if features[16][10] <= 247.5:
																		pixels_low.append((16, 10))
																		ans = 5																		 # approximately 9 were 5 out of 9 samples at leaf node
																	else:
																		pixels_high.append((16, 10))
																		ans = 6																		 # approximately 1 were 6 out of 1 samples at leaf node
																else:
																	pixels_high.append((19, 12))
																	if features[6][17] <= 249.0:
																		pixels_low.append((6, 17))
																		if features[16][11] <= 3.0:
																			pixels_low.append((16, 11))
																			if features[14][7] <= 95.0:
																				pixels_low.append((14, 7))
																				if features[9][17] <= 6.5:
																					pixels_low.append((9, 17))
																					ans = 8																					 # approximately 1 were 8 out of 1 samples at leaf node
																				else:
																					pixels_high.append((9, 17))
																					ans = 4																					 # approximately 1 were 4 out of 1 samples at leaf node
																			else:
																				pixels_high.append((14, 7))
																				ans = 2																				 # approximately 2 were 2 out of 2 samples at leaf node
																		else:
																			pixels_high.append((16, 11))
																			ans = 9																			 # approximately 3 were 9 out of 3 samples at leaf node
																	else:
																		pixels_high.append((6, 17))
																		ans = 0																		 # approximately 3 were 0 out of 3 samples at leaf node
														else:
															pixels_high.append((23, 12))
															if features[19][18] <= 29.5:
																pixels_low.append((19, 18))
																ans = 8																 # approximately 8 were 8 out of 8 samples at leaf node
															else:
																pixels_high.append((19, 18))
																if features[12][10] <= 172.5:
																	pixels_low.append((12, 10))
																	ans = 0																	 # approximately 1 were 0 out of 1 samples at leaf node
																else:
																	pixels_high.append((12, 10))
																	ans = 3																	 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														pixels_high.append((7, 25))
														if features[19][7] <= 58.0:
															pixels_low.append((19, 7))
															ans = 7															 # approximately 3 were 7 out of 3 samples at leaf node
														else:
															pixels_high.append((19, 7))
															if features[8][23] <= 121.0:
																pixels_low.append((8, 23))
																ans = 8																 # approximately 2 were 8 out of 2 samples at leaf node
															else:
																pixels_high.append((8, 23))
																if features[14][7] <= 253.5:
																	pixels_low.append((14, 7))
																	ans = 9																	 # approximately 22 were 9 out of 22 samples at leaf node
																else:
																	pixels_high.append((14, 7))
																	ans = 7																	 # approximately 1 were 7 out of 1 samples at leaf node
									else:
										pixels_high.append((16, 11))
										if features[19][5] <= 74.5:
											pixels_low.append((19, 5))
											if features[9][25] <= 19.0:
												pixels_low.append((9, 25))
												if features[19][9] <= 44.5:
													pixels_low.append((19, 9))
													ans = 2													 # approximately 5 were 2 out of 5 samples at leaf node
												else:
													pixels_high.append((19, 9))
													if features[9][16] <= 226.0:
														pixels_low.append((9, 16))
														if features[23][8] <= 39.5:
															pixels_low.append((23, 8))
															if features[12][8] <= 98.5:
																pixels_low.append((12, 8))
																if features[8][22] <= 133.5:
																	pixels_low.append((8, 22))
																	ans = 4																	 # approximately 2 were 4 out of 2 samples at leaf node
																else:
																	pixels_high.append((8, 22))
																	if features[22][10] <= 94.5:
																		pixels_low.append((22, 10))
																		ans = 9																		 # approximately 1 were 9 out of 1 samples at leaf node
																	else:
																		pixels_high.append((22, 10))
																		ans = 1																		 # approximately 1 were 1 out of 1 samples at leaf node
															else:
																pixels_high.append((12, 8))
																ans = 8																 # approximately 2 were 8 out of 2 samples at leaf node
														else:
															pixels_high.append((23, 8))
															ans = 5															 # approximately 3 were 5 out of 3 samples at leaf node
													else:
														pixels_high.append((9, 16))
														ans = 0														 # approximately 4 were 0 out of 4 samples at leaf node
											else:
												pixels_high.append((9, 25))
												if features[11][20] <= 160.0:
													pixels_low.append((11, 20))
													ans = 1													 # approximately 1 were 1 out of 1 samples at leaf node
												else:
													pixels_high.append((11, 20))
													ans = 7													 # approximately 7 were 7 out of 7 samples at leaf node
										else:
											pixels_high.append((19, 5))
											if features[13][11] <= 252.5:
												pixels_low.append((13, 11))
												ans = 1												 # approximately 57 were 1 out of 57 samples at leaf node
											else:
												pixels_high.append((13, 11))
												ans = 0												 # approximately 1 were 0 out of 1 samples at leaf node
								else:
									pixels_high.append((21, 18))
									if features[9][13] <= 195.5:
										pixels_low.append((9, 13))
										if features[4][9] <= 253.5:
											pixels_low.append((4, 9))
											if features[4][14] <= 6.5:
												pixels_low.append((4, 14))
												if features[6][24] <= 28.5:
													pixels_low.append((6, 24))
													if features[4][6] <= 170.5:
														pixels_low.append((4, 6))
														ans = 2														 # approximately 76 were 2 out of 76 samples at leaf node
													else:
														pixels_high.append((4, 6))
														ans = 3														 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													pixels_high.append((6, 24))
													ans = 7													 # approximately 1 were 7 out of 1 samples at leaf node
											else:
												pixels_high.append((4, 14))
												if features[18][7] <= 198.5:
													pixels_low.append((18, 7))
													ans = 9													 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													pixels_high.append((18, 7))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											pixels_high.append((4, 9))
											ans = 3											 # approximately 2 were 3 out of 2 samples at leaf node
									else:
										pixels_high.append((9, 13))
										if features[16][15] <= 251.5:
											pixels_low.append((16, 15))
											ans = 8											 # approximately 2 were 8 out of 2 samples at leaf node
										else:
											pixels_high.append((16, 15))
											if features[12][10] <= 211.5:
												pixels_low.append((12, 10))
												if features[14][22] <= 10.5:
													pixels_low.append((14, 22))
													if features[18][9] <= 232.5:
														pixels_low.append((18, 9))
														ans = 4														 # approximately 1 were 4 out of 1 samples at leaf node
													else:
														pixels_high.append((18, 9))
														ans = 2														 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													pixels_high.append((14, 22))
													ans = 6													 # approximately 2 were 6 out of 2 samples at leaf node
											else:
												pixels_high.append((12, 10))
												ans = 0												 # approximately 2 were 0 out of 2 samples at leaf node
							else:
								pixels_high.append((13, 23))
								if features[13][8] <= 6.0:
									pixels_low.append((13, 8))
									if features[12][18] <= 243.5:
										pixels_low.append((12, 18))
										if features[16][18] <= 126.5:
											pixels_low.append((16, 18))
											ans = 8											 # approximately 5 were 8 out of 5 samples at leaf node
										else:
											pixels_high.append((16, 18))
											if features[20][4] <= 138.5:
												pixels_low.append((20, 4))
												if features[15][7] <= 83.5:
													pixels_low.append((15, 7))
													ans = 0													 # approximately 2 were 0 out of 2 samples at leaf node
												else:
													pixels_high.append((15, 7))
													if features[14][21] <= 207.5:
														pixels_low.append((14, 21))
														ans = 5														 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														pixels_high.append((14, 21))
														ans = 2														 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												pixels_high.append((20, 4))
												ans = 6												 # approximately 3 were 6 out of 3 samples at leaf node
									else:
										pixels_high.append((12, 18))
										ans = 1										 # approximately 16 were 1 out of 16 samples at leaf node
								else:
									pixels_high.append((13, 8))
									if features[19][16] <= 81.0:
										pixels_low.append((19, 16))
										if features[5][7] <= 129.0:
											pixels_low.append((5, 7))
											if features[14][11] <= 253.5:
												pixels_low.append((14, 11))
												if features[20][21] <= 232.0:
													pixels_low.append((20, 21))
													if features[7][15] <= 237.0:
														pixels_low.append((7, 15))
														if features[4][10] <= 234.5:
															pixels_low.append((4, 10))
															if features[19][4] <= 219.0:
																pixels_low.append((19, 4))
																if features[14][21] <= 254.5:
																	pixels_low.append((14, 21))
																	ans = 8																	 # approximately 230 were 8 out of 230 samples at leaf node
																else:
																	pixels_high.append((14, 21))
																	if features[8][19] <= 47.5:
																		pixels_low.append((8, 19))
																		ans = 5																		 # approximately 1 were 5 out of 1 samples at leaf node
																	else:
																		pixels_high.append((8, 19))
																		ans = 8																		 # approximately 3 were 8 out of 3 samples at leaf node
															else:
																pixels_high.append((19, 4))
																ans = 0																 # approximately 1 were 0 out of 1 samples at leaf node
														else:
															pixels_high.append((4, 10))
															ans = 3															 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														pixels_high.append((7, 15))
														ans = 4														 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													pixels_high.append((20, 21))
													ans = 2													 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												pixels_high.append((14, 11))
												if features[20][12] <= 162.0:
													pixels_low.append((20, 12))
													if features[12][17] <= 131.5:
														pixels_low.append((12, 17))
														ans = 0														 # approximately 1 were 0 out of 1 samples at leaf node
													else:
														pixels_high.append((12, 17))
														if features[12][18] <= 141.5:
															pixels_low.append((12, 18))
															ans = 5															 # approximately 1 were 5 out of 1 samples at leaf node
														else:
															pixels_high.append((12, 18))
															ans = 7															 # approximately 1 were 7 out of 1 samples at leaf node
												else:
													pixels_high.append((20, 12))
													ans = 8													 # approximately 2 were 8 out of 2 samples at leaf node
										else:
											pixels_high.append((5, 7))
											ans = 2											 # approximately 5 were 2 out of 5 samples at leaf node
									else:
										pixels_high.append((19, 16))
										if features[10][19] <= 68.5:
											pixels_low.append((10, 19))
											if features[10][13] <= 36.5:
												pixels_low.append((10, 13))
												ans = 3												 # approximately 4 were 3 out of 4 samples at leaf node
											else:
												pixels_high.append((10, 13))
												if features[8][16] <= 252.5:
													pixels_low.append((8, 16))
													ans = 5													 # approximately 6 were 5 out of 6 samples at leaf node
												else:
													pixels_high.append((8, 16))
													if features[11][20] <= 123.0:
														pixels_low.append((11, 20))
														if features[21][6] <= 254.0:
															pixels_low.append((21, 6))
															ans = 6															 # approximately 1 were 6 out of 1 samples at leaf node
														else:
															pixels_high.append((21, 6))
															ans = 8															 # approximately 1 were 8 out of 1 samples at leaf node
													else:
														pixels_high.append((11, 20))
														ans = 9														 # approximately 1 were 9 out of 1 samples at leaf node
										else:
											pixels_high.append((10, 19))
											if features[9][10] <= 9.0:
												pixels_low.append((9, 10))
												if features[13][6] <= 6.5:
													pixels_low.append((13, 6))
													ans = 6													 # approximately 3 were 6 out of 3 samples at leaf node
												else:
													pixels_high.append((13, 6))
													if features[14][15] <= 155.5:
														pixels_low.append((14, 15))
														ans = 0														 # approximately 3 were 0 out of 3 samples at leaf node
													else:
														pixels_high.append((14, 15))
														if features[12][14] <= 194.5:
															pixels_low.append((12, 14))
															ans = 2															 # approximately 2 were 2 out of 2 samples at leaf node
														else:
															pixels_high.append((12, 14))
															if features[12][16] <= 126.5:
																pixels_low.append((12, 16))
																ans = 3																 # approximately 1 were 3 out of 1 samples at leaf node
															else:
																pixels_high.append((12, 16))
																ans = 8																 # approximately 2 were 8 out of 2 samples at leaf node
											else:
												pixels_high.append((9, 10))
												if features[21][7] <= 253.5:
													pixels_low.append((21, 7))
													if features[18][5] <= 252.5:
														pixels_low.append((18, 5))
														ans = 8														 # approximately 21 were 8 out of 21 samples at leaf node
													else:
														pixels_high.append((18, 5))
														ans = 5														 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													pixels_high.append((21, 7))
													ans = 4													 # approximately 1 were 4 out of 1 samples at leaf node
					else:
						pixels_high.append((20, 3))
						if features[20][9] <= 48.0:
							pixels_low.append((20, 9))
							if features[18][10] <= 164.0:
								pixels_low.append((18, 10))
								if features[25][5] <= 39.0:
									pixels_low.append((25, 5))
									if features[11][8] <= 22.5:
										pixels_low.append((11, 8))
										if features[15][22] <= 242.0:
											pixels_low.append((15, 22))
											if features[9][19] <= 2.0:
												pixels_low.append((9, 19))
												if features[19][17] <= 33.5:
													pixels_low.append((19, 17))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													pixels_high.append((19, 17))
													ans = 6													 # approximately 3 were 6 out of 3 samples at leaf node
											else:
												pixels_high.append((9, 19))
												ans = 6												 # approximately 202 were 6 out of 202 samples at leaf node
										else:
											pixels_high.append((15, 22))
											if features[13][16] <= 76.5:
												pixels_low.append((13, 16))
												ans = 5												 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												pixels_high.append((13, 16))
												ans = 6												 # approximately 3 were 6 out of 3 samples at leaf node
									else:
										pixels_high.append((11, 8))
										if features[8][12] <= 187.5:
											pixels_low.append((8, 12))
											ans = 5											 # approximately 2 were 5 out of 2 samples at leaf node
										else:
											pixels_high.append((8, 12))
											ans = 6											 # approximately 2 were 6 out of 2 samples at leaf node
								else:
									pixels_high.append((25, 5))
									ans = 5									 # approximately 1 were 5 out of 1 samples at leaf node
							else:
								pixels_high.append((18, 10))
								if features[16][6] <= 179.0:
									pixels_low.append((16, 6))
									ans = 1									 # approximately 1 were 1 out of 1 samples at leaf node
								else:
									pixels_high.append((16, 6))
									ans = 0									 # approximately 1 were 0 out of 1 samples at leaf node
						else:
							pixels_high.append((20, 9))
							if features[16][13] <= 95.5:
								pixels_low.append((16, 13))
								ans = 0								 # approximately 5 were 0 out of 5 samples at leaf node
							else:
								pixels_high.append((16, 13))
								if features[10][17] <= 141.0:
									pixels_low.append((10, 17))
									if features[18][4] <= 64.0:
										pixels_low.append((18, 4))
										ans = 4										 # approximately 1 were 4 out of 1 samples at leaf node
									else:
										pixels_high.append((18, 4))
										ans = 3										 # approximately 1 were 3 out of 1 samples at leaf node
								else:
									pixels_high.append((10, 17))
									ans = 2									 # approximately 3 were 2 out of 3 samples at leaf node
	else:
		pixels_high.append((15, 5))
		if features[13][23] <= 0.5:
			pixels_low.append((13, 23))
			if features[18][9] <= 0.5:
				pixels_low.append((18, 9))
				if features[21][8] <= 10.5:
					pixels_low.append((21, 8))
					if features[16][10] <= 93.5:
						pixels_low.append((16, 10))
						if features[11][19] <= 7.5:
							pixels_low.append((11, 19))
							if features[9][19] <= 23.5:
								pixels_low.append((9, 19))
								if features[19][5] <= 6.0:
									pixels_low.append((19, 5))
									if features[13][11] <= 201.5:
										pixels_low.append((13, 11))
										if features[11][7] <= 33.5:
											pixels_low.append((11, 7))
											if features[20][19] <= 3.0:
												pixels_low.append((20, 19))
												if features[16][6] <= 199.5:
													pixels_low.append((16, 6))
													if features[15][3] <= 184.5:
														pixels_low.append((15, 3))
														ans = 4														 # approximately 20 were 4 out of 20 samples at leaf node
													else:
														pixels_high.append((15, 3))
														ans = 6														 # approximately 1 were 6 out of 1 samples at leaf node
												else:
													pixels_high.append((16, 6))
													ans = 9													 # approximately 2 were 9 out of 2 samples at leaf node
											else:
												pixels_high.append((20, 19))
												if features[14][10] <= 47.0:
													pixels_low.append((14, 10))
													if features[19][15] <= 179.0:
														pixels_low.append((19, 15))
														ans = 6														 # approximately 3 were 6 out of 3 samples at leaf node
													else:
														pixels_high.append((19, 15))
														if features[22][18] <= 87.5:
															pixels_low.append((22, 18))
															ans = 2															 # approximately 1 were 2 out of 1 samples at leaf node
														else:
															pixels_high.append((22, 18))
															ans = 5															 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													pixels_high.append((14, 10))
													ans = 3													 # approximately 3 were 3 out of 3 samples at leaf node
										else:
											pixels_high.append((11, 7))
											if features[18][12] <= 31.5:
												pixels_low.append((18, 12))
												if features[6][10] <= 160.0:
													pixels_low.append((6, 10))
													if features[13][14] <= 254.5:
														pixels_low.append((13, 14))
														ans = 5														 # approximately 17 were 5 out of 17 samples at leaf node
													else:
														pixels_high.append((13, 14))
														ans = 9														 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													pixels_high.append((6, 10))
													ans = 8													 # approximately 2 were 8 out of 2 samples at leaf node
											else:
												pixels_high.append((18, 12))
												if features[13][22] <= 5.5:
													pixels_low.append((13, 22))
													if features[12][10] <= 121.0:
														pixels_low.append((12, 10))
														ans = 9														 # approximately 11 were 9 out of 11 samples at leaf node
													else:
														pixels_high.append((12, 10))
														ans = 4														 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													pixels_high.append((13, 22))
													if features[21][14] <= 63.0:
														pixels_low.append((21, 14))
														ans = 8														 # approximately 2 were 8 out of 2 samples at leaf node
													else:
														pixels_high.append((21, 14))
														ans = 6														 # approximately 1 were 6 out of 1 samples at leaf node
									else:
										pixels_high.append((13, 11))
										if features[15][15] <= 171.0:
											pixels_low.append((15, 15))
											ans = 3											 # approximately 19 were 3 out of 19 samples at leaf node
										else:
											pixels_high.append((15, 15))
											if features[13][6] <= 126.5:
												pixels_low.append((13, 6))
												ans = 5												 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												pixels_high.append((13, 6))
												if features[17][9] <= 6.5:
													pixels_low.append((17, 9))
													ans = 1													 # approximately 1 were 1 out of 1 samples at leaf node
												else:
													pixels_high.append((17, 9))
													ans = 8													 # approximately 1 were 8 out of 1 samples at leaf node
								else:
									pixels_high.append((19, 5))
									if features[20][10] <= 10.5:
										pixels_low.append((20, 10))
										if features[19][4] <= 253.5:
											pixels_low.append((19, 4))
											if features[5][23] <= 212.5:
												pixels_low.append((5, 23))
												ans = 5												 # approximately 43 were 5 out of 43 samples at leaf node
											else:
												pixels_high.append((5, 23))
												ans = 3												 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											pixels_high.append((19, 4))
											ans = 6											 # approximately 1 were 6 out of 1 samples at leaf node
									else:
										pixels_high.append((20, 10))
										if features[12][15] <= 253.5:
											pixels_low.append((12, 15))
											ans = 8											 # approximately 3 were 8 out of 3 samples at leaf node
										else:
											pixels_high.append((12, 15))
											ans = 2											 # approximately 1 were 2 out of 1 samples at leaf node
							else:
								pixels_high.append((9, 19))
								if features[9][15] <= 15.0:
									pixels_low.append((9, 15))
									if features[14][9] <= 251.5:
										pixels_low.append((14, 9))
										if features[6][22] <= 64.5:
											pixels_low.append((6, 22))
											if features[15][22] <= 4.0:
												pixels_low.append((15, 22))
												if features[14][19] <= 233.0:
													pixels_low.append((14, 19))
													ans = 6													 # approximately 6 were 6 out of 6 samples at leaf node
												else:
													pixels_high.append((14, 19))
													ans = 2													 # approximately 3 were 2 out of 3 samples at leaf node
											else:
												pixels_high.append((15, 22))
												if features[18][17] <= 1.5:
													pixels_low.append((18, 17))
													ans = 6													 # approximately 1 were 6 out of 1 samples at leaf node
												else:
													pixels_high.append((18, 17))
													ans = 5													 # approximately 6 were 5 out of 6 samples at leaf node
										else:
											pixels_high.append((6, 22))
											ans = 8											 # approximately 4 were 8 out of 4 samples at leaf node
									else:
										pixels_high.append((14, 9))
										ans = 3										 # approximately 8 were 3 out of 8 samples at leaf node
								else:
									pixels_high.append((9, 15))
									if features[14][21] <= 24.5:
										pixels_low.append((14, 21))
										if features[17][17] <= 161.5:
											pixels_low.append((17, 17))
											ans = 2											 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											pixels_high.append((17, 17))
											ans = 4											 # approximately 3 were 4 out of 3 samples at leaf node
									else:
										pixels_high.append((14, 21))
										if features[7][10] <= 110.5:
											pixels_low.append((7, 10))
											if features[19][9] <= 67.0:
												pixels_low.append((19, 9))
												ans = 6												 # approximately 79 were 6 out of 79 samples at leaf node
											else:
												pixels_high.append((19, 9))
												ans = 8												 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											pixels_high.append((7, 10))
											if features[12][13] <= 254.5:
												pixels_low.append((12, 13))
												ans = 8												 # approximately 2 were 8 out of 2 samples at leaf node
											else:
												pixels_high.append((12, 13))
												ans = 5												 # approximately 1 were 5 out of 1 samples at leaf node
						else:
							pixels_high.append((11, 19))
							if features[22][6] <= 95.5:
								pixels_low.append((22, 6))
								if features[19][8] <= 38.5:
									pixels_low.append((19, 8))
									if features[17][23] <= 3.0:
										pixels_low.append((17, 23))
										if features[15][11] <= 206.5:
											pixels_low.append((15, 11))
											if features[9][23] <= 120.5:
												pixels_low.append((9, 23))
												if features[10][3] <= 33.0:
													pixels_low.append((10, 3))
													if features[24][22] <= 79.0:
														pixels_low.append((24, 22))
														if features[3][20] <= 11.5:
															pixels_low.append((3, 20))
															if features[23][4] <= 249.0:
																pixels_low.append((23, 4))
																if features[10][24] <= 3.0:
																	pixels_low.append((10, 24))
																	if features[7][8] <= 253.5:
																		pixels_low.append((7, 8))
																		if features[9][5] <= 243.0:
																			pixels_low.append((9, 5))
																			if features[7][4] <= 244.5:
																				pixels_low.append((7, 4))
																				if features[26][11] <= 17.5:
																					pixels_low.append((26, 11))
																					if features[4][13] <= 25.5:
																						pixels_low.append((4, 13))
																						if features[14][12] <= 225.5:
																							pixels_low.append((14, 12))
																							if features[11][19] <= 110.5:
																								pixels_low.append((11, 19))
																								if features[18][22] <= 219.0:
																									pixels_low.append((18, 22))
																									if features[16][3] <= 254.5:
																										pixels_low.append((16, 3))
																										if features[18][18] <= 254.5:
																											pixels_low.append((18, 18))
																											if features[23][5] <= 129.5:
																												pixels_low.append((23, 5))
																												if features[16][22] <= 133.0:
																													pixels_low.append((16, 22))
																													if features[10][20] <= 254.5:
																														pixels_low.append((10, 20))
																														ans = 6																														 # approximately 129 were 6 out of 129 samples at leaf node
																													else:
																														pixels_high.append((10, 20))
																														if features[10][15] <= 254.5:
																															pixels_low.append((10, 15))
																															ans = 5																															 # approximately 1 were 5 out of 1 samples at leaf node
																														else:
																															pixels_high.append((10, 15))
																															ans = 6																															 # approximately 2 were 6 out of 2 samples at leaf node
																												else:
																													pixels_high.append((16, 22))
																													if features[14][13] <= 225.5:
																														pixels_low.append((14, 13))
																														ans = 6																														 # approximately 18 were 6 out of 18 samples at leaf node
																													else:
																														pixels_high.append((14, 13))
																														if features[21][16] <= 245.5:
																															pixels_low.append((21, 16))
																															ans = 5																															 # approximately 3 were 5 out of 3 samples at leaf node
																														else:
																															pixels_high.append((21, 16))
																															ans = 6																															 # approximately 1 were 6 out of 1 samples at leaf node
																											else:
																												pixels_high.append((23, 5))
																												ans = 5																												 # approximately 1 were 5 out of 1 samples at leaf node
																										else:
																											pixels_high.append((18, 18))
																											ans = 5																											 # approximately 1 were 5 out of 1 samples at leaf node
																									else:
																										pixels_high.append((16, 3))
																										ans = 4																										 # approximately 1 were 4 out of 1 samples at leaf node
																								else:
																									pixels_high.append((18, 22))
																									if features[23][14] <= 14.5:
																										pixels_low.append((23, 14))
																										ans = 5																										 # approximately 1 were 5 out of 1 samples at leaf node
																									else:
																										pixels_high.append((23, 14))
																										ans = 8																										 # approximately 1 were 8 out of 1 samples at leaf node
																							else:
																								pixels_high.append((11, 19))
																								if features[19][9] <= 41.5:
																									pixels_low.append((19, 9))
																									if features[15][21] <= 254.5:
																										pixels_low.append((15, 21))
																										ans = 6																										 # approximately 1662 were 6 out of 1662 samples at leaf node
																									else:
																										pixels_high.append((15, 21))
																										if features[9][7] <= 9.0:
																											pixels_low.append((9, 7))
																											ans = 6																											 # approximately 74 were 6 out of 74 samples at leaf node
																										else:
																											pixels_high.append((9, 7))
																											if features[17][14] <= 248.0:
																												pixels_low.append((17, 14))
																												ans = 5																												 # approximately 1 were 5 out of 1 samples at leaf node
																											else:
																												pixels_high.append((17, 14))
																												ans = 6																												 # approximately 4 were 6 out of 4 samples at leaf node
																								else:
																									pixels_high.append((19, 9))
																									if features[16][18] <= 221.5:
																										pixels_low.append((16, 18))
																										ans = 4																										 # approximately 1 were 4 out of 1 samples at leaf node
																									else:
																										pixels_high.append((16, 18))
																										ans = 6																										 # approximately 2 were 6 out of 2 samples at leaf node
																						else:
																							pixels_high.append((14, 12))
																							if features[10][17] <= 25.5:
																								pixels_low.append((10, 17))
																								if features[10][21] <= 73.5:
																									pixels_low.append((10, 21))
																									ans = 6																									 # approximately 1 were 6 out of 1 samples at leaf node
																								else:
																									pixels_high.append((10, 21))
																									ans = 5																									 # approximately 7 were 5 out of 7 samples at leaf node
																							else:
																								pixels_high.append((10, 17))
																								if features[12][13] <= 47.5:
																									pixels_low.append((12, 13))
																									if features[10][22] <= 37.5:
																										pixels_low.append((10, 22))
																										ans = 6																										 # approximately 2 were 6 out of 2 samples at leaf node
																									else:
																										pixels_high.append((10, 22))
																										if features[12][12] <= 205.0:
																											pixels_low.append((12, 12))
																											ans = 4																											 # approximately 1 were 4 out of 1 samples at leaf node
																										else:
																											pixels_high.append((12, 12))
																											if features[19][16] <= 164.5:
																												pixels_low.append((19, 16))
																												ans = 8																												 # approximately 1 were 8 out of 1 samples at leaf node
																											else:
																												pixels_high.append((19, 16))
																												if features[10][6] <= 1.0:
																													pixels_low.append((10, 6))
																													ans = 5																													 # approximately 1 were 5 out of 1 samples at leaf node
																												else:
																													pixels_high.append((10, 6))
																													ans = 3																													 # approximately 1 were 3 out of 1 samples at leaf node
																								else:
																									pixels_high.append((12, 13))
																									ans = 6																									 # approximately 90 were 6 out of 90 samples at leaf node
																					else:
																						pixels_high.append((4, 13))
																						ans = 5																						 # approximately 1 were 5 out of 1 samples at leaf node
																				else:
																					pixels_high.append((26, 11))
																					ans = 8																					 # approximately 1 were 8 out of 1 samples at leaf node
																			else:
																				pixels_high.append((7, 4))
																				ans = 3																				 # approximately 1 were 3 out of 1 samples at leaf node
																		else:
																			pixels_high.append((9, 5))
																			if features[10][16] <= 22.5:
																				pixels_low.append((10, 16))
																				ans = 6																				 # approximately 1 were 6 out of 1 samples at leaf node
																			else:
																				pixels_high.append((10, 16))
																				ans = 5																				 # approximately 2 were 5 out of 2 samples at leaf node
																	else:
																		pixels_high.append((7, 8))
																		if features[5][17] <= 62.0:
																			pixels_low.append((5, 17))
																			ans = 8																			 # approximately 1 were 8 out of 1 samples at leaf node
																		else:
																			pixels_high.append((5, 17))
																			ans = 5																			 # approximately 1 were 5 out of 1 samples at leaf node
																else:
																	pixels_high.append((10, 24))
																	if features[12][19] <= 206.0:
																		pixels_low.append((12, 19))
																		ans = 4																		 # approximately 1 were 4 out of 1 samples at leaf node
																	else:
																		pixels_high.append((12, 19))
																		ans = 1																		 # approximately 1 were 1 out of 1 samples at leaf node
															else:
																pixels_high.append((23, 4))
																ans = 5																 # approximately 2 were 5 out of 2 samples at leaf node
														else:
															pixels_high.append((3, 20))
															ans = 5															 # approximately 2 were 5 out of 2 samples at leaf node
													else:
														pixels_high.append((24, 22))
														ans = 9														 # approximately 2 were 9 out of 2 samples at leaf node
												else:
													pixels_high.append((10, 3))
													if features[10][17] <= 30.0:
														pixels_low.append((10, 17))
														if features[22][18] <= 251.5:
															pixels_low.append((22, 18))
															ans = 3															 # approximately 6 were 3 out of 6 samples at leaf node
														else:
															pixels_high.append((22, 18))
															ans = 5															 # approximately 2 were 5 out of 2 samples at leaf node
													else:
														pixels_high.append((10, 17))
														if features[25][8] <= 101.5:
															pixels_low.append((25, 8))
															ans = 6															 # approximately 10 were 6 out of 10 samples at leaf node
														else:
															pixels_high.append((25, 8))
															ans = 8															 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												pixels_high.append((9, 23))
												if features[17][15] <= 220.5:
													pixels_low.append((17, 15))
													ans = 8													 # approximately 5 were 8 out of 5 samples at leaf node
												else:
													pixels_high.append((17, 15))
													if features[20][12] <= 126.0:
														pixels_low.append((20, 12))
														if features[22][17] <= 46.0:
															pixels_low.append((22, 17))
															ans = 5															 # approximately 1 were 5 out of 1 samples at leaf node
														else:
															pixels_high.append((22, 17))
															ans = 6															 # approximately 1 were 6 out of 1 samples at leaf node
													else:
														pixels_high.append((20, 12))
														ans = 4														 # approximately 3 were 4 out of 3 samples at leaf node
										else:
											pixels_high.append((15, 11))
											if features[10][15] <= 121.0:
												pixels_low.append((10, 15))
												if features[12][7] <= 9.0:
													pixels_low.append((12, 7))
													if features[12][2] <= 57.0:
														pixels_low.append((12, 2))
														ans = 3														 # approximately 5 were 3 out of 5 samples at leaf node
													else:
														pixels_high.append((12, 2))
														ans = 2														 # approximately 2 were 2 out of 2 samples at leaf node
												else:
													pixels_high.append((12, 7))
													if features[9][20] <= 254.5:
														pixels_low.append((9, 20))
														ans = 5														 # approximately 13 were 5 out of 13 samples at leaf node
													else:
														pixels_high.append((9, 20))
														ans = 8														 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												pixels_high.append((10, 15))
												ans = 6												 # approximately 21 were 6 out of 21 samples at leaf node
									else:
										pixels_high.append((17, 23))
										if features[11][16] <= 67.5:
											pixels_low.append((11, 16))
											if features[14][20] <= 2.0:
												pixels_low.append((14, 20))
												if features[7][13] <= 246.5:
													pixels_low.append((7, 13))
													ans = 9													 # approximately 2 were 9 out of 2 samples at leaf node
												else:
													pixels_high.append((7, 13))
													ans = 3													 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												pixels_high.append((14, 20))
												ans = 5												 # approximately 6 were 5 out of 6 samples at leaf node
										else:
											pixels_high.append((11, 16))
											if features[13][14] <= 16.0:
												pixels_low.append((13, 14))
												if features[10][11] <= 153.0:
													pixels_low.append((10, 11))
													if features[14][5] <= 239.0:
														pixels_low.append((14, 5))
														ans = 0														 # approximately 1 were 0 out of 1 samples at leaf node
													else:
														pixels_high.append((14, 5))
														ans = 4														 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													pixels_high.append((10, 11))
													ans = 6													 # approximately 3 were 6 out of 3 samples at leaf node
											else:
												pixels_high.append((13, 14))
												ans = 8												 # approximately 5 were 8 out of 5 samples at leaf node
								else:
									pixels_high.append((19, 8))
									if features[14][21] <= 20.0:
										pixels_low.append((14, 21))
										if features[14][18] <= 58.5:
											pixels_low.append((14, 18))
											if features[18][12] <= 230.0:
												pixels_low.append((18, 12))
												ans = 9												 # approximately 2 were 9 out of 2 samples at leaf node
											else:
												pixels_high.append((18, 12))
												ans = 8												 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											pixels_high.append((14, 18))
											ans = 2											 # approximately 10 were 2 out of 10 samples at leaf node
									else:
										pixels_high.append((14, 21))
										if features[11][21] <= 215.5:
											pixels_low.append((11, 21))
											ans = 8											 # approximately 5 were 8 out of 5 samples at leaf node
										else:
											pixels_high.append((11, 21))
											if features[19][3] <= 28.5:
												pixels_low.append((19, 3))
												ans = 5												 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												pixels_high.append((19, 3))
												ans = 6												 # approximately 3 were 6 out of 3 samples at leaf node
							else:
								pixels_high.append((22, 6))
								if features[20][12] <= 32.0:
									pixels_low.append((20, 12))
									ans = 5									 # approximately 16 were 5 out of 16 samples at leaf node
								else:
									pixels_high.append((20, 12))
									if features[11][9] <= 254.0:
										pixels_low.append((11, 9))
										ans = 8										 # approximately 5 were 8 out of 5 samples at leaf node
									else:
										pixels_high.append((11, 9))
										ans = 6										 # approximately 1 were 6 out of 1 samples at leaf node
					else:
						pixels_high.append((16, 10))
						if features[12][20] <= 1.5:
							pixels_low.append((12, 20))
							if features[12][5] <= 2.5:
								pixels_low.append((12, 5))
								if features[11][19] <= 82.0:
									pixels_low.append((11, 19))
									if features[10][15] <= 26.0:
										pixels_low.append((10, 15))
										if features[17][6] <= 51.0:
											pixels_low.append((17, 6))
											if features[16][18] <= 179.0:
												pixels_low.append((16, 18))
												ans = 4												 # approximately 7 were 4 out of 7 samples at leaf node
											else:
												pixels_high.append((16, 18))
												if features[15][20] <= 126.5:
													pixels_low.append((15, 20))
													ans = 9													 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													pixels_high.append((15, 20))
													ans = 1													 # approximately 1 were 1 out of 1 samples at leaf node
										else:
											pixels_high.append((17, 6))
											if features[15][4] <= 70.0:
												pixels_low.append((15, 4))
												ans = 7												 # approximately 1 were 7 out of 1 samples at leaf node
											else:
												pixels_high.append((15, 4))
												if features[15][9] <= 117.5:
													pixels_low.append((15, 9))
													ans = 2													 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													pixels_high.append((15, 9))
													if features[8][21] <= 117.5:
														pixels_low.append((8, 21))
														ans = 8														 # approximately 1 were 8 out of 1 samples at leaf node
													else:
														pixels_high.append((8, 21))
														ans = 3														 # approximately 1 were 3 out of 1 samples at leaf node
									else:
										pixels_high.append((10, 15))
										ans = 4										 # approximately 104 were 4 out of 104 samples at leaf node
								else:
									pixels_high.append((11, 19))
									if features[13][7] <= 218.0:
										pixels_low.append((13, 7))
										if features[14][8] <= 132.0:
											pixels_low.append((14, 8))
											ans = 4											 # approximately 1 were 4 out of 1 samples at leaf node
										else:
											pixels_high.append((14, 8))
											if features[15][17] <= 152.5:
												pixels_low.append((15, 17))
												ans = 2												 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												pixels_high.append((15, 17))
												ans = 7												 # approximately 1 were 7 out of 1 samples at leaf node
									else:
										pixels_high.append((13, 7))
										ans = 9										 # approximately 3 were 9 out of 3 samples at leaf node
							else:
								pixels_high.append((12, 5))
								if features[7][19] <= 103.0:
									pixels_low.append((7, 19))
									if features[14][18] <= 202.5:
										pixels_low.append((14, 18))
										if features[12][6] <= 205.0:
											pixels_low.append((12, 6))
											if features[11][21] <= 94.0:
												pixels_low.append((11, 21))
												if features[19][12] <= 62.0:
													pixels_low.append((19, 12))
													ans = 3													 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													pixels_high.append((19, 12))
													ans = 4													 # approximately 1 were 4 out of 1 samples at leaf node
											else:
												pixels_high.append((11, 21))
												ans = 5												 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											pixels_high.append((12, 6))
											ans = 9											 # approximately 12 were 9 out of 12 samples at leaf node
									else:
										pixels_high.append((14, 18))
										if features[13][12] <= 106.5:
											pixels_low.append((13, 12))
											if features[9][8] <= 54.5:
												pixels_low.append((9, 8))
												if features[8][5] <= 4.5:
													pixels_low.append((8, 5))
													ans = 4													 # approximately 2 were 4 out of 2 samples at leaf node
												else:
													pixels_high.append((8, 5))
													ans = 2													 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												pixels_high.append((9, 8))
												ans = 8												 # approximately 2 were 8 out of 2 samples at leaf node
										else:
											pixels_high.append((13, 12))
											ans = 1											 # approximately 4 were 1 out of 4 samples at leaf node
								else:
									pixels_high.append((7, 19))
									ans = 2									 # approximately 6 were 2 out of 6 samples at leaf node
						else:
							pixels_high.append((12, 20))
							if features[12][11] <= 2.5:
								pixels_low.append((12, 11))
								if features[14][16] <= 4.0:
									pixels_low.append((14, 16))
									if features[11][22] <= 219.5:
										pixels_low.append((11, 22))
										if features[14][8] <= 186.5:
											pixels_low.append((14, 8))
											if features[8][12] <= 9.5:
												pixels_low.append((8, 12))
												if features[19][19] <= 127.0:
													pixels_low.append((19, 19))
													ans = 2													 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													pixels_high.append((19, 19))
													ans = 7													 # approximately 1 were 7 out of 1 samples at leaf node
											else:
												pixels_high.append((8, 12))
												ans = 6												 # approximately 3 were 6 out of 3 samples at leaf node
										else:
											pixels_high.append((14, 8))
											ans = 5											 # approximately 3 were 5 out of 3 samples at leaf node
									else:
										pixels_high.append((11, 22))
										ans = 3										 # approximately 6 were 3 out of 6 samples at leaf node
								else:
									pixels_high.append((14, 16))
									if features[17][4] <= 90.0:
										pixels_low.append((17, 4))
										if features[10][12] <= 148.0:
											pixels_low.append((10, 12))
											if features[16][11] <= 139.0:
												pixels_low.append((16, 11))
												if features[9][17] <= 13.0:
													pixels_low.append((9, 17))
													ans = 3													 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													pixels_high.append((9, 17))
													ans = 2													 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												pixels_high.append((16, 11))
												ans = 2												 # approximately 71 were 2 out of 71 samples at leaf node
										else:
											pixels_high.append((10, 12))
											if features[10][24] <= 3.5:
												pixels_low.append((10, 24))
												ans = 4												 # approximately 1 were 4 out of 1 samples at leaf node
											else:
												pixels_high.append((10, 24))
												ans = 8												 # approximately 1 were 8 out of 1 samples at leaf node
									else:
										pixels_high.append((17, 4))
										if features[16][15] <= 242.5:
											pixels_low.append((16, 15))
											ans = 1											 # approximately 4 were 1 out of 4 samples at leaf node
										else:
											pixels_high.append((16, 15))
											if features[19][15] <= 80.0:
												pixels_low.append((19, 15))
												if features[18][15] <= 48.5:
													pixels_low.append((18, 15))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													pixels_high.append((18, 15))
													ans = 8													 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												pixels_high.append((19, 15))
												ans = 2												 # approximately 2 were 2 out of 2 samples at leaf node
							else:
								pixels_high.append((12, 11))
								if features[10][15] <= 85.0:
									pixels_low.append((10, 15))
									if features[15][15] <= 166.5:
										pixels_low.append((15, 15))
										if features[8][12] <= 113.5:
											pixels_low.append((8, 12))
											if features[20][4] <= 42.0:
												pixels_low.append((20, 4))
												ans = 3												 # approximately 29 were 3 out of 29 samples at leaf node
											else:
												pixels_high.append((20, 4))
												ans = 5												 # approximately 2 were 5 out of 2 samples at leaf node
										else:
											pixels_high.append((8, 12))
											if features[14][4] <= 122.0:
												pixels_low.append((14, 4))
												if features[17][10] <= 44.0:
													pixels_low.append((17, 10))
													ans = 8													 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													pixels_high.append((17, 10))
													if features[22][16] <= 11.5:
														pixels_low.append((22, 16))
														ans = 4														 # approximately 1 were 4 out of 1 samples at leaf node
													else:
														pixels_high.append((22, 16))
														ans = 6														 # approximately 1 were 6 out of 1 samples at leaf node
											else:
												pixels_high.append((14, 4))
												ans = 5												 # approximately 2 were 5 out of 2 samples at leaf node
									else:
										pixels_high.append((15, 15))
										if features[15][12] <= 222.0:
											pixels_low.append((15, 12))
											if features[11][21] <= 159.0:
												pixels_low.append((11, 21))
												if features[14][22] <= 121.0:
													pixels_low.append((14, 22))
													ans = 9													 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													pixels_high.append((14, 22))
													ans = 8													 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												pixels_high.append((11, 21))
												ans = 6												 # approximately 3 were 6 out of 3 samples at leaf node
										else:
											pixels_high.append((15, 12))
											if features[5][18] <= 84.0:
												pixels_low.append((5, 18))
												ans = 1												 # approximately 8 were 1 out of 8 samples at leaf node
											else:
												pixels_high.append((5, 18))
												if features[16][9] <= 249.0:
													pixels_low.append((16, 9))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													pixels_high.append((16, 9))
													ans = 3													 # approximately 1 were 3 out of 1 samples at leaf node
								else:
									pixels_high.append((10, 15))
									if features[14][22] <= 254.5:
										pixels_low.append((14, 22))
										if features[21][5] <= 135.0:
											pixels_low.append((21, 5))
											ans = 6											 # approximately 26 were 6 out of 26 samples at leaf node
										else:
											pixels_high.append((21, 5))
											ans = 5											 # approximately 1 were 5 out of 1 samples at leaf node
									else:
										pixels_high.append((14, 22))
										if features[19][15] <= 127.0:
											pixels_low.append((19, 15))
											ans = 1											 # approximately 1 were 1 out of 1 samples at leaf node
										else:
											pixels_high.append((19, 15))
											ans = 0											 # approximately 2 were 0 out of 2 samples at leaf node
				else:
					pixels_high.append((21, 8))
					if features[12][11] <= 98.0:
						pixels_low.append((12, 11))
						if features[16][12] <= 142.0:
							pixels_low.append((16, 12))
							if features[10][11] <= 161.5:
								pixels_low.append((10, 11))
								if features[11][24] <= 23.0:
									pixels_low.append((11, 24))
									if features[15][9] <= 252.5:
										pixels_low.append((15, 9))
										if features[6][18] <= 1.5:
											pixels_low.append((6, 18))
											if features[14][17] <= 13.0:
												pixels_low.append((14, 17))
												if features[17][7] <= 46.0:
													pixels_low.append((17, 7))
													ans = 2													 # approximately 2 were 2 out of 2 samples at leaf node
												else:
													pixels_high.append((17, 7))
													ans = 3													 # approximately 6 were 3 out of 6 samples at leaf node
											else:
												pixels_high.append((14, 17))
												if features[17][5] <= 21.5:
													pixels_low.append((17, 5))
													if features[21][9] <= 208.0:
														pixels_low.append((21, 9))
														ans = 7														 # approximately 1 were 7 out of 1 samples at leaf node
													else:
														pixels_high.append((21, 9))
														ans = 9														 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													pixels_high.append((17, 5))
													if features[4][22] <= 234.5:
														pixels_low.append((4, 22))
														ans = 2														 # approximately 28 were 2 out of 28 samples at leaf node
													else:
														pixels_high.append((4, 22))
														ans = 3														 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											pixels_high.append((6, 18))
											if features[7][12] <= 253.5:
												pixels_low.append((7, 12))
												if features[14][12] <= 253.5:
													pixels_low.append((14, 12))
													ans = 2													 # approximately 292 were 2 out of 292 samples at leaf node
												else:
													pixels_high.append((14, 12))
													ans = 8													 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												pixels_high.append((7, 12))
												ans = 6												 # approximately 1 were 6 out of 1 samples at leaf node
									else:
										pixels_high.append((15, 9))
										if features[19][10] <= 64.0:
											pixels_low.append((19, 10))
											if features[16][5] <= 31.0:
												pixels_low.append((16, 5))
												ans = 8												 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												pixels_high.append((16, 5))
												ans = 5												 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											pixels_high.append((19, 10))
											ans = 0											 # approximately 1 were 0 out of 1 samples at leaf node
								else:
									pixels_high.append((11, 24))
									if features[16][17] <= 127.0:
										pixels_low.append((16, 17))
										ans = 8										 # approximately 4 were 8 out of 4 samples at leaf node
									else:
										pixels_high.append((16, 17))
										ans = 5										 # approximately 1 were 5 out of 1 samples at leaf node
							else:
								pixels_high.append((10, 11))
								if features[18][16] <= 6.5:
									pixels_low.append((18, 16))
									ans = 8									 # approximately 4 were 8 out of 4 samples at leaf node
								else:
									pixels_high.append((18, 16))
									if features[13][16] <= 14.0:
										pixels_low.append((13, 16))
										if features[23][6] <= 50.0:
											pixels_low.append((23, 6))
											ans = 0											 # approximately 4 were 0 out of 4 samples at leaf node
										else:
											pixels_high.append((23, 6))
											ans = 5											 # approximately 2 were 5 out of 2 samples at leaf node
									else:
										pixels_high.append((13, 16))
										if features[17][18] <= 206.5:
											pixels_low.append((17, 18))
											if features[11][11] <= 112.0:
												pixels_low.append((11, 11))
												if features[12][7] <= 222.0:
													pixels_low.append((12, 7))
													ans = 9													 # approximately 3 were 9 out of 3 samples at leaf node
												else:
													pixels_high.append((12, 7))
													ans = 6													 # approximately 1 were 6 out of 1 samples at leaf node
											else:
												pixels_high.append((11, 11))
												ans = 4												 # approximately 3 were 4 out of 3 samples at leaf node
										else:
											pixels_high.append((17, 18))
											ans = 2											 # approximately 5 were 2 out of 5 samples at leaf node
						else:
							pixels_high.append((16, 12))
							if features[14][20] <= 232.5:
								pixels_low.append((14, 20))
								if features[14][14] <= 252.5:
									pixels_low.append((14, 14))
									if features[10][9] <= 124.0:
										pixels_low.append((10, 9))
										if features[13][6] <= 126.0:
											pixels_low.append((13, 6))
											if features[11][21] <= 253.0:
												pixels_low.append((11, 21))
												ans = 5												 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												pixels_high.append((11, 21))
												ans = 9												 # approximately 1 were 9 out of 1 samples at leaf node
										else:
											pixels_high.append((13, 6))
											ans = 2											 # approximately 2 were 2 out of 2 samples at leaf node
									else:
										pixels_high.append((10, 9))
										ans = 4										 # approximately 2 were 4 out of 2 samples at leaf node
								else:
									pixels_high.append((14, 14))
									if features[5][20] <= 209.5:
										pixels_low.append((5, 20))
										ans = 8										 # approximately 5 were 8 out of 5 samples at leaf node
									else:
										pixels_high.append((5, 20))
										ans = 3										 # approximately 1 were 3 out of 1 samples at leaf node
							else:
								pixels_high.append((14, 20))
								if features[8][11] <= 115.0:
									pixels_low.append((8, 11))
									ans = 3									 # approximately 11 were 3 out of 11 samples at leaf node
								else:
									pixels_high.append((8, 11))
									ans = 5									 # approximately 1 were 5 out of 1 samples at leaf node
					else:
						pixels_high.append((12, 11))
						if features[20][11] <= 10.0:
							pixels_low.append((20, 11))
							if features[9][17] <= 252.5:
								pixels_low.append((9, 17))
								ans = 5								 # approximately 14 were 5 out of 14 samples at leaf node
							else:
								pixels_high.append((9, 17))
								if features[10][16] <= 99.0:
									pixels_low.append((10, 16))
									ans = 4									 # approximately 1 were 4 out of 1 samples at leaf node
								else:
									pixels_high.append((10, 16))
									ans = 6									 # approximately 4 were 6 out of 4 samples at leaf node
						else:
							pixels_high.append((20, 11))
							if features[16][14] <= 95.5:
								pixels_low.append((16, 14))
								if features[10][13] <= 49.5:
									pixels_low.append((10, 13))
									if features[15][13] <= 53.0:
										pixels_low.append((15, 13))
										ans = 2										 # approximately 5 were 2 out of 5 samples at leaf node
									else:
										pixels_high.append((15, 13))
										ans = 3										 # approximately 2 were 3 out of 2 samples at leaf node
								else:
									pixels_high.append((10, 13))
									ans = 0									 # approximately 14 were 0 out of 14 samples at leaf node
							else:
								pixels_high.append((16, 14))
								if features[9][13] <= 58.5:
									pixels_low.append((9, 13))
									if features[13][6] <= 254.0:
										pixels_low.append((13, 6))
										ans = 8										 # approximately 21 were 8 out of 21 samples at leaf node
									else:
										pixels_high.append((13, 6))
										ans = 2										 # approximately 1 were 2 out of 1 samples at leaf node
								else:
									pixels_high.append((9, 13))
									if features[20][19] <= 85.5:
										pixels_low.append((20, 19))
										ans = 4										 # approximately 11 were 4 out of 11 samples at leaf node
									else:
										pixels_high.append((20, 19))
										ans = 2										 # approximately 1 were 2 out of 1 samples at leaf node
			else:
				pixels_high.append((18, 9))
				if features[12][12] <= 1.5:
					pixels_low.append((12, 12))
					if features[8][13] <= 135.0:
						pixels_low.append((8, 13))
						if features[13][12] <= 10.5:
							pixels_low.append((13, 12))
							if features[10][12] <= 214.5:
								pixels_low.append((10, 12))
								if features[9][24] <= 4.5:
									pixels_low.append((9, 24))
									if features[6][13] <= 221.5:
										pixels_low.append((6, 13))
										if features[2][18] <= 97.0:
											pixels_low.append((2, 18))
											if features[4][24] <= 12.5:
												pixels_low.append((4, 24))
												if features[5][14] <= 211.0:
													pixels_low.append((5, 14))
													if features[13][17] <= 9.5:
														pixels_low.append((13, 17))
														if features[15][12] <= 4.5:
															pixels_low.append((15, 12))
															if features[16][16] <= 29.0:
																pixels_low.append((16, 16))
																if features[7][8] <= 26.0:
																	pixels_low.append((7, 8))
																	ans = 3																	 # approximately 2 were 3 out of 2 samples at leaf node
																else:
																	pixels_high.append((7, 8))
																	ans = 4																	 # approximately 1 were 4 out of 1 samples at leaf node
															else:
																pixels_high.append((16, 16))
																if features[9][12] <= 69.0:
																	pixels_low.append((9, 12))
																	if features[4][20] <= 253.5:
																		pixels_low.append((4, 20))
																		if features[18][24] <= 98.5:
																			pixels_low.append((18, 24))
																			ans = 2																			 # approximately 89 were 2 out of 89 samples at leaf node
																		else:
																			pixels_high.append((18, 24))
																			ans = 9																			 # approximately 1 were 9 out of 1 samples at leaf node
																	else:
																		pixels_high.append((4, 20))
																		ans = 3																		 # approximately 1 were 3 out of 1 samples at leaf node
																else:
																	pixels_high.append((9, 12))
																	if features[19][20] <= 13.0:
																		pixels_low.append((19, 20))
																		ans = 4																		 # approximately 1 were 4 out of 1 samples at leaf node
																	else:
																		pixels_high.append((19, 20))
																		ans = 0																		 # approximately 1 were 0 out of 1 samples at leaf node
														else:
															pixels_high.append((15, 12))
															if features[10][17] <= 222.5:
																pixels_low.append((10, 17))
																if features[15][9] <= 33.0:
																	pixels_low.append((15, 9))
																	ans = 3																	 # approximately 10 were 3 out of 10 samples at leaf node
																else:
																	pixels_high.append((15, 9))
																	if features[6][22] <= 127.0:
																		pixels_low.append((6, 22))
																		ans = 5																		 # approximately 1 were 5 out of 1 samples at leaf node
																	else:
																		pixels_high.append((6, 22))
																		ans = 1																		 # approximately 1 were 1 out of 1 samples at leaf node
															else:
																pixels_high.append((10, 17))
																ans = 2																 # approximately 6 were 2 out of 6 samples at leaf node
													else:
														pixels_high.append((13, 17))
														if features[14][11] <= 222.5:
															pixels_low.append((14, 11))
															if features[17][24] <= 229.0:
																pixels_low.append((17, 24))
																if features[3][14] <= 103.0:
																	pixels_low.append((3, 14))
																	if features[8][24] <= 198.0:
																		pixels_low.append((8, 24))
																		if features[12][23] <= 179.5:
																			pixels_low.append((12, 23))
																			if features[20][24] <= 243.5:
																				pixels_low.append((20, 24))
																				if features[3][7] <= 48.5:
																					pixels_low.append((3, 7))
																					if features[14][12] <= 172.5:
																						pixels_low.append((14, 12))
																						if features[23][7] <= 126.5:
																							pixels_low.append((23, 7))
																							if features[6][24] <= 201.0:
																								pixels_low.append((6, 24))
																								if features[12][22] <= 253.5:
																									pixels_low.append((12, 22))
																									if features[14][13] <= 254.5:
																										pixels_low.append((14, 13))
																										if features[12][21] <= 254.5:
																											pixels_low.append((12, 21))
																											if features[18][8] <= 254.5:
																												pixels_low.append((18, 8))
																												ans = 2																												 # approximately 1199 were 2 out of 1199 samples at leaf node
																											else:
																												pixels_high.append((18, 8))
																												if features[11][22] <= 215.0:
																													pixels_low.append((11, 22))
																													ans = 2																													 # approximately 32 were 2 out of 32 samples at leaf node
																												else:
																													pixels_high.append((11, 22))
																													ans = 3																													 # approximately 1 were 3 out of 1 samples at leaf node
																										else:
																											pixels_high.append((12, 21))
																											if features[13][17] <= 37.5:
																												pixels_low.append((13, 17))
																												ans = 1																												 # approximately 1 were 1 out of 1 samples at leaf node
																											else:
																												pixels_high.append((13, 17))
																												ans = 2																												 # approximately 20 were 2 out of 20 samples at leaf node
																									else:
																										pixels_high.append((14, 13))
																										if features[13][4] <= 166.0:
																											pixels_low.append((13, 4))
																											ans = 3																											 # approximately 1 were 3 out of 1 samples at leaf node
																										else:
																											pixels_high.append((13, 4))
																											ans = 2																											 # approximately 3 were 2 out of 3 samples at leaf node
																								else:
																									pixels_high.append((12, 22))
																									if features[9][21] <= 200.0:
																										pixels_low.append((9, 21))
																										if features[10][6] <= 24.5:
																											pixels_low.append((10, 6))
																											ans = 3																											 # approximately 2 were 3 out of 2 samples at leaf node
																										else:
																											pixels_high.append((10, 6))
																											ans = 2																											 # approximately 1 were 2 out of 1 samples at leaf node
																									else:
																										pixels_high.append((9, 21))
																										ans = 2																										 # approximately 9 were 2 out of 9 samples at leaf node
																							else:
																								pixels_high.append((6, 24))
																								if features[12][7] <= 85.0:
																									pixels_low.append((12, 7))
																									ans = 7																									 # approximately 1 were 7 out of 1 samples at leaf node
																								else:
																									pixels_high.append((12, 7))
																									ans = 2																									 # approximately 2 were 2 out of 2 samples at leaf node
																						else:
																							pixels_high.append((23, 7))
																							if features[6][20] <= 34.5:
																								pixels_low.append((6, 20))
																								ans = 8																								 # approximately 1 were 8 out of 1 samples at leaf node
																							else:
																								pixels_high.append((6, 20))
																								ans = 2																								 # approximately 2 were 2 out of 2 samples at leaf node
																					else:
																						pixels_high.append((14, 12))
																						if features[10][18] <= 201.0:
																							pixels_low.append((10, 18))
																							ans = 1																							 # approximately 2 were 1 out of 2 samples at leaf node
																						else:
																							pixels_high.append((10, 18))
																							ans = 2																							 # approximately 9 were 2 out of 9 samples at leaf node
																				else:
																					pixels_high.append((3, 7))
																					if features[21][11] <= 181.0:
																						pixels_low.append((21, 11))
																						ans = 2																						 # approximately 1 were 2 out of 1 samples at leaf node
																					else:
																						pixels_high.append((21, 11))
																						ans = 3																						 # approximately 1 were 3 out of 1 samples at leaf node
																			else:
																				pixels_high.append((20, 24))
																				if features[18][11] <= 217.0:
																					pixels_low.append((18, 11))
																					ans = 2																					 # approximately 1 were 2 out of 1 samples at leaf node
																				else:
																					pixels_high.append((18, 11))
																					ans = 7																					 # approximately 1 were 7 out of 1 samples at leaf node
																		else:
																			pixels_high.append((12, 23))
																			ans = 1																			 # approximately 1 were 1 out of 1 samples at leaf node
																	else:
																		pixels_high.append((8, 24))
																		ans = 7																		 # approximately 1 were 7 out of 1 samples at leaf node
																else:
																	pixels_high.append((3, 14))
																	ans = 9																	 # approximately 1 were 9 out of 1 samples at leaf node
															else:
																pixels_high.append((17, 24))
																if features[19][8] <= 79.0:
																	pixels_low.append((19, 8))
																	ans = 7																	 # approximately 1 were 7 out of 1 samples at leaf node
																else:
																	pixels_high.append((19, 8))
																	ans = 3																	 # approximately 1 were 3 out of 1 samples at leaf node
														else:
															pixels_high.append((14, 11))
															if features[13][10] <= 253.5:
																pixels_low.append((13, 10))
																ans = 8																 # approximately 2 were 8 out of 2 samples at leaf node
															else:
																pixels_high.append((13, 10))
																if features[19][16] <= 87.5:
																	pixels_low.append((19, 16))
																	ans = 2																	 # approximately 1 were 2 out of 1 samples at leaf node
																else:
																	pixels_high.append((19, 16))
																	ans = 3																	 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													pixels_high.append((5, 14))
													ans = 4													 # approximately 2 were 4 out of 2 samples at leaf node
											else:
												pixels_high.append((4, 24))
												if features[11][17] <= 60.0:
													pixels_low.append((11, 17))
													if features[20][22] <= 65.5:
														pixels_low.append((20, 22))
														ans = 3														 # approximately 2 were 3 out of 2 samples at leaf node
													else:
														pixels_high.append((20, 22))
														ans = 2														 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													pixels_high.append((11, 17))
													ans = 7													 # approximately 2 were 7 out of 2 samples at leaf node
										else:
											pixels_high.append((2, 18))
											ans = 3											 # approximately 4 were 3 out of 4 samples at leaf node
									else:
										pixels_high.append((6, 13))
										if features[18][24] <= 69.0:
											pixels_low.append((18, 24))
											ans = 4											 # approximately 4 were 4 out of 4 samples at leaf node
										else:
											pixels_high.append((18, 24))
											ans = 9											 # approximately 5 were 9 out of 5 samples at leaf node
								else:
									pixels_high.append((9, 24))
									if features[18][19] <= 6.0:
										pixels_low.append((18, 19))
										if features[9][8] <= 42.0:
											pixels_low.append((9, 8))
											if features[17][13] <= 200.0:
												pixels_low.append((17, 13))
												if features[13][22] <= 26.5:
													pixels_low.append((13, 22))
													ans = 1													 # approximately 2 were 1 out of 2 samples at leaf node
												else:
													pixels_high.append((13, 22))
													ans = 9													 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												pixels_high.append((17, 13))
												ans = 7												 # approximately 12 were 7 out of 12 samples at leaf node
										else:
											pixels_high.append((9, 8))
											if features[14][13] <= 98.5:
												pixels_low.append((14, 13))
												ans = 2												 # approximately 2 were 2 out of 2 samples at leaf node
											else:
												pixels_high.append((14, 13))
												ans = 3												 # approximately 4 were 3 out of 4 samples at leaf node
									else:
										pixels_high.append((18, 19))
										ans = 2										 # approximately 10 were 2 out of 10 samples at leaf node
							else:
								pixels_high.append((10, 12))
								if features[17][18] <= 27.0:
									pixels_low.append((17, 18))
									if features[18][21] <= 64.0:
										pixels_low.append((18, 21))
										ans = 8										 # approximately 5 were 8 out of 5 samples at leaf node
									else:
										pixels_high.append((18, 21))
										ans = 2										 # approximately 2 were 2 out of 2 samples at leaf node
								else:
									pixels_high.append((17, 18))
									if features[16][7] <= 30.0:
										pixels_low.append((16, 7))
										if features[14][3] <= 3.5:
											pixels_low.append((14, 3))
											ans = 4											 # approximately 3 were 4 out of 3 samples at leaf node
										else:
											pixels_high.append((14, 3))
											if features[15][15] <= 109.0:
												pixels_low.append((15, 15))
												ans = 0												 # approximately 1 were 0 out of 1 samples at leaf node
											else:
												pixels_high.append((15, 15))
												ans = 6												 # approximately 2 were 6 out of 2 samples at leaf node
									else:
										pixels_high.append((16, 7))
										if features[15][8] <= 7.5:
											pixels_low.append((15, 8))
											ans = 9											 # approximately 7 were 9 out of 7 samples at leaf node
										else:
											pixels_high.append((15, 8))
											ans = 4											 # approximately 1 were 4 out of 1 samples at leaf node
						else:
							pixels_high.append((13, 12))
							if features[9][18] <= 25.0:
								pixels_low.append((9, 18))
								if features[13][17] <= 140.5:
									pixels_low.append((13, 17))
									if features[14][12] <= 66.5:
										pixels_low.append((14, 12))
										ans = 8										 # approximately 1 were 8 out of 1 samples at leaf node
									else:
										pixels_high.append((14, 12))
										ans = 3										 # approximately 29 were 3 out of 29 samples at leaf node
								else:
									pixels_high.append((13, 17))
									if features[11][8] <= 35.5:
										pixels_low.append((11, 8))
										ans = 1										 # approximately 8 were 1 out of 8 samples at leaf node
									else:
										pixels_high.append((11, 8))
										if features[12][20] <= 253.5:
											pixels_low.append((12, 20))
											ans = 2											 # approximately 3 were 2 out of 3 samples at leaf node
										else:
											pixels_high.append((12, 20))
											ans = 9											 # approximately 1 were 9 out of 1 samples at leaf node
							else:
								pixels_high.append((9, 18))
								if features[13][10] <= 128.0:
									pixels_low.append((13, 10))
									if features[18][9] <= 14.5:
										pixels_low.append((18, 9))
										ans = 3										 # approximately 1 were 3 out of 1 samples at leaf node
									else:
										pixels_high.append((18, 9))
										if features[4][19] <= 242.0:
											pixels_low.append((4, 19))
											if features[20][3] <= 63.0:
												pixels_low.append((20, 3))
												ans = 2												 # approximately 40 were 2 out of 40 samples at leaf node
											else:
												pixels_high.append((20, 3))
												ans = 3												 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											pixels_high.append((4, 19))
											ans = 3											 # approximately 1 were 3 out of 1 samples at leaf node
								else:
									pixels_high.append((13, 10))
									if features[13][21] <= 232.0:
										pixels_low.append((13, 21))
										if features[13][12] <= 95.5:
											pixels_low.append((13, 12))
											ans = 2											 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											pixels_high.append((13, 12))
											ans = 3											 # approximately 1 were 3 out of 1 samples at leaf node
									else:
										pixels_high.append((13, 21))
										ans = 8										 # approximately 3 were 8 out of 3 samples at leaf node
					else:
						pixels_high.append((8, 13))
						if features[13][6] <= 16.5:
							pixels_low.append((13, 6))
							if features[17][9] <= 162.0:
								pixels_low.append((17, 9))
								if features[11][14] <= 169.0:
									pixels_low.append((11, 14))
									if features[11][18] <= 138.5:
										pixels_low.append((11, 18))
										ans = 4										 # approximately 2 were 4 out of 2 samples at leaf node
									else:
										pixels_high.append((11, 18))
										if features[21][19] <= 77.0:
											pixels_low.append((21, 19))
											ans = 0											 # approximately 1 were 0 out of 1 samples at leaf node
										else:
											pixels_high.append((21, 19))
											ans = 7											 # approximately 1 were 7 out of 1 samples at leaf node
								else:
									pixels_high.append((11, 14))
									ans = 2									 # approximately 9 were 2 out of 9 samples at leaf node
							else:
								pixels_high.append((17, 9))
								if features[12][7] <= 19.0:
									pixels_low.append((12, 7))
									ans = 4									 # approximately 54 were 4 out of 54 samples at leaf node
								else:
									pixels_high.append((12, 7))
									ans = 3									 # approximately 1 were 3 out of 1 samples at leaf node
						else:
							pixels_high.append((13, 6))
							if features[14][4] <= 6.5:
								pixels_low.append((14, 4))
								if features[9][16] <= 2.0:
									pixels_low.append((9, 16))
									if features[18][7] <= 249.5:
										pixels_low.append((18, 7))
										if features[17][11] <= 98.5:
											pixels_low.append((17, 11))
											if features[8][24] <= 123.5:
												pixels_low.append((8, 24))
												ans = 2												 # approximately 6 were 2 out of 6 samples at leaf node
											else:
												pixels_high.append((8, 24))
												ans = 7												 # approximately 1 were 7 out of 1 samples at leaf node
										else:
											pixels_high.append((17, 11))
											if features[14][14] <= 113.0:
												pixels_low.append((14, 14))
												if features[6][17] <= 126.5:
													pixels_low.append((6, 17))
													ans = 7													 # approximately 2 were 7 out of 2 samples at leaf node
												else:
													pixels_high.append((6, 17))
													ans = 4													 # approximately 1 were 4 out of 1 samples at leaf node
											else:
												pixels_high.append((14, 14))
												ans = 9												 # approximately 3 were 9 out of 3 samples at leaf node
									else:
										pixels_high.append((18, 7))
										ans = 8										 # approximately 5 were 8 out of 5 samples at leaf node
								else:
									pixels_high.append((9, 16))
									if features[15][5] <= 8.5:
										pixels_low.append((15, 5))
										ans = 4										 # approximately 4 were 4 out of 4 samples at leaf node
									else:
										pixels_high.append((15, 5))
										if features[8][19] <= 252.5:
											pixels_low.append((8, 19))
											if features[23][16] <= 37.5:
												pixels_low.append((23, 16))
												if features[21][23] <= 252.5:
													pixels_low.append((21, 23))
													ans = 9													 # approximately 45 were 9 out of 45 samples at leaf node
												else:
													pixels_high.append((21, 23))
													ans = 2													 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												pixels_high.append((23, 16))
												if features[7][14] <= 253.5:
													pixels_low.append((7, 14))
													ans = 4													 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													pixels_high.append((7, 14))
													ans = 8													 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											pixels_high.append((8, 19))
											ans = 0											 # approximately 3 were 0 out of 3 samples at leaf node
							else:
								pixels_high.append((14, 4))
								if features[10][15] <= 205.5:
									pixels_low.append((10, 15))
									if features[18][7] <= 180.0:
										pixels_low.append((18, 7))
										ans = 6										 # approximately 11 were 6 out of 11 samples at leaf node
									else:
										pixels_high.append((18, 7))
										if features[20][11] <= 93.0:
											pixels_low.append((20, 11))
											ans = 0											 # approximately 1 were 0 out of 1 samples at leaf node
										else:
											pixels_high.append((20, 11))
											ans = 4											 # approximately 1 were 4 out of 1 samples at leaf node
								else:
									pixels_high.append((10, 15))
									if features[7][19] <= 30.0:
										pixels_low.append((7, 19))
										ans = 8										 # approximately 1 were 8 out of 1 samples at leaf node
									else:
										pixels_high.append((7, 19))
										ans = 2										 # approximately 13 were 2 out of 13 samples at leaf node
				else:
					pixels_high.append((12, 12))
					if features[8][15] <= 11.5:
						pixels_low.append((8, 15))
						if features[12][17] <= 8.5:
							pixels_low.append((12, 17))
							if features[15][11] <= 53.5:
								pixels_low.append((15, 11))
								if features[18][11] <= 11.5:
									pixels_low.append((18, 11))
									if features[14][7] <= 119.0:
										pixels_low.append((14, 7))
										ans = 3										 # approximately 2 were 3 out of 2 samples at leaf node
									else:
										pixels_high.append((14, 7))
										ans = 5										 # approximately 10 were 5 out of 10 samples at leaf node
								else:
									pixels_high.append((18, 11))
									if features[14][21] <= 164.5:
										pixels_low.append((14, 21))
										if features[10][14] <= 225.0:
											pixels_low.append((10, 14))
											if features[6][22] <= 174.5:
												pixels_low.append((6, 22))
												if features[13][20] <= 85.5:
													pixels_low.append((13, 20))
													ans = 8													 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													pixels_high.append((13, 20))
													ans = 2													 # approximately 9 were 2 out of 9 samples at leaf node
											else:
												pixels_high.append((6, 22))
												ans = 9												 # approximately 1 were 9 out of 1 samples at leaf node
										else:
											pixels_high.append((10, 14))
											if features[12][8] <= 6.0:
												pixels_low.append((12, 8))
												ans = 0												 # approximately 2 were 0 out of 2 samples at leaf node
											else:
												pixels_high.append((12, 8))
												ans = 9												 # approximately 3 were 9 out of 3 samples at leaf node
									else:
										pixels_high.append((14, 21))
										if features[14][17] <= 218.0:
											pixels_low.append((14, 17))
											ans = 3											 # approximately 10 were 3 out of 10 samples at leaf node
										else:
											pixels_high.append((14, 17))
											if features[13][8] <= 156.5:
												pixels_low.append((13, 8))
												ans = 6												 # approximately 1 were 6 out of 1 samples at leaf node
											else:
												pixels_high.append((13, 8))
												ans = 8												 # approximately 1 were 8 out of 1 samples at leaf node
							else:
								pixels_high.append((15, 11))
								if features[23][8] <= 6.0:
									pixels_low.append((23, 8))
									if features[10][17] <= 157.0:
										pixels_low.append((10, 17))
										if features[7][13] <= 251.0:
											pixels_low.append((7, 13))
											ans = 3											 # approximately 170 were 3 out of 170 samples at leaf node
										else:
											pixels_high.append((7, 13))
											ans = 4											 # approximately 1 were 4 out of 1 samples at leaf node
									else:
										pixels_high.append((10, 17))
										if features[11][4] <= 68.0:
											pixels_low.append((11, 4))
											ans = 8											 # approximately 2 were 8 out of 2 samples at leaf node
										else:
											pixels_high.append((11, 4))
											if features[18][23] <= 119.5:
												pixels_low.append((18, 23))
												ans = 3												 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												pixels_high.append((18, 23))
												ans = 2												 # approximately 1 were 2 out of 1 samples at leaf node
								else:
									pixels_high.append((23, 8))
									if features[14][7] <= 116.5:
										pixels_low.append((14, 7))
										ans = 3										 # approximately 1 were 3 out of 1 samples at leaf node
									else:
										pixels_high.append((14, 7))
										ans = 5										 # approximately 4 were 5 out of 4 samples at leaf node
						else:
							pixels_high.append((12, 17))
							if features[15][10] <= 247.0:
								pixels_low.append((15, 10))
								if features[21][20] <= 4.5:
									pixels_low.append((21, 20))
									if features[10][15] <= 218.0:
										pixels_low.append((10, 15))
										if features[12][16] <= 194.5:
											pixels_low.append((12, 16))
											if features[10][18] <= 181.0:
												pixels_low.append((10, 18))
												if features[16][13] <= 201.5:
													pixels_low.append((16, 13))
													ans = 8													 # approximately 4 were 8 out of 4 samples at leaf node
												else:
													pixels_high.append((16, 13))
													if features[18][7] <= 135.0:
														pixels_low.append((18, 7))
														if features[18][6] <= 107.5:
															pixels_low.append((18, 6))
															ans = 4															 # approximately 2 were 4 out of 2 samples at leaf node
														else:
															pixels_high.append((18, 6))
															ans = 1															 # approximately 1 were 1 out of 1 samples at leaf node
													else:
														pixels_high.append((18, 7))
														ans = 9														 # approximately 6 were 9 out of 6 samples at leaf node
											else:
												pixels_high.append((10, 18))
												if features[22][7] <= 76.0:
													pixels_low.append((22, 7))
													ans = 2													 # approximately 5 were 2 out of 5 samples at leaf node
												else:
													pixels_high.append((22, 7))
													ans = 3													 # approximately 2 were 3 out of 2 samples at leaf node
										else:
											pixels_high.append((12, 16))
											if features[16][13] <= 160.0:
												pixels_low.append((16, 13))
												if features[17][10] <= 134.0:
													pixels_low.append((17, 10))
													ans = 2													 # approximately 3 were 2 out of 3 samples at leaf node
												else:
													pixels_high.append((17, 10))
													if features[18][6] <= 37.0:
														pixels_low.append((18, 6))
														ans = 0														 # approximately 1 were 0 out of 1 samples at leaf node
													else:
														pixels_high.append((18, 6))
														ans = 1														 # approximately 1 were 1 out of 1 samples at leaf node
											else:
												pixels_high.append((16, 13))
												ans = 8												 # approximately 27 were 8 out of 27 samples at leaf node
									else:
										pixels_high.append((10, 15))
										if features[12][21] <= 67.0:
											pixels_low.append((12, 21))
											ans = 4											 # approximately 7 were 4 out of 7 samples at leaf node
										else:
											pixels_high.append((12, 21))
											if features[10][12] <= 58.0:
												pixels_low.append((10, 12))
												if features[20][8] <= 126.5:
													pixels_low.append((20, 8))
													ans = 0													 # approximately 1 were 0 out of 1 samples at leaf node
												else:
													pixels_high.append((20, 8))
													ans = 3													 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												pixels_high.append((10, 12))
												ans = 6												 # approximately 4 were 6 out of 4 samples at leaf node
								else:
									pixels_high.append((21, 20))
									if features[19][22] <= 247.5:
										pixels_low.append((19, 22))
										ans = 2										 # approximately 14 were 2 out of 14 samples at leaf node
									else:
										pixels_high.append((19, 22))
										ans = 8										 # approximately 3 were 8 out of 3 samples at leaf node
							else:
								pixels_high.append((15, 10))
								if features[18][18] <= 4.0:
									pixels_low.append((18, 18))
									if features[11][10] <= 13.0:
										pixels_low.append((11, 10))
										ans = 1										 # approximately 18 were 1 out of 18 samples at leaf node
									else:
										pixels_high.append((11, 10))
										if features[19][10] <= 63.0:
											pixels_low.append((19, 10))
											ans = 5											 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											pixels_high.append((19, 10))
											ans = 9											 # approximately 1 were 9 out of 1 samples at leaf node
								else:
									pixels_high.append((18, 18))
									if features[11][15] <= 139.0:
										pixels_low.append((11, 15))
										if features[13][11] <= 253.5:
											pixels_low.append((13, 11))
											ans = 3											 # approximately 7 were 3 out of 7 samples at leaf node
										else:
											pixels_high.append((13, 11))
											ans = 5											 # approximately 1 were 5 out of 1 samples at leaf node
									else:
										pixels_high.append((11, 15))
										if features[20][18] <= 103.0:
											pixels_low.append((20, 18))
											ans = 6											 # approximately 2 were 6 out of 2 samples at leaf node
										else:
											pixels_high.append((20, 18))
											if features[21][20] <= 49.5:
												pixels_low.append((21, 20))
												ans = 8												 # approximately 2 were 8 out of 2 samples at leaf node
											else:
												pixels_high.append((21, 20))
												ans = 2												 # approximately 2 were 2 out of 2 samples at leaf node
					else:
						pixels_high.append((8, 15))
						if features[9][20] <= 29.5:
							pixels_low.append((9, 20))
							if features[13][21] <= 115.5:
								pixels_low.append((13, 21))
								if features[17][11] <= 17.5:
									pixels_low.append((17, 11))
									if features[16][3] <= 1.0:
										pixels_low.append((16, 3))
										ans = 8										 # approximately 1 were 8 out of 1 samples at leaf node
									else:
										pixels_high.append((16, 3))
										ans = 2										 # approximately 2 were 2 out of 2 samples at leaf node
								else:
									pixels_high.append((17, 11))
									if features[23][10] <= 67.0:
										pixels_low.append((23, 10))
										if features[14][19] <= 250.5:
											pixels_low.append((14, 19))
											ans = 4											 # approximately 69 were 4 out of 69 samples at leaf node
										else:
											pixels_high.append((14, 19))
											ans = 9											 # approximately 1 were 9 out of 1 samples at leaf node
									else:
										pixels_high.append((23, 10))
										ans = 9										 # approximately 1 were 9 out of 1 samples at leaf node
							else:
								pixels_high.append((13, 21))
								if features[20][16] <= 104.0:
									pixels_low.append((20, 16))
									ans = 3									 # approximately 7 were 3 out of 7 samples at leaf node
								else:
									pixels_high.append((20, 16))
									if features[18][7] <= 119.5:
										pixels_low.append((18, 7))
										ans = 0										 # approximately 1 were 0 out of 1 samples at leaf node
									else:
										pixels_high.append((18, 7))
										if features[14][18] <= 130.0:
											pixels_low.append((14, 18))
											ans = 2											 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											pixels_high.append((14, 18))
											ans = 8											 # approximately 1 were 8 out of 1 samples at leaf node
						else:
							pixels_high.append((9, 20))
							if features[14][14] <= 0.5:
								pixels_low.append((14, 14))
								if features[9][15] <= 205.0:
									pixels_low.append((9, 15))
									if features[8][15] <= 218.5:
										pixels_low.append((8, 15))
										if features[17][18] <= 251.5:
											pixels_low.append((17, 18))
											ans = 2											 # approximately 5 were 2 out of 5 samples at leaf node
										else:
											pixels_high.append((17, 18))
											ans = 5											 # approximately 2 were 5 out of 2 samples at leaf node
									else:
										pixels_high.append((8, 15))
										if features[22][17] <= 53.5:
											pixels_low.append((22, 17))
											ans = 0											 # approximately 3 were 0 out of 3 samples at leaf node
										else:
											pixels_high.append((22, 17))
											if features[10][12] <= 126.0:
												pixels_low.append((10, 12))
												ans = 8												 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												pixels_high.append((10, 12))
												ans = 4												 # approximately 1 were 4 out of 1 samples at leaf node
								else:
									pixels_high.append((9, 15))
									if features[24][17] <= 41.5:
										pixels_low.append((24, 17))
										ans = 0										 # approximately 46 were 0 out of 46 samples at leaf node
									else:
										pixels_high.append((24, 17))
										if features[15][20] <= 250.5:
											pixels_low.append((15, 20))
											ans = 4											 # approximately 2 were 4 out of 2 samples at leaf node
										else:
											pixels_high.append((15, 20))
											ans = 6											 # approximately 1 were 6 out of 1 samples at leaf node
							else:
								pixels_high.append((14, 14))
								if features[12][10] <= 241.0:
									pixels_low.append((12, 10))
									if features[7][17] <= 1.5:
										pixels_low.append((7, 17))
										if features[9][18] <= 5.0:
											pixels_low.append((9, 18))
											if features[10][22] <= 11.0:
												pixels_low.append((10, 22))
												ans = 2												 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												pixels_high.append((10, 22))
												ans = 3												 # approximately 11 were 3 out of 11 samples at leaf node
										else:
											pixels_high.append((9, 18))
											if features[13][10] <= 4.5:
												pixels_low.append((13, 10))
												ans = 2												 # approximately 6 were 2 out of 6 samples at leaf node
											else:
												pixels_high.append((13, 10))
												if features[15][7] <= 247.0:
													pixels_low.append((15, 7))
													ans = 8													 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													pixels_high.append((15, 7))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
									else:
										pixels_high.append((7, 17))
										if features[9][14] <= 19.5:
											pixels_low.append((9, 14))
											if features[9][20] <= 252.5:
												pixels_low.append((9, 20))
												if features[10][22] <= 71.0:
													pixels_low.append((10, 22))
													ans = 2													 # approximately 2 were 2 out of 2 samples at leaf node
												else:
													pixels_high.append((10, 22))
													if features[7][22] <= 97.5:
														pixels_low.append((7, 22))
														ans = 6														 # approximately 1 were 6 out of 1 samples at leaf node
													else:
														pixels_high.append((7, 22))
														ans = 8														 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												pixels_high.append((9, 20))
												ans = 3												 # approximately 4 were 3 out of 4 samples at leaf node
										else:
											pixels_high.append((9, 14))
											if features[7][12] <= 185.5:
												pixels_low.append((7, 12))
												if features[24][9] <= 10.5:
													pixels_low.append((24, 9))
													if features[15][5] <= 7.5:
														pixels_low.append((15, 5))
														ans = 8														 # approximately 1 were 8 out of 1 samples at leaf node
													else:
														pixels_high.append((15, 5))
														ans = 2														 # approximately 82 were 2 out of 82 samples at leaf node
												else:
													pixels_high.append((24, 9))
													ans = 8													 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												pixels_high.append((7, 12))
												ans = 6												 # approximately 1 were 6 out of 1 samples at leaf node
								else:
									pixels_high.append((12, 10))
									if features[18][9] <= 173.0:
										pixels_low.append((18, 9))
										if features[21][8] <= 169.0:
											pixels_low.append((21, 8))
											ans = 6											 # approximately 16 were 6 out of 16 samples at leaf node
										else:
											pixels_high.append((21, 8))
											ans = 0											 # approximately 1 were 0 out of 1 samples at leaf node
									else:
										pixels_high.append((18, 9))
										if features[16][21] <= 39.0:
											pixels_low.append((16, 21))
											ans = 2											 # approximately 5 were 2 out of 5 samples at leaf node
										else:
											pixels_high.append((16, 21))
											if features[22][16] <= 250.0:
												pixels_low.append((22, 16))
												if features[15][10] <= 42.5:
													pixels_low.append((15, 10))
													ans = 9													 # approximately 2 were 9 out of 2 samples at leaf node
												else:
													pixels_high.append((15, 10))
													if features[9][10] <= 39.0:
														pixels_low.append((9, 10))
														ans = 3														 # approximately 2 were 3 out of 2 samples at leaf node
													else:
														pixels_high.append((9, 10))
														if features[21][15] <= 126.5:
															pixels_low.append((21, 15))
															if features[12][18] <= 253.5:
																pixels_low.append((12, 18))
																ans = 4																 # approximately 1 were 4 out of 1 samples at leaf node
															else:
																pixels_high.append((12, 18))
																ans = 8																 # approximately 1 were 8 out of 1 samples at leaf node
														else:
															pixels_high.append((21, 15))
															ans = 6															 # approximately 1 were 6 out of 1 samples at leaf node
											else:
												pixels_high.append((22, 16))
												ans = 0												 # approximately 3 were 0 out of 3 samples at leaf node
		else:
			pixels_high.append((13, 23))
			if features[12][17] <= 1.5:
				pixels_low.append((12, 17))
				if features[10][10] <= 11.5:
					pixels_low.append((10, 10))
					if features[16][10] <= 3.5:
						pixels_low.append((16, 10))
						if features[19][10] <= 1.0:
							pixels_low.append((19, 10))
							if features[15][9] <= 64.5:
								pixels_low.append((15, 9))
								if features[9][17] <= 110.0:
									pixels_low.append((9, 17))
									if features[16][5] <= 0.5:
										pixels_low.append((16, 5))
										if features[10][22] <= 204.0:
											pixels_low.append((10, 22))
											ans = 3											 # approximately 5 were 3 out of 5 samples at leaf node
										else:
											pixels_high.append((10, 22))
											ans = 5											 # approximately 3 were 5 out of 3 samples at leaf node
									else:
										pixels_high.append((16, 5))
										if features[11][19] <= 231.0:
											pixels_low.append((11, 19))
											if features[13][6] <= 7.5:
												pixels_low.append((13, 6))
												if features[11][12] <= 11.5:
													pixels_low.append((11, 12))
													ans = 3													 # approximately 2 were 3 out of 2 samples at leaf node
												else:
													pixels_high.append((11, 12))
													if features[14][19] <= 1.0:
														pixels_low.append((14, 19))
														ans = 5														 # approximately 2 were 5 out of 2 samples at leaf node
													else:
														pixels_high.append((14, 19))
														ans = 8														 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												pixels_high.append((13, 6))
												if features[22][11] <= 105.0:
													pixels_low.append((22, 11))
													if features[12][4] <= 254.5:
														pixels_low.append((12, 4))
														if features[14][21] <= 254.5:
															pixels_low.append((14, 21))
															ans = 5															 # approximately 131 were 5 out of 131 samples at leaf node
														else:
															pixels_high.append((14, 21))
															if features[15][18] <= 6.5:
																pixels_low.append((15, 18))
																ans = 5																 # approximately 2 were 5 out of 2 samples at leaf node
															else:
																pixels_high.append((15, 18))
																ans = 3																 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														pixels_high.append((12, 4))
														if features[8][5] <= 113.0:
															pixels_low.append((8, 5))
															ans = 3															 # approximately 1 were 3 out of 1 samples at leaf node
														else:
															pixels_high.append((8, 5))
															ans = 5															 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													pixels_high.append((22, 11))
													ans = 9													 # approximately 1 were 9 out of 1 samples at leaf node
										else:
											pixels_high.append((11, 19))
											if features[17][16] <= 120.5:
												pixels_low.append((17, 16))
												ans = 3												 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												pixels_high.append((17, 16))
												ans = 2												 # approximately 1 were 2 out of 1 samples at leaf node
								else:
									pixels_high.append((9, 17))
									if features[20][12] <= 25.5:
										pixels_low.append((20, 12))
										if features[18][6] <= 233.5:
											pixels_low.append((18, 6))
											if features[17][15] <= 215.0:
												pixels_low.append((17, 15))
												ans = 6												 # approximately 3 were 6 out of 3 samples at leaf node
											else:
												pixels_high.append((17, 15))
												if features[10][8] <= 24.5:
													pixels_low.append((10, 8))
													ans = 2													 # approximately 2 were 2 out of 2 samples at leaf node
												else:
													pixels_high.append((10, 8))
													ans = 8													 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											pixels_high.append((18, 6))
											ans = 5											 # approximately 4 were 5 out of 4 samples at leaf node
									else:
										pixels_high.append((20, 12))
										ans = 8										 # approximately 6 were 8 out of 6 samples at leaf node
							else:
								pixels_high.append((15, 9))
								if features[21][6] <= 2.5:
									pixels_low.append((21, 6))
									if features[14][5] <= 9.0:
										pixels_low.append((14, 5))
										if features[20][4] <= 46.0:
											pixels_low.append((20, 4))
											ans = 6											 # approximately 1 were 6 out of 1 samples at leaf node
										else:
											pixels_high.append((20, 4))
											ans = 5											 # approximately 1 were 5 out of 1 samples at leaf node
									else:
										pixels_high.append((14, 5))
										if features[13][17] <= 59.5:
											pixels_low.append((13, 17))
											ans = 3											 # approximately 85 were 3 out of 85 samples at leaf node
										else:
											pixels_high.append((13, 17))
											ans = 1											 # approximately 1 were 1 out of 1 samples at leaf node
								else:
									pixels_high.append((21, 6))
									if features[14][24] <= 3.0:
										pixels_low.append((14, 24))
										ans = 5										 # approximately 7 were 5 out of 7 samples at leaf node
									else:
										pixels_high.append((14, 24))
										ans = 8										 # approximately 1 were 8 out of 1 samples at leaf node
						else:
							pixels_high.append((19, 10))
							if features[16][13] <= 130.0:
								pixels_low.append((16, 13))
								if features[12][10] <= 99.0:
									pixels_low.append((12, 10))
									if features[11][23] <= 121.5:
										pixels_low.append((11, 23))
										if features[9][4] <= 11.0:
											pixels_low.append((9, 4))
											ans = 8											 # approximately 4 were 8 out of 4 samples at leaf node
										else:
											pixels_high.append((9, 4))
											ans = 2											 # approximately 1 were 2 out of 1 samples at leaf node
									else:
										pixels_high.append((11, 23))
										if features[8][13] <= 51.5:
											pixels_low.append((8, 13))
											if features[15][9] <= 29.5:
												pixels_low.append((15, 9))
												if features[15][4] <= 254.5:
													pixels_low.append((15, 4))
													ans = 2													 # approximately 33 were 2 out of 33 samples at leaf node
												else:
													pixels_high.append((15, 4))
													ans = 3													 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												pixels_high.append((15, 9))
												ans = 7												 # approximately 1 were 7 out of 1 samples at leaf node
										else:
											pixels_high.append((8, 13))
											if features[10][14] <= 135.0:
												pixels_low.append((10, 14))
												ans = 0												 # approximately 2 were 0 out of 2 samples at leaf node
											else:
												pixels_high.append((10, 14))
												if features[5][21] <= 50.0:
													pixels_low.append((5, 21))
													ans = 9													 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													pixels_high.append((5, 21))
													ans = 3													 # approximately 1 were 3 out of 1 samples at leaf node
								else:
									pixels_high.append((12, 10))
									if features[12][22] <= 39.5:
										pixels_low.append((12, 22))
										if features[19][12] <= 142.0:
											pixels_low.append((19, 12))
											ans = 8											 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											pixels_high.append((19, 12))
											ans = 4											 # approximately 1 were 4 out of 1 samples at leaf node
									else:
										pixels_high.append((12, 22))
										ans = 0										 # approximately 34 were 0 out of 34 samples at leaf node
							else:
								pixels_high.append((16, 13))
								if features[9][17] <= 0.5:
									pixels_low.append((9, 17))
									if features[13][18] <= 231.0:
										pixels_low.append((13, 18))
										if features[7][14] <= 227.5:
											pixels_low.append((7, 14))
											if features[11][10] <= 95.0:
												pixels_low.append((11, 10))
												if features[22][11] <= 252.5:
													pixels_low.append((22, 11))
													if features[19][23] <= 253.5:
														pixels_low.append((19, 23))
														if features[7][12] <= 224.5:
															pixels_low.append((7, 12))
															ans = 3															 # approximately 138 were 3 out of 138 samples at leaf node
														else:
															pixels_high.append((7, 12))
															if features[16][6] <= 100.0:
																pixels_low.append((16, 6))
																ans = 3																 # approximately 1 were 3 out of 1 samples at leaf node
															else:
																pixels_high.append((16, 6))
																ans = 9																 # approximately 1 were 9 out of 1 samples at leaf node
													else:
														pixels_high.append((19, 23))
														ans = 8														 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													pixels_high.append((22, 11))
													ans = 8													 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												pixels_high.append((11, 10))
												if features[16][16] <= 123.0:
													pixels_low.append((16, 16))
													ans = 4													 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													pixels_high.append((16, 16))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											pixels_high.append((7, 14))
											if features[15][4] <= 86.5:
												pixels_low.append((15, 4))
												if features[20][9] <= 246.0:
													pixels_low.append((20, 9))
													ans = 8													 # approximately 2 were 8 out of 2 samples at leaf node
												else:
													pixels_high.append((20, 9))
													ans = 9													 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												pixels_high.append((15, 4))
												ans = 2												 # approximately 2 were 2 out of 2 samples at leaf node
									else:
										pixels_high.append((13, 18))
										if features[11][13] <= 98.0:
											pixels_low.append((11, 13))
											ans = 2											 # approximately 3 were 2 out of 3 samples at leaf node
										else:
											pixels_high.append((11, 13))
											ans = 8											 # approximately 2 were 8 out of 2 samples at leaf node
								else:
									pixels_high.append((9, 17))
									if features[11][15] <= 95.5:
										pixels_low.append((11, 15))
										if features[8][10] <= 124.0:
											pixels_low.append((8, 10))
											ans = 3											 # approximately 4 were 3 out of 4 samples at leaf node
										else:
											pixels_high.append((8, 10))
											ans = 6											 # approximately 1 were 6 out of 1 samples at leaf node
									else:
										pixels_high.append((11, 15))
										if features[17][21] <= 252.5:
											pixels_low.append((17, 21))
											if features[17][5] <= 2.0:
												pixels_low.append((17, 5))
												if features[16][9] <= 20.5:
													pixels_low.append((16, 9))
													ans = 4													 # approximately 2 were 4 out of 2 samples at leaf node
												else:
													pixels_high.append((16, 9))
													ans = 2													 # approximately 2 were 2 out of 2 samples at leaf node
											else:
												pixels_high.append((17, 5))
												ans = 8												 # approximately 29 were 8 out of 29 samples at leaf node
										else:
											pixels_high.append((17, 21))
											if features[12][13] <= 222.5:
												pixels_low.append((12, 13))
												ans = 3												 # approximately 3 were 3 out of 3 samples at leaf node
											else:
												pixels_high.append((12, 13))
												ans = 9												 # approximately 1 were 9 out of 1 samples at leaf node
					else:
						pixels_high.append((16, 10))
						if features[13][9] <= 204.5:
							pixels_low.append((13, 9))
							if features[8][11] <= 172.0:
								pixels_low.append((8, 11))
								if features[14][12] <= 3.5:
									pixels_low.append((14, 12))
									if features[14][18] <= 10.5:
										pixels_low.append((14, 18))
										if features[12][8] <= 79.5:
											pixels_low.append((12, 8))
											if features[8][18] <= 41.5:
												pixels_low.append((8, 18))
												ans = 3												 # approximately 20 were 3 out of 20 samples at leaf node
											else:
												pixels_high.append((8, 18))
												ans = 2												 # approximately 2 were 2 out of 2 samples at leaf node
										else:
											pixels_high.append((12, 8))
											if features[14][10] <= 119.0:
												pixels_low.append((14, 10))
												ans = 0												 # approximately 2 were 0 out of 2 samples at leaf node
											else:
												pixels_high.append((14, 10))
												ans = 9												 # approximately 1 were 9 out of 1 samples at leaf node
									else:
										pixels_high.append((14, 18))
										if features[10][21] <= 165.5:
											pixels_low.append((10, 21))
											if features[21][19] <= 28.5:
												pixels_low.append((21, 19))
												if features[17][8] <= 144.0:
													pixels_low.append((17, 8))
													if features[11][13] <= 1.5:
														pixels_low.append((11, 13))
														ans = 1														 # approximately 1 were 1 out of 1 samples at leaf node
													else:
														pixels_high.append((11, 13))
														if features[19][21] <= 102.5:
															pixels_low.append((19, 21))
															ans = 4															 # approximately 1 were 4 out of 1 samples at leaf node
														else:
															pixels_high.append((19, 21))
															ans = 8															 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													pixels_high.append((17, 8))
													ans = 7													 # approximately 6 were 7 out of 6 samples at leaf node
											else:
												pixels_high.append((21, 19))
												ans = 2												 # approximately 3 were 2 out of 3 samples at leaf node
										else:
											pixels_high.append((10, 21))
											ans = 2											 # approximately 12 were 2 out of 12 samples at leaf node
								else:
									pixels_high.append((14, 12))
									if features[9][17] <= 252.5:
										pixels_low.append((9, 17))
										if features[14][18] <= 237.5:
											pixels_low.append((14, 18))
											if features[12][10] <= 252.5:
												pixels_low.append((12, 10))
												if features[18][24] <= 251.5:
													pixels_low.append((18, 24))
													if features[7][11] <= 253.0:
														pixels_low.append((7, 11))
														if features[24][17] <= 157.0:
															pixels_low.append((24, 17))
															if features[13][9] <= 192.5:
																pixels_low.append((13, 9))
																if features[10][17] <= 175.0:
																	pixels_low.append((10, 17))
																	if features[8][17] <= 251.0:
																		pixels_low.append((8, 17))
																		ans = 3																		 # approximately 1471 were 3 out of 1471 samples at leaf node
																	else:
																		pixels_high.append((8, 17))
																		if features[12][6] <= 66.5:
																			pixels_low.append((12, 6))
																			if features[16][9] <= 126.5:
																				pixels_low.append((16, 9))
																				ans = 2																				 # approximately 1 were 2 out of 1 samples at leaf node
																			else:
																				pixels_high.append((16, 9))
																				ans = 8																				 # approximately 1 were 8 out of 1 samples at leaf node
																		else:
																			pixels_high.append((12, 6))
																			ans = 3																			 # approximately 20 were 3 out of 20 samples at leaf node
																else:
																	pixels_high.append((10, 17))
																	if features[16][13] <= 198.0:
																		pixels_low.append((16, 13))
																		ans = 8																		 # approximately 1 were 8 out of 1 samples at leaf node
																	else:
																		pixels_high.append((16, 13))
																		ans = 3																		 # approximately 5 were 3 out of 5 samples at leaf node
															else:
																pixels_high.append((13, 9))
																if features[17][13] <= 98.5:
																	pixels_low.append((17, 13))
																	if features[9][11] <= 4.0:
																		pixels_low.append((9, 11))
																		ans = 1																		 # approximately 1 were 1 out of 1 samples at leaf node
																	else:
																		pixels_high.append((9, 11))
																		ans = 0																		 # approximately 1 were 0 out of 1 samples at leaf node
																else:
																	pixels_high.append((17, 13))
																	ans = 3																	 # approximately 6 were 3 out of 6 samples at leaf node
														else:
															pixels_high.append((24, 17))
															if features[8][5] <= 114.5:
																pixels_low.append((8, 5))
																ans = 3																 # approximately 1 were 3 out of 1 samples at leaf node
															else:
																pixels_high.append((8, 5))
																ans = 2																 # approximately 1 were 2 out of 1 samples at leaf node
													else:
														pixels_high.append((7, 11))
														ans = 8														 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													pixels_high.append((18, 24))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												pixels_high.append((12, 10))
												if features[10][17] <= 38.5:
													pixels_low.append((10, 17))
													if features[15][21] <= 226.5:
														pixels_low.append((15, 21))
														ans = 5														 # approximately 2 were 5 out of 2 samples at leaf node
													else:
														pixels_high.append((15, 21))
														ans = 3														 # approximately 2 were 3 out of 2 samples at leaf node
												else:
													pixels_high.append((10, 17))
													ans = 8													 # approximately 3 were 8 out of 3 samples at leaf node
										else:
											pixels_high.append((14, 18))
											if features[11][20] <= 12.0:
												pixels_low.append((11, 20))
												if features[9][9] <= 2.0:
													pixels_low.append((9, 9))
													ans = 1													 # approximately 8 were 1 out of 8 samples at leaf node
												else:
													pixels_high.append((9, 9))
													ans = 9													 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												pixels_high.append((11, 20))
												ans = 3												 # approximately 10 were 3 out of 10 samples at leaf node
									else:
										pixels_high.append((9, 17))
										if features[12][15] <= 194.0:
											pixels_low.append((12, 15))
											if features[15][11] <= 139.0:
												pixels_low.append((15, 11))
												if features[12][23] <= 171.0:
													pixels_low.append((12, 23))
													ans = 0													 # approximately 1 were 0 out of 1 samples at leaf node
												else:
													pixels_high.append((12, 23))
													ans = 2													 # approximately 2 were 2 out of 2 samples at leaf node
											else:
												pixels_high.append((15, 11))
												ans = 3												 # approximately 3 were 3 out of 3 samples at leaf node
										else:
											pixels_high.append((12, 15))
											ans = 8											 # approximately 5 were 8 out of 5 samples at leaf node
							else:
								pixels_high.append((8, 11))
								if features[9][16] <= 59.0:
									pixels_low.append((9, 16))
									if features[15][9] <= 92.0:
										pixels_low.append((15, 9))
										if features[10][22] <= 227.5:
											pixels_low.append((10, 22))
											if features[18][10] <= 58.0:
												pixels_low.append((18, 10))
												ans = 5												 # approximately 4 were 5 out of 4 samples at leaf node
											else:
												pixels_high.append((18, 10))
												if features[9][19] <= 97.0:
													pixels_low.append((9, 19))
													if features[17][12] <= 250.0:
														pixels_low.append((17, 12))
														ans = 8														 # approximately 1 were 8 out of 1 samples at leaf node
													else:
														pixels_high.append((17, 12))
														if features[8][14] <= 15.0:
															pixels_low.append((8, 14))
															ans = 2															 # approximately 1 were 2 out of 1 samples at leaf node
														else:
															pixels_high.append((8, 14))
															ans = 9															 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													pixels_high.append((9, 19))
													ans = 0													 # approximately 1 were 0 out of 1 samples at leaf node
										else:
											pixels_high.append((10, 22))
											ans = 3											 # approximately 5 were 3 out of 5 samples at leaf node
									else:
										pixels_high.append((15, 9))
										ans = 9										 # approximately 7 were 9 out of 7 samples at leaf node
								else:
									pixels_high.append((9, 16))
									if features[9][12] <= 109.5:
										pixels_low.append((9, 12))
										ans = 3										 # approximately 1 were 3 out of 1 samples at leaf node
									else:
										pixels_high.append((9, 12))
										ans = 8										 # approximately 11 were 8 out of 11 samples at leaf node
						else:
							pixels_high.append((13, 9))
							if features[9][17] <= 139.5:
								pixels_low.append((9, 17))
								if features[11][6] <= 1.5:
									pixels_low.append((11, 6))
									if features[16][13] <= 157.0:
										pixels_low.append((16, 13))
										ans = 5										 # approximately 10 were 5 out of 10 samples at leaf node
									else:
										pixels_high.append((16, 13))
										if features[18][8] <= 7.5:
											pixels_low.append((18, 8))
											if features[17][13] <= 121.5:
												pixels_low.append((17, 13))
												ans = 1												 # approximately 8 were 1 out of 8 samples at leaf node
											else:
												pixels_high.append((17, 13))
												ans = 3												 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											pixels_high.append((18, 8))
											if features[19][9] <= 223.0:
												pixels_low.append((19, 9))
												if features[18][10] <= 124.0:
													pixels_low.append((18, 10))
													if features[16][15] <= 248.5:
														pixels_low.append((16, 15))
														if features[9][23] <= 62.0:
															pixels_low.append((9, 23))
															if features[17][7] <= 135.0:
																pixels_low.append((17, 7))
																ans = 6																 # approximately 1 were 6 out of 1 samples at leaf node
															else:
																pixels_high.append((17, 7))
																ans = 0																 # approximately 1 were 0 out of 1 samples at leaf node
														else:
															pixels_high.append((9, 23))
															ans = 5															 # approximately 2 were 5 out of 2 samples at leaf node
													else:
														pixels_high.append((16, 15))
														ans = 4														 # approximately 3 were 4 out of 3 samples at leaf node
												else:
													pixels_high.append((18, 10))
													ans = 9													 # approximately 5 were 9 out of 5 samples at leaf node
											else:
												pixels_high.append((19, 9))
												ans = 3												 # approximately 4 were 3 out of 4 samples at leaf node
								else:
									pixels_high.append((11, 6))
									if features[15][8] <= 112.5:
										pixels_low.append((15, 8))
										if features[8][23] <= 74.5:
											pixels_low.append((8, 23))
											ans = 5											 # approximately 4 were 5 out of 4 samples at leaf node
										else:
											pixels_high.append((8, 23))
											if features[14][13] <= 213.0:
												pixels_low.append((14, 13))
												ans = 8												 # approximately 2 were 8 out of 2 samples at leaf node
											else:
												pixels_high.append((14, 13))
												ans = 3												 # approximately 2 were 3 out of 2 samples at leaf node
									else:
										pixels_high.append((15, 8))
										if features[14][11] <= 6.0:
											pixels_low.append((14, 11))
											ans = 2											 # approximately 2 were 2 out of 2 samples at leaf node
										else:
											pixels_high.append((14, 11))
											if features[14][17] <= 191.0:
												pixels_low.append((14, 17))
												ans = 3												 # approximately 33 were 3 out of 33 samples at leaf node
											else:
												pixels_high.append((14, 17))
												ans = 1												 # approximately 1 were 1 out of 1 samples at leaf node
							else:
								pixels_high.append((9, 17))
								if features[15][13] <= 162.0:
									pixels_low.append((15, 13))
									if features[17][8] <= 5.5:
										pixels_low.append((17, 8))
										if features[22][8] <= 37.5:
											pixels_low.append((22, 8))
											ans = 5											 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											pixels_high.append((22, 8))
											ans = 8											 # approximately 1 were 8 out of 1 samples at leaf node
									else:
										pixels_high.append((17, 8))
										ans = 0										 # approximately 19 were 0 out of 19 samples at leaf node
								else:
									pixels_high.append((15, 13))
									if features[21][14] <= 28.5:
										pixels_low.append((21, 14))
										ans = 8										 # approximately 14 were 8 out of 14 samples at leaf node
									else:
										pixels_high.append((21, 14))
										ans = 3										 # approximately 2 were 3 out of 2 samples at leaf node
				else:
					pixels_high.append((10, 10))
					if features[18][10] <= 0.5:
						pixels_low.append((18, 10))
						if features[15][9] <= 128.5:
							pixels_low.append((15, 9))
							if features[20][10] <= 2.0:
								pixels_low.append((20, 10))
								if features[9][17] <= 244.5:
									pixels_low.append((9, 17))
									if features[17][5] <= 2.5:
										pixels_low.append((17, 5))
										if features[14][9] <= 99.5:
											pixels_low.append((14, 9))
											if features[10][11] <= 54.0:
												pixels_low.append((10, 11))
												if features[15][7] <= 102.0:
													pixels_low.append((15, 7))
													ans = 5													 # approximately 2 were 5 out of 2 samples at leaf node
												else:
													pixels_high.append((15, 7))
													ans = 3													 # approximately 6 were 3 out of 6 samples at leaf node
											else:
												pixels_high.append((10, 11))
												if features[16][10] <= 54.5:
													pixels_low.append((16, 10))
													if features[20][11] <= 20.0:
														pixels_low.append((20, 11))
														if features[17][14] <= 23.5:
															pixels_low.append((17, 14))
															if features[13][11] <= 124.0:
																pixels_low.append((13, 11))
																ans = 5																 # approximately 1 were 5 out of 1 samples at leaf node
															else:
																pixels_high.append((13, 11))
																ans = 3																 # approximately 1 were 3 out of 1 samples at leaf node
														else:
															pixels_high.append((17, 14))
															ans = 5															 # approximately 51 were 5 out of 51 samples at leaf node
													else:
														pixels_high.append((20, 11))
														ans = 4														 # approximately 2 were 4 out of 2 samples at leaf node
												else:
													pixels_high.append((16, 10))
													if features[18][17] <= 83.0:
														pixels_low.append((18, 17))
														if features[18][7] <= 126.5:
															pixels_low.append((18, 7))
															if features[12][6] <= 198.5:
																pixels_low.append((12, 6))
																ans = 2																 # approximately 1 were 2 out of 1 samples at leaf node
															else:
																pixels_high.append((12, 6))
																if features[12][8] <= 85.0:
																	pixels_low.append((12, 8))
																	ans = 8																	 # approximately 1 were 8 out of 1 samples at leaf node
																else:
																	pixels_high.append((12, 8))
																	ans = 7																	 # approximately 1 were 7 out of 1 samples at leaf node
														else:
															pixels_high.append((18, 7))
															ans = 5															 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														pixels_high.append((18, 17))
														ans = 9														 # approximately 2 were 9 out of 2 samples at leaf node
										else:
											pixels_high.append((14, 9))
											if features[10][5] <= 100.5:
												pixels_low.append((10, 5))
												if features[11][10] <= 174.5:
													pixels_low.append((11, 10))
													ans = 8													 # approximately 2 were 8 out of 2 samples at leaf node
												else:
													pixels_high.append((11, 10))
													if features[11][10] <= 248.0:
														pixels_low.append((11, 10))
														if features[11][11] <= 188.0:
															pixels_low.append((11, 11))
															ans = 0															 # approximately 1 were 0 out of 1 samples at leaf node
														else:
															pixels_high.append((11, 11))
															ans = 3															 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														pixels_high.append((11, 10))
														ans = 5														 # approximately 2 were 5 out of 2 samples at leaf node
											else:
												pixels_high.append((10, 5))
												ans = 3												 # approximately 16 were 3 out of 16 samples at leaf node
									else:
										pixels_high.append((17, 5))
										if features[16][9] <= 184.5:
											pixels_low.append((16, 9))
											if features[11][18] <= 224.5:
												pixels_low.append((11, 18))
												if features[14][17] <= 164.5:
													pixels_low.append((14, 17))
													if features[24][9] <= 46.5:
														pixels_low.append((24, 9))
														if features[22][11] <= 128.0:
															pixels_low.append((22, 11))
															if features[7][6] <= 253.5:
																pixels_low.append((7, 6))
																if features[8][4] <= 218.5:
																	pixels_low.append((8, 4))
																	if features[7][5] <= 253.5:
																		pixels_low.append((7, 5))
																		if features[17][9] <= 175.5:
																			pixels_low.append((17, 9))
																			if features[8][17] <= 253.5:
																				pixels_low.append((8, 17))
																				if features[15][18] <= 253.5:
																					pixels_low.append((15, 18))
																					if features[14][10] <= 254.5:
																						pixels_low.append((14, 10))
																						if features[14][20] <= 254.5:
																							pixels_low.append((14, 20))
																							if features[11][8] <= 1.0:
																								pixels_low.append((11, 8))
																								if features[20][8] <= 125.5:
																									pixels_low.append((20, 8))
																									if features[15][9] <= 88.0:
																										pixels_low.append((15, 9))
																										if features[13][7] <= 252.5:
																											pixels_low.append((13, 7))
																											ans = 5																											 # approximately 50 were 5 out of 50 samples at leaf node
																										else:
																											pixels_high.append((13, 7))
																											ans = 3																											 # approximately 1 were 3 out of 1 samples at leaf node
																									else:
																										pixels_high.append((15, 9))
																										ans = 3																										 # approximately 1 were 3 out of 1 samples at leaf node
																								else:
																									pixels_high.append((20, 8))
																									ans = 8																									 # approximately 1 were 8 out of 1 samples at leaf node
																							else:
																								pixels_high.append((11, 8))
																								ans = 5																								 # approximately 596 were 5 out of 596 samples at leaf node
																						else:
																							pixels_high.append((14, 20))
																							if features[13][24] <= 98.5:
																								pixels_low.append((13, 24))
																								ans = 5																								 # approximately 5 were 5 out of 5 samples at leaf node
																							else:
																								pixels_high.append((13, 24))
																								ans = 9																								 # approximately 1 were 9 out of 1 samples at leaf node
																					else:
																						pixels_high.append((14, 10))
																						if features[12][11] <= 127.5:
																							pixels_low.append((12, 11))
																							ans = 3																							 # approximately 1 were 3 out of 1 samples at leaf node
																						else:
																							pixels_high.append((12, 11))
																							ans = 5																							 # approximately 1 were 5 out of 1 samples at leaf node
																				else:
																					pixels_high.append((15, 18))
																					if features[9][23] <= 112.5:
																						pixels_low.append((9, 23))
																						ans = 9																						 # approximately 1 were 9 out of 1 samples at leaf node
																					else:
																						pixels_high.append((9, 23))
																						ans = 5																						 # approximately 1 were 5 out of 1 samples at leaf node
																			else:
																				pixels_high.append((8, 17))
																				if features[13][21] <= 113.5:
																					pixels_low.append((13, 21))
																					ans = 6																					 # approximately 1 were 6 out of 1 samples at leaf node
																				else:
																					pixels_high.append((13, 21))
																					ans = 5																					 # approximately 1 were 5 out of 1 samples at leaf node
																		else:
																			pixels_high.append((17, 9))
																			if features[7][22] <= 124.5:
																				pixels_low.append((7, 22))
																				if features[19][9] <= 2.5:
																					pixels_low.append((19, 9))
																					ans = 3																					 # approximately 1 were 3 out of 1 samples at leaf node
																				else:
																					pixels_high.append((19, 9))
																					ans = 8																					 # approximately 1 were 8 out of 1 samples at leaf node
																			else:
																				pixels_high.append((7, 22))
																				ans = 5																				 # approximately 2 were 5 out of 2 samples at leaf node
																	else:
																		pixels_high.append((7, 5))
																		ans = 3																		 # approximately 1 were 3 out of 1 samples at leaf node
																else:
																	pixels_high.append((8, 4))
																	ans = 3																	 # approximately 1 were 3 out of 1 samples at leaf node
															else:
																pixels_high.append((7, 6))
																ans = 3																 # approximately 1 were 3 out of 1 samples at leaf node
														else:
															pixels_high.append((22, 11))
															ans = 9															 # approximately 1 were 9 out of 1 samples at leaf node
													else:
														pixels_high.append((24, 9))
														ans = 6														 # approximately 1 were 6 out of 1 samples at leaf node
												else:
													pixels_high.append((14, 17))
													if features[17][11] <= 64.0:
														pixels_low.append((17, 11))
														ans = 8														 # approximately 1 were 8 out of 1 samples at leaf node
													else:
														pixels_high.append((17, 11))
														ans = 9														 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												pixels_high.append((11, 18))
												if features[16][18] <= 126.5:
													pixels_low.append((16, 18))
													ans = 8													 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													pixels_high.append((16, 18))
													ans = 6													 # approximately 1 were 6 out of 1 samples at leaf node
										else:
											pixels_high.append((16, 9))
											if features[13][13] <= 252.5:
												pixels_low.append((13, 13))
												ans = 8												 # approximately 4 were 8 out of 4 samples at leaf node
											else:
												pixels_high.append((13, 13))
												if features[18][12] <= 12.5:
													pixels_low.append((18, 12))
													if features[7][21] <= 120.0:
														pixels_low.append((7, 21))
														ans = 5														 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														pixels_high.append((7, 21))
														ans = 3														 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													pixels_high.append((18, 12))
													ans = 4													 # approximately 1 were 4 out of 1 samples at leaf node
								else:
									pixels_high.append((9, 17))
									if features[12][9] <= 252.5:
										pixels_low.append((12, 9))
										if features[17][6] <= 247.0:
											pixels_low.append((17, 6))
											if features[9][12] <= 124.5:
												pixels_low.append((9, 12))
												ans = 8												 # approximately 4 were 8 out of 4 samples at leaf node
											else:
												pixels_high.append((9, 12))
												ans = 6												 # approximately 4 were 6 out of 4 samples at leaf node
										else:
											pixels_high.append((17, 6))
											ans = 5											 # approximately 11 were 5 out of 11 samples at leaf node
									else:
										pixels_high.append((12, 9))
										ans = 6										 # approximately 10 were 6 out of 10 samples at leaf node
							else:
								pixels_high.append((20, 10))
								if features[16][14] <= 47.0:
									pixels_low.append((16, 14))
									if features[15][23] <= 95.5:
										pixels_low.append((15, 23))
										ans = 0										 # approximately 16 were 0 out of 16 samples at leaf node
									else:
										pixels_high.append((15, 23))
										ans = 2										 # approximately 1 were 2 out of 1 samples at leaf node
								else:
									pixels_high.append((16, 14))
									if features[8][18] <= 13.0:
										pixels_low.append((8, 18))
										if features[15][18] <= 224.0:
											pixels_low.append((15, 18))
											if features[12][7] <= 222.5:
												pixels_low.append((12, 7))
												ans = 8												 # approximately 5 were 8 out of 5 samples at leaf node
											else:
												pixels_high.append((12, 7))
												if features[17][8] <= 92.5:
													pixels_low.append((17, 8))
													ans = 3													 # approximately 4 were 3 out of 4 samples at leaf node
												else:
													pixels_high.append((17, 8))
													if features[8][24] <= 126.5:
														pixels_low.append((8, 24))
														ans = 5														 # approximately 2 were 5 out of 2 samples at leaf node
													else:
														pixels_high.append((8, 24))
														ans = 9														 # approximately 1 were 9 out of 1 samples at leaf node
										else:
											pixels_high.append((15, 18))
											ans = 4											 # approximately 5 were 4 out of 5 samples at leaf node
									else:
										pixels_high.append((8, 18))
										if features[17][13] <= 88.0:
											pixels_low.append((17, 13))
											ans = 2											 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											pixels_high.append((17, 13))
											ans = 8											 # approximately 20 were 8 out of 20 samples at leaf node
						else:
							pixels_high.append((15, 9))
							if features[20][7] <= 8.5:
								pixels_low.append((20, 7))
								if features[15][17] <= 47.0:
									pixels_low.append((15, 17))
									if features[10][17] <= 207.0:
										pixels_low.append((10, 17))
										if features[16][16] <= 243.5:
											pixels_low.append((16, 16))
											if features[9][9] <= 254.5:
												pixels_low.append((9, 9))
												if features[14][10] <= 7.0:
													pixels_low.append((14, 10))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													pixels_high.append((14, 10))
													if features[13][5] <= 17.0:
														pixels_low.append((13, 5))
														if features[9][8] <= 201.5:
															pixels_low.append((9, 8))
															ans = 3															 # approximately 3 were 3 out of 3 samples at leaf node
														else:
															pixels_high.append((9, 8))
															ans = 5															 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														pixels_high.append((13, 5))
														ans = 3														 # approximately 108 were 3 out of 108 samples at leaf node
											else:
												pixels_high.append((9, 9))
												ans = 9												 # approximately 1 were 9 out of 1 samples at leaf node
										else:
											pixels_high.append((16, 16))
											if features[17][20] <= 195.5:
												pixels_low.append((17, 20))
												ans = 9												 # approximately 2 were 9 out of 2 samples at leaf node
											else:
												pixels_high.append((17, 20))
												if features[20][23] <= 62.5:
													pixels_low.append((20, 23))
													ans = 3													 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													pixels_high.append((20, 23))
													ans = 4													 # approximately 1 were 4 out of 1 samples at leaf node
									else:
										pixels_high.append((10, 17))
										if features[13][8] <= 253.5:
											pixels_low.append((13, 8))
											ans = 8											 # approximately 2 were 8 out of 2 samples at leaf node
										else:
											pixels_high.append((13, 8))
											ans = 5											 # approximately 1 were 5 out of 1 samples at leaf node
								else:
									pixels_high.append((15, 17))
									if features[11][21] <= 9.5:
										pixels_low.append((11, 21))
										if features[17][23] <= 143.5:
											pixels_low.append((17, 23))
											ans = 4											 # approximately 10 were 4 out of 10 samples at leaf node
										else:
											pixels_high.append((17, 23))
											if features[12][9] <= 198.5:
												pixels_low.append((12, 9))
												ans = 8												 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												pixels_high.append((12, 9))
												ans = 2												 # approximately 1 were 2 out of 1 samples at leaf node
									else:
										pixels_high.append((11, 21))
										if features[11][21] <= 141.0:
											pixels_low.append((11, 21))
											if features[11][12] <= 222.0:
												pixels_low.append((11, 12))
												ans = 8												 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												pixels_high.append((11, 12))
												ans = 9												 # approximately 5 were 9 out of 5 samples at leaf node
										else:
											pixels_high.append((11, 21))
											if features[14][10] <= 248.0:
												pixels_low.append((14, 10))
												if features[6][21] <= 20.5:
													pixels_low.append((6, 21))
													ans = 1													 # approximately 2 were 1 out of 2 samples at leaf node
												else:
													pixels_high.append((6, 21))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												pixels_high.append((14, 10))
												ans = 3												 # approximately 4 were 3 out of 4 samples at leaf node
							else:
								pixels_high.append((20, 7))
								if features[19][12] <= 127.0:
									pixels_low.append((19, 12))
									if features[15][10] <= 226.0:
										pixels_low.append((15, 10))
										ans = 5										 # approximately 34 were 5 out of 34 samples at leaf node
									else:
										pixels_high.append((15, 10))
										if features[16][23] <= 221.0:
											pixels_low.append((16, 23))
											if features[7][19] <= 18.5:
												pixels_low.append((7, 19))
												ans = 3												 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												pixels_high.append((7, 19))
												if features[11][7] <= 48.5:
													pixels_low.append((11, 7))
													ans = 6													 # approximately 1 were 6 out of 1 samples at leaf node
												else:
													pixels_high.append((11, 7))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											pixels_high.append((16, 23))
											ans = 8											 # approximately 3 were 8 out of 3 samples at leaf node
								else:
									pixels_high.append((19, 12))
									if features[8][15] <= 216.5:
										pixels_low.append((8, 15))
										if features[21][13] <= 44.0:
											pixels_low.append((21, 13))
											if features[7][18] <= 11.0:
												pixels_low.append((7, 18))
												ans = 9												 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												pixels_high.append((7, 18))
												ans = 8												 # approximately 2 were 8 out of 2 samples at leaf node
										else:
											pixels_high.append((21, 13))
											ans = 3											 # approximately 3 were 3 out of 3 samples at leaf node
									else:
										pixels_high.append((8, 15))
										ans = 0										 # approximately 11 were 0 out of 11 samples at leaf node
					else:
						pixels_high.append((18, 10))
						if features[15][13] <= 1.0:
							pixels_low.append((15, 13))
							if features[8][16] <= 5.5:
								pixels_low.append((8, 16))
								if features[10][16] <= 139.0:
									pixels_low.append((10, 16))
									if features[15][10] <= 25.5:
										pixels_low.append((15, 10))
										if features[18][16] <= 49.5:
											pixels_low.append((18, 16))
											if features[10][15] <= 10.0:
												pixels_low.append((10, 15))
												ans = 8												 # approximately 6 were 8 out of 6 samples at leaf node
											else:
												pixels_high.append((10, 15))
												if features[12][15] <= 68.5:
													pixels_low.append((12, 15))
													ans = 7													 # approximately 2 were 7 out of 2 samples at leaf node
												else:
													pixels_high.append((12, 15))
													if features[14][17] <= 38.5:
														pixels_low.append((14, 17))
														ans = 5														 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														pixels_high.append((14, 17))
														ans = 4														 # approximately 1 were 4 out of 1 samples at leaf node
										else:
											pixels_high.append((18, 16))
											if features[13][15] <= 127.0:
												pixels_low.append((13, 15))
												ans = 2												 # approximately 11 were 2 out of 11 samples at leaf node
											else:
												pixels_high.append((13, 15))
												ans = 4												 # approximately 1 were 4 out of 1 samples at leaf node
									else:
										pixels_high.append((15, 10))
										if features[18][9] <= 61.0:
											pixels_low.append((18, 9))
											if features[15][8] <= 250.5:
												pixels_low.append((15, 8))
												ans = 5												 # approximately 16 were 5 out of 16 samples at leaf node
											else:
												pixels_high.append((15, 8))
												ans = 3												 # approximately 2 were 3 out of 2 samples at leaf node
										else:
											pixels_high.append((18, 9))
											if features[7][15] <= 9.5:
												pixels_low.append((7, 15))
												if features[10][11] <= 161.0:
													pixels_low.append((10, 11))
													if features[16][19] <= 166.5:
														pixels_low.append((16, 19))
														ans = 5														 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														pixels_high.append((16, 19))
														ans = 9														 # approximately 3 were 9 out of 3 samples at leaf node
												else:
													pixels_high.append((10, 11))
													ans = 3													 # approximately 7 were 3 out of 7 samples at leaf node
											else:
												pixels_high.append((7, 15))
												ans = 0												 # approximately 4 were 0 out of 4 samples at leaf node
								else:
									pixels_high.append((10, 16))
									ans = 0									 # approximately 13 were 0 out of 13 samples at leaf node
							else:
								pixels_high.append((8, 16))
								if features[16][15] <= 230.5:
									pixels_low.append((16, 15))
									if features[8][4] <= 29.5:
										pixels_low.append((8, 4))
										if features[15][5] <= 5.5:
											pixels_low.append((15, 5))
											ans = 9											 # approximately 1 were 9 out of 1 samples at leaf node
										else:
											pixels_high.append((15, 5))
											ans = 0											 # approximately 210 were 0 out of 210 samples at leaf node
									else:
										pixels_high.append((8, 4))
										ans = 3										 # approximately 1 were 3 out of 1 samples at leaf node
								else:
									pixels_high.append((16, 15))
									if features[16][6] <= 10.5:
										pixels_low.append((16, 6))
										ans = 4										 # approximately 3 were 4 out of 3 samples at leaf node
									else:
										pixels_high.append((16, 6))
										if features[13][13] <= 14.5:
											pixels_low.append((13, 13))
											ans = 2											 # approximately 2 were 2 out of 2 samples at leaf node
										else:
											pixels_high.append((13, 13))
											ans = 6											 # approximately 1 were 6 out of 1 samples at leaf node
						else:
							pixels_high.append((15, 13))
							if features[9][17] <= 73.5:
								pixels_low.append((9, 17))
								if features[8][22] <= 20.5:
									pixels_low.append((8, 22))
									if features[19][17] <= 2.0:
										pixels_low.append((19, 17))
										if features[13][19] <= 55.0:
											pixels_low.append((13, 19))
											if features[17][14] <= 109.5:
												pixels_low.append((17, 14))
												ans = 3												 # approximately 2 were 3 out of 2 samples at leaf node
											else:
												pixels_high.append((17, 14))
												if features[9][16] <= 169.0:
													pixels_low.append((9, 16))
													if features[10][5] <= 20.5:
														pixels_low.append((10, 5))
														ans = 9														 # approximately 24 were 9 out of 24 samples at leaf node
													else:
														pixels_high.append((10, 5))
														if features[16][8] <= 173.5:
															pixels_low.append((16, 8))
															ans = 9															 # approximately 1 were 9 out of 1 samples at leaf node
														else:
															pixels_high.append((16, 8))
															ans = 3															 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													pixels_high.append((9, 16))
													ans = 4													 # approximately 1 were 4 out of 1 samples at leaf node
										else:
											pixels_high.append((13, 19))
											if features[18][5] <= 63.0:
												pixels_low.append((18, 5))
												if features[12][7] <= 251.5:
													pixels_low.append((12, 7))
													if features[15][18] <= 236.0:
														pixels_low.append((15, 18))
														if features[17][19] <= 115.5:
															pixels_low.append((17, 19))
															if features[9][9] <= 126.0:
																pixels_low.append((9, 9))
																ans = 1																 # approximately 1 were 1 out of 1 samples at leaf node
															else:
																pixels_high.append((9, 9))
																ans = 2																 # approximately 2 were 2 out of 2 samples at leaf node
														else:
															pixels_high.append((17, 19))
															ans = 8															 # approximately 2 were 8 out of 2 samples at leaf node
													else:
														pixels_high.append((15, 18))
														ans = 4														 # approximately 5 were 4 out of 5 samples at leaf node
												else:
													pixels_high.append((12, 7))
													if features[18][9] <= 252.5:
														pixels_low.append((18, 9))
														ans = 9														 # approximately 3 were 9 out of 3 samples at leaf node
													else:
														pixels_high.append((18, 9))
														ans = 7														 # approximately 1 were 7 out of 1 samples at leaf node
											else:
												pixels_high.append((18, 5))
												ans = 8												 # approximately 6 were 8 out of 6 samples at leaf node
									else:
										pixels_high.append((19, 17))
										if features[14][12] <= 56.5:
											pixels_low.append((14, 12))
											if features[12][10] <= 77.0:
												pixels_low.append((12, 10))
												ans = 8												 # approximately 9 were 8 out of 9 samples at leaf node
											else:
												pixels_high.append((12, 10))
												if features[15][7] <= 137.5:
													pixels_low.append((15, 7))
													ans = 4													 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													pixels_high.append((15, 7))
													ans = 3													 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											pixels_high.append((14, 12))
											if features[11][10] <= 252.5:
												pixels_low.append((11, 10))
												if features[13][21] <= 21.0:
													pixels_low.append((13, 21))
													if features[11][11] <= 57.0:
														pixels_low.append((11, 11))
														ans = 9														 # approximately 6 were 9 out of 6 samples at leaf node
													else:
														pixels_high.append((11, 11))
														if features[14][13] <= 215.5:
															pixels_low.append((14, 13))
															ans = 8															 # approximately 2 were 8 out of 2 samples at leaf node
														else:
															pixels_high.append((14, 13))
															ans = 3															 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													pixels_high.append((13, 21))
													if features[17][10] <= 100.5:
														pixels_low.append((17, 10))
														if features[18][10] <= 135.0:
															pixels_low.append((18, 10))
															ans = 5															 # approximately 3 were 5 out of 3 samples at leaf node
														else:
															pixels_high.append((18, 10))
															if features[14][19] <= 191.0:
																pixels_low.append((14, 19))
																ans = 4																 # approximately 1 were 4 out of 1 samples at leaf node
															else:
																pixels_high.append((14, 19))
																ans = 8																 # approximately 1 were 8 out of 1 samples at leaf node
													else:
														pixels_high.append((17, 10))
														if features[10][16] <= 157.5:
															pixels_low.append((10, 16))
															ans = 3															 # approximately 20 were 3 out of 20 samples at leaf node
														else:
															pixels_high.append((10, 16))
															if features[19][13] <= 5.5:
																pixels_low.append((19, 13))
																ans = 4																 # approximately 1 were 4 out of 1 samples at leaf node
															else:
																pixels_high.append((19, 13))
																ans = 8																 # approximately 2 were 8 out of 2 samples at leaf node
											else:
												pixels_high.append((11, 10))
												ans = 5												 # approximately 5 were 5 out of 5 samples at leaf node
								else:
									pixels_high.append((8, 22))
									if features[7][14] <= 81.5:
										pixels_low.append((7, 14))
										if features[11][10] <= 246.5:
											pixels_low.append((11, 10))
											if features[16][24] <= 252.5:
												pixels_low.append((16, 24))
												if features[8][11] <= 253.5:
													pixels_low.append((8, 11))
													if features[22][5] <= 242.5:
														pixels_low.append((22, 5))
														if features[10][10] <= 203.0:
															pixels_low.append((10, 10))
															ans = 3															 # approximately 118 were 3 out of 118 samples at leaf node
														else:
															pixels_high.append((10, 10))
															if features[10][12] <= 190.0:
																pixels_low.append((10, 12))
																if features[17][4] <= 156.0:
																	pixels_low.append((17, 4))
																	ans = 3																	 # approximately 27 were 3 out of 27 samples at leaf node
																else:
																	pixels_high.append((17, 4))
																	ans = 1																	 # approximately 1 were 1 out of 1 samples at leaf node
															else:
																pixels_high.append((10, 12))
																ans = 9																 # approximately 6 were 9 out of 6 samples at leaf node
													else:
														pixels_high.append((22, 5))
														ans = 5														 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													pixels_high.append((8, 11))
													if features[17][5] <= 254.0:
														pixels_low.append((17, 5))
														ans = 1														 # approximately 1 were 1 out of 1 samples at leaf node
													else:
														pixels_high.append((17, 5))
														ans = 9														 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												pixels_high.append((16, 24))
												if features[16][17] <= 73.0:
													pixels_low.append((16, 17))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													pixels_high.append((16, 17))
													ans = 8													 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											pixels_high.append((11, 10))
											if features[14][9] <= 25.0:
												pixels_low.append((14, 9))
												if features[17][16] <= 238.5:
													pixels_low.append((17, 16))
													if features[8][21] <= 252.5:
														pixels_low.append((8, 21))
														ans = 3														 # approximately 3 were 3 out of 3 samples at leaf node
													else:
														pixels_high.append((8, 21))
														if features[12][6] <= 252.5:
															pixels_low.append((12, 6))
															ans = 8															 # approximately 2 were 8 out of 2 samples at leaf node
														else:
															pixels_high.append((12, 6))
															if features[18][10] <= 67.5:
																pixels_low.append((18, 10))
																ans = 5																 # approximately 1 were 5 out of 1 samples at leaf node
															else:
																pixels_high.append((18, 10))
																ans = 9																 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													pixels_high.append((17, 16))
													if features[15][22] <= 50.5:
														pixels_low.append((15, 22))
														ans = 5														 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														pixels_high.append((15, 22))
														ans = 9														 # approximately 11 were 9 out of 11 samples at leaf node
											else:
												pixels_high.append((14, 9))
												if features[21][6] <= 18.0:
													pixels_low.append((21, 6))
													if features[15][12] <= 125.5:
														pixels_low.append((15, 12))
														ans = 5														 # approximately 2 were 5 out of 2 samples at leaf node
													else:
														pixels_high.append((15, 12))
														if features[21][21] <= 254.5:
															pixels_low.append((21, 21))
															ans = 3															 # approximately 24 were 3 out of 24 samples at leaf node
														else:
															pixels_high.append((21, 21))
															ans = 5															 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													pixels_high.append((21, 6))
													if features[8][13] <= 23.5:
														pixels_low.append((8, 13))
														ans = 5														 # approximately 7 were 5 out of 7 samples at leaf node
													else:
														pixels_high.append((8, 13))
														ans = 3														 # approximately 2 were 3 out of 2 samples at leaf node
									else:
										pixels_high.append((7, 14))
										if features[21][10] <= 225.5:
											pixels_low.append((21, 10))
											if features[15][8] <= 140.5:
												pixels_low.append((15, 8))
												if features[6][16] <= 67.0:
													pixels_low.append((6, 16))
													ans = 3													 # approximately 3 were 3 out of 3 samples at leaf node
												else:
													pixels_high.append((6, 16))
													ans = 8													 # approximately 4 were 8 out of 4 samples at leaf node
											else:
												pixels_high.append((15, 8))
												if features[5][13] <= 135.0:
													pixels_low.append((5, 13))
													ans = 5													 # approximately 6 were 5 out of 6 samples at leaf node
												else:
													pixels_high.append((5, 13))
													ans = 9													 # approximately 1 were 9 out of 1 samples at leaf node
										else:
											pixels_high.append((21, 10))
											if features[10][14] <= 242.5:
												pixels_low.append((10, 14))
												ans = 0												 # approximately 7 were 0 out of 7 samples at leaf node
											else:
												pixels_high.append((10, 14))
												ans = 9												 # approximately 1 were 9 out of 1 samples at leaf node
							else:
								pixels_high.append((9, 17))
								if features[7][15] <= 226.0:
									pixels_low.append((7, 15))
									if features[10][16] <= 12.0:
										pixels_low.append((10, 16))
										if features[9][11] <= 186.5:
											pixels_low.append((9, 11))
											ans = 3											 # approximately 4 were 3 out of 4 samples at leaf node
										else:
											pixels_high.append((9, 11))
											if features[8][19] <= 125.5:
												pixels_low.append((8, 19))
												ans = 9												 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												pixels_high.append((8, 19))
												ans = 5												 # approximately 2 were 5 out of 2 samples at leaf node
									else:
										pixels_high.append((10, 16))
										if features[15][13] <= 61.5:
											pixels_low.append((15, 13))
											if features[9][19] <= 252.5:
												pixels_low.append((9, 19))
												if features[20][11] <= 126.5:
													pixels_low.append((20, 11))
													if features[11][12] <= 146.0:
														pixels_low.append((11, 12))
														ans = 2														 # approximately 1 were 2 out of 1 samples at leaf node
													else:
														pixels_high.append((11, 12))
														ans = 5														 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													pixels_high.append((20, 11))
													ans = 8													 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												pixels_high.append((9, 19))
												ans = 0												 # approximately 2 were 0 out of 2 samples at leaf node
										else:
											pixels_high.append((15, 13))
											if features[11][12] <= 3.0:
												pixels_low.append((11, 12))
												if features[11][10] <= 129.5:
													pixels_low.append((11, 10))
													if features[14][13] <= 246.5:
														pixels_low.append((14, 13))
														ans = 2														 # approximately 4 were 2 out of 4 samples at leaf node
													else:
														pixels_high.append((14, 13))
														if features[15][8] <= 9.5:
															pixels_low.append((15, 8))
															ans = 8															 # approximately 1 were 8 out of 1 samples at leaf node
														else:
															pixels_high.append((15, 8))
															ans = 3															 # approximately 2 were 3 out of 2 samples at leaf node
												else:
													pixels_high.append((11, 10))
													ans = 8													 # approximately 11 were 8 out of 11 samples at leaf node
											else:
												pixels_high.append((11, 12))
												if features[14][9] <= 253.5:
													pixels_low.append((14, 9))
													if features[11][18] <= 178.5:
														pixels_low.append((11, 18))
														if features[10][10] <= 21.5:
															pixels_low.append((10, 10))
															if features[13][15] <= 48.0:
																pixels_low.append((13, 15))
																ans = 6																 # approximately 1 were 6 out of 1 samples at leaf node
															else:
																pixels_high.append((13, 15))
																ans = 8																 # approximately 2 were 8 out of 2 samples at leaf node
														else:
															pixels_high.append((10, 10))
															ans = 8															 # approximately 109 were 8 out of 109 samples at leaf node
													else:
														pixels_high.append((11, 18))
														if features[22][19] <= 2.5:
															pixels_low.append((22, 19))
															ans = 8															 # approximately 2 were 8 out of 2 samples at leaf node
														else:
															pixels_high.append((22, 19))
															ans = 3															 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													pixels_high.append((14, 9))
													ans = 0													 # approximately 1 were 0 out of 1 samples at leaf node
								else:
									pixels_high.append((7, 15))
									if features[7][17] <= 210.5:
										pixels_low.append((7, 17))
										if features[21][6] <= 19.0:
											pixels_low.append((21, 6))
											if features[10][7] <= 127.0:
												pixels_low.append((10, 7))
												ans = 4												 # approximately 1 were 4 out of 1 samples at leaf node
											else:
												pixels_high.append((10, 7))
												ans = 6												 # approximately 1 were 6 out of 1 samples at leaf node
										else:
											pixels_high.append((21, 6))
											if features[8][21] <= 126.5:
												pixels_low.append((8, 21))
												ans = 9												 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												pixels_high.append((8, 21))
												ans = 3												 # approximately 1 were 3 out of 1 samples at leaf node
									else:
										pixels_high.append((7, 17))
										ans = 0										 # approximately 6 were 0 out of 6 samples at leaf node
			else:
				pixels_high.append((12, 17))
				if features[12][13] <= 0.5:
					pixels_low.append((12, 13))
					if features[10][5] <= 56.0:
						pixels_low.append((10, 5))
						if features[13][11] <= 169.0:
							pixels_low.append((13, 11))
							if features[9][13] <= 2.0:
								pixels_low.append((9, 13))
								if features[14][11] <= 38.0:
									pixels_low.append((14, 11))
									if features[10][19] <= 3.0:
										pixels_low.append((10, 19))
										if features[14][14] <= 239.0:
											pixels_low.append((14, 14))
											if features[7][12] <= 234.5:
												pixels_low.append((7, 12))
												if features[19][10] <= 242.0:
													pixels_low.append((19, 10))
													if features[18][6] <= 5.0:
														pixels_low.append((18, 6))
														if features[9][14] <= 57.0:
															pixels_low.append((9, 14))
															ans = 7															 # approximately 2 were 7 out of 2 samples at leaf node
														else:
															pixels_high.append((9, 14))
															ans = 4															 # approximately 1 were 4 out of 1 samples at leaf node
													else:
														pixels_high.append((18, 6))
														ans = 2														 # approximately 11 were 2 out of 11 samples at leaf node
												else:
													pixels_high.append((19, 10))
													if features[20][20] <= 126.5:
														pixels_low.append((20, 20))
														ans = 3														 # approximately 2 were 3 out of 2 samples at leaf node
													else:
														pixels_high.append((20, 20))
														ans = 8														 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												pixels_high.append((7, 12))
												ans = 9												 # approximately 5 were 9 out of 5 samples at leaf node
										else:
											pixels_high.append((14, 14))
											if features[12][16] <= 158.0:
												pixels_low.append((12, 16))
												if features[12][8] <= 16.0:
													pixels_low.append((12, 8))
													ans = 8													 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													pixels_high.append((12, 8))
													ans = 7													 # approximately 1 were 7 out of 1 samples at leaf node
											else:
												pixels_high.append((12, 16))
												ans = 3												 # approximately 20 were 3 out of 20 samples at leaf node
									else:
										pixels_high.append((10, 19))
										if features[11][12] <= 9.5:
											pixels_low.append((11, 12))
											if features[19][17] <= 22.0:
												pixels_low.append((19, 17))
												if features[20][12] <= 253.5:
													pixels_low.append((20, 12))
													ans = 2													 # approximately 78 were 2 out of 78 samples at leaf node
												else:
													pixels_high.append((20, 12))
													ans = 3													 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												pixels_high.append((19, 17))
												if features[12][20] <= 34.0:
													pixels_low.append((12, 20))
													if features[13][15] <= 36.5:
														pixels_low.append((13, 15))
														if features[17][18] <= 168.0:
															pixels_low.append((17, 18))
															ans = 7															 # approximately 2 were 7 out of 2 samples at leaf node
														else:
															pixels_high.append((17, 18))
															ans = 9															 # approximately 1 were 9 out of 1 samples at leaf node
													else:
														pixels_high.append((13, 15))
														ans = 3														 # approximately 4 were 3 out of 4 samples at leaf node
												else:
													pixels_high.append((12, 20))
													ans = 2													 # approximately 11 were 2 out of 11 samples at leaf node
										else:
											pixels_high.append((11, 12))
											if features[19][18] <= 243.0:
												pixels_low.append((19, 18))
												ans = 8												 # approximately 5 were 8 out of 5 samples at leaf node
											else:
												pixels_high.append((19, 18))
												ans = 6												 # approximately 1 were 6 out of 1 samples at leaf node
								else:
									pixels_high.append((14, 11))
									if features[16][8] <= 93.0:
										pixels_low.append((16, 8))
										if features[12][16] <= 59.0:
											pixels_low.append((12, 16))
											if features[14][23] <= 244.5:
												pixels_low.append((14, 23))
												ans = 1												 # approximately 1 were 1 out of 1 samples at leaf node
											else:
												pixels_high.append((14, 23))
												ans = 3												 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											pixels_high.append((12, 16))
											ans = 8											 # approximately 22 were 8 out of 22 samples at leaf node
									else:
										pixels_high.append((16, 8))
										if features[12][6] <= 30.5:
											pixels_low.append((12, 6))
											if features[13][18] <= 191.5:
												pixels_low.append((13, 18))
												if features[9][15] <= 2.5:
													pixels_low.append((9, 15))
													ans = 4													 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													pixels_high.append((9, 15))
													if features[12][10] <= 82.0:
														pixels_low.append((12, 10))
														ans = 8														 # approximately 1 were 8 out of 1 samples at leaf node
													else:
														pixels_high.append((12, 10))
														ans = 2														 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												pixels_high.append((13, 18))
												ans = 1												 # approximately 31 were 1 out of 31 samples at leaf node
										else:
											pixels_high.append((12, 6))
											if features[18][20] <= 7.0:
												pixels_low.append((18, 20))
												ans = 7												 # approximately 4 were 7 out of 4 samples at leaf node
											else:
												pixels_high.append((18, 20))
												if features[13][21] <= 101.0:
													pixels_low.append((13, 21))
													ans = 3													 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													pixels_high.append((13, 21))
													ans = 2													 # approximately 2 were 2 out of 2 samples at leaf node
							else:
								pixels_high.append((9, 13))
								if features[9][16] <= 31.0:
									pixels_low.append((9, 16))
									if features[11][15] <= 22.5:
										pixels_low.append((11, 15))
										if features[12][16] <= 76.0:
											pixels_low.append((12, 16))
											if features[12][7] <= 226.5:
												pixels_low.append((12, 7))
												if features[15][6] <= 253.5:
													pixels_low.append((15, 6))
													if features[15][22] <= 95.5:
														pixels_low.append((15, 22))
														ans = 1														 # approximately 1 were 1 out of 1 samples at leaf node
													else:
														pixels_high.append((15, 22))
														ans = 6														 # approximately 1 were 6 out of 1 samples at leaf node
												else:
													pixels_high.append((15, 6))
													ans = 7													 # approximately 2 were 7 out of 2 samples at leaf node
											else:
												pixels_high.append((12, 7))
												ans = 2												 # approximately 4 were 2 out of 4 samples at leaf node
										else:
											pixels_high.append((12, 16))
											if features[17][16] <= 231.5:
												pixels_low.append((17, 16))
												if features[8][15] <= 19.0:
													pixels_low.append((8, 15))
													ans = 3													 # approximately 3 were 3 out of 3 samples at leaf node
												else:
													pixels_high.append((8, 15))
													if features[20][8] <= 243.5:
														pixels_low.append((20, 8))
														ans = 8														 # approximately 1 were 8 out of 1 samples at leaf node
													else:
														pixels_high.append((20, 8))
														ans = 0														 # approximately 1 were 0 out of 1 samples at leaf node
											else:
												pixels_high.append((17, 16))
												ans = 9												 # approximately 2 were 9 out of 2 samples at leaf node
									else:
										pixels_high.append((11, 15))
										if features[6][14] <= 158.0:
											pixels_low.append((6, 14))
											if features[12][18] <= 52.5:
												pixels_low.append((12, 18))
												if features[10][19] <= 86.5:
													pixels_low.append((10, 19))
													if features[10][16] <= 128.5:
														pixels_low.append((10, 16))
														ans = 3														 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														pixels_high.append((10, 16))
														if features[10][6] <= 118.0:
															pixels_low.append((10, 6))
															if features[16][16] <= 162.5:
																pixels_low.append((16, 16))
																ans = 4																 # approximately 1 were 4 out of 1 samples at leaf node
															else:
																pixels_high.append((16, 16))
																ans = 9																 # approximately 1 were 9 out of 1 samples at leaf node
														else:
															pixels_high.append((10, 6))
															ans = 5															 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													pixels_high.append((10, 19))
													ans = 8													 # approximately 4 were 8 out of 4 samples at leaf node
											else:
												pixels_high.append((12, 18))
												ans = 8												 # approximately 57 were 8 out of 57 samples at leaf node
										else:
											pixels_high.append((6, 14))
											if features[22][10] <= 233.0:
												pixels_low.append((22, 10))
												ans = 4												 # approximately 2 were 4 out of 2 samples at leaf node
											else:
												pixels_high.append((22, 10))
												ans = 0												 # approximately 1 were 0 out of 1 samples at leaf node
								else:
									pixels_high.append((9, 16))
									if features[17][6] <= 51.0:
										pixels_low.append((17, 6))
										if features[16][9] <= 232.0:
											pixels_low.append((16, 9))
											ans = 4											 # approximately 27 were 4 out of 27 samples at leaf node
										else:
											pixels_high.append((16, 9))
											ans = 9											 # approximately 1 were 9 out of 1 samples at leaf node
									else:
										pixels_high.append((17, 6))
										if features[18][12] <= 65.5:
											pixels_low.append((18, 12))
											if features[17][4] <= 4.0:
												pixels_low.append((17, 4))
												if features[12][7] <= 73.5:
													pixels_low.append((12, 7))
													ans = 4													 # approximately 6 were 4 out of 6 samples at leaf node
												else:
													pixels_high.append((12, 7))
													if features[19][20] <= 43.5:
														pixels_low.append((19, 20))
														if features[19][19] <= 32.0:
															pixels_low.append((19, 19))
															ans = 8															 # approximately 5 were 8 out of 5 samples at leaf node
														else:
															pixels_high.append((19, 19))
															if features[15][17] <= 126.5:
																pixels_low.append((15, 17))
																ans = 5																 # approximately 1 were 5 out of 1 samples at leaf node
															else:
																pixels_high.append((15, 17))
																ans = 2																 # approximately 1 were 2 out of 1 samples at leaf node
													else:
														pixels_high.append((19, 20))
														ans = 5														 # approximately 8 were 5 out of 8 samples at leaf node
											else:
												pixels_high.append((17, 4))
												if features[16][22] <= 111.5:
													pixels_low.append((16, 22))
													if features[18][4] <= 7.0:
														pixels_low.append((18, 4))
														ans = 4														 # approximately 1 were 4 out of 1 samples at leaf node
													else:
														pixels_high.append((18, 4))
														if features[20][10] <= 239.5:
															pixels_low.append((20, 10))
															ans = 9															 # approximately 1 were 9 out of 1 samples at leaf node
														else:
															pixels_high.append((20, 10))
															ans = 0															 # approximately 1 were 0 out of 1 samples at leaf node
												else:
													pixels_high.append((16, 22))
													ans = 6													 # approximately 12 were 6 out of 12 samples at leaf node
										else:
											pixels_high.append((18, 12))
											if features[17][15] <= 251.5:
												pixels_low.append((17, 15))
												if features[8][16] <= 107.5:
													pixels_low.append((8, 16))
													if features[11][12] <= 155.0:
														pixels_low.append((11, 12))
														ans = 8														 # approximately 15 were 8 out of 15 samples at leaf node
													else:
														pixels_high.append((11, 12))
														if features[13][14] <= 126.0:
															pixels_low.append((13, 14))
															ans = 9															 # approximately 1 were 9 out of 1 samples at leaf node
														else:
															pixels_high.append((13, 14))
															ans = 5															 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													pixels_high.append((8, 16))
													if features[12][24] <= 35.0:
														pixels_low.append((12, 24))
														if features[14][14] <= 126.5:
															pixels_low.append((14, 14))
															if features[19][21] <= 45.5:
																pixels_low.append((19, 21))
																ans = 4																 # approximately 1 were 4 out of 1 samples at leaf node
															else:
																pixels_high.append((19, 21))
																ans = 0																 # approximately 2 were 0 out of 2 samples at leaf node
														else:
															pixels_high.append((14, 14))
															ans = 6															 # approximately 2 were 6 out of 2 samples at leaf node
													else:
														pixels_high.append((12, 24))
														ans = 9														 # approximately 5 were 9 out of 5 samples at leaf node
											else:
												pixels_high.append((17, 15))
												if features[17][23] <= 247.5:
													pixels_low.append((17, 23))
													if features[9][7] <= 207.0:
														pixels_low.append((9, 7))
														if features[9][21] <= 185.5:
															pixels_low.append((9, 21))
															ans = 9															 # approximately 32 were 9 out of 32 samples at leaf node
														else:
															pixels_high.append((9, 21))
															ans = 0															 # approximately 1 were 0 out of 1 samples at leaf node
													else:
														pixels_high.append((9, 7))
														ans = 4														 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													pixels_high.append((17, 23))
													ans = 8													 # approximately 2 were 8 out of 2 samples at leaf node
						else:
							pixels_high.append((13, 11))
							if features[13][16] <= 2.5:
								pixels_low.append((13, 16))
								if features[15][23] <= 44.5:
									pixels_low.append((15, 23))
									ans = 5									 # approximately 2 were 5 out of 2 samples at leaf node
								else:
									pixels_high.append((15, 23))
									ans = 0									 # approximately 3 were 0 out of 3 samples at leaf node
							else:
								pixels_high.append((13, 16))
								if features[15][9] <= 247.5:
									pixels_low.append((15, 9))
									ans = 8									 # approximately 75 were 8 out of 75 samples at leaf node
								else:
									pixels_high.append((15, 9))
									if features[13][15] <= 40.5:
										pixels_low.append((13, 15))
										ans = 2										 # approximately 2 were 2 out of 2 samples at leaf node
									else:
										pixels_high.append((13, 15))
										if features[22][14] <= 24.0:
											pixels_low.append((22, 14))
											ans = 8											 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											pixels_high.append((22, 14))
											ans = 3											 # approximately 1 were 3 out of 1 samples at leaf node
					else:
						pixels_high.append((10, 5))
						if features[13][11] <= 155.0:
							pixels_low.append((13, 11))
							if features[9][13] <= 31.5:
								pixels_low.append((9, 13))
								if features[10][19] <= 2.0:
									pixels_low.append((10, 19))
									if features[10][24] <= 0.5:
										pixels_low.append((10, 24))
										if features[6][13] <= 53.5:
											pixels_low.append((6, 13))
											if features[13][23] <= 247.5:
												pixels_low.append((13, 23))
												if features[17][9] <= 253.5:
													pixels_low.append((17, 9))
													ans = 2													 # approximately 27 were 2 out of 27 samples at leaf node
												else:
													pixels_high.append((17, 9))
													ans = 3													 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												pixels_high.append((13, 23))
												if features[11][19] <= 5.0:
													pixels_low.append((11, 19))
													if features[7][7] <= 14.5:
														pixels_low.append((7, 7))
														if features[17][10] <= 126.0:
															pixels_low.append((17, 10))
															ans = 5															 # approximately 1 were 5 out of 1 samples at leaf node
														else:
															pixels_high.append((17, 10))
															ans = 7															 # approximately 1 were 7 out of 1 samples at leaf node
													else:
														pixels_high.append((7, 7))
														ans = 3														 # approximately 4 were 3 out of 4 samples at leaf node
												else:
													pixels_high.append((11, 19))
													ans = 2													 # approximately 5 were 2 out of 5 samples at leaf node
										else:
											pixels_high.append((6, 13))
											ans = 9											 # approximately 2 were 9 out of 2 samples at leaf node
									else:
										pixels_high.append((10, 24))
										if features[13][19] <= 252.0:
											pixels_low.append((13, 19))
											ans = 3											 # approximately 13 were 3 out of 13 samples at leaf node
										else:
											pixels_high.append((13, 19))
											if features[16][17] <= 129.5:
												pixels_low.append((16, 17))
												ans = 2												 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												pixels_high.append((16, 17))
												ans = 7												 # approximately 1 were 7 out of 1 samples at leaf node
								else:
									pixels_high.append((10, 19))
									if features[6][14] <= 126.5:
										pixels_low.append((6, 14))
										if features[14][10] <= 253.5:
											pixels_low.append((14, 10))
											if features[13][11] <= 152.0:
												pixels_low.append((13, 11))
												if features[18][15] <= 254.5:
													pixels_low.append((18, 15))
													if features[6][24] <= 67.5:
														pixels_low.append((6, 24))
														ans = 2														 # approximately 212 were 2 out of 212 samples at leaf node
													else:
														pixels_high.append((6, 24))
														ans = 7														 # approximately 1 were 7 out of 1 samples at leaf node
												else:
													pixels_high.append((18, 15))
													ans = 3													 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												pixels_high.append((13, 11))
												ans = 5												 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											pixels_high.append((14, 10))
											if features[14][22] <= 254.0:
												pixels_low.append((14, 22))
												ans = 7												 # approximately 1 were 7 out of 1 samples at leaf node
											else:
												pixels_high.append((14, 22))
												ans = 8												 # approximately 1 were 8 out of 1 samples at leaf node
									else:
										pixels_high.append((6, 14))
										if features[8][21] <= 91.0:
											pixels_low.append((8, 21))
											ans = 6											 # approximately 1 were 6 out of 1 samples at leaf node
										else:
											pixels_high.append((8, 21))
											ans = 0											 # approximately 1 were 0 out of 1 samples at leaf node
							else:
								pixels_high.append((9, 13))
								if features[18][19] <= 172.0:
									pixels_low.append((18, 19))
									if features[18][5] <= 190.5:
										pixels_low.append((18, 5))
										ans = 8										 # approximately 10 were 8 out of 10 samples at leaf node
									else:
										pixels_high.append((18, 5))
										ans = 5										 # approximately 1 were 5 out of 1 samples at leaf node
								else:
									pixels_high.append((18, 19))
									if features[18][14] <= 237.0:
										pixels_low.append((18, 14))
										if features[10][5] <= 253.0:
											pixels_low.append((10, 5))
											if features[19][9] <= 128.5:
												pixels_low.append((19, 9))
												ans = 3												 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												pixels_high.append((19, 9))
												ans = 2												 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											pixels_high.append((10, 5))
											ans = 5											 # approximately 2 were 5 out of 2 samples at leaf node
									else:
										pixels_high.append((18, 14))
										ans = 0										 # approximately 3 were 0 out of 3 samples at leaf node
						else:
							pixels_high.append((13, 11))
							if features[14][15] <= 2.5:
								pixels_low.append((14, 15))
								if features[15][6] <= 181.0:
									pixels_low.append((15, 6))
									ans = 3									 # approximately 1 were 3 out of 1 samples at leaf node
								else:
									pixels_high.append((15, 6))
									ans = 0									 # approximately 1 were 0 out of 1 samples at leaf node
							else:
								pixels_high.append((14, 15))
								ans = 8								 # approximately 17 were 8 out of 17 samples at leaf node
				else:
					pixels_high.append((12, 13))
					if features[15][10] <= 248.5:
						pixels_low.append((15, 10))
						if features[14][15] <= 15.5:
							pixels_low.append((14, 15))
							if features[15][13] <= 14.5:
								pixels_low.append((15, 13))
								if features[11][21] <= 135.5:
									pixels_low.append((11, 21))
									if features[12][20] <= 96.5:
										pixels_low.append((12, 20))
										ans = 4										 # approximately 6 were 4 out of 6 samples at leaf node
									else:
										pixels_high.append((12, 20))
										if features[13][8] <= 69.5:
											pixels_low.append((13, 8))
											ans = 8											 # approximately 3 were 8 out of 3 samples at leaf node
										else:
											pixels_high.append((13, 8))
											if features[9][17] <= 12.5:
												pixels_low.append((9, 17))
												ans = 0												 # approximately 1 were 0 out of 1 samples at leaf node
											else:
												pixels_high.append((9, 17))
												ans = 6												 # approximately 2 were 6 out of 2 samples at leaf node
								else:
									pixels_high.append((11, 21))
									if features[10][16] <= 20.0:
										pixels_low.append((10, 16))
										if features[19][18] <= 42.5:
											pixels_low.append((19, 18))
											ans = 8											 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											pixels_high.append((19, 18))
											ans = 2											 # approximately 1 were 2 out of 1 samples at leaf node
									else:
										pixels_high.append((10, 16))
										if features[16][12] <= 227.5:
											pixels_low.append((16, 12))
											ans = 0											 # approximately 52 were 0 out of 52 samples at leaf node
										else:
											pixels_high.append((16, 12))
											ans = 6											 # approximately 1 were 6 out of 1 samples at leaf node
							else:
								pixels_high.append((15, 13))
								if features[11][12] <= 129.5:
									pixels_low.append((11, 12))
									if features[7][22] <= 160.0:
										pixels_low.append((7, 22))
										ans = 8										 # approximately 20 were 8 out of 20 samples at leaf node
									else:
										pixels_high.append((7, 22))
										if features[11][15] <= 127.0:
											pixels_low.append((11, 15))
											ans = 3											 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											pixels_high.append((11, 15))
											ans = 5											 # approximately 1 were 5 out of 1 samples at leaf node
								else:
									pixels_high.append((11, 12))
									if features[10][16] <= 190.5:
										pixels_low.append((10, 16))
										if features[14][14] <= 152.0:
											pixels_low.append((14, 14))
											if features[18][10] <= 49.0:
												pixels_low.append((18, 10))
												if features[14][13] <= 32.0:
													pixels_low.append((14, 13))
													ans = 3													 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													pixels_high.append((14, 13))
													ans = 5													 # approximately 18 were 5 out of 18 samples at leaf node
											else:
												pixels_high.append((18, 10))
												if features[5][20] <= 217.0:
													pixels_low.append((5, 20))
													ans = 3													 # approximately 7 were 3 out of 7 samples at leaf node
												else:
													pixels_high.append((5, 20))
													ans = 4													 # approximately 1 were 4 out of 1 samples at leaf node
										else:
											pixels_high.append((14, 14))
											ans = 8											 # approximately 7 were 8 out of 7 samples at leaf node
									else:
										pixels_high.append((10, 16))
										if features[9][21] <= 7.5:
											pixels_low.append((9, 21))
											if features[13][24] <= 2.5:
												pixels_low.append((13, 24))
												ans = 6												 # approximately 11 were 6 out of 11 samples at leaf node
											else:
												pixels_high.append((13, 24))
												ans = 4												 # approximately 1 were 4 out of 1 samples at leaf node
										else:
											pixels_high.append((9, 21))
											if features[14][12] <= 194.5:
												pixels_low.append((14, 12))
												ans = 0												 # approximately 4 were 0 out of 4 samples at leaf node
											else:
												pixels_high.append((14, 12))
												if features[11][23] <= 146.5:
													pixels_low.append((11, 23))
													ans = 8													 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													pixels_high.append((11, 23))
													ans = 5													 # approximately 1 were 5 out of 1 samples at leaf node
						else:
							pixels_high.append((14, 15))
							if features[11][18] <= 0.5:
								pixels_low.append((11, 18))
								if features[11][11] <= 32.5:
									pixels_low.append((11, 11))
									if features[9][12] <= 4.5:
										pixels_low.append((9, 12))
										if features[7][17] <= 42.5:
											pixels_low.append((7, 17))
											if features[13][14] <= 159.5:
												pixels_low.append((13, 14))
												ans = 8												 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												pixels_high.append((13, 14))
												ans = 3												 # approximately 60 were 3 out of 60 samples at leaf node
										else:
											pixels_high.append((7, 17))
											if features[18][9] <= 36.5:
												pixels_low.append((18, 9))
												ans = 8												 # approximately 5 were 8 out of 5 samples at leaf node
											else:
												pixels_high.append((18, 9))
												if features[9][19] <= 74.0:
													pixels_low.append((9, 19))
													ans = 3													 # approximately 3 were 3 out of 3 samples at leaf node
												else:
													pixels_high.append((9, 19))
													ans = 2													 # approximately 3 were 2 out of 3 samples at leaf node
									else:
										pixels_high.append((9, 12))
										if features[15][20] <= 110.0:
											pixels_low.append((15, 20))
											if features[11][12] <= 222.5:
												pixels_low.append((11, 12))
												if features[10][10] <= 250.5:
													pixels_low.append((10, 10))
													ans = 8													 # approximately 18 were 8 out of 18 samples at leaf node
												else:
													pixels_high.append((10, 10))
													ans = 4													 # approximately 1 were 4 out of 1 samples at leaf node
											else:
												pixels_high.append((11, 12))
												ans = 3												 # approximately 2 were 3 out of 2 samples at leaf node
										else:
											pixels_high.append((15, 20))
											if features[15][20] <= 251.5:
												pixels_low.append((15, 20))
												ans = 5												 # approximately 2 were 5 out of 2 samples at leaf node
											else:
												pixels_high.append((15, 20))
												if features[12][20] <= 80.0:
													pixels_low.append((12, 20))
													if features[10][6] <= 125.0:
														pixels_low.append((10, 6))
														ans = 4														 # approximately 1 were 4 out of 1 samples at leaf node
													else:
														pixels_high.append((10, 6))
														if features[8][23] <= 240.0:
															pixels_low.append((8, 23))
															ans = 9															 # approximately 1 were 9 out of 1 samples at leaf node
														else:
															pixels_high.append((8, 23))
															ans = 2															 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													pixels_high.append((12, 20))
													ans = 3													 # approximately 2 were 3 out of 2 samples at leaf node
								else:
									pixels_high.append((11, 11))
									if features[10][14] <= 241.5:
										pixels_low.append((10, 14))
										if features[17][15] <= 253.5:
											pixels_low.append((17, 15))
											if features[19][16] <= 245.0:
												pixels_low.append((19, 16))
												ans = 8												 # approximately 63 were 8 out of 63 samples at leaf node
											else:
												pixels_high.append((19, 16))
												if features[18][16] <= 240.0:
													pixels_low.append((18, 16))
													if features[15][11] <= 25.5:
														pixels_low.append((15, 11))
														ans = 5														 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														pixels_high.append((15, 11))
														ans = 3														 # approximately 2 were 3 out of 2 samples at leaf node
												else:
													pixels_high.append((18, 16))
													ans = 8													 # approximately 2 were 8 out of 2 samples at leaf node
										else:
											pixels_high.append((17, 15))
											if features[13][17] <= 93.5:
												pixels_low.append((13, 17))
												ans = 5												 # approximately 3 were 5 out of 3 samples at leaf node
											else:
												pixels_high.append((13, 17))
												if features[14][17] <= 230.5:
													pixels_low.append((14, 17))
													if features[16][22] <= 91.5:
														pixels_low.append((16, 22))
														ans = 2														 # approximately 1 were 2 out of 1 samples at leaf node
													else:
														pixels_high.append((16, 22))
														if features[14][5] <= 225.5:
															pixels_low.append((14, 5))
															ans = 9															 # approximately 1 were 9 out of 1 samples at leaf node
														else:
															pixels_high.append((14, 5))
															ans = 8															 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													pixels_high.append((14, 17))
													ans = 4													 # approximately 2 were 4 out of 2 samples at leaf node
									else:
										pixels_high.append((10, 14))
										if features[19][11] <= 3.0:
											pixels_low.append((19, 11))
											if features[12][23] <= 26.5:
												pixels_low.append((12, 23))
												if features[15][12] <= 59.0:
													pixels_low.append((15, 12))
													if features[10][17] <= 233.0:
														pixels_low.append((10, 17))
														ans = 3														 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														pixels_high.append((10, 17))
														ans = 4														 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													pixels_high.append((15, 12))
													if features[14][11] <= 4.5:
														pixels_low.append((14, 11))
														ans = 8														 # approximately 1 were 8 out of 1 samples at leaf node
													else:
														pixels_high.append((14, 11))
														ans = 9														 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												pixels_high.append((12, 23))
												ans = 5												 # approximately 14 were 5 out of 14 samples at leaf node
										else:
											pixels_high.append((19, 11))
											if features[18][6] <= 88.5:
												pixels_low.append((18, 6))
												if features[13][21] <= 253.5:
													pixels_low.append((13, 21))
													ans = 4													 # approximately 11 were 4 out of 11 samples at leaf node
												else:
													pixels_high.append((13, 21))
													ans = 9													 # approximately 2 were 9 out of 2 samples at leaf node
											else:
												pixels_high.append((18, 6))
												if features[17][17] <= 244.5:
													pixels_low.append((17, 17))
													if features[5][23] <= 43.5:
														pixels_low.append((5, 23))
														ans = 8														 # approximately 12 were 8 out of 12 samples at leaf node
													else:
														pixels_high.append((5, 23))
														ans = 3														 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													pixels_high.append((17, 17))
													if features[5][7] <= 79.0:
														pixels_low.append((5, 7))
														ans = 9														 # approximately 2 were 9 out of 2 samples at leaf node
													else:
														pixels_high.append((5, 7))
														ans = 3														 # approximately 1 were 3 out of 1 samples at leaf node
							else:
								pixels_high.append((11, 18))
								if features[10][15] <= 182.5:
									pixels_low.append((10, 15))
									if features[7][16] <= 150.0:
										pixels_low.append((7, 16))
										if features[9][5] <= 178.0:
											pixels_low.append((9, 5))
											if features[4][14] <= 59.5:
												pixels_low.append((4, 14))
												if features[6][5] <= 19.0:
													pixels_low.append((6, 5))
													if features[23][21] <= 236.0:
														pixels_low.append((23, 21))
														if features[7][15] <= 131.5:
															pixels_low.append((7, 15))
															if features[3][10] <= 124.5:
																pixels_low.append((3, 10))
																if features[12][12] <= 6.5:
																	pixels_low.append((12, 12))
																	if features[10][13] <= 18.5:
																		pixels_low.append((10, 13))
																		if features[10][6] <= 40.0:
																			pixels_low.append((10, 6))
																			ans = 8																			 # approximately 11 were 8 out of 11 samples at leaf node
																		else:
																			pixels_high.append((10, 6))
																			if features[13][4] <= 3.5:
																				pixels_low.append((13, 4))
																				ans = 3																				 # approximately 6 were 3 out of 6 samples at leaf node
																			else:
																				pixels_high.append((13, 4))
																				ans = 2																				 # approximately 4 were 2 out of 4 samples at leaf node
																	else:
																		pixels_high.append((10, 13))
																		if features[12][15] <= 19.0:
																			pixels_low.append((12, 15))
																			ans = 5																			 # approximately 1 were 5 out of 1 samples at leaf node
																		else:
																			pixels_high.append((12, 15))
																			ans = 8																			 # approximately 100 were 8 out of 100 samples at leaf node
																else:
																	pixels_high.append((12, 12))
																	if features[4][20] <= 96.5:
																		pixels_low.append((4, 20))
																		if features[11][4] <= 218.0:
																			pixels_low.append((11, 4))
																			if features[18][4] <= 254.5:
																				pixels_low.append((18, 4))
																				if features[15][9] <= 253.5:
																					pixels_low.append((15, 9))
																					if features[12][17] <= 38.5:
																						pixels_low.append((12, 17))
																						if features[14][23] <= 6.0:
																							pixels_low.append((14, 23))
																							ans = 4																							 # approximately 1 were 4 out of 1 samples at leaf node
																						else:
																							pixels_high.append((14, 23))
																							if features[17][4] <= 119.0:
																								pixels_low.append((17, 4))
																								ans = 8																								 # approximately 25 were 8 out of 25 samples at leaf node
																							else:
																								pixels_high.append((17, 4))
																								ans = 6																								 # approximately 1 were 6 out of 1 samples at leaf node
																					else:
																						pixels_high.append((12, 17))
																						if features[19][17] <= 253.5:
																							pixels_low.append((19, 17))
																							if features[16][8] <= 253.5:
																								pixels_low.append((16, 8))
																								ans = 8																								 # approximately 946 were 8 out of 946 samples at leaf node
																							else:
																								pixels_high.append((16, 8))
																								if features[12][14] <= 5.0:
																									pixels_low.append((12, 14))
																									ans = 2																									 # approximately 1 were 2 out of 1 samples at leaf node
																								else:
																									pixels_high.append((12, 14))
																									ans = 8																									 # approximately 16 were 8 out of 16 samples at leaf node
																						else:
																							pixels_high.append((19, 17))
																							if features[7][20] <= 166.5:
																								pixels_low.append((7, 20))
																								ans = 8																								 # approximately 17 were 8 out of 17 samples at leaf node
																							else:
																								pixels_high.append((7, 20))
																								ans = 5																								 # approximately 1 were 5 out of 1 samples at leaf node
																				else:
																					pixels_high.append((15, 9))
																					if features[13][7] <= 137.5:
																						pixels_low.append((13, 7))
																						ans = 6																						 # approximately 1 were 6 out of 1 samples at leaf node
																					else:
																						pixels_high.append((13, 7))
																						ans = 8																						 # approximately 6 were 8 out of 6 samples at leaf node
																			else:
																				pixels_high.append((18, 4))
																				if features[16][13] <= 15.0:
																					pixels_low.append((16, 13))
																					ans = 6																					 # approximately 2 were 6 out of 2 samples at leaf node
																				else:
																					pixels_high.append((16, 13))
																					ans = 8																					 # approximately 10 were 8 out of 10 samples at leaf node
																		else:
																			pixels_high.append((11, 4))
																			if features[17][7] <= 103.0:
																				pixels_low.append((17, 7))
																				ans = 5																				 # approximately 1 were 5 out of 1 samples at leaf node
																			else:
																				pixels_high.append((17, 7))
																				ans = 8																				 # approximately 2 were 8 out of 2 samples at leaf node
																	else:
																		pixels_high.append((4, 20))
																		if features[5][17] <= 1.5:
																			pixels_low.append((5, 17))
																			ans = 3																			 # approximately 1 were 3 out of 1 samples at leaf node
																		else:
																			pixels_high.append((5, 17))
																			ans = 8																			 # approximately 1 were 8 out of 1 samples at leaf node
															else:
																pixels_high.append((3, 10))
																ans = 3																 # approximately 1 were 3 out of 1 samples at leaf node
														else:
															pixels_high.append((7, 15))
															ans = 3															 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														pixels_high.append((23, 21))
														ans = 2														 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													pixels_high.append((6, 5))
													ans = 2													 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												pixels_high.append((4, 14))
												ans = 0												 # approximately 1 were 0 out of 1 samples at leaf node
										else:
											pixels_high.append((9, 5))
											if features[11][12] <= 9.5:
												pixels_low.append((11, 12))
												if features[8][19] <= 163.5:
													pixels_low.append((8, 19))
													if features[12][5] <= 253.5:
														pixels_low.append((12, 5))
														ans = 3														 # approximately 4 were 3 out of 4 samples at leaf node
													else:
														pixels_high.append((12, 5))
														ans = 8														 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													pixels_high.append((8, 19))
													ans = 2													 # approximately 6 were 2 out of 6 samples at leaf node
											else:
												pixels_high.append((11, 12))
												if features[17][4] <= 45.5:
													pixels_low.append((17, 4))
													ans = 8													 # approximately 13 were 8 out of 13 samples at leaf node
												else:
													pixels_high.append((17, 4))
													ans = 5													 # approximately 2 were 5 out of 2 samples at leaf node
									else:
										pixels_high.append((7, 16))
										if features[14][15] <= 246.0:
											pixels_low.append((14, 15))
											if features[19][10] <= 7.5:
												pixels_low.append((19, 10))
												ans = 5												 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												pixels_high.append((19, 10))
												if features[20][8] <= 229.0:
													pixels_low.append((20, 8))
													ans = 9													 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													pixels_high.append((20, 8))
													if features[11][17] <= 184.5:
														pixels_low.append((11, 17))
														ans = 3														 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														pixels_high.append((11, 17))
														ans = 0														 # approximately 1 were 0 out of 1 samples at leaf node
										else:
											pixels_high.append((14, 15))
											ans = 4											 # approximately 3 were 4 out of 3 samples at leaf node
								else:
									pixels_high.append((10, 15))
									if features[9][19] <= 56.5:
										pixels_low.append((9, 19))
										if features[12][17] <= 239.0:
											pixels_low.append((12, 17))
											if features[14][17] <= 187.0:
												pixels_low.append((14, 17))
												if features[16][12] <= 231.5:
													pixels_low.append((16, 12))
													if features[11][18] <= 249.5:
														pixels_low.append((11, 18))
														if features[19][11] <= 112.5:
															pixels_low.append((19, 11))
															ans = 5															 # approximately 7 were 5 out of 7 samples at leaf node
														else:
															pixels_high.append((19, 11))
															if features[17][18] <= 248.5:
																pixels_low.append((17, 18))
																if features[10][8] <= 187.5:
																	pixels_low.append((10, 8))
																	ans = 3																	 # approximately 1 were 3 out of 1 samples at leaf node
																else:
																	pixels_high.append((10, 8))
																	ans = 8																	 # approximately 2 were 8 out of 2 samples at leaf node
															else:
																pixels_high.append((17, 18))
																ans = 2																 # approximately 2 were 2 out of 2 samples at leaf node
													else:
														pixels_high.append((11, 18))
														ans = 6														 # approximately 6 were 6 out of 6 samples at leaf node
												else:
													pixels_high.append((16, 12))
													ans = 3													 # approximately 7 were 3 out of 7 samples at leaf node
											else:
												pixels_high.append((14, 17))
												if features[13][10] <= 103.5:
													pixels_low.append((13, 10))
													if features[9][23] <= 23.5:
														pixels_low.append((9, 23))
														if features[19][14] <= 52.0:
															pixels_low.append((19, 14))
															ans = 9															 # approximately 1 were 9 out of 1 samples at leaf node
														else:
															pixels_high.append((19, 14))
															ans = 6															 # approximately 1 were 6 out of 1 samples at leaf node
													else:
														pixels_high.append((9, 23))
														ans = 7														 # approximately 1 were 7 out of 1 samples at leaf node
												else:
													pixels_high.append((13, 10))
													ans = 4													 # approximately 8 were 4 out of 8 samples at leaf node
										else:
											pixels_high.append((12, 17))
											if features[13][10] <= 235.5:
												pixels_low.append((13, 10))
												if features[11][19] <= 1.5:
													pixels_low.append((11, 19))
													if features[13][17] <= 216.5:
														pixels_low.append((13, 17))
														ans = 3														 # approximately 2 were 3 out of 2 samples at leaf node
													else:
														pixels_high.append((13, 17))
														ans = 9														 # approximately 2 were 9 out of 2 samples at leaf node
												else:
													pixels_high.append((11, 19))
													if features[13][23] <= 19.0:
														pixels_low.append((13, 23))
														ans = 3														 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														pixels_high.append((13, 23))
														if features[8][4] <= 102.0:
															pixels_low.append((8, 4))
															if features[19][4] <= 218.0:
																pixels_low.append((19, 4))
																ans = 8																 # approximately 25 were 8 out of 25 samples at leaf node
															else:
																pixels_high.append((19, 4))
																ans = 5																 # approximately 1 were 5 out of 1 samples at leaf node
														else:
															pixels_high.append((8, 4))
															ans = 6															 # approximately 1 were 6 out of 1 samples at leaf node
											else:
												pixels_high.append((13, 10))
												if features[19][22] <= 32.0:
													pixels_low.append((19, 22))
													ans = 4													 # approximately 6 were 4 out of 6 samples at leaf node
												else:
													pixels_high.append((19, 22))
													ans = 8													 # approximately 2 were 8 out of 2 samples at leaf node
									else:
										pixels_high.append((9, 19))
										if features[7][5] <= 50.5:
											pixels_low.append((7, 5))
											if features[13][6] <= 6.5:
												pixels_low.append((13, 6))
												if features[9][18] <= 187.0:
													pixels_low.append((9, 18))
													ans = 6													 # approximately 3 were 6 out of 3 samples at leaf node
												else:
													pixels_high.append((9, 18))
													if features[16][6] <= 252.5:
														pixels_low.append((16, 6))
														ans = 0														 # approximately 1 were 0 out of 1 samples at leaf node
													else:
														pixels_high.append((16, 6))
														ans = 9														 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												pixels_high.append((13, 6))
												if features[12][23] <= 34.5:
													pixels_low.append((12, 23))
													if features[20][15] <= 205.0:
														pixels_low.append((20, 15))
														ans = 8														 # approximately 6 were 8 out of 6 samples at leaf node
													else:
														pixels_high.append((20, 15))
														if features[14][20] <= 211.0:
															pixels_low.append((14, 20))
															ans = 6															 # approximately 3 were 6 out of 3 samples at leaf node
														else:
															pixels_high.append((14, 20))
															if features[13][17] <= 39.5:
																pixels_low.append((13, 17))
																ans = 2																 # approximately 1 were 2 out of 1 samples at leaf node
															else:
																pixels_high.append((13, 17))
																ans = 5																 # approximately 3 were 5 out of 3 samples at leaf node
												else:
													pixels_high.append((12, 23))
													if features[5][17] <= 17.5:
														pixels_low.append((5, 17))
														if features[15][15] <= 9.0:
															pixels_low.append((15, 15))
															if features[14][14] <= 232.5:
																pixels_low.append((14, 14))
																if features[23][6] <= 55.5:
																	pixels_low.append((23, 6))
																	ans = 0																	 # approximately 1 were 0 out of 1 samples at leaf node
																else:
																	pixels_high.append((23, 6))
																	ans = 8																	 # approximately 1 were 8 out of 1 samples at leaf node
															else:
																pixels_high.append((14, 14))
																ans = 2																 # approximately 2 were 2 out of 2 samples at leaf node
														else:
															pixels_high.append((15, 15))
															if features[11][17] <= 110.0:
																pixels_low.append((11, 17))
																ans = 6																 # approximately 1 were 6 out of 1 samples at leaf node
															else:
																pixels_high.append((11, 17))
																if features[19][21] <= 254.5:
																	pixels_low.append((19, 21))
																	if features[9][21] <= 23.5:
																		pixels_low.append((9, 21))
																		if features[13][24] <= 151.5:
																			pixels_low.append((13, 24))
																			ans = 8																			 # approximately 11 were 8 out of 11 samples at leaf node
																		else:
																			pixels_high.append((13, 24))
																			if features[18][12] <= 60.0:
																				pixels_low.append((18, 12))
																				ans = 5																				 # approximately 2 were 5 out of 2 samples at leaf node
																			else:
																				pixels_high.append((18, 12))
																				ans = 3																				 # approximately 2 were 3 out of 2 samples at leaf node
																	else:
																		pixels_high.append((9, 21))
																		if features[9][4] <= 68.0:
																			pixels_low.append((9, 4))
																			ans = 8																			 # approximately 168 were 8 out of 168 samples at leaf node
																		else:
																			pixels_high.append((9, 4))
																			if features[19][18] <= 126.0:
																				pixels_low.append((19, 18))
																				ans = 2																				 # approximately 1 were 2 out of 1 samples at leaf node
																			else:
																				pixels_high.append((19, 18))
																				ans = 8																				 # approximately 1 were 8 out of 1 samples at leaf node
																else:
																	pixels_high.append((19, 21))
																	ans = 3																	 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														pixels_high.append((5, 17))
														if features[21][19] <= 6.0:
															pixels_low.append((21, 19))
															ans = 8															 # approximately 2 were 8 out of 2 samples at leaf node
														else:
															pixels_high.append((21, 19))
															ans = 2															 # approximately 3 were 2 out of 3 samples at leaf node
										else:
											pixels_high.append((7, 5))
											if features[18][10] <= 107.5:
												pixels_low.append((18, 10))
												ans = 5												 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												pixels_high.append((18, 10))
												ans = 2												 # approximately 5 were 2 out of 5 samples at leaf node
					else:
						pixels_high.append((15, 10))
						if features[18][16] <= 9.5:
							pixels_low.append((18, 16))
							if features[13][19] <= 126.0:
								pixels_low.append((13, 19))
								if features[18][21] <= 248.0:
									pixels_low.append((18, 21))
									if features[9][14] <= 211.5:
										pixels_low.append((9, 14))
										if features[12][10] <= 253.5:
											pixels_low.append((12, 10))
											ans = 8											 # approximately 17 were 8 out of 17 samples at leaf node
										else:
											pixels_high.append((12, 10))
											ans = 0											 # approximately 1 were 0 out of 1 samples at leaf node
									else:
										pixels_high.append((9, 14))
										ans = 3										 # approximately 1 were 3 out of 1 samples at leaf node
								else:
									pixels_high.append((18, 21))
									if features[8][23] <= 32.5:
										pixels_low.append((8, 23))
										ans = 3										 # approximately 2 were 3 out of 2 samples at leaf node
									else:
										pixels_high.append((8, 23))
										ans = 2										 # approximately 2 were 2 out of 2 samples at leaf node
							else:
								pixels_high.append((13, 19))
								if features[19][20] <= 46.0:
									pixels_low.append((19, 20))
									if features[11][8] <= 242.0:
										pixels_low.append((11, 8))
										if features[14][10] <= 71.5:
											pixels_low.append((14, 10))
											if features[12][15] <= 244.5:
												pixels_low.append((12, 15))
												ans = 7												 # approximately 1 were 7 out of 1 samples at leaf node
											else:
												pixels_high.append((12, 15))
												ans = 2												 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											pixels_high.append((14, 10))
											ans = 1											 # approximately 101 were 1 out of 101 samples at leaf node
									else:
										pixels_high.append((11, 8))
										ans = 8										 # approximately 2 were 8 out of 2 samples at leaf node
								else:
									pixels_high.append((19, 20))
									if features[12][18] <= 189.0:
										pixels_low.append((12, 18))
										ans = 8										 # approximately 1 were 8 out of 1 samples at leaf node
									else:
										pixels_high.append((12, 18))
										ans = 2										 # approximately 8 were 2 out of 8 samples at leaf node
						else:
							pixels_high.append((18, 16))
							if features[11][18] <= 58.0:
								pixels_low.append((11, 18))
								if features[10][6] <= 102.5:
									pixels_low.append((10, 6))
									if features[9][15] <= 252.0:
										pixels_low.append((9, 15))
										if features[18][14] <= 250.0:
											pixels_low.append((18, 14))
											if features[13][10] <= 237.5:
												pixels_low.append((13, 10))
												ans = 8												 # approximately 7 were 8 out of 7 samples at leaf node
											else:
												pixels_high.append((13, 10))
												if features[14][13] <= 126.0:
													pixels_low.append((14, 13))
													ans = 0													 # approximately 1 were 0 out of 1 samples at leaf node
												else:
													pixels_high.append((14, 13))
													ans = 1													 # approximately 1 were 1 out of 1 samples at leaf node
										else:
											pixels_high.append((18, 14))
											ans = 3											 # approximately 3 were 3 out of 3 samples at leaf node
									else:
										pixels_high.append((9, 15))
										ans = 4										 # approximately 5 were 4 out of 5 samples at leaf node
								else:
									pixels_high.append((10, 6))
									if features[9][11] <= 215.5:
										pixels_low.append((9, 11))
										if features[16][6] <= 6.0:
											pixels_low.append((16, 6))
											ans = 1											 # approximately 1 were 1 out of 1 samples at leaf node
										else:
											pixels_high.append((16, 6))
											ans = 3											 # approximately 25 were 3 out of 25 samples at leaf node
									else:
										pixels_high.append((9, 11))
										ans = 8										 # approximately 2 were 8 out of 2 samples at leaf node
							else:
								pixels_high.append((11, 18))
								if features[19][14] <= 148.5:
									pixels_low.append((19, 14))
									if features[14][18] <= 182.5:
										pixels_low.append((14, 18))
										if features[14][21] <= 253.5:
											pixels_low.append((14, 21))
											if features[19][23] <= 253.5:
												pixels_low.append((19, 23))
												if features[16][11] <= 2.0:
													pixels_low.append((16, 11))
													ans = 3													 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													pixels_high.append((16, 11))
													ans = 8													 # approximately 58 were 8 out of 58 samples at leaf node
											else:
												pixels_high.append((19, 23))
												ans = 3												 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											pixels_high.append((14, 21))
											if features[11][5] <= 21.5:
												pixels_low.append((11, 5))
												ans = 0												 # approximately 1 were 0 out of 1 samples at leaf node
											else:
												pixels_high.append((11, 5))
												ans = 3												 # approximately 1 were 3 out of 1 samples at leaf node
									else:
										pixels_high.append((14, 18))
										if features[20][10] <= 81.0:
											pixels_low.append((20, 10))
											if features[9][8] <= 242.5:
												pixels_low.append((9, 8))
												if features[14][9] <= 251.5:
													pixels_low.append((14, 9))
													ans = 1													 # approximately 2 were 1 out of 2 samples at leaf node
												else:
													pixels_high.append((14, 9))
													if features[14][7] <= 253.5:
														pixels_low.append((14, 7))
														if features[15][13] <= 236.5:
															pixels_low.append((15, 13))
															ans = 0															 # approximately 1 were 0 out of 1 samples at leaf node
														else:
															pixels_high.append((15, 13))
															if features[12][11] <= 82.0:
																pixels_low.append((12, 11))
																ans = 7																 # approximately 1 were 7 out of 1 samples at leaf node
															else:
																pixels_high.append((12, 11))
																if features[9][12] <= 144.5:
																	pixels_low.append((9, 12))
																	ans = 4																	 # approximately 1 were 4 out of 1 samples at leaf node
																else:
																	pixels_high.append((9, 12))
																	ans = 8																	 # approximately 1 were 8 out of 1 samples at leaf node
													else:
														pixels_high.append((14, 7))
														ans = 6														 # approximately 2 were 6 out of 2 samples at leaf node
											else:
												pixels_high.append((9, 8))
												ans = 2												 # approximately 3 were 2 out of 3 samples at leaf node
										else:
											pixels_high.append((20, 10))
											ans = 8											 # approximately 5 were 8 out of 5 samples at leaf node
								else:
									pixels_high.append((19, 14))
									if features[15][14] <= 199.0:
										pixels_low.append((15, 14))
										if features[10][14] <= 199.5:
											pixels_low.append((10, 14))
											if features[17][6] <= 252.5:
												pixels_low.append((17, 6))
												ans = 3												 # approximately 4 were 3 out of 4 samples at leaf node
											else:
												pixels_high.append((17, 6))
												if features[7][17] <= 125.5:
													pixels_low.append((7, 17))
													ans = 0													 # approximately 1 were 0 out of 1 samples at leaf node
												else:
													pixels_high.append((7, 17))
													ans = 2													 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											pixels_high.append((10, 14))
											if features[14][15] <= 174.5:
												pixels_low.append((14, 15))
												ans = 0												 # approximately 14 were 0 out of 14 samples at leaf node
											else:
												pixels_high.append((14, 15))
												ans = 8												 # approximately 1 were 8 out of 1 samples at leaf node
									else:
										pixels_high.append((15, 14))
										if features[11][10] <= 236.5:
											pixels_low.append((11, 10))
											if features[11][14] <= 253.5:
												pixels_low.append((11, 14))
												ans = 3												 # approximately 8 were 3 out of 8 samples at leaf node
											else:
												pixels_high.append((11, 14))
												if features[9][7] <= 42.0:
													pixels_low.append((9, 7))
													ans = 4													 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													pixels_high.append((9, 7))
													ans = 8													 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											pixels_high.append((11, 10))
											if features[13][7] <= 239.0:
												pixels_low.append((13, 7))
												if features[7][10] <= 6.5:
													pixels_low.append((7, 10))
													ans = 4													 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													pixels_high.append((7, 10))
													ans = 9													 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												pixels_high.append((13, 7))
												ans = 8												 # approximately 5 were 8 out of 5 samples at leaf node
with open("path_low.txt", 'w') as f: 
	f.write("\n".join([str(px[0]) + " " + str(px[1]) for px in pixels_low])) # save path to file
with open("path_high.txt", 'w') as f: 
	f.write("\n".join([str(px[0]) + " " + str(px[1]) for px in pixels_high])) # save path to file
