from .bot import Bot
from .data import *
from .functions import *
import re

class Chess(Bot):
	def add(self):
		text = self.update.get_command()
		write_file(self, text)
		command = read_file(self)
		return 	self.send_message(add_text, self.update.get_id())


	def answer(self):
		message = self.update.get_text()
		match_res = re.search(r'#?(?P<tour>\d+)\s*(?:тур)*\s*(?P<division>\w?)\s*\n*(?P<player_name>(?:\w+\s*)+)\s*-?:?\s*(?P<opponent_name>(?:\w+\s*)+)\s*\n*(?P<player_score>\d+\.?\,?\d?)-?:?\s*(?P<opponent_score>\d+\.?\,?\d?)\s*\n*(?P<links>https?:\/\/lichess\.org\/\w+\s*\n*(?:https?:\/\/lichess\.org\/\w+)*)', message)
		text = store_game(match_res)
		# if match_res == None:
		# 	return self.send_message(add_text, self.update.get_id())
		return self.send_message(text, self.update.get_id())
 
chess = Chess(token)
chess.polling()