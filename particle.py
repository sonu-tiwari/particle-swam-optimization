
import random
import sys
class Particle:
	

	def __init__(self,no_of_nodes):
		self.no_of_nodes = no_of_nodes       # no of nodes
		self.cost_best_i = sys.maxsize         # cost of Pbest
		self.cost = sys.maxsize           # cost individual
		self.position_i = {}              # particle position
		self.velocity_i = {}              # particle velocity
		self.pos_best_i = {}              # position of Pbest
		self.path_loc = []                # Decoded path of Pbest
		self.counter = 0

		for i in range(no_of_nodes):
			self.position_i[i] = random.randint(1,10000)
			self.velocity_i[i] = random.randint(1,10000)
			self.pos_best_i[i] = self.position_i[i];

    #######################################################################
    ##  Function to update the velocity of the particle by given formula ##
    ##  vid = *vid + j1*rnd()*(pid-xid) + j2*rnd()*(pgd-xid);            ##
    #######################################################################



	def update_velocity(self,pos_best_g):
		w  = 0.5       # constant inertia weight (how much to weigh the previous velocity)
		c1 = 2        # cognative constant
		c2 = 2        # social constant

		for i in range(0,self.no_of_nodes):
			r1 = random.random()
			r2 = random.random()
			
			vel_cognitive = c1*r1*(self.pos_best_i[i]-self.position_i[i])
			vel_social = c2*r2*(pos_best_g[i]-self.position_i[i])
			self.velocity_i[i] = w*self.velocity_i[i]+vel_cognitive+vel_social

    #####################################################################
    ## Function to update the position of the particle by given formula ##
    ## xid = xid + vid;                                                ##
    #####################################################################

	def update_position(self):
		for i in range(0,self.no_of_nodes):
			self.position_i[i]=self.position_i[i]+self.velocity_i[i]

    #reinitialize the particle position and velocity
	def reinitialize(self,j):
		for i in range(self.no_of_nodes):
			self.position_i[i] = random.randint(1,10000)
			self.velocity_i[i] = random.randint(1,10000)
		self.counter = j

	def PrintParticle(self):
		for i in range (self.no_of_nodes):
			print(self.position_i[i],end = " ")
		print(" ")

	