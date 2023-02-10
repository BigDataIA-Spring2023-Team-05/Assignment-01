from awscloud.s3 import nexrad_main as s3
import pytest

def test_get_all_nexrad_filename_by_filter():
    expected_file = ['KABR20230204_000536_V06', 'KABR20230204_001220_V06', 'KABR20230204_001905_V06', 'KABR20230204_002551_V06', 'KABR20230204_003234_V06', 'KABR20230204_003919_V06', 'KABR20230204_004604_V06', 'KABR20230204_005250_V06', 'KABR20230204_005935_V06', 'KABR20230204_005935_V06_MDM', 'KABR20230204_010619_V06', 'KABR20230204_011304_V06', 'KABR20230204_011954_V06', 'KABR20230204_012640_V06', 'KABR20230204_013325_V06', 'KABR20230204_014011_V06', 'KABR20230204_014656_V06', 'KABR20230204_015341_V06', 'KABR20230204_015341_V06_MDM', 'KABR20230204_020025_V06', 'KABR20230204_020709_V06', 'KABR20230204_021353_V06', 'KABR20230204_022038_V06', 'KABR20230204_022723_V06', 'KABR20230204_023407_V06', 'KABR20230204_024052_V06', 'KABR20230204_024738_V06', 'KABR20230204_025436_V06', 'KABR20230204_025436_V06_MDM', 'KABR20230204_030120_V06', 'KABR20230204_030805_V06', 'KABR20230204_031450_V06', 'KABR20230204_032135_V06', 'KABR20230204_032926_V06', 'KABR20230204_033610_V06', 'KABR20230204_034255_V06', 'KABR20230204_034940_V06', 'KABR20230204_035624_V06', 'KABR20230204_035624_V06_MDM', 'KABR20230204_040310_V06', 'KABR20230204_040954_V06', 'KABR20230204_041639_V06', 'KABR20230204_042324_V06', 'KABR20230204_043020_V06', 'KABR20230204_043705_V06', 'KABR20230204_044403_V06', 'KABR20230204_045101_V06', 'KABR20230204_045758_V06', 'KABR20230204_045758_V06_MDM', 'KABR20230204_050447_V06', 'KABR20230204_051151_V06', 'KABR20230204_051855_V06', 'KABR20230204_052558_V06', 'KABR20230204_053302_V06', 'KABR20230204_054007_V06', 'KABR20230204_054711_V06', 'KABR20230204_055416_V06', 'KABR20230204_055416_V06_MDM', 'KABR20230204_060120_V06', 'KABR20230204_060825_V06', 'KABR20230204_061531_V06', 'KABR20230204_062228_V06', 'KABR20230204_062932_V06', 'KABR20230204_063636_V06', 'KABR20230204_064340_V06', 'KABR20230204_065024_V06', 'KABR20230204_065723_V06', 'KABR20230204_065723_V06_MDM', 'KABR20230204_070428_V06', 'KABR20230204_071127_V06', 'KABR20230204_071825_V06', 'KABR20230204_072528_V06', 'KABR20230204_073232_V06', 'KABR20230204_073931_V06', 'KABR20230204_074635_V06', 'KABR20230204_075338_V06', 'KABR20230204_075338_V06_MDM', 'KABR20230204_080036_V06', 'KABR20230204_080734_V06', 'KABR20230204_081438_V06', 'KABR20230204_082137_V06', 'KABR20230204_082834_V06', 'KABR20230204_083538_V06', 'KABR20230204_084242_V06', 'KABR20230204_084946_V06', 'KABR20230204_085649_V06', 'KABR20230204_085649_V06_MDM', 'KABR20230204_090347_V06', 'KABR20230204_091046_V06', 'KABR20230204_091744_V06', 'KABR20230204_092449_V06', 'KABR20230204_093147_V06', 'KABR20230204_093845_V06', 'KABR20230204_094548_V06', 'KABR20230204_095247_V06', 'KABR20230204_095931_V06', 'KABR20230204_095931_V06_MDM', 'KABR20230204_100617_V06', 'KABR20230204_101306_V06', 'KABR20230204_101954_V06', 'KABR20230204_102643_V06', 'KABR20230204_103332_V06', 'KABR20230204_104021_V06', 'KABR20230204_104706_V06', 'KABR20230204_105404_V06', 'KABR20230204_105404_V06_MDM', 'KABR20230204_110108_V06', 'KABR20230204_110806_V06', 'KABR20230204_111505_V06', 'KABR20230204_112201_V06', 'KABR20230204_113015_V06', 'KABR20230204_113720_V06', 'KABR20230204_114424_V06', 'KABR20230204_115121_V06', 'KABR20230204_115825_V06', 'KABR20230204_115825_V06_MDM', 'KABR20230204_120529_V06', 'KABR20230204_121226_V06', 'KABR20230204_121929_V06', 'KABR20230204_122633_V06', 'KABR20230204_123338_V06', 'KABR20230204_124042_V06', 'KABR20230204_124746_V06', 'KABR20230204_125450_V06', 'KABR20230204_125450_V06_MDM', 'KABR20230204_130154_V06', 'KABR20230204_130859_V06', 'KABR20230204_131603_V06', 'KABR20230204_132300_V06', 'KABR20230204_132958_V06', 'KABR20230204_133703_V06', 'KABR20230204_134408_V06', 'KABR20230204_135112_V06', 'KABR20230204_135809_V06', 'KABR20230204_135809_V06_MDM', 'KABR20230204_140507_V06', 'KABR20230204_141200_V06', 'KABR20230204_141858_V06', 'KABR20230204_142555_V06', 'KABR20230204_143253_V06', 'KABR20230204_143951_V06', 'KABR20230204_144655_V06', 'KABR20230204_145400_V06', 'KABR20230204_145400_V06_MDM', 'KABR20230204_150105_V06', 'KABR20230204_150803_V06', 'KABR20230204_151500_V06', 'KABR20230204_152205_V06', 'KABR20230204_152903_V06', 'KABR20230204_153607_V06', 'KABR20230204_154312_V06', 'KABR20230204_155016_V06', 'KABR20230204_155721_V06', 'KABR20230204_155721_V06_MDM', 'KABR20230204_160419_V06', 'KABR20230204_161118_V06', 'KABR20230204_161821_V06', 'KABR20230204_162525_V06', 'KABR20230204_163229_V06', 'KABR20230204_163927_V06', 'KABR20230204_164616_V06', 'KABR20230204_165315_V06', 'KABR20230204_170009_V06', 'KABR20230204_170009_V06_MDM', 'KABR20230204_170654_V06', 'KABR20230204_171338_V06', 'KABR20230204_172022_V06', 'KABR20230204_172706_V06', 'KABR20230204_173351_V06', 'KABR20230204_174036_V06', 'KABR20230204_174721_V06', 'KABR20230204_175410_V06', 'KABR20230204_175410_V06_MDM', 'KABR20230204_180103_V06', 'KABR20230204_180748_V06', 'KABR20230204_181434_V06', 'KABR20230204_182118_V06', 'KABR20230204_182811_V06', 'KABR20230204_183505_V06', 'KABR20230204_184203_V06', 'KABR20230204_184900_V06', 'KABR20230204_185605_V06', 'KABR20230204_185605_V06_MDM', 'KABR20230204_190309_V06', 'KABR20230204_191006_V06', 'KABR20230204_191710_V06', 'KABR20230204_192355_V06', 'KABR20230204_193154_V06', 'KABR20230204_193838_V06', 'KABR20230204_194522_V06', 'KABR20230204_195206_V06', 'KABR20230204_195850_V06', 'KABR20230204_195850_V06_MDM', 'KABR20230204_200535_V06', 'KABR20230204_201218_V06', 'KABR20230204_201902_V06', 'KABR20230204_202547_V06', 'KABR20230204_203231_V06', 'KABR20230204_203914_V06', 'KABR20230204_204559_V06', 'KABR20230204_205248_V06', 'KABR20230204_205936_V06', 'KABR20230204_205936_V06_MDM', 'KABR20230204_210633_V06', 'KABR20230204_211318_V06', 'KABR20230204_212017_V06', 'KABR20230204_212714_V06', 'KABR20230204_213417_V06', 'KABR20230204_214121_V06', 'KABR20230204_214825_V06', 'KABR20230204_215529_V06', 'KABR20230204_215529_V06_MDM', 'KABR20230204_220233_V06', 'KABR20230204_220936_V06', 'KABR20230204_221640_V06', 'KABR20230204_222344_V06', 'KABR20230204_223049_V06', 'KABR20230204_223753_V06', 'KABR20230204_224458_V06', 'KABR20230204_225203_V06', 'KABR20230204_225908_V06', 'KABR20230204_225908_V06_MDM', 'KABR20230204_230611_V06', 'KABR20230204_231315_V06', 'KABR20230204_232020_V06', 'KABR20230204_232725_V06', 'KABR20230204_233429_V06', 'KABR20230204_234133_V06', 'KABR20230204_234837_V06', 'KABR20230204_235542_V06', 'KABR20230204_235542_V06_MDM']
    assert s3.get_all_nexrad_file_name_by_filter('2023', '02', '04', 'KABR') == expected_file


def test_generate_nexrad_link_by_filename_2022():
    assert s3.get_nexrad_aws_link('2023', '02', '04', 'KABR', 'KABR20230204_000536_V06') == ('https://damg7245-team-5.s3.amazonaws.com/2023/02/04/KABR/KABR20230204_000536_V06', 'https://noaa-nexrad-level2.s3.amazonaws.com/2023/02/04/KABR/KABR20230204_000536_V06')


def test_generating_nexrad_link_creation_by_filename():
    file_to_test = [
        'KBGM20111010_000301_V03.gz',
        'KBGM20110612_003045_V03.gz',
        'KARX20100512_014240_V03.gz',
        'KABX20130902_002911_V06.gz',
        'KBIS20001222_090728.gz',
        'KCCX20120203_013605_V03.gz',
        'KCBW20011213_002358.gz',
        'KBYX20150804_000940_V06.gz',
        'KAPX20120717_013219_V06.gz',
        'KAPX20140907_010223_V06.gz',
        'KCBW20080819_012424_V03.gz',
        'KLWX19931112_005128.gz',
        'KBOX20030717_014732.gz'
        ]
    
    generated_links_expected=[
        'https://noaa-nexrad-level2.s3.amazonaws.com/2011/10/10/KBGM/KBGM20111010_000301_V03.gz',
        'https://noaa-nexrad-level2.s3.amazonaws.com/2011/06/12/KBGM/KBGM20110612_003045_V03.gz',
        'https://noaa-nexrad-level2.s3.amazonaws.com/2010/05/12/KARX/KARX20100512_014240_V03.gz',
        'https://noaa-nexrad-level2.s3.amazonaws.com/2013/09/02/KABX/KABX20130902_002911_V06.gz',
        'https://noaa-nexrad-level2.s3.amazonaws.com/2000/12/22/KBIS/KBIS20001222_090728.gz',
        'https://noaa-nexrad-level2.s3.amazonaws.com/2012/02/03/KCCX/KCCX20120203_013605_V03.gz',
        'https://noaa-nexrad-level2.s3.amazonaws.com/2001/12/13/KCBW/KCBW20011213_002358.gz',
        'https://noaa-nexrad-level2.s3.amazonaws.com/2015/08/04/KBYX/KBYX20150804_000940_V06.gz',
        'https://noaa-nexrad-level2.s3.amazonaws.com/2012/07/17/KAPX/KAPX20120717_013219_V06.gz',
        'https://noaa-nexrad-level2.s3.amazonaws.com/2014/09/07/KAPX/KAPX20140907_010223_V06.gz',
        'https://noaa-nexrad-level2.s3.amazonaws.com/2008/08/19/KCBW/KCBW20080819_012424_V03.gz',
        'https://noaa-nexrad-level2.s3.amazonaws.com/1993/11/12/KLWX/KLWX19931112_005128.gz',
        'https://noaa-nexrad-level2.s3.amazonaws.com/2003/07/17/KBOX/KBOX20030717_014732.gz'
            ]

    generated_links = list()

    for file in file_to_test:
        generated_links.append(s3.get_nexrad_aws_link_by_filename(file))

    assert generated_links == generated_links_expected