import sys
#import numpy
from CSV2GML.CSV2GMLPlugin import *

def readClusterFile(myfile):
   clusters = []
   filestuff = open(myfile, 'r')
   for line in filestuff:
      vals = line.split(',')
      if (vals[0] == "\"\""):
          clusters.append([])
      else:
          clusters[len(clusters)-1].append(vals[1][1:len(vals[1])-2].strip())
   return clusters

def inSameCluster(bac1, bac2, clusters):
   if (bac1[0] == '\"'):
      bac1 = bac1[1:len(bac1)-1]
      bac2 = bac2[1:len(bac2)-1]
   for i in range(len(clusters)):
      if (clusters[i].count(bac1) > 0):
         if (clusters[i].count(bac2) > 0):
            return True
         else:
            return False


class ClusterizePlugin(CSV2GMLPlugin):
   def input(self, filename):
      CSV2GMLPlugin.input(self,filename+".csv")
      self.clusters = readClusterFile(filename+".clusters.csv")      

   def output(self, filename):
      filestuff = open(filename, 'w')
      filestuff.write('\"\",')
      for i in range(self.n-1):
         filestuff.write(self.bacteria[i]+",")
      filestuff.write(self.bacteria[self.n-1])
      for i in range(self.n):
         if (i == self.n-1): 
            filestuff.write(self.bacteria[i][0:len(self.bacteria[i])-1]+",")
         else:
            filestuff.write(self.bacteria[i]+",")
         for j in range(self.n-1):
            if (inSameCluster(self.bacteria[i], self.bacteria[j], self.clusters)):
               filestuff.write(str(abs(self.ADJ[i][j]))+",")
            else:
	       filestuff.write("0,")
         if (inSameCluster(self.bacteria[i], self.bacteria[self.n-1], self.clusters)):
            filestuff.write(str(self.ADJ[i][self.n-1]))
         else:
            filestuff.write("0")
         filestuff.write("\n")




