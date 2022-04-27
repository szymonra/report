import csv
import os


for dirpath, dirnames, filenames in os.walk('.'):
	for name in filenames:
		if name == "summary-per-cohort.csv":
			print(dirpath)
			filename = os.path.join(dirpath, name)
			print(filename)
			inputfile = csv.reader(open(filename), delimiter=',')
			baselineTimes = []
			experimentTimes = []
			for row in inputfile:
				if (row[0] == 'baseline' and row[1] == 'response time average'):
					baselineTimes = row
				if (row[0] == 'experiment' and row[1] == 'response time average'):
					experimentTimes = row
			timesDifference = []
			timesPercentage = []
			timesDifference.append('comparison')
			timesDifference.append('times difference')
			timesPercentage.append('comparison')
			timesPercentage.append('times percentage')
			i = 2
			print(baselineTimes)
			print(experimentTimes)
			while i < len(baselineTimes):
				print(experimentTimes[i])
				if(experimentTimes[i]!='' and baselineTimes[i]!=''):
					timeDiff = int(experimentTimes[i])-int(baselineTimes[i])
					timesDifference.append(timeDiff)
					timesPercentage.append(str(round(timeDiff/int(baselineTimes[i])*100,2))+'%')
				else:
					timesDifference.append('')
					timesPercentage.append('')
				i+=1
			for column in timesDifference:
				print(column)
			for column in timesPercentage:
				print(column)
			f = open(os.path.join(dirpath, 'summary-per-cohort-extended.csv'), 'w')
			writer = csv.writer(f)
			i=0
			inputfile = csv.reader(open(filename), delimiter=',')
			for row in inputfile:
				if(i==3):
					writer.writerow(timesDifference)
					writer.writerow(timesPercentage)
				writer.writerow(row)
				i+=1
			f.close()