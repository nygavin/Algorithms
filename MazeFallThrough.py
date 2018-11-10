#objective is to find quickest path down
class Solution(object):
	count = 0
	maze = [[0, 1, 1, 0, 0],
			[1, 1, 0, 1, 1],
			[0, 1, 0, 0, 1],
			[0, 1, 1, 1, 1],
			[1, 0, 1, 0, 1]]
	
	ROWS = len(maze)
	COLS = len(maze[0])
	
	def traverse(self, row, col, direction=1):#1 for right -1 for left
		pathlen = 1;
		while(col < self.COLS and col >= 0):

			if self.maze[row+1][col] > 0:
				return pathlen + self.maze[row+1][col]
			col +=direction
			self.count += 1
			pathlen +=1
			
		#return max lenght which would never be considered in minum
		return self.ROWS*self.COLS
		
		
	def calcRow(self, row):
		for col in range(self.COLS):
			self.count +=1
			if row > 0 and self.maze[row][col] > 0 and  self.maze[row-1][col] > 0\
				or row ==0 and  self.maze[row][col] > 0:
				self.maze[row][col] = min(self.traverse(row, col, -1), self.traverse(row, col, 1))
		#once traversed we clean
		self.maze[row] = [val if val>1 else 0 for val in self.maze[row]  ]
		
a= Solution()
for row in reversed(range(a.ROWS-1)):
	a.calcRow(row)

print a.maze
print "Iterations: " + str(a.count)
print "Min Path Is: " + str(min([val for val in a.maze[0] if val>0 ]))
