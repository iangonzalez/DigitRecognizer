import sys
features = sys.argv[1]
pixels = []
if features[14][17] <= 0.5:
	pixels.append((14, 17))
	if features[15][14] <= 0.5:
		pixels.append((15, 14))
		if features[16][7] <= 5.5:
			pixels.append((16, 7))
			if features[11][15] <= 8.0:
				pixels.append((11, 15))
				if features[17][13] <= 1.0:
					pixels.append((17, 13))
					if features[6][15] <= 1.5:
						pixels.append((6, 15))
						if features[20][10] <= 16.0:
							pixels.append((20, 10))
							if features[22][8] <= 27.0:
								pixels.append((22, 8))
								if features[19][12] <= 84.5:
									pixels.append((19, 12))
									if features[13][17] <= 112.5:
										pixels.append((13, 17))
										return 7 # approximately 84 were 7 out of 84 samples at leaf node
									else:
										if features[8][17] <= 127.0:
											pixels.append((8, 17))
											return 4 # approximately 1 were 4 out of 1 samples at leaf node
										else:
											return 9 # approximately 1 were 9 out of 1 samples at leaf node
								else:
									if features[7][7] <= 121.0:
										pixels.append((7, 7))
										return 6 # approximately 3 were 6 out of 3 samples at leaf node
									else:
										return 4 # approximately 1 were 4 out of 1 samples at leaf node
							else:
								if features[7][17] <= 5.5:
									pixels.append((7, 17))
									if features[22][7] <= 86.0:
										pixels.append((22, 7))
										if features[10][21] <= 41.0:
											pixels.append((10, 21))
											return 5 # approximately 2 were 5 out of 2 samples at leaf node
										else:
											return 8 # approximately 1 were 8 out of 1 samples at leaf node
									else:
										return 2 # approximately 2 were 2 out of 2 samples at leaf node
								else:
									return 0 # approximately 3 were 0 out of 3 samples at leaf node
						else:
							if features[14][12] <= 8.5:
								pixels.append((14, 12))
								if features[19][18] <= 3.5:
									pixels.append((19, 18))
									if features[15][10] <= 107.5:
										pixels.append((15, 10))
										if features[10][12] <= 177.0:
											pixels.append((10, 12))
											if features[14][11] <= 71.0:
												pixels.append((14, 11))
												return 2 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												return 6 # approximately 1 were 6 out of 1 samples at leaf node
										else:
											return 5 # approximately 2 were 5 out of 2 samples at leaf node
									else:
										return 0 # approximately 2 were 0 out of 2 samples at leaf node
								else:
									return 0 # approximately 28 were 0 out of 28 samples at leaf node
							else:
								if features[15][11] <= 5.5:
									pixels.append((15, 11))
									return 5 # approximately 4 were 5 out of 4 samples at leaf node
								else:
									if features[4][11] <= 126.5:
										pixels.append((4, 11))
										if features[14][12] <= 150.0:
											pixels.append((14, 12))
											if features[16][22] <= 126.0:
												pixels.append((16, 22))
												if features[6][21] <= 15.5:
													pixels.append((6, 21))
													return 7 # approximately 1 were 7 out of 1 samples at leaf node
												else:
													return 8 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												return 3 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											return 6 # approximately 3 were 6 out of 3 samples at leaf node
									else:
										return 2 # approximately 3 were 2 out of 3 samples at leaf node
					else:
						if features[22][11] <= 16.5:
							pixels.append((22, 11))
							if features[4][16] <= 17.0:
								pixels.append((4, 16))
								if features[9][20] <= 115.0:
									pixels.append((9, 20))
									if features[18][9] <= 143.5:
										pixels.append((18, 9))
										if features[21][15] <= 105.0:
											pixels.append((21, 15))
											if features[22][18] <= 178.5:
												pixels.append((22, 18))
												return 5 # approximately 7 were 5 out of 7 samples at leaf node
											else:
												return 9 # approximately 1 were 9 out of 1 samples at leaf node
										else:
											if features[8][15] <= 79.5:
												pixels.append((8, 15))
												return 0 # approximately 2 were 0 out of 2 samples at leaf node
											else:
												if features[20][12] <= 6.5:
													pixels.append((20, 12))
													return 7 # approximately 1 were 7 out of 1 samples at leaf node
												else:
													if features[7][9] <= 97.5:
														pixels.append((7, 9))
														return 6 # approximately 1 were 6 out of 1 samples at leaf node
													else:
														return 2 # approximately 1 were 2 out of 1 samples at leaf node
									else:
										return 2 # approximately 6 were 2 out of 6 samples at leaf node
								else:
									if features[18][16] <= 222.0:
										pixels.append((18, 16))
										return 0 # approximately 16 were 0 out of 16 samples at leaf node
									else:
										return 9 # approximately 2 were 9 out of 2 samples at leaf node
							else:
								if features[11][21] <= 112.0:
									pixels.append((11, 21))
									if features[11][12] <= 5.0:
										pixels.append((11, 12))
										return 0 # approximately 1 were 0 out of 1 samples at leaf node
									else:
										return 6 # approximately 20 were 6 out of 20 samples at leaf node
								else:
									if features[21][19] <= 42.5:
										pixels.append((21, 19))
										return 0 # approximately 1 were 0 out of 1 samples at leaf node
									else:
										if features[7][16] <= 80.0:
											pixels.append((7, 16))
											return 4 # approximately 1 were 4 out of 1 samples at leaf node
										else:
											return 1 # approximately 1 were 1 out of 1 samples at leaf node
						else:
							if features[13][16] <= 22.5:
								pixels.append((13, 16))
								if features[19][14] <= 181.5:
									pixels.append((19, 14))
									if features[10][15] <= 184.5:
										pixels.append((10, 15))
										if features[17][25] <= 3.0:
											pixels.append((17, 25))
											if features[3][20] <= 190.0:
												pixels.append((3, 20))
												if features[6][8] <= 253.5:
													pixels.append((6, 8))
													if features[10][14] <= 209.5:
														pixels.append((10, 14))
														return 0 # approximately 321 were 0 out of 321 samples at leaf node
													else:
														if features[6][18] <= 9.5:
															pixels.append((6, 18))
															if features[11][8] <= 126.0:
																pixels.append((11, 8))
																return 5 # approximately 1 were 5 out of 1 samples at leaf node
															else:
																return 9 # approximately 1 were 9 out of 1 samples at leaf node
														else:
															return 0 # approximately 9 were 0 out of 9 samples at leaf node
												else:
													if features[11][23] <= 24.5:
														pixels.append((11, 23))
														return 0 # approximately 1 were 0 out of 1 samples at leaf node
													else:
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												return 6 # approximately 1 were 6 out of 1 samples at leaf node
										else:
											return 2 # approximately 2 were 2 out of 2 samples at leaf node
									else:
										if features[11][17] <= 27.5:
											pixels.append((11, 17))
											return 0 # approximately 4 were 0 out of 4 samples at leaf node
										else:
											if features[8][15] <= 205.0:
												pixels.append((8, 15))
												return 5 # approximately 4 were 5 out of 4 samples at leaf node
											else:
												if features[14][10] <= 63.5:
													pixels.append((14, 10))
													return 3 # approximately 2 were 3 out of 2 samples at leaf node
												else:
													return 0 # approximately 1 were 0 out of 1 samples at leaf node
								else:
									if features[10][11] <= 21.0:
										pixels.append((10, 11))
										if features[9][20] <= 195.0:
											pixels.append((9, 20))
											if features[19][16] <= 90.0:
												pixels.append((19, 16))
												return 3 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												return 2 # approximately 9 were 2 out of 9 samples at leaf node
										else:
											return 7 # approximately 2 were 7 out of 2 samples at leaf node
									else:
										if features[15][17] <= 100.5:
											pixels.append((15, 17))
											if features[22][20] <= 9.0:
												pixels.append((22, 20))
												return 0 # approximately 15 were 0 out of 15 samples at leaf node
											else:
												return 2 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											if features[13][9] <= 124.5:
												pixels.append((13, 9))
												return 6 # approximately 1 were 6 out of 1 samples at leaf node
											else:
												return 7 # approximately 1 were 7 out of 1 samples at leaf node
							else:
								if features[6][18] <= 126.5:
									pixels.append((6, 18))
									if features[4][20] <= 20.5:
										pixels.append((4, 20))
										return 3 # approximately 1 were 3 out of 1 samples at leaf node
									else:
										return 6 # approximately 2 were 6 out of 2 samples at leaf node
								else:
									return 5 # approximately 5 were 5 out of 5 samples at leaf node
				else:
					if features[19][11] <= 86.0:
						pixels.append((19, 11))
						if features[15][19] <= 11.5:
							pixels.append((15, 19))
							if features[4][18] <= 26.0:
								pixels.append((4, 18))
								if features[2][15] <= 3.0:
									pixels.append((2, 15))
									if features[13][14] <= 36.0:
										pixels.append((13, 14))
										if features[18][21] <= 169.5:
											pixels.append((18, 21))
											if features[2][18] <= 11.5:
												pixels.append((2, 18))
												return 5 # approximately 98 were 5 out of 98 samples at leaf node
											else:
												return 6 # approximately 1 were 6 out of 1 samples at leaf node
										else:
											if features[14][9] <= 76.5:
												pixels.append((14, 9))
												return 0 # approximately 1 were 0 out of 1 samples at leaf node
											else:
												return 2 # approximately 2 were 2 out of 2 samples at leaf node
									else:
										if features[24][7] <= 27.5:
											pixels.append((24, 7))
											if features[7][22] <= 127.0:
												pixels.append((7, 22))
												return 1 # approximately 1 were 1 out of 1 samples at leaf node
											else:
												return 8 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											return 3 # approximately 2 were 3 out of 2 samples at leaf node
								else:
									return 6 # approximately 4 were 6 out of 4 samples at leaf node
							else:
								return 6 # approximately 6 were 6 out of 6 samples at leaf node
						else:
							if features[15][11] <= 103.5:
								pixels.append((15, 11))
								if features[8][16] <= 235.0:
									pixels.append((8, 16))
									return 2 # approximately 14 were 2 out of 14 samples at leaf node
								else:
									return 7 # approximately 3 were 7 out of 3 samples at leaf node
							else:
								if features[14][18] <= 32.0:
									pixels.append((14, 18))
									return 6 # approximately 6 were 6 out of 6 samples at leaf node
								else:
									if features[19][18] <= 245.5:
										pixels.append((19, 18))
										if features[9][6] <= 15.5:
											pixels.append((9, 6))
											return 4 # approximately 1 were 4 out of 1 samples at leaf node
										else:
											return 8 # approximately 1 were 8 out of 1 samples at leaf node
									else:
										return 9 # approximately 2 were 9 out of 2 samples at leaf node
					else:
						if features[7][9] <= 1.5:
							pixels.append((7, 9))
							if features[15][11] <= 12.0:
								pixels.append((15, 11))
								if features[18][8] <= 209.5:
									pixels.append((18, 8))
									if features[12][9] <= 13.0:
										pixels.append((12, 9))
										return 9 # approximately 2 were 9 out of 2 samples at leaf node
									else:
										if features[17][18] <= 39.0:
											pixels.append((17, 18))
											return 5 # approximately 2 were 5 out of 2 samples at leaf node
										else:
											if features[14][9] <= 79.0:
												pixels.append((14, 9))
												return 0 # approximately 1 were 0 out of 1 samples at leaf node
											else:
												return 6 # approximately 1 were 6 out of 1 samples at leaf node
								else:
									if features[13][21] <= 253.5:
										pixels.append((13, 21))
										return 2 # approximately 6 were 2 out of 6 samples at leaf node
									else:
										return 4 # approximately 1 were 4 out of 1 samples at leaf node
							else:
								if features[5][16] <= 2.5:
									pixels.append((5, 16))
									if features[4][15] <= 7.5:
										pixels.append((4, 15))
										if features[13][11] <= 248.0:
											pixels.append((13, 11))
											if features[19][13] <= 150.5:
												pixels.append((19, 13))
												if features[10][22] <= 127.0:
													pixels.append((10, 22))
													return 4 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													return 1 # approximately 1 were 1 out of 1 samples at leaf node
											else:
												if features[6][16] <= 68.0:
													pixels.append((6, 16))
													return 5 # approximately 4 were 5 out of 4 samples at leaf node
												else:
													return 6 # approximately 1 were 6 out of 1 samples at leaf node
										else:
											return 2 # approximately 3 were 2 out of 3 samples at leaf node
									else:
										return 6 # approximately 5 were 6 out of 5 samples at leaf node
								else:
									if features[21][22] <= 8.5:
										pixels.append((21, 22))
										return 6 # approximately 61 were 6 out of 61 samples at leaf node
									else:
										return 2 # approximately 1 were 2 out of 1 samples at leaf node
						else:
							if features[19][15] <= 64.0:
								pixels.append((19, 15))
								if features[22][15] <= 120.0:
									pixels.append((22, 15))
									if features[21][17] <= 234.5:
										pixels.append((21, 17))
										return 4 # approximately 2 were 4 out of 2 samples at leaf node
									else:
										return 6 # approximately 1 were 6 out of 1 samples at leaf node
								else:
									return 0 # approximately 5 were 0 out of 5 samples at leaf node
							else:
								if features[24][4] <= 30.0:
									pixels.append((24, 4))
									return 2 # approximately 32 were 2 out of 32 samples at leaf node
								else:
									return 7 # approximately 1 were 7 out of 1 samples at leaf node
			else:
				if features[10][4] <= 1.5:
					pixels.append((10, 4))
					if features[17][10] <= 112.5:
						pixels.append((17, 10))
						if features[10][9] <= 5.5:
							pixels.append((10, 9))
							if features[5][12] <= 12.5:
								pixels.append((5, 12))
								if features[7][11] <= 60.0:
									pixels.append((7, 11))
									if features[16][9] <= 227.0:
										pixels.append((16, 9))
										if features[19][4] <= 220.0:
											pixels.append((19, 4))
											if features[11][12] <= 7.5:
												pixels.append((11, 12))
												if features[20][14] <= 116.0:
													pixels.append((20, 14))
													if features[16][19] <= 123.5:
														pixels.append((16, 19))
														if features[15][11] <= 4.5:
															pixels.append((15, 11))
															return 5 # approximately 2 were 5 out of 2 samples at leaf node
														else:
															if features[23][12] <= 84.5:
																pixels.append((23, 12))
																return 2 # approximately 2 were 2 out of 2 samples at leaf node
															else:
																if features[5][17] <= 36.5:
																	pixels.append((5, 17))
																	return 1 # approximately 1 were 1 out of 1 samples at leaf node
																else:
																	return 8 # approximately 1 were 8 out of 1 samples at leaf node
													else:
														return 4 # approximately 2 were 4 out of 2 samples at leaf node
												else:
													if features[3][19] <= 114.0:
														pixels.append((3, 19))
														return 3 # approximately 5 were 3 out of 5 samples at leaf node
													else:
														return 6 # approximately 1 were 6 out of 1 samples at leaf node
											else:
												if features[12][3] <= 106.0:
													pixels.append((12, 3))
													if features[23][15] <= 207.0:
														pixels.append((23, 15))
														if features[12][23] <= 125.0:
															pixels.append((12, 23))
															if features[17][17] <= 252.5:
																pixels.append((17, 17))
																if features[23][9] <= 250.5:
																	pixels.append((23, 9))
																	return 5 # approximately 63 were 5 out of 63 samples at leaf node
																else:
																	return 3 # approximately 1 were 3 out of 1 samples at leaf node
															else:
																return 6 # approximately 1 were 6 out of 1 samples at leaf node
														else:
															return 0 # approximately 1 were 0 out of 1 samples at leaf node
													else:
														if features[10][10] <= 6.0:
															pixels.append((10, 10))
															if features[22][14] <= 103.5:
																pixels.append((22, 14))
																if features[18][15] <= 127.0:
																	pixels.append((18, 15))
																	return 3 # approximately 1 were 3 out of 1 samples at leaf node
																else:
																	return 4 # approximately 1 were 4 out of 1 samples at leaf node
															else:
																return 1 # approximately 3 were 1 out of 3 samples at leaf node
														else:
															return 5 # approximately 3 were 5 out of 3 samples at leaf node
												else:
													return 7 # approximately 3 were 7 out of 3 samples at leaf node
										else:
											return 3 # approximately 6 were 3 out of 6 samples at leaf node
									else:
										if features[9][15] <= 225.5:
											pixels.append((9, 15))
											if features[5][18] <= 50.5:
												pixels.append((5, 18))
												return 6 # approximately 2 were 6 out of 2 samples at leaf node
											else:
												return 8 # approximately 4 were 8 out of 4 samples at leaf node
										else:
											return 0 # approximately 5 were 0 out of 5 samples at leaf node
								else:
									if features[22][18] <= 236.5:
										pixels.append((22, 18))
										if features[12][14] <= 12.0:
											pixels.append((12, 14))
											if features[13][18] <= 57.5:
												pixels.append((13, 18))
												return 7 # approximately 2 were 7 out of 2 samples at leaf node
											else:
												if features[9][4] <= 82.5:
													pixels.append((9, 4))
													return 0 # approximately 1 were 0 out of 1 samples at leaf node
												else:
													return 2 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											if features[10][10] <= 60.5:
												pixels.append((10, 10))
												return 3 # approximately 27 were 3 out of 27 samples at leaf node
											else:
												if features[5][15] <= 87.5:
													pixels.append((5, 15))
													return 4 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													return 5 # approximately 1 were 5 out of 1 samples at leaf node
									else:
										return 5 # approximately 3 were 5 out of 3 samples at leaf node
							else:
								if features[9][11] <= 140.5:
									pixels.append((9, 11))
									if features[11][6] <= 109.5:
										pixels.append((11, 6))
										if features[18][11] <= 188.0:
											pixels.append((18, 11))
											if features[16][14] <= 218.5:
												pixels.append((16, 14))
												if features[11][8] <= 153.0:
													pixels.append((11, 8))
													if features[8][24] <= 70.0:
														pixels.append((8, 24))
														if features[9][12] <= 250.0:
															pixels.append((9, 12))
															return 3 # approximately 169 were 3 out of 169 samples at leaf node
														else:
															if features[7][16] <= 111.0:
																pixels.append((7, 16))
																return 5 # approximately 1 were 5 out of 1 samples at leaf node
															else:
																return 3 # approximately 2 were 3 out of 2 samples at leaf node
													else:
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													if features[15][12] <= 9.0:
														pixels.append((15, 12))
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														return 8 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												return 1 # approximately 2 were 1 out of 2 samples at leaf node
										else:
											if features[22][18] <= 1.5:
												pixels.append((22, 18))
												return 2 # approximately 4 were 2 out of 4 samples at leaf node
											else:
												if features[14][10] <= 7.0:
													pixels.append((14, 10))
													return 8 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													return 3 # approximately 2 were 3 out of 2 samples at leaf node
									else:
										if features[11][20] <= 251.0:
											pixels.append((11, 20))
											return 5 # approximately 6 were 5 out of 6 samples at leaf node
										else:
											return 9 # approximately 1 were 9 out of 1 samples at leaf node
								else:
									if features[8][16] <= 40.5:
										pixels.append((8, 16))
										if features[14][9] <= 101.0:
											pixels.append((14, 9))
											return 5 # approximately 12 were 5 out of 12 samples at leaf node
										else:
											return 6 # approximately 1 were 6 out of 1 samples at leaf node
									else:
										if features[18][16] <= 150.0:
											pixels.append((18, 16))
											return 3 # approximately 4 were 3 out of 4 samples at leaf node
										else:
											if features[10][14] <= 127.5:
												pixels.append((10, 14))
												return 8 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												return 5 # approximately 1 were 5 out of 1 samples at leaf node
						else:
							if features[6][14] <= 6.5:
								pixels.append((6, 14))
								if features[17][18] <= 84.5:
									pixels.append((17, 18))
									if features[15][5] <= 95.5:
										pixels.append((15, 5))
										if features[13][14] <= 27.5:
											pixels.append((13, 14))
											if features[12][20] <= 153.0:
												pixels.append((12, 20))
												if features[16][16] <= 126.5:
													pixels.append((16, 16))
													return 5 # approximately 18 were 5 out of 18 samples at leaf node
												else:
													return 7 # approximately 1 were 7 out of 1 samples at leaf node
											else:
												if features[24][17] <= 144.0:
													pixels.append((24, 17))
													if features[6][18] <= 78.0:
														pixels.append((6, 18))
														return 0 # approximately 1 were 0 out of 1 samples at leaf node
													else:
														return 3 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													return 7 # approximately 2 were 7 out of 2 samples at leaf node
										else:
											if features[8][12] <= 39.5:
												pixels.append((8, 12))
												if features[19][21] <= 127.5:
													pixels.append((19, 21))
													return 4 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													return 8 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												return 9 # approximately 4 were 9 out of 4 samples at leaf node
									else:
										return 0 # approximately 6 were 0 out of 6 samples at leaf node
								else:
									if features[6][19] <= 43.0:
										pixels.append((6, 19))
										return 7 # approximately 28 were 7 out of 28 samples at leaf node
									else:
										if features[17][5] <= 71.5:
											pixels.append((17, 5))
											if features[12][14] <= 128.5:
												pixels.append((12, 14))
												return 5 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												return 3 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											return 0 # approximately 2 were 0 out of 2 samples at leaf node
							else:
								if features[9][16] <= 112.0:
									pixels.append((9, 16))
									if features[9][14] <= 209.0:
										pixels.append((9, 14))
										if features[12][9] <= 42.0:
											pixels.append((12, 9))
											if features[7][14] <= 198.0:
												pixels.append((7, 14))
												return 5 # approximately 6 were 5 out of 6 samples at leaf node
											else:
												if features[19][21] <= 45.5:
													pixels.append((19, 21))
													return 3 # approximately 5 were 3 out of 5 samples at leaf node
												else:
													if features[5][10] <= 15.0:
														pixels.append((5, 10))
														return 0 # approximately 1 were 0 out of 1 samples at leaf node
													else:
														return 8 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											if features[16][17] <= 86.0:
												pixels.append((16, 17))
												if features[11][16] <= 4.5:
													pixels.append((11, 16))
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													if features[9][18] <= 253.0:
														pixels.append((9, 18))
														return 5 # approximately 110 were 5 out of 110 samples at leaf node
													else:
														return 8 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												return 9 # approximately 1 were 9 out of 1 samples at leaf node
									else:
										if features[5][13] <= 18.5:
											pixels.append((5, 13))
											if features[7][11] <= 127.0:
												pixels.append((7, 11))
												return 7 # approximately 1 were 7 out of 1 samples at leaf node
											else:
												return 5 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											return 3 # approximately 5 were 3 out of 5 samples at leaf node
								else:
									if features[9][20] <= 225.0:
										pixels.append((9, 20))
										if features[10][9] <= 204.5:
											pixels.append((10, 9))
											if features[9][12] <= 244.0:
												pixels.append((9, 12))
												if features[10][8] <= 172.0:
													pixels.append((10, 8))
													return 3 # approximately 20 were 3 out of 20 samples at leaf node
												else:
													if features[11][8] <= 98.5:
														pixels.append((11, 8))
														return 2 # approximately 1 were 2 out of 1 samples at leaf node
													else:
														return 8 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												return 5 # approximately 3 were 5 out of 3 samples at leaf node
										else:
											if features[11][10] <= 252.5:
												pixels.append((11, 10))
												if features[20][17] <= 47.0:
													pixels.append((20, 17))
													return 9 # approximately 2 were 9 out of 2 samples at leaf node
												else:
													if features[23][5] <= 23.5:
														pixels.append((23, 5))
														if features[8][15] <= 126.5:
															pixels.append((8, 15))
															return 8 # approximately 1 were 8 out of 1 samples at leaf node
														else:
															return 3 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														return 2 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												return 5 # approximately 9 were 5 out of 9 samples at leaf node
									else:
										if features[22][14] <= 254.0:
											pixels.append((22, 14))
											return 0 # approximately 7 were 0 out of 7 samples at leaf node
										else:
											return 9 # approximately 1 were 9 out of 1 samples at leaf node
					else:
						if features[12][10] <= 14.0:
							pixels.append((12, 10))
							if features[20][22] <= 0.5:
								pixels.append((20, 22))
								if features[3][20] <= 1.5:
									pixels.append((3, 20))
									if features[11][17] <= 108.0:
										pixels.append((11, 17))
										if features[10][12] <= 82.5:
											pixels.append((10, 12))
											if features[20][16] <= 252.5:
												pixels.append((20, 16))
												return 2 # approximately 22 were 2 out of 22 samples at leaf node
											else:
												if features[18][19] <= 124.0:
													pixels.append((18, 19))
													return 6 # approximately 3 were 6 out of 3 samples at leaf node
												else:
													return 2 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											if features[14][18] <= 5.5:
												pixels.append((14, 18))
												return 1 # approximately 2 were 1 out of 2 samples at leaf node
											else:
												return 0 # approximately 1 were 0 out of 1 samples at leaf node
									else:
										if features[13][15] <= 235.0:
											pixels.append((13, 15))
											if features[5][11] <= 176.5:
												pixels.append((5, 11))
												if features[13][18] <= 25.5:
													pixels.append((13, 18))
													if features[14][14] <= 18.0:
														pixels.append((14, 14))
														if features[7][16] <= 134.5:
															pixels.append((7, 16))
															return 5 # approximately 6 were 5 out of 6 samples at leaf node
														else:
															return 0 # approximately 1 were 0 out of 1 samples at leaf node
													else:
														if features[15][13] <= 83.5:
															pixels.append((15, 13))
															return 2 # approximately 3 were 2 out of 3 samples at leaf node
														else:
															if features[16][10] <= 112.0:
																pixels.append((16, 10))
																return 8 # approximately 1 were 8 out of 1 samples at leaf node
															else:
																if features[5][19] <= 69.0:
																	pixels.append((5, 19))
																	if features[4][17] <= 108.5:
																		pixels.append((4, 17))
																		return 1 # approximately 1 were 1 out of 1 samples at leaf node
																	else:
																		return 6 # approximately 1 were 6 out of 1 samples at leaf node
																else:
																	return 3 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													return 6 # approximately 6 were 6 out of 6 samples at leaf node
											else:
												if features[9][17] <= 31.5:
													pixels.append((9, 17))
													return 2 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													return 3 # approximately 5 were 3 out of 5 samples at leaf node
										else:
											return 8 # approximately 5 were 8 out of 5 samples at leaf node
								else:
									return 6 # approximately 12 were 6 out of 12 samples at leaf node
							else:
								if features[14][12] <= 85.0:
									pixels.append((14, 12))
									return 3 # approximately 2 were 3 out of 2 samples at leaf node
								else:
									if features[17][23] <= 247.0:
										pixels.append((17, 23))
										return 2 # approximately 46 were 2 out of 46 samples at leaf node
									else:
										return 8 # approximately 1 were 8 out of 1 samples at leaf node
						else:
							if features[19][18] <= 39.0:
								pixels.append((19, 18))
								if features[14][13] <= 127.5:
									pixels.append((14, 13))
									if features[5][19] <= 174.5:
										pixels.append((5, 19))
										if features[4][15] <= 85.5:
											pixels.append((4, 15))
											if features[16][17] <= 72.0:
												pixels.append((16, 17))
												if features[12][21] <= 191.5:
													pixels.append((12, 21))
													return 5 # approximately 38 were 5 out of 38 samples at leaf node
												else:
													return 6 # approximately 1 were 6 out of 1 samples at leaf node
											else:
												if features[13][10] <= 83.0:
													pixels.append((13, 10))
													return 8 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													if features[7][10] <= 127.0:
														pixels.append((7, 10))
														return 7 # approximately 1 were 7 out of 1 samples at leaf node
													else:
														return 4 # approximately 1 were 4 out of 1 samples at leaf node
										else:
											return 2 # approximately 2 were 2 out of 2 samples at leaf node
									else:
										if features[18][13] <= 39.0:
											pixels.append((18, 13))
											return 0 # approximately 1 were 0 out of 1 samples at leaf node
										else:
											return 6 # approximately 3 were 6 out of 3 samples at leaf node
								else:
									if features[20][12] <= 224.0:
										pixels.append((20, 12))
										return 8 # approximately 7 were 8 out of 7 samples at leaf node
									else:
										if features[9][18] <= 127.0:
											pixels.append((9, 18))
											return 6 # approximately 2 were 6 out of 2 samples at leaf node
										else:
											return 0 # approximately 1 were 0 out of 1 samples at leaf node
							else:
								if features[23][12] <= 6.0:
									pixels.append((23, 12))
									if features[19][6] <= 13.0:
										pixels.append((19, 6))
										if features[17][8] <= 244.0:
											pixels.append((17, 8))
											if features[16][25] <= 71.0:
												pixels.append((16, 25))
												return 6 # approximately 35 were 6 out of 35 samples at leaf node
											else:
												return 2 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											return 0 # approximately 1 were 0 out of 1 samples at leaf node
									else:
										if features[22][8] <= 126.0:
											pixels.append((22, 8))
											return 2 # approximately 2 were 2 out of 2 samples at leaf node
										else:
											return 3 # approximately 1 were 3 out of 1 samples at leaf node
								else:
									if features[9][15] <= 29.5:
										pixels.append((9, 15))
										if features[18][17] <= 52.5:
											pixels.append((18, 17))
											return 5 # approximately 5 were 5 out of 5 samples at leaf node
										else:
											if features[17][10] <= 249.5:
												pixels.append((17, 10))
												return 8 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												return 6 # approximately 1 were 6 out of 1 samples at leaf node
									else:
										if features[16][19] <= 11.0:
											pixels.append((16, 19))
											if features[19][19] <= 173.0:
												pixels.append((19, 19))
												return 5 # approximately 2 were 5 out of 2 samples at leaf node
											else:
												if features[13][21] <= 126.0:
													pixels.append((13, 21))
													return 2 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													return 8 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											if features[20][17] <= 29.5:
												pixels.append((20, 17))
												return 6 # approximately 1 were 6 out of 1 samples at leaf node
											else:
												if features[9][18] <= 44.5:
													pixels.append((9, 18))
													if features[18][17] <= 140.5:
														pixels.append((18, 17))
														return 6 # approximately 1 were 6 out of 1 samples at leaf node
													else:
														return 0 # approximately 1 were 0 out of 1 samples at leaf node
												else:
													return 0 # approximately 21 were 0 out of 21 samples at leaf node
				else:
					if features[20][10] <= 7.5:
						pixels.append((20, 10))
						if features[6][11] <= 64.0:
							pixels.append((6, 11))
							return 7 # approximately 78 were 7 out of 78 samples at leaf node
						else:
							if features[23][7] <= 12.5:
								pixels.append((23, 7))
								return 5 # approximately 2 were 5 out of 2 samples at leaf node
							else:
								return 3 # approximately 2 were 3 out of 2 samples at leaf node
					else:
						if features[13][9] <= 38.5:
							pixels.append((13, 9))
							return 3 # approximately 7 were 3 out of 7 samples at leaf node
						else:
							return 8 # approximately 1 were 8 out of 1 samples at leaf node
		else:
			if features[17][13] <= 127.0:
				pixels.append((17, 13))
				if features[22][11] <= 0.5:
					pixels.append((22, 11))
					if features[19][7] <= 34.0:
						pixels.append((19, 7))
						if features[19][11] <= 5.0:
							pixels.append((19, 11))
							if features[14][11] <= 65.5:
								pixels.append((14, 11))
								if features[6][15] <= 93.0:
									pixels.append((6, 15))
									if features[17][13] <= 62.0:
										pixels.append((17, 13))
										return 7 # approximately 54 were 7 out of 54 samples at leaf node
									else:
										return 5 # approximately 3 were 5 out of 3 samples at leaf node
								else:
									if features[8][13] <= 52.5:
										pixels.append((8, 13))
										return 4 # approximately 1 were 4 out of 1 samples at leaf node
									else:
										return 0 # approximately 3 were 0 out of 3 samples at leaf node
							else:
								if features[15][20] <= 116.5:
									pixels.append((15, 20))
									return 5 # approximately 6 were 5 out of 6 samples at leaf node
								else:
									if features[9][9] <= 124.0:
										pixels.append((9, 9))
										if features[18][7] <= 1.0:
											pixels.append((18, 7))
											return 7 # approximately 3 were 7 out of 3 samples at leaf node
										else:
											return 4 # approximately 1 were 4 out of 1 samples at leaf node
									else:
										return 9 # approximately 5 were 9 out of 5 samples at leaf node
						else:
							if features[8][17] <= 28.5:
								pixels.append((8, 17))
								if features[20][16] <= 73.0:
									pixels.append((20, 16))
									if features[17][14] <= 7.0:
										pixels.append((17, 14))
										if features[8][18] <= 53.0:
											pixels.append((8, 18))
											if features[20][10] <= 17.5:
												pixels.append((20, 10))
												if features[16][17] <= 77.5:
													pixels.append((16, 17))
													return 6 # approximately 2 were 6 out of 2 samples at leaf node
												else:
													return 9 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												return 2 # approximately 2 were 2 out of 2 samples at leaf node
										else:
											return 0 # approximately 2 were 0 out of 2 samples at leaf node
									else:
										return 4 # approximately 4 were 4 out of 4 samples at leaf node
								else:
									if features[10][5] <= 195.0:
										pixels.append((10, 5))
										if features[21][21] <= 103.0:
											pixels.append((21, 21))
											return 6 # approximately 24 were 6 out of 24 samples at leaf node
										else:
											return 2 # approximately 1 were 2 out of 1 samples at leaf node
									else:
										return 0 # approximately 2 were 0 out of 2 samples at leaf node
							else:
								if features[14][19] <= 84.0:
									pixels.append((14, 19))
									if features[9][14] <= 253.5:
										pixels.append((9, 14))
										if features[2][8] <= 63.5:
											pixels.append((2, 8))
											return 0 # approximately 24 were 0 out of 24 samples at leaf node
										else:
											return 6 # approximately 1 were 6 out of 1 samples at leaf node
									else:
										return 5 # approximately 1 were 5 out of 1 samples at leaf node
								else:
									if features[20][10] <= 112.5:
										pixels.append((20, 10))
										return 9 # approximately 8 were 9 out of 8 samples at leaf node
									else:
										if features[15][9] <= 29.5:
											pixels.append((15, 9))
											if features[12][12] <= 118.5:
												pixels.append((12, 12))
												return 3 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												return 5 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											return 0 # approximately 5 were 0 out of 5 samples at leaf node
					else:
						if features[12][22] <= 1.5:
							pixels.append((12, 22))
							if features[23][9] <= 40.5:
								pixels.append((23, 9))
								if features[16][20] <= 62.5:
									pixels.append((16, 20))
									if features[8][21] <= 114.0:
										pixels.append((8, 21))
										if features[17][24] <= 253.0:
											pixels.append((17, 24))
											if features[15][23] <= 150.0:
												pixels.append((15, 23))
												return 2 # approximately 10 were 2 out of 10 samples at leaf node
											else:
												return 6 # approximately 1 were 6 out of 1 samples at leaf node
										else:
											return 1 # approximately 1 were 1 out of 1 samples at leaf node
									else:
										return 5 # approximately 2 were 5 out of 2 samples at leaf node
								else:
									if features[19][13] <= 105.5:
										pixels.append((19, 13))
										if features[9][9] <= 149.0:
											pixels.append((9, 9))
											return 5 # approximately 3 were 5 out of 3 samples at leaf node
										else:
											return 7 # approximately 4 were 7 out of 4 samples at leaf node
									else:
										if features[14][9] <= 10.5:
											pixels.append((14, 9))
											if features[12][23] <= 43.0:
												pixels.append((12, 23))
												if features[12][14] <= 49.5:
													pixels.append((12, 14))
													return 9 # approximately 2 were 9 out of 2 samples at leaf node
												else:
													return 3 # approximately 2 were 3 out of 2 samples at leaf node
											else:
												return 0 # approximately 3 were 0 out of 3 samples at leaf node
										else:
											if features[18][6] <= 246.5:
												pixels.append((18, 6))
												if features[17][6] <= 253.5:
													pixels.append((17, 6))
													return 6 # approximately 8 were 6 out of 8 samples at leaf node
												else:
													return 2 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												return 4 # approximately 1 were 4 out of 1 samples at leaf node
							else:
								return 0 # approximately 9 were 0 out of 9 samples at leaf node
						else:
							if features[4][11] <= 129.5:
								pixels.append((4, 11))
								if features[15][13] <= 74.5:
									pixels.append((15, 13))
									if features[24][16] <= 213.0:
										pixels.append((24, 16))
										if features[25][22] <= 45.0:
											pixels.append((25, 22))
											if features[14][4] <= 254.5:
												pixels.append((14, 4))
												if features[17][5] <= 254.5:
													pixels.append((17, 5))
													return 0 # approximately 150 were 0 out of 150 samples at leaf node
												else:
													if features[21][6] <= 21.0:
														pixels.append((21, 6))
														return 0 # approximately 4 were 0 out of 4 samples at leaf node
													else:
														return 6 # approximately 1 were 6 out of 1 samples at leaf node
											else:
												return 4 # approximately 1 were 4 out of 1 samples at leaf node
										else:
											return 9 # approximately 1 were 9 out of 1 samples at leaf node
									else:
										if features[13][10] <= 12.5:
											pixels.append((13, 10))
											return 7 # approximately 2 were 7 out of 2 samples at leaf node
										else:
											if features[12][7] <= 122.5:
												pixels.append((12, 7))
												return 0 # approximately 2 were 0 out of 2 samples at leaf node
											else:
												return 9 # approximately 1 were 9 out of 1 samples at leaf node
								else:
									if features[13][11] <= 15.0:
										pixels.append((13, 11))
										return 5 # approximately 1 were 5 out of 1 samples at leaf node
									else:
										return 6 # approximately 1 were 6 out of 1 samples at leaf node
							else:
								if features[23][24] <= 126.0:
									pixels.append((23, 24))
									return 6 # approximately 4 were 6 out of 4 samples at leaf node
								else:
									return 9 # approximately 1 were 9 out of 1 samples at leaf node
				else:
					if features[12][16] <= 119.5:
						pixels.append((12, 16))
						if features[11][16] <= 201.5:
							pixels.append((11, 16))
							if features[25][11] <= 12.5:
								pixels.append((25, 11))
								if features[3][19] <= 3.5:
									pixels.append((3, 19))
									if features[19][3] <= 189.5:
										pixels.append((19, 3))
										if features[25][7] <= 126.5:
											pixels.append((25, 7))
											if features[13][14] <= 253.5:
												pixels.append((13, 14))
												if features[3][12] <= 254.5:
													pixels.append((3, 12))
													if features[17][12] <= 246.5:
														pixels.append((17, 12))
														if features[18][12] <= 251.5:
															pixels.append((18, 12))
															if features[10][16] <= 253.5:
																pixels.append((10, 16))
																if features[3][12] <= 251.5:
																	pixels.append((3, 12))
																	if features[17][14] <= 113.5:
																		pixels.append((17, 14))
																		if features[13][19] <= 253.5:
																			pixels.append((13, 19))
																			if features[4][21] <= 214.5:
																				pixels.append((4, 21))
																				return 0 # approximately 2386 were 0 out of 2386 samples at leaf node
																			else:
																				if features[17][20] <= 254.5:
																					pixels.append((17, 20))
																					return 0 # approximately 53 were 0 out of 53 samples at leaf node
																				else:
																					return 6 # approximately 1 were 6 out of 1 samples at leaf node
																		else:
																			if features[9][19] <= 19.0:
																				pixels.append((9, 19))
																				return 5 # approximately 1 were 5 out of 1 samples at leaf node
																			else:
																				if features[24][16] <= 216.0:
																					pixels.append((24, 16))
																					return 0 # approximately 45 were 0 out of 45 samples at leaf node
																				else:
																					return 9 # approximately 1 were 9 out of 1 samples at leaf node
																	else:
																		if features[9][22] <= 94.0:
																			pixels.append((9, 22))
																			return 6 # approximately 1 were 6 out of 1 samples at leaf node
																		else:
																			return 0 # approximately 12 were 0 out of 12 samples at leaf node
																else:
																	if features[18][19] <= 7.5:
																		pixels.append((18, 19))
																		return 6 # approximately 1 were 6 out of 1 samples at leaf node
																	else:
																		return 0 # approximately 7 were 0 out of 7 samples at leaf node
															else:
																if features[4][11] <= 19.5:
																	pixels.append((4, 11))
																	return 0 # approximately 20 were 0 out of 20 samples at leaf node
																else:
																	if features[16][22] <= 123.0:
																		pixels.append((16, 22))
																		return 3 # approximately 1 were 3 out of 1 samples at leaf node
																	else:
																		return 5 # approximately 1 were 5 out of 1 samples at leaf node
														else:
															if features[20][12] <= 113.0:
																pixels.append((20, 12))
																return 2 # approximately 2 were 2 out of 2 samples at leaf node
															else:
																return 0 # approximately 13 were 0 out of 13 samples at leaf node
													else:
														if features[6][15] <= 126.0:
															pixels.append((6, 15))
															return 0 # approximately 1 were 0 out of 1 samples at leaf node
														else:
															return 6 # approximately 1 were 6 out of 1 samples at leaf node
												else:
													if features[8][9] <= 110.0:
														pixels.append((8, 9))
														return 3 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														return 0 # approximately 1 were 0 out of 1 samples at leaf node
											else:
												return 2 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											return 7 # approximately 1 were 7 out of 1 samples at leaf node
									else:
										if features[7][19] <= 117.5:
											pixels.append((7, 19))
											return 5 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											return 2 # approximately 1 were 2 out of 1 samples at leaf node
								else:
									if features[9][21] <= 1.5:
										pixels.append((9, 21))
										if features[17][17] <= 245.5:
											pixels.append((17, 17))
											if features[12][13] <= 152.0:
												pixels.append((12, 13))
												return 0 # approximately 6 were 0 out of 6 samples at leaf node
											else:
												if features[18][25] <= 11.0:
													pixels.append((18, 25))
													return 2 # approximately 2 were 2 out of 2 samples at leaf node
												else:
													return 6 # approximately 1 were 6 out of 1 samples at leaf node
										else:
											return 6 # approximately 9 were 6 out of 9 samples at leaf node
									else:
										if features[17][3] <= 71.5:
											pixels.append((17, 3))
											return 0 # approximately 41 were 0 out of 41 samples at leaf node
										else:
											return 3 # approximately 1 were 3 out of 1 samples at leaf node
							else:
								if features[24][11] <= 240.5:
									pixels.append((24, 11))
									return 7 # approximately 2 were 7 out of 2 samples at leaf node
								else:
									if features[16][24] <= 72.5:
										pixels.append((16, 24))
										if features[17][11] <= 6.5:
											pixels.append((17, 11))
											return 5 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											return 9 # approximately 1 were 9 out of 1 samples at leaf node
									else:
										return 0 # approximately 1 were 0 out of 1 samples at leaf node
						else:
							if features[10][21] <= 55.0:
								pixels.append((10, 21))
								if features[8][14] <= 205.0:
									pixels.append((8, 14))
									if features[9][16] <= 12.0:
										pixels.append((9, 16))
										return 5 # approximately 8 were 5 out of 8 samples at leaf node
									else:
										if features[19][18] <= 43.5:
											pixels.append((19, 18))
											if features[23][9] <= 172.0:
												pixels.append((23, 9))
												if features[23][10] <= 41.5:
													pixels.append((23, 10))
													return 0 # approximately 1 were 0 out of 1 samples at leaf node
												else:
													return 8 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												return 5 # approximately 3 were 5 out of 3 samples at leaf node
										else:
											if features[8][11] <= 69.5:
												pixels.append((8, 11))
												return 3 # approximately 7 were 3 out of 7 samples at leaf node
											else:
												return 6 # approximately 1 were 6 out of 1 samples at leaf node
								else:
									if features[5][17] <= 218.0:
										pixels.append((5, 17))
										return 0 # approximately 8 were 0 out of 8 samples at leaf node
									else:
										if features[13][22] <= 63.5:
											pixels.append((13, 22))
											if features[3][15] <= 104.0:
												pixels.append((3, 15))
												return 8 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												if features[16][18] <= 8.0:
													pixels.append((16, 18))
													return 2 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											return 6 # approximately 2 were 6 out of 2 samples at leaf node
							else:
								if features[9][25] <= 66.0:
									pixels.append((9, 25))
									return 0 # approximately 51 were 0 out of 51 samples at leaf node
								else:
									return 5 # approximately 1 were 5 out of 1 samples at leaf node
					else:
						if features[9][15] <= 217.5:
							pixels.append((9, 15))
							if features[18][8] <= 241.0:
								pixels.append((18, 8))
								if features[9][19] <= 6.0:
									pixels.append((9, 19))
									if features[13][20] <= 18.0:
										pixels.append((13, 20))
										if features[22][9] <= 120.0:
											pixels.append((22, 9))
											return 6 # approximately 1 were 6 out of 1 samples at leaf node
										else:
											return 8 # approximately 2 were 8 out of 2 samples at leaf node
									else:
										if features[13][18] <= 20.5:
											pixels.append((13, 18))
											if features[13][8] <= 9.5:
												pixels.append((13, 8))
												return 3 # approximately 3 were 3 out of 3 samples at leaf node
											else:
												if features[19][20] <= 43.0:
													pixels.append((19, 20))
													return 5 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													return 0 # approximately 1 were 0 out of 1 samples at leaf node
										else:
											if features[23][8] <= 211.5:
												pixels.append((23, 8))
												return 5 # approximately 20 were 5 out of 20 samples at leaf node
											else:
												return 3 # approximately 1 were 3 out of 1 samples at leaf node
								else:
									if features[9][13] <= 5.5:
										pixels.append((9, 13))
										if features[19][15] <= 2.0:
											pixels.append((19, 15))
											if features[12][12] <= 88.5:
												pixels.append((12, 12))
												return 2 # approximately 2 were 2 out of 2 samples at leaf node
											else:
												return 8 # approximately 5 were 8 out of 5 samples at leaf node
										else:
											return 3 # approximately 7 were 3 out of 7 samples at leaf node
									else:
										return 0 # approximately 7 were 0 out of 7 samples at leaf node
							else:
								if features[8][18] <= 71.0:
									pixels.append((8, 18))
									if features[14][8] <= 8.0:
										pixels.append((14, 8))
										if features[9][16] <= 28.5:
											pixels.append((9, 16))
											return 8 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											return 5 # approximately 1 were 5 out of 1 samples at leaf node
									else:
										return 6 # approximately 16 were 6 out of 16 samples at leaf node
								else:
									if features[18][20] <= 233.5:
										pixels.append((18, 20))
										return 2 # approximately 3 were 2 out of 3 samples at leaf node
									else:
										if features[11][22] <= 97.0:
											pixels.append((11, 22))
											return 8 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											return 0 # approximately 2 were 0 out of 2 samples at leaf node
						else:
							if features[10][20] <= 49.0:
								pixels.append((10, 20))
								if features[13][9] <= 148.5:
									pixels.append((13, 9))
									if features[18][17] <= 210.5:
										pixels.append((18, 17))
										return 3 # approximately 2 were 3 out of 2 samples at leaf node
									else:
										if features[7][20] <= 138.0:
											pixels.append((7, 20))
											return 5 # approximately 2 were 5 out of 2 samples at leaf node
										else:
											return 2 # approximately 1 were 2 out of 1 samples at leaf node
								else:
									return 0 # approximately 4 were 0 out of 4 samples at leaf node
							else:
								return 0 # approximately 38 were 0 out of 38 samples at leaf node
			else:
				if features[12][8] <= 2.0:
					pixels.append((12, 8))
					if features[18][16] <= 169.0:
						pixels.append((18, 16))
						if features[7][24] <= 141.5:
							pixels.append((7, 24))
							if features[10][6] <= 87.0:
								pixels.append((10, 6))
								if features[15][20] <= 249.0:
									pixels.append((15, 20))
									if features[15][20] <= 32.0:
										pixels.append((15, 20))
										if features[4][18] <= 119.0:
											pixels.append((4, 18))
											if features[6][9] <= 126.5:
												pixels.append((6, 9))
												if features[19][10] <= 127.5:
													pixels.append((19, 10))
													return 8 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													return 5 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												return 3 # approximately 2 were 3 out of 2 samples at leaf node
										else:
											return 6 # approximately 2 were 6 out of 2 samples at leaf node
									else:
										return 2 # approximately 3 were 2 out of 3 samples at leaf node
								else:
									return 0 # approximately 4 were 0 out of 4 samples at leaf node
							else:
								if features[8][14] <= 10.5:
									pixels.append((8, 14))
									if features[8][10] <= 127.0:
										pixels.append((8, 10))
										return 4 # approximately 3 were 4 out of 3 samples at leaf node
									else:
										return 0 # approximately 1 were 0 out of 1 samples at leaf node
								else:
									return 9 # approximately 8 were 9 out of 8 samples at leaf node
						else:
							return 5 # approximately 6 were 5 out of 6 samples at leaf node
					else:
						if features[11][6] <= 126.0:
							pixels.append((11, 6))
							if features[4][23] <= 111.0:
								pixels.append((4, 23))
								if features[24][13] <= 63.0:
									pixels.append((24, 13))
									if features[11][16] <= 253.5:
										pixels.append((11, 16))
										return 2 # approximately 56 were 2 out of 56 samples at leaf node
									else:
										return 3 # approximately 1 were 3 out of 1 samples at leaf node
								else:
									return 3 # approximately 1 were 3 out of 1 samples at leaf node
							else:
								return 6 # approximately 2 were 6 out of 2 samples at leaf node
						else:
							if features[17][21] <= 167.5:
								pixels.append((17, 21))
								return 9 # approximately 2 were 9 out of 2 samples at leaf node
							else:
								return 4 # approximately 2 were 4 out of 2 samples at leaf node
				else:
					if features[13][23] <= 60.0:
						pixels.append((13, 23))
						if features[14][19] <= 44.5:
							pixels.append((14, 19))
							if features[5][17] <= 127.5:
								pixels.append((5, 17))
								if features[15][22] <= 20.0:
									pixels.append((15, 22))
									if features[16][17] <= 157.5:
										pixels.append((16, 17))
										return 5 # approximately 23 were 5 out of 23 samples at leaf node
									else:
										if features[6][20] <= 253.5:
											pixels.append((6, 20))
											return 9 # approximately 2 were 9 out of 2 samples at leaf node
										else:
											return 5 # approximately 1 were 5 out of 1 samples at leaf node
								else:
									if features[16][8] <= 126.0:
										pixels.append((16, 8))
										return 9 # approximately 1 were 9 out of 1 samples at leaf node
									else:
										return 6 # approximately 4 were 6 out of 4 samples at leaf node
							else:
								if features[14][12] <= 154.5:
									pixels.append((14, 12))
									return 6 # approximately 7 were 6 out of 7 samples at leaf node
								else:
									if features[12][15] <= 62.5:
										pixels.append((12, 15))
										return 2 # approximately 1 were 2 out of 1 samples at leaf node
									else:
										return 8 # approximately 3 were 8 out of 3 samples at leaf node
						else:
							if features[7][13] <= 193.0:
								pixels.append((7, 13))
								if features[23][23] <= 18.5:
									pixels.append((23, 23))
									return 4 # approximately 23 were 4 out of 23 samples at leaf node
								else:
									return 9 # approximately 1 were 9 out of 1 samples at leaf node
							else:
								if features[10][12] <= 24.5:
									pixels.append((10, 12))
									return 9 # approximately 8 were 9 out of 8 samples at leaf node
								else:
									if features[12][19] <= 124.5:
										pixels.append((12, 19))
										return 2 # approximately 2 were 2 out of 2 samples at leaf node
									else:
										if features[9][11] <= 245.5:
											pixels.append((9, 11))
											return 4 # approximately 1 were 4 out of 1 samples at leaf node
										else:
											return 0 # approximately 2 were 0 out of 2 samples at leaf node
					else:
						if features[12][14] <= 168.0:
							pixels.append((12, 14))
							if features[3][15] <= 32.0:
								pixels.append((3, 15))
								if features[24][14] <= 201.0:
									pixels.append((24, 14))
									return 0 # approximately 26 were 0 out of 26 samples at leaf node
								else:
									return 9 # approximately 1 were 9 out of 1 samples at leaf node
							else:
								if features[15][23] <= 29.0:
									pixels.append((15, 23))
									return 2 # approximately 1 were 2 out of 1 samples at leaf node
								else:
									if features[12][10] <= 59.5:
										pixels.append((12, 10))
										return 6 # approximately 1 were 6 out of 1 samples at leaf node
									else:
										return 4 # approximately 1 were 4 out of 1 samples at leaf node
						else:
							return 6 # approximately 9 were 6 out of 9 samples at leaf node
	else:
		if features[13][11] <= 0.5:
			pixels.append((13, 11))
			if features[19][18] <= 0.5:
				pixels.append((19, 18))
				if features[7][10] <= 0.5:
					pixels.append((7, 10))
					if features[16][9] <= 7.5:
						pixels.append((16, 9))
						if features[10][11] <= 41.5:
							pixels.append((10, 11))
							if features[21][19] <= 52.5:
								pixels.append((21, 19))
								if features[18][6] <= 1.0:
									pixels.append((18, 6))
									if features[10][20] <= 130.0:
										pixels.append((10, 20))
										if features[17][17] <= 2.0:
											pixels.append((17, 17))
											if features[5][10] <= 89.0:
												pixels.append((5, 10))
												if features[25][10] <= 105.5:
													pixels.append((25, 10))
													if features[8][22] <= 123.5:
														pixels.append((8, 22))
														if features[13][14] <= 141.5:
															pixels.append((13, 14))
															if features[10][19] <= 55.0:
																pixels.append((10, 19))
																if features[15][12] <= 125.5:
																	pixels.append((15, 12))
																	if features[6][20] <= 251.5:
																		pixels.append((6, 20))
																		if features[10][9] <= 3.0:
																			pixels.append((10, 9))
																			if features[5][12] <= 208.5:
																				pixels.append((5, 12))
																				return 1 # approximately 55 were 1 out of 55 samples at leaf node
																			else:
																				return 7 # approximately 1 were 7 out of 1 samples at leaf node
																		else:
																			if features[24][14] <= 127.0:
																				pixels.append((24, 14))
																				return 4 # approximately 1 were 4 out of 1 samples at leaf node
																			else:
																				return 7 # approximately 1 were 7 out of 1 samples at leaf node
																	else:
																		return 5 # approximately 2 were 5 out of 2 samples at leaf node
																else:
																	if features[16][11] <= 100.0:
																		pixels.append((16, 11))
																		if features[11][12] <= 98.5:
																			pixels.append((11, 12))
																			if features[13][14] <= 85.0:
																				pixels.append((13, 14))
																				return 3 # approximately 1 were 3 out of 1 samples at leaf node
																			else:
																				return 4 # approximately 1 were 4 out of 1 samples at leaf node
																		else:
																			if features[9][14] <= 184.0:
																				pixels.append((9, 14))
																				return 8 # approximately 1 were 8 out of 1 samples at leaf node
																			else:
																				return 5 # approximately 1 were 5 out of 1 samples at leaf node
																	else:
																		return 6 # approximately 2 were 6 out of 2 samples at leaf node
															else:
																if features[16][14] <= 142.5:
																	pixels.append((16, 14))
																	if features[18][10] <= 110.0:
																		pixels.append((18, 10))
																		if features[16][14] <= 103.0:
																			pixels.append((16, 14))
																			return 1 # approximately 1 were 1 out of 1 samples at leaf node
																		else:
																			return 8 # approximately 1 were 8 out of 1 samples at leaf node
																	else:
																		return 2 # approximately 2 were 2 out of 2 samples at leaf node
																else:
																	return 7 # approximately 4 were 7 out of 4 samples at leaf node
														else:
															if features[9][20] <= 63.5:
																pixels.append((9, 20))
																if features[12][18] <= 220.5:
																	pixels.append((12, 18))
																	if features[18][8] <= 40.0:
																		pixels.append((18, 8))
																		if features[6][10] <= 151.0:
																			pixels.append((6, 10))
																			if features[20][5] <= 103.0:
																				pixels.append((20, 5))
																				if features[18][17] <= 43.5:
																					pixels.append((18, 17))
																					if features[13][18] <= 5.0:
																						pixels.append((13, 18))
																						if features[3][20] <= 231.0:
																							pixels.append((3, 20))
																							if features[3][15] <= 202.0:
																								pixels.append((3, 15))
																								if features[15][17] <= 3.0:
																									pixels.append((15, 17))
																									if features[11][12] <= 254.0:
																										pixels.append((11, 12))
																										if features[12][12] <= 225.5:
																											pixels.append((12, 12))
																											if features[24][9] <= 254.5:
																												pixels.append((24, 9))
																												if features[4][11] <= 218.5:
																													pixels.append((4, 11))
																													if features[8][19] <= 253.5:
																														pixels.append((8, 19))
																														if features[17][16] <= 140.5:
																															pixels.append((17, 16))
																															if features[9][17] <= 254.5:
																																pixels.append((9, 17))
																																return 1 # approximately 3236 were 1 out of 3236 samples at leaf node
																															else:
																																if features[9][13] <= 152.0:
																																	pixels.append((9, 13))
																																	return 1 # approximately 70 were 1 out of 70 samples at leaf node
																																else:
																																	return 8 # approximately 1 were 8 out of 1 samples at leaf node
																														else:
																															if features[17][11] <= 44.5:
																																pixels.append((17, 11))
																																return 1 # approximately 118 were 1 out of 118 samples at leaf node
																															else:
																																if features[7][14] <= 193.0:
																																	pixels.append((7, 14))
																																	return 8 # approximately 2 were 8 out of 2 samples at leaf node
																																else:
																																	return 1 # approximately 1 were 1 out of 1 samples at leaf node
																													else:
																														if features[17][16] <= 20.0:
																															pixels.append((17, 16))
																															return 1 # approximately 26 were 1 out of 26 samples at leaf node
																														else:
																															return 8 # approximately 2 were 8 out of 2 samples at leaf node
																												else:
																													if features[23][11] <= 12.5:
																														pixels.append((23, 11))
																														return 1 # approximately 6 were 1 out of 6 samples at leaf node
																													else:
																														return 2 # approximately 1 were 2 out of 1 samples at leaf node
																											else:
																												if features[20][16] <= 70.5:
																													pixels.append((20, 16))
																													return 1 # approximately 5 were 1 out of 5 samples at leaf node
																												else:
																													return 3 # approximately 1 were 3 out of 1 samples at leaf node
																										else:
																											if features[4][17] <= 73.5:
																												pixels.append((4, 17))
																												return 1 # approximately 18 were 1 out of 18 samples at leaf node
																											else:
																												return 8 # approximately 2 were 8 out of 2 samples at leaf node
																									else:
																										if features[12][12] <= 191.5:
																											pixels.append((12, 12))
																											return 8 # approximately 1 were 8 out of 1 samples at leaf node
																										else:
																											return 1 # approximately 3 were 1 out of 3 samples at leaf node
																								else:
																									if features[9][15] <= 54.5:
																										pixels.append((9, 15))
																										return 3 # approximately 1 were 3 out of 1 samples at leaf node
																									else:
																										return 1 # approximately 3 were 1 out of 3 samples at leaf node
																							else:
																								if features[12][13] <= 201.0:
																									pixels.append((12, 13))
																									return 1 # approximately 3 were 1 out of 3 samples at leaf node
																								else:
																									return 6 # approximately 1 were 6 out of 1 samples at leaf node
																						else:
																							if features[5][18] <= 162.0:
																								pixels.append((5, 18))
																								return 1 # approximately 1 were 1 out of 1 samples at leaf node
																							else:
																								return 6 # approximately 1 were 6 out of 1 samples at leaf node
																					else:
																						if features[9][16] <= 65.0:
																							pixels.append((9, 16))
																							return 8 # approximately 2 were 8 out of 2 samples at leaf node
																						else:
																							return 1 # approximately 5 were 1 out of 5 samples at leaf node
																				else:
																					if features[20][12] <= 105.5:
																						pixels.append((20, 12))
																						return 1 # approximately 4 were 1 out of 4 samples at leaf node
																					else:
																						return 8 # approximately 2 were 8 out of 2 samples at leaf node
																			else:
																				return 5 # approximately 1 were 5 out of 1 samples at leaf node
																		else:
																			return 7 # approximately 1 were 7 out of 1 samples at leaf node
																	else:
																		if features[19][14] <= 117.0:
																			pixels.append((19, 14))
																			return 1 # approximately 12 were 1 out of 12 samples at leaf node
																		else:
																			if features[13][17] <= 1.0:
																				pixels.append((13, 17))
																				return 5 # approximately 2 were 5 out of 2 samples at leaf node
																			else:
																				return 8 # approximately 3 were 8 out of 3 samples at leaf node
																else:
																	if features[11][18] <= 182.5:
																		pixels.append((11, 18))
																		return 1 # approximately 1 were 1 out of 1 samples at leaf node
																	else:
																		return 8 # approximately 2 were 8 out of 2 samples at leaf node
															else:
																if features[7][14] <= 11.0:
																	pixels.append((7, 14))
																	return 1 # approximately 49 were 1 out of 49 samples at leaf node
																else:
																	if features[9][16] <= 47.5:
																		pixels.append((9, 16))
																		return 8 # approximately 9 were 8 out of 9 samples at leaf node
																	else:
																		if features[6][11] <= 120.0:
																			pixels.append((6, 11))
																			return 9 # approximately 1 were 9 out of 1 samples at leaf node
																		else:
																			return 3 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														if features[10][17] <= 11.0:
															pixels.append((10, 17))
															return 5 # approximately 4 were 5 out of 4 samples at leaf node
														else:
															if features[21][12] <= 14.5:
																pixels.append((21, 12))
																return 1 # approximately 1 were 1 out of 1 samples at leaf node
															else:
																return 8 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													if features[12][11] <= 1.5:
														pixels.append((12, 11))
														return 7 # approximately 4 were 7 out of 4 samples at leaf node
													else:
														return 9 # approximately 2 were 9 out of 2 samples at leaf node
											else:
												if features[13][16] <= 20.5:
													pixels.append((13, 16))
													return 1 # approximately 3 were 1 out of 3 samples at leaf node
												else:
													if features[4][13] <= 18.0:
														pixels.append((4, 13))
														if features[20][13] <= 77.5:
															pixels.append((20, 13))
															return 3 # approximately 3 were 3 out of 3 samples at leaf node
														else:
															return 7 # approximately 3 were 7 out of 3 samples at leaf node
													else:
														return 2 # approximately 4 were 2 out of 4 samples at leaf node
										else:
											if features[17][14] <= 144.5:
												pixels.append((17, 14))
												if features[16][12] <= 43.5:
													pixels.append((16, 12))
													if features[8][13] <= 245.5:
														pixels.append((8, 13))
														return 3 # approximately 14 were 3 out of 14 samples at leaf node
													else:
														if features[20][15] <= 213.5:
															pixels.append((20, 15))
															return 1 # approximately 2 were 1 out of 2 samples at leaf node
														else:
															return 5 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													if features[19][14] <= 72.0:
														pixels.append((19, 14))
														return 8 # approximately 7 were 8 out of 7 samples at leaf node
													else:
														if features[20][11] <= 187.0:
															pixels.append((20, 11))
															if features[10][12] <= 24.5:
																pixels.append((10, 12))
																return 2 # approximately 2 were 2 out of 2 samples at leaf node
															else:
																return 5 # approximately 1 were 5 out of 1 samples at leaf node
														else:
															return 6 # approximately 3 were 6 out of 3 samples at leaf node
											else:
												if features[13][14] <= 201.0:
													pixels.append((13, 14))
													if features[3][11] <= 42.5:
														pixels.append((3, 11))
														if features[22][11] <= 239.5:
															pixels.append((22, 11))
															if features[6][15] <= 11.5:
																pixels.append((6, 15))
																return 1 # approximately 1 were 1 out of 1 samples at leaf node
															else:
																if features[14][5] <= 14.5:
																	pixels.append((14, 5))
																	if features[14][16] <= 34.0:
																		pixels.append((14, 16))
																		if features[10][16] <= 5.5:
																			pixels.append((10, 16))
																			return 6 # approximately 1 were 6 out of 1 samples at leaf node
																		else:
																			return 5 # approximately 1 were 5 out of 1 samples at leaf node
																	else:
																		return 4 # approximately 1 were 4 out of 1 samples at leaf node
																else:
																	return 8 # approximately 1 were 8 out of 1 samples at leaf node
														else:
															return 7 # approximately 2 were 7 out of 2 samples at leaf node
													else:
														return 2 # approximately 2 were 2 out of 2 samples at leaf node
												else:
													if features[16][11] <= 170.5:
														pixels.append((16, 11))
														return 1 # approximately 47 were 1 out of 47 samples at leaf node
													else:
														return 6 # approximately 1 were 6 out of 1 samples at leaf node
									else:
										if features[23][10] <= 17.5:
											pixels.append((23, 10))
											if features[11][16] <= 78.0:
												pixels.append((11, 16))
												return 2 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												if features[9][22] <= 9.5:
													pixels.append((9, 22))
													return 1 # approximately 1 were 1 out of 1 samples at leaf node
												else:
													return 5 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											return 8 # approximately 14 were 8 out of 14 samples at leaf node
								else:
									if features[12][16] <= 209.0:
										pixels.append((12, 16))
										if features[15][10] <= 97.0:
											pixels.append((15, 10))
											if features[4][18] <= 200.0:
												pixels.append((4, 18))
												return 5 # approximately 21 were 5 out of 21 samples at leaf node
											else:
												return 1 # approximately 1 were 1 out of 1 samples at leaf node
										else:
											return 2 # approximately 2 were 2 out of 2 samples at leaf node
									else:
										if features[20][11] <= 232.5:
											pixels.append((20, 11))
											if features[5][12] <= 7.5:
												pixels.append((5, 12))
												return 7 # approximately 1 were 7 out of 1 samples at leaf node
											else:
												return 2 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											return 3 # approximately 3 were 3 out of 3 samples at leaf node
							else:
								if features[8][13] <= 101.0:
									pixels.append((8, 13))
									if features[18][20] <= 126.5:
										pixels.append((18, 20))
										return 2 # approximately 42 were 2 out of 42 samples at leaf node
									else:
										return 3 # approximately 1 were 3 out of 1 samples at leaf node
								else:
									if features[13][20] <= 45.5:
										pixels.append((13, 20))
										return 1 # approximately 8 were 1 out of 8 samples at leaf node
									else:
										return 9 # approximately 1 were 9 out of 1 samples at leaf node
						else:
							if features[10][8] <= 24.5:
								pixels.append((10, 8))
								if features[7][18] <= 11.0:
									pixels.append((7, 18))
									if features[17][14] <= 170.0:
										pixels.append((17, 14))
										if features[12][15] <= 51.5:
											pixels.append((12, 15))
											return 5 # approximately 5 were 5 out of 5 samples at leaf node
										else:
											if features[17][13] <= 16.0:
												pixels.append((17, 13))
												return 9 # approximately 3 were 9 out of 3 samples at leaf node
											else:
												if features[11][11] <= 178.5:
													pixels.append((11, 11))
													return 4 # approximately 2 were 4 out of 2 samples at leaf node
												else:
													return 8 # approximately 1 were 8 out of 1 samples at leaf node
									else:
										if features[8][17] <= 157.5:
											pixels.append((8, 17))
											if features[13][7] <= 14.5:
												pixels.append((13, 7))
												return 1 # approximately 40 were 1 out of 40 samples at leaf node
											else:
												if features[11][20] <= 127.5:
													pixels.append((11, 20))
													return 2 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													return 6 # approximately 1 were 6 out of 1 samples at leaf node
										else:
											if features[10][9] <= 2.5:
												pixels.append((10, 9))
												if features[10][13] <= 102.5:
													pixels.append((10, 13))
													return 9 # approximately 2 were 9 out of 2 samples at leaf node
												else:
													return 5 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												return 7 # approximately 3 were 7 out of 3 samples at leaf node
								else:
									if features[6][14] <= 13.5:
										pixels.append((6, 14))
										if features[25][10] <= 10.0:
											pixels.append((25, 10))
											if features[17][12] <= 249.5:
												pixels.append((17, 12))
												if features[15][12] <= 203.5:
													pixels.append((15, 12))
													if features[6][21] <= 18.0:
														pixels.append((6, 21))
														return 9 # approximately 3 were 9 out of 3 samples at leaf node
													else:
														if features[20][15] <= 125.0:
															pixels.append((20, 15))
															return 4 # approximately 1 were 4 out of 1 samples at leaf node
														else:
															return 5 # approximately 3 were 5 out of 3 samples at leaf node
												else:
													return 8 # approximately 3 were 8 out of 3 samples at leaf node
											else:
												return 1 # approximately 4 were 1 out of 4 samples at leaf node
										else:
											if features[24][6] <= 64.0:
												pixels.append((24, 6))
												return 7 # approximately 7 were 7 out of 7 samples at leaf node
											else:
												return 3 # approximately 1 were 3 out of 1 samples at leaf node
									else:
										if features[19][6] <= 3.0:
											pixels.append((19, 6))
											if features[22][17] <= 208.0:
												pixels.append((22, 17))
												if features[10][9] <= 41.0:
													pixels.append((10, 9))
													return 8 # approximately 28 were 8 out of 28 samples at leaf node
												else:
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												return 2 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											if features[5][17] <= 24.0:
												pixels.append((5, 17))
												return 2 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												return 5 # approximately 2 were 5 out of 2 samples at leaf node
							else:
								if features[11][6] <= 136.0:
									pixels.append((11, 6))
									if features[9][16] <= 31.5:
										pixels.append((9, 16))
										return 3 # approximately 2 were 3 out of 2 samples at leaf node
									else:
										return 7 # approximately 23 were 7 out of 23 samples at leaf node
								else:
									if features[23][11] <= 77.5:
										pixels.append((23, 11))
										return 2 # approximately 3 were 2 out of 3 samples at leaf node
									else:
										return 5 # approximately 1 were 5 out of 1 samples at leaf node
					else:
						if features[13][8] <= 4.0:
							pixels.append((13, 8))
							if features[11][13] <= 27.0:
								pixels.append((11, 13))
								if features[23][8] <= 9.0:
									pixels.append((23, 8))
									if features[21][9] <= 25.5:
										pixels.append((21, 9))
										if features[17][7] <= 74.5:
											pixels.append((17, 7))
											if features[14][13] <= 85.0:
												pixels.append((14, 13))
												return 7 # approximately 6 were 7 out of 6 samples at leaf node
											else:
												if features[16][15] <= 139.5:
													pixels.append((16, 15))
													return 1 # approximately 3 were 1 out of 3 samples at leaf node
												else:
													if features[10][16] <= 251.0:
														pixels.append((10, 16))
														return 5 # approximately 2 were 5 out of 2 samples at leaf node
													else:
														return 3 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											if features[14][7] <= 6.5:
												pixels.append((14, 7))
												if features[5][20] <= 5.0:
													pixels.append((5, 20))
													return 2 # approximately 9 were 2 out of 9 samples at leaf node
												else:
													return 5 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												if features[7][25] <= 32.5:
													pixels.append((7, 25))
													return 4 # approximately 2 were 4 out of 2 samples at leaf node
												else:
													return 5 # approximately 1 were 5 out of 1 samples at leaf node
									else:
										if features[16][16] <= 254.5:
											pixels.append((16, 16))
											return 2 # approximately 28 were 2 out of 28 samples at leaf node
										else:
											return 8 # approximately 1 were 8 out of 1 samples at leaf node
								else:
									if features[21][9] <= 151.0:
										pixels.append((21, 9))
										if features[14][16] <= 109.5:
											pixels.append((14, 16))
											if features[20][9] <= 1.0:
												pixels.append((20, 9))
												return 3 # approximately 2 were 3 out of 2 samples at leaf node
											else:
												if features[22][16] <= 83.0:
													pixels.append((22, 16))
													return 7 # approximately 2 were 7 out of 2 samples at leaf node
												else:
													return 2 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											return 8 # approximately 3 were 8 out of 3 samples at leaf node
									else:
										return 1 # approximately 17 were 1 out of 17 samples at leaf node
							else:
								if features[10][15] <= 215.5:
									pixels.append((10, 15))
									if features[18][18] <= 22.0:
										pixels.append((18, 18))
										return 8 # approximately 33 were 8 out of 33 samples at leaf node
									else:
										return 2 # approximately 1 were 2 out of 1 samples at leaf node
								else:
									if features[22][12] <= 41.5:
										pixels.append((22, 12))
										if features[20][16] <= 160.0:
											pixels.append((20, 16))
											return 1 # approximately 7 were 1 out of 7 samples at leaf node
										else:
											if features[4][11] <= 113.5:
												pixels.append((4, 11))
												return 4 # approximately 1 were 4 out of 1 samples at leaf node
											else:
												return 2 # approximately 1 were 2 out of 1 samples at leaf node
									else:
										if features[6][16] <= 202.5:
											pixels.append((6, 16))
											if features[22][19] <= 72.5:
												pixels.append((22, 19))
												if features[5][19] <= 126.5:
													pixels.append((5, 19))
													return 5 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													return 6 # approximately 1 were 6 out of 1 samples at leaf node
											else:
												return 2 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											return 8 # approximately 2 were 8 out of 2 samples at leaf node
						else:
							if features[16][18] <= 40.0:
								pixels.append((16, 18))
								if features[13][16] <= 59.0:
									pixels.append((13, 16))
									return 5 # approximately 15 were 5 out of 15 samples at leaf node
								else:
									if features[14][15] <= 251.0:
										pixels.append((14, 15))
										if features[17][9] <= 37.5:
											pixels.append((17, 9))
											if features[10][15] <= 121.0:
												pixels.append((10, 15))
												if features[19][22] <= 60.5:
													pixels.append((19, 22))
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													return 6 # approximately 1 were 6 out of 1 samples at leaf node
											else:
												return 9 # approximately 2 were 9 out of 2 samples at leaf node
										else:
											return 8 # approximately 2 were 8 out of 2 samples at leaf node
									else:
										return 4 # approximately 4 were 4 out of 4 samples at leaf node
							else:
								if features[8][20] <= 230.5:
									pixels.append((8, 20))
									if features[16][15] <= 45.5:
										pixels.append((16, 15))
										if features[20][10] <= 32.5:
											pixels.append((20, 10))
											return 2 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											return 6 # approximately 1 were 6 out of 1 samples at leaf node
									else:
										return 4 # approximately 23 were 4 out of 23 samples at leaf node
								else:
									return 9 # approximately 2 were 9 out of 2 samples at leaf node
				else:
					if features[19][10] <= 3.0:
						pixels.append((19, 10))
						if features[10][12] <= 111.5:
							pixels.append((10, 12))
							if features[13][13] <= 20.5:
								pixels.append((13, 13))
								if features[22][18] <= 3.5:
									pixels.append((22, 18))
									if features[15][8] <= 71.5:
										pixels.append((15, 8))
										if features[21][9] <= 6.0:
											pixels.append((21, 9))
											if features[17][14] <= 35.0:
												pixels.append((17, 14))
												return 9 # approximately 2 were 9 out of 2 samples at leaf node
											else:
												if features[12][16] <= 87.0:
													pixels.append((12, 16))
													if features[20][13] <= 224.5:
														pixels.append((20, 13))
														return 1 # approximately 2 were 1 out of 2 samples at leaf node
													else:
														return 7 # approximately 1 were 7 out of 1 samples at leaf node
												else:
													if features[18][16] <= 248.0:
														pixels.append((18, 16))
														return 7 # approximately 70 were 7 out of 70 samples at leaf node
													else:
														return 3 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											if features[18][13] <= 5.0:
												pixels.append((18, 13))
												if features[9][9] <= 136.0:
													pixels.append((9, 9))
													return 2 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													return 5 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												return 3 # approximately 2 were 3 out of 2 samples at leaf node
									else:
										if features[16][9] <= 252.5:
											pixels.append((16, 9))
											if features[14][8] <= 87.0:
												pixels.append((14, 8))
												return 2 # approximately 4 were 2 out of 4 samples at leaf node
											else:
												if features[8][24] <= 111.0:
													pixels.append((8, 24))
													if features[18][15] <= 58.5:
														pixels.append((18, 15))
														return 4 # approximately 1 were 4 out of 1 samples at leaf node
													else:
														return 9 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													return 5 # approximately 2 were 5 out of 2 samples at leaf node
										else:
											return 4 # approximately 3 were 4 out of 3 samples at leaf node
								else:
									if features[18][13] <= 89.0:
										pixels.append((18, 13))
										if features[23][15] <= 111.5:
											pixels.append((23, 15))
											if features[21][13] <= 72.5:
												pixels.append((21, 13))
												if features[15][17] <= 61.0:
													pixels.append((15, 17))
													return 9 # approximately 2 were 9 out of 2 samples at leaf node
												else:
													if features[25][18] <= 12.0:
														pixels.append((25, 18))
														return 8 # approximately 1 were 8 out of 1 samples at leaf node
													else:
														return 4 # approximately 1 were 4 out of 1 samples at leaf node
											else:
												return 1 # approximately 2 were 1 out of 2 samples at leaf node
										else:
											return 5 # approximately 5 were 5 out of 5 samples at leaf node
									else:
										return 2 # approximately 10 were 2 out of 10 samples at leaf node
							else:
								if features[20][12] <= 144.0:
									pixels.append((20, 12))
									if features[10][14] <= 242.0:
										pixels.append((10, 14))
										if features[15][8] <= 12.0:
											pixels.append((15, 8))
											if features[16][17] <= 239.5:
												pixels.append((16, 17))
												return 3 # approximately 33 were 3 out of 33 samples at leaf node
											else:
												if features[24][12] <= 48.0:
													pixels.append((24, 12))
													return 7 # approximately 2 were 7 out of 2 samples at leaf node
												else:
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											if features[4][21] <= 27.5:
												pixels.append((4, 21))
												return 9 # approximately 2 were 9 out of 2 samples at leaf node
											else:
												return 2 # approximately 1 were 2 out of 1 samples at leaf node
									else:
										if features[6][16] <= 97.5:
											pixels.append((6, 16))
											if features[15][16] <= 107.0:
												pixels.append((15, 16))
												if features[12][10] <= 81.0:
													pixels.append((12, 10))
													return 0 # approximately 1 were 0 out of 1 samples at leaf node
												else:
													return 4 # approximately 1 were 4 out of 1 samples at leaf node
											else:
												return 7 # approximately 2 were 7 out of 2 samples at leaf node
										else:
											return 1 # approximately 2 were 1 out of 2 samples at leaf node
								else:
									if features[11][10] <= 13.0:
										pixels.append((11, 10))
										if features[19][11] <= 62.0:
											pixels.append((19, 11))
											if features[5][15] <= 152.5:
												pixels.append((5, 15))
												return 7 # approximately 3 were 7 out of 3 samples at leaf node
											else:
												return 1 # approximately 2 were 1 out of 2 samples at leaf node
										else:
											if features[22][10] <= 147.0:
												pixels.append((22, 10))
												return 2 # approximately 9 were 2 out of 9 samples at leaf node
											else:
												return 7 # approximately 1 were 7 out of 1 samples at leaf node
									else:
										return 8 # approximately 4 were 8 out of 4 samples at leaf node
						else:
							if features[9][17] <= 17.0:
								pixels.append((9, 17))
								return 1 # approximately 42 were 1 out of 42 samples at leaf node
							else:
								if features[17][13] <= 203.5:
									pixels.append((17, 13))
									if features[10][17] <= 105.5:
										pixels.append((10, 17))
										return 9 # approximately 2 were 9 out of 2 samples at leaf node
									else:
										if features[9][23] <= 58.5:
											pixels.append((9, 23))
											if features[10][17] <= 211.0:
												pixels.append((10, 17))
												return 1 # approximately 1 were 1 out of 1 samples at leaf node
											else:
												return 7 # approximately 1 were 7 out of 1 samples at leaf node
										else:
											return 5 # approximately 1 were 5 out of 1 samples at leaf node
								else:
									return 8 # approximately 3 were 8 out of 3 samples at leaf node
					else:
						if features[11][12] <= 30.5:
							pixels.append((11, 12))
							if features[13][8] <= 22.0:
								pixels.append((13, 8))
								if features[5][13] <= 4.0:
									pixels.append((5, 13))
									if features[16][15] <= 87.5:
										pixels.append((16, 15))
										return 2 # approximately 13 were 2 out of 13 samples at leaf node
									else:
										if features[20][9] <= 141.5:
											pixels.append((20, 9))
											return 7 # approximately 12 were 7 out of 12 samples at leaf node
										else:
											if features[15][16] <= 248.0:
												pixels.append((15, 16))
												return 2 # approximately 5 were 2 out of 5 samples at leaf node
											else:
												return 7 # approximately 1 were 7 out of 1 samples at leaf node
								else:
									if features[8][11] <= 254.5:
										pixels.append((8, 11))
										if features[23][11] <= 253.5:
											pixels.append((23, 11))
											return 2 # approximately 80 were 2 out of 80 samples at leaf node
										else:
											if features[16][8] <= 64.0:
												pixels.append((16, 8))
												return 7 # approximately 1 were 7 out of 1 samples at leaf node
											else:
												return 2 # approximately 1 were 2 out of 1 samples at leaf node
									else:
										return 1 # approximately 1 were 1 out of 1 samples at leaf node
							else:
								if features[7][17] <= 13.5:
									pixels.append((7, 17))
									return 6 # approximately 10 were 6 out of 10 samples at leaf node
								else:
									if features[17][22] <= 89.5:
										pixels.append((17, 22))
										return 8 # approximately 2 were 8 out of 2 samples at leaf node
									else:
										if features[13][16] <= 95.5:
											pixels.append((13, 16))
											if features[20][19] <= 75.0:
												pixels.append((20, 19))
												return 2 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												return 0 # approximately 1 were 0 out of 1 samples at leaf node
										else:
											return 9 # approximately 1 were 9 out of 1 samples at leaf node
						else:
							if features[23][11] <= 19.0:
								pixels.append((23, 11))
								if features[19][9] <= 190.5:
									pixels.append((19, 9))
									return 2 # approximately 6 were 2 out of 6 samples at leaf node
								else:
									if features[24][19] <= 33.5:
										pixels.append((24, 19))
										return 1 # approximately 1 were 1 out of 1 samples at leaf node
									else:
										return 9 # approximately 1 were 9 out of 1 samples at leaf node
							else:
								if features[25][9] <= 70.0:
									pixels.append((25, 9))
									return 8 # approximately 29 were 8 out of 29 samples at leaf node
								else:
									return 7 # approximately 1 were 7 out of 1 samples at leaf node
			else:
				if features[13][8] <= 2.0:
					pixels.append((13, 8))
					if features[23][15] <= 1.5:
						pixels.append((23, 15))
						if features[16][12] <= 1.0:
							pixels.append((16, 12))
							if features[10][18] <= 29.0:
								pixels.append((10, 18))
								if features[18][15] <= 38.5:
									pixels.append((18, 15))
									if features[8][12] <= 111.0:
										pixels.append((8, 12))
										if features[23][9] <= 46.0:
											pixels.append((23, 9))
											return 2 # approximately 2 were 2 out of 2 samples at leaf node
										else:
											return 3 # approximately 2 were 3 out of 2 samples at leaf node
									else:
										return 5 # approximately 3 were 5 out of 3 samples at leaf node
								else:
									if features[4][9] <= 116.5:
										pixels.append((4, 9))
										if features[22][14] <= 205.5:
											pixels.append((22, 14))
											if features[12][19] <= 116.5:
												pixels.append((12, 19))
												return 1 # approximately 31 were 1 out of 31 samples at leaf node
											else:
												return 6 # approximately 1 were 6 out of 1 samples at leaf node
										else:
											if features[23][11] <= 126.0:
												pixels.append((23, 11))
												return 2 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												return 5 # approximately 1 were 5 out of 1 samples at leaf node
									else:
										return 2 # approximately 4 were 2 out of 4 samples at leaf node
							else:
								if features[6][20] <= 16.0:
									pixels.append((6, 20))
									if features[15][12] <= 70.5:
										pixels.append((15, 12))
										return 6 # approximately 6 were 6 out of 6 samples at leaf node
									else:
										return 2 # approximately 2 were 2 out of 2 samples at leaf node
								else:
									return 3 # approximately 6 were 3 out of 6 samples at leaf node
						else:
							if features[13][6] <= 123.5:
								pixels.append((13, 6))
								if features[20][9] <= 5.5:
									pixels.append((20, 9))
									if features[19][20] <= 13.5:
										pixels.append((19, 20))
										if features[10][17] <= 94.5:
											pixels.append((10, 17))
											if features[19][17] <= 10.5:
												pixels.append((19, 17))
												return 1 # approximately 4 were 1 out of 4 samples at leaf node
											else:
												if features[5][13] <= 42.5:
													pixels.append((5, 13))
													if features[20][15] <= 24.5:
														pixels.append((20, 15))
														if features[6][7] <= 43.0:
															pixels.append((6, 7))
															return 4 # approximately 1 were 4 out of 1 samples at leaf node
														else:
															if features[9][14] <= 151.0:
																pixels.append((9, 14))
																return 2 # approximately 1 were 2 out of 1 samples at leaf node
															else:
																return 3 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														return 6 # approximately 6 were 6 out of 6 samples at leaf node
												else:
													if features[9][10] <= 227.5:
														pixels.append((9, 10))
														return 2 # approximately 7 were 2 out of 7 samples at leaf node
													else:
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											if features[14][12] <= 2.0:
												pixels.append((14, 12))
												return 7 # approximately 2 were 7 out of 2 samples at leaf node
											else:
												return 3 # approximately 8 were 3 out of 8 samples at leaf node
									else:
										if features[24][19] <= 6.5:
											pixels.append((24, 19))
											if features[26][11] <= 85.0:
												pixels.append((26, 11))
												return 2 # approximately 44 were 2 out of 44 samples at leaf node
											else:
												return 7 # approximately 1 were 7 out of 1 samples at leaf node
										else:
											if features[18][16] <= 57.0:
												pixels.append((18, 16))
												return 7 # approximately 1 were 7 out of 1 samples at leaf node
											else:
												return 3 # approximately 2 were 3 out of 2 samples at leaf node
								else:
									if features[12][12] <= 107.0:
										pixels.append((12, 12))
										if features[24][6] <= 173.5:
											pixels.append((24, 6))
											if features[9][12] <= 254.5:
												pixels.append((9, 12))
												if features[23][13] <= 154.5:
													pixels.append((23, 13))
													if features[22][18] <= 253.5:
														pixels.append((22, 18))
														return 2 # approximately 345 were 2 out of 345 samples at leaf node
													else:
														if features[4][13] <= 127.5:
															pixels.append((4, 13))
															return 1 # approximately 1 were 1 out of 1 samples at leaf node
														else:
															return 2 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													if features[16][7] <= 127.0:
														pixels.append((16, 7))
														return 1 # approximately 1 were 1 out of 1 samples at leaf node
													else:
														return 2 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												return 6 # approximately 1 were 6 out of 1 samples at leaf node
										else:
											return 7 # approximately 1 were 7 out of 1 samples at leaf node
									else:
										if features[13][15] <= 180.5:
											pixels.append((13, 15))
											return 1 # approximately 2 were 1 out of 2 samples at leaf node
										else:
											if features[9][18] <= 124.5:
												pixels.append((9, 18))
												return 2 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												return 8 # approximately 1 were 8 out of 1 samples at leaf node
							else:
								if features[19][13] <= 11.5:
									pixels.append((19, 13))
									if features[11][6] <= 252.5:
										pixels.append((11, 6))
										return 4 # approximately 3 were 4 out of 3 samples at leaf node
									else:
										return 9 # approximately 1 were 9 out of 1 samples at leaf node
								else:
									return 6 # approximately 12 were 6 out of 12 samples at leaf node
					else:
						if features[11][12] <= 41.0:
							pixels.append((11, 12))
							if features[17][17] <= 13.0:
								pixels.append((17, 17))
								if features[21][11] <= 24.0:
									pixels.append((21, 11))
									if features[12][15] <= 147.5:
										pixels.append((12, 15))
										if features[14][11] <= 69.5:
											pixels.append((14, 11))
											return 3 # approximately 2 were 3 out of 2 samples at leaf node
										else:
											return 5 # approximately 1 were 5 out of 1 samples at leaf node
									else:
										return 1 # approximately 5 were 1 out of 5 samples at leaf node
								else:
									if features[24][18] <= 15.5:
										pixels.append((24, 18))
										if features[19][18] <= 6.0:
											pixels.append((19, 18))
											return 1 # approximately 1 were 1 out of 1 samples at leaf node
										else:
											return 2 # approximately 39 were 2 out of 39 samples at leaf node
									else:
										return 9 # approximately 1 were 9 out of 1 samples at leaf node
							else:
								if features[14][13] <= 7.5:
									pixels.append((14, 13))
									if features[20][7] <= 18.5:
										pixels.append((20, 7))
										if features[22][17] <= 14.0:
											pixels.append((22, 17))
											return 7 # approximately 8 were 7 out of 8 samples at leaf node
										else:
											if features[23][11] <= 35.5:
												pixels.append((23, 11))
												return 4 # approximately 1 were 4 out of 1 samples at leaf node
											else:
												if features[23][15] <= 203.5:
													pixels.append((23, 15))
													return 1 # approximately 1 were 1 out of 1 samples at leaf node
												else:
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
									else:
										return 2 # approximately 5 were 2 out of 5 samples at leaf node
								else:
									if features[13][20] <= 53.0:
										pixels.append((13, 20))
										if features[10][13] <= 214.0:
											pixels.append((10, 13))
											if features[25][17] <= 232.5:
												pixels.append((25, 17))
												if features[18][8] <= 250.5:
													pixels.append((18, 8))
													return 3 # approximately 74 were 3 out of 74 samples at leaf node
												else:
													return 8 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												return 7 # approximately 1 were 7 out of 1 samples at leaf node
										else:
											if features[5][17] <= 112.0:
												pixels.append((5, 17))
												return 1 # approximately 1 were 1 out of 1 samples at leaf node
											else:
												return 8 # approximately 1 were 8 out of 1 samples at leaf node
									else:
										if features[16][16] <= 104.0:
											pixels.append((16, 16))
											return 9 # approximately 1 were 9 out of 1 samples at leaf node
										else:
											return 2 # approximately 2 were 2 out of 2 samples at leaf node
						else:
							if features[19][15] <= 231.5:
								pixels.append((19, 15))
								if features[10][14] <= 96.0:
									pixels.append((10, 14))
									if features[22][7] <= 93.5:
										pixels.append((22, 7))
										if features[13][13] <= 47.5:
											pixels.append((13, 13))
											if features[11][14] <= 5.0:
												pixels.append((11, 14))
												return 9 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												return 3 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											if features[14][15] <= 4.5:
												pixels.append((14, 15))
												return 5 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												return 8 # approximately 43 were 8 out of 43 samples at leaf node
									else:
										if features[14][15] <= 105.0:
											pixels.append((14, 15))
											return 2 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											return 5 # approximately 3 were 5 out of 3 samples at leaf node
								else:
									if features[16][14] <= 152.0:
										pixels.append((16, 14))
										return 3 # approximately 6 were 3 out of 6 samples at leaf node
									else:
										if features[12][17] <= 22.0:
											pixels.append((12, 17))
											return 5 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											return 8 # approximately 1 were 8 out of 1 samples at leaf node
							else:
								if features[17][19] <= 3.5:
									pixels.append((17, 19))
									return 1 # approximately 24 were 1 out of 24 samples at leaf node
								else:
									if features[16][10] <= 2.0:
										pixels.append((16, 10))
										return 3 # approximately 1 were 3 out of 1 samples at leaf node
									else:
										return 7 # approximately 1 were 7 out of 1 samples at leaf node
				else:
					if features[20][12] <= 53.5:
						pixels.append((20, 12))
						if features[14][19] <= 2.5:
							pixels.append((14, 19))
							if features[13][15] <= 19.0:
								pixels.append((13, 15))
								if features[20][10] <= 180.5:
									pixels.append((20, 10))
									return 5 # approximately 47 were 5 out of 47 samples at leaf node
								else:
									return 6 # approximately 2 were 6 out of 2 samples at leaf node
							else:
								if features[11][21] <= 48.0:
									pixels.append((11, 21))
									if features[15][10] <= 106.5:
										pixels.append((15, 10))
										if features[9][14] <= 72.5:
											pixels.append((9, 14))
											return 3 # approximately 3 were 3 out of 3 samples at leaf node
										else:
											if features[14][22] <= 28.5:
												pixels.append((14, 22))
												if features[9][14] <= 208.0:
													pixels.append((9, 14))
													return 7 # approximately 1 were 7 out of 1 samples at leaf node
												else:
													return 2 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												return 0 # approximately 2 were 0 out of 2 samples at leaf node
									else:
										if features[20][18] <= 219.5:
											pixels.append((20, 18))
											return 8 # approximately 6 were 8 out of 6 samples at leaf node
										else:
											if features[25][16] <= 23.5:
												pixels.append((25, 16))
												return 2 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												return 5 # approximately 1 were 5 out of 1 samples at leaf node
								else:
									return 6 # approximately 6 were 6 out of 6 samples at leaf node
						else:
							if features[7][15] <= 8.0:
								pixels.append((7, 15))
								if features[6][16] <= 161.5:
									pixels.append((6, 16))
									return 4 # approximately 35 were 4 out of 35 samples at leaf node
								else:
									if features[13][15] <= 33.0:
										pixels.append((13, 15))
										return 0 # approximately 1 were 0 out of 1 samples at leaf node
									else:
										return 9 # approximately 1 were 9 out of 1 samples at leaf node
							else:
								if features[12][10] <= 100.0:
									pixels.append((12, 10))
									return 9 # approximately 11 were 9 out of 11 samples at leaf node
								else:
									if features[9][10] <= 167.5:
										pixels.append((9, 10))
										return 4 # approximately 1 were 4 out of 1 samples at leaf node
									else:
										return 0 # approximately 1 were 0 out of 1 samples at leaf node
					else:
						if features[8][15] <= 40.5:
							pixels.append((8, 15))
							if features[21][8] <= 252.5:
								pixels.append((21, 8))
								if features[7][20] <= 241.5:
									pixels.append((7, 20))
									return 6 # approximately 96 were 6 out of 96 samples at leaf node
								else:
									if features[10][17] <= 99.0:
										pixels.append((10, 17))
										return 2 # approximately 1 were 2 out of 1 samples at leaf node
									else:
										return 8 # approximately 1 were 8 out of 1 samples at leaf node
							else:
								return 5 # approximately 2 were 5 out of 2 samples at leaf node
						else:
							if features[15][23] <= 19.0:
								pixels.append((15, 23))
								if features[12][16] <= 1.0:
									pixels.append((12, 16))
									if features[15][14] <= 125.0:
										pixels.append((15, 14))
										return 6 # approximately 4 were 6 out of 4 samples at leaf node
									else:
										if features[15][19] <= 2.0:
											pixels.append((15, 19))
											return 5 # approximately 3 were 5 out of 3 samples at leaf node
										else:
											return 2 # approximately 2 were 2 out of 2 samples at leaf node
								else:
									if features[15][10] <= 14.5:
										pixels.append((15, 10))
										return 2 # approximately 1 were 2 out of 1 samples at leaf node
									else:
										return 8 # approximately 7 were 8 out of 7 samples at leaf node
							else:
								return 0 # approximately 4 were 0 out of 4 samples at leaf node
		else:
			if features[12][15] <= 23.5:
				pixels.append((12, 15))
				if features[18][11] <= 52.5:
					pixels.append((18, 11))
					if features[15][20] <= 3.0:
						pixels.append((15, 20))
						if features[5][10] <= 77.5:
							pixels.append((5, 10))
							if features[18][9] <= 213.5:
								pixels.append((18, 9))
								if features[7][21] <= 2.5:
									pixels.append((7, 21))
									if features[12][14] <= 139.0:
										pixels.append((12, 14))
										if features[8][7] <= 48.5:
											pixels.append((8, 7))
											if features[13][16] <= 35.0:
												pixels.append((13, 16))
												if features[4][11] <= 103.0:
													pixels.append((4, 11))
													if features[6][11] <= 138.0:
														pixels.append((6, 11))
														if features[13][19] <= 26.0:
															pixels.append((13, 19))
															if features[16][20] <= 37.5:
																pixels.append((16, 20))
																if features[4][13] <= 160.5:
																	pixels.append((4, 13))
																	if features[19][12] <= 254.5:
																		pixels.append((19, 12))
																		if features[24][13] <= 254.5:
																			pixels.append((24, 13))
																			if features[23][7] <= 253.5:
																				pixels.append((23, 7))
																				if features[8][10] <= 252.5:
																					pixels.append((8, 10))
																					if features[18][12] <= 188.5:
																						pixels.append((18, 12))
																						return 5 # approximately 188 were 5 out of 188 samples at leaf node
																					else:
																						if features[9][14] <= 219.5:
																							pixels.append((9, 14))
																							return 5 # approximately 3 were 5 out of 3 samples at leaf node
																						else:
																							return 8 # approximately 1 were 8 out of 1 samples at leaf node
																				else:
																					if features[20][17] <= 105.5:
																						pixels.append((20, 17))
																						return 3 # approximately 1 were 3 out of 1 samples at leaf node
																					else:
																						return 5 # approximately 3 were 5 out of 3 samples at leaf node
																			else:
																				return 3 # approximately 1 were 3 out of 1 samples at leaf node
																		else:
																			return 3 # approximately 1 were 3 out of 1 samples at leaf node
																	else:
																		return 6 # approximately 1 were 6 out of 1 samples at leaf node
																else:
																	if features[19][9] <= 56.0:
																		pixels.append((19, 9))
																		return 3 # approximately 2 were 3 out of 2 samples at leaf node
																	else:
																		return 5 # approximately 1 were 5 out of 1 samples at leaf node
															else:
																if features[12][11] <= 170.5:
																	pixels.append((12, 11))
																	return 6 # approximately 2 were 6 out of 2 samples at leaf node
																else:
																	return 2 # approximately 1 were 2 out of 1 samples at leaf node
														else:
															if features[20][14] <= 160.0:
																pixels.append((20, 14))
																if features[19][7] <= 85.0:
																	pixels.append((19, 7))
																	return 4 # approximately 1 were 4 out of 1 samples at leaf node
																else:
																	return 2 # approximately 1 were 2 out of 1 samples at leaf node
															else:
																return 9 # approximately 2 were 9 out of 2 samples at leaf node
													else:
														if features[11][13] <= 101.0:
															pixels.append((11, 13))
															if features[23][19] <= 110.5:
																pixels.append((23, 19))
																return 5 # approximately 18 were 5 out of 18 samples at leaf node
															else:
																if features[5][12] <= 127.5:
																	pixels.append((5, 12))
																	return 0 # approximately 1 were 0 out of 1 samples at leaf node
																else:
																	return 1 # approximately 1 were 1 out of 1 samples at leaf node
														else:
															if features[18][15] <= 250.5:
																pixels.append((18, 15))
																return 3 # approximately 9 were 3 out of 9 samples at leaf node
															else:
																return 1 # approximately 2 were 1 out of 2 samples at leaf node
												else:
													return 3 # approximately 5 were 3 out of 5 samples at leaf node
											else:
												if features[23][15] <= 1.0:
													pixels.append((23, 15))
													if features[5][19] <= 30.0:
														pixels.append((5, 19))
														if features[24][13] <= 115.0:
															pixels.append((24, 13))
															return 2 # approximately 1 were 2 out of 1 samples at leaf node
														else:
															return 9 # approximately 1 were 9 out of 1 samples at leaf node
													else:
														return 4 # approximately 3 were 4 out of 3 samples at leaf node
												else:
													return 8 # approximately 4 were 8 out of 4 samples at leaf node
										else:
											if features[22][18] <= 26.5:
												pixels.append((22, 18))
												if features[12][13] <= 146.5:
													pixels.append((12, 13))
													if features[14][14] <= 46.0:
														pixels.append((14, 14))
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														return 8 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													return 2 # approximately 2 were 2 out of 2 samples at leaf node
											else:
												if features[15][10] <= 254.0:
													pixels.append((15, 10))
													return 3 # approximately 10 were 3 out of 10 samples at leaf node
												else:
													return 5 # approximately 1 were 5 out of 1 samples at leaf node
									else:
										if features[9][13] <= 229.5:
											pixels.append((9, 13))
											if features[6][11] <= 12.0:
												pixels.append((6, 11))
												if features[7][12] <= 2.0:
													pixels.append((7, 12))
													return 5 # approximately 3 were 5 out of 3 samples at leaf node
												else:
													return 2 # approximately 2 were 2 out of 2 samples at leaf node
											else:
												return 3 # approximately 5 were 3 out of 5 samples at leaf node
										else:
											return 1 # approximately 13 were 1 out of 13 samples at leaf node
								else:
									if features[12][17] <= 178.5:
										pixels.append((12, 17))
										return 5 # approximately 560 were 5 out of 560 samples at leaf node
									else:
										if features[8][19] <= 6.5:
											pixels.append((8, 19))
											return 8 # approximately 2 were 8 out of 2 samples at leaf node
										else:
											if features[9][14] <= 126.0:
												pixels.append((9, 14))
												return 4 # approximately 1 were 4 out of 1 samples at leaf node
											else:
												return 9 # approximately 1 were 9 out of 1 samples at leaf node
							else:
								if features[4][20] <= 8.0:
									pixels.append((4, 20))
									if features[23][16] <= 7.5:
										pixels.append((23, 16))
										if features[11][12] <= 98.0:
											pixels.append((11, 12))
											return 8 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											return 5 # approximately 7 were 5 out of 7 samples at leaf node
									else:
										if features[14][8] <= 228.0:
											pixels.append((14, 8))
											return 8 # approximately 7 were 8 out of 7 samples at leaf node
										else:
											if features[7][15] <= 131.5:
												pixels.append((7, 15))
												return 0 # approximately 1 were 0 out of 1 samples at leaf node
											else:
												return 6 # approximately 1 were 6 out of 1 samples at leaf node
								else:
									if features[5][12] <= 121.0:
										pixels.append((5, 12))
										return 6 # approximately 16 were 6 out of 16 samples at leaf node
									else:
										return 8 # approximately 1 were 8 out of 1 samples at leaf node
						else:
							if features[9][10] <= 31.0:
								pixels.append((9, 10))
								if features[16][16] <= 80.5:
									pixels.append((16, 16))
									if features[16][13] <= 253.5:
										pixels.append((16, 13))
										return 8 # approximately 3 were 8 out of 3 samples at leaf node
									else:
										if features[17][11] <= 77.5:
											pixels.append((17, 11))
											return 1 # approximately 1 were 1 out of 1 samples at leaf node
										else:
											return 2 # approximately 1 were 2 out of 1 samples at leaf node
								else:
									return 3 # approximately 42 were 3 out of 42 samples at leaf node
							else:
								if features[12][12] <= 248.5:
									pixels.append((12, 12))
									return 5 # approximately 17 were 5 out of 17 samples at leaf node
								else:
									if features[5][11] <= 127.0:
										pixels.append((5, 11))
										return 0 # approximately 2 were 0 out of 2 samples at leaf node
									else:
										if features[7][9] <= 242.0:
											pixels.append((7, 9))
											return 1 # approximately 2 were 1 out of 2 samples at leaf node
										else:
											return 3 # approximately 1 were 3 out of 1 samples at leaf node
					else:
						if features[16][16] <= 32.5:
							pixels.append((16, 16))
							if features[11][10] <= 3.5:
								pixels.append((11, 10))
								if features[19][18] <= 112.0:
									pixels.append((19, 18))
									return 9 # approximately 1 were 9 out of 1 samples at leaf node
								else:
									return 2 # approximately 1 were 2 out of 1 samples at leaf node
							else:
								return 0 # approximately 15 were 0 out of 15 samples at leaf node
						else:
							if features[4][14] <= 5.0:
								pixels.append((4, 14))
								if features[13][19] <= 54.5:
									pixels.append((13, 19))
									if features[18][22] <= 68.5:
										pixels.append((18, 22))
										if features[13][8] <= 72.0:
											pixels.append((13, 8))
											if features[15][18] <= 131.5:
												pixels.append((15, 18))
												return 2 # approximately 4 were 2 out of 4 samples at leaf node
											else:
												if features[16][20] <= 214.5:
													pixels.append((16, 20))
													return 6 # approximately 1 were 6 out of 1 samples at leaf node
												else:
													return 5 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											if features[22][12] <= 206.0:
												pixels.append((22, 12))
												return 9 # approximately 4 were 9 out of 4 samples at leaf node
											else:
												if features[7][19] <= 14.0:
													pixels.append((7, 19))
													return 4 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													if features[7][15] <= 234.5:
														pixels.append((7, 15))
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														if features[24][9] <= 68.5:
															pixels.append((24, 9))
															return 6 # approximately 1 were 6 out of 1 samples at leaf node
														else:
															return 0 # approximately 1 were 0 out of 1 samples at leaf node
									else:
										return 3 # approximately 3 were 3 out of 3 samples at leaf node
								else:
									if features[22][7] <= 1.5:
										pixels.append((22, 7))
										return 4 # approximately 10 were 4 out of 10 samples at leaf node
									else:
										if features[5][15] <= 187.0:
											pixels.append((5, 15))
											return 2 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											return 9 # approximately 1 were 9 out of 1 samples at leaf node
							else:
								if features[19][21] <= 241.0:
									pixels.append((19, 21))
									return 2 # approximately 20 were 2 out of 20 samples at leaf node
								else:
									return 5 # approximately 1 were 5 out of 1 samples at leaf node
				else:
					if features[9][20] <= 11.5:
						pixels.append((9, 20))
						if features[23][13] <= 18.0:
							pixels.append((23, 13))
							if features[21][13] <= 32.0:
								pixels.append((21, 13))
								if features[17][14] <= 138.0:
									pixels.append((17, 14))
									if features[6][23] <= 128.0:
										pixels.append((6, 23))
										return 6 # approximately 6 were 6 out of 6 samples at leaf node
									else:
										return 5 # approximately 1 were 5 out of 1 samples at leaf node
								else:
									if features[8][16] <= 50.0:
										pixels.append((8, 16))
										if features[3][14] <= 130.0:
											pixels.append((3, 14))
											return 2 # approximately 7 were 2 out of 7 samples at leaf node
										else:
											return 6 # approximately 1 were 6 out of 1 samples at leaf node
									else:
										return 5 # approximately 4 were 5 out of 4 samples at leaf node
							else:
								if features[22][19] <= 247.5:
									pixels.append((22, 19))
									if features[23][7] <= 4.0:
										pixels.append((23, 7))
										return 6 # approximately 124 were 6 out of 124 samples at leaf node
									else:
										return 8 # approximately 1 were 8 out of 1 samples at leaf node
								else:
									if features[12][14] <= 95.0:
										pixels.append((12, 14))
										return 5 # approximately 1 were 5 out of 1 samples at leaf node
									else:
										return 2 # approximately 1 were 2 out of 1 samples at leaf node
						else:
							if features[4][19] <= 74.5:
								pixels.append((4, 19))
								if features[6][18] <= 212.5:
									pixels.append((6, 18))
									if features[19][11] <= 120.0:
										pixels.append((19, 11))
										if features[14][15] <= 84.5:
											pixels.append((14, 15))
											if features[17][16] <= 62.0:
												pixels.append((17, 16))
												return 1 # approximately 1 were 1 out of 1 samples at leaf node
											else:
												return 5 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											return 4 # approximately 2 were 4 out of 2 samples at leaf node
									else:
										return 8 # approximately 11 were 8 out of 11 samples at leaf node
								else:
									if features[20][15] <= 252.5:
										pixels.append((20, 15))
										return 5 # approximately 9 were 5 out of 9 samples at leaf node
									else:
										if features[24][14] <= 17.0:
											pixels.append((24, 14))
											return 6 # approximately 1 were 6 out of 1 samples at leaf node
										else:
											return 8 # approximately 2 were 8 out of 2 samples at leaf node
							else:
								if features[13][11] <= 229.5:
									pixels.append((13, 11))
									return 8 # approximately 2 were 8 out of 2 samples at leaf node
								else:
									return 6 # approximately 11 were 6 out of 11 samples at leaf node
					else:
						if features[22][14] <= 2.5:
							pixels.append((22, 14))
							if features[15][21] <= 2.0:
								pixels.append((15, 21))
								if features[24][18] <= 154.0:
									pixels.append((24, 18))
									return 5 # approximately 32 were 5 out of 32 samples at leaf node
								else:
									return 8 # approximately 1 were 8 out of 1 samples at leaf node
							else:
								if features[12][8] <= 87.5:
									pixels.append((12, 8))
									return 2 # approximately 6 were 2 out of 6 samples at leaf node
								else:
									if features[17][9] <= 57.0:
										pixels.append((17, 9))
										return 0 # approximately 2 were 0 out of 2 samples at leaf node
									else:
										return 4 # approximately 2 were 4 out of 2 samples at leaf node
						else:
							if features[17][9] <= 70.0:
								pixels.append((17, 9))
								if features[9][13] <= 242.5:
									pixels.append((9, 13))
									return 8 # approximately 18 were 8 out of 18 samples at leaf node
								else:
									if features[9][22] <= 1.0:
										pixels.append((9, 22))
										if features[23][13] <= 252.5:
											pixels.append((23, 13))
											return 8 # approximately 3 were 8 out of 3 samples at leaf node
										else:
											if features[20][18] <= 82.5:
												pixels.append((20, 18))
												return 1 # approximately 1 were 1 out of 1 samples at leaf node
											else:
												return 6 # approximately 1 were 6 out of 1 samples at leaf node
									else:
										return 5 # approximately 4 were 5 out of 4 samples at leaf node
							else:
								if features[17][16] <= 102.5:
									pixels.append((17, 16))
									return 0 # approximately 4 were 0 out of 4 samples at leaf node
								else:
									if features[12][19] <= 13.5:
										pixels.append((12, 19))
										if features[14][15] <= 11.5:
											pixels.append((14, 15))
											return 6 # approximately 5 were 6 out of 5 samples at leaf node
										else:
											if features[10][21] <= 100.0:
												pixels.append((10, 21))
												return 8 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												return 5 # approximately 1 were 5 out of 1 samples at leaf node
									else:
										return 2 # approximately 3 were 2 out of 3 samples at leaf node
			else:
				if features[23][13] <= 1.5:
					pixels.append((23, 13))
					if features[13][20] <= 8.0:
						pixels.append((13, 20))
						if features[9][23] <= 58.5:
							pixels.append((9, 23))
							if features[18][22] <= 6.0:
								pixels.append((18, 22))
								if features[13][10] <= 1.5:
									pixels.append((13, 10))
									if features[11][14] <= 245.0:
										pixels.append((11, 14))
										if features[11][11] <= 6.5:
											pixels.append((11, 11))
											if features[17][16] <= 165.5:
												pixels.append((17, 16))
												if features[20][13] <= 120.5:
													pixels.append((20, 13))
													return 1 # approximately 12 were 1 out of 12 samples at leaf node
												else:
													if features[9][17] <= 216.0:
														pixels.append((9, 17))
														if features[15][13] <= 116.5:
															pixels.append((15, 13))
															return 1 # approximately 1 were 1 out of 1 samples at leaf node
														else:
															return 6 # approximately 3 were 6 out of 3 samples at leaf node
													else:
														if features[8][13] <= 253.5:
															pixels.append((8, 13))
															return 2 # approximately 11 were 2 out of 11 samples at leaf node
														else:
															return 8 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												if features[20][22] <= 18.0:
													pixels.append((20, 22))
													return 3 # approximately 11 were 3 out of 11 samples at leaf node
												else:
													return 2 # approximately 2 were 2 out of 2 samples at leaf node
										else:
											if features[11][16] <= 3.5:
												pixels.append((11, 16))
												if features[7][15] <= 186.5:
													pixels.append((7, 15))
													return 1 # approximately 4 were 1 out of 4 samples at leaf node
												else:
													return 9 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												if features[20][3] <= 119.5:
													pixels.append((20, 3))
													return 8 # approximately 16 were 8 out of 16 samples at leaf node
												else:
													return 2 # approximately 1 were 2 out of 1 samples at leaf node
									else:
										if features[14][15] <= 33.0:
											pixels.append((14, 15))
											if features[14][13] <= 251.5:
												pixels.append((14, 13))
												return 6 # approximately 3 were 6 out of 3 samples at leaf node
											else:
												if features[11][14] <= 252.5:
													pixels.append((11, 14))
													return 8 # approximately 2 were 8 out of 2 samples at leaf node
												else:
													if features[15][11] <= 220.5:
														pixels.append((15, 11))
														return 1 # approximately 1 were 1 out of 1 samples at leaf node
													else:
														return 2 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											if features[19][8] <= 252.5:
												pixels.append((19, 8))
												if features[20][8] <= 254.0:
													pixels.append((20, 8))
													return 1 # approximately 60 were 1 out of 60 samples at leaf node
												else:
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												return 2 # approximately 2 were 2 out of 2 samples at leaf node
								else:
									if features[18][18] <= 41.5:
										pixels.append((18, 18))
										if features[16][18] <= 8.0:
											pixels.append((16, 18))
											if features[19][6] <= 19.5:
												pixels.append((19, 6))
												if features[10][19] <= 2.5:
													pixels.append((10, 19))
													if features[5][15] <= 4.0:
														pixels.append((5, 15))
														if features[7][14] <= 21.0:
															pixels.append((7, 14))
															if features[9][14] <= 175.0:
																pixels.append((9, 14))
																if features[9][19] <= 22.0:
																	pixels.append((9, 19))
																	if features[14][15] <= 201.5:
																		pixels.append((14, 15))
																		if features[12][24] <= 26.0:
																			pixels.append((12, 24))
																			return 2 # approximately 1 were 2 out of 1 samples at leaf node
																		else:
																			return 5 # approximately 1 were 5 out of 1 samples at leaf node
																	else:
																		return 4 # approximately 5 were 4 out of 5 samples at leaf node
																else:
																	return 1 # approximately 3 were 1 out of 3 samples at leaf node
															else:
																return 9 # approximately 3 were 9 out of 3 samples at leaf node
														else:
															return 9 # approximately 19 were 9 out of 19 samples at leaf node
													else:
														if features[11][13] <= 213.0:
															pixels.append((11, 13))
															if features[18][11] <= 15.5:
																pixels.append((18, 11))
																return 4 # approximately 6 were 4 out of 6 samples at leaf node
															else:
																if features[15][12] <= 24.0:
																	pixels.append((15, 12))
																	return 9 # approximately 1 were 9 out of 1 samples at leaf node
																else:
																	return 2 # approximately 2 were 2 out of 2 samples at leaf node
														else:
															if features[20][20] <= 200.5:
																pixels.append((20, 20))
																return 1 # approximately 8 were 1 out of 8 samples at leaf node
															else:
																return 2 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													if features[9][11] <= 51.0:
														pixels.append((9, 11))
														if features[18][12] <= 67.0:
															pixels.append((18, 12))
															return 3 # approximately 4 were 3 out of 4 samples at leaf node
														else:
															if features[10][23] <= 38.5:
																pixels.append((10, 23))
																if features[18][12] <= 246.0:
																	pixels.append((18, 12))
																	if features[12][10] <= 142.0:
																		pixels.append((12, 10))
																		return 2 # approximately 2 were 2 out of 2 samples at leaf node
																	else:
																		if features[5][22] <= 125.5:
																			pixels.append((5, 22))
																			if features[11][10] <= 77.5:
																				pixels.append((11, 10))
																				return 9 # approximately 1 were 9 out of 1 samples at leaf node
																			else:
																				return 4 # approximately 1 were 4 out of 1 samples at leaf node
																		else:
																			return 8 # approximately 1 were 8 out of 1 samples at leaf node
																else:
																	return 1 # approximately 2 were 1 out of 2 samples at leaf node
															else:
																return 5 # approximately 3 were 5 out of 3 samples at leaf node
													else:
														if features[15][12] <= 21.0:
															pixels.append((15, 12))
															return 9 # approximately 2 were 9 out of 2 samples at leaf node
														else:
															return 8 # approximately 11 were 8 out of 11 samples at leaf node
											else:
												if features[10][18] <= 233.5:
													pixels.append((10, 18))
													return 5 # approximately 12 were 5 out of 12 samples at leaf node
												else:
													if features[17][9] <= 213.5:
														pixels.append((17, 9))
														if features[22][10] <= 215.5:
															pixels.append((22, 10))
															return 3 # approximately 2 were 3 out of 2 samples at leaf node
														else:
															return 8 # approximately 1 were 8 out of 1 samples at leaf node
													else:
														return 2 # approximately 3 were 2 out of 3 samples at leaf node
										else:
											if features[16][15] <= 44.0:
												pixels.append((16, 15))
												if features[12][13] <= 59.0:
													pixels.append((12, 13))
													return 6 # approximately 1 were 6 out of 1 samples at leaf node
												else:
													if features[9][8] <= 145.0:
														pixels.append((9, 8))
														return 3 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														return 8 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												return 4 # approximately 24 were 4 out of 24 samples at leaf node
									else:
										if features[19][16] <= 115.0:
											pixels.append((19, 16))
											if features[12][9] <= 13.5:
												pixels.append((12, 9))
												if features[17][13] <= 136.5:
													pixels.append((17, 13))
													return 3 # approximately 10 were 3 out of 10 samples at leaf node
												else:
													if features[18][19] <= 51.0:
														pixels.append((18, 19))
														return 8 # approximately 1 were 8 out of 1 samples at leaf node
													else:
														return 2 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												if features[17][20] <= 147.5:
													pixels.append((17, 20))
													return 8 # approximately 19 were 8 out of 19 samples at leaf node
												else:
													return 4 # approximately 1 were 4 out of 1 samples at leaf node
										else:
											if features[15][15] <= 231.0:
												pixels.append((15, 15))
												if features[10][16] <= 239.0:
													pixels.append((10, 16))
													if features[9][7] <= 126.5:
														pixels.append((9, 7))
														if features[21][15] <= 68.5:
															pixels.append((21, 15))
															return 1 # approximately 1 were 1 out of 1 samples at leaf node
														else:
															return 6 # approximately 15 were 6 out of 15 samples at leaf node
													else:
														return 8 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													if features[20][10] <= 252.5:
														pixels.append((20, 10))
														return 2 # approximately 3 were 2 out of 3 samples at leaf node
													else:
														return 6 # approximately 1 were 6 out of 1 samples at leaf node
											else:
												if features[10][12] <= 17.5:
													pixels.append((10, 12))
													return 3 # approximately 2 were 3 out of 2 samples at leaf node
												else:
													if features[15][13] <= 159.0:
														pixels.append((15, 13))
														return 4 # approximately 2 were 4 out of 2 samples at leaf node
													else:
														return 1 # approximately 1 were 1 out of 1 samples at leaf node
							else:
								if features[13][9] <= 246.5:
									pixels.append((13, 9))
									if features[13][14] <= 184.5:
										pixels.append((13, 14))
										if features[21][11] <= 2.5:
											pixels.append((21, 11))
											return 2 # approximately 4 were 2 out of 4 samples at leaf node
										else:
											if features[9][16] <= 36.0:
												pixels.append((9, 16))
												return 1 # approximately 1 were 1 out of 1 samples at leaf node
											else:
												if features[23][19] <= 126.5:
													pixels.append((23, 19))
													if features[16][20] <= 195.5:
														pixels.append((16, 20))
														return 7 # approximately 1 were 7 out of 1 samples at leaf node
													else:
														if features[12][14] <= 139.5:
															pixels.append((12, 14))
															return 6 # approximately 1 were 6 out of 1 samples at leaf node
														else:
															return 3 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													return 8 # approximately 1 were 8 out of 1 samples at leaf node
									else:
										if features[10][22] <= 127.0:
											pixels.append((10, 22))
											return 2 # approximately 80 were 2 out of 80 samples at leaf node
										else:
											return 6 # approximately 1 were 6 out of 1 samples at leaf node
								else:
									if features[8][8] <= 27.0:
										pixels.append((8, 8))
										return 4 # approximately 2 were 4 out of 2 samples at leaf node
									else:
										if features[16][10] <= 55.0:
											pixels.append((16, 10))
											return 3 # approximately 2 were 3 out of 2 samples at leaf node
										else:
											if features[23][22] <= 17.0:
												pixels.append((23, 22))
												return 6 # approximately 2 were 6 out of 2 samples at leaf node
											else:
												return 8 # approximately 1 were 8 out of 1 samples at leaf node
						else:
							if features[13][16] <= 188.0:
								pixels.append((13, 16))
								if features[16][19] <= 123.5:
									pixels.append((16, 19))
									return 5 # approximately 71 were 5 out of 71 samples at leaf node
								else:
									if features[9][4] <= 127.0:
										pixels.append((9, 4))
										return 0 # approximately 1 were 0 out of 1 samples at leaf node
									else:
										return 8 # approximately 1 were 8 out of 1 samples at leaf node
							else:
								if features[10][19] <= 114.5:
									pixels.append((10, 19))
									if features[10][19] <= 49.5:
										pixels.append((10, 19))
										return 0 # approximately 1 were 0 out of 1 samples at leaf node
									else:
										return 3 # approximately 1 were 3 out of 1 samples at leaf node
								else:
									return 8 # approximately 5 were 8 out of 5 samples at leaf node
					else:
						if features[7][20] <= 87.5:
							pixels.append((7, 20))
							if features[9][16] <= 198.0:
								pixels.append((9, 16))
								return 6 # approximately 109 were 6 out of 109 samples at leaf node
							else:
								if features[15][11] <= 252.0:
									pixels.append((15, 11))
									if features[10][18] <= 253.5:
										pixels.append((10, 18))
										return 6 # approximately 6 were 6 out of 6 samples at leaf node
									else:
										return 3 # approximately 1 were 3 out of 1 samples at leaf node
								else:
									if features[16][7] <= 241.0:
										pixels.append((16, 7))
										if features[7][13] <= 44.0:
											pixels.append((7, 13))
											if features[15][5] <= 100.0:
												pixels.append((15, 5))
												return 0 # approximately 1 were 0 out of 1 samples at leaf node
											else:
												return 5 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											return 4 # approximately 1 were 4 out of 1 samples at leaf node
									else:
										return 2 # approximately 2 were 2 out of 2 samples at leaf node
						else:
							if features[20][12] <= 252.5:
								pixels.append((20, 12))
								if features[11][18] <= 126.0:
									pixels.append((11, 18))
									return 9 # approximately 1 were 9 out of 1 samples at leaf node
								else:
									if features[22][11] <= 110.5:
										pixels.append((22, 11))
										return 1 # approximately 1 were 1 out of 1 samples at leaf node
									else:
										return 8 # approximately 1 were 8 out of 1 samples at leaf node
							else:
								return 0 # approximately 4 were 0 out of 4 samples at leaf node
				else:
					if features[18][11] <= 2.5:
						pixels.append((18, 11))
						if features[17][9] <= 68.5:
							pixels.append((17, 9))
							if features[19][13] <= 30.0:
								pixels.append((19, 13))
								if features[10][11] <= 59.0:
									pixels.append((10, 11))
									if features[8][24] <= 12.5:
										pixels.append((8, 24))
										if features[10][13] <= 254.0:
											pixels.append((10, 13))
											if features[12][8] <= 252.5:
												pixels.append((12, 8))
												if features[19][14] <= 253.5:
													pixels.append((19, 14))
													return 3 # approximately 227 were 3 out of 227 samples at leaf node
												else:
													return 9 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												if features[19][17] <= 126.5:
													pixels.append((19, 17))
													return 5 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													return 0 # approximately 1 were 0 out of 1 samples at leaf node
										else:
											return 1 # approximately 2 were 1 out of 2 samples at leaf node
									else:
										return 5 # approximately 3 were 5 out of 3 samples at leaf node
								else:
									if features[22][9] <= 39.0:
										pixels.append((22, 9))
										if features[25][14] <= 43.5:
											pixels.append((25, 14))
											if features[10][16] <= 162.5:
												pixels.append((10, 16))
												if features[14][21] <= 126.0:
													pixels.append((14, 21))
													if features[12][11] <= 213.0:
														pixels.append((12, 11))
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														if features[23][16] <= 189.5:
															pixels.append((23, 16))
															return 1 # approximately 1 were 1 out of 1 samples at leaf node
														else:
															return 8 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													return 0 # approximately 1 were 0 out of 1 samples at leaf node
											else:
												return 3 # approximately 5 were 3 out of 5 samples at leaf node
										else:
											if features[10][11] <= 175.0:
												pixels.append((10, 11))
												return 4 # approximately 2 were 4 out of 2 samples at leaf node
											else:
												return 9 # approximately 5 were 9 out of 5 samples at leaf node
									else:
										if features[6][14] <= 213.5:
											pixels.append((6, 14))
											return 5 # approximately 16 were 5 out of 16 samples at leaf node
										else:
											if features[21][17] <= 210.0:
												pixels.append((21, 17))
												if features[21][19] <= 63.5:
													pixels.append((21, 19))
													if features[20][17] <= 247.5:
														pixels.append((20, 17))
														if features[17][7] <= 126.5:
															pixels.append((17, 7))
															if features[13][10] <= 240.5:
																pixels.append((13, 10))
																return 9 # approximately 1 were 9 out of 1 samples at leaf node
															else:
																return 1 # approximately 1 were 1 out of 1 samples at leaf node
														else:
															return 8 # approximately 1 were 8 out of 1 samples at leaf node
													else:
														return 0 # approximately 2 were 0 out of 2 samples at leaf node
												else:
													return 3 # approximately 2 were 3 out of 2 samples at leaf node
											else:
												return 5 # approximately 3 were 5 out of 3 samples at leaf node
							else:
								if features[11][14] <= 211.5:
									pixels.append((11, 14))
									if features[23][16] <= 17.5:
										pixels.append((23, 16))
										if features[25][12] <= 4.5:
											pixels.append((25, 12))
											if features[21][8] <= 70.5:
												pixels.append((21, 8))
												if features[6][15] <= 140.5:
													pixels.append((6, 15))
													if features[10][16] <= 3.0:
														pixels.append((10, 16))
														return 9 # approximately 1 were 9 out of 1 samples at leaf node
													else:
														return 4 # approximately 12 were 4 out of 12 samples at leaf node
												else:
													if features[18][14] <= 252.0:
														pixels.append((18, 14))
														if features[20][17] <= 27.0:
															pixels.append((20, 17))
															if features[21][12] <= 231.0:
																pixels.append((21, 12))
																return 4 # approximately 1 were 4 out of 1 samples at leaf node
															else:
																if features[12][13] <= 5.5:
																	pixels.append((12, 13))
																	return 1 # approximately 1 were 1 out of 1 samples at leaf node
																else:
																	if features[5][20] <= 28.5:
																		pixels.append((5, 20))
																		return 7 # approximately 1 were 7 out of 1 samples at leaf node
																	else:
																		return 5 # approximately 1 were 5 out of 1 samples at leaf node
														else:
															return 8 # approximately 2 were 8 out of 2 samples at leaf node
													else:
														return 9 # approximately 3 were 9 out of 3 samples at leaf node
											else:
												return 3 # approximately 7 were 3 out of 7 samples at leaf node
										else:
											if features[13][14] <= 138.0:
												pixels.append((13, 14))
												if features[14][9] <= 13.5:
													pixels.append((14, 9))
													return 9 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													return 7 # approximately 3 were 7 out of 3 samples at leaf node
											else:
												return 9 # approximately 15 were 9 out of 15 samples at leaf node
									else:
										if features[17][13] <= 56.5:
											pixels.append((17, 13))
											if features[24][15] <= 117.0:
												pixels.append((24, 15))
												return 5 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												if features[19][12] <= 79.0:
													pixels.append((19, 12))
													return 9 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											return 8 # approximately 38 were 8 out of 38 samples at leaf node
								else:
									if features[8][18] <= 21.0:
										pixels.append((8, 18))
										if features[20][13] <= 181.0:
											pixels.append((20, 13))
											if features[6][16] <= 174.5:
												pixels.append((6, 16))
												return 9 # approximately 3 were 9 out of 3 samples at leaf node
											else:
												if features[19][17] <= 84.0:
													pixels.append((19, 17))
													return 1 # approximately 3 were 1 out of 3 samples at leaf node
												else:
													if features[16][7] <= 28.5:
														pixels.append((16, 7))
														return 3 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														return 4 # approximately 1 were 4 out of 1 samples at leaf node
										else:
											return 1 # approximately 36 were 1 out of 36 samples at leaf node
									else:
										if features[11][16] <= 251.5:
											pixels.append((11, 16))
											if features[15][5] <= 28.5:
												pixels.append((15, 5))
												if features[25][13] <= 82.0:
													pixels.append((25, 13))
													return 8 # approximately 2 were 8 out of 2 samples at leaf node
												else:
													if features[22][16] <= 126.5:
														pixels.append((22, 16))
														return 7 # approximately 1 were 7 out of 1 samples at leaf node
													else:
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												return 0 # approximately 2 were 0 out of 2 samples at leaf node
										else:
											return 3 # approximately 4 were 3 out of 4 samples at leaf node
						else:
							if features[14][9] <= 222.5:
								pixels.append((14, 9))
								if features[22][5] <= 192.5:
									pixels.append((22, 5))
									if features[16][19] <= 248.0:
										pixels.append((16, 19))
										if features[20][21] <= 254.0:
											pixels.append((20, 21))
											if features[4][13] <= 253.5:
												pixels.append((4, 13))
												if features[4][23] <= 26.0:
													pixels.append((4, 23))
													if features[10][26] <= 59.5:
														pixels.append((10, 26))
														return 8 # approximately 83 were 8 out of 83 samples at leaf node
													else:
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													return 5 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												return 3 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											return 2 # approximately 1 were 2 out of 1 samples at leaf node
									else:
										if features[12][12] <= 135.0:
											pixels.append((12, 12))
											return 2 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											return 4 # approximately 1 were 4 out of 1 samples at leaf node
								else:
									if features[18][7] <= 126.5:
										pixels.append((18, 7))
										return 3 # approximately 3 were 3 out of 3 samples at leaf node
									else:
										return 8 # approximately 1 were 8 out of 1 samples at leaf node
							else:
								if features[6][12] <= 160.5:
									pixels.append((6, 12))
									if features[17][10] <= 98.5:
										pixels.append((17, 10))
										return 5 # approximately 4 were 5 out of 4 samples at leaf node
									else:
										if features[21][10] <= 129.0:
											pixels.append((21, 10))
											if features[25][12] <= 28.0:
												pixels.append((25, 12))
												if features[18][7] <= 25.5:
													pixels.append((18, 7))
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													return 4 # approximately 1 were 4 out of 1 samples at leaf node
											else:
												return 9 # approximately 2 were 9 out of 2 samples at leaf node
										else:
											return 0 # approximately 3 were 0 out of 3 samples at leaf node
								else:
									return 8 # approximately 4 were 8 out of 4 samples at leaf node
					else:
						if features[10][14] <= 250.0:
							pixels.append((10, 14))
							if features[15][20] <= 3.5:
								pixels.append((15, 20))
								if features[20][23] <= 18.0:
									pixels.append((20, 23))
									if features[15][14] <= 22.0:
										pixels.append((15, 14))
										if features[22][18] <= 4.0:
											pixels.append((22, 18))
											if features[17][7] <= 107.5:
												pixels.append((17, 7))
												if features[13][12] <= 83.0:
													pixels.append((13, 12))
													return 7 # approximately 1 were 7 out of 1 samples at leaf node
												else:
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												if features[5][19] <= 30.0:
													pixels.append((5, 19))
													return 6 # approximately 1 were 6 out of 1 samples at leaf node
												else:
													return 8 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											return 2 # approximately 3 were 2 out of 3 samples at leaf node
									else:
										if features[6][6] <= 17.5:
											pixels.append((6, 6))
											if features[22][4] <= 122.0:
												pixels.append((22, 4))
												if features[14][13] <= 6.5:
													pixels.append((14, 13))
													if features[22][17] <= 36.5:
														pixels.append((22, 17))
														if features[18][15] <= 243.0:
															pixels.append((18, 15))
															return 4 # approximately 2 were 4 out of 2 samples at leaf node
														else:
															if features[8][14] <= 51.0:
																pixels.append((8, 14))
																return 9 # approximately 1 were 9 out of 1 samples at leaf node
															else:
																return 7 # approximately 1 were 7 out of 1 samples at leaf node
													else:
														return 8 # approximately 2 were 8 out of 2 samples at leaf node
												else:
													if features[19][6] <= 239.5:
														pixels.append((19, 6))
														if features[4][8] <= 73.0:
															pixels.append((4, 8))
															if features[25][7] <= 141.0:
																pixels.append((25, 7))
																if features[4][11] <= 254.5:
																	pixels.append((4, 11))
																	if features[23][14] <= 0.5:
																		pixels.append((23, 14))
																		if features[10][16] <= 245.5:
																			pixels.append((10, 16))
																			if features[11][15] <= 244.0:
																				pixels.append((11, 15))
																				return 8 # approximately 25 were 8 out of 25 samples at leaf node
																			else:
																				return 3 # approximately 1 were 3 out of 1 samples at leaf node
																		else:
																			if features[17][8] <= 28.5:
																				pixels.append((17, 8))
																				return 1 # approximately 3 were 1 out of 3 samples at leaf node
																			else:
																				return 2 # approximately 1 were 2 out of 1 samples at leaf node
																	else:
																		return 8 # approximately 498 were 8 out of 498 samples at leaf node
																else:
																	return 3 # approximately 1 were 3 out of 1 samples at leaf node
															else:
																return 3 # approximately 1 were 3 out of 1 samples at leaf node
														else:
															return 2 # approximately 1 were 2 out of 1 samples at leaf node
													else:
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												return 3 # approximately 2 were 3 out of 2 samples at leaf node
										else:
											if features[18][14] <= 20.5:
												pixels.append((18, 14))
												return 2 # approximately 2 were 2 out of 2 samples at leaf node
											else:
												return 3 # approximately 2 were 3 out of 2 samples at leaf node
								else:
									return 2 # approximately 6 were 2 out of 6 samples at leaf node
							else:
								if features[14][13] <= 183.0:
									pixels.append((14, 13))
									return 4 # approximately 4 were 4 out of 4 samples at leaf node
								else:
									if features[6][18] <= 113.5:
										pixels.append((6, 18))
										return 6 # approximately 4 were 6 out of 4 samples at leaf node
									else:
										if features[15][9] <= 44.5:
											pixels.append((15, 9))
											return 8 # approximately 3 were 8 out of 3 samples at leaf node
										else:
											if features[11][19] <= 14.0:
												pixels.append((11, 19))
												return 0 # approximately 2 were 0 out of 2 samples at leaf node
											else:
												if features[20][7] <= 40.5:
													pixels.append((20, 7))
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													if features[6][8] <= 122.5:
														pixels.append((6, 8))
														if features[5][17] <= 253.0:
															pixels.append((5, 17))
															return 5 # approximately 1 were 5 out of 1 samples at leaf node
														else:
															return 9 # approximately 1 were 9 out of 1 samples at leaf node
													else:
														return 2 # approximately 1 were 2 out of 1 samples at leaf node
						else:
							if features[19][13] <= 233.5:
								pixels.append((19, 13))
								if features[7][17] <= 153.5:
									pixels.append((7, 17))
									if features[16][12] <= 154.0:
										pixels.append((16, 12))
										return 3 # approximately 4 were 3 out of 4 samples at leaf node
									else:
										if features[5][17] <= 31.5:
											pixels.append((5, 17))
											return 5 # approximately 2 were 5 out of 2 samples at leaf node
										else:
											if features[6][16] <= 252.0:
												pixels.append((6, 16))
												return 8 # approximately 2 were 8 out of 2 samples at leaf node
											else:
												if features[5][18] <= 5.5:
													pixels.append((5, 18))
													return 2 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													return 4 # approximately 1 were 4 out of 1 samples at leaf node
								else:
									if features[4][17] <= 16.5:
										pixels.append((4, 17))
										return 8 # approximately 19 were 8 out of 19 samples at leaf node
									else:
										if features[8][12] <= 126.0:
											pixels.append((8, 12))
											return 1 # approximately 1 were 1 out of 1 samples at leaf node
										else:
											if features[10][11] <= 142.5:
												pixels.append((10, 11))
												return 2 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												return 0 # approximately 1 were 0 out of 1 samples at leaf node
							else:
								if features[7][20] <= 45.0:
									pixels.append((7, 20))
									if features[19][22] <= 34.0:
										pixels.append((19, 22))
										if features[12][13] <= 175.5:
											pixels.append((12, 13))
											return 7 # approximately 1 were 7 out of 1 samples at leaf node
										else:
											return 1 # approximately 63 were 1 out of 63 samples at leaf node
									else:
										return 2 # approximately 2 were 2 out of 2 samples at leaf node
								else:
									if features[15][9] <= 46.5:
										pixels.append((15, 9))
										if features[12][11] <= 66.5:
											pixels.append((12, 11))
											return 1 # approximately 1 were 1 out of 1 samples at leaf node
										else:
											return 8 # approximately 5 were 8 out of 5 samples at leaf node
									else:
										if features[7][13] <= 126.0:
											pixels.append((7, 13))
											return 6 # approximately 2 were 6 out of 2 samples at leaf node
										else:
											return 0 # approximately 2 were 0 out of 2 samples at leaf node
else:
	if features[5][15] <= 0.5:
		pixels.append((5, 15))
		if features[8][15] <= 0.5:
			pixels.append((8, 15))
			if features[3][12] <= 0.5:
				pixels.append((3, 12))
				if features[15][9] <= 36.5:
					pixels.append((15, 9))
					if features[10][14] <= 72.5:
						pixels.append((10, 14))
						if features[21][9] <= 53.5:
							pixels.append((21, 9))
							if features[7][15] <= 19.0:
								pixels.append((7, 15))
								if features[12][23] <= 27.5:
									pixels.append((12, 23))
									if features[3][13] <= 4.5:
										pixels.append((3, 13))
										if features[11][14] <= 109.5:
											pixels.append((11, 14))
											if features[16][16] <= 7.5:
												pixels.append((16, 16))
												if features[7][12] <= 252.5:
													pixels.append((7, 12))
													if features[20][14] <= 43.0:
														pixels.append((20, 14))
														if features[16][6] <= 252.5:
															pixels.append((16, 6))
															if features[13][20] <= 17.5:
																pixels.append((13, 20))
																if features[18][11] <= 14.5:
																	pixels.append((18, 11))
																	if features[12][7] <= 45.5:
																		pixels.append((12, 7))
																		return 4 # approximately 6 were 4 out of 6 samples at leaf node
																	else:
																		if features[19][23] <= 107.0:
																			pixels.append((19, 23))
																			if features[12][10] <= 126.5:
																				pixels.append((12, 10))
																				if features[20][9] <= 45.0:
																					pixels.append((20, 9))
																					return 9 # approximately 1 were 9 out of 1 samples at leaf node
																				else:
																					return 6 # approximately 1 were 6 out of 1 samples at leaf node
																			else:
																				return 3 # approximately 1 were 3 out of 1 samples at leaf node
																		else:
																			return 5 # approximately 1 were 5 out of 1 samples at leaf node
																else:
																	return 1 # approximately 4 were 1 out of 4 samples at leaf node
															else:
																return 4 # approximately 12 were 4 out of 12 samples at leaf node
														else:
															if features[10][9] <= 130.0:
																pixels.append((10, 9))
																return 9 # approximately 2 were 9 out of 2 samples at leaf node
															else:
																return 7 # approximately 1 were 7 out of 1 samples at leaf node
													else:
														if features[16][12] <= 125.5:
															pixels.append((16, 12))
															return 5 # approximately 3 were 5 out of 3 samples at leaf node
														else:
															if features[17][20] <= 127.0:
																pixels.append((17, 20))
																if features[8][20] <= 206.0:
																	pixels.append((8, 20))
																	return 8 # approximately 1 were 8 out of 1 samples at leaf node
																else:
																	return 2 # approximately 1 were 2 out of 1 samples at leaf node
															else:
																return 6 # approximately 2 were 6 out of 2 samples at leaf node
												else:
													return 3 # approximately 8 were 3 out of 8 samples at leaf node
											else:
												if features[20][9] <= 25.0:
													pixels.append((20, 9))
													if features[12][4] <= 86.5:
														pixels.append((12, 4))
														if features[18][22] <= 195.0:
															pixels.append((18, 22))
															if features[22][8] <= 2.0:
																pixels.append((22, 8))
																if features[5][12] <= 254.5:
																	pixels.append((5, 12))
																	if features[2][11] <= 11.0:
																		pixels.append((2, 11))
																		if features[6][14] <= 72.5:
																			pixels.append((6, 14))
																			if features[5][9] <= 254.5:
																				pixels.append((5, 9))
																				if features[25][9] <= 229.0:
																					pixels.append((25, 9))
																					if features[10][15] <= 226.0:
																						pixels.append((10, 15))
																						if features[18][16] <= 254.5:
																							pixels.append((18, 16))
																							return 4 # approximately 275 were 4 out of 275 samples at leaf node
																						else:
																							if features[24][14] <= 120.0:
																								pixels.append((24, 14))
																								return 4 # approximately 5 were 4 out of 5 samples at leaf node
																							else:
																								return 9 # approximately 1 were 9 out of 1 samples at leaf node
																					else:
																						if features[18][15] <= 212.5:
																							pixels.append((18, 15))
																							return 4 # approximately 1 were 4 out of 1 samples at leaf node
																						else:
																							return 5 # approximately 1 were 5 out of 1 samples at leaf node
																				else:
																					if features[6][12] <= 34.0:
																						pixels.append((6, 12))
																						return 7 # approximately 1 were 7 out of 1 samples at leaf node
																					else:
																						return 4 # approximately 1 were 4 out of 1 samples at leaf node
																			else:
																				if features[14][20] <= 126.5:
																					pixels.append((14, 20))
																					return 8 # approximately 1 were 8 out of 1 samples at leaf node
																				else:
																					return 4 # approximately 1 were 4 out of 1 samples at leaf node
																		else:
																			if features[5][11] <= 19.0:
																				pixels.append((5, 11))
																				if features[11][11] <= 1.0:
																					pixels.append((11, 11))
																					return 9 # approximately 1 were 9 out of 1 samples at leaf node
																				else:
																					return 4 # approximately 24 were 4 out of 24 samples at leaf node
																			else:
																				if features[18][12] <= 73.5:
																					pixels.append((18, 12))
																					return 9 # approximately 1 were 9 out of 1 samples at leaf node
																				else:
																					return 8 # approximately 3 were 8 out of 3 samples at leaf node
																	else:
																		return 6 # approximately 1 were 6 out of 1 samples at leaf node
																else:
																	if features[11][10] <= 231.0:
																		pixels.append((11, 10))
																		return 3 # approximately 1 were 3 out of 1 samples at leaf node
																	else:
																		return 9 # approximately 1 were 9 out of 1 samples at leaf node
															else:
																if features[22][13] <= 65.5:
																	pixels.append((22, 13))
																	return 7 # approximately 1 were 7 out of 1 samples at leaf node
																else:
																	return 5 # approximately 1 were 5 out of 1 samples at leaf node
														else:
															if features[9][6] <= 28.0:
																pixels.append((9, 6))
																return 3 # approximately 2 were 3 out of 2 samples at leaf node
															else:
																if features[22][20] <= 126.5:
																	pixels.append((22, 20))
																	if features[12][16] <= 126.5:
																		pixels.append((12, 16))
																		return 4 # approximately 1 were 4 out of 1 samples at leaf node
																	else:
																		return 6 # approximately 1 were 6 out of 1 samples at leaf node
																else:
																	return 5 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														if features[8][4] <= 23.5:
															pixels.append((8, 4))
															return 7 # approximately 5 were 7 out of 5 samples at leaf node
														else:
															if features[13][19] <= 126.0:
																pixels.append((13, 19))
																return 1 # approximately 1 were 1 out of 1 samples at leaf node
															else:
																return 4 # approximately 4 were 4 out of 4 samples at leaf node
												else:
													if features[15][14] <= 247.5:
														pixels.append((15, 14))
														if features[16][7] <= 166.0:
															pixels.append((16, 7))
															if features[20][19] <= 137.5:
																pixels.append((20, 19))
																return 5 # approximately 2 were 5 out of 2 samples at leaf node
															else:
																if features[8][21] <= 127.5:
																	pixels.append((8, 21))
																	return 6 # approximately 1 were 6 out of 1 samples at leaf node
																else:
																	return 9 # approximately 1 were 9 out of 1 samples at leaf node
														else:
															return 4 # approximately 4 were 4 out of 4 samples at leaf node
													else:
														return 2 # approximately 4 were 2 out of 4 samples at leaf node
										else:
											if features[11][7] <= 7.0:
												pixels.append((11, 7))
												if features[6][11] <= 189.0:
													pixels.append((6, 11))
													if features[18][17] <= 32.5:
														pixels.append((18, 17))
														return 4 # approximately 5 were 4 out of 5 samples at leaf node
													else:
														if features[6][12] <= 8.0:
															pixels.append((6, 12))
															if features[9][17] <= 120.5:
																pixels.append((9, 17))
																if features[15][18] <= 70.0:
																	pixels.append((15, 18))
																	return 7 # approximately 1 were 7 out of 1 samples at leaf node
																else:
																	return 6 # approximately 1 were 6 out of 1 samples at leaf node
															else:
																return 5 # approximately 1 were 5 out of 1 samples at leaf node
														else:
															return 8 # approximately 2 were 8 out of 2 samples at leaf node
												else:
													return 3 # approximately 5 were 3 out of 5 samples at leaf node
											else:
												if features[14][13] <= 84.5:
													pixels.append((14, 13))
													if features[22][22] <= 123.5:
														pixels.append((22, 22))
														return 7 # approximately 15 were 7 out of 15 samples at leaf node
													else:
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													if features[5][11] <= 0.5:
														pixels.append((5, 11))
														return 2 # approximately 2 were 2 out of 2 samples at leaf node
													else:
														if features[13][10] <= 129.0:
															pixels.append((13, 10))
															return 8 # approximately 1 were 8 out of 1 samples at leaf node
														else:
															return 9 # approximately 1 were 9 out of 1 samples at leaf node
									else:
										return 6 # approximately 19 were 6 out of 19 samples at leaf node
								else:
									if features[15][23] <= 16.0:
										pixels.append((15, 23))
										if features[13][8] <= 60.5:
											pixels.append((13, 8))
											if features[13][21] <= 159.0:
												pixels.append((13, 21))
												return 6 # approximately 3 were 6 out of 3 samples at leaf node
											else:
												if features[13][22] <= 199.0:
													pixels.append((13, 22))
													return 8 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													return 7 # approximately 1 were 7 out of 1 samples at leaf node
										else:
											return 4 # approximately 4 were 4 out of 4 samples at leaf node
									else:
										return 6 # approximately 26 were 6 out of 26 samples at leaf node
							else:
								if features[7][9] <= 7.5:
									pixels.append((7, 9))
									if features[15][16] <= 44.5:
										pixels.append((15, 16))
										if features[23][16] <= 209.0:
											pixels.append((23, 16))
											if features[12][10] <= 213.5:
												pixels.append((12, 10))
												return 7 # approximately 2 were 7 out of 2 samples at leaf node
											else:
												if features[16][18] <= 189.5:
													pixels.append((16, 18))
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													return 5 # approximately 2 were 5 out of 2 samples at leaf node
										else:
											return 8 # approximately 3 were 8 out of 3 samples at leaf node
									else:
										if features[20][11] <= 213.5:
											pixels.append((20, 11))
											if features[5][17] <= 15.5:
												pixels.append((5, 17))
												if features[11][22] <= 225.0:
													pixels.append((11, 22))
													if features[7][15] <= 22.0:
														pixels.append((7, 15))
														return 7 # approximately 1 were 7 out of 1 samples at leaf node
													else:
														if features[18][19] <= 184.5:
															pixels.append((18, 19))
															if features[23][12] <= 213.0:
																pixels.append((23, 12))
																return 9 # approximately 72 were 9 out of 72 samples at leaf node
															else:
																if features[13][15] <= 4.5:
																	pixels.append((13, 15))
																	if features[16][9] <= 118.0:
																		pixels.append((16, 9))
																		return 7 # approximately 3 were 7 out of 3 samples at leaf node
																	else:
																		return 9 # approximately 2 were 9 out of 2 samples at leaf node
																else:
																	if features[22][12] <= 154.5:
																		pixels.append((22, 12))
																		return 4 # approximately 1 were 4 out of 1 samples at leaf node
																	else:
																		return 9 # approximately 16 were 9 out of 16 samples at leaf node
														else:
															return 7 # approximately 1 were 7 out of 1 samples at leaf node
												else:
													return 8 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												return 4 # approximately 2 were 4 out of 2 samples at leaf node
										else:
											if features[14][13] <= 124.5:
												pixels.append((14, 13))
												return 7 # approximately 2 were 7 out of 2 samples at leaf node
											else:
												return 8 # approximately 1 were 8 out of 1 samples at leaf node
								else:
									if features[14][13] <= 5.5:
										pixels.append((14, 13))
										if features[24][17] <= 29.5:
											pixels.append((24, 17))
											return 7 # approximately 20 were 7 out of 20 samples at leaf node
										else:
											if features[18][17] <= 8.0:
												pixels.append((18, 17))
												return 5 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												return 9 # approximately 2 were 9 out of 2 samples at leaf node
									else:
										if features[19][10] <= 3.0:
											pixels.append((19, 10))
											if features[19][16] <= 49.5:
												pixels.append((19, 16))
												if features[24][15] <= 194.0:
													pixels.append((24, 15))
													return 3 # approximately 8 were 3 out of 8 samples at leaf node
												else:
													return 5 # approximately 2 were 5 out of 2 samples at leaf node
											else:
												if features[12][12] <= 7.5:
													pixels.append((12, 12))
													return 9 # approximately 3 were 9 out of 3 samples at leaf node
												else:
													return 5 # approximately 2 were 5 out of 2 samples at leaf node
										else:
											if features[8][9] <= 254.0:
												pixels.append((8, 9))
												return 8 # approximately 4 were 8 out of 4 samples at leaf node
											else:
												return 6 # approximately 1 were 6 out of 1 samples at leaf node
						else:
							if features[11][16] <= 194.0:
								pixels.append((11, 16))
								if features[16][14] <= 12.0:
									pixels.append((16, 14))
									if features[18][22] <= 7.5:
										pixels.append((18, 22))
										if features[9][15] <= 13.0:
											pixels.append((9, 15))
											return 5 # approximately 9 were 5 out of 9 samples at leaf node
										else:
											return 3 # approximately 1 were 3 out of 1 samples at leaf node
									else:
										if features[19][11] <= 94.5:
											pixels.append((19, 11))
											return 3 # approximately 2 were 3 out of 2 samples at leaf node
										else:
											return 2 # approximately 1 were 2 out of 1 samples at leaf node
								else:
									if features[23][13] <= 82.5:
										pixels.append((23, 13))
										if features[11][10] <= 139.5:
											pixels.append((11, 10))
											if features[24][7] <= 2.0:
												pixels.append((24, 7))
												if features[20][14] <= 252.5:
													pixels.append((20, 14))
													if features[12][16] <= 222.5:
														pixels.append((12, 16))
														if features[21][13] <= 161.5:
															pixels.append((21, 13))
															return 2 # approximately 8 were 2 out of 8 samples at leaf node
														else:
															if features[9][14] <= 107.5:
																pixels.append((9, 14))
																return 6 # approximately 1 were 6 out of 1 samples at leaf node
															else:
																return 8 # approximately 1 were 8 out of 1 samples at leaf node
													else:
														return 1 # approximately 4 were 1 out of 4 samples at leaf node
												else:
													return 6 # approximately 6 were 6 out of 6 samples at leaf node
											else:
												return 7 # approximately 6 were 7 out of 6 samples at leaf node
										else:
											if features[7][18] <= 175.0:
												pixels.append((7, 18))
												return 4 # approximately 7 were 4 out of 7 samples at leaf node
											else:
												if features[20][16] <= 4.0:
													pixels.append((20, 16))
													return 9 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													return 8 # approximately 1 were 8 out of 1 samples at leaf node
									else:
										if features[6][10] <= 253.5:
											pixels.append((6, 10))
											return 8 # approximately 10 were 8 out of 10 samples at leaf node
										else:
											return 2 # approximately 1 were 2 out of 1 samples at leaf node
							else:
								if features[13][11] <= 78.5:
									pixels.append((13, 11))
									if features[20][17] <= 3.5:
										pixels.append((20, 17))
										if features[15][18] <= 43.0:
											pixels.append((15, 18))
											return 1 # approximately 168 were 1 out of 168 samples at leaf node
										else:
											return 2 # approximately 2 were 2 out of 2 samples at leaf node
									else:
										if features[9][16] <= 48.0:
											pixels.append((9, 16))
											return 6 # approximately 3 were 6 out of 3 samples at leaf node
										else:
											if features[21][9] <= 254.0:
												pixels.append((21, 9))
												return 5 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												return 2 # approximately 1 were 2 out of 1 samples at leaf node
								else:
									if features[24][10] <= 162.5:
										pixels.append((24, 10))
										if features[19][17] <= 100.5:
											pixels.append((19, 17))
											if features[5][13] <= 34.0:
												pixels.append((5, 13))
												if features[24][8] <= 127.5:
													pixels.append((24, 8))
													return 5 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													return 9 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												return 8 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											return 3 # approximately 2 were 3 out of 2 samples at leaf node
									else:
										return 4 # approximately 4 were 4 out of 4 samples at leaf node
					else:
						if features[14][13] <= 0.5:
							pixels.append((14, 13))
							if features[18][9] <= 3.5:
								pixels.append((18, 9))
								if features[5][13] <= 29.0:
									pixels.append((5, 13))
									if features[7][17] <= 147.0:
										pixels.append((7, 17))
										if features[19][22] <= 117.5:
											pixels.append((19, 22))
											if features[6][7] <= 237.0:
												pixels.append((6, 7))
												if features[20][5] <= 1.5:
													pixels.append((20, 5))
													if features[7][12] <= 247.0:
														pixels.append((7, 12))
														return 7 # approximately 209 were 7 out of 209 samples at leaf node
													else:
														if features[26][14] <= 73.0:
															pixels.append((26, 14))
															return 7 # approximately 7 were 7 out of 7 samples at leaf node
														else:
															return 9 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													if features[20][7] <= 105.5:
														pixels.append((20, 7))
														return 3 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												if features[10][13] <= 225.0:
													pixels.append((10, 13))
													return 5 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											if features[17][17] <= 52.5:
												pixels.append((17, 17))
												if features[13][15] <= 116.5:
													pixels.append((13, 15))
													return 9 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													return 7 # approximately 1 were 7 out of 1 samples at leaf node
											else:
												return 2 # approximately 2 were 2 out of 2 samples at leaf node
									else:
										return 5 # approximately 2 were 5 out of 2 samples at leaf node
								else:
									if features[13][10] <= 212.5:
										pixels.append((13, 10))
										return 3 # approximately 6 were 3 out of 6 samples at leaf node
									else:
										if features[9][13] <= 49.5:
											pixels.append((9, 13))
											return 5 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											return 9 # approximately 1 were 9 out of 1 samples at leaf node
							else:
								if features[12][14] <= 121.5:
									pixels.append((12, 14))
									if features[16][15] <= 187.5:
										pixels.append((16, 15))
										if features[21][15] <= 111.5:
											pixels.append((21, 15))
											if features[14][8] <= 50.0:
												pixels.append((14, 8))
												if features[11][13] <= 123.5:
													pixels.append((11, 13))
													return 9 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													if features[18][20] <= 51.5:
														pixels.append((18, 20))
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														return 7 # approximately 1 were 7 out of 1 samples at leaf node
											else:
												return 0 # approximately 2 were 0 out of 2 samples at leaf node
										else:
											return 8 # approximately 2 were 8 out of 2 samples at leaf node
									else:
										if features[26][15] <= 55.5:
											pixels.append((26, 15))
											return 2 # approximately 5 were 2 out of 5 samples at leaf node
										else:
											return 7 # approximately 1 were 7 out of 1 samples at leaf node
								else:
									return 5 # approximately 7 were 5 out of 7 samples at leaf node
						else:
							if features[19][6] <= 23.5:
								pixels.append((19, 6))
								if features[19][11] <= 13.5:
									pixels.append((19, 11))
									if features[15][19] <= 196.5:
										pixels.append((15, 19))
										if features[22][18] <= 73.5:
											pixels.append((22, 18))
											if features[12][11] <= 223.5:
												pixels.append((12, 11))
												if features[11][18] <= 10.5:
													pixels.append((11, 18))
													if features[7][20] <= 2.0:
														pixels.append((7, 20))
														if features[17][11] <= 63.5:
															pixels.append((17, 11))
															if features[7][13] <= 150.0:
																pixels.append((7, 13))
																return 7 # approximately 1 were 7 out of 1 samples at leaf node
															else:
																return 3 # approximately 1 were 3 out of 1 samples at leaf node
														else:
															if features[18][15] <= 252.0:
																pixels.append((18, 15))
																return 2 # approximately 1 were 2 out of 1 samples at leaf node
															else:
																return 4 # approximately 1 were 4 out of 1 samples at leaf node
													else:
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													return 9 # approximately 4 were 9 out of 4 samples at leaf node
											else:
												if features[26][14] <= 98.0:
													pixels.append((26, 14))
													return 4 # approximately 6 were 4 out of 6 samples at leaf node
												else:
													return 7 # approximately 1 were 7 out of 1 samples at leaf node
										else:
											if features[14][13] <= 253.5:
												pixels.append((14, 13))
												return 1 # approximately 6 were 1 out of 6 samples at leaf node
											else:
												return 3 # approximately 1 were 3 out of 1 samples at leaf node
									else:
										if features[9][13] <= 247.5:
											pixels.append((9, 13))
											return 7 # approximately 9 were 7 out of 9 samples at leaf node
										else:
											if features[7][6] <= 253.0:
												pixels.append((7, 6))
												return 3 # approximately 4 were 3 out of 4 samples at leaf node
											else:
												return 7 # approximately 1 were 7 out of 1 samples at leaf node
								else:
									if features[6][20] <= 248.5:
										pixels.append((6, 20))
										if features[17][23] <= 6.5:
											pixels.append((17, 23))
											if features[11][10] <= 82.5:
												pixels.append((11, 10))
												if features[10][17] <= 81.5:
													pixels.append((10, 17))
													return 2 # approximately 3 were 2 out of 3 samples at leaf node
												else:
													if features[18][15] <= 57.5:
														pixels.append((18, 15))
														if features[16][20] <= 6.5:
															pixels.append((16, 20))
															if features[16][10] <= 126.5:
																pixels.append((16, 10))
																return 4 # approximately 1 were 4 out of 1 samples at leaf node
															else:
																return 8 # approximately 1 were 8 out of 1 samples at leaf node
														else:
															return 3 # approximately 2 were 3 out of 2 samples at leaf node
													else:
														return 5 # approximately 3 were 5 out of 3 samples at leaf node
											else:
												if features[25][9] <= 127.0:
													pixels.append((25, 9))
													return 8 # approximately 11 were 8 out of 11 samples at leaf node
												else:
													return 7 # approximately 1 were 7 out of 1 samples at leaf node
										else:
											return 2 # approximately 6 were 2 out of 6 samples at leaf node
									else:
										if features[11][13] <= 198.5:
											pixels.append((11, 13))
											return 1 # approximately 7 were 1 out of 7 samples at leaf node
										else:
											return 6 # approximately 1 were 6 out of 1 samples at leaf node
							else:
								if features[16][9] <= 46.5:
									pixels.append((16, 9))
									return 5 # approximately 17 were 5 out of 17 samples at leaf node
								else:
									if features[17][17] <= 15.0:
										pixels.append((17, 17))
										return 8 # approximately 3 were 8 out of 3 samples at leaf node
									else:
										return 2 # approximately 2 were 2 out of 2 samples at leaf node
				else:
					if features[6][15] <= 86.5:
						pixels.append((6, 15))
						if features[3][9] <= 2.0:
							pixels.append((3, 9))
							if features[3][15] <= 3.0:
								pixels.append((3, 15))
								if features[10][15] <= 145.5:
									pixels.append((10, 15))
									if features[11][14] <= 126.5:
										pixels.append((11, 14))
										if features[3][7] <= 81.0:
											pixels.append((3, 7))
											if features[3][10] <= 10.5:
												pixels.append((3, 10))
												if features[20][5] <= 217.0:
													pixels.append((20, 5))
													if features[25][21] <= 219.5:
														pixels.append((25, 21))
														if features[2][18] <= 11.0:
															pixels.append((2, 18))
															if features[26][15] <= 32.0:
																pixels.append((26, 15))
																if features[26][17] <= 68.5:
																	pixels.append((26, 17))
																	if features[17][3] <= 204.5:
																		pixels.append((17, 3))
																		if features[18][23] <= 245.5:
																			pixels.append((18, 23))
																			if features[20][8] <= 242.0:
																				pixels.append((20, 8))
																				if features[13][26] <= 42.0:
																					pixels.append((13, 26))
																					if features[16][26] <= 66.0:
																						pixels.append((16, 26))
																						if features[11][3] <= 253.5:
																							pixels.append((11, 3))
																							if features[22][6] <= 231.0:
																								pixels.append((22, 6))
																								if features[13][23] <= 254.5:
																									pixels.append((13, 23))
																									if features[1][23] <= 98.5:
																										pixels.append((1, 23))
																										if features[3][13] <= 109.0:
																											pixels.append((3, 13))
																											if features[7][15] <= 169.5:
																												pixels.append((7, 15))
																												if features[20][24] <= 225.0:
																													pixels.append((20, 24))
																													if features[3][17] <= 23.5:
																														pixels.append((3, 17))
																														if features[21][7] <= 246.5:
																															pixels.append((21, 7))
																															if features[6][11] <= 253.5:
																																pixels.append((6, 11))
																																if features[6][15] <= 50.5:
																																	pixels.append((6, 15))
																																	if features[5][14] <= 93.0:
																																		pixels.append((5, 14))
																																		if features[4][13] <= 192.0:
																																			pixels.append((4, 13))
																																			if features[25][20] <= 192.0:
																																				pixels.append((25, 20))
																																				if features[25][16] <= 252.5:
																																					pixels.append((25, 16))
																																					if features[8][13] <= 254.5:
																																						pixels.append((8, 13))
																																						return 4 # approximately 2199 were 4 out of 2199 samples at leaf node
																																					else:
																																						if features[17][15] <= 64.0:
																																							pixels.append((17, 15))
																																							return 9 # approximately 1 were 9 out of 1 samples at leaf node
																																						else:
																																							return 4 # approximately 16 were 4 out of 16 samples at leaf node
																																				else:
																																					if features[9][13] <= 221.5:
																																						pixels.append((9, 13))
																																						return 4 # approximately 13 were 4 out of 13 samples at leaf node
																																					else:
																																						return 9 # approximately 1 were 9 out of 1 samples at leaf node
																																			else:
																																				if features[14][17] <= 247.5:
																																					pixels.append((14, 17))
																																					return 9 # approximately 1 were 9 out of 1 samples at leaf node
																																				else:
																																					return 4 # approximately 8 were 4 out of 8 samples at leaf node
																																		else:
																																			if features[9][11] <= 131.0:
																																				pixels.append((9, 11))
																																				return 0 # approximately 1 were 0 out of 1 samples at leaf node
																																			else:
																																				return 4 # approximately 2 were 4 out of 2 samples at leaf node
																																	else:
																																		if features[13][6] <= 115.5:
																																			pixels.append((13, 6))
																																			if features[5][14] <= 98.0:
																																				pixels.append((5, 14))
																																				return 9 # approximately 1 were 9 out of 1 samples at leaf node
																																			else:
																																				if features[9][10] <= 253.5:
																																					pixels.append((9, 10))
																																					return 4 # approximately 40 were 4 out of 40 samples at leaf node
																																				else:
																																					return 6 # approximately 1 were 6 out of 1 samples at leaf node
																																		else:
																																			return 9 # approximately 2 were 9 out of 2 samples at leaf node
																																else:
																																	if features[10][18] <= 6.5:
																																		pixels.append((10, 18))
																																		return 9 # approximately 2 were 9 out of 2 samples at leaf node
																																	else:
																																		return 4 # approximately 12 were 4 out of 12 samples at leaf node
																															else:
																																if features[7][8] <= 163.5:
																																	pixels.append((7, 8))
																																	if features[13][21] <= 128.5:
																																		pixels.append((13, 21))
																																		if features[10][15] <= 9.5:
																																			pixels.append((10, 15))
																																			return 4 # approximately 56 were 4 out of 56 samples at leaf node
																																		else:
																																			return 9 # approximately 1 were 9 out of 1 samples at leaf node
																																	else:
																																		if features[12][6] <= 86.5:
																																			pixels.append((12, 6))
																																			return 4 # approximately 3 were 4 out of 3 samples at leaf node
																																		else:
																																			if features[17][8] <= 174.5:
																																				pixels.append((17, 8))
																																				return 9 # approximately 2 were 9 out of 2 samples at leaf node
																																			else:
																																				return 6 # approximately 1 were 6 out of 1 samples at leaf node
																																else:
																																	if features[14][7] <= 51.5:
																																		pixels.append((14, 7))
																																		if features[20][19] <= 71.0:
																																			pixels.append((20, 19))
																																			return 3 # approximately 1 were 3 out of 1 samples at leaf node
																																		else:
																																			return 5 # approximately 1 were 5 out of 1 samples at leaf node
																																	else:
																																		return 8 # approximately 1 were 8 out of 1 samples at leaf node
																														else:
																															if features[17][13] <= 3.5:
																																pixels.append((17, 13))
																																return 4 # approximately 1 were 4 out of 1 samples at leaf node
																															else:
																																return 0 # approximately 1 were 0 out of 1 samples at leaf node
																													else:
																														if features[16][15] <= 71.5:
																															pixels.append((16, 15))
																															if features[10][16] <= 3.0:
																																pixels.append((10, 16))
																																return 8 # approximately 1 were 8 out of 1 samples at leaf node
																															else:
																																return 0 # approximately 1 were 0 out of 1 samples at leaf node
																														else:
																															return 4 # approximately 2 were 4 out of 2 samples at leaf node
																												else:
																													return 9 # approximately 1 were 9 out of 1 samples at leaf node
																											else:
																												return 9 # approximately 1 were 9 out of 1 samples at leaf node
																										else:
																											return 6 # approximately 1 were 6 out of 1 samples at leaf node
																									else:
																										return 6 # approximately 1 were 6 out of 1 samples at leaf node
																								else:
																									return 6 # approximately 1 were 6 out of 1 samples at leaf node
																							else:
																								return 8 # approximately 1 were 8 out of 1 samples at leaf node
																						else:
																							return 8 # approximately 1 were 8 out of 1 samples at leaf node
																					else:
																						return 2 # approximately 1 were 2 out of 1 samples at leaf node
																				else:
																					if features[12][8] <= 47.0:
																						pixels.append((12, 8))
																						return 2 # approximately 2 were 2 out of 2 samples at leaf node
																					else:
																						return 4 # approximately 1 were 4 out of 1 samples at leaf node
																			else:
																				if features[17][17] <= 47.0:
																					pixels.append((17, 17))
																					if features[16][12] <= 22.0:
																						pixels.append((16, 12))
																						if features[6][12] <= 46.5:
																							pixels.append((6, 12))
																							return 2 # approximately 1 were 2 out of 1 samples at leaf node
																						else:
																							return 6 # approximately 1 were 6 out of 1 samples at leaf node
																					else:
																						return 8 # approximately 3 were 8 out of 3 samples at leaf node
																				else:
																					if features[12][17] <= 32.0:
																						pixels.append((12, 17))
																						if features[14][19] <= 127.0:
																							pixels.append((14, 19))
																							return 5 # approximately 1 were 5 out of 1 samples at leaf node
																						else:
																							return 0 # approximately 1 were 0 out of 1 samples at leaf node
																					else:
																						return 4 # approximately 12 were 4 out of 12 samples at leaf node
																		else:
																			if features[16][19] <= 250.5:
																				pixels.append((16, 19))
																				if features[10][22] <= 10.5:
																					pixels.append((10, 22))
																					if features[12][16] <= 87.0:
																						pixels.append((12, 16))
																						return 3 # approximately 1 were 3 out of 1 samples at leaf node
																					else:
																						if features[17][24] <= 190.0:
																							pixels.append((17, 24))
																							return 5 # approximately 1 were 5 out of 1 samples at leaf node
																						else:
																							return 6 # approximately 1 were 6 out of 1 samples at leaf node
																				else:
																					return 0 # approximately 1 were 0 out of 1 samples at leaf node
																			else:
																				return 4 # approximately 2 were 4 out of 2 samples at leaf node
																	else:
																		return 2 # approximately 2 were 2 out of 2 samples at leaf node
																else:
																	if features[9][20] <= 94.5:
																		pixels.append((9, 20))
																		return 9 # approximately 3 were 9 out of 3 samples at leaf node
																	else:
																		return 4 # approximately 1 were 4 out of 1 samples at leaf node
															else:
																if features[10][12] <= 11.5:
																	pixels.append((10, 12))
																	return 9 # approximately 3 were 9 out of 3 samples at leaf node
																else:
																	if features[11][9] <= 236.5:
																		pixels.append((11, 9))
																		return 7 # approximately 1 were 7 out of 1 samples at leaf node
																	else:
																		return 4 # approximately 1 were 4 out of 1 samples at leaf node
														else:
															return 2 # approximately 3 were 2 out of 3 samples at leaf node
													else:
														if features[16][15] <= 103.0:
															pixels.append((16, 15))
															return 9 # approximately 4 were 9 out of 4 samples at leaf node
														else:
															return 4 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													if features[19][12] <= 99.0:
														pixels.append((19, 12))
														if features[22][15] <= 17.5:
															pixels.append((22, 15))
															if features[6][20] <= 230.5:
																pixels.append((6, 20))
																return 1 # approximately 1 were 1 out of 1 samples at leaf node
															else:
																return 4 # approximately 1 were 4 out of 1 samples at leaf node
														else:
															return 0 # approximately 1 were 0 out of 1 samples at leaf node
													else:
														return 2 # approximately 4 were 2 out of 4 samples at leaf node
											else:
												if features[19][7] <= 127.0:
													pixels.append((19, 7))
													return 6 # approximately 6 were 6 out of 6 samples at leaf node
												else:
													return 4 # approximately 1 were 4 out of 1 samples at leaf node
										else:
											return 6 # approximately 7 were 6 out of 7 samples at leaf node
									else:
										if features[13][11] <= 237.0:
											pixels.append((13, 11))
											if features[11][11] <= 235.5:
												pixels.append((11, 11))
												if features[11][11] <= 45.0:
													pixels.append((11, 11))
													if features[13][18] <= 165.0:
														pixels.append((13, 18))
														return 2 # approximately 3 were 2 out of 3 samples at leaf node
													else:
														if features[5][11] <= 127.5:
															pixels.append((5, 11))
															return 9 # approximately 3 were 9 out of 3 samples at leaf node
														else:
															return 4 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													return 8 # approximately 4 were 8 out of 4 samples at leaf node
											else:
												if features[17][18] <= 254.5:
													pixels.append((17, 18))
													return 7 # approximately 7 were 7 out of 7 samples at leaf node
												else:
													return 5 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											if features[10][19] <= 23.5:
												pixels.append((10, 19))
												if features[8][14] <= 41.0:
													pixels.append((8, 14))
													if features[15][8] <= 126.0:
														pixels.append((15, 8))
														if features[12][11] <= 219.0:
															pixels.append((12, 11))
															return 4 # approximately 1 were 4 out of 1 samples at leaf node
														else:
															return 6 # approximately 1 were 6 out of 1 samples at leaf node
													else:
														return 5 # approximately 2 were 5 out of 2 samples at leaf node
												else:
													return 3 # approximately 2 were 3 out of 2 samples at leaf node
											else:
												if features[9][22] <= 226.0:
													pixels.append((9, 22))
													return 4 # approximately 19 were 4 out of 19 samples at leaf node
												else:
													return 7 # approximately 1 were 7 out of 1 samples at leaf node
								else:
									if features[14][13] <= 1.5:
										pixels.append((14, 13))
										if features[16][11] <= 143.0:
											pixels.append((16, 11))
											if features[18][4] <= 126.5:
												pixels.append((18, 4))
												return 7 # approximately 30 were 7 out of 30 samples at leaf node
											else:
												return 0 # approximately 1 were 0 out of 1 samples at leaf node
										else:
											if features[13][10] <= 94.5:
												pixels.append((13, 10))
												if features[8][8] <= 125.0:
													pixels.append((8, 8))
													if features[19][17] <= 51.0:
														pixels.append((19, 17))
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														if features[8][11] <= 126.0:
															pixels.append((8, 11))
															return 3 # approximately 1 were 3 out of 1 samples at leaf node
														else:
															return 2 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													return 7 # approximately 2 were 7 out of 2 samples at leaf node
											else:
												return 4 # approximately 5 were 4 out of 5 samples at leaf node
									else:
										if features[8][23] <= 3.5:
											pixels.append((8, 23))
											if features[10][14] <= 135.0:
												pixels.append((10, 14))
												if features[13][9] <= 3.5:
													pixels.append((13, 9))
													if features[17][24] <= 29.0:
														pixels.append((17, 24))
														return 1 # approximately 1 were 1 out of 1 samples at leaf node
													else:
														return 2 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													return 4 # approximately 14 were 4 out of 14 samples at leaf node
											else:
												if features[21][14] <= 151.5:
													pixels.append((21, 14))
													if features[18][8] <= 9.5:
														pixels.append((18, 8))
														if features[17][16] <= 53.0:
															pixels.append((17, 16))
															if features[19][18] <= 22.0:
																pixels.append((19, 18))
																if features[10][16] <= 205.5:
																	pixels.append((10, 16))
																	return 9 # approximately 1 were 9 out of 1 samples at leaf node
																else:
																	if features[15][8] <= 133.0:
																		pixels.append((15, 8))
																		return 5 # approximately 1 were 5 out of 1 samples at leaf node
																	else:
																		if features[18][10] <= 52.0:
																			pixels.append((18, 10))
																			return 1 # approximately 1 were 1 out of 1 samples at leaf node
																		else:
																			return 4 # approximately 1 were 4 out of 1 samples at leaf node
															else:
																return 3 # approximately 2 were 3 out of 2 samples at leaf node
														else:
															if features[6][7] <= 51.0:
																pixels.append((6, 7))
																return 9 # approximately 11 were 9 out of 11 samples at leaf node
															else:
																return 7 # approximately 1 were 7 out of 1 samples at leaf node
													else:
														if features[9][17] <= 30.5:
															pixels.append((9, 17))
															return 2 # approximately 4 were 2 out of 4 samples at leaf node
														else:
															if features[11][19] <= 4.5:
																pixels.append((11, 19))
																return 6 # approximately 3 were 6 out of 3 samples at leaf node
															else:
																if features[13][17] <= 191.0:
																	pixels.append((13, 17))
																	return 0 # approximately 2 were 0 out of 2 samples at leaf node
																else:
																	if features[9][17] <= 176.0:
																		pixels.append((9, 17))
																		return 8 # approximately 1 were 8 out of 1 samples at leaf node
																	else:
																		return 9 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													return 7 # approximately 4 were 7 out of 4 samples at leaf node
										else:
											if features[6][24] <= 192.5:
												pixels.append((6, 24))
												return 5 # approximately 14 were 5 out of 14 samples at leaf node
											else:
												if features[20][14] <= 101.5:
													pixels.append((20, 14))
													if features[8][17] <= 126.5:
														pixels.append((8, 17))
														return 8 # approximately 1 were 8 out of 1 samples at leaf node
													else:
														return 1 # approximately 1 were 1 out of 1 samples at leaf node
												else:
													if features[20][18] <= 113.0:
														pixels.append((20, 18))
														return 0 # approximately 1 were 0 out of 1 samples at leaf node
													else:
														return 4 # approximately 1 were 4 out of 1 samples at leaf node
							else:
								if features[5][18] <= 8.0:
									pixels.append((5, 18))
									return 6 # approximately 42 were 6 out of 42 samples at leaf node
								else:
									return 2 # approximately 14 were 2 out of 14 samples at leaf node
						else:
							if features[20][14] <= 30.0:
								pixels.append((20, 14))
								if features[10][16] <= 130.0:
									pixels.append((10, 16))
									return 4 # approximately 5 were 4 out of 5 samples at leaf node
								else:
									return 6 # approximately 1 were 6 out of 1 samples at leaf node
							else:
								return 6 # approximately 76 were 6 out of 76 samples at leaf node
					else:
						if features[7][22] <= 1.0:
							pixels.append((7, 22))
							if features[17][16] <= 12.5:
								pixels.append((17, 16))
								if features[6][17] <= 189.0:
									pixels.append((6, 17))
									if features[20][10] <= 2.5:
										pixels.append((20, 10))
										return 9 # approximately 12 were 9 out of 12 samples at leaf node
									else:
										if features[18][6] <= 126.5:
											pixels.append((18, 6))
											if features[8][22] <= 48.5:
												pixels.append((8, 22))
												if features[21][16] <= 127.0:
													pixels.append((21, 16))
													if features[6][14] <= 116.0:
														pixels.append((6, 14))
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														return 7 # approximately 1 were 7 out of 1 samples at leaf node
												else:
													return 6 # approximately 1 were 6 out of 1 samples at leaf node
											else:
												return 4 # approximately 1 were 4 out of 1 samples at leaf node
										else:
											return 2 # approximately 1 were 2 out of 1 samples at leaf node
								else:
									if features[24][9] <= 32.0:
										pixels.append((24, 9))
										if features[24][17] <= 34.0:
											pixels.append((24, 17))
											if features[19][18] <= 4.5:
												pixels.append((19, 18))
												return 7 # approximately 2 were 7 out of 2 samples at leaf node
											else:
												return 2 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											return 5 # approximately 2 were 5 out of 2 samples at leaf node
									else:
										return 3 # approximately 4 were 3 out of 4 samples at leaf node
							else:
								if features[10][12] <= 227.5:
									pixels.append((10, 12))
									if features[6][11] <= 156.0:
										pixels.append((6, 11))
										if features[8][8] <= 206.5:
											pixels.append((8, 8))
											return 9 # approximately 115 were 9 out of 115 samples at leaf node
										else:
											return 3 # approximately 1 were 3 out of 1 samples at leaf node
									else:
										return 7 # approximately 2 were 7 out of 2 samples at leaf node
								else:
									return 4 # approximately 2 were 4 out of 2 samples at leaf node
						else:
							if features[14][9] <= 211.0:
								pixels.append((14, 9))
								if features[16][14] <= 12.5:
									pixels.append((16, 14))
									if features[23][12] <= 127.5:
										pixels.append((23, 12))
										return 2 # approximately 1 were 2 out of 1 samples at leaf node
									else:
										return 3 # approximately 1 were 3 out of 1 samples at leaf node
								else:
									return 8 # approximately 2 were 8 out of 2 samples at leaf node
							else:
								return 4 # approximately 4 were 4 out of 4 samples at leaf node
			else:
				if features[6][18] <= 5.0:
					pixels.append((6, 18))
					if features[20][15] <= 13.5:
						pixels.append((20, 15))
						if features[17][18] <= 237.5:
							pixels.append((17, 18))
							if features[13][14] <= 21.0:
								pixels.append((13, 14))
								if features[8][13] <= 9.0:
									pixels.append((8, 13))
									return 6 # approximately 8 were 6 out of 8 samples at leaf node
								else:
									if features[21][6] <= 4.5:
										pixels.append((21, 6))
										if features[16][5] <= 42.5:
											pixels.append((16, 5))
											return 3 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											return 4 # approximately 1 were 4 out of 1 samples at leaf node
									else:
										return 0 # approximately 1 were 0 out of 1 samples at leaf node
							else:
								return 5 # approximately 3 were 5 out of 3 samples at leaf node
						else:
							return 4 # approximately 5 were 4 out of 5 samples at leaf node
					else:
						if features[8][14] <= 105.5:
							pixels.append((8, 14))
							if features[8][18] <= 93.5:
								pixels.append((8, 18))
								if features[8][21] <= 251.5:
									pixels.append((8, 21))
									if features[11][15] <= 254.5:
										pixels.append((11, 15))
										if features[4][15] <= 214.0:
											pixels.append((4, 15))
											if features[6][14] <= 241.0:
												pixels.append((6, 14))
												if features[22][15] <= 253.5:
													pixels.append((22, 15))
													return 6 # approximately 555 were 6 out of 555 samples at leaf node
												else:
													if features[14][15] <= 248.0:
														pixels.append((14, 15))
														return 6 # approximately 4 were 6 out of 4 samples at leaf node
													else:
														return 8 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												if features[6][13] <= 251.5:
													pixels.append((6, 13))
													return 5 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													return 6 # approximately 1 were 6 out of 1 samples at leaf node
										else:
											return 5 # approximately 1 were 5 out of 1 samples at leaf node
									else:
										return 5 # approximately 1 were 5 out of 1 samples at leaf node
								else:
									return 4 # approximately 1 were 4 out of 1 samples at leaf node
							else:
								return 4 # approximately 2 were 4 out of 2 samples at leaf node
						else:
							return 1 # approximately 2 were 1 out of 2 samples at leaf node
				else:
					if features[22][13] <= 27.0:
						pixels.append((22, 13))
						return 2 # approximately 22 were 2 out of 22 samples at leaf node
					else:
						if features[10][10] <= 39.0:
							pixels.append((10, 10))
							return 3 # approximately 3 were 3 out of 3 samples at leaf node
						else:
							return 6 # approximately 1 were 6 out of 1 samples at leaf node
		else:
			if features[15][11] <= 0.5:
				pixels.append((15, 11))
				if features[13][13] <= 9.5:
					pixels.append((13, 13))
					if features[17][9] <= 4.5:
						pixels.append((17, 9))
						if features[5][12] <= 10.0:
							pixels.append((5, 12))
							if features[19][6] <= 7.5:
								pixels.append((19, 6))
								if features[5][18] <= 15.0:
									pixels.append((5, 18))
									if features[19][21] <= 25.5:
										pixels.append((19, 21))
										if features[16][10] <= 123.5:
											pixels.append((16, 10))
											if features[21][21] <= 122.0:
												pixels.append((21, 21))
												if features[18][8] <= 167.5:
													pixels.append((18, 8))
													if features[24][22] <= 42.0:
														pixels.append((24, 22))
														if features[17][22] <= 83.0:
															pixels.append((17, 22))
															if features[13][24] <= 112.5:
																pixels.append((13, 24))
																if features[12][14] <= 197.0:
																	pixels.append((12, 14))
																	if features[9][13] <= 10.5:
																		pixels.append((9, 13))
																		if features[11][13] <= 35.5:
																			pixels.append((11, 13))
																			if features[24][18] <= 70.0:
																				pixels.append((24, 18))
																				if features[22][17] <= 234.5:
																					pixels.append((22, 17))
																					if features[6][22] <= 102.0:
																						pixels.append((6, 22))
																						if features[15][20] <= 253.5:
																							pixels.append((15, 20))
																							if features[9][6] <= 253.5:
																								pixels.append((9, 6))
																								if features[10][15] <= 167.5:
																									pixels.append((10, 15))
																									if features[14][17] <= 8.0:
																										pixels.append((14, 17))
																										if features[15][14] <= 197.5:
																											pixels.append((15, 14))
																											return 7 # approximately 3 were 7 out of 3 samples at leaf node
																										else:
																											return 2 # approximately 1 were 2 out of 1 samples at leaf node
																									else:
																										return 7 # approximately 221 were 7 out of 221 samples at leaf node
																								else:
																									if features[25][13] <= 10.5:
																										pixels.append((25, 13))
																										return 3 # approximately 1 were 3 out of 1 samples at leaf node
																									else:
																										return 7 # approximately 3 were 7 out of 3 samples at leaf node
																							else:
																								return 2 # approximately 1 were 2 out of 1 samples at leaf node
																						else:
																							return 2 # approximately 1 were 2 out of 1 samples at leaf node
																					else:
																						return 3 # approximately 1 were 3 out of 1 samples at leaf node
																				else:
																					return 3 # approximately 2 were 3 out of 2 samples at leaf node
																			else:
																				if features[18][18] <= 4.0:
																					pixels.append((18, 18))
																					return 2 # approximately 6 were 2 out of 6 samples at leaf node
																				else:
																					if features[23][18] <= 247.0:
																						pixels.append((23, 18))
																						return 7 # approximately 4 were 7 out of 4 samples at leaf node
																					else:
																						return 3 # approximately 1 were 3 out of 1 samples at leaf node
																		else:
																			if features[11][5] <= 72.0:
																				pixels.append((11, 5))
																				return 9 # approximately 10 were 9 out of 10 samples at leaf node
																			else:
																				return 7 # approximately 1 were 7 out of 1 samples at leaf node
																	else:
																		if features[14][13] <= 179.0:
																			pixels.append((14, 13))
																			if features[5][10] <= 226.5:
																				pixels.append((5, 10))
																				if features[18][3] <= 77.0:
																					pixels.append((18, 3))
																					if features[14][11] <= 193.0:
																						pixels.append((14, 11))
																						if features[26][5] <= 145.0:
																							pixels.append((26, 5))
																							if features[14][13] <= 124.5:
																								pixels.append((14, 13))
																								if features[16][10] <= 41.5:
																									pixels.append((16, 10))
																									if features[12][13] <= 138.5:
																										pixels.append((12, 13))
																										if features[6][14] <= 202.5:
																											pixels.append((6, 14))
																											if features[24][7] <= 253.5:
																												pixels.append((24, 7))
																												if features[15][17] <= 23.5:
																													pixels.append((15, 17))
																													if features[16][20] <= 171.5:
																														pixels.append((16, 20))
																														if features[15][8] <= 184.0:
																															pixels.append((15, 8))
																															if features[6][15] <= 238.0:
																																pixels.append((6, 15))
																																if features[11][13] <= 90.0:
																																	pixels.append((11, 13))
																																	return 7 # approximately 140 were 7 out of 140 samples at leaf node
																																else:
																																	if features[16][15] <= 253.5:
																																		pixels.append((16, 15))
																																		return 7 # approximately 9 were 7 out of 9 samples at leaf node
																																	else:
																																		return 9 # approximately 2 were 9 out of 2 samples at leaf node
																															else:
																																return 9 # approximately 1 were 9 out of 1 samples at leaf node
																														else:
																															return 9 # approximately 1 were 9 out of 1 samples at leaf node
																													else:
																														return 3 # approximately 1 were 3 out of 1 samples at leaf node
																												else:
																													if features[21][19] <= 253.5:
																														pixels.append((21, 19))
																														if features[15][12] <= 19.0:
																															pixels.append((15, 12))
																															return 7 # approximately 2457 were 7 out of 2457 samples at leaf node
																														else:
																															if features[14][15] <= 98.5:
																																pixels.append((14, 15))
																																return 3 # approximately 1 were 3 out of 1 samples at leaf node
																															else:
																																return 7 # approximately 16 were 7 out of 16 samples at leaf node
																													else:
																														if features[10][9] <= 1.5:
																															pixels.append((10, 9))
																															return 2 # approximately 1 were 2 out of 1 samples at leaf node
																														else:
																															return 7 # approximately 7 were 7 out of 7 samples at leaf node
																											else:
																												if features[10][14] <= 20.5:
																													pixels.append((10, 14))
																													return 2 # approximately 1 were 2 out of 1 samples at leaf node
																												else:
																													return 7 # approximately 5 were 7 out of 5 samples at leaf node
																										else:
																											if features[6][14] <= 209.0:
																												pixels.append((6, 14))
																												return 3 # approximately 2 were 3 out of 2 samples at leaf node
																											else:
																												if features[25][16] <= 251.0:
																													pixels.append((25, 16))
																													if features[6][12] <= 254.5:
																														pixels.append((6, 12))
																														return 7 # approximately 67 were 7 out of 67 samples at leaf node
																													else:
																														if features[24][14] <= 105.0:
																															pixels.append((24, 14))
																															return 7 # approximately 4 were 7 out of 4 samples at leaf node
																														else:
																															return 3 # approximately 1 were 3 out of 1 samples at leaf node
																												else:
																													if features[14][17] <= 130.5:
																														pixels.append((14, 17))
																														return 7 # approximately 1 were 7 out of 1 samples at leaf node
																													else:
																														return 2 # approximately 1 were 2 out of 1 samples at leaf node
																									else:
																										if features[10][13] <= 175.0:
																											pixels.append((10, 13))
																											return 9 # approximately 2 were 9 out of 2 samples at leaf node
																										else:
																											if features[6][13] <= 127.5:
																												pixels.append((6, 13))
																												return 7 # approximately 28 were 7 out of 28 samples at leaf node
																											else:
																												return 5 # approximately 1 were 5 out of 1 samples at leaf node
																								else:
																									if features[12][18] <= 253.0:
																										pixels.append((12, 18))
																										return 7 # approximately 3 were 7 out of 3 samples at leaf node
																									else:
																										return 9 # approximately 1 were 9 out of 1 samples at leaf node
																							else:
																								if features[7][23] <= 41.5:
																									pixels.append((7, 23))
																									return 7 # approximately 2 were 7 out of 2 samples at leaf node
																								else:
																									return 3 # approximately 1 were 3 out of 1 samples at leaf node
																						else:
																							if features[9][22] <= 86.5:
																								pixels.append((9, 22))
																								if features[12][17] <= 6.5:
																									pixels.append((12, 17))
																									return 9 # approximately 1 were 9 out of 1 samples at leaf node
																								else:
																									return 4 # approximately 1 were 4 out of 1 samples at leaf node
																							else:
																								return 7 # approximately 6 were 7 out of 6 samples at leaf node
																					else:
																						return 9 # approximately 1 were 9 out of 1 samples at leaf node
																				else:
																					return 3 # approximately 1 were 3 out of 1 samples at leaf node
																			else:
																				return 4 # approximately 1 were 4 out of 1 samples at leaf node
																		else:
																			return 8 # approximately 1 were 8 out of 1 samples at leaf node
																else:
																	if features[6][17] <= 51.5:
																		pixels.append((6, 17))
																		if features[6][7] <= 103.5:
																			pixels.append((6, 7))
																			return 7 # approximately 17 were 7 out of 17 samples at leaf node
																		else:
																			return 3 # approximately 1 were 3 out of 1 samples at leaf node
																	else:
																		if features[11][17] <= 208.5:
																			pixels.append((11, 17))
																			if features[12][12] <= 40.0:
																				pixels.append((12, 12))
																				return 3 # approximately 2 were 3 out of 2 samples at leaf node
																			else:
																				if features[10][5] <= 24.0:
																					pixels.append((10, 5))
																					return 5 # approximately 1 were 5 out of 1 samples at leaf node
																				else:
																					return 8 # approximately 1 were 8 out of 1 samples at leaf node
																		else:
																			return 9 # approximately 4 were 9 out of 4 samples at leaf node
															else:
																return 2 # approximately 2 were 2 out of 2 samples at leaf node
														else:
															if features[11][18] <= 215.5:
																pixels.append((11, 18))
																return 2 # approximately 5 were 2 out of 5 samples at leaf node
															else:
																return 7 # approximately 6 were 7 out of 6 samples at leaf node
													else:
														if features[10][8] <= 126.5:
															pixels.append((10, 8))
															return 2 # approximately 3 were 2 out of 3 samples at leaf node
														else:
															return 7 # approximately 1 were 7 out of 1 samples at leaf node
												else:
													if features[7][23] <= 115.5:
														pixels.append((7, 23))
														if features[10][12] <= 109.0:
															pixels.append((10, 12))
															return 9 # approximately 1 were 9 out of 1 samples at leaf node
														else:
															return 0 # approximately 1 were 0 out of 1 samples at leaf node
													else:
														return 5 # approximately 2 were 5 out of 2 samples at leaf node
											else:
												return 2 # approximately 3 were 2 out of 3 samples at leaf node
										else:
											return 9 # approximately 5 were 9 out of 5 samples at leaf node
									else:
										if features[16][13] <= 62.0:
											pixels.append((16, 13))
											if features[22][10] <= 92.5:
												pixels.append((22, 10))
												if features[8][16] <= 9.5:
													pixels.append((8, 16))
													return 2 # approximately 2 were 2 out of 2 samples at leaf node
												else:
													if features[25][10] <= 252.5:
														pixels.append((25, 10))
														if features[21][11] <= 203.0:
															pixels.append((21, 11))
															return 7 # approximately 19 were 7 out of 19 samples at leaf node
														else:
															return 2 # approximately 1 were 2 out of 1 samples at leaf node
													else:
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												if features[19][14] <= 120.0:
													pixels.append((19, 14))
													return 3 # approximately 3 were 3 out of 3 samples at leaf node
												else:
													if features[20][8] <= 13.0:
														pixels.append((20, 8))
														return 9 # approximately 1 were 9 out of 1 samples at leaf node
													else:
														return 2 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											if features[14][20] <= 15.0:
												pixels.append((14, 20))
												return 2 # approximately 16 were 2 out of 16 samples at leaf node
											else:
												if features[15][4] <= 64.0:
													pixels.append((15, 4))
													return 3 # approximately 4 were 3 out of 4 samples at leaf node
												else:
													return 9 # approximately 1 were 9 out of 1 samples at leaf node
								else:
									if features[10][17] <= 87.5:
										pixels.append((10, 17))
										if features[19][14] <= 15.5:
											pixels.append((19, 14))
											return 5 # approximately 5 were 5 out of 5 samples at leaf node
										else:
											if features[16][15] <= 239.5:
												pixels.append((16, 15))
												if features[14][17] <= 29.0:
													pixels.append((14, 17))
													return 0 # approximately 1 were 0 out of 1 samples at leaf node
												else:
													if features[17][17] <= 5.5:
														pixels.append((17, 17))
														return 4 # approximately 1 were 4 out of 1 samples at leaf node
													else:
														if features[15][13] <= 114.0:
															pixels.append((15, 13))
															if features[8][18] <= 133.5:
																pixels.append((8, 18))
																return 9 # approximately 1 were 9 out of 1 samples at leaf node
															else:
																return 3 # approximately 1 were 3 out of 1 samples at leaf node
														else:
															return 6 # approximately 1 were 6 out of 1 samples at leaf node
											else:
												return 8 # approximately 3 were 8 out of 3 samples at leaf node
									else:
										if features[14][18] <= 95.5:
											pixels.append((14, 18))
											return 1 # approximately 11 were 1 out of 11 samples at leaf node
										else:
											return 2 # approximately 1 were 2 out of 1 samples at leaf node
							else:
								if features[12][20] <= 75.5:
									pixels.append((12, 20))
									if features[11][14] <= 158.5:
										pixels.append((11, 14))
										if features[7][12] <= 0.5:
											pixels.append((7, 12))
											return 6 # approximately 6 were 6 out of 6 samples at leaf node
										else:
											if features[21][9] <= 121.5:
												pixels.append((21, 9))
												return 7 # approximately 3 were 7 out of 3 samples at leaf node
											else:
												if features[6][17] <= 77.0:
													pixels.append((6, 17))
													return 2 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													return 5 # approximately 1 were 5 out of 1 samples at leaf node
									else:
										if features[16][7] <= 169.0:
											pixels.append((16, 7))
											return 5 # approximately 17 were 5 out of 17 samples at leaf node
										else:
											return 0 # approximately 1 were 0 out of 1 samples at leaf node
								else:
									if features[7][21] <= 115.0:
										pixels.append((7, 21))
										return 9 # approximately 8 were 9 out of 8 samples at leaf node
									else:
										if features[16][6] <= 76.5:
											pixels.append((16, 6))
											return 2 # approximately 2 were 2 out of 2 samples at leaf node
										else:
											return 0 # approximately 20 were 0 out of 20 samples at leaf node
						else:
							if features[11][14] <= 162.5:
								pixels.append((11, 14))
								if features[24][10] <= 0.5:
									pixels.append((24, 10))
									if features[24][6] <= 81.0:
										pixels.append((24, 6))
										if features[11][8] <= 239.5:
											pixels.append((11, 8))
											if features[12][14] <= 58.0:
												pixels.append((12, 14))
												if features[6][13] <= 26.0:
													pixels.append((6, 13))
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													if features[23][5] <= 115.0:
														pixels.append((23, 5))
														return 2 # approximately 44 were 2 out of 44 samples at leaf node
													else:
														return 3 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												if features[16][12] <= 9.5:
													pixels.append((16, 12))
													return 7 # approximately 3 were 7 out of 3 samples at leaf node
												else:
													return 2 # approximately 4 were 2 out of 4 samples at leaf node
										else:
											return 7 # approximately 2 were 7 out of 2 samples at leaf node
									else:
										return 7 # approximately 2 were 7 out of 2 samples at leaf node
								else:
									if features[17][14] <= 95.0:
										pixels.append((17, 14))
										if features[20][18] <= 158.5:
											pixels.append((20, 18))
											return 2 # approximately 3 were 2 out of 3 samples at leaf node
										else:
											return 3 # approximately 1 were 3 out of 1 samples at leaf node
									else:
										return 7 # approximately 8 were 7 out of 8 samples at leaf node
							else:
								if features[15][14] <= 92.5:
									pixels.append((15, 14))
									if features[9][14] <= 22.0:
										pixels.append((9, 14))
										return 5 # approximately 4 were 5 out of 4 samples at leaf node
									else:
										if features[9][7] <= 240.0:
											pixels.append((9, 7))
											return 3 # approximately 6 were 3 out of 6 samples at leaf node
										else:
											if features[15][21] <= 122.0:
												pixels.append((15, 21))
												return 2 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												if features[19][10] <= 41.0:
													pixels.append((19, 10))
													return 0 # approximately 1 were 0 out of 1 samples at leaf node
												else:
													return 7 # approximately 1 were 7 out of 1 samples at leaf node
								else:
									return 1 # approximately 4 were 1 out of 4 samples at leaf node
					else:
						if features[15][8] <= 1.0:
							pixels.append((15, 8))
							if features[15][6] <= 23.5:
								pixels.append((15, 6))
								if features[20][9] <= 1.0:
									pixels.append((20, 9))
									if features[18][6] <= 162.5:
										pixels.append((18, 6))
										if features[15][10] <= 47.5:
											pixels.append((15, 10))
											if features[20][18] <= 175.5:
												pixels.append((20, 18))
												if features[22][8] <= 196.5:
													pixels.append((22, 8))
													if features[21][20] <= 126.5:
														pixels.append((21, 20))
														return 7 # approximately 57 were 7 out of 57 samples at leaf node
													else:
														return 9 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												if features[6][14] <= 53.5:
													pixels.append((6, 14))
													return 3 # approximately 3 were 3 out of 3 samples at leaf node
												else:
													if features[12][7] <= 12.0:
														pixels.append((12, 7))
														return 2 # approximately 1 were 2 out of 1 samples at leaf node
													else:
														return 7 # approximately 1 were 7 out of 1 samples at leaf node
										else:
											if features[14][16] <= 222.0:
												pixels.append((14, 16))
												if features[20][12] <= 84.0:
													pixels.append((20, 12))
													return 7 # approximately 1 were 7 out of 1 samples at leaf node
												else:
													return 8 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												return 9 # approximately 4 were 9 out of 4 samples at leaf node
									else:
										if features[10][7] <= 30.5:
											pixels.append((10, 7))
											return 2 # approximately 3 were 2 out of 3 samples at leaf node
										else:
											if features[6][12] <= 46.0:
												pixels.append((6, 12))
												return 9 # approximately 2 were 9 out of 2 samples at leaf node
											else:
												return 3 # approximately 1 were 3 out of 1 samples at leaf node
								else:
									if features[24][9] <= 52.0:
										pixels.append((24, 9))
										if features[24][5] <= 21.5:
											pixels.append((24, 5))
											if features[25][13] <= 7.0:
												pixels.append((25, 13))
												if features[17][12] <= 62.0:
													pixels.append((17, 12))
													if features[17][14] <= 125.5:
														pixels.append((17, 14))
														if features[11][20] <= 202.5:
															pixels.append((11, 20))
															return 0 # approximately 1 were 0 out of 1 samples at leaf node
														else:
															if features[6][17] <= 233.5:
																pixels.append((6, 17))
																return 3 # approximately 1 were 3 out of 1 samples at leaf node
															else:
																return 2 # approximately 1 were 2 out of 1 samples at leaf node
													else:
														return 7 # approximately 2 were 7 out of 2 samples at leaf node
												else:
													return 2 # approximately 51 were 2 out of 51 samples at leaf node
											else:
												if features[9][21] <= 23.0:
													pixels.append((9, 21))
													return 7 # approximately 3 were 7 out of 3 samples at leaf node
												else:
													return 2 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											return 7 # approximately 4 were 7 out of 4 samples at leaf node
									else:
										if features[11][13] <= 116.5:
											pixels.append((11, 13))
											return 7 # approximately 9 were 7 out of 9 samples at leaf node
										else:
											return 8 # approximately 2 were 8 out of 2 samples at leaf node
							else:
								if features[11][10] <= 251.0:
									pixels.append((11, 10))
									if features[11][15] <= 194.0:
										pixels.append((11, 15))
										return 9 # approximately 38 were 9 out of 38 samples at leaf node
									else:
										return 7 # approximately 1 were 7 out of 1 samples at leaf node
								else:
									if features[7][13] <= 14.0:
										pixels.append((7, 13))
										return 9 # approximately 1 were 9 out of 1 samples at leaf node
									else:
										return 4 # approximately 2 were 4 out of 2 samples at leaf node
						else:
							if features[7][13] <= 5.5:
								pixels.append((7, 13))
								if features[9][13] <= 179.5:
									pixels.append((9, 13))
									if features[7][16] <= 119.0:
										pixels.append((7, 16))
										if features[22][10] <= 58.5:
											pixels.append((22, 10))
											return 9 # approximately 3 were 9 out of 3 samples at leaf node
										else:
											if features[18][11] <= 147.5:
												pixels.append((18, 11))
												return 5 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												return 8 # approximately 1 were 8 out of 1 samples at leaf node
									else:
										return 4 # approximately 20 were 4 out of 20 samples at leaf node
								else:
									if features[14][11] <= 7.5:
										pixels.append((14, 11))
										if features[17][11] <= 35.0:
											pixels.append((17, 11))
											if features[19][13] <= 94.0:
												pixels.append((19, 13))
												return 7 # approximately 10 were 7 out of 10 samples at leaf node
											else:
												return 9 # approximately 1 were 9 out of 1 samples at leaf node
										else:
											if features[16][20] <= 10.0:
												pixels.append((16, 20))
												if features[20][9] <= 230.5:
													pixels.append((20, 9))
													if features[7][25] <= 67.5:
														pixels.append((7, 25))
														return 9 # approximately 19 were 9 out of 19 samples at leaf node
													else:
														return 4 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													if features[11][25] <= 99.0:
														pixels.append((11, 25))
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														return 8 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												return 4 # approximately 4 were 4 out of 4 samples at leaf node
									else:
										if features[9][20] <= 24.5:
											pixels.append((9, 20))
											return 6 # approximately 13 were 6 out of 13 samples at leaf node
										else:
											if features[7][15] <= 76.0:
												pixels.append((7, 15))
												return 9 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												return 0 # approximately 2 were 0 out of 2 samples at leaf node
							else:
								if features[17][12] <= 1.5:
									pixels.append((17, 12))
									if features[15][10] <= 37.5:
										pixels.append((15, 10))
										if features[21][14] <= 131.5:
											pixels.append((21, 14))
											if features[19][5] <= 120.0:
												pixels.append((19, 5))
												return 9 # approximately 19 were 9 out of 19 samples at leaf node
											else:
												return 3 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											if features[21][13] <= 78.0:
												pixels.append((21, 13))
												return 7 # approximately 2 were 7 out of 2 samples at leaf node
											else:
												if features[20][13] <= 148.0:
													pixels.append((20, 13))
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													return 0 # approximately 2 were 0 out of 2 samples at leaf node
									else:
										if features[21][9] <= 12.0:
											pixels.append((21, 9))
											return 7 # approximately 14 were 7 out of 14 samples at leaf node
										else:
											return 0 # approximately 7 were 0 out of 7 samples at leaf node
								else:
									if features[16][22] <= 148.0:
										pixels.append((16, 22))
										if features[19][5] <= 97.0:
											pixels.append((19, 5))
											if features[5][22] <= 95.5:
												pixels.append((5, 22))
												if features[11][12] <= 253.5:
													pixels.append((11, 12))
													if features[5][18] <= 244.5:
														pixels.append((5, 18))
														if features[5][9] <= 9.5:
															pixels.append((5, 9))
															if features[11][25] <= 69.5:
																pixels.append((11, 25))
																if features[19][21] <= 254.5:
																	pixels.append((19, 21))
																	if features[13][10] <= 254.5:
																		pixels.append((13, 10))
																		if features[23][15] <= 254.5:
																			pixels.append((23, 15))
																			if features[7][19] <= 253.5:
																				pixels.append((7, 19))
																				return 9 # approximately 288 were 9 out of 288 samples at leaf node
																			else:
																				if features[17][20] <= 10.5:
																					pixels.append((17, 20))
																					return 9 # approximately 4 were 9 out of 4 samples at leaf node
																				else:
																					return 7 # approximately 1 were 7 out of 1 samples at leaf node
																		else:
																			if features[17][15] <= 100.5:
																				pixels.append((17, 15))
																				return 4 # approximately 1 were 4 out of 1 samples at leaf node
																			else:
																				return 9 # approximately 3 were 9 out of 3 samples at leaf node
																	else:
																		return 4 # approximately 1 were 4 out of 1 samples at leaf node
																else:
																	return 2 # approximately 1 were 2 out of 1 samples at leaf node
															else:
																return 8 # approximately 1 were 8 out of 1 samples at leaf node
														else:
															return 0 # approximately 1 were 0 out of 1 samples at leaf node
													else:
														if features[13][16] <= 23.5:
															pixels.append((13, 16))
															return 6 # approximately 1 were 6 out of 1 samples at leaf node
														else:
															return 4 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													return 4 # approximately 3 were 4 out of 3 samples at leaf node
											else:
												if features[9][11] <= 246.5:
													pixels.append((9, 11))
													return 4 # approximately 3 were 4 out of 3 samples at leaf node
												else:
													return 5 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											if features[17][19] <= 126.5:
												pixels.append((17, 19))
												return 2 # approximately 3 were 2 out of 3 samples at leaf node
											else:
												return 0 # approximately 1 were 0 out of 1 samples at leaf node
									else:
										if features[7][13] <= 136.5:
											pixels.append((7, 13))
											return 4 # approximately 3 were 4 out of 3 samples at leaf node
										else:
											if features[6][13] <= 10.0:
												pixels.append((6, 13))
												if features[18][13] <= 157.0:
													pixels.append((18, 13))
													return 2 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													return 7 # approximately 1 were 7 out of 1 samples at leaf node
											else:
												return 6 # approximately 2 were 6 out of 2 samples at leaf node
				else:
					if features[7][22] <= 3.5:
						pixels.append((7, 22))
						if features[17][15] <= 10.5:
							pixels.append((17, 15))
							if features[6][9] <= 1.5:
								pixels.append((6, 9))
								if features[10][17] <= 6.0:
									pixels.append((10, 17))
									if features[7][17] <= 3.5:
										pixels.append((7, 17))
										if features[8][11] <= 88.0:
											pixels.append((8, 11))
											return 3 # approximately 6 were 3 out of 6 samples at leaf node
										else:
											if features[15][18] <= 19.0:
												pixels.append((15, 18))
												return 5 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												return 9 # approximately 5 were 9 out of 5 samples at leaf node
									else:
										if features[16][13] <= 5.0:
											pixels.append((16, 13))
											if features[8][6] <= 134.5:
												pixels.append((8, 6))
												if features[11][7] <= 252.5:
													pixels.append((11, 7))
													return 5 # approximately 59 were 5 out of 59 samples at leaf node
												else:
													if features[15][20] <= 253.5:
														pixels.append((15, 20))
														return 9 # approximately 1 were 9 out of 1 samples at leaf node
													else:
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												if features[17][5] <= 80.0:
													pixels.append((17, 5))
													return 3 # approximately 3 were 3 out of 3 samples at leaf node
												else:
													return 5 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											if features[19][16] <= 116.5:
												pixels.append((19, 16))
												if features[23][13] <= 40.0:
													pixels.append((23, 13))
													if features[19][9] <= 45.0:
														pixels.append((19, 9))
														return 2 # approximately 1 were 2 out of 1 samples at leaf node
													else:
														return 9 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													if features[14][18] <= 32.0:
														pixels.append((14, 18))
														return 4 # approximately 1 were 4 out of 1 samples at leaf node
													else:
														return 8 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												return 6 # approximately 1 were 6 out of 1 samples at leaf node
								else:
									if features[11][8] <= 57.0:
										pixels.append((11, 8))
										if features[17][13] <= 13.0:
											pixels.append((17, 13))
											if features[11][10] <= 234.5:
												pixels.append((11, 10))
												if features[20][17] <= 253.5:
													pixels.append((20, 17))
													if features[10][13] <= 253.5:
														pixels.append((10, 13))
														return 3 # approximately 19 were 3 out of 19 samples at leaf node
													else:
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													return 9 # approximately 2 were 9 out of 2 samples at leaf node
											else:
												if features[8][10] <= 158.0:
													pixels.append((8, 10))
													return 5 # approximately 2 were 5 out of 2 samples at leaf node
												else:
													return 9 # approximately 1 were 9 out of 1 samples at leaf node
										else:
											if features[13][13] <= 156.5:
												pixels.append((13, 13))
												if features[7][17] <= 196.5:
													pixels.append((7, 17))
													return 2 # approximately 2 were 2 out of 2 samples at leaf node
												else:
													if features[18][11] <= 63.5:
														pixels.append((18, 11))
														return 7 # approximately 1 were 7 out of 1 samples at leaf node
													else:
														return 1 # approximately 2 were 1 out of 2 samples at leaf node
											else:
												if features[9][14] <= 252.0:
													pixels.append((9, 14))
													return 8 # approximately 5 were 8 out of 5 samples at leaf node
												else:
													return 4 # approximately 1 were 4 out of 1 samples at leaf node
									else:
										if features[10][11] <= 243.5:
											pixels.append((10, 11))
											if features[19][21] <= 216.0:
												pixels.append((19, 21))
												if features[8][6] <= 193.0:
													pixels.append((8, 6))
													return 9 # approximately 20 were 9 out of 20 samples at leaf node
												else:
													return 4 # approximately 1 were 4 out of 1 samples at leaf node
											else:
												if features[10][7] <= 244.0:
													pixels.append((10, 7))
													return 2 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													return 5 # approximately 2 were 5 out of 2 samples at leaf node
										else:
											if features[13][12] <= 195.0:
												pixels.append((13, 12))
												return 7 # approximately 7 were 7 out of 7 samples at leaf node
											else:
												if features[14][12] <= 45.5:
													pixels.append((14, 12))
													if features[20][15] <= 237.5:
														pixels.append((20, 15))
														return 3 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														return 0 # approximately 1 were 0 out of 1 samples at leaf node
												else:
													return 5 # approximately 3 were 5 out of 3 samples at leaf node
							else:
								if features[10][9] <= 41.5:
									pixels.append((10, 9))
									if features[13][8] <= 253.5:
										pixels.append((13, 8))
										if features[17][12] <= 113.5:
											pixels.append((17, 12))
											if features[11][7] <= 253.5:
												pixels.append((11, 7))
												return 3 # approximately 116 were 3 out of 116 samples at leaf node
											else:
												return 9 # approximately 1 were 9 out of 1 samples at leaf node
										else:
											return 7 # approximately 1 were 7 out of 1 samples at leaf node
									else:
										if features[8][15] <= 182.0:
											pixels.append((8, 15))
											return 5 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											return 2 # approximately 1 were 2 out of 1 samples at leaf node
								else:
									if features[6][17] <= 1.0:
										pixels.append((6, 17))
										if features[18][19] <= 1.0:
											pixels.append((18, 19))
											if features[14][20] <= 35.0:
												pixels.append((14, 20))
												return 9 # approximately 3 were 9 out of 3 samples at leaf node
											else:
												return 8 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											if features[8][13] <= 101.0:
												pixels.append((8, 13))
												if features[10][7] <= 126.0:
													pixels.append((10, 7))
													return 5 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													return 7 # approximately 1 were 7 out of 1 samples at leaf node
											else:
												return 3 # approximately 9 were 3 out of 9 samples at leaf node
									else:
										if features[11][9] <= 17.0:
											pixels.append((11, 9))
											if features[19][10] <= 114.5:
												pixels.append((19, 10))
												return 3 # approximately 3 were 3 out of 3 samples at leaf node
											else:
												return 8 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											if features[21][6] <= 40.0:
												pixels.append((21, 6))
												if features[9][21] <= 143.5:
													pixels.append((9, 21))
													return 5 # approximately 16 were 5 out of 16 samples at leaf node
												else:
													return 8 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												return 3 # approximately 1 were 3 out of 1 samples at leaf node
						else:
							if features[15][13] <= 153.0:
								pixels.append((15, 13))
								if features[10][14] <= 211.5:
									pixels.append((10, 14))
									if features[20][8] <= 39.5:
										pixels.append((20, 8))
										if features[7][14] <= 2.5:
											pixels.append((7, 14))
											if features[12][10] <= 165.5:
												pixels.append((12, 10))
												if features[12][10] <= 76.5:
													pixels.append((12, 10))
													if features[15][14] <= 246.0:
														pixels.append((15, 14))
														return 7 # approximately 4 were 7 out of 4 samples at leaf node
													else:
														if features[9][10] <= 127.5:
															pixels.append((9, 10))
															return 1 # approximately 1 were 1 out of 1 samples at leaf node
														else:
															return 4 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													return 9 # approximately 4 were 9 out of 4 samples at leaf node
											else:
												return 4 # approximately 8 were 4 out of 8 samples at leaf node
										else:
											if features[7][9] <= 150.0:
												pixels.append((7, 9))
												if features[13][17] <= 7.5:
													pixels.append((13, 17))
													if features[12][13] <= 219.0:
														pixels.append((12, 13))
														return 9 # approximately 2 were 9 out of 2 samples at leaf node
													else:
														return 5 # approximately 4 were 5 out of 4 samples at leaf node
												else:
													if features[8][23] <= 97.0:
														pixels.append((8, 23))
														if features[23][7] <= 253.0:
															pixels.append((23, 7))
															if features[11][20] <= 254.5:
																pixels.append((11, 20))
																if features[18][13] <= 254.5:
																	pixels.append((18, 13))
																	if features[24][22] <= 167.5:
																		pixels.append((24, 22))
																		if features[13][13] <= 16.5:
																			pixels.append((13, 13))
																			if features[19][15] <= 206.5:
																				pixels.append((19, 15))
																				return 7 # approximately 2 were 7 out of 2 samples at leaf node
																			else:
																				return 9 # approximately 4 were 9 out of 4 samples at leaf node
																		else:
																			if features[6][10] <= 57.5:
																				pixels.append((6, 10))
																				if features[16][17] <= 254.5:
																					pixels.append((16, 17))
																					if features[17][15] <= 24.5:
																						pixels.append((17, 15))
																						if features[22][11] <= 15.0:
																							pixels.append((22, 11))
																							return 9 # approximately 6 were 9 out of 6 samples at leaf node
																						else:
																							return 5 # approximately 1 were 5 out of 1 samples at leaf node
																					else:
																						if features[21][15] <= 253.5:
																							pixels.append((21, 15))
																							return 9 # approximately 240 were 9 out of 240 samples at leaf node
																						else:
																							if features[7][13] <= 117.0:
																								pixels.append((7, 13))
																								return 4 # approximately 1 were 4 out of 1 samples at leaf node
																							else:
																								return 9 # approximately 12 were 9 out of 12 samples at leaf node
																				else:
																					if features[17][15] <= 147.0:
																						pixels.append((17, 15))
																						return 8 # approximately 1 were 8 out of 1 samples at leaf node
																					else:
																						return 9 # approximately 3 were 9 out of 3 samples at leaf node
																			else:
																				if features[7][9] <= 6.5:
																					pixels.append((7, 9))
																					return 7 # approximately 1 were 7 out of 1 samples at leaf node
																				else:
																					return 9 # approximately 2 were 9 out of 2 samples at leaf node
																	else:
																		return 4 # approximately 1 were 4 out of 1 samples at leaf node
																else:
																	return 4 # approximately 1 were 4 out of 1 samples at leaf node
															else:
																return 4 # approximately 1 were 4 out of 1 samples at leaf node
														else:
															return 5 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														return 4 # approximately 2 were 4 out of 2 samples at leaf node
											else:
												if features[22][15] <= 252.5:
													pixels.append((22, 15))
													if features[7][5] <= 29.0:
														pixels.append((7, 5))
														if features[12][21] <= 110.5:
															pixels.append((12, 21))
															return 8 # approximately 6 were 8 out of 6 samples at leaf node
														else:
															return 4 # approximately 1 were 4 out of 1 samples at leaf node
													else:
														if features[9][16] <= 126.0:
															pixels.append((9, 16))
															return 5 # approximately 1 were 5 out of 1 samples at leaf node
														else:
															return 7 # approximately 1 were 7 out of 1 samples at leaf node
												else:
													return 9 # approximately 4 were 9 out of 4 samples at leaf node
									else:
										if features[18][20] <= 84.0:
											pixels.append((18, 20))
											if features[16][14] <= 234.5:
												pixels.append((16, 14))
												if features[11][18] <= 33.5:
													pixels.append((11, 18))
													return 5 # approximately 4 were 5 out of 4 samples at leaf node
												else:
													return 3 # approximately 5 were 3 out of 5 samples at leaf node
											else:
												return 8 # approximately 4 were 8 out of 4 samples at leaf node
										else:
											return 2 # approximately 4 were 2 out of 4 samples at leaf node
								else:
									if features[15][18] <= 54.0:
										pixels.append((15, 18))
										if features[12][16] <= 243.5:
											pixels.append((12, 16))
											if features[20][13] <= 154.0:
												pixels.append((20, 13))
												if features[17][15] <= 79.0:
													pixels.append((17, 15))
													return 3 # approximately 4 were 3 out of 4 samples at leaf node
												else:
													if features[17][15] <= 194.5:
														pixels.append((17, 15))
														return 4 # approximately 4 were 4 out of 4 samples at leaf node
													else:
														if features[13][17] <= 121.0:
															pixels.append((13, 17))
															return 1 # approximately 3 were 1 out of 3 samples at leaf node
														else:
															if features[19][15] <= 225.5:
																pixels.append((19, 15))
																return 8 # approximately 2 were 8 out of 2 samples at leaf node
															else:
																if features[11][10] <= 247.5:
																	pixels.append((11, 10))
																	return 9 # approximately 1 were 9 out of 1 samples at leaf node
																else:
																	return 7 # approximately 1 were 7 out of 1 samples at leaf node
											else:
												if features[13][13] <= 107.0:
													pixels.append((13, 13))
													return 6 # approximately 1 were 6 out of 1 samples at leaf node
												else:
													return 5 # approximately 6 were 5 out of 6 samples at leaf node
										else:
											if features[14][9] <= 234.0:
												pixels.append((14, 9))
												if features[10][19] <= 240.5:
													pixels.append((10, 19))
													if features[12][12] <= 11.0:
														pixels.append((12, 12))
														return 7 # approximately 1 were 7 out of 1 samples at leaf node
													else:
														return 9 # approximately 16 were 9 out of 16 samples at leaf node
												else:
													if features[26][10] <= 112.5:
														pixels.append((26, 10))
														return 4 # approximately 1 were 4 out of 1 samples at leaf node
													else:
														return 7 # approximately 1 were 7 out of 1 samples at leaf node
											else:
												if features[11][13] <= 228.0:
													pixels.append((11, 13))
													return 5 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													return 1 # approximately 1 were 1 out of 1 samples at leaf node
									else:
										if features[10][16] <= 209.0:
											pixels.append((10, 16))
											if features[24][15] <= 99.0:
												pixels.append((24, 15))
												if features[13][22] <= 1.5:
													pixels.append((13, 22))
													if features[11][15] <= 241.0:
														pixels.append((11, 15))
														if features[20][10] <= 245.5:
															pixels.append((20, 10))
															return 5 # approximately 2 were 5 out of 2 samples at leaf node
														else:
															if features[7][18] <= 65.0:
																pixels.append((7, 18))
																if features[8][11] <= 127.0:
																	pixels.append((8, 11))
																	return 2 # approximately 1 were 2 out of 1 samples at leaf node
																else:
																	return 1 # approximately 1 were 1 out of 1 samples at leaf node
															else:
																return 6 # approximately 1 were 6 out of 1 samples at leaf node
													else:
														if features[10][11] <= 17.0:
															pixels.append((10, 11))
															return 9 # approximately 1 were 9 out of 1 samples at leaf node
														else:
															return 3 # approximately 3 were 3 out of 3 samples at leaf node
												else:
													return 7 # approximately 2 were 7 out of 2 samples at leaf node
											else:
												return 8 # approximately 3 were 8 out of 3 samples at leaf node
										else:
											if features[6][14] <= 184.5:
												pixels.append((6, 14))
												return 7 # approximately 25 were 7 out of 25 samples at leaf node
											else:
												return 9 # approximately 1 were 9 out of 1 samples at leaf node
							else:
								if features[12][11] <= 20.0:
									pixels.append((12, 11))
									if features[8][10] <= 16.5:
										pixels.append((8, 10))
										if features[12][18] <= 187.0:
											pixels.append((12, 18))
											return 1 # approximately 39 were 1 out of 39 samples at leaf node
										else:
											if features[21][13] <= 158.5:
												pixels.append((21, 13))
												if features[9][13] <= 5.0:
													pixels.append((9, 13))
													return 3 # approximately 2 were 3 out of 2 samples at leaf node
												else:
													if features[16][11] <= 13.5:
														pixels.append((16, 11))
														return 9 # approximately 1 were 9 out of 1 samples at leaf node
													else:
														return 7 # approximately 1 were 7 out of 1 samples at leaf node
											else:
												return 8 # approximately 2 were 8 out of 2 samples at leaf node
									else:
										if features[18][13] <= 98.0:
											pixels.append((18, 13))
											if features[12][17] <= 31.5:
												pixels.append((12, 17))
												return 1 # approximately 2 were 1 out of 2 samples at leaf node
											else:
												return 3 # approximately 6 were 3 out of 6 samples at leaf node
										else:
											if features[8][16] <= 186.0:
												pixels.append((8, 16))
												return 2 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												return 7 # approximately 28 were 7 out of 28 samples at leaf node
								else:
									if features[17][13] <= 10.5:
										pixels.append((17, 13))
										if features[12][18] <= 21.0:
											pixels.append((12, 18))
											return 8 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											return 9 # approximately 6 were 9 out of 6 samples at leaf node
									else:
										if features[13][15] <= 252.5:
											pixels.append((13, 15))
											return 8 # approximately 31 were 8 out of 31 samples at leaf node
										else:
											if features[12][11] <= 231.0:
												pixels.append((12, 11))
												return 4 # approximately 3 were 4 out of 3 samples at leaf node
											else:
												if features[23][14] <= 144.5:
													pixels.append((23, 14))
													if features[19][15] <= 132.0:
														pixels.append((19, 15))
														if features[9][15] <= 180.0:
															pixels.append((9, 15))
															return 9 # approximately 1 were 9 out of 1 samples at leaf node
														else:
															return 7 # approximately 1 were 7 out of 1 samples at leaf node
													else:
														return 1 # approximately 2 were 1 out of 2 samples at leaf node
												else:
													return 8 # approximately 3 were 8 out of 3 samples at leaf node
					else:
						if features[11][19] <= 13.5:
							pixels.append((11, 19))
							if features[12][21] <= 45.5:
								pixels.append((12, 21))
								if features[3][24] <= 90.0:
									pixels.append((3, 24))
									if features[10][19] <= 236.0:
										pixels.append((10, 19))
										if features[11][24] <= 61.0:
											pixels.append((11, 24))
											if features[25][8] <= 194.5:
												pixels.append((25, 8))
												return 5 # approximately 222 were 5 out of 222 samples at leaf node
											else:
												if features[9][22] <= 16.5:
													pixels.append((9, 22))
													return 5 # approximately 2 were 5 out of 2 samples at leaf node
												else:
													return 9 # approximately 1 were 9 out of 1 samples at leaf node
										else:
											return 9 # approximately 1 were 9 out of 1 samples at leaf node
									else:
										return 8 # approximately 1 were 8 out of 1 samples at leaf node
								else:
									return 6 # approximately 1 were 6 out of 1 samples at leaf node
							else:
								if features[18][6] <= 127.5:
									pixels.append((18, 6))
									return 8 # approximately 3 were 8 out of 3 samples at leaf node
								else:
									return 0 # approximately 1 were 0 out of 1 samples at leaf node
						else:
							if features[16][13] <= 145.0:
								pixels.append((16, 13))
								if features[10][12] <= 6.0:
									pixels.append((10, 12))
									if features[10][7] <= 41.5:
										pixels.append((10, 7))
										return 3 # approximately 14 were 3 out of 14 samples at leaf node
									else:
										return 5 # approximately 1 were 5 out of 1 samples at leaf node
								else:
									if features[17][7] <= 187.0:
										pixels.append((17, 7))
										if features[13][16] <= 70.0:
											pixels.append((13, 16))
											if features[8][16] <= 2.5:
												pixels.append((8, 16))
												return 4 # approximately 1 were 4 out of 1 samples at leaf node
											else:
												return 7 # approximately 6 were 7 out of 6 samples at leaf node
										else:
											if features[11][15] <= 253.5:
												pixels.append((11, 15))
												if features[10][13] <= 77.0:
													pixels.append((10, 13))
													return 9 # approximately 4 were 9 out of 4 samples at leaf node
												else:
													if features[9][16] <= 43.0:
														pixels.append((9, 16))
														return 4 # approximately 3 were 4 out of 3 samples at leaf node
													else:
														if features[9][17] <= 26.0:
															pixels.append((9, 17))
															return 2 # approximately 1 were 2 out of 1 samples at leaf node
														else:
															return 3 # approximately 3 were 3 out of 3 samples at leaf node
											else:
												return 5 # approximately 5 were 5 out of 5 samples at leaf node
									else:
										return 0 # approximately 10 were 0 out of 10 samples at leaf node
							else:
								if features[25][7] <= 21.5:
									pixels.append((25, 7))
									if features[13][13] <= 22.0:
										pixels.append((13, 13))
										return 7 # approximately 1 were 7 out of 1 samples at leaf node
									else:
										if features[10][13] <= 253.5:
											pixels.append((10, 13))
											return 8 # approximately 31 were 8 out of 31 samples at leaf node
										else:
											return 7 # approximately 1 were 7 out of 1 samples at leaf node
								else:
									if features[13][16] <= 252.0:
										pixels.append((13, 16))
										return 7 # approximately 1 were 7 out of 1 samples at leaf node
									else:
										return 9 # approximately 3 were 9 out of 3 samples at leaf node
			else:
				if features[20][9] <= 0.5:
					pixels.append((20, 9))
					if features[11][9] <= 0.5:
						pixels.append((11, 9))
						if features[13][13] <= 178.5:
							pixels.append((13, 13))
							if features[12][6] <= 1.5:
								pixels.append((12, 6))
								if features[12][11] <= 7.0:
									pixels.append((12, 11))
									if features[19][19] <= 1.0:
										pixels.append((19, 19))
										if features[15][16] <= 205.0:
											pixels.append((15, 16))
											if features[20][16] <= 198.5:
												pixels.append((20, 16))
												if features[23][18] <= 75.5:
													pixels.append((23, 18))
													if features[16][7] <= 99.5:
														pixels.append((16, 7))
														if features[8][11] <= 25.0:
															pixels.append((8, 11))
															if features[10][22] <= 114.5:
																pixels.append((10, 22))
																if features[14][21] <= 12.5:
																	pixels.append((14, 21))
																	if features[5][8] <= 32.0:
																		pixels.append((5, 8))
																		return 6 # approximately 1 were 6 out of 1 samples at leaf node
																	else:
																		if features[12][19] <= 64.0:
																			pixels.append((12, 19))
																			return 2 # approximately 1 were 2 out of 1 samples at leaf node
																		else:
																			return 3 # approximately 1 were 3 out of 1 samples at leaf node
																else:
																	return 4 # approximately 1 were 4 out of 1 samples at leaf node
															else:
																return 8 # approximately 2 were 8 out of 2 samples at leaf node
														else:
															return 7 # approximately 5 were 7 out of 5 samples at leaf node
													else:
														return 2 # approximately 4 were 2 out of 4 samples at leaf node
												else:
													return 9 # approximately 4 were 9 out of 4 samples at leaf node
											else:
												if features[8][14] <= 75.5:
													pixels.append((8, 14))
													return 9 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													return 3 # approximately 13 were 3 out of 13 samples at leaf node
										else:
											if features[17][7] <= 253.5:
												pixels.append((17, 7))
												if features[22][6] <= 40.5:
													pixels.append((22, 6))
													if features[12][8] <= 126.5:
														pixels.append((12, 8))
														if features[16][25] <= 10.0:
															pixels.append((16, 25))
															if features[23][21] <= 27.5:
																pixels.append((23, 21))
																if features[5][13] <= 224.5:
																	pixels.append((5, 13))
																	if features[18][7] <= 234.5:
																		pixels.append((18, 7))
																		if features[15][17] <= 58.5:
																			pixels.append((15, 17))
																			if features[24][15] <= 226.0:
																				pixels.append((24, 15))
																				return 7 # approximately 3 were 7 out of 3 samples at leaf node
																			else:
																				return 3 # approximately 1 were 3 out of 1 samples at leaf node
																		else:
																			return 7 # approximately 138 were 7 out of 138 samples at leaf node
																	else:
																		return 3 # approximately 1 were 3 out of 1 samples at leaf node
																else:
																	if features[19][16] <= 253.5:
																		pixels.append((19, 16))
																		return 3 # approximately 1 were 3 out of 1 samples at leaf node
																	else:
																		return 4 # approximately 1 were 4 out of 1 samples at leaf node
															else:
																if features[10][6] <= 49.0:
																	pixels.append((10, 6))
																	return 2 # approximately 1 were 2 out of 1 samples at leaf node
																else:
																	return 3 # approximately 1 were 3 out of 1 samples at leaf node
														else:
															return 2 # approximately 2 were 2 out of 2 samples at leaf node
													else:
														return 9 # approximately 2 were 9 out of 2 samples at leaf node
												else:
													return 3 # approximately 5 were 3 out of 5 samples at leaf node
											else:
												if features[24][12] <= 127.5:
													pixels.append((24, 12))
													return 2 # approximately 6 were 2 out of 6 samples at leaf node
												else:
													return 7 # approximately 1 were 7 out of 1 samples at leaf node
									else:
										if features[22][17] <= 11.5:
											pixels.append((22, 17))
											if features[17][16] <= 1.0:
												pixels.append((17, 16))
												if features[19][21] <= 54.0:
													pixels.append((19, 21))
													return 3 # approximately 4 were 3 out of 4 samples at leaf node
												else:
													if features[7][17] <= 145.5:
														pixels.append((7, 17))
														if features[14][21] <= 64.0:
															pixels.append((14, 21))
															return 5 # approximately 1 were 5 out of 1 samples at leaf node
														else:
															return 9 # approximately 1 were 9 out of 1 samples at leaf node
													else:
														return 2 # approximately 2 were 2 out of 2 samples at leaf node
											else:
												if features[10][7] <= 169.0:
													pixels.append((10, 7))
													if features[24][22] <= 97.5:
														pixels.append((24, 22))
														return 2 # approximately 22 were 2 out of 22 samples at leaf node
													else:
														return 3 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													return 7 # approximately 2 were 7 out of 2 samples at leaf node
										else:
											if features[18][11] <= 174.5:
												pixels.append((18, 11))
												return 3 # approximately 15 were 3 out of 15 samples at leaf node
											else:
												return 7 # approximately 1 were 7 out of 1 samples at leaf node
								else:
									if features[16][8] <= 50.0:
										pixels.append((16, 8))
										if features[16][19] <= 11.0:
											pixels.append((16, 19))
											if features[14][14] <= 3.0:
												pixels.append((14, 14))
												if features[16][13] <= 2.0:
													pixels.append((16, 13))
													if features[12][18] <= 5.0:
														pixels.append((12, 18))
														if features[16][11] <= 22.5:
															pixels.append((16, 11))
															return 5 # approximately 2 were 5 out of 2 samples at leaf node
														else:
															return 9 # approximately 2 were 9 out of 2 samples at leaf node
													else:
														return 7 # approximately 17 were 7 out of 17 samples at leaf node
												else:
													if features[20][14] <= 79.5:
														pixels.append((20, 14))
														if features[13][17] <= 31.0:
															pixels.append((13, 17))
															return 5 # approximately 1 were 5 out of 1 samples at leaf node
														else:
															return 4 # approximately 7 were 4 out of 7 samples at leaf node
													else:
														if features[13][12] <= 204.0:
															pixels.append((13, 12))
															return 9 # approximately 10 were 9 out of 10 samples at leaf node
														else:
															if features[10][12] <= 152.0:
																pixels.append((10, 12))
																return 4 # approximately 2 were 4 out of 2 samples at leaf node
															else:
																return 0 # approximately 1 were 0 out of 1 samples at leaf node
											else:
												if features[21][6] <= 7.0:
													pixels.append((21, 6))
													if features[9][13] <= 170.5:
														pixels.append((9, 13))
														if features[15][11] <= 225.5:
															pixels.append((15, 11))
															if features[8][10] <= 120.5:
																pixels.append((8, 10))
																if features[11][20] <= 43.5:
																	pixels.append((11, 20))
																	return 9 # approximately 17 were 9 out of 17 samples at leaf node
																else:
																	return 4 # approximately 2 were 4 out of 2 samples at leaf node
															else:
																if features[10][16] <= 11.0:
																	pixels.append((10, 16))
																	return 5 # approximately 1 were 5 out of 1 samples at leaf node
																else:
																	return 7 # approximately 2 were 7 out of 2 samples at leaf node
														else:
															if features[14][16] <= 252.5:
																pixels.append((14, 16))
																if features[17][15] <= 85.0:
																	pixels.append((17, 15))
																	return 4 # approximately 2 were 4 out of 2 samples at leaf node
																else:
																	return 9 # approximately 5 were 9 out of 5 samples at leaf node
															else:
																if features[10][16] <= 2.5:
																	pixels.append((10, 16))
																	return 9 # approximately 1 were 9 out of 1 samples at leaf node
																else:
																	return 4 # approximately 9 were 4 out of 9 samples at leaf node
													else:
														if features[13][17] <= 2.0:
															pixels.append((13, 17))
															return 5 # approximately 2 were 5 out of 2 samples at leaf node
														else:
															if features[13][12] <= 253.5:
																pixels.append((13, 12))
																if features[14][7] <= 5.5:
																	pixels.append((14, 7))
																	if features[26][15] <= 155.5:
																		pixels.append((26, 15))
																		return 9 # approximately 105 were 9 out of 105 samples at leaf node
																	else:
																		if features[15][11] <= 223.5:
																			pixels.append((15, 11))
																			return 9 # approximately 2 were 9 out of 2 samples at leaf node
																		else:
																			return 4 # approximately 1 were 4 out of 1 samples at leaf node
																else:
																	return 4 # approximately 1 were 4 out of 1 samples at leaf node
															else:
																return 8 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													if features[17][13] <= 12.0:
														pixels.append((17, 13))
														if features[9][20] <= 231.0:
															pixels.append((9, 20))
															return 5 # approximately 3 were 5 out of 3 samples at leaf node
														else:
															return 3 # approximately 2 were 3 out of 2 samples at leaf node
													else:
														return 8 # approximately 6 were 8 out of 6 samples at leaf node
										else:
											if features[4][18] <= 51.0:
												pixels.append((4, 18))
												if features[16][14] <= 204.0:
													pixels.append((16, 14))
													if features[7][18] <= 175.0:
														pixels.append((7, 18))
														if features[11][11] <= 226.0:
															pixels.append((11, 11))
															return 3 # approximately 10 were 3 out of 10 samples at leaf node
														else:
															if features[12][10] <= 69.5:
																pixels.append((12, 10))
																return 0 # approximately 1 were 0 out of 1 samples at leaf node
															else:
																return 8 # approximately 1 were 8 out of 1 samples at leaf node
													else:
														return 5 # approximately 4 were 5 out of 4 samples at leaf node
												else:
													return 4 # approximately 5 were 4 out of 5 samples at leaf node
											else:
												return 6 # approximately 7 were 6 out of 7 samples at leaf node
									else:
										if features[16][15] <= 95.5:
											pixels.append((16, 15))
											if features[5][19] <= 85.5:
												pixels.append((5, 19))
												if features[14][11] <= 94.0:
													pixels.append((14, 11))
													return 9 # approximately 5 were 9 out of 5 samples at leaf node
												else:
													if features[21][16] <= 42.5:
														pixels.append((21, 16))
														if features[22][8] <= 63.0:
															pixels.append((22, 8))
															if features[8][8] <= 126.5:
																pixels.append((8, 8))
																if features[10][18] <= 125.5:
																	pixels.append((10, 18))
																	return 6 # approximately 1 were 6 out of 1 samples at leaf node
																else:
																	if features[15][12] <= 122.0:
																		pixels.append((15, 12))
																		return 7 # approximately 1 were 7 out of 1 samples at leaf node
																	else:
																		return 4 # approximately 1 were 4 out of 1 samples at leaf node
															else:
																return 3 # approximately 1 were 3 out of 1 samples at leaf node
														else:
															return 8 # approximately 3 were 8 out of 3 samples at leaf node
													else:
														return 5 # approximately 4 were 5 out of 4 samples at leaf node
											else:
												return 0 # approximately 5 were 0 out of 5 samples at leaf node
										else:
											if features[25][11] <= 55.5:
												pixels.append((25, 11))
												if features[11][11] <= 253.5:
													pixels.append((11, 11))
													if features[22][8] <= 67.0:
														pixels.append((22, 8))
														if features[2][18] <= 7.5:
															pixels.append((2, 18))
															return 4 # approximately 70 were 4 out of 70 samples at leaf node
														else:
															return 6 # approximately 1 were 6 out of 1 samples at leaf node
													else:
														if features[23][7] <= 115.5:
															pixels.append((23, 7))
															return 7 # approximately 1 were 7 out of 1 samples at leaf node
														else:
															return 0 # approximately 1 were 0 out of 1 samples at leaf node
												else:
													if features[14][11] <= 102.0:
														pixels.append((14, 11))
														if features[5][20] <= 33.5:
															pixels.append((5, 20))
															return 9 # approximately 3 were 9 out of 3 samples at leaf node
														else:
															return 5 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														return 4 # approximately 3 were 4 out of 3 samples at leaf node
											else:
												if features[8][20] <= 182.5:
													pixels.append((8, 20))
													if features[20][12] <= 39.5:
														pixels.append((20, 12))
														return 3 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														return 4 # approximately 4 were 4 out of 4 samples at leaf node
												else:
													if features[9][15] <= 222.0:
														pixels.append((9, 15))
														return 9 # approximately 4 were 9 out of 4 samples at leaf node
													else:
														return 7 # approximately 2 were 7 out of 2 samples at leaf node
							else:
								if features[7][12] <= 1.5:
									pixels.append((7, 12))
									if features[11][6] <= 214.5:
										pixels.append((11, 6))
										if features[21][9] <= 27.0:
											pixels.append((21, 9))
											if features[11][20] <= 1.5:
												pixels.append((11, 20))
												return 9 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												if features[16][22] <= 32.0:
													pixels.append((16, 22))
													return 2 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													return 7 # approximately 1 were 7 out of 1 samples at leaf node
										else:
											return 8 # approximately 1 were 8 out of 1 samples at leaf node
									else:
										return 4 # approximately 9 were 4 out of 9 samples at leaf node
								else:
									if features[19][13] <= 252.5:
										pixels.append((19, 13))
										if features[12][13] <= 14.5:
											pixels.append((12, 13))
											if features[15][9] <= 8.0:
												pixels.append((15, 9))
												if features[14][17] <= 175.0:
													pixels.append((14, 17))
													return 7 # approximately 2 were 7 out of 2 samples at leaf node
												else:
													if features[14][13] <= 162.0:
														pixels.append((14, 13))
														return 9 # approximately 2 were 9 out of 2 samples at leaf node
													else:
														if features[16][19] <= 67.0:
															pixels.append((16, 19))
															return 8 # approximately 1 were 8 out of 1 samples at leaf node
														else:
															return 3 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												if features[7][22] <= 120.0:
													pixels.append((7, 22))
													return 9 # approximately 118 were 9 out of 118 samples at leaf node
												else:
													if features[18][16] <= 99.5:
														pixels.append((18, 16))
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														return 4 # approximately 1 were 4 out of 1 samples at leaf node
										else:
											return 3 # approximately 3 were 3 out of 3 samples at leaf node
									else:
										if features[16][13] <= 95.5:
											pixels.append((16, 13))
											return 9 # approximately 1 were 9 out of 1 samples at leaf node
										else:
											return 8 # approximately 5 were 8 out of 5 samples at leaf node
						else:
							if features[6][11] <= 3.0:
								pixels.append((6, 11))
								if features[18][8] <= 219.5:
									pixels.append((18, 8))
									if features[11][17] <= 35.5:
										pixels.append((11, 17))
										if features[19][11] <= 216.5:
											pixels.append((19, 11))
											if features[8][19] <= 1.5:
												pixels.append((8, 19))
												if features[16][10] <= 36.0:
													pixels.append((16, 10))
													if features[7][18] <= 201.0:
														pixels.append((7, 18))
														return 3 # approximately 7 were 3 out of 7 samples at leaf node
													else:
														return 7 # approximately 1 were 7 out of 1 samples at leaf node
												else:
													if features[8][12] <= 95.0:
														pixels.append((8, 12))
														if features[13][8] <= 25.0:
															pixels.append((13, 8))
															return 4 # approximately 1 were 4 out of 1 samples at leaf node
														else:
															return 2 # approximately 1 were 2 out of 1 samples at leaf node
													else:
														return 5 # approximately 2 were 5 out of 2 samples at leaf node
											else:
												if features[12][20] <= 80.5:
													pixels.append((12, 20))
													if features[15][11] <= 4.5:
														pixels.append((15, 11))
														return 9 # approximately 1 were 9 out of 1 samples at leaf node
													else:
														return 5 # approximately 25 were 5 out of 25 samples at leaf node
												else:
													if features[24][11] <= 13.0:
														pixels.append((24, 11))
														return 3 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														return 8 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											return 6 # approximately 11 were 6 out of 11 samples at leaf node
									else:
										if features[11][11] <= 220.5:
											pixels.append((11, 11))
											if features[23][8] <= 35.5:
												pixels.append((23, 8))
												if features[8][11] <= 91.5:
													pixels.append((8, 11))
													if features[15][17] <= 153.0:
														pixels.append((15, 17))
														if features[9][16] <= 218.5:
															pixels.append((9, 16))
															return 9 # approximately 6 were 9 out of 6 samples at leaf node
														else:
															if features[14][19] <= 4.0:
																pixels.append((14, 19))
																return 1 # approximately 7 were 1 out of 7 samples at leaf node
															else:
																if features[22][14] <= 5.5:
																	pixels.append((22, 14))
																	return 7 # approximately 1 were 7 out of 1 samples at leaf node
																else:
																	return 4 # approximately 2 were 4 out of 2 samples at leaf node
													else:
														return 4 # approximately 14 were 4 out of 14 samples at leaf node
												else:
													if features[11][6] <= 54.0:
														pixels.append((11, 6))
														if features[20][17] <= 30.0:
															pixels.append((20, 17))
															if features[17][18] <= 119.0:
																pixels.append((17, 18))
																return 7 # approximately 4 were 7 out of 4 samples at leaf node
															else:
																if features[24][12] <= 60.5:
																	pixels.append((24, 12))
																	return 2 # approximately 3 were 2 out of 3 samples at leaf node
																else:
																	return 3 # approximately 1 were 3 out of 1 samples at leaf node
														else:
															return 3 # approximately 7 were 3 out of 7 samples at leaf node
													else:
														return 9 # approximately 12 were 9 out of 12 samples at leaf node
											else:
												if features[9][19] <= 121.5:
													pixels.append((9, 19))
													if features[14][15] <= 172.0:
														pixels.append((14, 15))
														return 5 # approximately 4 were 5 out of 4 samples at leaf node
													else:
														return 1 # approximately 1 were 1 out of 1 samples at leaf node
												else:
													return 3 # approximately 16 were 3 out of 16 samples at leaf node
										else:
											if features[24][14] <= 253.5:
												pixels.append((24, 14))
												if features[21][10] <= 195.0:
													pixels.append((21, 10))
													return 9 # approximately 30 were 9 out of 30 samples at leaf node
												else:
													return 4 # approximately 1 were 4 out of 1 samples at leaf node
											else:
												return 4 # approximately 2 were 4 out of 2 samples at leaf node
								else:
									if features[7][17] <= 19.5:
										pixels.append((7, 17))
										if features[8][13] <= 120.0:
											pixels.append((8, 13))
											return 5 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											if features[13][16] <= 127.0:
												pixels.append((13, 16))
												return 4 # approximately 1 were 4 out of 1 samples at leaf node
											else:
												return 2 # approximately 1 were 2 out of 1 samples at leaf node
									else:
										if features[16][18] <= 169.0:
											pixels.append((16, 18))
											return 8 # approximately 27 were 8 out of 27 samples at leaf node
										else:
											return 3 # approximately 1 were 3 out of 1 samples at leaf node
							else:
								if features[18][12] <= 150.5:
									pixels.append((18, 12))
									if features[12][7] <= 130.0:
										pixels.append((12, 7))
										if features[10][11] <= 187.0:
											pixels.append((10, 11))
											return 3 # approximately 139 were 3 out of 139 samples at leaf node
										else:
											if features[9][9] <= 98.5:
												pixels.append((9, 9))
												if features[18][14] <= 126.0:
													pixels.append((18, 14))
													return 5 # approximately 3 were 5 out of 3 samples at leaf node
												else:
													if features[5][10] <= 43.0:
														pixels.append((5, 10))
														return 4 # approximately 1 were 4 out of 1 samples at leaf node
													else:
														return 1 # approximately 2 were 1 out of 2 samples at leaf node
											else:
												return 3 # approximately 3 were 3 out of 3 samples at leaf node
									else:
										if features[21][21] <= 209.0:
											pixels.append((21, 21))
											return 9 # approximately 5 were 9 out of 5 samples at leaf node
										else:
											return 5 # approximately 1 were 5 out of 1 samples at leaf node
								else:
									if features[22][18] <= 19.0:
										pixels.append((22, 18))
										return 7 # approximately 5 were 7 out of 5 samples at leaf node
									else:
										if features[8][11] <= 252.5:
											pixels.append((8, 11))
											if features[21][11] <= 31.0:
												pixels.append((21, 11))
												if features[11][15] <= 148.0:
													pixels.append((11, 15))
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													return 1 # approximately 1 were 1 out of 1 samples at leaf node
											else:
												return 2 # approximately 2 were 2 out of 2 samples at leaf node
										else:
											return 8 # approximately 3 were 8 out of 3 samples at leaf node
					else:
						if features[8][13] <= 1.0:
							pixels.append((8, 13))
							if features[6][14] <= 76.5:
								pixels.append((6, 14))
								if features[10][13] <= 131.5:
									pixels.append((10, 13))
									if features[15][16] <= 111.0:
										pixels.append((15, 16))
										return 9 # approximately 2 were 9 out of 2 samples at leaf node
									else:
										if features[5][13] <= 181.5:
											pixels.append((5, 13))
											return 4 # approximately 140 were 4 out of 140 samples at leaf node
										else:
											return 8 # approximately 2 were 8 out of 2 samples at leaf node
								else:
									if features[10][16] <= 183.0:
										pixels.append((10, 16))
										if features[6][19] <= 11.0:
											pixels.append((6, 19))
											if features[15][14] <= 5.5:
												pixels.append((15, 14))
												if features[24][12] <= 83.0:
													pixels.append((24, 12))
													if features[11][18] <= 15.0:
														pixels.append((11, 18))
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														return 8 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													return 7 # approximately 1 were 7 out of 1 samples at leaf node
											else:
												if features[13][23] <= 123.5:
													pixels.append((13, 23))
													return 9 # approximately 6 were 9 out of 6 samples at leaf node
												else:
													return 2 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											if features[8][15] <= 254.5:
												pixels.append((8, 15))
												return 4 # approximately 5 were 4 out of 5 samples at leaf node
											else:
												return 5 # approximately 1 were 5 out of 1 samples at leaf node
									else:
										if features[25][13] <= 237.5:
											pixels.append((25, 13))
											return 7 # approximately 8 were 7 out of 8 samples at leaf node
										else:
											return 9 # approximately 1 were 9 out of 1 samples at leaf node
							else:
								if features[5][12] <= 137.5:
									pixels.append((5, 12))
									if features[9][15] <= 248.5:
										pixels.append((9, 15))
										if features[19][11] <= 114.0:
											pixels.append((19, 11))
											if features[15][12] <= 254.5:
												pixels.append((15, 12))
												return 9 # approximately 39 were 9 out of 39 samples at leaf node
											else:
												return 3 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											return 8 # approximately 1 were 8 out of 1 samples at leaf node
									else:
										if features[10][15] <= 227.0:
											pixels.append((10, 15))
											return 3 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											return 4 # approximately 3 were 4 out of 3 samples at leaf node
								else:
									return 8 # approximately 4 were 8 out of 4 samples at leaf node
						else:
							if features[6][23] <= 8.5:
								pixels.append((6, 23))
								if features[16][21] <= 0.5:
									pixels.append((16, 21))
									if features[19][11] <= 182.0:
										pixels.append((19, 11))
										if features[22][7] <= 16.0:
											pixels.append((22, 7))
											if features[12][17] <= 2.5:
												pixels.append((12, 17))
												if features[12][19] <= 16.5:
													pixels.append((12, 19))
													if features[17][15] <= 31.0:
														pixels.append((17, 15))
														if features[12][15] <= 42.5:
															pixels.append((12, 15))
															if features[23][18] <= 252.0:
																pixels.append((23, 18))
																if features[19][15] <= 31.5:
																	pixels.append((19, 15))
																	return 5 # approximately 32 were 5 out of 32 samples at leaf node
																else:
																	return 9 # approximately 1 were 9 out of 1 samples at leaf node
															else:
																return 9 # approximately 2 were 9 out of 2 samples at leaf node
														else:
															if features[12][15] <= 210.5:
																pixels.append((12, 15))
																return 3 # approximately 3 were 3 out of 3 samples at leaf node
															else:
																if features[24][18] <= 151.5:
																	pixels.append((24, 18))
																	if features[22][14] <= 126.5:
																		pixels.append((22, 14))
																		if features[11][7] <= 233.0:
																			pixels.append((11, 7))
																			return 7 # approximately 1 were 7 out of 1 samples at leaf node
																		else:
																			return 4 # approximately 1 were 4 out of 1 samples at leaf node
																	else:
																		return 8 # approximately 1 were 8 out of 1 samples at leaf node
																else:
																	return 9 # approximately 2 were 9 out of 2 samples at leaf node
													else:
														if features[9][15] <= 243.5:
															pixels.append((9, 15))
															return 9 # approximately 14 were 9 out of 14 samples at leaf node
														else:
															if features[15][14] <= 180.0:
																pixels.append((15, 14))
																if features[11][16] <= 115.5:
																	pixels.append((11, 16))
																	return 5 # approximately 1 were 5 out of 1 samples at leaf node
																else:
																	return 9 # approximately 1 were 9 out of 1 samples at leaf node
															else:
																return 4 # approximately 4 were 4 out of 4 samples at leaf node
												else:
													if features[7][17] <= 22.0:
														pixels.append((7, 17))
														if features[8][16] <= 145.5:
															pixels.append((8, 16))
															if features[13][13] <= 253.5:
																pixels.append((13, 13))
																return 4 # approximately 11 were 4 out of 11 samples at leaf node
															else:
																return 8 # approximately 1 were 8 out of 1 samples at leaf node
														else:
															if features[11][21] <= 71.5:
																pixels.append((11, 21))
																return 9 # approximately 4 were 9 out of 4 samples at leaf node
															else:
																if features[17][7] <= 29.5:
																	pixels.append((17, 7))
																	return 7 # approximately 2 were 7 out of 2 samples at leaf node
																else:
																	return 2 # approximately 1 were 2 out of 1 samples at leaf node
													else:
														if features[15][9] <= 2.5:
															pixels.append((15, 9))
															if features[14][14] <= 173.5:
																pixels.append((14, 14))
																if features[18][16] <= 252.5:
																	pixels.append((18, 16))
																	return 8 # approximately 6 were 8 out of 6 samples at leaf node
																else:
																	if features[19][15] <= 134.5:
																		pixels.append((19, 15))
																		return 2 # approximately 1 were 2 out of 1 samples at leaf node
																	else:
																		if features[11][19] <= 200.5:
																			pixels.append((11, 19))
																			return 7 # approximately 1 were 7 out of 1 samples at leaf node
																		else:
																			return 9 # approximately 1 were 9 out of 1 samples at leaf node
															else:
																return 9 # approximately 6 were 9 out of 6 samples at leaf node
														else:
															if features[5][18] <= 181.5:
																pixels.append((5, 18))
																if features[17][6] <= 252.5:
																	pixels.append((17, 6))
																	if features[11][13] <= 156.5:
																		pixels.append((11, 13))
																		return 9 # approximately 72 were 9 out of 72 samples at leaf node
																	else:
																		if features[15][20] <= 32.0:
																			pixels.append((15, 20))
																			return 7 # approximately 1 were 7 out of 1 samples at leaf node
																		else:
																			return 9 # approximately 1 were 9 out of 1 samples at leaf node
																else:
																	return 4 # approximately 1 were 4 out of 1 samples at leaf node
															else:
																return 4 # approximately 1 were 4 out of 1 samples at leaf node
											else:
												if features[7][7] <= 10.0:
													pixels.append((7, 7))
													if features[15][21] <= 126.5:
														pixels.append((15, 21))
														if features[15][13] <= 0.5:
															pixels.append((15, 13))
															if features[13][14] <= 35.5:
																pixels.append((13, 14))
																if features[16][12] <= 15.5:
																	pixels.append((16, 12))
																	if features[12][10] <= 186.0:
																		pixels.append((12, 10))
																		if features[23][15] <= 210.0:
																			pixels.append((23, 15))
																			return 9 # approximately 3 were 9 out of 3 samples at leaf node
																		else:
																			return 7 # approximately 1 were 7 out of 1 samples at leaf node
																	else:
																		if features[13][13] <= 119.0:
																			pixels.append((13, 13))
																			return 7 # approximately 28 were 7 out of 28 samples at leaf node
																		else:
																			return 9 # approximately 1 were 9 out of 1 samples at leaf node
																else:
																	if features[8][11] <= 3.0:
																		pixels.append((8, 11))
																		return 4 # approximately 4 were 4 out of 4 samples at leaf node
																	else:
																		if features[20][12] <= 150.0:
																			pixels.append((20, 12))
																			if features[15][12] <= 110.5:
																				pixels.append((15, 12))
																				if features[21][17] <= 254.5:
																					pixels.append((21, 17))
																					return 9 # approximately 35 were 9 out of 35 samples at leaf node
																				else:
																					return 4 # approximately 1 were 4 out of 1 samples at leaf node
																			else:
																				return 7 # approximately 1 were 7 out of 1 samples at leaf node
																		else:
																			return 8 # approximately 2 were 8 out of 2 samples at leaf node
															else:
																if features[13][23] <= 114.5:
																	pixels.append((13, 23))
																	if features[20][20] <= 98.5:
																		pixels.append((20, 20))
																		return 9 # approximately 73 were 9 out of 73 samples at leaf node
																	else:
																		return 5 # approximately 1 were 5 out of 1 samples at leaf node
																else:
																	return 4 # approximately 1 were 4 out of 1 samples at leaf node
														else:
															if features[5][12] <= 13.0:
																pixels.append((5, 12))
																if features[18][12] <= 210.0:
																	pixels.append((18, 12))
																	if features[8][16] <= 3.5:
																		pixels.append((8, 16))
																		if features[11][11] <= 244.0:
																			pixels.append((11, 11))
																			if features[25][14] <= 253.5:
																				pixels.append((25, 14))
																				if features[8][23] <= 54.5:
																					pixels.append((8, 23))
																					if features[8][8] <= 237.0:
																						pixels.append((8, 8))
																						return 9 # approximately 55 were 9 out of 55 samples at leaf node
																					else:
																						return 4 # approximately 1 were 4 out of 1 samples at leaf node
																				else:
																					return 4 # approximately 1 were 4 out of 1 samples at leaf node
																			else:
																				if features[21][12] <= 95.5:
																					pixels.append((21, 12))
																					return 4 # approximately 2 were 4 out of 2 samples at leaf node
																				else:
																					return 9 # approximately 1 were 9 out of 1 samples at leaf node
																		else:
																			if features[18][11] <= 6.5:
																				pixels.append((18, 11))
																				if features[7][17] <= 125.0:
																					pixels.append((7, 17))
																					return 4 # approximately 14 were 4 out of 14 samples at leaf node
																				else:
																					return 9 # approximately 1 were 9 out of 1 samples at leaf node
																			else:
																				return 9 # approximately 5 were 9 out of 5 samples at leaf node
																	else:
																		if features[18][24] <= 112.5:
																			pixels.append((18, 24))
																			if features[7][25] <= 13.5:
																				pixels.append((7, 25))
																				if features[16][20] <= 232.0:
																					pixels.append((16, 20))
																					if features[15][21] <= 9.5:
																						pixels.append((15, 21))
																						if features[26][19] <= 253.5:
																							pixels.append((26, 19))
																							if features[5][19] <= 49.5:
																								pixels.append((5, 19))
																								if features[20][7] <= 4.0:
																									pixels.append((20, 7))
																									if features[9][7] <= 202.5:
																										pixels.append((9, 7))
																										if features[7][9] <= 254.5:
																											pixels.append((7, 9))
																											if features[8][12] <= 26.5:
																												pixels.append((8, 12))
																												if features[6][16] <= 155.0:
																													pixels.append((6, 16))
																													if features[14][5] <= 168.0:
																														pixels.append((14, 5))
																														if features[16][6] <= 253.5:
																															pixels.append((16, 6))
																															if features[7][16] <= 254.5:
																																pixels.append((7, 16))
																																return 9 # approximately 85 were 9 out of 85 samples at leaf node
																															else:
																																if features[10][13] <= 159.0:
																																	pixels.append((10, 13))
																																	return 9 # approximately 1 were 9 out of 1 samples at leaf node
																																else:
																																	return 4 # approximately 1 were 4 out of 1 samples at leaf node
																														else:
																															return 4 # approximately 1 were 4 out of 1 samples at leaf node
																													else:
																														return 4 # approximately 2 were 4 out of 2 samples at leaf node
																												else:
																													if features[12][11] <= 241.0:
																														pixels.append((12, 11))
																														return 4 # approximately 4 were 4 out of 4 samples at leaf node
																													else:
																														return 9 # approximately 1 were 9 out of 1 samples at leaf node
																											else:
																												if features[7][23] <= 146.0:
																													pixels.append((7, 23))
																													if features[18][20] <= 116.5:
																														pixels.append((18, 20))
																														if features[7][8] <= 44.0:
																															pixels.append((7, 8))
																															if features[11][23] <= 178.0:
																																pixels.append((11, 23))
																																if features[7][21] <= 254.5:
																																	pixels.append((7, 21))
																																	if features[13][4] <= 196.0:
																																		pixels.append((13, 4))
																																		if features[8][15] <= 4.5:
																																			pixels.append((8, 15))
																																			if features[6][12] <= 175.0:
																																				pixels.append((6, 12))
																																				return 9 # approximately 2 were 9 out of 2 samples at leaf node
																																			else:
																																				return 4 # approximately 1 were 4 out of 1 samples at leaf node
																																		else:
																																			if features[9][6] <= 47.5:
																																				pixels.append((9, 6))
																																				if features[15][13] <= 4.5:
																																					pixels.append((15, 13))
																																					if features[6][20] <= 143.5:
																																						pixels.append((6, 20))
																																						return 9 # approximately 7 were 9 out of 7 samples at leaf node
																																					else:
																																						return 7 # approximately 1 were 7 out of 1 samples at leaf node
																																				else:
																																					if features[17][20] <= 72.5:
																																						pixels.append((17, 20))
																																						if features[8][12] <= 86.5:
																																							pixels.append((8, 12))
																																							if features[21][17] <= 253.5:
																																								pixels.append((21, 17))
																																								if features[26][15] <= 207.0:
																																									pixels.append((26, 15))
																																									if features[8][15] <= 63.5:
																																										pixels.append((8, 15))
																																										if features[14][11] <= 146.0:
																																											pixels.append((14, 11))
																																											return 9 # approximately 1 were 9 out of 1 samples at leaf node
																																										else:
																																											return 4 # approximately 1 were 4 out of 1 samples at leaf node
																																									else:
																																										return 9 # approximately 93 were 9 out of 93 samples at leaf node
																																								else:
																																									return 4 # approximately 1 were 4 out of 1 samples at leaf node
																																							else:
																																								return 4 # approximately 1 were 4 out of 1 samples at leaf node
																																						else:
																																							if features[13][17] <= 46.5:
																																								pixels.append((13, 17))
																																								if features[23][11] <= 95.0:
																																									pixels.append((23, 11))
																																									return 9 # approximately 12 were 9 out of 12 samples at leaf node
																																								else:
																																									return 3 # approximately 1 were 3 out of 1 samples at leaf node
																																							else:
																																								if features[14][17] <= 32.5:
																																									pixels.append((14, 17))
																																									if features[8][8] <= 40.0:
																																										pixels.append((8, 8))
																																										return 9 # approximately 12 were 9 out of 12 samples at leaf node
																																									else:
																																										return 8 # approximately 1 were 8 out of 1 samples at leaf node
																																								else:
																																									if features[15][11] <= 7.0:
																																										pixels.append((15, 11))
																																										if features[8][9] <= 139.5:
																																											pixels.append((8, 9))
																																											return 9 # approximately 15 were 9 out of 15 samples at leaf node
																																										else:
																																											return 3 # approximately 1 were 3 out of 1 samples at leaf node
																																									else:
																																										if features[9][21] <= 253.5:
																																											pixels.append((9, 21))
																																											return 9 # approximately 1481 were 9 out of 1481 samples at leaf node
																																										else:
																																											if features[12][15] <= 233.5:
																																												pixels.append((12, 15))
																																												return 9 # approximately 15 were 9 out of 15 samples at leaf node
																																											else:
																																												return 4 # approximately 1 were 4 out of 1 samples at leaf node
																																					else:
																																						if features[25][15] <= 151.5:
																																							pixels.append((25, 15))
																																							return 9 # approximately 11 were 9 out of 11 samples at leaf node
																																						else:
																																							return 7 # approximately 1 were 7 out of 1 samples at leaf node
																																			else:
																																				if features[18][16] <= 64.0:
																																					pixels.append((18, 16))
																																					return 7 # approximately 1 were 7 out of 1 samples at leaf node
																																				else:
																																					return 9 # approximately 3 were 9 out of 3 samples at leaf node
																																	else:
																																		if features[7][18] <= 65.5:
																																			pixels.append((7, 18))
																																			return 4 # approximately 1 were 4 out of 1 samples at leaf node
																																		else:
																																			return 9 # approximately 2 were 9 out of 2 samples at leaf node
																																else:
																																	if features[7][23] <= 5.0:
																																		pixels.append((7, 23))
																																		return 3 # approximately 1 were 3 out of 1 samples at leaf node
																																	else:
																																		return 9 # approximately 2 were 9 out of 2 samples at leaf node
																															else:
																																if features[16][18] <= 122.0:
																																	pixels.append((16, 18))
																																	return 8 # approximately 1 were 8 out of 1 samples at leaf node
																																else:
																																	return 9 # approximately 2 were 9 out of 2 samples at leaf node
																														else:
																															if features[13][8] <= 20.0:
																																pixels.append((13, 8))
																																if features[11][9] <= 173.0:
																																	pixels.append((11, 9))
																																	if features[23][15] <= 130.0:
																																		pixels.append((23, 15))
																																		return 3 # approximately 1 were 3 out of 1 samples at leaf node
																																	else:
																																		return 7 # approximately 1 were 7 out of 1 samples at leaf node
																																else:
																																	return 8 # approximately 2 were 8 out of 2 samples at leaf node
																															else:
																																return 9 # approximately 21 were 9 out of 21 samples at leaf node
																													else:
																														if features[10][16] <= 16.5:
																															pixels.append((10, 16))
																															if features[18][12] <= 38.0:
																																pixels.append((18, 12))
																																return 5 # approximately 1 were 5 out of 1 samples at leaf node
																															else:
																																return 8 # approximately 1 were 8 out of 1 samples at leaf node
																														else:
																															return 9 # approximately 5 were 9 out of 5 samples at leaf node
																												else:
																													return 4 # approximately 1 were 4 out of 1 samples at leaf node
																										else:
																											return 7 # approximately 1 were 7 out of 1 samples at leaf node
																									else:
																										if features[13][7] <= 35.0:
																											pixels.append((13, 7))
																											if features[13][15] <= 212.5:
																												pixels.append((13, 15))
																												return 8 # approximately 3 were 8 out of 3 samples at leaf node
																											else:
																												if features[11][9] <= 143.0:
																													pixels.append((11, 9))
																													return 7 # approximately 1 were 7 out of 1 samples at leaf node
																												else:
																													return 3 # approximately 2 were 3 out of 2 samples at leaf node
																										else:
																											return 9 # approximately 24 were 9 out of 24 samples at leaf node
																								else:
																									return 4 # approximately 1 were 4 out of 1 samples at leaf node
																							else:
																								if features[17][13] <= 186.0:
																									pixels.append((17, 13))
																									if features[13][15] <= 41.0:
																										pixels.append((13, 15))
																										return 8 # approximately 1 were 8 out of 1 samples at leaf node
																									else:
																										return 9 # approximately 8 were 9 out of 8 samples at leaf node
																								else:
																									return 4 # approximately 3 were 4 out of 3 samples at leaf node
																						else:
																							return 3 # approximately 1 were 3 out of 1 samples at leaf node
																					else:
																						if features[12][19] <= 40.5:
																							pixels.append((12, 19))
																							if features[9][12] <= 106.5:
																								pixels.append((9, 12))
																								return 7 # approximately 2 were 7 out of 2 samples at leaf node
																							else:
																								return 4 # approximately 4 were 4 out of 4 samples at leaf node
																						else:
																							return 9 # approximately 18 were 9 out of 18 samples at leaf node
																				else:
																					if features[7][14] <= 253.0:
																						pixels.append((7, 14))
																						return 4 # approximately 1 were 4 out of 1 samples at leaf node
																					else:
																						return 3 # approximately 1 were 3 out of 1 samples at leaf node
																			else:
																				return 4 # approximately 2 were 4 out of 2 samples at leaf node
																		else:
																			return 2 # approximately 2 were 2 out of 2 samples at leaf node
																else:
																	if features[16][10] <= 19.5:
																		pixels.append((16, 10))
																		if features[19][12] <= 145.5:
																			pixels.append((19, 12))
																			if features[14][14] <= 198.0:
																				pixels.append((14, 14))
																				return 7 # approximately 1 were 7 out of 1 samples at leaf node
																			else:
																				return 3 # approximately 1 were 3 out of 1 samples at leaf node
																		else:
																			if features[22][14] <= 61.5:
																				pixels.append((22, 14))
																				return 9 # approximately 1 were 9 out of 1 samples at leaf node
																			else:
																				return 8 # approximately 10 were 8 out of 10 samples at leaf node
																	else:
																		if features[9][22] <= 82.5:
																			pixels.append((9, 22))
																			if features[12][17] <= 95.5:
																				pixels.append((12, 17))
																				if features[8][21] <= 21.5:
																					pixels.append((8, 21))
																					return 4 # approximately 1 were 4 out of 1 samples at leaf node
																				else:
																					return 8 # approximately 1 were 8 out of 1 samples at leaf node
																			else:
																				if features[26][10] <= 57.5:
																					pixels.append((26, 10))
																					if features[14][18] <= 41.0:
																						pixels.append((14, 18))
																						if features[21][22] <= 38.5:
																							pixels.append((21, 22))
																							return 3 # approximately 1 were 3 out of 1 samples at leaf node
																						else:
																							return 9 # approximately 1 were 9 out of 1 samples at leaf node
																					else:
																						return 9 # approximately 36 were 9 out of 36 samples at leaf node
																				else:
																					return 7 # approximately 1 were 7 out of 1 samples at leaf node
																		else:
																			if features[12][13] <= 193.5:
																				pixels.append((12, 13))
																				return 4 # approximately 2 were 4 out of 2 samples at leaf node
																			else:
																				if features[9][15] <= 220.5:
																					pixels.append((9, 15))
																					return 2 # approximately 1 were 2 out of 1 samples at leaf node
																				else:
																					return 8 # approximately 1 were 8 out of 1 samples at leaf node
															else:
																if features[9][9] <= 100.0:
																	pixels.append((9, 9))
																	return 4 # approximately 6 were 4 out of 6 samples at leaf node
																else:
																	if features[13][9] <= 105.0:
																		pixels.append((13, 9))
																		if features[12][15] <= 220.0:
																			pixels.append((12, 15))
																			return 8 # approximately 3 were 8 out of 3 samples at leaf node
																		else:
																			return 2 # approximately 1 were 2 out of 1 samples at leaf node
																	else:
																		return 9 # approximately 3 were 9 out of 3 samples at leaf node
													else:
														if features[13][7] <= 20.5:
															pixels.append((13, 7))
															return 7 # approximately 5 were 7 out of 5 samples at leaf node
														else:
															return 4 # approximately 4 were 4 out of 4 samples at leaf node
												else:
													if features[19][13] <= 214.5:
														pixels.append((19, 13))
														if features[12][10] <= 72.0:
															pixels.append((12, 10))
															if features[16][16] <= 14.0:
																pixels.append((16, 16))
																return 3 # approximately 1 were 3 out of 1 samples at leaf node
															else:
																return 9 # approximately 13 were 9 out of 13 samples at leaf node
														else:
															if features[14][13] <= 53.0:
																pixels.append((14, 13))
																return 7 # approximately 6 were 7 out of 6 samples at leaf node
															else:
																if features[24][17] <= 239.0:
																	pixels.append((24, 17))
																	return 4 # approximately 5 were 4 out of 5 samples at leaf node
																else:
																	if features[7][18] <= 122.0:
																		pixels.append((7, 18))
																		return 9 # approximately 3 were 9 out of 3 samples at leaf node
																	else:
																		return 8 # approximately 1 were 8 out of 1 samples at leaf node
													else:
														if features[14][18] <= 253.5:
															pixels.append((14, 18))
															return 8 # approximately 13 were 8 out of 13 samples at leaf node
														else:
															return 9 # approximately 1 were 9 out of 1 samples at leaf node
										else:
											if features[18][8] <= 137.0:
												pixels.append((18, 8))
												if features[12][9] <= 51.5:
													pixels.append((12, 9))
													return 3 # approximately 4 were 3 out of 4 samples at leaf node
												else:
													if features[10][14] <= 218.5:
														pixels.append((10, 14))
														return 5 # approximately 11 were 5 out of 11 samples at leaf node
													else:
														if features[15][18] <= 117.0:
															pixels.append((15, 18))
															return 5 # approximately 2 were 5 out of 2 samples at leaf node
														else:
															if features[20][18] <= 41.0:
																pixels.append((20, 18))
																if features[15][10] <= 222.0:
																	pixels.append((15, 10))
																	return 2 # approximately 1 were 2 out of 1 samples at leaf node
																else:
																	return 9 # approximately 1 were 9 out of 1 samples at leaf node
															else:
																return 3 # approximately 2 were 3 out of 2 samples at leaf node
											else:
												return 8 # approximately 7 were 8 out of 7 samples at leaf node
									else:
										if features[23][13] <= 94.0:
											pixels.append((23, 13))
											if features[16][15] <= 246.0:
												pixels.append((16, 15))
												if features[13][8] <= 216.0:
													pixels.append((13, 8))
													if features[20][15] <= 233.5:
														pixels.append((20, 15))
														if features[16][16] <= 122.5:
															pixels.append((16, 16))
															if features[11][19] <= 88.5:
																pixels.append((11, 19))
																if features[17][16] <= 126.5:
																	pixels.append((17, 16))
																	return 6 # approximately 1 were 6 out of 1 samples at leaf node
																else:
																	return 2 # approximately 1 were 2 out of 1 samples at leaf node
															else:
																return 8 # approximately 2 were 8 out of 2 samples at leaf node
														else:
															return 7 # approximately 2 were 7 out of 2 samples at leaf node
													else:
														return 0 # approximately 2 were 0 out of 2 samples at leaf node
												else:
													return 4 # approximately 2 were 4 out of 2 samples at leaf node
											else:
												if features[11][10] <= 210.0:
													pixels.append((11, 10))
													if features[22][22] <= 80.0:
														pixels.append((22, 22))
														return 3 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														return 2 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													return 9 # approximately 11 were 9 out of 11 samples at leaf node
										else:
											if features[8][11] <= 3.5:
												pixels.append((8, 11))
												if features[11][14] <= 51.5:
													pixels.append((11, 14))
													return 6 # approximately 1 were 6 out of 1 samples at leaf node
												else:
													return 4 # approximately 1 were 4 out of 1 samples at leaf node
											else:
												if features[14][21] <= 22.0:
													pixels.append((14, 21))
													return 8 # approximately 38 were 8 out of 38 samples at leaf node
												else:
													return 9 # approximately 1 were 9 out of 1 samples at leaf node
								else:
									if features[10][8] <= 21.5:
										pixels.append((10, 8))
										if features[6][9] <= 95.5:
											pixels.append((6, 9))
											if features[16][17] <= 77.5:
												pixels.append((16, 17))
												if features[7][15] <= 244.0:
													pixels.append((7, 15))
													if features[21][19] <= 75.5:
														pixels.append((21, 19))
														if features[19][12] <= 201.5:
															pixels.append((19, 12))
															return 7 # approximately 1 were 7 out of 1 samples at leaf node
														else:
															return 4 # approximately 1 were 4 out of 1 samples at leaf node
													else:
														return 5 # approximately 3 were 5 out of 3 samples at leaf node
												else:
													return 9 # approximately 4 were 9 out of 4 samples at leaf node
											else:
												if features[6][15] <= 253.5:
													pixels.append((6, 15))
													if features[18][9] <= 229.0:
														pixels.append((18, 9))
														return 4 # approximately 37 were 4 out of 37 samples at leaf node
													else:
														if features[18][22] <= 126.5:
															pixels.append((18, 22))
															return 9 # approximately 1 were 9 out of 1 samples at leaf node
														else:
															return 2 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													return 9 # approximately 2 were 9 out of 2 samples at leaf node
										else:
											return 3 # approximately 8 were 3 out of 8 samples at leaf node
									else:
										if features[13][20] <= 196.0:
											pixels.append((13, 20))
											if features[17][15] <= 42.5:
												pixels.append((17, 15))
												if features[14][9] <= 44.5:
													pixels.append((14, 9))
													if features[20][11] <= 25.0:
														pixels.append((20, 11))
														if features[22][17] <= 42.5:
															pixels.append((22, 17))
															if features[8][10] <= 35.5:
																pixels.append((8, 10))
																return 2 # approximately 1 were 2 out of 1 samples at leaf node
															else:
																return 9 # approximately 1 were 9 out of 1 samples at leaf node
														else:
															return 3 # approximately 6 were 3 out of 6 samples at leaf node
													else:
														return 8 # approximately 4 were 8 out of 4 samples at leaf node
												else:
													if features[9][15] <= 252.5:
														pixels.append((9, 15))
														if features[18][21] <= 26.0:
															pixels.append((18, 21))
															if features[14][22] <= 21.5:
																pixels.append((14, 22))
																return 2 # approximately 1 were 2 out of 1 samples at leaf node
															else:
																return 4 # approximately 1 were 4 out of 1 samples at leaf node
														else:
															return 5 # approximately 20 were 5 out of 20 samples at leaf node
													else:
														if features[18][23] <= 21.0:
															pixels.append((18, 23))
															if features[10][14] <= 208.5:
																pixels.append((10, 14))
																return 9 # approximately 1 were 9 out of 1 samples at leaf node
															else:
																return 0 # approximately 2 were 0 out of 2 samples at leaf node
														else:
															return 8 # approximately 2 were 8 out of 2 samples at leaf node
											else:
												if features[12][8] <= 74.5:
													pixels.append((12, 8))
													if features[6][11] <= 115.0:
														pixels.append((6, 11))
														if features[21][18] <= 136.5:
															pixels.append((21, 18))
															return 7 # approximately 20 were 7 out of 20 samples at leaf node
														else:
															return 3 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														return 2 # approximately 2 were 2 out of 2 samples at leaf node
												else:
													if features[15][22] <= 2.5:
														pixels.append((15, 22))
														if features[18][21] <= 249.5:
															pixels.append((18, 21))
															return 9 # approximately 12 were 9 out of 12 samples at leaf node
														else:
															if features[15][13] <= 211.0:
																pixels.append((15, 13))
																if features[13][11] <= 51.5:
																	pixels.append((13, 11))
																	return 9 # approximately 1 were 9 out of 1 samples at leaf node
																else:
																	return 5 # approximately 1 were 5 out of 1 samples at leaf node
															else:
																return 8 # approximately 4 were 8 out of 4 samples at leaf node
													else:
														if features[15][8] <= 51.5:
															pixels.append((15, 8))
															if features[8][8] <= 24.0:
																pixels.append((8, 8))
																if features[13][7] <= 73.5:
																	pixels.append((13, 7))
																	if features[13][14] <= 127.0:
																		pixels.append((13, 14))
																		return 8 # approximately 1 were 8 out of 1 samples at leaf node
																	else:
																		return 2 # approximately 1 were 2 out of 1 samples at leaf node
																else:
																	return 9 # approximately 1 were 9 out of 1 samples at leaf node
															else:
																return 7 # approximately 6 were 7 out of 6 samples at leaf node
														else:
															if features[13][21] <= 0.5:
																pixels.append((13, 21))
																if features[9][21] <= 52.0:
																	pixels.append((9, 21))
																	return 3 # approximately 1 were 3 out of 1 samples at leaf node
																else:
																	return 5 # approximately 1 were 5 out of 1 samples at leaf node
															else:
																return 4 # approximately 7 were 4 out of 7 samples at leaf node
										else:
											if features[21][12] <= 90.5:
												pixels.append((21, 12))
												if features[15][9] <= 254.5:
													pixels.append((15, 9))
													if features[6][14] <= 254.5:
														pixels.append((6, 14))
														return 9 # approximately 41 were 9 out of 41 samples at leaf node
													else:
														return 7 # approximately 1 were 7 out of 1 samples at leaf node
												else:
													if features[10][21] <= 107.5:
														pixels.append((10, 21))
														if features[25][13] <= 95.5:
															pixels.append((25, 13))
															return 4 # approximately 1 were 4 out of 1 samples at leaf node
														else:
															return 5 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														return 3 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												if features[12][8] <= 195.0:
													pixels.append((12, 8))
													return 7 # approximately 3 were 7 out of 3 samples at leaf node
												else:
													if features[19][22] <= 203.5:
														pixels.append((19, 22))
														if features[10][8] <= 251.5:
															pixels.append((10, 8))
															if features[8][20] <= 126.5:
																pixels.append((8, 20))
																return 0 # approximately 1 were 0 out of 1 samples at leaf node
															else:
																return 4 # approximately 1 were 4 out of 1 samples at leaf node
														else:
															return 8 # approximately 2 were 8 out of 2 samples at leaf node
													else:
														return 3 # approximately 2 were 3 out of 2 samples at leaf node
							else:
								if features[12][19] <= 11.0:
									pixels.append((12, 19))
									if features[22][4] <= 127.0:
										pixels.append((22, 4))
										return 5 # approximately 65 were 5 out of 65 samples at leaf node
									else:
										return 3 # approximately 1 were 3 out of 1 samples at leaf node
								else:
									if features[6][19] <= 15.5:
										pixels.append((6, 19))
										if features[10][11] <= 118.0:
											pixels.append((10, 11))
											return 8 # approximately 4 were 8 out of 4 samples at leaf node
										else:
											if features[25][15] <= 156.5:
												pixels.append((25, 15))
												return 4 # approximately 39 were 4 out of 39 samples at leaf node
											else:
												if features[10][8] <= 144.5:
													pixels.append((10, 8))
													return 9 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													return 7 # approximately 1 were 7 out of 1 samples at leaf node
									else:
										if features[10][12] <= 80.0:
											pixels.append((10, 12))
											return 8 # approximately 10 were 8 out of 10 samples at leaf node
										else:
											if features[12][16] <= 143.5:
												pixels.append((12, 16))
												return 9 # approximately 12 were 9 out of 12 samples at leaf node
											else:
												if features[13][11] <= 196.0:
													pixels.append((13, 11))
													return 8 # approximately 3 were 8 out of 3 samples at leaf node
												else:
													if features[8][6] <= 23.0:
														pixels.append((8, 6))
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														return 3 # approximately 1 were 3 out of 1 samples at leaf node
				else:
					if features[3][20] <= 2.0:
						pixels.append((3, 20))
						if features[17][12] <= 8.5:
							pixels.append((17, 12))
							if features[12][19] <= 2.5:
								pixels.append((12, 19))
								if features[11][16] <= 117.5:
									pixels.append((11, 16))
									if features[17][9] <= 171.5:
										pixels.append((17, 9))
										if features[17][10] <= 253.5:
											pixels.append((17, 10))
											if features[11][17] <= 130.5:
												pixels.append((11, 17))
												if features[5][8] <= 31.5:
													pixels.append((5, 8))
													if features[12][22] <= 119.0:
														pixels.append((12, 22))
														return 5 # approximately 175 were 5 out of 175 samples at leaf node
													else:
														return 2 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													if features[8][11] <= 44.0:
														pixels.append((8, 11))
														return 3 # approximately 2 were 3 out of 2 samples at leaf node
													else:
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												if features[20][12] <= 147.5:
													pixels.append((20, 12))
													return 2 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													return 0 # approximately 1 were 0 out of 1 samples at leaf node
										else:
											return 8 # approximately 2 were 8 out of 2 samples at leaf node
									else:
										if features[4][19] <= 6.5:
											pixels.append((4, 19))
											if features[16][12] <= 106.5:
												pixels.append((16, 12))
												return 5 # approximately 9 were 5 out of 9 samples at leaf node
											else:
												if features[9][9] <= 58.0:
													pixels.append((9, 9))
													return 6 # approximately 1 were 6 out of 1 samples at leaf node
												else:
													return 8 # approximately 2 were 8 out of 2 samples at leaf node
										else:
											return 6 # approximately 12 were 6 out of 12 samples at leaf node
								else:
									if features[19][9] <= 1.5:
										pixels.append((19, 9))
										if features[14][22] <= 132.0:
											pixels.append((14, 22))
											return 3 # approximately 27 were 3 out of 27 samples at leaf node
										else:
											return 9 # approximately 1 were 9 out of 1 samples at leaf node
									else:
										if features[17][9] <= 69.5:
											pixels.append((17, 9))
											if features[11][13] <= 104.5:
												pixels.append((11, 13))
												return 3 # approximately 8 were 3 out of 8 samples at leaf node
											else:
												if features[12][23] <= 109.0:
													pixels.append((12, 23))
													if features[23][20] <= 90.5:
														pixels.append((23, 20))
														return 5 # approximately 14 were 5 out of 14 samples at leaf node
													else:
														return 3 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													return 0 # approximately 1 were 0 out of 1 samples at leaf node
										else:
											if features[17][15] <= 221.0:
												pixels.append((17, 15))
												return 8 # approximately 8 were 8 out of 8 samples at leaf node
											else:
												if features[19][6] <= 5.0:
													pixels.append((19, 6))
													return 2 # approximately 5 were 2 out of 5 samples at leaf node
												else:
													if features[16][8] <= 49.0:
														pixels.append((16, 8))
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														return 6 # approximately 1 were 6 out of 1 samples at leaf node
							else:
								if features[14][15] <= 20.5:
									pixels.append((14, 15))
									if features[22][11] <= 31.0:
										pixels.append((22, 11))
										if features[18][5] <= 127.0:
											pixels.append((18, 5))
											if features[6][18] <= 26.5:
												pixels.append((6, 18))
												return 2 # approximately 3 were 2 out of 3 samples at leaf node
											else:
												if features[10][14] <= 227.5:
													pixels.append((10, 14))
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													return 0 # approximately 1 were 0 out of 1 samples at leaf node
										else:
											return 5 # approximately 3 were 5 out of 3 samples at leaf node
									else:
										if features[16][9] <= 23.0:
											pixels.append((16, 9))
											return 5 # approximately 2 were 5 out of 2 samples at leaf node
										else:
											return 0 # approximately 58 were 0 out of 58 samples at leaf node
								else:
									if features[16][8] <= 34.0:
										pixels.append((16, 8))
										if features[20][16] <= 2.0:
											pixels.append((20, 16))
											if features[19][8] <= 234.5:
												pixels.append((19, 8))
												if features[21][10] <= 163.0:
													pixels.append((21, 10))
													if features[10][14] <= 241.0:
														pixels.append((10, 14))
														return 3 # approximately 4 were 3 out of 4 samples at leaf node
													else:
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													if features[13][14] <= 237.5:
														pixels.append((13, 14))
														return 9 # approximately 4 were 9 out of 4 samples at leaf node
													else:
														return 5 # approximately 2 were 5 out of 2 samples at leaf node
											else:
												return 2 # approximately 3 were 2 out of 3 samples at leaf node
										else:
											if features[14][8] <= 231.0:
												pixels.append((14, 8))
												return 3 # approximately 40 were 3 out of 40 samples at leaf node
											else:
												if features[12][10] <= 126.5:
													pixels.append((12, 10))
													return 9 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													return 5 # approximately 1 were 5 out of 1 samples at leaf node
									else:
										if features[12][10] <= 15.0:
											pixels.append((12, 10))
											if features[16][18] <= 125.5:
												pixels.append((16, 18))
												if features[12][18] <= 197.0:
													pixels.append((12, 18))
													if features[16][10] <= 50.0:
														pixels.append((16, 10))
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														if features[13][21] <= 126.5:
															pixels.append((13, 21))
															return 3 # approximately 1 were 3 out of 1 samples at leaf node
														else:
															return 2 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													return 8 # approximately 2 were 8 out of 2 samples at leaf node
											else:
												return 2 # approximately 11 were 2 out of 11 samples at leaf node
										else:
											if features[9][22] <= 158.0:
												pixels.append((9, 22))
												if features[8][13] <= 162.0:
													pixels.append((8, 13))
													return 6 # approximately 4 were 6 out of 4 samples at leaf node
												else:
													if features[9][11] <= 237.0:
														pixels.append((9, 11))
														if features[6][6] <= 40.0:
															pixels.append((6, 6))
															if features[14][18] <= 151.5:
																pixels.append((14, 18))
																return 5 # approximately 2 were 5 out of 2 samples at leaf node
															else:
																if features[6][16] <= 124.0:
																	pixels.append((6, 16))
																	return 8 # approximately 1 were 8 out of 1 samples at leaf node
																else:
																	return 0 # approximately 2 were 0 out of 2 samples at leaf node
														else:
															return 3 # approximately 3 were 3 out of 3 samples at leaf node
													else:
														return 9 # approximately 3 were 9 out of 3 samples at leaf node
											else:
												if features[13][16] <= 74.5:
													pixels.append((13, 16))
													return 4 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													return 8 # approximately 6 were 8 out of 6 samples at leaf node
						else:
							if features[23][13] <= 2.0:
								pixels.append((23, 13))
								if features[18][21] <= 4.0:
									pixels.append((18, 21))
									if features[11][16] <= 248.0:
										pixels.append((11, 16))
										if features[15][17] <= 48.5:
											pixels.append((15, 17))
											if features[16][19] <= 19.5:
												pixels.append((16, 19))
												if features[11][17] <= 175.0:
													pixels.append((11, 17))
													if features[16][12] <= 152.5:
														pixels.append((16, 12))
														if features[6][20] <= 34.0:
															pixels.append((6, 20))
															return 5 # approximately 1 were 5 out of 1 samples at leaf node
														else:
															return 9 # approximately 2 were 9 out of 2 samples at leaf node
													else:
														return 8 # approximately 39 were 8 out of 39 samples at leaf node
												else:
													if features[18][9] <= 252.5:
														pixels.append((18, 9))
														if features[6][23] <= 54.5:
															pixels.append((6, 23))
															if features[9][21] <= 238.5:
																pixels.append((9, 21))
																return 2 # approximately 3 were 2 out of 3 samples at leaf node
															else:
																if features[19][13] <= 46.0:
																	pixels.append((19, 13))
																	return 7 # approximately 2 were 7 out of 2 samples at leaf node
																else:
																	return 9 # approximately 1 were 9 out of 1 samples at leaf node
														else:
															return 4 # approximately 4 were 4 out of 4 samples at leaf node
													else:
														return 8 # approximately 4 were 8 out of 4 samples at leaf node
											else:
												if features[8][23] <= 124.5:
													pixels.append((8, 23))
													return 6 # approximately 8 were 6 out of 8 samples at leaf node
												else:
													return 8 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											if features[11][11] <= 5.5:
												pixels.append((11, 11))
												if features[17][7] <= 16.0:
													pixels.append((17, 7))
													if features[8][13] <= 169.5:
														pixels.append((8, 13))
														if features[11][21] <= 2.5:
															pixels.append((11, 21))
															if features[10][9] <= 126.0:
																pixels.append((10, 9))
																return 6 # approximately 11 were 6 out of 11 samples at leaf node
															else:
																return 4 # approximately 1 were 4 out of 1 samples at leaf node
														else:
															if features[15][11] <= 250.0:
																pixels.append((15, 11))
																if features[14][20] <= 57.5:
																	pixels.append((14, 20))
																	return 3 # approximately 2 were 3 out of 2 samples at leaf node
																else:
																	if features[15][15] <= 140.5:
																		pixels.append((15, 15))
																		return 0 # approximately 1 were 0 out of 1 samples at leaf node
																	else:
																		if features[18][16] <= 98.0:
																			pixels.append((18, 16))
																			return 9 # approximately 1 were 9 out of 1 samples at leaf node
																		else:
																			return 2 # approximately 1 were 2 out of 1 samples at leaf node
															else:
																return 8 # approximately 2 were 8 out of 2 samples at leaf node
													else:
														if features[19][18] <= 28.0:
															pixels.append((19, 18))
															return 7 # approximately 16 were 7 out of 16 samples at leaf node
														else:
															return 3 # approximately 2 were 3 out of 2 samples at leaf node
												else:
													if features[12][13] <= 244.5:
														pixels.append((12, 13))
														if features[20][14] <= 248.5:
															pixels.append((20, 14))
															if features[24][6] <= 125.5:
																pixels.append((24, 6))
																if features[12][12] <= 112.0:
																	pixels.append((12, 12))
																	return 2 # approximately 34 were 2 out of 34 samples at leaf node
																else:
																	return 3 # approximately 1 were 3 out of 1 samples at leaf node
															else:
																return 7 # approximately 1 were 7 out of 1 samples at leaf node
														else:
															if features[8][22] <= 125.0:
																pixels.append((8, 22))
																return 6 # approximately 1 were 6 out of 1 samples at leaf node
															else:
																return 9 # approximately 1 were 9 out of 1 samples at leaf node
													else:
														if features[11][13] <= 251.0:
															pixels.append((11, 13))
															if features[11][20] <= 10.0:
																pixels.append((11, 20))
																return 5 # approximately 1 were 5 out of 1 samples at leaf node
															else:
																if features[16][7] <= 2.0:
																	pixels.append((16, 7))
																	return 4 # approximately 1 were 4 out of 1 samples at leaf node
																else:
																	return 0 # approximately 1 were 0 out of 1 samples at leaf node
														else:
															return 8 # approximately 4 were 8 out of 4 samples at leaf node
											else:
												if features[8][17] <= 60.0:
													pixels.append((8, 17))
													if features[5][19] <= 1.0:
														pixels.append((5, 19))
														if features[16][13] <= 124.0:
															pixels.append((16, 13))
															return 9 # approximately 1 were 9 out of 1 samples at leaf node
														else:
															return 4 # approximately 33 were 4 out of 33 samples at leaf node
													else:
														if features[5][18] <= 107.5:
															pixels.append((5, 18))
															return 8 # approximately 3 were 8 out of 3 samples at leaf node
														else:
															if features[11][14] <= 9.5:
																pixels.append((11, 14))
																return 9 # approximately 1 were 9 out of 1 samples at leaf node
															else:
																return 6 # approximately 2 were 6 out of 2 samples at leaf node
												else:
													if features[25][7] <= 2.5:
														pixels.append((25, 7))
														if features[12][23] <= 26.0:
															pixels.append((12, 23))
															if features[8][20] <= 26.0:
																pixels.append((8, 20))
																if features[7][15] <= 18.5:
																	pixels.append((7, 15))
																	return 4 # approximately 7 were 4 out of 7 samples at leaf node
																else:
																	if features[13][9] <= 32.0:
																		pixels.append((13, 9))
																		if features[23][16] <= 126.0:
																			pixels.append((23, 16))
																			return 4 # approximately 1 were 4 out of 1 samples at leaf node
																		else:
																			return 3 # approximately 1 were 3 out of 1 samples at leaf node
																	else:
																		return 6 # approximately 5 were 6 out of 5 samples at leaf node
															else:
																if features[12][19] <= 24.0:
																	pixels.append((12, 19))
																	if features[5][22] <= 47.5:
																		pixels.append((5, 22))
																		return 5 # approximately 9 were 5 out of 9 samples at leaf node
																	else:
																		return 6 # approximately 1 were 6 out of 1 samples at leaf node
																else:
																	if features[12][13] <= 238.5:
																		pixels.append((12, 13))
																		if features[14][14] <= 78.0:
																			pixels.append((14, 14))
																			if features[9][11] <= 55.5:
																				pixels.append((9, 11))
																				if features[9][20] <= 110.5:
																					pixels.append((9, 20))
																					return 4 # approximately 1 were 4 out of 1 samples at leaf node
																				else:
																					return 8 # approximately 1 were 8 out of 1 samples at leaf node
																			else:
																				return 2 # approximately 2 were 2 out of 2 samples at leaf node
																		else:
																			return 9 # approximately 3 were 9 out of 3 samples at leaf node
																	else:
																		return 0 # approximately 3 were 0 out of 3 samples at leaf node
														else:
															if features[20][16] <= 15.0:
																pixels.append((20, 16))
																return 8 # approximately 8 were 8 out of 8 samples at leaf node
															else:
																if features[5][22] <= 105.5:
																	pixels.append((5, 22))
																	return 3 # approximately 1 were 3 out of 1 samples at leaf node
																else:
																	return 0 # approximately 1 were 0 out of 1 samples at leaf node
													else:
														if features[7][19] <= 58.0:
															pixels.append((7, 19))
															return 7 # approximately 3 were 7 out of 3 samples at leaf node
														else:
															if features[21][10] <= 157.0:
																pixels.append((21, 10))
																return 8 # approximately 2 were 8 out of 2 samples at leaf node
															else:
																if features[24][9] <= 253.5:
																	pixels.append((24, 9))
																	return 9 # approximately 22 were 9 out of 22 samples at leaf node
																else:
																	return 7 # approximately 1 were 7 out of 1 samples at leaf node
									else:
										if features[5][19] <= 74.5:
											pixels.append((5, 19))
											if features[25][9] <= 19.0:
												pixels.append((25, 9))
												if features[9][19] <= 44.5:
													pixels.append((9, 19))
													return 2 # approximately 5 were 2 out of 5 samples at leaf node
												else:
													if features[16][9] <= 226.0:
														pixels.append((16, 9))
														if features[8][23] <= 39.5:
															pixels.append((8, 23))
															if features[9][11] <= 104.0:
																pixels.append((9, 11))
																if features[11][14] <= 203.5:
																	pixels.append((11, 14))
																	if features[6][18] <= 116.0:
																		pixels.append((6, 18))
																		return 9 # approximately 1 were 9 out of 1 samples at leaf node
																	else:
																		return 1 # approximately 1 were 1 out of 1 samples at leaf node
																else:
																	return 4 # approximately 2 were 4 out of 2 samples at leaf node
															else:
																return 8 # approximately 2 were 8 out of 2 samples at leaf node
														else:
															return 5 # approximately 3 were 5 out of 3 samples at leaf node
													else:
														return 0 # approximately 4 were 0 out of 4 samples at leaf node
											else:
												if features[21][12] <= 18.5:
													pixels.append((21, 12))
													return 1 # approximately 1 were 1 out of 1 samples at leaf node
												else:
													return 7 # approximately 7 were 7 out of 7 samples at leaf node
										else:
											if features[8][23] <= 32.5:
												pixels.append((8, 23))
												return 1 # approximately 57 were 1 out of 57 samples at leaf node
											else:
												return 0 # approximately 1 were 0 out of 1 samples at leaf node
								else:
									if features[13][9] <= 195.5:
										pixels.append((13, 9))
										if features[9][4] <= 253.5:
											pixels.append((9, 4))
											if features[14][4] <= 6.5:
												pixels.append((14, 4))
												if features[22][17] <= 108.5:
													pixels.append((22, 17))
													if features[23][10] <= 145.5:
														pixels.append((23, 10))
														return 2 # approximately 76 were 2 out of 76 samples at leaf node
													else:
														return 7 # approximately 1 were 7 out of 1 samples at leaf node
												else:
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												if features[16][19] <= 55.5:
													pixels.append((16, 19))
													return 5 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													return 9 # approximately 1 were 9 out of 1 samples at leaf node
										else:
											return 3 # approximately 2 were 3 out of 2 samples at leaf node
									else:
										if features[19][20] <= 252.0:
											pixels.append((19, 20))
											if features[10][11] <= 251.5:
												pixels.append((10, 11))
												if features[13][22] <= 22.5:
													pixels.append((13, 22))
													if features[15][15] <= 243.0:
														pixels.append((15, 15))
														return 4 # approximately 1 were 4 out of 1 samples at leaf node
													else:
														return 2 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													return 6 # approximately 2 were 6 out of 2 samples at leaf node
											else:
												return 0 # approximately 2 were 0 out of 2 samples at leaf node
										else:
											return 8 # approximately 2 were 8 out of 2 samples at leaf node
							else:
								if features[8][13] <= 6.0:
									pixels.append((8, 13))
									if features[18][12] <= 243.5:
										pixels.append((18, 12))
										if features[18][16] <= 126.5:
											pixels.append((18, 16))
											return 8 # approximately 5 were 8 out of 5 samples at leaf node
										else:
											if features[19][17] <= 215.0:
												pixels.append((19, 17))
												if features[20][10] <= 157.0:
													pixels.append((20, 10))
													if features[18][10] <= 73.0:
														pixels.append((18, 10))
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														return 2 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													return 0 # approximately 2 were 0 out of 2 samples at leaf node
											else:
												return 6 # approximately 3 were 6 out of 3 samples at leaf node
									else:
										return 1 # approximately 16 were 1 out of 16 samples at leaf node
								else:
									if features[16][19] <= 81.0:
										pixels.append((16, 19))
										if features[7][5] <= 129.0:
											pixels.append((7, 5))
											if features[11][14] <= 253.5:
												pixels.append((11, 14))
												if features[10][4] <= 234.5:
													pixels.append((10, 4))
													if features[15][6] <= 140.5:
														pixels.append((15, 6))
														if features[21][20] <= 232.0:
															pixels.append((21, 20))
															if features[4][19] <= 219.0:
																pixels.append((4, 19))
																if features[21][14] <= 254.5:
																	pixels.append((21, 14))
																	return 8 # approximately 230 were 8 out of 230 samples at leaf node
																else:
																	if features[18][18] <= 104.0:
																		pixels.append((18, 18))
																		return 8 # approximately 3 were 8 out of 3 samples at leaf node
																	else:
																		return 5 # approximately 1 were 5 out of 1 samples at leaf node
															else:
																return 0 # approximately 1 were 0 out of 1 samples at leaf node
														else:
															return 2 # approximately 1 were 2 out of 1 samples at leaf node
													else:
														return 4 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												if features[12][22] <= 1.5:
													pixels.append((12, 22))
													if features[16][13] <= 126.5:
														pixels.append((16, 13))
														return 0 # approximately 1 were 0 out of 1 samples at leaf node
													else:
														if features[22][14] <= 253.5:
															pixels.append((22, 14))
															return 7 # approximately 1 were 7 out of 1 samples at leaf node
														else:
															return 5 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													return 8 # approximately 2 were 8 out of 2 samples at leaf node
										else:
											return 2 # approximately 5 were 2 out of 5 samples at leaf node
									else:
										if features[19][10] <= 68.5:
											pixels.append((19, 10))
											if features[13][10] <= 36.5:
												pixels.append((13, 10))
												return 3 # approximately 4 were 3 out of 4 samples at leaf node
											else:
												if features[8][11] <= 156.0:
													pixels.append((8, 11))
													if features[8][11] <= 67.0:
														pixels.append((8, 11))
														if features[17][7] <= 254.0:
															pixels.append((17, 7))
															return 6 # approximately 1 were 6 out of 1 samples at leaf node
														else:
															return 8 # approximately 1 were 8 out of 1 samples at leaf node
													else:
														return 9 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													return 5 # approximately 6 were 5 out of 6 samples at leaf node
										else:
											if features[10][9] <= 9.0:
												pixels.append((10, 9))
												if features[6][13] <= 6.5:
													pixels.append((6, 13))
													return 6 # approximately 3 were 6 out of 3 samples at leaf node
												else:
													if features[15][14] <= 155.5:
														pixels.append((15, 14))
														return 0 # approximately 3 were 0 out of 3 samples at leaf node
													else:
														if features[9][14] <= 245.5:
															pixels.append((9, 14))
															return 2 # approximately 2 were 2 out of 2 samples at leaf node
														else:
															if features[16][10] <= 126.0:
																pixels.append((16, 10))
																return 3 # approximately 1 were 3 out of 1 samples at leaf node
															else:
																return 8 # approximately 2 were 8 out of 2 samples at leaf node
											else:
												if features[19][14] <= 253.0:
													pixels.append((19, 14))
													if features[5][18] <= 252.5:
														pixels.append((5, 18))
														return 8 # approximately 21 were 8 out of 21 samples at leaf node
													else:
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													return 4 # approximately 1 were 4 out of 1 samples at leaf node
					else:
						if features[9][20] <= 48.0:
							pixels.append((9, 20))
							if features[10][18] <= 164.0:
								pixels.append((10, 18))
								if features[5][25] <= 39.0:
									pixels.append((5, 25))
									if features[8][11] <= 22.5:
										pixels.append((8, 11))
										if features[22][15] <= 242.0:
											pixels.append((22, 15))
											if features[19][9] <= 2.0:
												pixels.append((19, 9))
												if features[15][8] <= 53.5:
													pixels.append((15, 8))
													return 5 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													return 6 # approximately 3 were 6 out of 3 samples at leaf node
											else:
												return 6 # approximately 202 were 6 out of 202 samples at leaf node
										else:
											if features[9][13] <= 78.5:
												pixels.append((9, 13))
												return 5 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												return 6 # approximately 3 were 6 out of 3 samples at leaf node
									else:
										if features[13][20] <= 119.0:
											pixels.append((13, 20))
											return 5 # approximately 2 were 5 out of 2 samples at leaf node
										else:
											return 6 # approximately 2 were 6 out of 2 samples at leaf node
								else:
									return 5 # approximately 1 were 5 out of 1 samples at leaf node
							else:
								if features[14][15] <= 126.5:
									pixels.append((14, 15))
									return 0 # approximately 1 were 0 out of 1 samples at leaf node
								else:
									return 1 # approximately 1 were 1 out of 1 samples at leaf node
						else:
							if features[15][12] <= 10.0:
								pixels.append((15, 12))
								return 0 # approximately 5 were 0 out of 5 samples at leaf node
							else:
								if features[11][15] <= 25.5:
									pixels.append((11, 15))
									return 2 # approximately 3 were 2 out of 3 samples at leaf node
								else:
									if features[16][10] <= 127.0:
										pixels.append((16, 10))
										return 3 # approximately 1 were 3 out of 1 samples at leaf node
									else:
										return 4 # approximately 1 were 4 out of 1 samples at leaf node
	else:
		if features[23][13] <= 0.5:
			pixels.append((23, 13))
			if features[9][18] <= 0.5:
				pixels.append((9, 18))
				if features[8][21] <= 10.5:
					pixels.append((8, 21))
					if features[10][16] <= 93.5:
						pixels.append((10, 16))
						if features[19][11] <= 7.5:
							pixels.append((19, 11))
							if features[19][9] <= 23.5:
								pixels.append((19, 9))
								if features[5][19] <= 6.0:
									pixels.append((5, 19))
									if features[11][13] <= 201.5:
										pixels.append((11, 13))
										if features[7][11] <= 33.5:
											pixels.append((7, 11))
											if features[19][20] <= 3.0:
												pixels.append((19, 20))
												if features[6][18] <= 3.0:
													pixels.append((6, 18))
													if features[6][12] <= 124.5:
														pixels.append((6, 12))
														return 4 # approximately 20 were 4 out of 20 samples at leaf node
													else:
														return 6 # approximately 1 were 6 out of 1 samples at leaf node
												else:
													return 9 # approximately 2 were 9 out of 2 samples at leaf node
											else:
												if features[12][15] <= 56.5:
													pixels.append((12, 15))
													if features[7][7] <= 2.0:
														pixels.append((7, 7))
														return 6 # approximately 3 were 6 out of 3 samples at leaf node
													else:
														if features[18][17] <= 126.5:
															pixels.append((18, 17))
															return 5 # approximately 1 were 5 out of 1 samples at leaf node
														else:
															return 2 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													return 3 # approximately 3 were 3 out of 3 samples at leaf node
										else:
											if features[12][18] <= 31.5:
												pixels.append((12, 18))
												if features[18][13] <= 90.0:
													pixels.append((18, 13))
													if features[16][17] <= 254.5:
														pixels.append((16, 17))
														return 5 # approximately 17 were 5 out of 17 samples at leaf node
													else:
														return 9 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													return 8 # approximately 2 were 8 out of 2 samples at leaf node
											else:
												if features[18][13] <= 212.5:
													pixels.append((18, 13))
													if features[12][10] <= 252.5:
														pixels.append((12, 10))
														return 9 # approximately 11 were 9 out of 11 samples at leaf node
													else:
														return 4 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													if features[23][16] <= 126.0:
														pixels.append((23, 16))
														return 6 # approximately 1 were 6 out of 1 samples at leaf node
													else:
														return 8 # approximately 2 were 8 out of 2 samples at leaf node
									else:
										if features[15][15] <= 171.0:
											pixels.append((15, 15))
											return 3 # approximately 19 were 3 out of 19 samples at leaf node
										else:
											if features[9][17] <= 6.5:
												pixels.append((9, 17))
												if features[14][9] <= 126.5:
													pixels.append((14, 9))
													return 5 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													return 1 # approximately 1 were 1 out of 1 samples at leaf node
											else:
												return 8 # approximately 1 were 8 out of 1 samples at leaf node
								else:
									if features[10][20] <= 10.5:
										pixels.append((10, 20))
										if features[9][16] <= 101.0:
											pixels.append((9, 16))
											if features[17][22] <= 253.0:
												pixels.append((17, 22))
												return 5 # approximately 43 were 5 out of 43 samples at leaf node
											else:
												return 6 # approximately 1 were 6 out of 1 samples at leaf node
										else:
											return 3 # approximately 1 were 3 out of 1 samples at leaf node
									else:
										if features[16][9] <= 253.5:
											pixels.append((16, 9))
											return 8 # approximately 3 were 8 out of 3 samples at leaf node
										else:
											return 2 # approximately 1 were 2 out of 1 samples at leaf node
							else:
								if features[15][9] <= 15.0:
									pixels.append((15, 9))
									if features[8][15] <= 230.5:
										pixels.append((8, 15))
										if features[22][7] <= 190.0:
											pixels.append((22, 7))
											if features[22][13] <= 117.5:
												pixels.append((22, 13))
												if features[17][14] <= 51.0:
													pixels.append((17, 14))
													return 6 # approximately 6 were 6 out of 6 samples at leaf node
												else:
													return 2 # approximately 3 were 2 out of 3 samples at leaf node
											else:
												if features[15][15] <= 68.5:
													pixels.append((15, 15))
													return 5 # approximately 6 were 5 out of 6 samples at leaf node
												else:
													return 6 # approximately 1 were 6 out of 1 samples at leaf node
										else:
											return 8 # approximately 4 were 8 out of 4 samples at leaf node
									else:
										return 3 # approximately 8 were 3 out of 8 samples at leaf node
								else:
									if features[21][14] <= 24.5:
										pixels.append((21, 14))
										if features[16][18] <= 253.5:
											pixels.append((16, 18))
											return 4 # approximately 3 were 4 out of 3 samples at leaf node
										else:
											return 2 # approximately 1 were 2 out of 1 samples at leaf node
									else:
										if features[10][7] <= 110.5:
											pixels.append((10, 7))
											if features[8][20] <= 78.5:
												pixels.append((8, 20))
												return 6 # approximately 79 were 6 out of 79 samples at leaf node
											else:
												return 8 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											if features[14][17] <= 155.5:
												pixels.append((14, 17))
												return 8 # approximately 2 were 8 out of 2 samples at leaf node
											else:
												return 5 # approximately 1 were 5 out of 1 samples at leaf node
						else:
							if features[6][22] <= 95.5:
								pixels.append((6, 22))
								if features[8][19] <= 38.5:
									pixels.append((8, 19))
									if features[23][17] <= 3.0:
										pixels.append((23, 17))
										if features[11][15] <= 206.5:
											pixels.append((11, 15))
											if features[23][9] <= 120.5:
												pixels.append((23, 9))
												if features[3][10] <= 33.0:
													pixels.append((3, 10))
													if features[22][23] <= 125.0:
														pixels.append((22, 23))
														if features[20][3] <= 11.5:
															pixels.append((20, 3))
															if features[4][23] <= 249.0:
																pixels.append((4, 23))
																if features[24][10] <= 3.0:
																	pixels.append((24, 10))
																	if features[8][7] <= 253.5:
																		pixels.append((8, 7))
																		if features[5][9] <= 243.0:
																			pixels.append((5, 9))
																			if features[5][8] <= 210.0:
																				pixels.append((5, 8))
																				if features[9][26] <= 45.5:
																					pixels.append((9, 26))
																					if features[13][4] <= 25.5:
																						pixels.append((13, 4))
																						if features[12][14] <= 225.5:
																							pixels.append((12, 14))
																							if features[19][11] <= 110.5:
																								pixels.append((19, 11))
																								if features[22][18] <= 219.0:
																									pixels.append((22, 18))
																									if features[3][16] <= 254.5:
																										pixels.append((3, 16))
																										if features[5][23] <= 129.5:
																											pixels.append((5, 23))
																											if features[18][18] <= 254.5:
																												pixels.append((18, 18))
																												if features[22][18] <= 6.5:
																													pixels.append((22, 18))
																													if features[20][10] <= 254.5:
																														pixels.append((20, 10))
																														return 6 # approximately 129 were 6 out of 129 samples at leaf node
																													else:
																														if features[18][9] <= 127.5:
																															pixels.append((18, 9))
																															return 5 # approximately 1 were 5 out of 1 samples at leaf node
																														else:
																															return 6 # approximately 2 were 6 out of 2 samples at leaf node
																												else:
																													if features[13][13] <= 204.5:
																														pixels.append((13, 13))
																														return 6 # approximately 18 were 6 out of 18 samples at leaf node
																													else:
																														if features[8][9] <= 86.5:
																															pixels.append((8, 9))
																															return 5 # approximately 3 were 5 out of 3 samples at leaf node
																														else:
																															return 6 # approximately 1 were 6 out of 1 samples at leaf node
																											else:
																												return 5 # approximately 1 were 5 out of 1 samples at leaf node
																										else:
																											return 5 # approximately 1 were 5 out of 1 samples at leaf node
																									else:
																										return 4 # approximately 1 were 4 out of 1 samples at leaf node
																								else:
																									if features[19][19] <= 100.5:
																										pixels.append((19, 19))
																										return 8 # approximately 1 were 8 out of 1 samples at leaf node
																									else:
																										return 5 # approximately 1 were 5 out of 1 samples at leaf node
																							else:
																								if features[9][19] <= 41.5:
																									pixels.append((9, 19))
																									if features[21][15] <= 254.5:
																										pixels.append((21, 15))
																										return 6 # approximately 1662 were 6 out of 1662 samples at leaf node
																									else:
																										if features[7][9] <= 9.0:
																											pixels.append((7, 9))
																											return 6 # approximately 74 were 6 out of 74 samples at leaf node
																										else:
																											if features[13][15] <= 93.0:
																												pixels.append((13, 15))
																												return 6 # approximately 4 were 6 out of 4 samples at leaf node
																											else:
																												return 5 # approximately 1 were 5 out of 1 samples at leaf node
																								else:
																									if features[11][12] <= 64.0:
																										pixels.append((11, 12))
																										return 4 # approximately 1 were 4 out of 1 samples at leaf node
																									else:
																										return 6 # approximately 2 were 6 out of 2 samples at leaf node
																						else:
																							if features[17][10] <= 25.5:
																								pixels.append((17, 10))
																								if features[7][12] <= 68.0:
																									pixels.append((7, 12))
																									return 6 # approximately 1 were 6 out of 1 samples at leaf node
																								else:
																									return 5 # approximately 7 were 5 out of 7 samples at leaf node
																							else:
																								if features[13][12] <= 47.5:
																									pixels.append((13, 12))
																									if features[11][11] <= 249.0:
																										pixels.append((11, 11))
																										if features[17][9] <= 86.5:
																											pixels.append((17, 9))
																											return 4 # approximately 1 were 4 out of 1 samples at leaf node
																										else:
																											if features[4][14] <= 53.5:
																												pixels.append((4, 14))
																												return 5 # approximately 1 were 5 out of 1 samples at leaf node
																											else:
																												if features[16][11] <= 126.5:
																													pixels.append((16, 11))
																													return 3 # approximately 1 were 3 out of 1 samples at leaf node
																												else:
																													return 8 # approximately 1 were 8 out of 1 samples at leaf node
																									else:
																										return 6 # approximately 2 were 6 out of 2 samples at leaf node
																								else:
																									return 6 # approximately 90 were 6 out of 90 samples at leaf node
																					else:
																						return 5 # approximately 1 were 5 out of 1 samples at leaf node
																				else:
																					return 8 # approximately 1 were 8 out of 1 samples at leaf node
																			else:
																				return 3 # approximately 1 were 3 out of 1 samples at leaf node
																		else:
																			if features[12][5] <= 130.0:
																				pixels.append((12, 5))
																				return 5 # approximately 2 were 5 out of 2 samples at leaf node
																			else:
																				return 6 # approximately 1 were 6 out of 1 samples at leaf node
																	else:
																		if features[22][12] <= 68.5:
																			pixels.append((22, 12))
																			return 5 # approximately 1 were 5 out of 1 samples at leaf node
																		else:
																			return 8 # approximately 1 were 8 out of 1 samples at leaf node
																else:
																	if features[11][13] <= 129.0:
																		pixels.append((11, 13))
																		return 4 # approximately 1 were 4 out of 1 samples at leaf node
																	else:
																		return 1 # approximately 1 were 1 out of 1 samples at leaf node
															else:
																return 5 # approximately 2 were 5 out of 2 samples at leaf node
														else:
															return 5 # approximately 2 were 5 out of 2 samples at leaf node
													else:
														return 9 # approximately 2 were 9 out of 2 samples at leaf node
												else:
													if features[17][10] <= 30.0:
														pixels.append((17, 10))
														if features[11][9] <= 212.5:
															pixels.append((11, 9))
															return 3 # approximately 6 were 3 out of 6 samples at leaf node
														else:
															return 5 # approximately 2 were 5 out of 2 samples at leaf node
													else:
														if features[4][15] <= 199.5:
															pixels.append((4, 15))
															return 6 # approximately 10 were 6 out of 10 samples at leaf node
														else:
															return 8 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												if features[15][17] <= 220.5:
													pixels.append((15, 17))
													return 8 # approximately 5 were 8 out of 5 samples at leaf node
												else:
													if features[8][13] <= 252.5:
														pixels.append((8, 13))
														return 4 # approximately 3 were 4 out of 3 samples at leaf node
													else:
														if features[13][20] <= 88.5:
															pixels.append((13, 20))
															return 5 # approximately 1 were 5 out of 1 samples at leaf node
														else:
															return 6 # approximately 1 were 6 out of 1 samples at leaf node
										else:
											if features[15][10] <= 121.0:
												pixels.append((15, 10))
												if features[7][12] <= 9.0:
													pixels.append((7, 12))
													if features[2][12] <= 57.0:
														pixels.append((2, 12))
														return 3 # approximately 5 were 3 out of 5 samples at leaf node
													else:
														return 2 # approximately 2 were 2 out of 2 samples at leaf node
												else:
													if features[22][10] <= 254.5:
														pixels.append((22, 10))
														return 5 # approximately 13 were 5 out of 13 samples at leaf node
													else:
														return 8 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												return 6 # approximately 21 were 6 out of 21 samples at leaf node
									else:
										if features[16][11] <= 67.5:
											pixels.append((16, 11))
											if features[17][19] <= 104.0:
												pixels.append((17, 19))
												if features[20][12] <= 127.0:
													pixels.append((20, 12))
													return 9 # approximately 2 were 9 out of 2 samples at leaf node
												else:
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												return 5 # approximately 6 were 5 out of 6 samples at leaf node
										else:
											if features[16][10] <= 175.5:
												pixels.append((16, 10))
												return 8 # approximately 5 were 8 out of 5 samples at leaf node
											else:
												if features[20][20] <= 52.0:
													pixels.append((20, 20))
													if features[10][12] <= 253.5:
														pixels.append((10, 12))
														return 0 # approximately 1 were 0 out of 1 samples at leaf node
													else:
														return 4 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													return 6 # approximately 3 were 6 out of 3 samples at leaf node
								else:
									if features[21][13] <= 24.5:
										pixels.append((21, 13))
										if features[18][14] <= 58.5:
											pixels.append((18, 14))
											if features[8][11] <= 85.5:
												pixels.append((8, 11))
												return 8 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												return 9 # approximately 2 were 9 out of 2 samples at leaf node
										else:
											return 2 # approximately 10 were 2 out of 10 samples at leaf node
									else:
										if features[21][11] <= 215.5:
											pixels.append((21, 11))
											return 8 # approximately 5 were 8 out of 5 samples at leaf node
										else:
											if features[14][20] <= 116.5:
												pixels.append((14, 20))
												return 5 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												return 6 # approximately 3 were 6 out of 3 samples at leaf node
							else:
								if features[12][20] <= 32.0:
									pixels.append((12, 20))
									return 5 # approximately 16 were 5 out of 16 samples at leaf node
								else:
									if features[17][12] <= 254.0:
										pixels.append((17, 12))
										return 8 # approximately 5 were 8 out of 5 samples at leaf node
									else:
										return 6 # approximately 1 were 6 out of 1 samples at leaf node
					else:
						if features[20][12] <= 1.5:
							pixels.append((20, 12))
							if features[5][12] <= 2.5:
								pixels.append((5, 12))
								if features[19][11] <= 82.0:
									pixels.append((19, 11))
									if features[15][10] <= 26.0:
										pixels.append((15, 10))
										if features[7][17] <= 53.5:
											pixels.append((7, 17))
											if features[15][14] <= 195.0:
												pixels.append((15, 14))
												return 4 # approximately 7 were 4 out of 7 samples at leaf node
											else:
												if features[17][14] <= 100.5:
													pixels.append((17, 14))
													return 9 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													return 1 # approximately 1 were 1 out of 1 samples at leaf node
										else:
											if features[24][15] <= 2.5:
												pixels.append((24, 15))
												if features[10][8] <= 127.0:
													pixels.append((10, 8))
													if features[12][8] <= 15.0:
														pixels.append((12, 8))
														return 3 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														return 2 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													return 8 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												return 7 # approximately 1 were 7 out of 1 samples at leaf node
									else:
										return 4 # approximately 104 were 4 out of 104 samples at leaf node
								else:
									if features[19][9] <= 65.5:
										pixels.append((19, 9))
										return 9 # approximately 3 were 9 out of 3 samples at leaf node
									else:
										if features[8][9] <= 127.0:
											pixels.append((8, 9))
											if features[13][14] <= 254.0:
												pixels.append((13, 14))
												return 2 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												return 4 # approximately 1 were 4 out of 1 samples at leaf node
										else:
											return 7 # approximately 1 were 7 out of 1 samples at leaf node
							else:
								if features[19][6] <= 4.5:
									pixels.append((19, 6))
									if features[18][14] <= 202.5:
										pixels.append((18, 14))
										if features[6][12] <= 205.0:
											pixels.append((6, 12))
											if features[22][14] <= 71.5:
												pixels.append((22, 14))
												if features[17][11] <= 149.5:
													pixels.append((17, 11))
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													return 4 # approximately 1 were 4 out of 1 samples at leaf node
											else:
												return 5 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											return 9 # approximately 12 were 9 out of 12 samples at leaf node
									else:
										if features[12][13] <= 106.5:
											pixels.append((12, 13))
											if features[11][11] <= 180.0:
												pixels.append((11, 11))
												if features[11][15] <= 126.0:
													pixels.append((11, 15))
													return 2 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													return 8 # approximately 2 were 8 out of 2 samples at leaf node
											else:
												return 4 # approximately 2 were 4 out of 2 samples at leaf node
										else:
											return 1 # approximately 4 were 1 out of 4 samples at leaf node
								else:
									return 2 # approximately 6 were 2 out of 6 samples at leaf node
						else:
							if features[11][12] <= 2.5:
								pixels.append((11, 12))
								if features[16][14] <= 4.0:
									pixels.append((16, 14))
									if features[22][11] <= 219.5:
										pixels.append((22, 11))
										if features[9][11] <= 12.5:
											pixels.append((9, 11))
											if features[8][17] <= 34.5:
												pixels.append((8, 17))
												return 5 # approximately 3 were 5 out of 3 samples at leaf node
											else:
												if features[9][6] <= 26.5:
													pixels.append((9, 6))
													return 2 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													return 7 # approximately 1 were 7 out of 1 samples at leaf node
										else:
											return 6 # approximately 3 were 6 out of 3 samples at leaf node
									else:
										return 3 # approximately 6 were 3 out of 6 samples at leaf node
								else:
									if features[4][17] <= 90.0:
										pixels.append((4, 17))
										if features[11][10] <= 156.5:
											pixels.append((11, 10))
											if features[10][14] <= 253.5:
												pixels.append((10, 14))
												return 2 # approximately 71 were 2 out of 71 samples at leaf node
											else:
												if features[11][18] <= 2.5:
													pixels.append((11, 18))
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													return 2 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											if features[19][13] <= 68.0:
												pixels.append((19, 13))
												return 8 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												return 4 # approximately 1 were 4 out of 1 samples at leaf node
									else:
										if features[15][17] <= 106.0:
											pixels.append((15, 17))
											return 1 # approximately 4 were 1 out of 4 samples at leaf node
										else:
											if features[8][14] <= 127.0:
												pixels.append((8, 14))
												return 2 # approximately 2 were 2 out of 2 samples at leaf node
											else:
												if features[16][13] <= 217.0:
													pixels.append((16, 13))
													return 5 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													return 8 # approximately 1 were 8 out of 1 samples at leaf node
							else:
								if features[15][10] <= 85.0:
									pixels.append((15, 10))
									if features[15][15] <= 166.5:
										pixels.append((15, 15))
										if features[12][9] <= 251.5:
											pixels.append((12, 9))
											if features[5][20] <= 32.5:
												pixels.append((5, 20))
												return 3 # approximately 29 were 3 out of 29 samples at leaf node
											else:
												return 5 # approximately 2 were 5 out of 2 samples at leaf node
										else:
											if features[22][13] <= 96.0:
												pixels.append((22, 13))
												if features[11][7] <= 102.5:
													pixels.append((11, 7))
													if features[20][16] <= 220.0:
														pixels.append((20, 16))
														return 6 # approximately 1 were 6 out of 1 samples at leaf node
													else:
														return 4 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													return 8 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												return 5 # approximately 2 were 5 out of 2 samples at leaf node
									else:
										if features[12][15] <= 222.0:
											pixels.append((12, 15))
											if features[3][17] <= 109.0:
												pixels.append((3, 17))
												if features[5][15] <= 140.5:
													pixels.append((5, 15))
													return 8 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													return 9 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												return 6 # approximately 3 were 6 out of 3 samples at leaf node
										else:
											if features[18][5] <= 84.0:
												pixels.append((18, 5))
												return 1 # approximately 8 were 1 out of 8 samples at leaf node
											else:
												if features[18][12] <= 126.5:
													pixels.append((18, 12))
													return 5 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
								else:
									if features[22][14] <= 254.5:
										pixels.append((22, 14))
										if features[6][20] <= 116.0:
											pixels.append((6, 20))
											return 6 # approximately 26 were 6 out of 26 samples at leaf node
										else:
											return 5 # approximately 1 were 5 out of 1 samples at leaf node
									else:
										if features[6][16] <= 159.5:
											pixels.append((6, 16))
											return 0 # approximately 2 were 0 out of 2 samples at leaf node
										else:
											return 1 # approximately 1 were 1 out of 1 samples at leaf node
				else:
					if features[11][12] <= 98.0:
						pixels.append((11, 12))
						if features[12][16] <= 142.0:
							pixels.append((12, 16))
							if features[11][10] <= 161.5:
								pixels.append((11, 10))
								if features[24][11] <= 23.0:
									pixels.append((24, 11))
									if features[9][15] <= 252.5:
										pixels.append((9, 15))
										if features[18][6] <= 1.5:
											pixels.append((18, 6))
											if features[17][14] <= 13.0:
												pixels.append((17, 14))
												if features[7][18] <= 5.0:
													pixels.append((7, 18))
													return 2 # approximately 2 were 2 out of 2 samples at leaf node
												else:
													return 3 # approximately 6 were 3 out of 6 samples at leaf node
											else:
												if features[5][17] <= 21.5:
													pixels.append((5, 17))
													if features[16][9] <= 126.5:
														pixels.append((16, 9))
														return 7 # approximately 1 were 7 out of 1 samples at leaf node
													else:
														return 9 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													if features[13][14] <= 216.0:
														pixels.append((13, 14))
														return 2 # approximately 28 were 2 out of 28 samples at leaf node
													else:
														return 3 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											if features[9][24] <= 20.5:
												pixels.append((9, 24))
												if features[10][14] <= 224.5:
													pixels.append((10, 14))
													return 2 # approximately 292 were 2 out of 292 samples at leaf node
												else:
													return 8 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												return 6 # approximately 1 were 6 out of 1 samples at leaf node
									else:
										if features[10][20] <= 6.0:
											pixels.append((10, 20))
											return 5 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											if features[19][18] <= 126.0:
												pixels.append((19, 18))
												return 0 # approximately 1 were 0 out of 1 samples at leaf node
											else:
												return 8 # approximately 1 were 8 out of 1 samples at leaf node
								else:
									if features[5][21] <= 169.5:
										pixels.append((5, 21))
										return 8 # approximately 4 were 8 out of 4 samples at leaf node
									else:
										return 5 # approximately 1 were 5 out of 1 samples at leaf node
							else:
								if features[16][18] <= 6.5:
									pixels.append((16, 18))
									return 8 # approximately 4 were 8 out of 4 samples at leaf node
								else:
									if features[16][14] <= 15.0:
										pixels.append((16, 14))
										if features[13][13] <= 110.0:
											pixels.append((13, 13))
											return 0 # approximately 4 were 0 out of 4 samples at leaf node
										else:
											return 5 # approximately 2 were 5 out of 2 samples at leaf node
									else:
										if features[18][17] <= 206.5:
											pixels.append((18, 17))
											if features[10][11] <= 241.0:
												pixels.append((10, 11))
												if features[16][21] <= 55.5:
													pixels.append((16, 21))
													return 9 # approximately 3 were 9 out of 3 samples at leaf node
												else:
													return 6 # approximately 1 were 6 out of 1 samples at leaf node
											else:
												return 4 # approximately 3 were 4 out of 3 samples at leaf node
										else:
											return 2 # approximately 5 were 2 out of 5 samples at leaf node
						else:
							if features[20][14] <= 232.5:
								pixels.append((20, 14))
								if features[14][19] <= 18.0:
									pixels.append((14, 19))
									if features[8][12] <= 237.5:
										pixels.append((8, 12))
										return 8 # approximately 5 were 8 out of 5 samples at leaf node
									else:
										return 9 # approximately 1 were 9 out of 1 samples at leaf node
								else:
									if features[13][8] <= 4.0:
										pixels.append((13, 8))
										if features[18][9] <= 212.0:
											pixels.append((18, 9))
											if features[21][8] <= 58.5:
												pixels.append((21, 8))
												return 5 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												return 3 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											return 2 # approximately 2 were 2 out of 2 samples at leaf node
									else:
										return 4 # approximately 2 were 4 out of 2 samples at leaf node
							else:
								if features[15][8] <= 144.5:
									pixels.append((15, 8))
									return 3 # approximately 11 were 3 out of 11 samples at leaf node
								else:
									return 5 # approximately 1 were 5 out of 1 samples at leaf node
					else:
						if features[11][20] <= 10.0:
							pixels.append((11, 20))
							if features[17][9] <= 252.5:
								pixels.append((17, 9))
								return 5 # approximately 14 were 5 out of 14 samples at leaf node
							else:
								if features[9][12] <= 123.5:
									pixels.append((9, 12))
									return 4 # approximately 1 were 4 out of 1 samples at leaf node
								else:
									return 6 # approximately 4 were 6 out of 4 samples at leaf node
						else:
							if features[14][16] <= 95.5:
								pixels.append((14, 16))
								if features[13][10] <= 49.5:
									pixels.append((13, 10))
									if features[9][14] <= 1.0:
										pixels.append((9, 14))
										return 3 # approximately 2 were 3 out of 2 samples at leaf node
									else:
										return 2 # approximately 5 were 2 out of 5 samples at leaf node
								else:
									return 0 # approximately 14 were 0 out of 14 samples at leaf node
							else:
								if features[13][9] <= 58.5:
									pixels.append((13, 9))
									if features[12][18] <= 83.0:
										pixels.append((12, 18))
										return 2 # approximately 1 were 2 out of 1 samples at leaf node
									else:
										return 8 # approximately 21 were 8 out of 21 samples at leaf node
								else:
									if features[21][13] <= 236.0:
										pixels.append((21, 13))
										return 4 # approximately 11 were 4 out of 11 samples at leaf node
									else:
										return 2 # approximately 1 were 2 out of 1 samples at leaf node
			else:
				if features[12][12] <= 1.5:
					pixels.append((12, 12))
					if features[13][8] <= 135.0:
						pixels.append((13, 8))
						if features[12][13] <= 10.5:
							pixels.append((12, 13))
							if features[12][10] <= 214.5:
								pixels.append((12, 10))
								if features[24][9] <= 4.5:
									pixels.append((24, 9))
									if features[13][6] <= 221.5:
										pixels.append((13, 6))
										if features[18][2] <= 97.0:
											pixels.append((18, 2))
											if features[24][4] <= 12.5:
												pixels.append((24, 4))
												if features[13][5] <= 252.5:
													pixels.append((13, 5))
													if features[17][13] <= 9.5:
														pixels.append((17, 13))
														if features[12][15] <= 4.5:
															pixels.append((12, 15))
															if features[16][16] <= 29.0:
																pixels.append((16, 16))
																if features[5][14] <= 45.5:
																	pixels.append((5, 14))
																	return 4 # approximately 1 were 4 out of 1 samples at leaf node
																else:
																	return 3 # approximately 2 were 3 out of 2 samples at leaf node
															else:
																if features[12][9] <= 69.0:
																	pixels.append((12, 9))
																	if features[19][3] <= 170.5:
																		pixels.append((19, 3))
																		if features[12][7] <= 124.5:
																			pixels.append((12, 7))
																			return 2 # approximately 89 were 2 out of 89 samples at leaf node
																		else:
																			return 9 # approximately 1 were 9 out of 1 samples at leaf node
																	else:
																		return 3 # approximately 1 were 3 out of 1 samples at leaf node
																else:
																	if features[18][10] <= 78.0:
																		pixels.append((18, 10))
																		return 4 # approximately 1 were 4 out of 1 samples at leaf node
																	else:
																		return 0 # approximately 1 were 0 out of 1 samples at leaf node
														else:
															if features[17][11] <= 56.5:
																pixels.append((17, 11))
																if features[8][19] <= 9.5:
																	pixels.append((8, 19))
																	if features[7][7] <= 77.5:
																		pixels.append((7, 7))
																		return 5 # approximately 1 were 5 out of 1 samples at leaf node
																	else:
																		return 1 # approximately 1 were 1 out of 1 samples at leaf node
																else:
																	return 3 # approximately 10 were 3 out of 10 samples at leaf node
															else:
																return 2 # approximately 6 were 2 out of 6 samples at leaf node
													else:
														if features[11][14] <= 222.5:
															pixels.append((11, 14))
															if features[24][17] <= 229.0:
																pixels.append((24, 17))
																if features[11][3] <= 3.0:
																	pixels.append((11, 3))
																	if features[24][8] <= 198.0:
																		pixels.append((24, 8))
																		if features[23][12] <= 179.5:
																			pixels.append((23, 12))
																			if features[24][20] <= 243.5:
																				pixels.append((24, 20))
																				if features[7][3] <= 48.5:
																					pixels.append((7, 3))
																					if features[12][14] <= 172.5:
																						pixels.append((12, 14))
																						if features[7][23] <= 126.5:
																							pixels.append((7, 23))
																							if features[24][6] <= 201.0:
																								pixels.append((24, 6))
																								if features[22][12] <= 253.5:
																									pixels.append((22, 12))
																									if features[13][14] <= 254.5:
																										pixels.append((13, 14))
																										if features[21][12] <= 254.5:
																											pixels.append((21, 12))
																											if features[8][18] <= 254.5:
																												pixels.append((8, 18))
																												return 2 # approximately 1199 were 2 out of 1199 samples at leaf node
																											else:
																												if features[22][11] <= 215.0:
																													pixels.append((22, 11))
																													return 2 # approximately 32 were 2 out of 32 samples at leaf node
																												else:
																													return 3 # approximately 1 were 3 out of 1 samples at leaf node
																										else:
																											if features[17][13] <= 37.5:
																												pixels.append((17, 13))
																												return 1 # approximately 1 were 1 out of 1 samples at leaf node
																											else:
																												return 2 # approximately 20 were 2 out of 20 samples at leaf node
																									else:
																										if features[14][17] <= 167.0:
																											pixels.append((14, 17))
																											return 3 # approximately 1 were 3 out of 1 samples at leaf node
																										else:
																											return 2 # approximately 3 were 2 out of 3 samples at leaf node
																								else:
																									if features[21][9] <= 200.0:
																										pixels.append((21, 9))
																										if features[17][13] <= 237.0:
																											pixels.append((17, 13))
																											return 2 # approximately 1 were 2 out of 1 samples at leaf node
																										else:
																											return 3 # approximately 2 were 3 out of 2 samples at leaf node
																									else:
																										return 2 # approximately 9 were 2 out of 9 samples at leaf node
																							else:
																								if features[7][11] <= 75.0:
																									pixels.append((7, 11))
																									return 7 # approximately 1 were 7 out of 1 samples at leaf node
																								else:
																									return 2 # approximately 2 were 2 out of 2 samples at leaf node
																						else:
																							if features[7][18] <= 10.5:
																								pixels.append((7, 18))
																								return 8 # approximately 1 were 8 out of 1 samples at leaf node
																							else:
																								return 2 # approximately 2 were 2 out of 2 samples at leaf node
																					else:
																						if features[14][12] <= 30.5:
																							pixels.append((14, 12))
																							return 1 # approximately 2 were 1 out of 2 samples at leaf node
																						else:
																							return 2 # approximately 9 were 2 out of 9 samples at leaf node
																				else:
																					if features[17][3] <= 5.0:
																						pixels.append((17, 3))
																						return 2 # approximately 1 were 2 out of 1 samples at leaf node
																					else:
																						return 3 # approximately 1 were 3 out of 1 samples at leaf node
																			else:
																				if features[8][8] <= 91.5:
																					pixels.append((8, 8))
																					return 2 # approximately 1 were 2 out of 1 samples at leaf node
																				else:
																					return 7 # approximately 1 were 7 out of 1 samples at leaf node
																		else:
																			return 1 # approximately 1 were 1 out of 1 samples at leaf node
																	else:
																		return 7 # approximately 1 were 7 out of 1 samples at leaf node
																else:
																	return 9 # approximately 1 were 9 out of 1 samples at leaf node
															else:
																if features[14][18] <= 130.5:
																	pixels.append((14, 18))
																	return 3 # approximately 1 were 3 out of 1 samples at leaf node
																else:
																	return 7 # approximately 1 were 7 out of 1 samples at leaf node
														else:
															if features[17][13] <= 253.0:
																pixels.append((17, 13))
																return 8 # approximately 2 were 8 out of 2 samples at leaf node
															else:
																if features[9][18] <= 229.5:
																	pixels.append((9, 18))
																	return 3 # approximately 1 were 3 out of 1 samples at leaf node
																else:
																	return 2 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													return 4 # approximately 2 were 4 out of 2 samples at leaf node
											else:
												if features[17][14] <= 244.5:
													pixels.append((17, 14))
													return 7 # approximately 2 were 7 out of 2 samples at leaf node
												else:
													if features[7][21] <= 111.5:
														pixels.append((7, 21))
														return 3 # approximately 2 were 3 out of 2 samples at leaf node
													else:
														return 2 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											return 3 # approximately 4 were 3 out of 4 samples at leaf node
									else:
										if features[9][19] <= 57.5:
											pixels.append((9, 19))
											return 4 # approximately 4 were 4 out of 4 samples at leaf node
										else:
											return 9 # approximately 5 were 9 out of 5 samples at leaf node
								else:
									if features[18][18] <= 13.0:
										pixels.append((18, 18))
										if features[8][10] <= 77.0:
											pixels.append((8, 10))
											if features[13][17] <= 200.0:
												pixels.append((13, 17))
												if features[11][17] <= 253.5:
													pixels.append((11, 17))
													return 1 # approximately 2 were 1 out of 2 samples at leaf node
												else:
													return 9 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												return 7 # approximately 12 were 7 out of 12 samples at leaf node
										else:
											if features[13][13] <= 50.0:
												pixels.append((13, 13))
												return 2 # approximately 2 were 2 out of 2 samples at leaf node
											else:
												return 3 # approximately 4 were 3 out of 4 samples at leaf node
									else:
										return 2 # approximately 10 were 2 out of 10 samples at leaf node
							else:
								if features[18][17] <= 27.0:
									pixels.append((18, 17))
									if features[20][9] <= 254.5:
										pixels.append((20, 9))
										return 8 # approximately 5 were 8 out of 5 samples at leaf node
									else:
										return 2 # approximately 2 were 2 out of 2 samples at leaf node
								else:
									if features[7][16] <= 30.0:
										pixels.append((7, 16))
										if features[5][14] <= 188.5:
											pixels.append((5, 14))
											return 4 # approximately 3 were 4 out of 3 samples at leaf node
										else:
											if features[21][13] <= 239.5:
												pixels.append((21, 13))
												return 6 # approximately 2 were 6 out of 2 samples at leaf node
											else:
												return 0 # approximately 1 were 0 out of 1 samples at leaf node
									else:
										if features[8][17] <= 245.5:
											pixels.append((8, 17))
											return 9 # approximately 7 were 9 out of 7 samples at leaf node
										else:
											return 4 # approximately 1 were 4 out of 1 samples at leaf node
						else:
							if features[18][9] <= 25.0:
								pixels.append((18, 9))
								if features[17][13] <= 140.5:
									pixels.append((17, 13))
									if features[17][8] <= 224.5:
										pixels.append((17, 8))
										return 3 # approximately 29 were 3 out of 29 samples at leaf node
									else:
										return 8 # approximately 1 were 8 out of 1 samples at leaf node
								else:
									if features[7][13] <= 69.5:
										pixels.append((7, 13))
										return 1 # approximately 8 were 1 out of 8 samples at leaf node
									else:
										if features[14][16] <= 253.5:
											pixels.append((14, 16))
											return 2 # approximately 3 were 2 out of 3 samples at leaf node
										else:
											return 9 # approximately 1 were 9 out of 1 samples at leaf node
							else:
								if features[10][13] <= 128.0:
									pixels.append((10, 13))
									if features[15][4] <= 79.0:
										pixels.append((15, 4))
										if features[12][17] <= 87.0:
											pixels.append((12, 17))
											return 3 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											if features[3][19] <= 169.0:
												pixels.append((3, 19))
												return 2 # approximately 40 were 2 out of 40 samples at leaf node
											else:
												return 3 # approximately 1 were 3 out of 1 samples at leaf node
									else:
										return 3 # approximately 1 were 3 out of 1 samples at leaf node
								else:
									if features[8][19] <= 140.0:
										pixels.append((8, 19))
										return 8 # approximately 3 were 8 out of 3 samples at leaf node
									else:
										if features[14][18] <= 151.5:
											pixels.append((14, 18))
											return 3 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											return 2 # approximately 1 were 2 out of 1 samples at leaf node
					else:
						if features[6][13] <= 16.5:
							pixels.append((6, 13))
							if features[9][17] <= 162.0:
								pixels.append((9, 17))
								if features[19][12] <= 252.5:
									pixels.append((19, 12))
									return 2 # approximately 9 were 2 out of 9 samples at leaf node
								else:
									if features[16][14] <= 181.5:
										pixels.append((16, 14))
										if features[7][17] <= 226.0:
											pixels.append((7, 17))
											return 7 # approximately 1 were 7 out of 1 samples at leaf node
										else:
											return 0 # approximately 1 were 0 out of 1 samples at leaf node
									else:
										return 4 # approximately 2 were 4 out of 2 samples at leaf node
							else:
								if features[9][11] <= 253.0:
									pixels.append((9, 11))
									return 4 # approximately 54 were 4 out of 54 samples at leaf node
								else:
									return 3 # approximately 1 were 3 out of 1 samples at leaf node
						else:
							if features[4][14] <= 6.5:
								pixels.append((4, 14))
								if features[16][9] <= 2.0:
									pixels.append((16, 9))
									if features[7][18] <= 249.5:
										pixels.append((7, 18))
										if features[11][17] <= 98.5:
											pixels.append((11, 17))
											if features[9][18] <= 39.0:
												pixels.append((9, 18))
												return 7 # approximately 1 were 7 out of 1 samples at leaf node
											else:
												return 2 # approximately 6 were 2 out of 6 samples at leaf node
										else:
											if features[10][9] <= 201.5:
												pixels.append((10, 9))
												if features[18][11] <= 244.5:
													pixels.append((18, 11))
													return 7 # approximately 2 were 7 out of 2 samples at leaf node
												else:
													return 4 # approximately 1 were 4 out of 1 samples at leaf node
											else:
												return 9 # approximately 3 were 9 out of 3 samples at leaf node
									else:
										return 8 # approximately 5 were 8 out of 5 samples at leaf node
								else:
									if features[5][15] <= 8.5:
										pixels.append((5, 15))
										return 4 # approximately 4 were 4 out of 4 samples at leaf node
									else:
										if features[19][8] <= 252.5:
											pixels.append((19, 8))
											if features[21][12] <= 250.5:
												pixels.append((21, 12))
												if features[13][11] <= 104.0:
													pixels.append((13, 11))
													return 9 # approximately 45 were 9 out of 45 samples at leaf node
												else:
													return 2 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												if features[21][17] <= 126.5:
													pixels.append((21, 17))
													return 4 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													return 8 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											return 0 # approximately 3 were 0 out of 3 samples at leaf node
							else:
								if features[15][10] <= 205.5:
									pixels.append((15, 10))
									if features[15][15] <= 54.5:
										pixels.append((15, 15))
										if features[12][11] <= 124.5:
											pixels.append((12, 11))
											return 0 # approximately 1 were 0 out of 1 samples at leaf node
										else:
											return 4 # approximately 1 were 4 out of 1 samples at leaf node
									else:
										return 6 # approximately 11 were 6 out of 11 samples at leaf node
								else:
									if features[10][7] <= 247.0:
										pixels.append((10, 7))
										return 2 # approximately 13 were 2 out of 13 samples at leaf node
									else:
										return 8 # approximately 1 were 8 out of 1 samples at leaf node
				else:
					if features[15][8] <= 11.5:
						pixels.append((15, 8))
						if features[17][12] <= 8.5:
							pixels.append((17, 12))
							if features[11][15] <= 53.5:
								pixels.append((11, 15))
								if features[11][18] <= 11.5:
									pixels.append((11, 18))
									if features[7][14] <= 119.0:
										pixels.append((7, 14))
										return 3 # approximately 2 were 3 out of 2 samples at leaf node
									else:
										return 5 # approximately 10 were 5 out of 10 samples at leaf node
								else:
									if features[21][14] <= 164.5:
										pixels.append((21, 14))
										if features[7][17] <= 242.5:
											pixels.append((7, 17))
											if features[9][18] <= 31.0:
												pixels.append((9, 18))
												if features[10][11] <= 70.5:
													pixels.append((10, 11))
													return 8 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													return 9 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												return 2 # approximately 9 were 2 out of 9 samples at leaf node
										else:
											if features[6][15] <= 216.0:
												pixels.append((6, 15))
												return 0 # approximately 2 were 0 out of 2 samples at leaf node
											else:
												return 9 # approximately 3 were 9 out of 3 samples at leaf node
									else:
										if features[20][7] <= 10.0:
											pixels.append((20, 7))
											if features[19][15] <= 162.0:
												pixels.append((19, 15))
												return 8 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												return 6 # approximately 1 were 6 out of 1 samples at leaf node
										else:
											return 3 # approximately 10 were 3 out of 10 samples at leaf node
							else:
								if features[8][23] <= 6.0:
									pixels.append((8, 23))
									if features[16][10] <= 212.5:
										pixels.append((16, 10))
										if features[10][7] <= 243.0:
											pixels.append((10, 7))
											return 3 # approximately 170 were 3 out of 170 samples at leaf node
										else:
											return 4 # approximately 1 were 4 out of 1 samples at leaf node
									else:
										if features[19][10] <= 238.5:
											pixels.append((19, 10))
											return 8 # approximately 2 were 8 out of 2 samples at leaf node
										else:
											if features[21][13] <= 211.5:
												pixels.append((21, 13))
												return 2 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												return 3 # approximately 1 were 3 out of 1 samples at leaf node
								else:
									if features[10][20] <= 126.0:
										pixels.append((10, 20))
										return 5 # approximately 4 were 5 out of 4 samples at leaf node
									else:
										return 3 # approximately 1 were 3 out of 1 samples at leaf node
						else:
							if features[10][15] <= 247.0:
								pixels.append((10, 15))
								if features[20][21] <= 4.5:
									pixels.append((20, 21))
									if features[15][10] <= 218.0:
										pixels.append((15, 10))
										if features[16][12] <= 194.5:
											pixels.append((16, 12))
											if features[18][10] <= 181.0:
												pixels.append((18, 10))
												if features[12][16] <= 103.0:
													pixels.append((12, 16))
													return 8 # approximately 4 were 8 out of 4 samples at leaf node
												else:
													if features[18][12] <= 252.0:
														pixels.append((18, 12))
														return 9 # approximately 6 were 9 out of 6 samples at leaf node
													else:
														if features[17][16] <= 132.0:
															pixels.append((17, 16))
															return 4 # approximately 2 were 4 out of 2 samples at leaf node
														else:
															return 1 # approximately 1 were 1 out of 1 samples at leaf node
											else:
												if features[4][20] <= 14.5:
													pixels.append((4, 20))
													return 2 # approximately 5 were 2 out of 5 samples at leaf node
												else:
													return 3 # approximately 2 were 3 out of 2 samples at leaf node
										else:
											if features[13][16] <= 160.0:
												pixels.append((13, 16))
												if features[19][13] <= 225.5:
													pixels.append((19, 13))
													if features[16][12] <= 231.0:
														pixels.append((16, 12))
														return 0 # approximately 1 were 0 out of 1 samples at leaf node
													else:
														return 1 # approximately 1 were 1 out of 1 samples at leaf node
												else:
													return 2 # approximately 3 were 2 out of 3 samples at leaf node
											else:
												return 8 # approximately 27 were 8 out of 27 samples at leaf node
									else:
										if features[20][12] <= 221.5:
											pixels.append((20, 12))
											return 4 # approximately 7 were 4 out of 7 samples at leaf node
										else:
											if features[10][18] <= 239.0:
												pixels.append((10, 18))
												return 6 # approximately 4 were 6 out of 4 samples at leaf node
											else:
												if features[15][18] <= 250.0:
													pixels.append((15, 18))
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													return 0 # approximately 1 were 0 out of 1 samples at leaf node
								else:
									if features[22][19] <= 247.5:
										pixels.append((22, 19))
										return 2 # approximately 14 were 2 out of 14 samples at leaf node
									else:
										return 8 # approximately 3 were 8 out of 3 samples at leaf node
							else:
								if features[15][18] <= 13.0:
									pixels.append((15, 18))
									if features[17][11] <= 98.0:
										pixels.append((17, 11))
										if features[5][20] <= 9.5:
											pixels.append((5, 20))
											return 9 # approximately 1 were 9 out of 1 samples at leaf node
										else:
											return 5 # approximately 1 were 5 out of 1 samples at leaf node
									else:
										return 1 # approximately 18 were 1 out of 18 samples at leaf node
								else:
									if features[16][11] <= 184.0:
										pixels.append((16, 11))
										if features[9][15] <= 253.0:
											pixels.append((9, 15))
											return 3 # approximately 7 were 3 out of 7 samples at leaf node
										else:
											return 5 # approximately 1 were 5 out of 1 samples at leaf node
									else:
										if features[6][12] <= 116.5:
											pixels.append((6, 12))
											return 6 # approximately 2 were 6 out of 2 samples at leaf node
										else:
											if features[16][13] <= 227.0:
												pixels.append((16, 13))
												return 8 # approximately 2 were 8 out of 2 samples at leaf node
											else:
												return 2 # approximately 2 were 2 out of 2 samples at leaf node
					else:
						if features[20][9] <= 29.5:
							pixels.append((20, 9))
							if features[21][13] <= 115.5:
								pixels.append((21, 13))
								if features[11][17] <= 17.5:
									pixels.append((11, 17))
									if features[9][7] <= 84.0:
										pixels.append((9, 7))
										return 2 # approximately 2 were 2 out of 2 samples at leaf node
									else:
										return 8 # approximately 1 were 8 out of 1 samples at leaf node
								else:
									if features[14][9] <= 62.5:
										pixels.append((14, 9))
										return 9 # approximately 1 were 9 out of 1 samples at leaf node
									else:
										if features[19][14] <= 250.5:
											pixels.append((19, 14))
											return 4 # approximately 69 were 4 out of 69 samples at leaf node
										else:
											return 9 # approximately 1 were 9 out of 1 samples at leaf node
							else:
								if features[17][21] <= 180.0:
									pixels.append((17, 21))
									return 3 # approximately 7 were 3 out of 7 samples at leaf node
								else:
									if features[20][18] <= 125.5:
										pixels.append((20, 18))
										return 2 # approximately 1 were 2 out of 1 samples at leaf node
									else:
										if features[15][13] <= 125.5:
											pixels.append((15, 13))
											return 0 # approximately 1 were 0 out of 1 samples at leaf node
										else:
											return 8 # approximately 1 were 8 out of 1 samples at leaf node
						else:
							if features[14][14] <= 0.5:
								pixels.append((14, 14))
								if features[15][9] <= 205.0:
									pixels.append((15, 9))
									if features[15][8] <= 218.5:
										pixels.append((15, 8))
										if features[17][16] <= 229.0:
											pixels.append((17, 16))
											return 5 # approximately 2 were 5 out of 2 samples at leaf node
										else:
											return 2 # approximately 5 were 2 out of 5 samples at leaf node
									else:
										if features[8][15] <= 232.5:
											pixels.append((8, 15))
											if features[14][5] <= 9.5:
												pixels.append((14, 5))
												return 8 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												return 4 # approximately 1 were 4 out of 1 samples at leaf node
										else:
											return 0 # approximately 3 were 0 out of 3 samples at leaf node
								else:
									if features[17][24] <= 41.5:
										pixels.append((17, 24))
										return 0 # approximately 46 were 0 out of 46 samples at leaf node
									else:
										if features[7][13] <= 247.5:
											pixels.append((7, 13))
											return 4 # approximately 2 were 4 out of 2 samples at leaf node
										else:
											return 6 # approximately 1 were 6 out of 1 samples at leaf node
							else:
								if features[10][12] <= 241.0:
									pixels.append((10, 12))
									if features[17][7] <= 1.5:
										pixels.append((17, 7))
										if features[18][9] <= 5.0:
											pixels.append((18, 9))
											if features[22][10] <= 11.0:
												pixels.append((22, 10))
												return 2 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												return 3 # approximately 11 were 3 out of 11 samples at leaf node
										else:
											if features[10][17] <= 6.0:
												pixels.append((10, 17))
												if features[15][21] <= 77.5:
													pixels.append((15, 21))
													return 8 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													return 5 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												return 2 # approximately 6 were 2 out of 6 samples at leaf node
									else:
										if features[14][9] <= 19.5:
											pixels.append((14, 9))
											if features[20][9] <= 252.5:
												pixels.append((20, 9))
												if features[17][13] <= 178.5:
													pixels.append((17, 13))
													if features[20][7] <= 126.0:
														pixels.append((20, 7))
														return 6 # approximately 1 were 6 out of 1 samples at leaf node
													else:
														return 8 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													return 2 # approximately 2 were 2 out of 2 samples at leaf node
											else:
												return 3 # approximately 4 were 3 out of 4 samples at leaf node
										else:
											if features[12][7] <= 185.5:
												pixels.append((12, 7))
												if features[7][24] <= 35.0:
													pixels.append((7, 24))
													if features[5][15] <= 7.5:
														pixels.append((5, 15))
														return 8 # approximately 1 were 8 out of 1 samples at leaf node
													else:
														return 2 # approximately 82 were 2 out of 82 samples at leaf node
												else:
													return 8 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												return 6 # approximately 1 were 6 out of 1 samples at leaf node
								else:
									if features[9][18] <= 173.0:
										pixels.append((9, 18))
										if features[13][23] <= 113.0:
											pixels.append((13, 23))
											return 6 # approximately 16 were 6 out of 16 samples at leaf node
										else:
											return 0 # approximately 1 were 0 out of 1 samples at leaf node
									else:
										if features[21][16] <= 39.0:
											pixels.append((21, 16))
											return 2 # approximately 5 were 2 out of 5 samples at leaf node
										else:
											if features[14][6] <= 192.5:
												pixels.append((14, 6))
												if features[9][16] <= 45.0:
													pixels.append((9, 16))
													return 9 # approximately 2 were 9 out of 2 samples at leaf node
												else:
													if features[10][17] <= 239.5:
														pixels.append((10, 17))
														return 3 # approximately 2 were 3 out of 2 samples at leaf node
													else:
														if features[4][19] <= 64.0:
															pixels.append((4, 19))
															if features[20][14] <= 252.5:
																pixels.append((20, 14))
																return 4 # approximately 1 were 4 out of 1 samples at leaf node
															else:
																return 6 # approximately 1 were 6 out of 1 samples at leaf node
														else:
															return 8 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												return 0 # approximately 3 were 0 out of 3 samples at leaf node
		else:
			if features[17][12] <= 1.5:
				pixels.append((17, 12))
				if features[10][10] <= 11.5:
					pixels.append((10, 10))
					if features[10][16] <= 3.5:
						pixels.append((10, 16))
						if features[10][19] <= 1.0:
							pixels.append((10, 19))
							if features[9][15] <= 64.5:
								pixels.append((9, 15))
								if features[17][9] <= 110.0:
									pixels.append((17, 9))
									if features[5][16] <= 0.5:
										pixels.append((5, 16))
										if features[8][18] <= 25.0:
											pixels.append((8, 18))
											return 3 # approximately 5 were 3 out of 5 samples at leaf node
										else:
											return 5 # approximately 3 were 5 out of 3 samples at leaf node
									else:
										if features[20][14] <= 253.5:
											pixels.append((20, 14))
											if features[4][10] <= 156.0:
												pixels.append((4, 10))
												if features[11][19] <= 45.5:
													pixels.append((11, 19))
													if features[16][12] <= 208.5:
														pixels.append((16, 12))
														if features[21][14] <= 254.5:
															pixels.append((21, 14))
															return 5 # approximately 130 were 5 out of 130 samples at leaf node
														else:
															if features[18][19] <= 106.5:
																pixels.append((18, 19))
																return 3 # approximately 1 were 3 out of 1 samples at leaf node
															else:
																return 5 # approximately 2 were 5 out of 2 samples at leaf node
													else:
														return 8 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													return 9 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												if features[22][19] <= 181.0:
													pixels.append((22, 19))
													return 3 # approximately 3 were 3 out of 3 samples at leaf node
												else:
													return 5 # approximately 4 were 5 out of 4 samples at leaf node
										else:
											if features[23][9] <= 19.0:
												pixels.append((23, 9))
												return 2 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												return 3 # approximately 1 were 3 out of 1 samples at leaf node
								else:
									if features[12][21] <= 1.5:
										pixels.append((12, 21))
										if features[6][19] <= 195.5:
											pixels.append((6, 19))
											if features[22][11] <= 156.0:
												pixels.append((22, 11))
												if features[21][10] <= 52.5:
													pixels.append((21, 10))
													return 2 # approximately 2 were 2 out of 2 samples at leaf node
												else:
													return 8 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												return 6 # approximately 3 were 6 out of 3 samples at leaf node
										else:
											return 5 # approximately 4 were 5 out of 4 samples at leaf node
									else:
										return 8 # approximately 6 were 8 out of 6 samples at leaf node
							else:
								if features[6][21] <= 2.5:
									pixels.append((6, 21))
									if features[5][14] <= 9.0:
										pixels.append((5, 14))
										if features[21][8] <= 102.5:
											pixels.append((21, 8))
											return 6 # approximately 1 were 6 out of 1 samples at leaf node
										else:
											return 5 # approximately 1 were 5 out of 1 samples at leaf node
									else:
										if features[16][13] <= 83.5:
											pixels.append((16, 13))
											return 3 # approximately 85 were 3 out of 85 samples at leaf node
										else:
											return 1 # approximately 1 were 1 out of 1 samples at leaf node
								else:
									if features[22][10] <= 132.5:
										pixels.append((22, 10))
										return 8 # approximately 1 were 8 out of 1 samples at leaf node
									else:
										return 5 # approximately 7 were 5 out of 7 samples at leaf node
						else:
							if features[13][16] <= 130.0:
								pixels.append((13, 16))
								if features[11][11] <= 7.0:
									pixels.append((11, 11))
									if features[23][11] <= 121.5:
										pixels.append((23, 11))
										if features[6][7] <= 117.5:
											pixels.append((6, 7))
											return 8 # approximately 4 were 8 out of 4 samples at leaf node
										else:
											return 2 # approximately 1 were 2 out of 1 samples at leaf node
									else:
										if features[13][8] <= 51.5:
											pixels.append((13, 8))
											if features[12][16] <= 28.0:
												pixels.append((12, 16))
												if features[4][15] <= 254.5:
													pixels.append((4, 15))
													return 2 # approximately 33 were 2 out of 33 samples at leaf node
												else:
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												return 7 # approximately 1 were 7 out of 1 samples at leaf node
										else:
											if features[6][9] <= 1.0:
												pixels.append((6, 9))
												return 0 # approximately 2 were 0 out of 2 samples at leaf node
											else:
												if features[21][11] <= 106.5:
													pixels.append((21, 11))
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													return 9 # approximately 1 were 9 out of 1 samples at leaf node
								else:
									if features[15][13] <= 229.5:
										pixels.append((15, 13))
										return 0 # approximately 34 were 0 out of 34 samples at leaf node
									else:
										if features[13][13] <= 177.5:
											pixels.append((13, 13))
											return 4 # approximately 1 were 4 out of 1 samples at leaf node
										else:
											return 8 # approximately 1 were 8 out of 1 samples at leaf node
							else:
								if features[17][9] <= 0.5:
									pixels.append((17, 9))
									if features[18][13] <= 231.0:
										pixels.append((18, 13))
										if features[14][7] <= 227.5:
											pixels.append((14, 7))
											if features[10][11] <= 95.0:
												pixels.append((10, 11))
												if features[20][23] <= 162.5:
													pixels.append((20, 23))
													if features[12][23] <= 5.5:
														pixels.append((12, 23))
														if features[11][7] <= 211.5:
															pixels.append((11, 7))
															return 3 # approximately 138 were 3 out of 138 samples at leaf node
														else:
															if features[7][19] <= 126.5:
																pixels.append((7, 19))
																return 9 # approximately 1 were 9 out of 1 samples at leaf node
															else:
																return 3 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														return 8 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													return 8 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												if features[5][16] <= 127.0:
													pixels.append((5, 16))
													return 4 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													return 5 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											if features[9][10] <= 21.5:
												pixels.append((9, 10))
												return 2 # approximately 2 were 2 out of 2 samples at leaf node
											else:
												if features[12][6] <= 252.5:
													pixels.append((12, 6))
													return 8 # approximately 2 were 8 out of 2 samples at leaf node
												else:
													return 9 # approximately 1 were 9 out of 1 samples at leaf node
									else:
										if features[7][10] <= 252.5:
											pixels.append((7, 10))
											return 2 # approximately 3 were 2 out of 3 samples at leaf node
										else:
											return 8 # approximately 2 were 8 out of 2 samples at leaf node
								else:
									if features[15][11] <= 95.5:
										pixels.append((15, 11))
										if features[17][9] <= 20.5:
											pixels.append((17, 9))
											return 6 # approximately 1 were 6 out of 1 samples at leaf node
										else:
											return 3 # approximately 4 were 3 out of 4 samples at leaf node
									else:
										if features[21][17] <= 252.5:
											pixels.append((21, 17))
											if features[5][16] <= 40.5:
												pixels.append((5, 16))
												if features[7][23] <= 21.5:
													pixels.append((7, 23))
													return 2 # approximately 2 were 2 out of 2 samples at leaf node
												else:
													return 4 # approximately 2 were 4 out of 2 samples at leaf node
											else:
												return 8 # approximately 29 were 8 out of 29 samples at leaf node
										else:
											if features[11][9] <= 49.5:
												pixels.append((11, 9))
												return 3 # approximately 3 were 3 out of 3 samples at leaf node
											else:
												return 9 # approximately 1 were 9 out of 1 samples at leaf node
					else:
						if features[9][13] <= 204.5:
							pixels.append((9, 13))
							if features[11][8] <= 172.0:
								pixels.append((11, 8))
								if features[12][14] <= 3.5:
									pixels.append((12, 14))
									if features[18][14] <= 10.5:
										pixels.append((18, 14))
										if features[8][12] <= 79.5:
											pixels.append((8, 12))
											if features[18][8] <= 41.5:
												pixels.append((18, 8))
												return 3 # approximately 20 were 3 out of 20 samples at leaf node
											else:
												return 2 # approximately 2 were 2 out of 2 samples at leaf node
										else:
											if features[11][18] <= 79.5:
												pixels.append((11, 18))
												return 9 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												return 0 # approximately 2 were 0 out of 2 samples at leaf node
									else:
										if features[21][10] <= 165.5:
											pixels.append((21, 10))
											if features[19][21] <= 28.5:
												pixels.append((19, 21))
												if features[8][17] <= 144.0:
													pixels.append((8, 17))
													if features[19][12] <= 32.0:
														pixels.append((19, 12))
														if features[6][11] <= 84.0:
															pixels.append((6, 11))
															return 4 # approximately 1 were 4 out of 1 samples at leaf node
														else:
															return 1 # approximately 1 were 1 out of 1 samples at leaf node
													else:
														return 8 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													return 7 # approximately 6 were 7 out of 6 samples at leaf node
											else:
												return 2 # approximately 3 were 2 out of 3 samples at leaf node
										else:
											return 2 # approximately 12 were 2 out of 12 samples at leaf node
								else:
									if features[17][9] <= 252.5:
										pixels.append((17, 9))
										if features[18][14] <= 237.5:
											pixels.append((18, 14))
											if features[10][12] <= 252.5:
												pixels.append((10, 12))
												if features[24][18] <= 251.5:
													pixels.append((24, 18))
													if features[11][7] <= 253.0:
														pixels.append((11, 7))
														if features[17][24] <= 157.0:
															pixels.append((17, 24))
															if features[9][13] <= 192.5:
																pixels.append((9, 13))
																if features[17][10] <= 175.0:
																	pixels.append((17, 10))
																	if features[17][8] <= 251.0:
																		pixels.append((17, 8))
																		return 3 # approximately 1471 were 3 out of 1471 samples at leaf node
																	else:
																		if features[7][11] <= 14.5:
																			pixels.append((7, 11))
																			if features[10][15] <= 102.0:
																				pixels.append((10, 15))
																				return 2 # approximately 1 were 2 out of 1 samples at leaf node
																			else:
																				return 8 # approximately 1 were 8 out of 1 samples at leaf node
																		else:
																			return 3 # approximately 20 were 3 out of 20 samples at leaf node
																else:
																	if features[22][9] <= 55.0:
																		pixels.append((22, 9))
																		return 8 # approximately 1 were 8 out of 1 samples at leaf node
																	else:
																		return 3 # approximately 5 were 3 out of 5 samples at leaf node
															else:
																if features[20][9] <= 17.5:
																	pixels.append((20, 9))
																	if features[12][10] <= 152.5:
																		pixels.append((12, 10))
																		return 1 # approximately 1 were 1 out of 1 samples at leaf node
																	else:
																		return 0 # approximately 1 were 0 out of 1 samples at leaf node
																else:
																	return 3 # approximately 6 were 3 out of 6 samples at leaf node
														else:
															if features[19][7] <= 111.0:
																pixels.append((19, 7))
																return 3 # approximately 1 were 3 out of 1 samples at leaf node
															else:
																return 2 # approximately 1 were 2 out of 1 samples at leaf node
													else:
														return 8 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													return 5 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												if features[17][10] <= 38.5:
													pixels.append((17, 10))
													if features[21][11] <= 78.5:
														pixels.append((21, 11))
														return 5 # approximately 2 were 5 out of 2 samples at leaf node
													else:
														return 3 # approximately 2 were 3 out of 2 samples at leaf node
												else:
													return 8 # approximately 3 were 8 out of 3 samples at leaf node
										else:
											if features[20][11] <= 12.0:
												pixels.append((20, 11))
												if features[12][5] <= 3.0:
													pixels.append((12, 5))
													return 1 # approximately 8 were 1 out of 8 samples at leaf node
												else:
													return 9 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												return 3 # approximately 10 were 3 out of 10 samples at leaf node
									else:
										if features[15][12] <= 194.0:
											pixels.append((15, 12))
											if features[10][15] <= 238.5:
												pixels.append((10, 15))
												if features[16][9] <= 253.5:
													pixels.append((16, 9))
													return 2 # approximately 2 were 2 out of 2 samples at leaf node
												else:
													return 0 # approximately 1 were 0 out of 1 samples at leaf node
											else:
												return 3 # approximately 3 were 3 out of 3 samples at leaf node
										else:
											return 8 # approximately 5 were 8 out of 5 samples at leaf node
							else:
								if features[17][9] <= 2.0:
									pixels.append((17, 9))
									if features[9][15] <= 92.0:
										pixels.append((9, 15))
										if features[22][10] <= 227.5:
											pixels.append((22, 10))
											if features[8][15] <= 31.0:
												pixels.append((8, 15))
												if features[13][19] <= 3.0:
													pixels.append((13, 19))
													if features[19][19] <= 10.0:
														pixels.append((19, 19))
														return 2 # approximately 1 were 2 out of 1 samples at leaf node
													else:
														return 8 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													if features[23][10] <= 7.5:
														pixels.append((23, 10))
														return 0 # approximately 1 were 0 out of 1 samples at leaf node
													else:
														return 9 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												return 5 # approximately 4 were 5 out of 4 samples at leaf node
										else:
											return 3 # approximately 5 were 3 out of 5 samples at leaf node
									else:
										return 9 # approximately 7 were 9 out of 7 samples at leaf node
								else:
									if features[8][12] <= 129.5:
										pixels.append((8, 12))
										return 8 # approximately 11 were 8 out of 11 samples at leaf node
									else:
										return 3 # approximately 1 were 3 out of 1 samples at leaf node
						else:
							if features[17][9] <= 139.5:
								pixels.append((17, 9))
								if features[6][11] <= 1.5:
									pixels.append((6, 11))
									if features[13][16] <= 157.0:
										pixels.append((13, 16))
										return 5 # approximately 10 were 5 out of 10 samples at leaf node
									else:
										if features[7][18] <= 7.5:
											pixels.append((7, 18))
											if features[15][17] <= 227.0:
												pixels.append((15, 17))
												return 1 # approximately 8 were 1 out of 8 samples at leaf node
											else:
												return 3 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											if features[8][19] <= 245.0:
												pixels.append((8, 19))
												if features[24][11] <= 24.5:
													pixels.append((24, 11))
													if features[24][15] <= 40.0:
														pixels.append((24, 15))
														if features[23][8] <= 47.5:
															pixels.append((23, 8))
															if features[17][13] <= 101.5:
																pixels.append((17, 13))
																return 0 # approximately 1 were 0 out of 1 samples at leaf node
															else:
																return 6 # approximately 1 were 6 out of 1 samples at leaf node
														else:
															return 5 # approximately 2 were 5 out of 2 samples at leaf node
													else:
														return 4 # approximately 3 were 4 out of 3 samples at leaf node
												else:
													return 9 # approximately 5 were 9 out of 5 samples at leaf node
											else:
												return 3 # approximately 4 were 3 out of 4 samples at leaf node
								else:
									if features[8][15] <= 112.5:
										pixels.append((8, 15))
										if features[9][18] <= 56.0:
											pixels.append((9, 18))
											return 5 # approximately 4 were 5 out of 4 samples at leaf node
										else:
											if features[21][13] <= 166.5:
												pixels.append((21, 13))
												return 8 # approximately 2 were 8 out of 2 samples at leaf node
											else:
												return 3 # approximately 2 were 3 out of 2 samples at leaf node
									else:
										if features[11][14] <= 6.0:
											pixels.append((11, 14))
											return 2 # approximately 2 were 2 out of 2 samples at leaf node
										else:
											if features[17][13] <= 69.0:
												pixels.append((17, 13))
												return 3 # approximately 33 were 3 out of 33 samples at leaf node
											else:
												return 1 # approximately 1 were 1 out of 1 samples at leaf node
							else:
								if features[13][15] <= 162.0:
									pixels.append((13, 15))
									if features[20][15] <= 186.5:
										pixels.append((20, 15))
										if features[21][13] <= 50.0:
											pixels.append((21, 13))
											return 5 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											return 8 # approximately 1 were 8 out of 1 samples at leaf node
									else:
										return 0 # approximately 19 were 0 out of 19 samples at leaf node
								else:
									if features[14][21] <= 28.5:
										pixels.append((14, 21))
										return 8 # approximately 14 were 8 out of 14 samples at leaf node
									else:
										return 3 # approximately 2 were 3 out of 2 samples at leaf node
				else:
					if features[10][18] <= 0.5:
						pixels.append((10, 18))
						if features[9][15] <= 128.5:
							pixels.append((9, 15))
							if features[10][20] <= 2.0:
								pixels.append((10, 20))
								if features[17][9] <= 244.5:
									pixels.append((17, 9))
									if features[5][17] <= 2.5:
										pixels.append((5, 17))
										if features[9][14] <= 99.5:
											pixels.append((9, 14))
											if features[11][10] <= 54.0:
												pixels.append((11, 10))
												if features[24][13] <= 33.0:
													pixels.append((24, 13))
													return 3 # approximately 6 were 3 out of 6 samples at leaf node
												else:
													return 5 # approximately 2 were 5 out of 2 samples at leaf node
											else:
												if features[10][16] <= 54.5:
													pixels.append((10, 16))
													if features[11][20] <= 20.0:
														pixels.append((11, 20))
														if features[5][8] <= 248.0:
															pixels.append((5, 8))
															return 5 # approximately 51 were 5 out of 51 samples at leaf node
														else:
															if features[23][18] <= 122.5:
																pixels.append((23, 18))
																return 5 # approximately 1 were 5 out of 1 samples at leaf node
															else:
																return 3 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														return 4 # approximately 2 were 4 out of 2 samples at leaf node
												else:
													if features[19][18] <= 208.0:
														pixels.append((19, 18))
														if features[19][8] <= 13.5:
															pixels.append((19, 8))
															if features[21][8] <= 57.0:
																pixels.append((21, 8))
																if features[5][16] <= 46.5:
																	pixels.append((5, 16))
																	return 8 # approximately 1 were 8 out of 1 samples at leaf node
																else:
																	return 7 # approximately 1 were 7 out of 1 samples at leaf node
															else:
																return 2 # approximately 1 were 2 out of 1 samples at leaf node
														else:
															return 5 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														return 9 # approximately 2 were 9 out of 2 samples at leaf node
										else:
											if features[5][10] <= 100.5:
												pixels.append((5, 10))
												if features[19][7] <= 64.0:
													pixels.append((19, 7))
													if features[10][11] <= 174.5:
														pixels.append((10, 11))
														return 8 # approximately 2 were 8 out of 2 samples at leaf node
													else:
														if features[16][10] <= 122.5:
															pixels.append((16, 10))
															return 3 # approximately 1 were 3 out of 1 samples at leaf node
														else:
															return 0 # approximately 1 were 0 out of 1 samples at leaf node
												else:
													return 5 # approximately 2 were 5 out of 2 samples at leaf node
											else:
												return 3 # approximately 16 were 3 out of 16 samples at leaf node
									else:
										if features[9][16] <= 184.5:
											pixels.append((9, 16))
											if features[18][11] <= 224.5:
												pixels.append((18, 11))
												if features[17][14] <= 164.5:
													pixels.append((17, 14))
													if features[8][24] <= 218.5:
														pixels.append((8, 24))
														if features[12][22] <= 243.5:
															pixels.append((12, 22))
															if features[4][8] <= 218.5:
																pixels.append((4, 8))
																if features[5][7] <= 253.5:
																	pixels.append((5, 7))
																	if features[6][7] <= 253.5:
																		pixels.append((6, 7))
																		if features[9][17] <= 175.5:
																			pixels.append((9, 17))
																			if features[17][8] <= 253.5:
																				pixels.append((17, 8))
																				if features[18][15] <= 253.5:
																					pixels.append((18, 15))
																					if features[10][14] <= 254.5:
																						pixels.append((10, 14))
																						if features[20][14] <= 254.5:
																							pixels.append((20, 14))
																							if features[8][11] <= 1.0:
																								pixels.append((8, 11))
																								if features[8][20] <= 125.5:
																									pixels.append((8, 20))
																									if features[7][13] <= 252.5:
																										pixels.append((7, 13))
																										if features[9][15] <= 88.0:
																											pixels.append((9, 15))
																											return 5 # approximately 50 were 5 out of 50 samples at leaf node
																										else:
																											return 3 # approximately 1 were 3 out of 1 samples at leaf node
																									else:
																										return 3 # approximately 1 were 3 out of 1 samples at leaf node
																								else:
																									return 8 # approximately 1 were 8 out of 1 samples at leaf node
																							else:
																								return 5 # approximately 596 were 5 out of 596 samples at leaf node
																						else:
																							if features[16][15] <= 80.5:
																								pixels.append((16, 15))
																								return 5 # approximately 5 were 5 out of 5 samples at leaf node
																							else:
																								return 9 # approximately 1 were 9 out of 1 samples at leaf node
																					else:
																						if features[19][7] <= 106.0:
																							pixels.append((19, 7))
																							return 5 # approximately 1 were 5 out of 1 samples at leaf node
																						else:
																							return 3 # approximately 1 were 3 out of 1 samples at leaf node
																				else:
																					if features[17][19] <= 116.0:
																						pixels.append((17, 19))
																						return 9 # approximately 1 were 9 out of 1 samples at leaf node
																					else:
																						return 5 # approximately 1 were 5 out of 1 samples at leaf node
																			else:
																				if features[13][20] <= 211.5:
																					pixels.append((13, 20))
																					return 6 # approximately 1 were 6 out of 1 samples at leaf node
																				else:
																					return 5 # approximately 1 were 5 out of 1 samples at leaf node
																		else:
																			if features[7][11] <= 193.0:
																				pixels.append((7, 11))
																				if features[9][7] <= 25.5:
																					pixels.append((9, 7))
																					return 8 # approximately 1 were 8 out of 1 samples at leaf node
																				else:
																					return 3 # approximately 1 were 3 out of 1 samples at leaf node
																			else:
																				return 5 # approximately 2 were 5 out of 2 samples at leaf node
																	else:
																		return 3 # approximately 1 were 3 out of 1 samples at leaf node
																else:
																	return 3 # approximately 1 were 3 out of 1 samples at leaf node
															else:
																return 3 # approximately 1 were 3 out of 1 samples at leaf node
														else:
															return 9 # approximately 1 were 9 out of 1 samples at leaf node
													else:
														return 6 # approximately 1 were 6 out of 1 samples at leaf node
												else:
													if features[17][13] <= 101.0:
														pixels.append((17, 13))
														return 9 # approximately 1 were 9 out of 1 samples at leaf node
													else:
														return 8 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												if features[5][17] <= 196.5:
													pixels.append((5, 17))
													return 8 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													return 6 # approximately 1 were 6 out of 1 samples at leaf node
										else:
											if features[9][18] <= 43.0:
												pixels.append((9, 18))
												return 8 # approximately 4 were 8 out of 4 samples at leaf node
											else:
												if features[20][15] <= 127.0:
													pixels.append((20, 15))
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													if features[13][7] <= 12.5:
														pixels.append((13, 7))
														return 4 # approximately 1 were 4 out of 1 samples at leaf node
													else:
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
								else:
									if features[9][12] <= 252.5:
										pixels.append((9, 12))
										if features[6][17] <= 247.0:
											pixels.append((6, 17))
											if features[14][18] <= 245.5:
												pixels.append((14, 18))
												return 8 # approximately 4 were 8 out of 4 samples at leaf node
											else:
												return 6 # approximately 4 were 6 out of 4 samples at leaf node
										else:
											return 5 # approximately 11 were 5 out of 11 samples at leaf node
									else:
										return 6 # approximately 10 were 6 out of 10 samples at leaf node
							else:
								if features[14][16] <= 47.0:
									pixels.append((14, 16))
									if features[22][20] <= 27.0:
										pixels.append((22, 20))
										return 0 # approximately 16 were 0 out of 16 samples at leaf node
									else:
										return 2 # approximately 1 were 2 out of 1 samples at leaf node
								else:
									if features[18][8] <= 13.0:
										pixels.append((18, 8))
										if features[18][15] <= 224.0:
											pixels.append((18, 15))
											if features[8][22] <= 12.0:
												pixels.append((8, 22))
												return 8 # approximately 5 were 8 out of 5 samples at leaf node
											else:
												if features[23][11] <= 250.0:
													pixels.append((23, 11))
													if features[22][17] <= 44.0:
														pixels.append((22, 17))
														return 9 # approximately 1 were 9 out of 1 samples at leaf node
													else:
														return 5 # approximately 2 were 5 out of 2 samples at leaf node
												else:
													return 3 # approximately 4 were 3 out of 4 samples at leaf node
										else:
											return 4 # approximately 5 were 4 out of 5 samples at leaf node
									else:
										if features[19][16] <= 246.0:
											pixels.append((19, 16))
											return 8 # approximately 20 were 8 out of 20 samples at leaf node
										else:
											return 2 # approximately 1 were 2 out of 1 samples at leaf node
						else:
							if features[7][20] <= 8.5:
								pixels.append((7, 20))
								if features[17][15] <= 47.0:
									pixels.append((17, 15))
									if features[16][10] <= 242.5:
										pixels.append((16, 10))
										if features[16][16] <= 243.5:
											pixels.append((16, 16))
											if features[9][9] <= 254.5:
												pixels.append((9, 9))
												if features[10][14] <= 7.0:
													pixels.append((10, 14))
													return 5 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													if features[5][13] <= 17.0:
														pixels.append((5, 13))
														if features[21][11] <= 251.5:
															pixels.append((21, 11))
															return 3 # approximately 3 were 3 out of 3 samples at leaf node
														else:
															return 5 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														return 3 # approximately 108 were 3 out of 108 samples at leaf node
											else:
												return 9 # approximately 1 were 9 out of 1 samples at leaf node
										else:
											if features[21][19] <= 153.5:
												pixels.append((21, 19))
												return 9 # approximately 2 were 9 out of 2 samples at leaf node
											else:
												if features[23][20] <= 62.5:
													pixels.append((23, 20))
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													return 4 # approximately 1 were 4 out of 1 samples at leaf node
									else:
										if features[16][7] <= 27.0:
											pixels.append((16, 7))
											return 8 # approximately 2 were 8 out of 2 samples at leaf node
										else:
											return 5 # approximately 1 were 5 out of 1 samples at leaf node
								else:
									if features[21][11] <= 9.5:
										pixels.append((21, 11))
										if features[5][13] <= 108.5:
											pixels.append((5, 13))
											return 4 # approximately 10 were 4 out of 10 samples at leaf node
										else:
											if features[8][13] <= 205.0:
												pixels.append((8, 13))
												return 2 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												return 8 # approximately 1 were 8 out of 1 samples at leaf node
									else:
										if features[5][16] <= 60.5:
											pixels.append((5, 16))
											if features[9][10] <= 254.5:
												pixels.append((9, 10))
												return 9 # approximately 5 were 9 out of 5 samples at leaf node
											else:
												return 8 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											if features[5][13] <= 128.0:
												pixels.append((5, 13))
												if features[13][8] <= 122.5:
													pixels.append((13, 8))
													return 1 # approximately 2 were 1 out of 2 samples at leaf node
												else:
													return 5 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												return 3 # approximately 4 were 3 out of 4 samples at leaf node
							else:
								if features[12][19] <= 127.0:
									pixels.append((12, 19))
									if features[10][15] <= 226.0:
										pixels.append((10, 15))
										return 5 # approximately 34 were 5 out of 34 samples at leaf node
									else:
										if features[21][19] <= 41.5:
											pixels.append((21, 19))
											if features[12][9] <= 97.0:
												pixels.append((12, 9))
												return 5 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												if features[11][8] <= 114.5:
													pixels.append((11, 8))
													return 6 # approximately 1 were 6 out of 1 samples at leaf node
												else:
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											return 8 # approximately 3 were 8 out of 3 samples at leaf node
								else:
									if features[13][17] <= 156.5:
										pixels.append((13, 17))
										return 0 # approximately 11 were 0 out of 11 samples at leaf node
									else:
										if features[23][7] <= 41.5:
											pixels.append((23, 7))
											if features[18][18] <= 90.5:
												pixels.append((18, 18))
												return 8 # approximately 2 were 8 out of 2 samples at leaf node
											else:
												return 9 # approximately 1 were 9 out of 1 samples at leaf node
										else:
											return 3 # approximately 3 were 3 out of 3 samples at leaf node
					else:
						if features[13][15] <= 1.0:
							pixels.append((13, 15))
							if features[16][8] <= 5.5:
								pixels.append((16, 8))
								if features[16][10] <= 139.0:
									pixels.append((16, 10))
									if features[10][15] <= 25.5:
										pixels.append((10, 15))
										if features[16][18] <= 49.5:
											pixels.append((16, 18))
											if features[15][10] <= 10.0:
												pixels.append((15, 10))
												return 8 # approximately 6 were 8 out of 6 samples at leaf node
											else:
												if features[7][14] <= 252.5:
													pixels.append((7, 14))
													if features[14][17] <= 169.5:
														pixels.append((14, 17))
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														return 4 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													return 7 # approximately 2 were 7 out of 2 samples at leaf node
										else:
											if features[17][18] <= 253.5:
												pixels.append((17, 18))
												return 2 # approximately 11 were 2 out of 11 samples at leaf node
											else:
												return 4 # approximately 1 were 4 out of 1 samples at leaf node
									else:
										if features[9][18] <= 61.0:
											pixels.append((9, 18))
											if features[8][15] <= 250.5:
												pixels.append((8, 15))
												return 5 # approximately 16 were 5 out of 16 samples at leaf node
											else:
												return 3 # approximately 2 were 3 out of 2 samples at leaf node
										else:
											if features[15][5] <= 59.5:
												pixels.append((15, 5))
												if features[10][16] <= 138.5:
													pixels.append((10, 16))
													if features[8][21] <= 23.5:
														pixels.append((8, 21))
														return 9 # approximately 3 were 9 out of 3 samples at leaf node
													else:
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													return 3 # approximately 7 were 3 out of 7 samples at leaf node
											else:
												return 0 # approximately 4 were 0 out of 4 samples at leaf node
								else:
									return 0 # approximately 13 were 0 out of 13 samples at leaf node
							else:
								if features[15][16] <= 230.5:
									pixels.append((15, 16))
									if features[5][15] <= 5.5:
										pixels.append((5, 15))
										return 9 # approximately 1 were 9 out of 1 samples at leaf node
									else:
										if features[4][8] <= 29.5:
											pixels.append((4, 8))
											return 0 # approximately 210 were 0 out of 210 samples at leaf node
										else:
											return 3 # approximately 1 were 3 out of 1 samples at leaf node
								else:
									if features[8][17] <= 2.0:
										pixels.append((8, 17))
										return 4 # approximately 3 were 4 out of 3 samples at leaf node
									else:
										if features[18][10] <= 126.5:
											pixels.append((18, 10))
											return 2 # approximately 2 were 2 out of 2 samples at leaf node
										else:
											return 6 # approximately 1 were 6 out of 1 samples at leaf node
						else:
							if features[17][9] <= 73.5:
								pixels.append((17, 9))
								if features[22][8] <= 20.5:
									pixels.append((22, 8))
									if features[17][19] <= 2.0:
										pixels.append((17, 19))
										if features[19][13] <= 55.0:
											pixels.append((19, 13))
											if features[14][17] <= 109.5:
												pixels.append((14, 17))
												return 3 # approximately 2 were 3 out of 2 samples at leaf node
											else:
												if features[15][6] <= 118.5:
													pixels.append((15, 6))
													if features[5][10] <= 20.5:
														pixels.append((5, 10))
														return 9 # approximately 24 were 9 out of 24 samples at leaf node
													else:
														if features[9][8] <= 138.0:
															pixels.append((9, 8))
															return 3 # approximately 1 were 3 out of 1 samples at leaf node
														else:
															return 9 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													return 4 # approximately 1 were 4 out of 1 samples at leaf node
										else:
											if features[5][18] <= 63.0:
												pixels.append((5, 18))
												if features[7][12] <= 251.5:
													pixels.append((7, 12))
													if features[15][9] <= 28.0:
														pixels.append((15, 9))
														if features[24][12] <= 148.5:
															pixels.append((24, 12))
															if features[10][9] <= 64.0:
																pixels.append((10, 9))
																return 1 # approximately 1 were 1 out of 1 samples at leaf node
															else:
																return 2 # approximately 2 were 2 out of 2 samples at leaf node
														else:
															return 8 # approximately 2 were 8 out of 2 samples at leaf node
													else:
														return 4 # approximately 5 were 4 out of 5 samples at leaf node
												else:
													if features[9][18] <= 252.5:
														pixels.append((9, 18))
														return 9 # approximately 3 were 9 out of 3 samples at leaf node
													else:
														return 7 # approximately 1 were 7 out of 1 samples at leaf node
											else:
												return 8 # approximately 6 were 8 out of 6 samples at leaf node
									else:
										if features[12][14] <= 56.5:
											pixels.append((12, 14))
											if features[14][9] <= 252.5:
												pixels.append((14, 9))
												return 8 # approximately 9 were 8 out of 9 samples at leaf node
											else:
												if features[15][19] <= 191.5:
													pixels.append((15, 19))
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													return 4 # approximately 1 were 4 out of 1 samples at leaf node
										else:
											if features[10][11] <= 252.5:
												pixels.append((10, 11))
												if features[21][13] <= 21.0:
													pixels.append((21, 13))
													if features[18][17] <= 41.5:
														pixels.append((18, 17))
														if features[10][11] <= 3.5:
															pixels.append((10, 11))
															return 3 # approximately 1 were 3 out of 1 samples at leaf node
														else:
															return 8 # approximately 2 were 8 out of 2 samples at leaf node
													else:
														return 9 # approximately 6 were 9 out of 6 samples at leaf node
												else:
													if features[10][17] <= 100.5:
														pixels.append((10, 17))
														if features[13][17] <= 242.5:
															pixels.append((13, 17))
															return 5 # approximately 3 were 5 out of 3 samples at leaf node
														else:
															if features[11][20] <= 88.5:
																pixels.append((11, 20))
																return 8 # approximately 1 were 8 out of 1 samples at leaf node
															else:
																return 4 # approximately 1 were 4 out of 1 samples at leaf node
													else:
														if features[16][10] <= 157.5:
															pixels.append((16, 10))
															return 3 # approximately 20 were 3 out of 20 samples at leaf node
														else:
															if features[5][13] <= 115.5:
																pixels.append((5, 13))
																return 4 # approximately 1 were 4 out of 1 samples at leaf node
															else:
																return 8 # approximately 2 were 8 out of 2 samples at leaf node
											else:
												return 5 # approximately 5 were 5 out of 5 samples at leaf node
								else:
									if features[14][7] <= 81.5:
										pixels.append((14, 7))
										if features[10][11] <= 246.5:
											pixels.append((10, 11))
											if features[24][16] <= 252.5:
												pixels.append((24, 16))
												if features[11][8] <= 253.5:
													pixels.append((11, 8))
													if features[6][23] <= 155.0:
														pixels.append((6, 23))
														if features[10][10] <= 203.0:
															pixels.append((10, 10))
															return 3 # approximately 118 were 3 out of 118 samples at leaf node
														else:
															if features[12][10] <= 190.0:
																pixels.append((12, 10))
																if features[18][14] <= 120.5:
																	pixels.append((18, 14))
																	return 3 # approximately 27 were 3 out of 27 samples at leaf node
																else:
																	return 1 # approximately 1 were 1 out of 1 samples at leaf node
															else:
																return 9 # approximately 6 were 9 out of 6 samples at leaf node
													else:
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													if features[7][13] <= 205.0:
														pixels.append((7, 13))
														return 1 # approximately 1 were 1 out of 1 samples at leaf node
													else:
														return 9 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												if features[21][8] <= 193.0:
													pixels.append((21, 8))
													return 5 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													return 8 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											if features[9][14] <= 25.0:
												pixels.append((9, 14))
												if features[16][17] <= 238.5:
													pixels.append((16, 17))
													if features[17][8] <= 5.5:
														pixels.append((17, 8))
														return 3 # approximately 3 were 3 out of 3 samples at leaf node
													else:
														if features[20][16] <= 252.5:
															pixels.append((20, 16))
															return 8 # approximately 2 were 8 out of 2 samples at leaf node
														else:
															if features[15][9] <= 112.5:
																pixels.append((15, 9))
																return 9 # approximately 1 were 9 out of 1 samples at leaf node
															else:
																return 5 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													if features[6][22] <= 27.5:
														pixels.append((6, 22))
														return 9 # approximately 11 were 9 out of 11 samples at leaf node
													else:
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												if features[6][21] <= 18.0:
													pixels.append((6, 21))
													if features[10][23] <= 19.0:
														pixels.append((10, 23))
														if features[20][11] <= 253.5:
															pixels.append((20, 11))
															return 3 # approximately 24 were 3 out of 24 samples at leaf node
														else:
															return 5 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														return 5 # approximately 2 were 5 out of 2 samples at leaf node
												else:
													if features[14][8] <= 5.0:
														pixels.append((14, 8))
														return 5 # approximately 7 were 5 out of 7 samples at leaf node
													else:
														return 3 # approximately 2 were 3 out of 2 samples at leaf node
									else:
										if features[10][21] <= 225.5:
											pixels.append((10, 21))
											if features[8][15] <= 140.5:
												pixels.append((8, 15))
												if features[23][9] <= 162.5:
													pixels.append((23, 9))
													return 8 # approximately 4 were 8 out of 4 samples at leaf node
												else:
													return 3 # approximately 3 were 3 out of 3 samples at leaf node
											else:
												if features[11][11] <= 95.0:
													pixels.append((11, 11))
													return 9 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													return 5 # approximately 6 were 5 out of 6 samples at leaf node
										else:
											if features[16][12] <= 6.5:
												pixels.append((16, 12))
												return 0 # approximately 7 were 0 out of 7 samples at leaf node
											else:
												return 9 # approximately 1 were 9 out of 1 samples at leaf node
							else:
								if features[15][7] <= 226.0:
									pixels.append((15, 7))
									if features[16][10] <= 12.0:
										pixels.append((16, 10))
										if features[11][9] <= 186.5:
											pixels.append((11, 9))
											return 3 # approximately 4 were 3 out of 4 samples at leaf node
										else:
											if features[11][12] <= 154.5:
												pixels.append((11, 12))
												return 9 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												return 5 # approximately 2 were 5 out of 2 samples at leaf node
									else:
										if features[13][15] <= 61.5:
											pixels.append((13, 15))
											if features[9][13] <= 252.5:
												pixels.append((9, 13))
												if features[23][9] <= 32.0:
													pixels.append((23, 9))
													return 2 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													if features[18][11] <= 84.5:
														pixels.append((18, 11))
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														return 8 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												return 0 # approximately 2 were 0 out of 2 samples at leaf node
										else:
											if features[12][11] <= 3.0:
												pixels.append((12, 11))
												if features[10][11] <= 129.5:
													pixels.append((10, 11))
													if features[21][6] <= 6.5:
														pixels.append((21, 6))
														return 2 # approximately 4 were 2 out of 4 samples at leaf node
													else:
														if features[4][13] <= 23.0:
															pixels.append((4, 13))
															return 3 # approximately 2 were 3 out of 2 samples at leaf node
														else:
															return 8 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													return 8 # approximately 11 were 8 out of 11 samples at leaf node
											else:
												if features[24][8] <= 252.5:
													pixels.append((24, 8))
													if features[10][10] <= 21.5:
														pixels.append((10, 10))
														if features[11][12] <= 133.5:
															pixels.append((11, 12))
															return 8 # approximately 2 were 8 out of 2 samples at leaf node
														else:
															return 6 # approximately 1 were 6 out of 1 samples at leaf node
													else:
														if features[18][11] <= 178.5:
															pixels.append((18, 11))
															return 8 # approximately 109 were 8 out of 109 samples at leaf node
														else:
															if features[18][21] <= 243.0:
																pixels.append((18, 21))
																return 8 # approximately 2 were 8 out of 2 samples at leaf node
															else:
																return 3 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													return 0 # approximately 1 were 0 out of 1 samples at leaf node
								else:
									if features[9][16] <= 81.5:
										pixels.append((9, 16))
										if features[13][10] <= 222.5:
											pixels.append((13, 10))
											return 9 # approximately 1 were 9 out of 1 samples at leaf node
										else:
											if features[19][10] <= 127.5:
												pixels.append((19, 10))
												if features[11][22] <= 80.5:
													pixels.append((11, 22))
													return 4 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												return 6 # approximately 1 were 6 out of 1 samples at leaf node
									else:
										return 0 # approximately 6 were 0 out of 6 samples at leaf node
			else:
				if features[13][12] <= 0.5:
					pixels.append((13, 12))
					if features[5][10] <= 56.0:
						pixels.append((5, 10))
						if features[11][13] <= 169.0:
							pixels.append((11, 13))
							if features[13][9] <= 2.0:
								pixels.append((13, 9))
								if features[11][14] <= 38.0:
									pixels.append((11, 14))
									if features[19][10] <= 3.0:
										pixels.append((19, 10))
										if features[14][14] <= 239.0:
											pixels.append((14, 14))
											if features[12][7] <= 234.5:
												pixels.append((12, 7))
												if features[6][18] <= 5.0:
													pixels.append((6, 18))
													if features[13][20] <= 126.5:
														pixels.append((13, 20))
														return 7 # approximately 2 were 7 out of 2 samples at leaf node
													else:
														return 4 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													if features[9][19] <= 248.0:
														pixels.append((9, 19))
														return 2 # approximately 11 were 2 out of 11 samples at leaf node
													else:
														if features[19][17] <= 56.0:
															pixels.append((19, 17))
															return 8 # approximately 1 were 8 out of 1 samples at leaf node
														else:
															return 3 # approximately 2 were 3 out of 2 samples at leaf node
											else:
												return 9 # approximately 5 were 9 out of 5 samples at leaf node
										else:
											if features[22][14] <= 32.5:
												pixels.append((22, 14))
												if features[21][13] <= 144.0:
													pixels.append((21, 13))
													return 8 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													return 7 # approximately 1 were 7 out of 1 samples at leaf node
											else:
												return 3 # approximately 20 were 3 out of 20 samples at leaf node
									else:
										if features[12][11] <= 9.5:
											pixels.append((12, 11))
											if features[17][19] <= 22.0:
												pixels.append((17, 19))
												if features[12][20] <= 253.5:
													pixels.append((12, 20))
													return 2 # approximately 78 were 2 out of 78 samples at leaf node
												else:
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												if features[20][12] <= 34.0:
													pixels.append((20, 12))
													if features[21][10] <= 14.5:
														pixels.append((21, 10))
														if features[14][17] <= 239.5:
															pixels.append((14, 17))
															return 9 # approximately 1 were 9 out of 1 samples at leaf node
														else:
															return 7 # approximately 2 were 7 out of 2 samples at leaf node
													else:
														return 3 # approximately 4 were 3 out of 4 samples at leaf node
												else:
													return 2 # approximately 11 were 2 out of 11 samples at leaf node
										else:
											if features[19][19] <= 225.0:
												pixels.append((19, 19))
												return 8 # approximately 5 were 8 out of 5 samples at leaf node
											else:
												return 6 # approximately 1 were 6 out of 1 samples at leaf node
								else:
									if features[8][16] <= 93.0:
										pixels.append((8, 16))
										if features[17][11] <= 49.5:
											pixels.append((17, 11))
											if features[13][13] <= 65.0:
												pixels.append((13, 13))
												return 3 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												return 1 # approximately 1 were 1 out of 1 samples at leaf node
										else:
											return 8 # approximately 22 were 8 out of 22 samples at leaf node
									else:
										if features[6][12] <= 30.5:
											pixels.append((6, 12))
											if features[15][17] <= 162.5:
												pixels.append((15, 17))
												return 1 # approximately 31 were 1 out of 31 samples at leaf node
											else:
												if features[11][16] <= 22.5:
													pixels.append((11, 16))
													return 2 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													if features[14][15] <= 201.5:
														pixels.append((14, 15))
														return 4 # approximately 1 were 4 out of 1 samples at leaf node
													else:
														return 8 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											if features[12][18] <= 2.0:
												pixels.append((12, 18))
												return 7 # approximately 4 were 7 out of 4 samples at leaf node
											else:
												if features[22][19] <= 53.0:
													pixels.append((22, 19))
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													return 2 # approximately 2 were 2 out of 2 samples at leaf node
							else:
								if features[16][9] <= 31.0:
									pixels.append((16, 9))
									if features[15][11] <= 22.5:
										pixels.append((15, 11))
										if features[16][12] <= 76.0:
											pixels.append((16, 12))
											if features[7][12] <= 226.5:
												pixels.append((7, 12))
												if features[16][15] <= 251.0:
													pixels.append((16, 15))
													return 7 # approximately 2 were 7 out of 2 samples at leaf node
												else:
													if features[6][18] <= 36.0:
														pixels.append((6, 18))
														return 6 # approximately 1 were 6 out of 1 samples at leaf node
													else:
														return 1 # approximately 1 were 1 out of 1 samples at leaf node
											else:
												return 2 # approximately 4 were 2 out of 4 samples at leaf node
										else:
											if features[16][17] <= 231.5:
												pixels.append((16, 17))
												if features[15][8] <= 19.0:
													pixels.append((15, 8))
													return 3 # approximately 3 were 3 out of 3 samples at leaf node
												else:
													if features[7][13] <= 252.5:
														pixels.append((7, 13))
														return 8 # approximately 1 were 8 out of 1 samples at leaf node
													else:
														return 0 # approximately 1 were 0 out of 1 samples at leaf node
											else:
												return 9 # approximately 2 were 9 out of 2 samples at leaf node
									else:
										if features[14][6] <= 158.0:
											pixels.append((14, 6))
											if features[18][12] <= 52.5:
												pixels.append((18, 12))
												if features[18][10] <= 239.5:
													pixels.append((18, 10))
													if features[18][12] <= 24.0:
														pixels.append((18, 12))
														if features[15][9] <= 40.0:
															pixels.append((15, 9))
															return 5 # approximately 1 were 5 out of 1 samples at leaf node
														else:
															if features[21][19] <= 3.0:
																pixels.append((21, 19))
																return 9 # approximately 1 were 9 out of 1 samples at leaf node
															else:
																return 3 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														return 4 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													return 8 # approximately 4 were 8 out of 4 samples at leaf node
											else:
												return 8 # approximately 57 were 8 out of 57 samples at leaf node
										else:
											if features[11][8] <= 211.0:
												pixels.append((11, 8))
												return 4 # approximately 2 were 4 out of 2 samples at leaf node
											else:
												return 0 # approximately 1 were 0 out of 1 samples at leaf node
								else:
									if features[6][17] <= 51.0:
										pixels.append((6, 17))
										if features[8][16] <= 251.0:
											pixels.append((8, 16))
											return 4 # approximately 27 were 4 out of 27 samples at leaf node
										else:
											return 9 # approximately 1 were 9 out of 1 samples at leaf node
									else:
										if features[12][18] <= 65.5:
											pixels.append((12, 18))
											if features[4][17] <= 4.0:
												pixels.append((4, 17))
												if features[7][12] <= 73.5:
													pixels.append((7, 12))
													return 4 # approximately 6 were 4 out of 6 samples at leaf node
												else:
													if features[24][11] <= 150.0:
														pixels.append((24, 11))
														return 5 # approximately 8 were 5 out of 8 samples at leaf node
													else:
														if features[10][12] <= 227.5:
															pixels.append((10, 12))
															return 8 # approximately 5 were 8 out of 5 samples at leaf node
														else:
															if features[11][8] <= 128.5:
																pixels.append((11, 8))
																return 2 # approximately 1 were 2 out of 1 samples at leaf node
															else:
																return 5 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												if features[12][20] <= 59.0:
													pixels.append((12, 20))
													return 6 # approximately 12 were 6 out of 12 samples at leaf node
												else:
													if features[10][23] <= 125.0:
														pixels.append((10, 23))
														if features[19][15] <= 254.5:
															pixels.append((19, 15))
															return 4 # approximately 1 were 4 out of 1 samples at leaf node
														else:
															return 9 # approximately 1 were 9 out of 1 samples at leaf node
													else:
														return 0 # approximately 1 were 0 out of 1 samples at leaf node
										else:
											if features[15][17] <= 251.5:
												pixels.append((15, 17))
												if features[16][8] <= 107.5:
													pixels.append((16, 8))
													if features[13][11] <= 129.0:
														pixels.append((13, 11))
														return 8 # approximately 15 were 8 out of 15 samples at leaf node
													else:
														if features[23][16] <= 31.0:
															pixels.append((23, 16))
															return 9 # approximately 1 were 9 out of 1 samples at leaf node
														else:
															return 5 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													if features[24][12] <= 35.0:
														pixels.append((24, 12))
														if features[16][12] <= 104.5:
															pixels.append((16, 12))
															return 0 # approximately 2 were 0 out of 2 samples at leaf node
														else:
															if features[18][3] <= 87.0:
																pixels.append((18, 3))
																return 6 # approximately 2 were 6 out of 2 samples at leaf node
															else:
																return 4 # approximately 1 were 4 out of 1 samples at leaf node
													else:
														return 9 # approximately 5 were 9 out of 5 samples at leaf node
											else:
												if features[23][17] <= 247.5:
													pixels.append((23, 17))
													if features[7][8] <= 21.5:
														pixels.append((7, 8))
														if features[5][18] <= 254.5:
															pixels.append((5, 18))
															return 9 # approximately 32 were 9 out of 32 samples at leaf node
														else:
															return 0 # approximately 1 were 0 out of 1 samples at leaf node
													else:
														return 4 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													return 8 # approximately 2 were 8 out of 2 samples at leaf node
						else:
							if features[16][13] <= 2.5:
								pixels.append((16, 13))
								if features[6][17] <= 252.5:
									pixels.append((6, 17))
									return 5 # approximately 2 were 5 out of 2 samples at leaf node
								else:
									return 0 # approximately 3 were 0 out of 3 samples at leaf node
							else:
								if features[9][15] <= 247.5:
									pixels.append((9, 15))
									return 8 # approximately 75 were 8 out of 75 samples at leaf node
								else:
									if features[21][11] <= 176.0:
										pixels.append((21, 11))
										if features[23][14] <= 73.5:
											pixels.append((23, 14))
											return 8 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											return 3 # approximately 1 were 3 out of 1 samples at leaf node
									else:
										return 2 # approximately 2 were 2 out of 2 samples at leaf node
					else:
						if features[11][13] <= 155.0:
							pixels.append((11, 13))
							if features[13][9] <= 31.5:
								pixels.append((13, 9))
								if features[19][10] <= 2.0:
									pixels.append((19, 10))
									if features[24][10] <= 0.5:
										pixels.append((24, 10))
										if features[14][8] <= 20.0:
											pixels.append((14, 8))
											if features[23][13] <= 247.5:
												pixels.append((23, 13))
												if features[7][14] <= 253.5:
													pixels.append((7, 14))
													return 2 # approximately 27 were 2 out of 27 samples at leaf node
												else:
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												if features[16][12] <= 182.0:
													pixels.append((16, 12))
													return 2 # approximately 5 were 2 out of 5 samples at leaf node
												else:
													if features[21][18] <= 15.0:
														pixels.append((21, 18))
														if features[7][11] <= 113.5:
															pixels.append((7, 11))
															return 7 # approximately 1 were 7 out of 1 samples at leaf node
														else:
															return 5 # approximately 1 were 5 out of 1 samples at leaf node
													else:
														return 3 # approximately 4 were 3 out of 4 samples at leaf node
										else:
											return 9 # approximately 2 were 9 out of 2 samples at leaf node
									else:
										if features[5][8] <= 159.5:
											pixels.append((5, 8))
											return 3 # approximately 13 were 3 out of 13 samples at leaf node
										else:
											if features[6][8] <= 252.5:
												pixels.append((6, 8))
												return 2 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												return 7 # approximately 1 were 7 out of 1 samples at leaf node
								else:
									if features[14][7] <= 220.0:
										pixels.append((14, 7))
										if features[10][15] <= 254.0:
											pixels.append((10, 15))
											if features[11][13] <= 152.0:
												pixels.append((11, 13))
												if features[15][18] <= 254.5:
													pixels.append((15, 18))
													if features[24][6] <= 67.5:
														pixels.append((24, 6))
														return 2 # approximately 212 were 2 out of 212 samples at leaf node
													else:
														return 7 # approximately 1 were 7 out of 1 samples at leaf node
												else:
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												return 5 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											if features[20][8] <= 127.5:
												pixels.append((20, 8))
												return 7 # approximately 1 were 7 out of 1 samples at leaf node
											else:
												return 8 # approximately 1 were 8 out of 1 samples at leaf node
									else:
										if features[12][20] <= 159.0:
											pixels.append((12, 20))
											return 0 # approximately 1 were 0 out of 1 samples at leaf node
										else:
											return 6 # approximately 1 were 6 out of 1 samples at leaf node
							else:
								if features[19][18] <= 172.0:
									pixels.append((19, 18))
									if features[4][22] <= 127.0:
										pixels.append((4, 22))
										return 8 # approximately 10 were 8 out of 10 samples at leaf node
									else:
										return 5 # approximately 1 were 5 out of 1 samples at leaf node
								else:
									if features[18][9] <= 30.0:
										pixels.append((18, 9))
										if features[12][18] <= 36.5:
											pixels.append((12, 18))
											return 5 # approximately 2 were 5 out of 2 samples at leaf node
										else:
											if features[6][17] <= 108.5:
												pixels.append((6, 17))
												return 3 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												return 2 # approximately 1 were 2 out of 1 samples at leaf node
									else:
										return 0 # approximately 3 were 0 out of 3 samples at leaf node
						else:
							if features[16][13] <= 27.0:
								pixels.append((16, 13))
								if features[16][11] <= 53.5:
									pixels.append((16, 11))
									return 3 # approximately 1 were 3 out of 1 samples at leaf node
								else:
									return 0 # approximately 1 were 0 out of 1 samples at leaf node
							else:
								return 8 # approximately 17 were 8 out of 17 samples at leaf node
				else:
					if features[10][15] <= 248.5:
						pixels.append((10, 15))
						if features[15][14] <= 15.5:
							pixels.append((15, 14))
							if features[13][15] <= 14.5:
								pixels.append((13, 15))
								if features[21][11] <= 135.5:
									pixels.append((21, 11))
									if features[19][12] <= 126.5:
										pixels.append((19, 12))
										return 4 # approximately 6 were 4 out of 6 samples at leaf node
									else:
										if features[18][18] <= 9.0:
											pixels.append((18, 18))
											return 8 # approximately 3 were 8 out of 3 samples at leaf node
										else:
											if features[15][15] <= 77.0:
												pixels.append((15, 15))
												return 0 # approximately 1 were 0 out of 1 samples at leaf node
											else:
												return 6 # approximately 2 were 6 out of 2 samples at leaf node
								else:
									if features[17][10] <= 54.5:
										pixels.append((17, 10))
										if features[21][17] <= 221.5:
											pixels.append((21, 17))
											return 2 # approximately 1 were 2 out of 1 samples at leaf node
										else:
											return 8 # approximately 1 were 8 out of 1 samples at leaf node
									else:
										if features[5][20] <= 236.0:
											pixels.append((5, 20))
											return 0 # approximately 52 were 0 out of 52 samples at leaf node
										else:
											return 6 # approximately 1 were 6 out of 1 samples at leaf node
							else:
								if features[12][11] <= 129.5:
									pixels.append((12, 11))
									if features[14][17] <= 252.5:
										pixels.append((14, 17))
										return 8 # approximately 20 were 8 out of 20 samples at leaf node
									else:
										if features[15][14] <= 1.5:
											pixels.append((15, 14))
											return 5 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											return 3 # approximately 1 were 3 out of 1 samples at leaf node
								else:
									if features[16][10] <= 190.5:
										pixels.append((16, 10))
										if features[14][14] <= 152.0:
											pixels.append((14, 14))
											if features[10][18] <= 49.0:
												pixels.append((10, 18))
												if features[13][13] <= 21.5:
													pixels.append((13, 13))
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													return 5 # approximately 18 were 5 out of 18 samples at leaf node
											else:
												if features[4][22] <= 95.0:
													pixels.append((4, 22))
													return 3 # approximately 7 were 3 out of 7 samples at leaf node
												else:
													return 4 # approximately 1 were 4 out of 1 samples at leaf node
										else:
											return 8 # approximately 7 were 8 out of 7 samples at leaf node
									else:
										if features[23][10] <= 0.5:
											pixels.append((23, 10))
											if features[22][17] <= 11.5:
												pixels.append((22, 17))
												return 4 # approximately 1 were 4 out of 1 samples at leaf node
											else:
												return 6 # approximately 11 were 6 out of 11 samples at leaf node
										else:
											if features[22][15] <= 253.5:
												pixels.append((22, 15))
												return 0 # approximately 4 were 0 out of 4 samples at leaf node
											else:
												if features[20][16] <= 240.5:
													pixels.append((20, 16))
													return 8 # approximately 1 were 8 out of 1 samples at leaf node
												else:
													return 5 # approximately 1 were 5 out of 1 samples at leaf node
						else:
							if features[18][11] <= 0.5:
								pixels.append((18, 11))
								if features[11][11] <= 32.5:
									pixels.append((11, 11))
									if features[12][9] <= 4.5:
										pixels.append((12, 9))
										if features[18][7] <= 95.0:
											pixels.append((18, 7))
											if features[6][15] <= 63.0:
												pixels.append((6, 15))
												return 8 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												return 3 # approximately 60 were 3 out of 60 samples at leaf node
										else:
											if features[7][11] <= 91.5:
												pixels.append((7, 11))
												return 8 # approximately 5 were 8 out of 5 samples at leaf node
											else:
												if features[5][14] <= 226.5:
													pixels.append((5, 14))
													return 3 # approximately 3 were 3 out of 3 samples at leaf node
												else:
													return 2 # approximately 3 were 2 out of 3 samples at leaf node
									else:
										if features[20][15] <= 110.0:
											pixels.append((20, 15))
											if features[12][12] <= 229.5:
												pixels.append((12, 12))
												if features[23][14] <= 95.0:
													pixels.append((23, 14))
													return 4 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													return 8 # approximately 18 were 8 out of 18 samples at leaf node
											else:
												return 3 # approximately 2 were 3 out of 2 samples at leaf node
										else:
											if features[17][23] <= 113.5:
												pixels.append((17, 23))
												if features[15][18] <= 137.5:
													pixels.append((15, 18))
													return 3 # approximately 2 were 3 out of 2 samples at leaf node
												else:
													if features[18][15] <= 154.0:
														pixels.append((18, 15))
														return 9 # approximately 1 were 9 out of 1 samples at leaf node
													else:
														if features[8][8] <= 164.0:
															pixels.append((8, 8))
															return 4 # approximately 1 were 4 out of 1 samples at leaf node
														else:
															return 2 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												return 5 # approximately 2 were 5 out of 2 samples at leaf node
								else:
									if features[14][10] <= 241.5:
										pixels.append((14, 10))
										if features[15][17] <= 253.5:
											pixels.append((15, 17))
											if features[16][19] <= 245.0:
												pixels.append((16, 19))
												return 8 # approximately 63 were 8 out of 63 samples at leaf node
											else:
												if features[21][12] <= 106.5:
													pixels.append((21, 12))
													if features[7][13] <= 195.0:
														pixels.append((7, 13))
														return 3 # approximately 2 were 3 out of 2 samples at leaf node
													else:
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
												else:
													return 8 # approximately 2 were 8 out of 2 samples at leaf node
										else:
											if features[12][12] <= 197.5:
												pixels.append((12, 12))
												return 5 # approximately 3 were 5 out of 3 samples at leaf node
											else:
												if features[16][17] <= 251.5:
													pixels.append((16, 17))
													return 4 # approximately 2 were 4 out of 2 samples at leaf node
												else:
													if features[22][9] <= 126.0:
														pixels.append((22, 9))
														if features[15][11] <= 127.0:
															pixels.append((15, 11))
															return 8 # approximately 1 were 8 out of 1 samples at leaf node
														else:
															return 9 # approximately 1 were 9 out of 1 samples at leaf node
													else:
														return 2 # approximately 1 were 2 out of 1 samples at leaf node
									else:
										if features[11][19] <= 3.0:
											pixels.append((11, 19))
											if features[23][12] <= 26.5:
												pixels.append((23, 12))
												if features[11][10] <= 28.0:
													pixels.append((11, 10))
													return 4 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													if features[16][22] <= 127.0:
														pixels.append((16, 22))
														if features[18][13] <= 107.5:
															pixels.append((18, 13))
															return 9 # approximately 1 were 9 out of 1 samples at leaf node
														else:
															return 8 # approximately 1 were 8 out of 1 samples at leaf node
													else:
														return 3 # approximately 1 were 3 out of 1 samples at leaf node
											else:
												return 5 # approximately 14 were 5 out of 14 samples at leaf node
										else:
											if features[6][18] <= 88.5:
												pixels.append((6, 18))
												if features[8][17] <= 153.0:
													pixels.append((8, 17))
													return 4 # approximately 11 were 4 out of 11 samples at leaf node
												else:
													return 9 # approximately 2 were 9 out of 2 samples at leaf node
											else:
												if features[13][7] <= 84.0:
													pixels.append((13, 7))
													if features[12][21] <= 242.5:
														pixels.append((12, 21))
														return 8 # approximately 12 were 8 out of 12 samples at leaf node
													else:
														return 3 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													if features[6][18] <= 205.0:
														pixels.append((6, 18))
														return 3 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														return 9 # approximately 2 were 9 out of 2 samples at leaf node
							else:
								if features[15][10] <= 182.5:
									pixels.append((15, 10))
									if features[16][7] <= 150.0:
										pixels.append((16, 7))
										if features[5][9] <= 178.0:
											pixels.append((5, 9))
											if features[14][4] <= 59.5:
												pixels.append((14, 4))
												if features[18][25] <= 27.0:
													pixels.append((18, 25))
													if features[21][23] <= 236.0:
														pixels.append((21, 23))
														if features[15][7] <= 131.5:
															pixels.append((15, 7))
															if features[11][3] <= 227.0:
																pixels.append((11, 3))
																if features[12][12] <= 6.5:
																	pixels.append((12, 12))
																	if features[13][10] <= 18.5:
																		pixels.append((13, 10))
																		if features[11][14] <= 29.5:
																			pixels.append((11, 14))
																			if features[4][13] <= 3.5:
																				pixels.append((4, 13))
																				return 3 # approximately 6 were 3 out of 6 samples at leaf node
																			else:
																				return 2 # approximately 4 were 2 out of 4 samples at leaf node
																		else:
																			return 8 # approximately 11 were 8 out of 11 samples at leaf node
																	else:
																		if features[8][12] <= 254.5:
																			pixels.append((8, 12))
																			return 8 # approximately 100 were 8 out of 100 samples at leaf node
																		else:
																			return 5 # approximately 1 were 5 out of 1 samples at leaf node
																else:
																	if features[20][4] <= 96.5:
																		pixels.append((20, 4))
																		if features[4][11] <= 218.0:
																			pixels.append((4, 11))
																			if features[4][18] <= 254.5:
																				pixels.append((4, 18))
																				if features[9][15] <= 253.5:
																					pixels.append((9, 15))
																					if features[17][12] <= 38.5:
																						pixels.append((17, 12))
																						if features[20][13] <= 227.0:
																							pixels.append((20, 13))
																							if features[22][14] <= 254.5:
																								pixels.append((22, 14))
																								return 8 # approximately 25 were 8 out of 25 samples at leaf node
																							else:
																								return 6 # approximately 1 were 6 out of 1 samples at leaf node
																						else:
																							return 4 # approximately 1 were 4 out of 1 samples at leaf node
																					else:
																						if features[17][19] <= 253.5:
																							pixels.append((17, 19))
																							if features[8][16] <= 253.5:
																								pixels.append((8, 16))
																								return 8 # approximately 946 were 8 out of 946 samples at leaf node
																							else:
																								if features[4][15] <= 216.0:
																									pixels.append((4, 15))
																									return 8 # approximately 16 were 8 out of 16 samples at leaf node
																								else:
																									return 2 # approximately 1 were 2 out of 1 samples at leaf node
																						else:
																							if features[13][13] <= 109.5:
																								pixels.append((13, 13))
																								return 5 # approximately 1 were 5 out of 1 samples at leaf node
																							else:
																								return 8 # approximately 17 were 8 out of 17 samples at leaf node
																				else:
																					if features[23][11] <= 43.5:
																						pixels.append((23, 11))
																						return 6 # approximately 1 were 6 out of 1 samples at leaf node
																					else:
																						return 8 # approximately 6 were 8 out of 6 samples at leaf node
																			else:
																				if features[23][12] <= 128.5:
																					pixels.append((23, 12))
																					return 6 # approximately 2 were 6 out of 2 samples at leaf node
																				else:
																					return 8 # approximately 10 were 8 out of 10 samples at leaf node
																		else:
																			if features[6][13] <= 102.0:
																				pixels.append((6, 13))
																				return 5 # approximately 1 were 5 out of 1 samples at leaf node
																			else:
																				return 8 # approximately 2 were 8 out of 2 samples at leaf node
																	else:
																		if features[11][15] <= 38.0:
																			pixels.append((11, 15))
																			return 8 # approximately 1 were 8 out of 1 samples at leaf node
																		else:
																			return 3 # approximately 1 were 3 out of 1 samples at leaf node
															else:
																return 3 # approximately 1 were 3 out of 1 samples at leaf node
														else:
															return 3 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														return 2 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													return 2 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												return 0 # approximately 1 were 0 out of 1 samples at leaf node
										else:
											if features[12][11] <= 9.5:
												pixels.append((12, 11))
												if features[19][8] <= 163.5:
													pixels.append((19, 8))
													if features[16][15] <= 54.0:
														pixels.append((16, 15))
														return 8 # approximately 1 were 8 out of 1 samples at leaf node
													else:
														return 3 # approximately 4 were 3 out of 4 samples at leaf node
												else:
													return 2 # approximately 6 were 2 out of 6 samples at leaf node
											else:
												if features[4][14] <= 245.0:
													pixels.append((4, 14))
													return 8 # approximately 13 were 8 out of 13 samples at leaf node
												else:
													return 5 # approximately 2 were 5 out of 2 samples at leaf node
									else:
										if features[15][15] <= 202.0:
											pixels.append((15, 15))
											if features[7][16] <= 161.5:
												pixels.append((7, 16))
												return 0 # approximately 1 were 0 out of 1 samples at leaf node
											else:
												if features[10][12] <= 169.0:
													pixels.append((10, 12))
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													if features[10][11] <= 232.0:
														pixels.append((10, 11))
														return 9 # approximately 1 were 9 out of 1 samples at leaf node
													else:
														return 5 # approximately 1 were 5 out of 1 samples at leaf node
										else:
											return 4 # approximately 3 were 4 out of 3 samples at leaf node
								else:
									if features[19][9] <= 56.5:
										pixels.append((19, 9))
										if features[17][12] <= 239.0:
											pixels.append((17, 12))
											if features[17][14] <= 187.0:
												pixels.append((17, 14))
												if features[12][16] <= 231.5:
													pixels.append((12, 16))
													if features[19][11] <= 239.0:
														pixels.append((19, 11))
														if features[10][19] <= 150.0:
															pixels.append((10, 19))
															return 5 # approximately 7 were 5 out of 7 samples at leaf node
														else:
															if features[10][10] <= 83.5:
																pixels.append((10, 10))
																if features[17][15] <= 68.0:
																	pixels.append((17, 15))
																	return 3 # approximately 1 were 3 out of 1 samples at leaf node
																else:
																	return 2 # approximately 2 were 2 out of 2 samples at leaf node
															else:
																return 8 # approximately 2 were 8 out of 2 samples at leaf node
													else:
														return 6 # approximately 6 were 6 out of 6 samples at leaf node
												else:
													return 3 # approximately 7 were 3 out of 7 samples at leaf node
											else:
												if features[9][13] <= 177.5:
													pixels.append((9, 13))
													if features[16][19] <= 43.0:
														pixels.append((16, 19))
														return 9 # approximately 1 were 9 out of 1 samples at leaf node
													else:
														if features[13][17] <= 203.0:
															pixels.append((13, 17))
															return 6 # approximately 1 were 6 out of 1 samples at leaf node
														else:
															return 7 # approximately 1 were 7 out of 1 samples at leaf node
												else:
													return 4 # approximately 8 were 4 out of 8 samples at leaf node
										else:
											if features[10][13] <= 235.5:
												pixels.append((10, 13))
												if features[19][11] <= 1.5:
													pixels.append((19, 11))
													if features[18][17] <= 60.0:
														pixels.append((18, 17))
														return 9 # approximately 2 were 9 out of 2 samples at leaf node
													else:
														return 3 # approximately 2 were 3 out of 2 samples at leaf node
												else:
													if features[13][12] <= 12.0:
														pixels.append((13, 12))
														return 3 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														if features[5][6] <= 3.5:
															pixels.append((5, 6))
															if features[4][19] <= 218.0:
																pixels.append((4, 19))
																return 8 # approximately 25 were 8 out of 25 samples at leaf node
															else:
																return 5 # approximately 1 were 5 out of 1 samples at leaf node
														else:
															return 6 # approximately 1 were 6 out of 1 samples at leaf node
											else:
												if features[12][21] <= 217.5:
													pixels.append((12, 21))
													return 4 # approximately 6 were 4 out of 6 samples at leaf node
												else:
													return 8 # approximately 2 were 8 out of 2 samples at leaf node
									else:
										if features[5][7] <= 50.5:
											pixels.append((5, 7))
											if features[6][13] <= 6.5:
												pixels.append((6, 13))
												if features[10][17] <= 126.0:
													pixels.append((10, 17))
													return 6 # approximately 3 were 6 out of 3 samples at leaf node
												else:
													if features[19][16] <= 137.5:
														pixels.append((19, 16))
														return 0 # approximately 1 were 0 out of 1 samples at leaf node
													else:
														return 9 # approximately 1 were 9 out of 1 samples at leaf node
											else:
												if features[23][12] <= 34.5:
													pixels.append((23, 12))
													if features[15][19] <= 251.0:
														pixels.append((15, 19))
														return 8 # approximately 6 were 8 out of 6 samples at leaf node
													else:
														if features[7][9] <= 70.0:
															pixels.append((7, 9))
															return 6 # approximately 3 were 6 out of 3 samples at leaf node
														else:
															if features[21][19] <= 115.0:
																pixels.append((21, 19))
																return 2 # approximately 1 were 2 out of 1 samples at leaf node
															else:
																return 5 # approximately 3 were 5 out of 3 samples at leaf node
												else:
													if features[17][5] <= 17.5:
														pixels.append((17, 5))
														if features[15][15] <= 9.0:
															pixels.append((15, 15))
															if features[8][19] <= 152.5:
																pixels.append((8, 19))
																if features[20][16] <= 231.5:
																	pixels.append((20, 16))
																	return 0 # approximately 1 were 0 out of 1 samples at leaf node
																else:
																	return 8 # approximately 1 were 8 out of 1 samples at leaf node
															else:
																return 2 # approximately 2 were 2 out of 2 samples at leaf node
														else:
															if features[14][12] <= 52.0:
																pixels.append((14, 12))
																return 6 # approximately 1 were 6 out of 1 samples at leaf node
															else:
																if features[21][19] <= 254.5:
																	pixels.append((21, 19))
																	if features[21][9] <= 23.5:
																		pixels.append((21, 9))
																		if features[24][13] <= 151.5:
																			pixels.append((24, 13))
																			return 8 # approximately 11 were 8 out of 11 samples at leaf node
																		else:
																			if features[18][13] <= 10.0:
																				pixels.append((18, 13))
																				return 3 # approximately 2 were 3 out of 2 samples at leaf node
																			else:
																				return 5 # approximately 2 were 5 out of 2 samples at leaf node
																	else:
																		if features[4][9] <= 68.0:
																			pixels.append((4, 9))
																			return 8 # approximately 168 were 8 out of 168 samples at leaf node
																		else:
																			if features[5][17] <= 151.5:
																				pixels.append((5, 17))
																				return 2 # approximately 1 were 2 out of 1 samples at leaf node
																			else:
																				return 8 # approximately 1 were 8 out of 1 samples at leaf node
																else:
																	return 3 # approximately 1 were 3 out of 1 samples at leaf node
													else:
														if features[24][14] <= 2.5:
															pixels.append((24, 14))
															return 2 # approximately 3 were 2 out of 3 samples at leaf node
														else:
															return 8 # approximately 2 were 8 out of 2 samples at leaf node
										else:
											if features[18][10] <= 56.0:
												pixels.append((18, 10))
												return 5 # approximately 1 were 5 out of 1 samples at leaf node
											else:
												return 2 # approximately 5 were 2 out of 5 samples at leaf node
					else:
						if features[16][18] <= 9.5:
							pixels.append((16, 18))
							if features[19][13] <= 126.0:
								pixels.append((19, 13))
								if features[21][18] <= 248.0:
									pixels.append((21, 18))
									if features[10][15] <= 251.0:
										pixels.append((10, 15))
										return 3 # approximately 1 were 3 out of 1 samples at leaf node
									else:
										if features[15][13] <= 7.5:
											pixels.append((15, 13))
											return 0 # approximately 1 were 0 out of 1 samples at leaf node
										else:
											return 8 # approximately 17 were 8 out of 17 samples at leaf node
								else:
									if features[21][6] <= 26.0:
										pixels.append((21, 6))
										return 3 # approximately 2 were 3 out of 2 samples at leaf node
									else:
										return 2 # approximately 2 were 2 out of 2 samples at leaf node
							else:
								if features[20][19] <= 46.0:
									pixels.append((20, 19))
									if features[10][9] <= 56.5:
										pixels.append((10, 9))
										if features[10][14] <= 71.5:
											pixels.append((10, 14))
											if features[6][17] <= 109.0:
												pixels.append((6, 17))
												return 2 # approximately 1 were 2 out of 1 samples at leaf node
											else:
												return 7 # approximately 1 were 7 out of 1 samples at leaf node
										else:
											return 1 # approximately 101 were 1 out of 101 samples at leaf node
									else:
										return 8 # approximately 2 were 8 out of 2 samples at leaf node
								else:
									if features[17][12] <= 126.0:
										pixels.append((17, 12))
										return 8 # approximately 1 were 8 out of 1 samples at leaf node
									else:
										return 2 # approximately 8 were 2 out of 8 samples at leaf node
						else:
							if features[18][11] <= 58.0:
								pixels.append((18, 11))
								if features[6][10] <= 102.5:
									pixels.append((6, 10))
									if features[15][9] <= 252.0:
										pixels.append((15, 9))
										if features[14][18] <= 250.0:
											pixels.append((14, 18))
											if features[10][13] <= 237.5:
												pixels.append((10, 13))
												return 8 # approximately 7 were 8 out of 7 samples at leaf node
											else:
												if features[14][14] <= 126.5:
													pixels.append((14, 14))
													return 0 # approximately 1 were 0 out of 1 samples at leaf node
												else:
													return 1 # approximately 1 were 1 out of 1 samples at leaf node
										else:
											return 3 # approximately 3 were 3 out of 3 samples at leaf node
									else:
										return 4 # approximately 5 were 4 out of 5 samples at leaf node
								else:
									if features[11][9] <= 215.5:
										pixels.append((11, 9))
										if features[15][11] <= 46.5:
											pixels.append((15, 11))
											return 1 # approximately 1 were 1 out of 1 samples at leaf node
										else:
											return 3 # approximately 25 were 3 out of 25 samples at leaf node
									else:
										return 8 # approximately 2 were 8 out of 2 samples at leaf node
							else:
								if features[14][19] <= 148.5:
									pixels.append((14, 19))
									if features[18][14] <= 182.5:
										pixels.append((18, 14))
										if features[21][14] <= 253.5:
											pixels.append((21, 14))
											if features[7][4] <= 55.0:
												pixels.append((7, 4))
												if features[11][16] <= 2.0:
													pixels.append((11, 16))
													return 3 # approximately 1 were 3 out of 1 samples at leaf node
												else:
													return 8 # approximately 58 were 8 out of 58 samples at leaf node
											else:
												return 3 # approximately 1 were 3 out of 1 samples at leaf node
										else:
											if features[22][10] <= 123.0:
												pixels.append((22, 10))
												return 0 # approximately 1 were 0 out of 1 samples at leaf node
											else:
												return 3 # approximately 1 were 3 out of 1 samples at leaf node
									else:
										if features[10][20] <= 81.0:
											pixels.append((10, 20))
											if features[8][10] <= 252.5:
												pixels.append((8, 10))
												if features[17][17] <= 253.5:
													pixels.append((17, 17))
													if features[8][14] <= 251.5:
														pixels.append((8, 14))
														return 1 # approximately 2 were 1 out of 2 samples at leaf node
													else:
														if features[13][15] <= 236.5:
															pixels.append((13, 15))
															return 0 # approximately 1 were 0 out of 1 samples at leaf node
														else:
															if features[24][12] <= 126.0:
																pixels.append((24, 12))
																if features[21][13] <= 227.0:
																	pixels.append((21, 13))
																	return 4 # approximately 1 were 4 out of 1 samples at leaf node
																else:
																	return 8 # approximately 1 were 8 out of 1 samples at leaf node
															else:
																return 7 # approximately 1 were 7 out of 1 samples at leaf node
												else:
													return 6 # approximately 2 were 6 out of 2 samples at leaf node
											else:
												return 2 # approximately 3 were 2 out of 3 samples at leaf node
										else:
											return 8 # approximately 5 were 8 out of 5 samples at leaf node
								else:
									if features[14][15] <= 199.0:
										pixels.append((14, 15))
										if features[14][10] <= 199.5:
											pixels.append((14, 10))
											if features[19][15] <= 252.5:
												pixels.append((19, 15))
												return 3 # approximately 4 were 3 out of 4 samples at leaf node
											else:
												if features[12][14] <= 145.0:
													pixels.append((12, 14))
													return 2 # approximately 1 were 2 out of 1 samples at leaf node
												else:
													return 0 # approximately 1 were 0 out of 1 samples at leaf node
										else:
											if features[21][14] <= 33.5:
												pixels.append((21, 14))
												return 8 # approximately 1 were 8 out of 1 samples at leaf node
											else:
												return 0 # approximately 14 were 0 out of 14 samples at leaf node
									else:
										if features[10][11] <= 236.5:
											pixels.append((10, 11))
											if features[14][18] <= 253.5:
												pixels.append((14, 18))
												return 3 # approximately 8 were 3 out of 8 samples at leaf node
											else:
												if features[23][13] <= 77.5:
													pixels.append((23, 13))
													return 4 # approximately 1 were 4 out of 1 samples at leaf node
												else:
													return 8 # approximately 1 were 8 out of 1 samples at leaf node
										else:
											if features[19][9] <= 125.5:
												pixels.append((19, 9))
												if features[10][18] <= 49.0:
													pixels.append((10, 18))
													return 9 # approximately 1 were 9 out of 1 samples at leaf node
												else:
													return 4 # approximately 1 were 4 out of 1 samples at leaf node
											else:
												return 8 # approximately 5 were 8 out of 5 samples at leaf node
	return pixels
np.savetxt("path", pixels # save path to file
