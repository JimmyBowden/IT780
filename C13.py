#C13
#Jimmy Bowden

from bayesText import *

#change these to match your directory structure

baseDirectory = "20news/"
trainingDir = baseDirectory + "20news-bydate-train/"
testDir = baseDirectory + "20news-bydate-test/"

print("Stoplist 0 ")
bT = BayesText(trainingDir, baseDirectory + "stopwords.txt")
print("probability of word 'god' appearing in rec.motorcycles:", bT.prob["rec.motorcycles"]["god"])
print("probability of word 'god' appearing in soc.religion.christian:", bT.prob["soc.religion.christian"]["god"])

print("Running Test ...")
bT.test(testDir)
print("\nClassify post@classify1:", bT.classify("20news/classify1.txt"))
print("\nClassify post@classify2:", bT.classify("20news/classify2.txt"))
print("\nClassify post@classify3:", bT.classify("20news/classify3.txt"))
print("\nClassify post@classify4:", bT.classify("20news/classify4.txt"))

print("The new blog tests: ")
print("")
print("\nClassify post@classify5:", bT.classify("20news/classify5.txt"))
print("\nClassify post@classify6:", bT.classify("20news/classify6.txt"))
print("\nClassify post@classify7:", bT.classify("20news/classify7.txt"))
print("\nClassify post@classify8:", bT.classify("20news/classify8.txt"))
