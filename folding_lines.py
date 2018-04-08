###
# This is an example of folding frequency ranges for finding recombination lines
###
import pyfits

CHS361 = range(0, 50, 1)
chs361 = map(str, CHS361)
CHS360 = range(0, 45, 1)
chs360 = map(str, CHS360)
CHS359 = range(0, 35, 1)
chs359 = map(str, CHS359)
CHS355 = range(30, 60, 1)
chs355 = map(str, CHS355)
CHS354 = range(35, 70, 1)
chs354 = map(str, CHS354)
CHS353 = range(35, 70, 1)
chs353 = map(str, CHS353)
CHS352 = range(35, 70, 1)
chs352 = map(str, CHS352)
CHS351 = range(35, 70, 1)
chs351 = map(str, CHS351)
CHS350 = range(35, 70, 1)
chs350 = map(str, CHS350)
CHS349 = range(35, 70, 1)
chs349 = map(str, CHS349)
CHS345 = range(0, 35, 1)
chs345 = map(str, CHS345)

CUBE = range(1, 4, 1)
cube = map(str, CUBE)

for i in range(len(cube)):
  ch349 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/349/131048_349_'+chs349[i]+'_30obs.fits')
  ch349.writeto('131048_cube_30obs_'+cube[i]+'.fits')

CUBE = range(4, 5, 1)
cube = map(str, CUBE)

for i in range(len(cube)):
  ch354 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/354/131048_354_'+chs354[i]+'_29obs.fits')
  ch350 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/350/131048_350_'+chs350[i]+'_29obs.fits')
  ch349 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/349/131048_349_'+chs349[i+3]+'_30obs.fits')
  ch354data = ch354[0].data
  ch350data = ch350[0].data
  ch349data = ch349[0].data
  ch354data2 = ch354data[0,0]
  ch350data2 = ch350data[0,0]
  ch349data2 = ch349data[0,0]
  fold = ch354data2 + ch350data2 + ch349data2
  fold
  ch354data3 = ch354[0].data
  ch354data3[0,0] = fold
  ch3542 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/354/131048_354_'+chs354[i]+'_29obs.fits')
  ch3542[0].data = ch354data3
  ch3542.writeto('131048_cube_30obs_'+cube[i]+'.fits')

CUBE = range(5, 6, 1)
cube = map(str, CUBE)

for i in range(len(cube)):
  ch355 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/355/131048_355_'+chs355[i]+'_30obs.fits')
  ch354 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/354/131048_354_'+chs354[i+1]+'_29obs.fits')
  ch350 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/350/131048_350_'+chs350[i+1]+'_29obs.fits')
  ch349 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/349/131048_349_'+chs349[i+4]+'_30obs.fits')
  ch355data = ch355[0].data
  ch354data = ch354[0].data
  ch350data = ch350[0].data
  ch349data = ch349[0].data
  ch355data2 = ch355data[0,0]
  ch354data2 = ch354data[0,0]
  ch350data2 = ch350data[0,0]
  ch349data2 = ch349data[0,0]
  fold = ch355data2 + ch354data2 + ch350data2 + ch349data2
  fold
  ch354data3 = ch354[0].data
  ch354data3[0,0] = fold
  ch3542 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/354/131048_354_'+chs354[i+1]+'_29obs.fits')
  ch3542[0].data = ch354data3
  ch3542.writeto('131048_cube_30obs_'+cube[i]+'.fits')

CUBE = range(6, 7, 1)
cube = map(str, CUBE)

for i in range(len(cube)):
  ch361 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/361_30obs/131048_361_'+chs361[i]+'_30obs.fits')
  ch355 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/355/131048_355_'+chs355[i+1]+'_30obs.fits')
  ch354 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/354/131048_354_'+chs354[i+2]+'_29obs.fits')
  ch353 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/353/131048_353_'+chs353[i]+'_30obs.fits')
  ch351 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/351/131048_351_'+chs351[i]+'_30obs.fits')
  ch350 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/350/131048_350_'+chs350[i+2]+'_29obs.fits')
  ch349 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/349/131048_349_'+chs349[i+5]+'_30obs.fits')

  ch361data = ch361[0].data
  ch355data = ch355[0].data
  ch354data = ch354[0].data
  ch353data = ch353[0].data
  ch351data = ch351[0].data
  ch350data = ch350[0].data
  ch349data = ch349[0].data

  ch361data2 = ch361data[0,0]
  ch355data2 = ch355data[0,0]
  ch354data2 = ch354data[0,0]
  ch353data2 = ch353data[0,0]
  ch351data2 = ch351data[0,0]
  ch350data2 = ch350data[0,0]
  ch349data2 = ch349data[0,0]

  fold = -(ch361data2) + ch355data2 + ch354data2 + ch353data2 + ch351data2 + ch350data2 + ch349data2
  fold
  ch354data3 = ch354[0].data
  ch354data3[0,0] = fold
  ch3542 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/354/131048_354_'+chs354[i+2]+'_29obs.fits')
  ch3542[0].data = ch354data3
  ch3542.writeto('131048_cube_30obs_'+cube[i]+'.fits')

CUBE = range(7, 12, 1)
cube = map(str, CUBE)

for i in range(len(cube)):
  ch361 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/361_30obs/131048_361_'+chs361[i+1]+'_30obs.fits')
  ch355 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/355/131048_355_'+chs355[i+2]+'_30obs.fits')
  ch354 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/354/131048_354_'+chs354[i+3]+'_29obs.fits')
  ch353 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/353/131048_353_'+chs353[i+1]+'_30obs.fits')
  ch352 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/352/131048_352_'+chs352[i]+'_29obs.fits')
  ch351 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/351/131048_351_'+chs351[i+1]+'_30obs.fits')
  ch350 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/350/131048_350_'+chs350[i+3]+'_29obs.fits')
  ch349 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/349/131048_349_'+chs349[i+6]+'_30obs.fits')

  ch361data = ch361[0].data
  ch355data = ch355[0].data
  ch354data = ch354[0].data
  ch353data = ch353[0].data
  ch352data = ch352[0].data
  ch351data = ch351[0].data
  ch350data = ch350[0].data
  ch349data = ch349[0].data

  ch361data2 = ch361data[0,0]
  ch355data2 = ch355data[0,0]
  ch354data2 = ch354data[0,0]
  ch353data2 = ch353data[0,0]
  ch352data2 = ch352data[0,0]
  ch351data2 = ch351data[0,0]
  ch350data2 = ch350data[0,0]
  ch349data2 = ch349data[0,0]

  fold = -(ch361data2) + ch355data2 + ch354data2 + ch353data2 + ch352data2 + ch351data2 + ch350data2 + ch349data2
  fold
  ch354data3 = ch354[0].data
  ch354data3[0,0] = fold
  ch3542 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/354/131048_354_'+chs354[i+3]+'_29obs.fits')
  ch3542[0].data = ch354data3
  ch3542.writeto('131048_cube_30obs_'+cube[i]+'.fits')

CUBE = range(12,13,1)
cube = map(str, CUBE)

for i in range(len(cube)):
  ch361 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/361_30obs/131048_361_'+chs361[i+6]+'_30obs.fits')
  ch355 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/355/131048_355_'+chs355[i+7]+'_30obs.fits')
  ch354 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/354/131048_354_'+chs354[i+8]+'_29obs.fits')
  ch353 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/353/131048_353_'+chs353[i+6]+'_30obs.fits')
  ch352 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/352/131048_352_'+chs352[i+5]+'_29obs.fits')
  ch351 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/351/131048_351_'+chs351[i+6]+'_30obs.fits')
  ch350 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/350/131048_350_'+chs350[i+8]+'_29obs.fits')
  ch349 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/349/131048_349_'+chs349[i+11]+'_30obs.fits')

  ch361data = ch361[0].data
  ch355data = ch355[0].data
  ch354data = ch354[0].data
  ch353data = ch353[0].data
  ch352data = ch352[0].data
  ch351data = ch351[0].data
  ch350data = ch350[0].data
  ch349data = ch349[0].data


  ch361data2 = ch361data[0,0]
  ch355data2 = ch355data[0,0]
  ch354data2 = ch354data[0,0]
  ch353data2 = ch353data[0,0]
  ch352data2 = ch352data[0,0]
  ch351data2 = ch351data[0,0]
  ch350data2 = ch350data[0,0]
  ch349data2 = ch349data[0,0]


  fold = -(ch361data2) + ch355data2 + ch354data2 + ch353data2 + ch352data2 + ch351data2 + ch350data2 + ch349data2
  fold
  ch354data3 = ch354[0].data
  ch354data3[0,0] = fold
  ch3542 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/354/131048_354_'+chs354[i+8]+'_29obs.fits')
  ch3542[0].data = ch354data3
  ch3542.writeto('131048_cube_30obs_'+cube[i]+'.fits')


CUBE = range(13,17,1)
cube = map(str, CUBE)

for i in range(len(cube)):
  ch361 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/361_30obs/131048_361_'+chs361[i+7]+'_30obs.fits')
  ch360 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/360/131048_360_'+chs360[i]+'_30obs.fits')
  ch355 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/355/131048_355_'+chs355[i+8]+'_30obs.fits')
  ch354 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/354/131048_354_'+chs354[i+9]+'_29obs.fits')
  ch353 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/353/131048_353_'+chs353[i+7]+'_30obs.fits')
  ch352 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/352/131048_352_'+chs352[i+6]+'_29obs.fits')
  ch351 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/351/131048_351_'+chs351[i+7]+'_30obs.fits')
  ch350 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/350/131048_350_'+chs350[i+9]+'_29obs.fits')
  ch349 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/349/131048_349_'+chs349[i+12]+'_30obs.fits')

  ch361data = ch361[0].data
  ch360data = ch360[0].data
  ch355data = ch355[0].data
  ch354data = ch354[0].data
  ch353data = ch353[0].data
  ch352data = ch352[0].data
  ch351data = ch351[0].data
  ch350data = ch350[0].data
  ch349data = ch349[0].data


  ch361data2 = ch361data[0,0]
  ch360data2 = ch360data[0,0]
  ch355data2 = ch355data[0,0]
  ch354data2 = ch354data[0,0]
  ch353data2 = ch353data[0,0]
  ch352data2 = ch352data[0,0]
  ch351data2 = ch351data[0,0]
  ch350data2 = ch350data[0,0]
  ch349data2 = ch349data[0,0]


  fold = -(ch361data2) - ch360data2 + ch355data2 + ch354data2 + ch353data2 + ch352data2 + ch351data2 + ch350data2 + ch349data2
  fold
  ch354data3 = ch354[0].data
  ch354data3[0,0] = fold
  ch3542 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/354/131048_354_'+chs354[i+9]+'_29obs.fits')
  ch3542[0].data = ch354data3
  ch3542.writeto('131048_cube_30obs_'+cube[i]+'.fits')


CUBE = range(17, 35, 1)
cube = map(str, CUBE)

for i in range(len(cube)):
  ch361 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/361_30obs/131048_361_'+chs361[i+11]+'_30obs.fits')
  ch360 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/360/131048_360_'+chs360[i+4]+'_30obs.fits')
  ch359 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/359/131048_359_'+chs359[i]+'_30obs.fits')
  ch355 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/355/131048_355_'+chs355[i+12]+'_30obs.fits')
  ch354 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/354/131048_354_'+chs354[i+13]+'_29obs.fits')
  ch353 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/353/131048_353_'+chs353[i+11]+'_30obs.fits')
  ch352 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/352/131048_352_'+chs352[i+10]+'_29obs.fits')
  ch351 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/351/131048_351_'+chs351[i+11]+'_30obs.fits')
  ch350 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/350/131048_350_'+chs350[i+13]+'_29obs.fits')
  ch349 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/349/131048_349_'+chs349[i+16]+'_30obs.fits')
  ch345 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/345/131048_345_'+chs345[i]+'_30obs.fits')

  ch361data = ch361[0].data
  ch360data = ch360[0].data
  ch359data = ch359[0].data
  ch355data = ch355[0].data
  ch354data = ch354[0].data
  ch353data = ch353[0].data
  ch352data = ch352[0].data
  ch351data = ch351[0].data
  ch350data = ch350[0].data
  ch349data = ch349[0].data
  ch345data = ch345[0].data


  ch361data2 = ch361data[0,0]
  ch360data2 = ch360data[0,0]
  ch359data2 = ch359data[0,0]
  ch355data2 = ch355data[0,0]
  ch354data2 = ch354data[0,0]
  ch353data2 = ch353data[0,0]
  ch352data2 = ch352data[0,0]
  ch351data2 = ch351data[0,0]
  ch350data2 = ch350data[0,0]
  ch349data2 = ch349data[0,0]
  ch345data2 = ch345data[0,0]


  fold = -(ch361data2) - ch360data2 - ch359data2  + ch355data2 + ch354data2 + ch353data2 + ch352data2 + ch351data2 + ch350data2 + ch349data2 - ch345data2
  fold
  ch354data3 = ch354[0].data
  ch354data3[0,0] = fold
  ch3542 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/354/131048_354_'+chs354[i+13]+'_29obs.fits')
  ch3542[0].data = ch354data3
  ch3542.writeto('131048_cube_30obs_'+cube[i]+'.fits')

CUBE = range(35, 36, 1)
cube = map(str, CUBE)

for i in range(len(cube)):
  ch361 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/361_30obs/131048_361_'+chs361[i+29]+'_30obs.fits')
  ch360 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/360/131048_360_'+chs360[i+22]+'_30obs.fits')
  ch359 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/359/131048_359_'+chs359[i+18]+'_30obs.fits')
  ch354 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/354/131048_354_'+chs354[i+31]+'_29obs.fits')
  ch353 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/353/131048_353_'+chs353[i+29]+'_30obs.fits')
  ch352 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/352/131048_352_'+chs352[i+28]+'_29obs.fits')
  ch351 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/351/131048_351_'+chs351[i+29]+'_30obs.fits')
  ch350 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/350/131048_350_'+chs350[i+31]+'_29obs.fits')
  ch349 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/349/131048_349_'+chs349[i+34]+'_30obs.fits')
  ch345 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/345/131048_345_'+chs345[i+18]+'_30obs.fits')

  ch361data = ch361[0].data
  ch360data = ch360[0].data
  ch359data = ch359[0].data
  ch354data = ch354[0].data
  ch353data = ch353[0].data
  ch352data = ch352[0].data
  ch351data = ch351[0].data
  ch350data = ch350[0].data
  ch349data = ch349[0].data
  ch345data = ch345[0].data


  ch361data2 = ch361data[0,0]
  ch360data2 = ch360data[0,0]
  ch359data2 = ch359data[0,0]
  ch354data2 = ch354data[0,0]
  ch353data2 = ch353data[0,0]
  ch352data2 = ch352data[0,0]
  ch351data2 = ch351data[0,0]
  ch350data2 = ch350data[0,0]
  ch349data2 = ch349data[0,0]
  ch345data2 = ch345data[0,0]


  fold = -(ch361data2) - ch360data2 - ch359data2 + ch354data2 + ch353data2 + ch352data2 + ch351data2 + ch350data2 + ch349data2 - ch345data2
  fold
  ch354data3 = ch354[0].data
  ch354data3[0,0] = fold
  ch3542 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/354/131048_354_'+chs354[i+31]+'_29obs.fits')
  ch3542[0].data = ch354data3
  ch3542.writeto('131048_cube_30obs_'+cube[i]+'.fits')

CUBE = range(36, 39, 1)
cube = map(str, CUBE)

for i in range(len(cube)):
  ch361 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/361_30obs/131048_361_'+chs361[i+30]+'_30obs.fits')
  ch360 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/360/131048_360_'+chs360[i+23]+'_30obs.fits')
  ch359 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/359/131048_359_'+chs359[i+19]+'_30obs.fits')
  ch354 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/354/131048_354_'+chs354[i+32]+'_29obs.fits')
  ch353 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/353/131048_353_'+chs353[i+30]+'_30obs.fits')
  ch352 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/352/131048_352_'+chs352[i+29]+'_29obs.fits')
  ch351 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/351/131048_351_'+chs351[i+30]+'_30obs.fits')
  ch350 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/350/131048_350_'+chs350[i+32]+'_29obs.fits')
  ch345 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/345/131048_345_'+chs345[i+19]+'_30obs.fits')

  ch361data = ch361[0].data
  ch360data = ch360[0].data
  ch359data = ch359[0].data
  ch354data = ch354[0].data
  ch353data = ch353[0].data
  ch352data = ch352[0].data
  ch351data = ch351[0].data
  ch350data = ch350[0].data
  ch345data = ch345[0].data


  ch361data2 = ch361data[0,0]
  ch360data2 = ch360data[0,0]
  ch359data2 = ch359data[0,0]
  ch354data2 = ch354data[0,0]
  ch353data2 = ch353data[0,0]
  ch352data2 = ch352data[0,0]
  ch351data2 = ch351data[0,0]
  ch350data2 = ch350data[0,0]
  ch345data2 = ch345data[0,0]


  fold = -(ch361data2) - ch360data2 - ch359data2 + ch354data2 + ch353data2 + ch352data2 + ch351data2 + ch350data2 - ch345data2
  fold
  ch354data3 = ch354[0].data
  ch354data3[0,0] = fold
  ch3542 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/354/131048_354_'+chs354[i+32]+'_29obs.fits')
  ch3542[0].data = ch354data3
  ch3542.writeto('131048_cube_30obs_'+cube[i]+'.fits')

CUBE = range(39, 41, 1)
cube = map(str, CUBE)

for i in range(len(cube)):
  ch361 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/361_30obs/131048_361_'+chs361[i+33]+'_30obs.fits')
  ch360 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/360/131048_360_'+chs360[i+26]+'_30obs.fits')
  ch359 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/359/131048_359_'+chs359[i+22]+'_30obs.fits')
  ch353 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/353/131048_353_'+chs353[i+33]+'_30obs.fits')
  ch352 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/352/131048_352_'+chs352[i+32]+'_29obs.fits')
  ch351 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/351/131048_351_'+chs351[i+33]+'_30obs.fits')
  ch345 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/345/131048_345_'+chs345[i+22]+'_30obs.fits')

  ch361data = ch361[0].data
  ch360data = ch360[0].data
  ch359data = ch359[0].data
  ch353data = ch353[0].data
  ch352data = ch352[0].data
  ch351data = ch351[0].data
  ch345data = ch345[0].data


  ch361data2 = ch361data[0,0]
  ch360data2 = ch360data[0,0]
  ch359data2 = ch359data[0,0]
  ch353data2 = ch353data[0,0]
  ch352data2 = ch352data[0,0]
  ch351data2 = ch351data[0,0]
  ch345data2 = ch345data[0,0]


  fold = -(ch361data2) - ch360data2 - ch359data2 + ch353data2 + ch352data2 + ch351data2 - ch345data2
  fold
  ch360data3 = ch360[0].data
  ch360data3[0,0] = fold
  ch3602 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/360/131048_360_'+chs360[i+26]+'_30obs.fits')
  ch3602[0].data = ch360data3
  ch3602.writeto('131048_cube_30obs_'+cube[i]+'.fits')

CUBE = range(41, 42, 1)
cube = map(str, CUBE)

for i in range(len(cube)):
  ch361 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/361_30obs/131048_361_'+chs361[i+35]+'_30obs.fits')
  ch360 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/360/131048_360_'+chs360[i+28]+'_30obs.fits')
  ch359 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/359/131048_359_'+chs359[i+24]+'_30obs.fits')
  ch352 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/352/131048_352_'+chs352[i+34]+'_29obs.fits')
  ch345 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/345/131048_345_'+chs345[i+24]+'_30obs.fits')


  ch361data = ch361[0].data
  ch360data = ch360[0].data
  ch359data = ch359[0].data
  ch352data = ch352[0].data
  ch345data = ch345[0].data


  ch361data2 = ch361data[0,0]
  ch360data2 = ch360data[0,0]
  ch359data2 = ch359data[0,0]
  ch352data2 = ch352data[0,0]
  ch345data2 = ch345data[0,0]


  fold = -(ch361data2) - ch360data2 - ch359data2 + ch352data2 - ch345data2
  fold
  ch360data3 = ch360[0].data
  ch360data3[0,0] = fold
  ch3602 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/360/131048_360_'+chs360[i+28]+'_30obs.fits')
  ch3602[0].data = ch360data3
  ch3602.writeto('131048_cube_30obs_'+cube[i]+'.fits')

CUBE = range(42, 52, 1)
cube = map(str, CUBE)

for i in range(len(cube)):
  ch361 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/361_30obs/131048_361_'+chs361[i+36]+'_30obs.fits')
  ch360 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/360/131048_360_'+chs360[i+29]+'_30obs.fits')
  ch359 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/359/131048_359_'+chs359[i+25]+'_30obs.fits')
  ch345 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/345/131048_345_'+chs345[i+25]+'_30obs.fits')


  ch361data = ch361[0].data
  ch360data = ch360[0].data
  ch359data = ch359[0].data
  ch345data = ch345[0].data


  ch361data2 = ch361data[0,0]
  ch360data2 = ch360data[0,0]
  ch359data2 = ch359data[0,0]
  ch345data2 = ch345data[0,0]


  fold = -(ch361data2) - ch360data2 - ch359data2 - ch345data2
  fold
  ch360data3 = ch360[0].data
  ch360data3[0,0] = fold
  ch3602 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/360/131048_360_'+chs360[i+29]+'_30obs.fits')
  ch3602[0].data = ch360data3
  ch3602.writeto('131048_cube_30obs_'+cube[i]+'.fits')

CUBE = range(52, 56, 1)
cube = map(str, CUBE)

for i in range(len(cube)):
  ch361 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/361_30obs/131048_361_'+chs361[i+46]+'_30obs.fits')
  ch360 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/360/131048_360_'+chs360[i+39]+'_30obs.fits')


  ch361data = ch361[0].data
  ch360data = ch360[0].data


  ch361data2 = ch361data[0,0]
  ch360data2 = ch360data[0,0]


  fold = -(ch361data2) - ch360data2
  fold
  ch360data3 = ch360[0].data
  ch360data3[0,0] = fold
  ch3602 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/360/131048_360_'+chs360[i+39]+'_30obs.fits')
  ch3602[0].data = ch360data3
  ch3602.writeto('131048_cube_30obs_'+cube[i]+'.fits')

CUBE = range(56, 57, 1)
cube = map(str, CUBE)

for i in range(len(cube)):
  ch360 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/360/131048_360_'+chs360[i+43]+'_30obs.fits')

  ch360data = ch360[0].data


  ch360data2 = ch360data[0,0]


  fold = -(ch360data2)
  fold
  ch360data3 = ch360[0].data
  ch360data3[0,0] = fold
  ch3602 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/360/131048_360_'+chs360[i+43]+'_30obs.fits')
  ch3602[0].data = ch360data3
  ch3602.writeto('131048_cube_30obs_'+cube[i]+'.fits')

CUBE = range(57, 58, 1)
cube = map(str, CUBE)

for i in range(len(cube)):
  ch360 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/360/131048_360_'+chs360[i+44]+'_30obs.fits')

  ch360data = ch360[0].data

  ch360data2 = ch360data[0,0]

  fold = -(ch360data2)
  fold
  ch360data3 = ch360[0].data
  ch360data3[0,0] = fold
  ch3602 = pyfits.open('/mnt/ict_test/HighResMWA/Krystal/calibrating/360/131048_360_'+chs360[i+44]+'_30obs.fits')
  ch3602[0].data = ch360data3
  ch3602.writeto('131048_cube_30obs_'+cube[i]+'.fits')
