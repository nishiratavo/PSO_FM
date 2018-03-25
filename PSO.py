import random
import math




def paraboloid_func(x):
	y = 0
	for i in range(len(x)):
		y += x[i]**2 - 2
	return y

def poly_func(x):
	y = (x[0]**3) - (2*x[0]**2) + 3 - (x[1]**2)
	return y





class Particle:
	"""docstring for Particle"""
	def __init__(self,initial_pos):
		self.actual_pos = []
		self.actual_vel = []
		self.actual_error = -1
		self.best_pos = []
		self.best_error = 0
		self.first_iteration = 1
		
		for i in range(len(initial_pos)):
			self.actual_vel.append(random.uniform(-1,1))
			self.actual_pos.append(initial_pos[i])

	def evaluate(self,cost_func):
		self.actual_error = cost_func(self.actual_pos)

		if (abs(self.actual_error) < abs(self.best_error)) or self.first_iteration == 1:
			self.first_iteration = 0
			self.best_error = self.actual_error
			self.best_pos = self.actual_pos

	def update_velocity(self,best_pos_g):
		w=0.5       #inertia
		c1=1        #individual constant
		c2=2        #group constant

		for i in range(len(initial_pos)):
			r1=random.random()
			r2=random.random()

			vel_cognitive = c1*r1*(self.best_pos[i]-self.actual_pos[i])
			vel_social = c2*r2*(best_pos_g[i]-self.actual_pos[i])
			self.actual_vel[i] = w*self.actual_vel[i] + vel_cognitive + vel_social


	def update_position(self, bounds):
		for i in range(len(initial_pos)):
			self.actual_pos[i] = self.actual_pos[i] + self.actual_vel[i]

			if self.actual_pos[i] > bounds[i][1]:
				self.actual_pos = bounds[i][1]

			if self.actual_pos[i] < bounds[i][0]:
				self.actual_pos = bounds[i][0]



class PSO():
	"""docstring for PSO"""
	def __init__(self, cost_func, initial_pos, bounds, n_particles, iterations):
		self.best_pos_g = []
		self.best_error_g = 0
		self.first_iteration = 1

		for i in range(len(initial_pos)):
			self.best_pos_g.append(0)

		swarm = []
		for i in range(n_particles):
			swarm.append(Particle(initial_pos))

		i = 0
		while i < iterations:
			for j in range(n_particles):
				swarm[j].evaluate(cost_func)

				if (abs(swarm[j].best_error) < abs(self.best_error_g)) or self.first_iteration == 1:
					self.first_iteration = 0
					self.best_error_g = swarm[j].best_error
					for k in range(len(initial_pos)):
						self.best_pos_g[k] = swarm[j].best_pos[k]


			for k in range(n_particles):
				swarm[k].update_velocity(self.best_pos_g)
				swarm[k].update_position(bounds)

			i += 1

		print(self.best_pos_g)
		print(self.best_error_g)


initial_pos = [1]
bounds = [(-15,15)]
PSO(paraboloid_func, initial_pos, bounds, 20, 600)





















		




