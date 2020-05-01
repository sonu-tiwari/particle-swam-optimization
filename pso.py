import particle as P
import graph1
import sys
import argparse
import time
import random
import queue as Q

####class which is used in dijistra algorithm to evaluate optimim path to compare the result with pso

class PQEntry:
	def __init__(self,priority,value):
		self.priority=priority
		self.value=value
	def __cmp__(self,other):
		return cmp(self.priority,other.priority)


class PSO():
	def __init__(self, num_particles, maxiter,no_of_nodes,start_node,end_node,graph,maximum_path_length):
	    
	    self.swarm=[]                                                    #array of paticle

        #####P is the Particle class

	    for i in range(0,num_particles):
	        self.swarm.append(P.Particle(no_of_nodes))  

	    self.global_best_cost=-1                                        #cost of Gbest
	    self.global_best_pos={}                                         #position of Gbest
	    self.global_path=[]                                             #decoded path corresponding to Gbest

	    i=0
	    while i < maxiter:
	        
	        for j in range(0,num_particles):
	           
	            # self.swarm[j].PrintParticle()
	            path=self.decode(self.swarm[j].position_i,graph,start_node,end_node,maximum_path_length)
	            
	            if path[-1]==end_node:
	                for x in path:
	                    print(x,end=" ")
	                print("\n")
	                self.swarm[j].counter=i
	                self.swarm[j].cost =self.cost_fun(graph,path)
	                ##if present cost is samller than cost of Pbest then update Pbest
	                if self.swarm[j].cost< self.swarm[j].cost_best_i:
	                	self.swarm[j].cost_best_i=self.swarm[j].cost
	                	self.swarm[j].pos_best_i =self.swarm[j].position_i
	                	self.swarm[j].path_loc = path
	               
	                
	            else:
	            	###if path is not valid then give penalty to the particle
	                self.swarm[j].cost=sys.maxsize
	                self.give_penalty(self.swarm[j],path)
	                
	        
	        ###update the Gbest
	        for j in range(0,num_particles):
	            if self.swarm[j].cost_best_i < self.global_best_cost or self.global_best_cost == -1:
	                self.global_best_pos=self.swarm[j].pos_best_i
	                self.global_best_cost=self.swarm[j].cost_best_i  
	                self.global_path = self.swarm[j].path_loc     


	        # cycle through swarm and update velocities and position
	        for j in range(0,num_particles):
	            if i-self.swarm[j].counter>=5:
	                self.swarm[j].reinitialize(i)
	                
	            else:
	                self.swarm[j].update_velocity(self.global_best_pos)
	                self.swarm[j].update_position()

	        i+=1


    ######give penalty to a particle 
	def give_penalty(self,par,path):

	    for i in range(0,par.no_of_nodes):
	        if(i in path):
	            par.position_i[i]=-1*random.randint(1,100)
	            par.velocity_i[i]=-1*random.randint(1,100)

    ###find the cost of the path
	def cost_fun(self,graph,path):
	
		cost=0
		for i in range(len(path)-1):
			
			cost+=graph.vertices[path[i]][path[i+1]]
			
		return cost	
		

	def decode(self,position_i,g,start_node,end_node,maximum_path_length):

		# position_i is the position of particle to decode
		# g is the insatnce of graph

		path=[start_node]
		count=0

		while (start_node != end_node and count<=maximum_path_length):
			whole_cost=0
			c=sys.maxsize
			temp=start_node
            
            ###reach a node with no outgoing edge so return path
			if not g.vertices[start_node]:
				return path

			for x in g.vertices[start_node]:
				if x in path:
					continue
				cost = (g.vertices[start_node][x]) * (position_i[x])
				if cost<c:
					c=cost
					temp=x

		    #####if nodes repeat then retuen the path
			if temp in path:
			    return path

			path.append(temp)
			start_node=temp	
			whole_cost+=c	
			count = count+1

        #######if length of path exceeds a predefined value return path
		if count == maximum_path_length+1:
			print("length exceeded",end="")
			return path

		return path


# def processCmdLine():
    
#     #list of options
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--start_node", help="enter start node")
#     parser.add_argument("--dest_node", help="enter destination node")
#     parser.add_argument("--no_of_nodes", help="enter number of nodes in graph")
#     parser.add_argument("--no_of_particle", help="enter number of particle")
#     parser.add_argument("--maximum_iteration", help="enter maximum iteration")
#     parser.add_argument("--maximum_path_length", help="enter maximum path length")
#     #if none of the options are specified then throw error
#     if len(sys.argv) != 6 :
#         parser.print_help()
#         sys.exit(1)
#     args = parser.parse_args()
#     return args




def isReachable(graph, s, d):
	visited={}
	for i in range(0,graph.no_of_nodes+1):
	    visited[i]=False 
	q=Q.PriorityQueue()
	q.put((0,s))

	visited[s] = True 
	while q:

	    n=q.get()
	    if n[1]==d: 
	        return n[0]

	    for i in graph.vertices[n[1]]: 
	        if visited[i] == False: 
	            q.put((n[0]+graph.vertices[n[1]][i],i))
	            visited[i] = True
	return 9999999999999999



def Main():
	#args = processCmdLine()
	g = graph1.Graph()


    #######################################################
    ##    code when graph is given as                    ##
    ##    src,dest,edge cost                             ##
    #######################################################


	with open("advogato.txt" , "r") as f:
	    for line in f:
	        word= line.split()
	        g.add_edge(int(word[0]),int(word[1]),float(word[2]))
	    no_of_nodes = g.no_of_nodes+1
	    
	    f.close()

    ##########################################################
    ##                    end                               ##
    ##                                                      ##
    ##########################################################
	

    ##########################################################
    ##       code when graph is taken as matrix             ##
    ##                                                      ##
    ##########################################################

	# with open("wolf.csv" , "r") as f:
	#     i=0
	#     for line in f:
	#         word=line.split()
	#         p=0
	#         for x in word:
	#             if int(x)!=0:
	#                 g.add_edge(i,p,int(x))
	#             p=p+1
	#         i=i+1
	#     no_of_nodes = g.no_of_nodes+1
	#     print(no_of_nodes)
	#     f.close()
	# g.print_graph()

	##########################################################
    ##                    end                               ##
    ##                                                      ##
    ##########################################################

	num_particles = 100
	maxiter = 50
	start_node = 1
	end_node= 450
	maximum_path_length = 1000
	
	  
	start_time=time.time()
	
	pso=PSO(num_particles, maxiter,no_of_nodes,start_node,end_node,g,maximum_path_length)
	pso_time = time.time() - start_time
	

	print("OPtimum path---")
	for x in pso.global_path:
	    print(x,end=" ")
	print("\n")
	cost=pso.cost_fun(g,pso.global_path)
	print("cost=",cost)
	print("Total number of nodes is graph = ", no_of_nodes)
	print("Number of particle = ", num_particles)
	print("Number of iteration = ", maxiter)
	print("Time taken by pso in seconds ---", pso_time)

	start_time=time.time()
	print("shortest cost is =", isReachable(g,start_node,end_node))
	dijstra_time=time.time() - start_time
	print("Time taken by dijstra algo in  seconds ---",  dijstra_time)



if __name__ == '__main__':
    Main()
   