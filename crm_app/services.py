from datetime import date

class NationalIdService(object):
	def __init__(self, national_id):
		self.national_id = national_id
		self.governorates = {'01': 'Cairo',
					'02': 'Alexandria',
					'03': 'Port Said',
					'04': 'Suez',
					'11': 'Damietta',
					'12': 'Dakahlia',
					'13': 'Ash Sharqia',
					'14': 'Kaliobeya',
					'15': 'Kafr El - Sheikh',
					'16': 'Gharbia',
					'17': 'Monoufia',
					'18': 'El Beheira',
					'19': 'Ismailia',
					'21': 'Giza',
					'22': 'Beni Suef',
					'23': 'Fayoum',
					'24': 'El Menia',
					'25': 'Assiut',
					'26': 'Sohag',
					'27': 'Qena',
					'28': 'Aswan',
					'29': 'Luxor',
					'31': 'Red Sea',
					'32': 'New Valley',
					'33': 'Matrouh',
					'34': 'North Sinai',
					'35': 'South Sinai',
					'88': 'Foreign'}

	def is_valid(self) :
		'''
			check if national id is valid
				must be lenght= 14
				must start wuth 2 or 3 
				must be digit (1-9)  
			:param 
			:return: bool
		'''
		if len(self.national_id) != 14 or  ( self.national_id[0] not in ['2', '3']) or ( not self.national_id.isdigit()):
			return False
		return True

	@staticmethod
	def is_birthday_valid(birthday):
		'''
			check if birthday id is valid
				must bigger than 16 years old
			:param birthday: date
			:return: bool
		'''
		today = date.today()
		if int((today - birthday).days / 365) < 16:
			return False
		return True

	def get_birthday(self):
		'''
			extract and return birthday from first 5 number from national id  
			:param  
			:return: date
		'''
		if self.national_id[0] == "2":
			year = 1900
		else:
			year = 2000
		year += int(self.national_id[1:3])
		return date( year, int(self.national_id[3:5]) , int(self.national_id[5:7]) )

	def get_gender(self):
		'''
			return gender type form national_id char 
			:param 
			:return: str
		'''		
		return "Male" if int(self.national_id[12]) % 2 == 1 else "Female"

	def is_governorate_valid(self):
		'''
			check govermant code in in key in govermant dictory 
			:param 
			:return: bool
		'''
		if not (self.national_id[7:9] in self.governorates):
			return False 
		return True

	def get_govermante_code(self):
		'''
			return govermant text from govermant dictory 
			:param
			:return: str
		'''
		return self.governorates[self.national_id[7:9]]

	def extract_informations_valid(self):
		'''
			Extract information from national EG national ID
			:param national_id: str
					EG national id must be number of 14 digit
			:return:
				info_is_valid: bool
				national_id_info : dict
					birthday: date
					gender: str
					governorate: str
					unique_number_per_governorate_day
			
		'''
		info = {}
		info['birthday'] = self.get_birthday()
		if ( not NationalIdService.is_birthday_valid(info['birthday']) ) or (not self.is_governorate_valid() ):
			return False , {}
		info['govermant_code'] = self.get_govermante_code()
		info['gender'] = self.get_gender()
		info['unique_number_per_governorate_day'] = self.national_id[9:13]
		return True , info
