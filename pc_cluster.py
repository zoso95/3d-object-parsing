import os 
import os.path
import random
import shutil
import numpy
import subprocess
from scipy.cluster.vq import vq, kmeans,kmeans2, whiten


INPUT = "/home/gb/demo_data/tea_small/tea.ply"

OUTPUT = "/home/gb/demo_data/tea_small/parsed/t{}.ply"

HEADER = """ply
format ascii 1.0
element vertex {}
property float x
property float y
property float z
property float nx
property float ny
property float nz
property uchar diffuse_red
property uchar diffuse_green
property uchar diffuse_blue
end_header
"""

CLUSTERS = 100



def main():
	data = read_ply(INPUT)
	white = whiten(data)
	_, labels = kmeans2(white, CLUSTERS)
	for i in xrange(CLUSTERS):
		cluster = data[labels==i]
		write_ply(cluster, OUTPUT.format(i))


def write_ply(cluster, output):
	s = HEADER.format(len(cluster))
	for d in cluster.tolist():
		s += format_line(d)
	with open(output, 'w+') as f:
		f.write(s)


def format_line(d):
	s = ' '.join([str(s) for s in d[:-3]])
	s += ' '.join([str(int(i)) for i in d[-4:]])
	s +='\n'
	return s

def read_ply(path):
	f = open(path)
	header = True
	data = []
	for line in f:
		if "end_header" in line:
			header = False
			continue
		if header:
			continue
		#print(line)
		d = [float(s) for s in line.rstrip().split(' ')]
		data.append(d)
	return numpy.array(data)


if __name__ == "__main__":
    main()
