NUMBERS = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26']
LETTERS = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

EQUIPMENT_DICT = {
                  'MACHINES' : ['WEHRMACHT','KRIEGSMARINE_M3','KRIEGSMARINE_M4','LUFTWAFFE','SWISS_K'],
                  'ENTRY_WHEELS' : {
                                    'WEHRMACHT' : ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
                                    'KRIEGSMARINE_M3' : ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
                                    'KRIEGSMARINE_M4' : ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
                                    'LUFTWAFFE' : ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
                                    'SWISS_K' : ['Q','W','E','R','T','Z','U','I','O','A','S','D','F','G','H','J','K','P','Y','X','C','V','B','N','M','L']
                                  },
                  'ROTORS' : {
                              'WEHRMACHT' : ['Rotor 1','Rotor 2','Rotor 3','Rotor 4','Rotor 5'],
                              'KRIEGSMARINE_M3' : ['Rotor 1','Rotor 2','Rotor 3','Rotor 4','Rotor 5','Rotor 6','Rotor 7','Rotor 8'],
                              'KRIEGSMARINE_M4' : ['Rotor 1','Rotor 2','Rotor 3','Rotor 4','Rotor 5','Rotor 6','Rotor 7','Rotor 8','Rotor B','Rotor C'],
                              'LUFTWAFFE' : ['Rotor 1','Rotor 2','Rotor 3','Rotor 4','Rotor 5','Rotor 6','Rotor 7','Rotor 8','Rotor B','Rotor C'],
                              'SWISS_K' : ['Rotor I','Rotor II','Rotor III']
                            },
                  'RING_CHARACTERS' : {
                  						'WEHRMACHT' : ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26'],
                  						'KRIEGSMARINE_M3' : ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
                  						'KRIEGSMARINE_M4' : ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
                  						'LUFTWAFFE' : ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
                  						'SWISS_K' : ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
                  					  },
                  'REFLECTORS' : {
                                  'WEHRMACHT' : ['Reflector B','Reflector C'],
                                  'KRIEGSMARINE_M3' : ['Reflector B','Reflector C'],
                                  'KRIEGSMARINE_M4' : ['Reflector thin B','Reflector thin C'],
                                  'LUFTWAFFE' : ['Reflector thin B','Reflector thin C'],
                                  'SWISS_K' : ['Reflector swiss K']
                                }
                  }

# ROTORS
                        
ROTOR_DICT = {
              'Rotor 1':[['E','K','M','F','L','G','D','Q','V','Z','N','T','O','W','Y','H','X','U','S','P','A','I','B','R','C','J'],['Q']],
              'Rotor 2':[['A','J','D','K','S','I','R','U','X','B','L','H','W','T','M','C','Q','G','Z','N','P','Y','F','V','O','E'],['E']],
              'Rotor 3':[['B','D','F','H','J','L','C','P','R','T','X','V','Z','N','Y','E','I','W','G','A','K','M','U','S','Q','O'],['V']],
              'Rotor 4':[['E','S','O','V','P','Z','J','A','Y','Q','U','I','R','H','X','L','N','F','T','G','K','D','C','M','W','B'],['J']],
              'Rotor 5':[['V','Z','B','R','G','I','T','Y','U','P','S','D','N','H','L','X','A','W','M','J','Q','O','F','E','C','K'],['Z']],
              'Rotor 6':[['J','P','G','V','O','U','M','F','Y','Q','B','E','N','H','Z','R','D','K','A','S','X','L','I','C','T','W'],['M','Z']],
              'Rotor 7':[['N','Z','J','H','G','R','C','X','M','Y','S','W','B','O','U','F','A','I','V','L','P','E','K','Q','D','T'],['M','Z']],
              'Rotor 8':[['F','K','Q','H','T','L','X','O','C','B','J','S','P','D','Z','R','A','M','E','W','N','I','U','Y','G','V'],['M','Z']],
              'Rotor B':[['L','E','Y','J','V','C','N','I','X','W','P','B','Q','M','D','R','T','A','K','Z','G','F','U','H','O','S'],[]],
              'Rotor C':[['F','S','O','K','A','N','U','E','R','H','M','B','T','I','Y','C','W','L','Q','P','Z','X','V','G','J','D'],[]],
              'Rotor I':[['P','E','Z','U','O','H','X','S','C','V','F','M','T','B','G','L','R','I','N','Q','J','W','A','Y','D','K'],['Y']],
              'Rotor II':[['Z','O','U','E','S','Y','D','K','F','W','P','C','I','Q','X','H','M','V','B','L','G','N','J','R','A','T'],['E']],
              'Rotor III':[['E','H','R','V','X','G','A','O','B','Q','U','S','I','M','Z','F','L','Y','N','W','K','T','P','D','J','C'],['N']]
              }

# REFLECTORS

REFLECTOR_DICT = {
                  'Reflector B':['Y','R','U','H','Q','S','L','D','P','X','N','G','O','K','M','I','E','B','F','Z','C','W','V','J','A','T'],
                  'Reflector C':['F','V','P','J','I','A','O','Y','E','D','R','Z','X','W','G','C','T','K','U','Q','S','B','N','M','H','L'],
                  'Reflector thin B':['E','N','K','Q','A','U','Y','W','J','I','C','O','P','B','L','M','D','X','Z','V','F','T','H','R','G','S'],
                  'Reflector thin C':['R','D','O','B','J','N','T','K','V','E','H','M','L','F','C','W','Z','A','X','G','Y','I','P','S','U','Q'],
                  'Reflector swiss K':['I','M','E','T','C','F','G','R','A','Y','S','Q','B','Z','X','W','L','H','K','D','V','U','P','O','J','N']
                  }

# ENIGMA MACHINE LAYOUT

ENIGMA_LAYOUT = {
      'FIRST_ROW':['Q','W','E','R','T','Z','U','I','O'],
      'SECOND_ROW':['A','S','D','F','G','H','J','K'],
      'THIRD_ROW':['P','Y','X','C','V','B','N','M','L']
    }

NUMBERS_DICT = {
                '1' : 'Q',
                '2' : 'W',
                '3' : 'E',
                '4' : 'R',
                '5' : 'T',
                '6' : 'Z',
                '7' : 'U',
                '8' : 'I',
                '9' : 'O',
                '0' : 'P'
                }

# UHR BOX

UHR_BOX = {
      'CONNECTIONS_LIST':[6,31,4,29,18,39,16,25,30,23,
                		 28,1,38,11,36,37,26,27,24,21,
                		 14,3,12,17,2,7,0,33,10,35,
                		 8,5,22,19,20,13,34,15,32,9],
                
      'PLUG_A_MAP':{
              0: '01ALG', 2: '01ASM',
              4: '02ALG', 6: '02ASM',
              8: '03ALG', 10: '03ASM',
              12: '04ALG', 14: '04ASM',
              16: '05ALG', 18: '05ASM',
              20: '06ALG', 22: '06ASM',
              24: '07ALG', 26: '07ASM',
              28: '08ALG', 30: '08ASM',
              32: '09ALG', 34: '09ASM',
              36: '10ALG', 38: '10ASM'
              },

      'PLUG_B_MAP':{
              0: '07BLG', 2: '07BSM',
              4: '01BLG', 6: '01BSM',
              8: '08BLG', 10: '08BSM',
              12: '06BLG', 14: '06BSM',
              16: '02BLG', 18: '02BSM',
              20: '09BLG', 22: '09BSM',
              24: '05BLG', 26: '05BSM',
              28: '03BLG', 30: '03BSM',
              32: '10BLG', 34: '10BSM',
              36: '04BLG', 38: '04BSM'
              },

      'PLUGS_LIST':['01A','02A','03A','04A','05A',
      				'06A','07A','08A','09A','10A',
              		'01B','02B','03B','04B','05B',
              		'06B','07B','08B','09B','10B']
    }