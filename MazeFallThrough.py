#objective is to find quickest path down
class Solution(object):
	maze = [ [0,0,1,0,0],
	[1,1,0,1,1],
	[0,1,0,0,1],
	[0,1,1,1,1],
	[1,0,1,0,1]]
	
	ROWS = len(maze)
	COLS = len(maze[0])
	
	def traverse(self, row, col, direction=1):#1 for right -1 for left
		pathlen = 1;
		while(col < self.COLS and col > 0):
			pathlen +=1
			if self.maze[row+1][col] > 0:
				return pathlen + self.maze[row+1][col]
			col +=direction
		#return max lenght which would never be considered in minum
		return self.ROWS*self.COLS
		
		
	def calcRow(self, row):
		for col in range(self.COLS):
			if row > 0 and self.maze[row-1][col] > 0:
				self.maze[row][col] = min(self.traverse(row, col, -1),self.traverse(row, col, 1))

		#for col in range(cols):#only traverse cells which have immediate connection to above row
		#if maze[row, col-1] > 0:
    	#		print maze#maze[row,col] = min(traverse( row, col, 1), self.traverse(row, col, -1))

a= Solution()
for row in reversed(range(a.ROWS-1)):
	a.calcRow(row)
print a.maze
	
#print maze# your code goes here
