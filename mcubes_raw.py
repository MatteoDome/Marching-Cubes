import numpy as np
import tables


kx, ky, kz = np.mgrid[-10:10, -10,10,-10:10]
vertices = []

f = kx**2 + ky**2 + kz**2 - 1

# class coord(object):
# 	def __init__(self, kx, ky, kz):
# 		self.kx = kx
# 		self.ky = ky
# 		self.kz = kz

class cell(object):
	def __init__(self, kxs kys, kzs, func, i, j, k):
		self.kxs = kxs
		self.kys = kys
		self.kzs = kzs
		self.func = func
		self.ijk = i, j, k

		self.values = (self.func(kxs[i], kys[j], kyz[k]), self.func(kxs[(i+)%20], kys[j], kyz[k]),
					  self.func(kxs[(i+1)%20], kys[(j+1)%20], kyz[k]), self.func(kxs[i], kys[(j+1)%20], kyz[k]), 
					  self.func(kxs[i], kys[j], kyz[(k+1)%20]), self.func(kxs[(i+1)%20], kys[j], kyz[(k+1)%20]), 
					  self.func(kxs[(i+1)%20], kys[(j+1)%20], kyz[(k+1)%20]), self.func(kxs[i], kys[(j+1)%20], kyz[(k+1)%20]));

		self.grid = np.zeros(shape = [len(kxs)-1, len(kys)-1, len(kzs)-1, 8])
		for i, j, k in intertools.product(range(len(kxs)-1), range(length(kys)-1), range(lent(kzs))-1):
			self.grid[i, k, j, :] = self.values[:]


		##20 is a placeholder; it represents the length of one side of the grid. The indexing convention in the one found in the paper by Lorensen and Cline

def find_vertices (kx, ky, kz, isolevel):
	vertlist = np.zeros(12)

	if cell.values[0] < isolevel:
		cubeindex |= 1
	if cell.values[1] < isolevel:
		cubeindex |= 2
	if cell.values[2] < isolevel:
		cubeindex |= 4
	if cell.values[3] < isolevel:
		cubeindex |= 8
	if cell.values[4] < isolevel:
		cubeindex |= 16
	if cell.values[5] < isolevel:
		cubeindex |= 32
	if cell.values[6] < isolevel:
		cubeindex |= 64
	if cell.values[7] < isolevel:
		cubeindex |= 128

	if edgeTable[cubeindex] == 0:
		return 0

	if (edgeTable[cubeindex] & 1):
		vertlist[0] = interpolate_vertices(isolevel,grid.p[0],grid.p[1],cell.values[0],cell.values[1]);
   	if (edgeTable[cubeindex] & 2):
   		vertlist[1] = interpolate_vertices(isolevel,grid.p[1],grid.p[2],cell.values[1],cell.values[2]);
   	if (edgeTable[cubeindex] & 4):
   		vertlist[2] = interpolate_vertices(isolevel,grid.p[2],grid.p[3],cell.values[2],cell.values[3]);
   	if (edgeTable[cubeindex] & 8):
   		vertlist[3] = interpolate_vertices(isolevel,grid.p[3],grid.p[0],cell.values[3],cell.values[0]);
   	if (edgeTable[cubeindex] & 16):
   		vertlist[4] = interpolate_vertices(isolevel,grid.p[4],grid.p[5],cell.values[4],cell.values[5]);
   	if (edgeTable[cubeindex] & 32):
   		vertlist[5] = interpolate_vertices(isolevel,grid.p[5],grid.p[6],cell.values[5],cell.values[6]);
   	if (edgeTable[cubeindex] & 64):
   		vertlist[6] = interpolate_vertices(isolevel,grid.p[6],grid.p[7],cell.values[6],cell.values[7]);
   	if (edgeTable[cubeindex] & 128):
   		vertlist[7] = interpolate_vertices(isolevel,grid.p[7],grid.p[4],cell.values[7],cell.values[4]);
   	if (edgeTable[cubeindex] & 256):
   		vertlist[8] = interpolate_vertices(isolevel,grid.p[0],grid.p[4],cell.values[0],cell.values[4]);
   	if (edgeTable[cubeindex] & 512):
   		vertlist[9] = interpolate_vertices(isolevel,grid.p[1],grid.p[5],cell.values[1],cell.values[5]);
   	if (edgeTable[cubeindex] & 1024):
   		vertlist[10] = interpolate_vertices(isolevel,grid.p[2],grid.p[6],cell.values[2],cell.values[6]);
   	if (edgeTable[cubeindex] & 2048):
   		vertlist[11] = interpolate_vertices(isolevel,grid.p[3],grid.p[7],cell.values[3],cell.values[7]);

   	for i in xrange(0, triTable[cubeindex][i] != 1, 3):
   		triangles[ntriang].p[0] = vertlist[triTable[cubeindex][i]]
   		triangles[ntriang].p[1] = vertlist[triTable[cubeindex][i+1]]
   		triangles[ntriang].p[2] = vertlist[triTable[cubeindex][i+2]]
   		ntriang +=1

   	return ntriang, triangles


def interpolate_vertices(isolevel, p1, p2, value1, value2):
	if (np.absolute(isolevel - value1) < 0.001):
		return p1
	elif (np.absolute(isolevel2 - value2) < 0.001):
		return p2
	if (np.absolute(value1-value2) < 0.001):
		return p1

	m = (isolevel - value1)/(value2 - value1)
	p = p1[:] + m*(p1[:] - p2[:])

	return p