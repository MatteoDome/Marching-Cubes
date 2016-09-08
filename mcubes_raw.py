import numpy as np
import tables


kx, ky, kz = np.mgrid[-10:10, -10,10,-10:10]

f = kx**2 + ky**2 + kz**2 - 1

class coordinate(object):
	def __init__(self, kx, ky, kz):
		self.kx = kx
		self.ky = ky
		self.kz = kz

class cell(object):
	def __init__(self, kxs, kys, kzs, func):
		self.kxs = kxs
		self.kys = kys
		self.kzs = kzs
		self.func = func

		self.values = (self.func(kxs[i], kys[j], kyz[k]), self.func(kxs[i+1], kys[j], kyz[k]),
					  self.func(kxs[i+1], kys[j+1], kyz[k]), self.func(kxs[i], kys[j+1], kyz[k]), 
					  self.func(kxs[i], kys[j], kyz[k+1]), self.func(kxs[i+1], kys[j], kyz[k+1]), 
					  self.func(kxs[i+1], kys[j+1], kyz[k+1]), self.func(kxs[i], kys[j+1], kyz[k+1]));

def polygonize (kx, ky, kz, isolevel):
	ntriang = 0
	cubeindex = 0

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
		vertlist[0] = vertex_interp(isolevel,grid.p[0],grid.p[1],cell.values[0],cell.values[1]);
   	if (edgeTable[cubeindex] & 2):
   		vertlist[1] = vertex_interp(isolevel,grid.p[1],grid.p[2],cell.values[1],cell.values[2]);
   	if (edgeTable[cubeindex] & 4):
   		vertlist[2] = vertex_interp(isolevel,grid.p[2],grid.p[3],cell.values[2],cell.values[3]);
   	if (edgeTable[cubeindex] & 8):
   		vertlist[3] = vertex_interp(isolevel,grid.p[3],grid.p[0],cell.values[3],cell.values[0]);
   	if (edgeTable[cubeindex] & 16):
   		vertlist[4] = vertex_interp(isolevel,grid.p[4],grid.p[5],cell.values[4],cell.values[5]);
   	if (edgeTable[cubeindex] & 32):
   		vertlist[5] = vertex_interp(isolevel,grid.p[5],grid.p[6],cell.values[5],cell.values[6]);
   	if (edgeTable[cubeindex] & 64):
   		vertlist[6] = vertex_interp(isolevel,grid.p[6],grid.p[7],cell.values[6],cell.values[7]);
   	if (edgeTable[cubeindex] & 128):
   		vertlist[7] = vertex_interp(isolevel,grid.p[7],grid.p[4],cell.values[7],cell.values[4]);
   	if (edgeTable[cubeindex] & 256):
   		vertlist[8] = vertex_interp(isolevel,grid.p[0],grid.p[4],cell.values[0],cell.values[4]);
   	if (edgeTable[cubeindex] & 512):
   		vertlist[9] = vertex_interp(isolevel,grid.p[1],grid.p[5],cell.values[1],cell.values[5]);
   	if (edgeTable[cubeindex] & 1024):
   		vertlist[10] = vertex_interp(isolevel,grid.p[2],grid.p[6],cell.values[2],cell.values[6]);
   	if (edgeTable[cubeindex] & 2048):
   		vertlist[11] = vertex_interp(isolevel,grid.p[3],grid.p[7],cell.values[3],cell.values[7]);

def vertex_interp(isolevel, p1, p2, value1, value2):
	if (np.absolute(isolevel - value1) < 0.001):
		return p1
	elif (np.absolute(isolevel2 - value2) < 0.001):
		return p2
	if (np.absolute(value1-value2) < 0.001):
		return p1

	m = (isolevel - value1)/(value2 - value1)
	p = p1[:] + m*(p1[:] - p2[:])

	return p