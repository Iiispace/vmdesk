from mathutils import Vector
from math import degrees, radians

INT_min = -2147483648
INT_max = 2147483647
FLOAT_min = -3.402823e+38
FLOAT_max = 3.402823e+38
FLOAT_rad = degrees(1.0)
FLOAT_deg = radians(1.0)

TUP_111 = (1, 1, 1)
TUP_XYZ = ('X', 'Y', 'Z')
TUP_RGBA = ('R', 'G', 'B', 'A')
TUP_HSV = ('H', 'S', 'V')
TUP_HEX = ('#',)

FLO_000 = (0.0, 0.0, 0.0)
FLO_0000 = (0.0, 0.0, 0.0, 0.0)

RANGE_2 = range(2)
RANGE_3 = range(3)
RANGE_4 = range(4)

VEC_001 = Vector((0, 0, 1))
VEC_00M1 = Vector((0, 0, -1))
VEC_010 = Vector((0, 1, 0))
VEC_111 = Vector((1, 1, 1))
VEC_111U = VEC_111.normalized()
ROT_00M1_111U = VEC_00M1.rotation_difference(VEC_111U)
ROT_00M1_111U_inv = ROT_00M1_111U.inverted()

STR_AZ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
STR_az = 'abcdefghijklmnopqrstuvwxyz'
STR_AZaz = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
STR_A_Z = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_'
STR_a_z = 'abcdefghijklmnopqrstuvwxyz_'
STR_AZ_az = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_'
STR_09 = '0123456789'
STR_09dot = '0123456789.'
STR_AZ_az_09 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_0123456789'
STR_AZ_az_09dot = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_0123456789.'
STR_break_sign = ' !"#$%&\'()*+,-./:;<=>?@[\\]^`{|}~'

D_unit_replace = {
    'μm': 'um',
    'μm2': 'um2',
    'μm²': 'um2',
    'μm3': 'um3',
    'μm³': 'um3',
    'μs': 'us',
    '°': 'd',
    '°C': 'c',
    '°c': 'c',
    '°F': 'f',
    '°f': 'f',
    'celsius': 'c',
    'fahrenheit': 'f'}
D_length_unit_to_display = {
    "KILOMETERS": "km",
    "METERS": "m",
    "CENTIMETERS": "cm",
    "MILLIMETERS": "mm",
    "MICROMETERS": "µm",
    "MILES": "mi",
    "FEET": "'",
    "INCHES": "\"",
    "THOU": "thou"}
# D_length_unit_to_display_inv = {e: k  for k, e in D_length_unit_to_display.items()}
D_mass_unit_to_display = {
    'TONNES': 'ton',
    'KILOGRAMS': 'kg',
    'GRAMS': 'g',
    'MILLIGRAMS': 'mg',
    'CENTUM_WEIGHTS': 'cwt',
    'STONES': 'st',
    'POUNDS': 'lb',
    'OUNCES': 'oz'}
D_time_unit_to_display = {
    'DAYS': 'd',
    'HOURS': 'hr',
    'MINUTES': 'min',
    'SECONDS': 'sec',
    'MILLISECONDS': 'ms',
    'MICROSECONDS': 'μs'}
D_temperature_unit_to_display = {
    'KELVIN': 'K',
    'CELSIUS': '°C',
    'FAHRENHEIT': '°F'}
D_length_name_to_value = {
    'km': 'KILOMETERS',
    'kilometer': 'KILOMETERS',
    'kilometers': 'KILOMETERS',
    'm': 'METERS',
    'meter': 'METERS',
    'meters': 'METERS',
    'cm': 'CENTIMETERS',
    'centimeter': 'CENTIMETERS',
    'centimeters': 'CENTIMETERS',
    'mm': 'MILLIMETERS',
    'millimeter': 'MILLIMETERS',
    'millimeters': 'MILLIMETERS',
    'um': 'MICROMETERS',
    'μm': 'MICROMETERS',
    'micrometer': 'MICROMETERS',
    'micrometers': 'MICROMETERS',
    'mi': 'MILES',
    'mile': 'MILES',
    'miles': 'MILES',
    'ft': 'FEET',
    'feet': 'FEET',
    'foot': 'FEET',
    'in': 'INCHES',
    'inche': 'INCHES',
    'inches': 'INCHES',
    'mil': 'THOU',
    'thou': 'THOU'}
D_length_name_to_value_inv = {
    'KILOMETERS': 'km',
    'METERS': 'm',
    'CENTIMETERS': 'cm',
    'MILLIMETERS': 'mm',
    'MICROMETERS': 'μm',
    'MILES': 'mi',
    'FEET': 'ft',
    'INCHES': 'in',
    'THOU': 'mil'}
S_all_area_unit = {
    'km2', 'km²',
    'kilometer2', 'kilometer²',
    'kilometers2', 'kilometers²',
    'm2', 'm²',
    'meter2', 'meter²',
    'meters2', 'meters²',
    'cm2', 'cm²',
    'centimeter2', 'centimeter²',
    'centimeters2', 'centimeters²',
    'mm2', 'mm²',
    'millimeter2', 'millimeter²',
    'millimeters2', 'millimeters²',
    'um2', 'um²',
    'μm2', 'μm²',
    'micrometer2', 'micrometer²',
    'micrometers2', 'micrometers²',
    'mi2', 'mi²',
    'mile2', 'mile²',
    'miles2', 'miles²',
    'ft2', 'ft²',
    'feet2', 'feet²',
    'foot2', 'foot²',
    'in2', 'in²',
    'inche2', 'inche²',
    'inches2', 'inches²',
    'mil2', 'mil²',
    'thou2', 'thou²'}
S_all_volume_unit = {
    'km3', 'km³',
    'kilometer3', 'kilometer³',
    'kilometers3', 'kilometers³',
    'm3', 'm³',
    'meter3', 'meter³',
    'meters3', 'meters³',
    'cm3', 'cm³',
    'centimeter3', 'centimeter³',
    'centimeters3', 'centimeters³',
    'mm3', 'mm³',
    'millimeter3', 'millimeter³',
    'millimeters3', 'millimeters³',
    'um3', 'um³',
    'μm3', 'μm³',
    'micrometer3', 'micrometer³',
    'micrometers3', 'micrometers³',
    'mi3', 'mi³',
    'mile3', 'mile³',
    'miles3', 'miles³',
    'ft3', 'ft³',
    'feet3', 'feet³',
    'foot3', 'foot³',
    'in3', 'in³',
    'inche3', 'inche³',
    'inches3', 'inches³',
    'mil3', 'mil³',
    'thou3', 'thou³'}
S_all_mass_unit = {
    'ton', 'tonnes',
    'kg', 'kilograms', 'kilogram',
    'g', 'grams', 'gram',
    'mg', 'milligrams', 'milligram',
    'cwt',
    'st', 'stones', 'stone'
    'lb', 'pounds', 'pound',
    'oz', 'ounces', 'ounce'}
S_all_time_unit = {
    'd', 'day', 'days',
    'hr', 'h', 'hour', 'hours',
    'min', 'm', 'minute', 'minutes',
    'sec', 's', 'second', 'seconds',
    'ms', 'millisecond', 'milliseconds',
    'μs', 'us', 'microsecond', 'microseconds'}
S_all_temperature_unit = {
    'k', 'kelvin',
    '°c', 'c', 'celsius',
    '°f', 'f', 'fahrenheit'}

D_img_format = {
    'BMP': 'bmp',
    'IRIS': 'rgb',
    'PNG': 'png',
    'JPEG': 'jpg',
    'JPEG2000': 'jp2',
    'TARGA': 'tga',
    'TARGA_RAW': 'tga',
    'CINEON': 'cin',
    'DPX': 'dpx',
    'OPEN_EXR_MULTILAYER': 'exr',
    'OPEN_EXR': 'exr',
    'HDR': 'hdr',
    'TIFF': 'tif',
    'WEBP': 'webp',
    'AVI_JPEG': 'avi',
    'AVI_RAW': 'avi',
    'FFMPEG': 'mkv',
}

D_bake_map_type_inv = {
    "combined": "COMB",
    "diffuse": "COL",
    "glossy": "GLOSS",
    "roughness": "ROUGHNESS",
    "transmission": "TRANSMISSION",
    "normal": "NRM",
    "displacement": "DISP",
    "emit": "EMIT",
    "ao": "AO",
    "shadow": "SHADOW",
    "position": "POS",
    "uv": "UV",
    "environment": "ENVIRONMENT",
}
