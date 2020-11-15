'''
This is your AGENT. It is technically random agent but this is yours
# PLEASE don't use any additional packages other than those provided below
'''
import time
import random
import numpy as np

class agent:
	def __init__(self, player_num, env):
		self.name = "minimax"  ###### give your bot a name ######
		self.player_num = player_num
		self.env = env


	def give_next_move(self, solid_state):
		'''
		This method is called each time the player needs to choose an 
		action
		solid_state: is a dictionary containing all the information about the board
		''' 

		#transfering a single solid_state
		
		self.board = solid_state["board"] 
		self.done = solid_state["done"]
		self.bombs = solid_state["bombs"]
		self.turn = solid_state["turn"]
		self.player = solid_state["players"][self.player_num-1]


		#############################
		###### Your Code Here #######

		import copy

		local_state = copy.deepcopy(solid_state)
		local_env = copy.deepcopy(self.env)

		def max_top(state, a, b, depth):
			print("top, depth={}".format(depth))
			if state["done"] or depth==0:
				return state["players"][0].score - state["players"][1].score, 0
			v = -np.inf
			for action in sorted(local_env.get_valid_actions(state)[0],reverse=True):
				v = max(v, min_val(state,action,a,b,depth))
				if v >= b:
					return v, action
				if v > a:
					a = v
					choice = action
			return v, choice

		def max_val(state, a, b, depth):
			if state["done"] or depth==0:
				
				print(depth)
				print("player1: {}".format(state["players"][0].score))
				print("player2: {}".format(state["players"][1].score))
				
				return state["players"][0].score - state["players"][1].score
			v = -np.inf
			for action in sorted(local_env.get_valid_actions(state)[0],reverse=True):
				v = max(v, min_val(state,action,a,b,depth))
				if v >= b:
					return v
				a = max(a, v)
			return v
		
		def min_val(state, max_act, a, b, depth):
			v = np.inf
			for action in sorted(local_env.get_valid_actions(state)[1],reverse=True):
				v = min(v, max_val(local_env.next_state(state, [max_act,action]),a,b,depth-1))
				if v <= a:
					return v
				b = min(a, v)
			return v
		
		val, action = max_top(local_state, -np.inf, np.inf, 10)
		print(val)

		#############################
		
		return action
