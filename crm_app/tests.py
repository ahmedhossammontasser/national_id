from django.test import TestCase
import unittest
from .services import NationalIdService
from datetime import date
# Create your tests here.
class TestNationalIDValidation(unittest.TestCase):
	"""Test National ID Validation classes

	Arguments:
		unittest {Testcase} -- the unit test module
	"""

	def test_validation_national_id(self):
		"""
			Test validation of national_id 
		"""
		self.assertEqual(NationalIdService("29210232101257").is_valid(), True)
		self.assertEqual(NationalIdService("30410232101257").is_valid(), True)
		self.assertEqual(NationalIdService("29210232101a57").is_valid(), False) ## char in national_id
		self.assertEqual(NationalIdService("2921023210127").is_valid(), False) ## len less than 14
		self.assertEqual(NationalIdService("292102321012574").is_valid(), False) ## len more than 14
		self.assertEqual(NationalIdService("49210232101257").is_valid(), False) ## first chat is 4
		self.assertEqual(NationalIdService("19210232101257").is_valid(), False) ## first chat is 1

	def test_function_is_birthday_valid(self):
		"""
			Test function of is_birthday_valid
		"""
		self.assertEqual(NationalIdService.is_birthday_valid(date(1992,3,4)), True)
		self.assertEqual(NationalIdService.is_birthday_valid(date(2004,3,4)), True)
		self.assertEqual(NationalIdService.is_birthday_valid(date(2006,3,4)), False) ## age less than 15


		# def is_governorate_valid(self):
	def test_function_is_governorate_valid(self):
		"""
			Test function of is_governorate_valid 
		"""
		self.assertEqual(NationalIdService("29105190102551").is_governorate_valid(), True)
		self.assertEqual(NationalIdService("30410238881257").is_governorate_valid(), True)
		self.assertEqual(NationalIdService("29105199902551").is_governorate_valid(), False) ## invalid gover code 99
		self.assertEqual(NationalIdService("29105190502551").is_governorate_valid(), False) ## invalid gover code 05


	def test_function_extract_informations(self):
		"""
			Test function of extract_informations which run get_birthday, get_gender, get_govermante_code, 	

		"""
		data = {
			"birthday": date(1991,5,19),
			"govermant_code": "Cairo",
			"gender": "Male",
			"unique_number_per_governorate_day": "0255"
		}
		info_valid, info_dict = NationalIdService("29105190102551").extract_informations_valid()
		self.assertEqual(info_dict, data)
		self.assertEqual(info_valid, True)

		data = {
			"birthday": date(2001, 5, 19),
			"govermant_code": "Alexandria",
			"gender": "Female",
			"unique_number_per_governorate_day": "0252"
		}
		info_valid, info_dict = NationalIdService("30105190202522").extract_informations_valid()
		self.assertEqual(info_dict, data)
		self.assertEqual(info_valid, True)

		data = {}
		info_valid, info_dict = NationalIdService("31005190202522").extract_informations_valid()
		self.assertEqual(info_dict, data)
		self.assertEqual(info_valid, False)
